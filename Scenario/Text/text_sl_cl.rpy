label alt_day4_sl_cl_begin:
    scene
    $ renpy.show("bg int_aidpost_day", what = Dawn("bg int_aidpost_day"))
    with dissolve
    play music music_list["timid_girl"] fadein 3
    play ambience ambience_medstation_inside_day fadein 3
    if herc:
        "Former athlete, former musician, soldier, security guard and sales manager, and now pioneer Syoma Sychev was lying down in the infirmary."
    else:
        "A hereditary slacker and a specimen of God's talentless waste, Semyon Semyonovich Persunov, whose greatest achievement was a repaired antenna, was now lying down in the infirmary."
    "After a skirmish with the dreaded enemy, the slippery roof."
    "Yeah, the word «lucky» definitely doesn't describe me."
    with fade2
    $ set_mode_nvl()
    "It's just as it is: instead of quietly cuddling the cuddly pussy in the blue sundress, the idiot went to help two similar idiots with a fear of heights."
    "Slavya, by the way, was just as agoraphobic, so she wasn't even considered for the job."
    "Or acrophobic?"
    "If only knowing the exact term would somehow help me deal with the results of my nobility."
    "Results? Um..."
    "How would it be without swearing?{w} Oh right."
    "Slipped, fell, woke up - Viola."
    "No, thank goodness, no casts."
    "All in all, fell on a solid bone. {w}If it had needed a cast, the story would have been a lot sadder."
    nvl clear
    "Alright, what are we talking about?"
    "Yeah.{w} So the vision test plate."
    "There was a special name for it, but I can't remember, for the life of me."
    "And the nurse certainly has a sense of humor."
    "From the way she shuffled the letters, it was not only pretty good, but also remarkably dark."
    "A drawing of some freak skeleton in the corner, no doubt stolen from a sneaking UFO."
    "And a computer of unknown model on the table."
    "To the word, behind which Violetta Cernovna was now tinkering with nothing but the… «Ksonix»!"
    "Pardonnez-moi, I read it in Ukrainian again. {w}Xonix, of course!"
    "An arcade classic of all time, the brainless painted-out field that has migrated virtually unchanged from the pioneer 'knives'."
    nvl clear
    "My mother, that's our man!"
    "Okay, graphics are on EGA level, but that's not what's important!"
    $ set_mode_adv()
    "She looked away from painting a field with an ASCII-style image of a naked maiden and turned in my direction."
    show cs normal with dissolve
    cs "Arisen... Pioneer?"
    "She nodded somewhere in my lap area, and I followed her gaze."
    "Yeah. Arisen."
    me "Woke up."
    show cs smile with dspr
    cs "That too. {w} How do you feel?"
    "I tried to shake my head cheerfully, and very vainly did so."
    me "I won't drink that much ever again."
    cs "You all say that."
    show cs grin with dspr
    pause(.3)
    show cs smile with dspr
    "She grinned."
    "The back of my head ached, and my fingers jerked away, coming across a bandage soaked in some damp abomination."
    me "What happened to me?"
    cs "Not much. {w} Minor concussion of the interstitial ganglion, you'll be running by tonight."
    me "If everything is so rosy, why am I here?"
    "Viola shrugged her shoulders."
    cs "They told me to... treat you. {w}Will you let me?"
    me "Thank you, but no."
    "Unyieldingly, I replied."
    me "I think I'll pass for now."
    show cs grin with dspr
    pause(.3)
    show cs smile with dspr
    cs "Then I don't know anything."
    cs "You don't embarrass me, you don't ask me to eat.{w} By the way, how about eating?"
    "She pointed to the pots, which appeared to contain provisions for the sick man."
    "I was a little nauseous and didn't want to eat. {w}But when I refused free food!"
    "Even though I have no appetite because of the concussion of the cranial nerve knot."
    with fade
    "I nodded and gratefully accepted the breakfast."
    cs "Before breakfast - drink this:"
    "She held out to me a wrapped up piece of transparent paper with some kind of powder rustling in it."
    "Intercepting my gaze, she nodded."
    cs "Otherwise I won't let you out of the infirmary."
    "Watching me carefully as I drank my medicine - I couldn't get away from the impression that I was a volunteer test group for some new medicine - Viola smiled."
    cs "Now chew. {w}And while you're chewing, listen to this:"
    cs "There are freeloaders walking around the camp and looking in every corner. {w} See, if anyone happens to look in here, pretend I bandaged you in training."
    me "Excuse me?"
    show cs normal with dspr
    cs "Not my words.{w} It was the director who checked in."
    me "Ah..."
    cs "Yeah, yeah, some kind of commission."
    cs "Sounds to me like a bunch of freeloaders who had a bad time coinciding with vacations."
    "The nurse got up, went over to the medicine cabinet and jumped up and removed some rectangular object from the top."
    "Blow, spit, wiped the cuffs - instantly stained gray."
    "And she hung the object right on top of the vision test table."
    "The object turned out to be everyone's favorite, unforgettable comrade with round glasses and incomprehensible accomplishments."
    "Comrade Genda, in short."
    "There was even a saying of some sort, in gold on a mournful background, but I didn't look closely."
    cs "Who knows.{w} Maybe they'll ask why I don't have a portrait of General Secretary in here.{w} And I do.{w} You seeing this?"
    $ renpy.show("genda_portrait", what = Dawn("genda_portrait"))
    with flash
    "Let there be Genda!"
    "True, a little fly-covered and a little dusty, but nobody cares, do they?"
    "Most importantly, you can see the round glasses, the fancy white gloves, and the Leninist beard framing the sarcastic smirk."
    show cs smile with dspr
    cs "You chew, chew, fatten your sides.{w} It's disgraceful when you weigh less than the girl you're dating."
    me "Oh. {w}Am I dating someone?"
    "I asked politely."
    cs "No, of course.{w} You're on your own."
    cs "And the pioneer girl who carried you on her back did so out of great friendship, not waiting for a stretcher or at least Boris... Boris Alexandrovich. {w} She's on her own, too."
    me "..."
    cs "Especially on her own, the one with the complexes, who kept trying to wash your shirt, until she was first affected by the oral method."
    me "Oral?"
    show cs shy with dspr
    cs "Well..."
    "Viola stroked the edges of her lips with her index and middle fingers."
    me "Yeah. {w}I figured as much."
    "I would have reacted, honestly! I'd probably even blush."
    "But not like that."
    show cs normal with dspr
    cs "You're boring."
    "Cernovna sighed."
    cs "Get out of here outside, fresh air is good for a growing body."
    "Nodding to her, I hastened to do just that."
    play sound sfx_open_door_1
    scene bg ext_aidpost_sunset_7dl with dissolve
    play ambience ambience_camp_center_day fadein 3
    "I had just finished my breakfast by this point, so I gladly complied with her demand."
    "And, feeling like a grandmother in a handkerchief, I settled down on a bench next to the infirmary."
    "Our medicine, they say, is both dangerous and difficult."
    scene bg ext_square_sunset with dissolve
    "I got bored just sitting there, so I first stretched out my legs on the bench and then spread out on the sun-warmed planks, propped my cheeks on my palms, and began to study the flickering camp life thoughtfully."
    "The infirmary, despite the fact that it was practically in the geographical center of the camp, was so sensibly fenced off by greenery and folds of terrain that it hid as if in a 'pocket' where the pounding activity of back-bending pioneers almost did not reach."
    "Everyone was running, trembling, and afraid of the commission."
    "What the hell was that commission - wasn't clear."
    "None of my business."
    "I switched to contemplative mode and very soon stopped feeling bored."
    "Life really was hitting a key, now and then a wrench, and the spectacle of someone dragging something somewhere was almost never boring."
    "The camp looked great - the pioneers of every troop had successfully cleaned all the paths, picked up all the trash, and painted the grass green."
    scene bg ext_square_day with dissolve2
    "The day was spreading, the sun was rolling toward the zenith, and, as if charged by photocells, the pioneers scurrying back and forth accelerated and accelerated."
    "It felt as if it was possible to make perfect order at the last moment, since no one had succeeded in doing so in the previous few days."
    "Weren't they all told yesterday that an inspection was coming to visit?"
    "Or?"
    "In fact, there was something stirring about the idea of conveying such information to subordinates strictly under the curtain. {w}Refreshing."
    "From my vantage point I could see a small piece of the square with Genda fixing his glasses, Olga Dmitrievna's rostrum, the web of paths leading to the residential buildings, the brick cube of the administration building visible at the edge of my vision."
    "If we continue in our chosen direction, the path will lead to the centers of our culture and science: respectively, the Miku's abode and the clubs."
    scene bg ext_square_day:
        zoom 1.1 xalign .5 yalign .5
        linear 2.0 xalign .2 yalign .5
    "The layout is thoughtful, everything is serious."
    "The standard for the required number of square meters per hypothetical nose is met exactly."
    "So that no one would feel cramped."
    scene bg ext_square_day:
        zoom 1.1 xalign .2 yalign .5
        linear 2.0 xalign .8 yalign .5
    "It must have been great to come here with everyone else on the first day of check-in - of which shift was it? The second one? Yeah.{w} Together with everyone else, to get acquainted, to check in."
    "Then maybe they wouldn't put me in with a counselor - although I don't mind, not at all! - but with some Electronik or some pioneers from the second or third squad."
    "And they would have put a picture of me in one of the photo albums yesterday, too!"
    "By now everyone would have made friends, I would have found myself a steady circle of acquaintances and fellowship - dark corners and books.{w} In short, everything as I used to."
    scene bg ext_square_day with dissolve
    "There's nothing good about coming here with everyone else.{w} That way I look exotic and fresh, I'm popular, and they don't grind their teeth at me with «annoyance, get off»."
    with fade
    "Some chunky pioneer was dragging some gray cube object somewhere, stopping momentarily and correcting his slipping hands."
    "He would have grabbed his oversized cargo more comfortably, but there was a coil of gray braided cord dangling from his right arm."
    th "Uh... Internet guy found the local equivalent of free wi-fi?"
    with fade
    th "Alright... No more drinks for Semyon."
    "Somewhere in the distance, at the edge of earshot, a police GAZ roared its engine and drove off into the blue realm of the local great Soviets, cardboard sausages, and unification in everything, including clothing style."
    with fade2
    "Contemplation quickly bored me, and I got up, shaking off the paint scales and pine needles stuck to my shirt."
    "My head wasn't giving me any reason to worry, so I decided to take a sort of promenade around the infirmary, stretch my legs a little."
    "There wasn't much else to do anyway, and I didn't want to fight Viola for the right to cut into Xonix."
    "Not yet, anyway."
    scene bg ext_aidpost_day
    with dissolve
    th "It's not like I'm leaving the medical facility."
    th "And anyway, I'm on vigilant duty, despite my battle wound. The inspectors should be proud of me."
    with fade
    th "Well, I've got to at least do something!"
    th "Maybe play partisan and crawl to the library?"
    "It might work, in principle."
    "I'd have to get dangerously close to the main road to do that, though, and that's fraught."
    scene bg ext_aidpost_day:
        xalign .5 yalign .5 zoom 1.4
        ease .8 zoom 1.0
    stop music fadeout 3
    "It's amazing how sad it is without the Internet!"
    "I mean, the last three days I've been distracted by all sorts of interesting acquaintances, events and so on. And now that's it!"
    "Come on, at least give me a calculator, let me press some buttons!"
    "Or distract me with something else."
    play music music_list["smooth_machine"] fadein 3
    "I'll even settle for an interesting book."
    "But I don't think Viola has anything that would interest me. {w}I suspect she has a vinaigrette of medical encyclopedias and women's romance novels."
    th "But I can't just chase her into the library! She'll refuse it herself and scold me, and she's right to do so."
    "Also... I could lurk in the bushes, then jump out and take a hostage!"
    "And, threatening his life and health - ahem, with what? - for example, with this bandage, reeking of Vichniovsky's ointment, make him get into a car and drive at top speed 'to the mainland' - to the nearest district center."
    "Which is rumored to be about three hundred kilometers away, or two and a half hours of not-so-cheerful driving."
    th "Oh, I'm going to be famous! {w}On TV, in newspapers... {w}Speaking of the media!"
    th "I risked my occipital bone yesterday for the freedom of the local radio station!"
    th "Why can't I hear them on the active air?"
    "There was the usual summer silence over the camp, undisturbed by anything but the occasional song of grasshoppers and scraps of conversation - nervous, restless."
    "So there was no musical accompaniment to this morning.{w} Which means that my sacrifice was wasted."
    "Sad."
    "And the potential hostages aren't coming."
    "What about them? What haven't I seen in the district center?"
    "Compared to the mess going on there, «Sovyonok», in any case, represents the center of order and tranquility."
    "Besides, who needs me there?"
    "Let's not rush into an early end to an unanticipated vacation, since I'm not required to have any papers or money here, especially since there's not much time left."
    "Having accomplished my marathon feat around the infirmary, I flopped back onto the bench, my eyes covered with the palm of my hand against the sun."
    "It wasn't evening, but the number of classes was heading toward zero."
    "Except for the clouds to chase with his gaze - that one looks like Moomin-Troll, and that one... Looks like Syroezhkin in an apron!"
    "Her heels clattered on the concrete, and she sailed into my abode of sleepy, idle drowsiness, smiled, stroked her cheek, and sat down beside me."
    show sl smile pioneer close with dissolve
    me "Hello, sunshine!"
    "I replied."
    sl "Hello. How are you?"
    me "Q."
    sl "What does that mean?"
    me "It means I'm brain damaged and out of my mind."
    show sl laugh pioneer close with dspr
    "Slavya laughed."
    "She was especially good today.{w} Almost like yesterday, only even better today."
    "She was especially good every day, though - an enchanting beast."
    "Yesterday's remorse at the river was successfully defeated by a refreshing kick to the head."
    "And communicating with Slavya was easy now - I had resigned myself to the fact that this level was just out of my league, and that meant friendship at best."
    "Her gaze said «you're my hero» and «give me an autograph»."
    dreamgirl "Wasn't it something like «sign on my chest»?"
    th "Mm-hmm.{w} Good morning, I take it?"
    dreamgirl "Evil morning.{w} Remember when you fell over yesterday? That was quite a flight!"
    dreamgirl "Now she owes you at least a kiss."
    th "Owes?"
    if alt_day3_lp_route == 2:
        dreamgirl "In case you've forgotten, she's the one who sent you to fiddle with the antenna without listening to objections."
        me "Really?"
        sl "What?"
        me "I wanted to dance with you yesterday, but you sent me to help the cyberneticists. {w} Yeah?"
        show sl shy pioneer close with dspr
        "Slavya shook her shoulder in embarrassment."
        sl "Yes. That was silly."
        "Hearing «that was silly» from the buttoned-down pioneer girl-thingy was as wild as this morning with our kindest nurse spitting in Genda's face."
    else:
        "I have no idea what my inner voice is ranting about, but personally, I don't remember anyone owing me anything."
        "After all, I'm the fool, I volunteered, I'm to blame."
    show sl normal pioneer close with dspr
    me "Intelligence reports that you dragged me from the battlefield on your own hump?"
    sl "Lena helped me."
    "Weakly smiled the girl."
    me "Practically like a nurse on the battlefield."
    me "Hospital nurse, my sad love... Do you know that song?"
    show sl smile2 pioneer close with dspr
    "Slavya nodded."
    sl "By the way, I really wanted to go into medicine.{w} And then become a veterinarian."
    me "And now?"
    if (alt_day2_walk == 2) and not herc:
        sl "Well, as you said..."
        "The girl's fingers were rubbing her braid, machine-like."
        sl "Rescuer..."
    else:
        sl "Local history, maybe.{w} Or ecology."
    sl "I want to help at a level where my help will be needed.{w} Not to cure the individual animal, but to make sure it has nothing to get sick with."
    show sl normal pioneer close with dspr
    if herc:
        dreamgirl "Wow.{w} We'll have another Nobel Prize winner for ecology."
        th "Why not? If Misha got his - you know why - let this girl be valued too."
    sl "It'll be hard, but I'll try. I think it's my thing, it's the power point."
    show sl smile pioneer close  with dspr
    "Said a very nice, very beautiful future Nobel Prize winner in ecology, who has not yet shown herself in any way in ecology."
    "And it's okay, as long as there are putschists, as long as there are elections and re-elections and political filth, the girl will be involved in nature and its health, such a beautiful and talented kitty with huge blue eyes."
    "I wish she could get tears in those eyes just from happiness. {w} But, man, not with my luck to do it."
    "And anyway, what am I into all this romance all of a sudden? I've got nothing better to do than ponder the fate of a girl who's a complete stranger to me. Like she'd want to talk to me, if anything."
    "What?"
    "What anything in «if anything»?"
    show prologue_dream with flash
    "Well, for example, Petersburg, going up from 'Lomonosovskaya', me from the bottom to the city, her from the city to the subway."
    "We crossed paths, we parted ways."
    "The next day we met in the lobby, or I held the door for her, letting her out into the city, slowed down the minibus - my mother has learned me these small gentlemanly gestures, I do them, no longer thinking."
    "What's next? {w}Quiet «merci», smile, and not even dignifying with a glance."
    "Who invented this damn romance to drive me crazy, who then walks around for three weeks looking for a familiar look in the crowd?"
    th "What did I do to deserve this?"
    show sl serious pioneer close with dspr
    sl "You're kind of alienated."
    "That's right.{w} I'm alienated, I'm alienated from your unseens, take it and carry it away, leave me my swamp."
    me "That's alright. I'll soon be whimsical back."
    "Slavya smiled."
    show sl smile pioneer close with dspr
    sl "Still, you're the most unusual pioneer I've ever met."
    me "No, I'm quite usual."
    show sl normal pioneer close with dspr
    "Just not a pioneer."
    hide prologue_dream with fade2
    sl "I won't tell you stupid things about how every person is unique, can I?"
    show sl normal pioneer with dspr
    "She stood up, leaving me to stare at her back."
    "And a white, see-through shirt that hugged tightly around her back."
    "An even band across the entire surface, giving away the owner's complete lack of a bra."
    th "That's how I missed the best part."
    show sl normal pioneer far with dissolve
    sl "I just feel something in you, just waiting to be dragged out."
    me "And thrown on the fan?"
    "I asked politely."
    sl "What?"
    "I knew I was saying unnecessary and empty things again."
    me "You see, Slavya, you're very biased.{w} You've been babysitting me for four days now, and even yesterday..."
    me "Anyway, get it out of your head and don't look for anything good in me. Let's look for something in you."
    sl "Like what?"
    me "I don't know. Oil?"
    show sl smile pioneer with dissolve
    "Slavya smiled politely."
    me "If you simplify things to the extreme, you get a boring man who's forced to play by rules he's not very used to."
    me "Why, it's not very clear.{w} You probably should get him."
    show el normal pioneer far at left with moveinleft
    "I pointed to Syroezhkin, rushing about his business, looking extremely businesslike."
    "He mumbled something to himself, waving his right hand, and looked wild and disheveled."
    "All that was missing was half a bald head and glasses of the caliber of «phantasmal dioptres» to create a full-fledged image of the mad scientist."
    "Although Shurik would look much more confident in this role."
    hide el with easeoutleft
    sl "Electronik is funny, but very keen."
    sl "When we first moved here, and he and Sasha hadn't become friends, he was going from extreme to extreme, borrowing all kinds of books from the library, constantly looking and looking for something, trying to learn."
    me "You mean he was in the library day and night?"
    sl "Yes."
    "Slavya laughed."
    sl "Until Sasha took him to his club.{w} He used his talents."
    "The day was pushed to the back of my imagination."
    scene black
    show mz normal glasses pioneer
    show prologue_dream
    with fade
    "Sacred simplicity.{w} To think that a man infuriates a librarian with his presence simply because he has nothing better to do."
    show el sad pioneer behind mz
    pause(.8)
    show el smile pioneer behind mz with flash
    "Brrr!"
    "I had a slightly different version of this behavior of Syroezhkin, but all comes in good time."
    show mz rage pioneer with dspr
    pause(1)
    show el upset pioneer behind mz
    with dissolve
    "It's a little off topic to discuss with a girl.{w} Especially with such a beautiful girl!"
    scene bg ext_aidpost_day
    show sl shy pioneer
    with dissolve
    sl "Although sometimes I don't think it's about interests."
    "Slavya blushed a little."
    "Well, yes, and I didn't have to say anything."
    me "We can't know for sure."
    "I came to her rescue."
    show sl normal pioneer with dspr
    sl "Yes."
    "I hummed."
    "That's the atmosphere here - patriarchal, calm, judgmentless.{w} Random himself told me to find a subject for sighing - and, in fact, to sigh."
    me "What about you?"
    sl "Me? What do you mean?"
    show sl surprise pioneer with dspr
    "In terms of admirers, of course, silly girl."
    "There are, understandably, only three guys in the first squad, of whom I am sexless, Electronik has a crush on the librarian, and Shurik seems to be married to his hobby. {w} Both cybernetics and the wall newspaper."
    me "Did you find your place in camp fast?"
    show sl smile pioneer with dspr
    sl "Yes."
    "She smiled serenely."
    sl "It's not the first time I've been here, so Olga Dmitrievna knows me, she put me straight to the point."
    me "And the boys?"
    with flash_pink
    "I asked before I knew what I was even doing."
    "I guess I'm not so sexless."
    sl "What?"
    show sl tender pioneer with dspr
    "Asked Slavya.{w} Her ears flashed."
    me "Did you meet anyone interesting?"
    sl "Oh... You know, it's such a subject...{w} Personal.{w} You know?"
    me "What a delicate form of wishful thinking."
    "I delighted."
    show sl shy2 pioneer with dspr
    sl "I'm sorry.{w} But I think it's too early for me to think about such things."
    "She was still red.{w} Apparently, she doesn't have to talk about these things very often."
    "Especially with members of the opposite sex."
    "Potential candidates."
    "Even if their full potential fits between zero and one hundredth."
    sl "I have to study first, and..."
    "O. What great talk."
    "Blue-stockish."
    "Giving out not only the owner of said «stocking» in the owner, but also a person who has never really been in love."
    "It doesn't give me any advantage by any means, just some things fall into place."
    "In particular, her perfectionism."
    "Pure sublimation."
    me "You don't have to tell me all those things.{w} I got the hint from the first time - don't get your dirty hands where they're not asked."
    show sl normal pioneer with dspr
    sl "You're too mean to yourself."
    "Slavya sighed."
    "The reluctance to directly forbid me to discuss such topics says something, too."
    stop music fadeout 3
    play sound sfx_7dl["eat_horn"] fadein 1
    "The camp bounced over the camp with the joyous eighths, urging the pioneers to hurry to fill their stomachs."
    "And to the High Inspection, on the other hand, hinting that it was time to surrender their credentials and vacate the territory."
    "The sleepy calm of the morning was instantly shattered, the unkind tension of waiting for you to make a mistake and thereby expose your friends and comrades to the faces of the evaluating officers."
    "I don't know about the others, but that's the feeling I had whenever I got caught up in any kind of test or exam."
    "Slavya went up."
    sl "Not busy this afternoon?"
    "She asked."
    "I shrugged."
    me "Why?"
    sl "It's the kids' bath day from six o'clock."
    me "I don't see the connection."
    show sl smile2 pioneer with dspr
    sl "I need to get them ready for a change of clothes and bedding.{w} Would you keep me company at the warehouse?"
    me "May I?"
    show cs normal far at left with dissolve
    cs "You may."
    "Violetta called back from the porch, locking the infirmary."
    cs "Knowing her, I'm sure she won't burden you."
    cs "Shall we go, pioneer girl?"
    "She shook the pots."
    "Slavya nodded."
    sl "Wait here for me!"
    "She instructed me in an almost commanding tone."
    hide sl
    hide cs
    with flash
    "They left, leaving me alone."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_sl_cl_shurik:
    scene bg ext_aidpost_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    "That's how it goes."
    "They don't forget about you, no.{w} They don't sideline you."
    "They just periodically show you how defective you are now, that you can't even go to the canteen because you're overworked and all.{w} Work and glory to heroes, yeah."
    "To the parody pilots."
    "It's a worldly thing, nobody owes anybody anything, despite the carefully planted human values."
    "Maybe in two hundred years, if we're lucky, humanity will grow up to Efremov's or Bulychev's communism, where characters like Dara the Wind and Alisa Selezneva are possible."
    "But not now.{w} And not here."
    "And yet even the local communism under construction looks good compared to the ugliness I got here from."
    "Though it doesn't feel like the warm-orange romance of the country where I went to kindergarten and graduated in another country."
    scene bg ext_square_day with dissolve
    "On the square a huge mantle flag with a sickle and hammer symbol had already been untied, and a triangular flag with the colors of the squadron on duty was promptly tied in its place."
    "The platz, swept with crowbars, was swiftly settled by the dust, and the tense stiffness disappeared from the posture."
    "That's it. The higher-ups barked and departed."
    "This isn't the IRS or socials, where the higher-ups from the capital are buzzing around on a booked ship for a week and banally paralyzing the unit's work."
    "Here it's fast, angry, and completely gehsheft-free."
    "Now it was up to the evening to relax - of course, trying to remember - that not all the adults had left. {w}Some of them wouldn't be kicked out until after dinner."
    "We had to live."

    th "I wonder what our cyberneticists are doing now?"
    th "If it wasn't for their request, I'd be running around with everyone else right now, pretending to be very active."
    th "And okay, there might have been an impression about Syroezhkin - the guy is obviously a coward."
    th "But I didn't expect that from our cybernetic genius."
    th "And why, one might ask, haven't the two of them visited the sick man yet?"
    th "And that's why! They don't give a damn about a comrade who, through their fault, has further mangled an already long-abandoned brain! I bet they ran right after breakfast to fix their robot with new parts."
    dreamgirl "I wouldn't be surprised if it were true..."
    $ set_mode_nvl()
    dreamgirl "Rumor has it that this is not the first time a robot has been assembled here."
    "And, by the way, under the direction of the same Shurik."
    "And when it came to developing the control mechanism, our genius of the hammer and soldering iron developed a curious mechanism that, by all appearances, would pass every Turing test in the world without a problem."
    "In Russian, it translates as: from wires, screws and such and such, our genius has assembled a working prototype of artificial intelligence."
    "Not Altron and the Geths, of course, but still, a self-sufficient and equilibrium system."
    nvl clear
    dreamgirl "Though the vain minds have sneered, saying, 'He built himself a robot girl for the pleasures of the flesh and soul'."
    "They should have seen the robot!"
    "True, this prototype, when mounted on an experimental chassis - that robot - successfully made manipulators."
    "That's probably the right thing to say, isn't it? {w}If legs make the man, manipulators make the robot?"
    "The prototype didn't run for very long, but it was a lot of fun, and we had to catch it in some quiet backwater."
    nvl clear
    dreamgirl "There the ill-fated skink learned firsthand that water and electronics are incompatible as part of an environmental study."
    "The high foreheads of the party came, the robot was confiscated, Shurik was forced to sign a nondisclosure agreement."
    "But the luminary got the reins, of course, he went to work on it.{w} And, of course, it didn't work."
    "It didn't even work."
    "Oh, I wish I'd known him before. I'd have shared with him the wisdom of a world many years older.{w} Wisdom simple in its banality, programmer's wisdom."
    nvl clear
    dreamgirl "If it works, don't touch it! {w} Don't fix what's not broken."
    "That's what it sounds like."
    "An unambiguous instruction that even if you suddenly don't know why it's WORKING - make a brick face and enjoy the dithyrambs."
    "Now, of course, he is unlikely to be able to reproduce the starting conditions in which he made his robot, too many 'upgrades' have been made to the starting concept."
    "And like all geniuses, Shurik was squeamish about making records."
    nvl clear
    dreamgirl "So a new working theory crystallized in his head, the third one in a row."
    "According to which the bloody KGBsts had placed a brain-liquefying device somewhere in the club, so that no more funny mishaps like this would occur."
    "Although it seems a bit wasteful, the secret service never threw away any bright heads, take Perelman for instance."
    $ set_mode_adv()
    "The story I'd just been told didn't fit in my head."
    th "That's just fiction."
    "I don't know if the inner voice made it up, or if it really happened..."
    th "Anyway, all the more or less sophisticated technology is here, and if I ever need anything from here - which is doubtful given the local level of technology - I can find it here."
    dreamgirl "Like a phone charger?"
    "Innocently inquired the subconscious."

    sh "Hello."
    "Someone stepped into the sun, and I, squinting, raised my head."
    show sh normal pioneer at cleft
    with dissolve
    "The voice is familiar."
    "No kidding, it was that voice that sent me into an uncontrollable dive toward the ground yesterday."
    sh "How are you?"
    th "What's the saying? Speak of the devil..."
    me "I'd tell you."
    sh "Well, I'm sorry about that."
    me "Can you at least tell me why the hell the radio doesn't work?"
    show sh upset pioneer with dspr
    sh "You see, there's... There's a problem."
    me "Oh, you betcha."
    show sh normal pioneer with dspr
    "He looked depressed, and it wasn't about today's commission at all.{w} There was something else."
    me "So what is it?"
    sh "You see..."
    show sh upset pioneer with dspr
    "He fixed his glasses with Genda's trademark gesture, which looked pathetic and inappropriate in his performance."
    sh "I can't go in there."
    me "Let me guess, your religion forbids it?"
    sh "No!"
    show sh serious pioneer with dspr
    "He grimaced."
    sh "When I try to go into the clubs, I feel a strange sensation in my whole body, like I've done something really bad."
    me "Great. A leak of laughing gas?"
    sh "Gas?{w} But Electronik goes in there easy and doesn't feel anything."
    me "So he's immune. That can happen."
    me "Did you look for the source?"
    sh "He looked.{w} I don't even know where to go now."
    me "Why aren't you coming to lunch?"
    show sh upset pioneer with dspr
    "Shurik got embarrassed."
    sh "I just tried to go in again."
    me "Yeah, and?"
    sh "It occurred to me, too, that it might be the gas, so I tried not to breathe."
    sh "Nauseated after a minute."
    "He did look greenish."
    sh "Now I can't think about food."
    me "Okay, stop.{w} Were you okay yesterday?"
    sh "Yeah. {w}We were just finishing up a project yesterday."
    me "And then I climbed up on the roof and put the power back on your equipment."
    "The concept of a sci-fi synthesizer, producing a special anti-Shurik gas the whole time it's plugged in, popped into my head."
    dreamgirl "Maybe it's not the gas, but the vibration? {w}It's too high or too low to be heard."
    th "Are you hinting at an infrasound curtain?"
    "I remembered getting hit by one once.{w}The impressions... {w}Rocking."
    dreamgirl "Sort of."
    dreamgirl "Maybe there's a scarecrow-deratizer so rodents don't chew on the wiring."
    th "It's unlikely a human would feel it the way Shurik describes.{w} Not the same frequencies, not the same power."
    dreamgirl "Maybe.{w} But what if that very scarecrow had broken down and was now phoning in just the right range?"
    th "Well... It's worth checking out."
    stop music fadeout 3
    menu:
        "Let's go look at it" if herc:
            me "I want to see it too."
            "I went up."
            show sh surprise pioneer with dspr
            sh "What about...?"
            me "Nothing, lunch can wait. Let's go!"
            me "Don't put off the good deed."
            $ karma += 10
            $ alt_sp += 2
        "Let's run and see while we have time":
            me "I don't have a lot of time before Slavya comes back, so keep up with me!"
            $ alt_sp += 1
            $ lp_sl -= 1
            me "Just don't tell anyone!"
        "Actually, Slavya forbade me to…":
            $ lp_sl += 1
            $ alt_sp -= 1
            me "So I can't."
            show sh upset pioneer with dspr
            sh "I see."
            sh "Well, can you at least just stand there so we can compare impressions?"
            me "Sorry, no."
            $ alt_day4_sl_cl_tut_iz = True
            return
        "I hope those slackers have already left" if loki:
            "I was very curious about what happened there at Shurik's."
            "And then there's this interesting thing."
            "I was dreaming of using it against my enemies."
            $ karma -= 10
            $ alt_sp += 2
            me "Let's go take a look."
            show sh surprise pioneer with dspr
            sh "Are you sure?"
            "What an idiotic question."
            me "Let's go, I say."
    play music music_7dl["tilltheend"] fadein 3
    $ persistent.sprite_time = "day"
    $ day_time()
    scene bg ext_clubs_day
    show sh normal pioneer with dspr
    with flash
    play ambience ambience_camp_center_day fadein 5
    sh "This is the limit of being relatively well."
    "We were standing on the porch."
    sh "One more step - and I'm getting really sick."
    sh "How about you?"
    "I shrugged."
    "No, some disturbing, {i}dark{/i} presence was felt."
    "But it didn't cause any perceptible discomfort."
    me "Wait here."
    "I ordered."
    "And opened the door."
    with fade
    play sound sfx_open_door_clubs
    "Five minutes later I came out."
    sh "Well? How is it?"
    me "I don't get it."
    me "I can't get a clear direction, I need some kind of detector. Can you put it together?"
    show sh smile pioneer with dspr
    "Shurik grinned and, taking a folding hiking pocket from his pocket, opened it in one motion."
    sh "Science has many gits.{w} But sometimes simple worldly wisdom is enough."
    me "What are you talking about?"
    sh "There was a jar of boiled water on the table.{w} If it didn't get poured out."
    sh "Pour some into the glass."
    me "And?"
    sh "And that's it.{w} That's a simplified model of your body."
    sh "No nonsense like bones or muscles. Or rather, a model of your body's response to vibration."
    me "So, vibration?"
    sh "That hypothesis is as good as any other."
    "Shurik shrugged."
    show sh serious pioneer with dspr
    sh "The organism is too complex, so there are inevitable leads.{w} And here you have a ready-made 'hot-cold' detector."
    sh "You see?"
    me "I think so."
    sh "Well, then, fair wind."
    "I nodded and headed back in, holding the «detector» with both hands."
    stop music fadeout 3
    stop ambience fadeout 2
    play sound sfx_open_door_clubs
    scene bg int_clubs_male_day
    with dissolve
    play ambience ambience_clubs_inside_day fadein 3
    "Watching the surface reaction, I wiggled the glass in front of me, and after a couple of minutes I concluded that the hum seemed to be coming from exactly where I'd switched something on yesterday."
    "Trying not to think about the consequences of being here, under an invigorating low-frequency shower, I turned to Shurik."
    me "I think it's in the attic. {w} I'll try to climb up."
    sh "Are you sure? Won't Slavya take my head off later for dragging a sick man into my adventures?"
    "I shrugged."
    me "It's more fun than hanging around the infirmary all morning."
    sh "Yeah?"
    "He adjusted his glasses again in doubt."
    "But he seemed a little too eager to get back to his precious iron."
    "He sighed."
    sh "There's a ladder in the back room that we used yesterday.{w} Unfortunately, that's all I can help with - good advice."
    "He spread his hands as he did so, propping the doorjamb with his shoulder."
    sh "Take a flashlight with you just in case.{w} The light is there, from the skylight, but just in case."
    "I shrugged and went to the back room and fetched a ladder."
    me "Flashlight?"
    sh "In the closet."
    "Once I got what I was looking for, I proceeded to disarm the dangerous device."
    play music music_7dl["areyouabully"] fadein 3
    "Damn amateur."
    "Technology in the hands of a savage is like a pile of scrap metal."
    "After fiddling with the hatch for a while, I threw it back up and adapted the ladder to the edge."
    me "Good luck to me."
    sh "Yeah."
    "Shurik gave me a thumbs up, and I climbed up."
    stop ambience fadeout 3
    stop ambience fadeout 2
    play sound sfx_open_metal_hatch
    scene bg int_attic2_day_7dl
    with dissolve
    "And here the unpleasant experience was already more palpable."
    "Apparently, the lion's share of the hum was shielded by the ceiling and the boards."
    "Although I was sure until the last minute that even a concrete shelter wouldn't help against the infrasound."
    "Apparently Shurik feels about the same way downstairs as I feel up here now."
    "So I've only got a minute or so."
    "The spot of light bounced across the balusters, picking out some incomprehensible machinery, from the looks of it, long dead and de-energized."
    "It certainly wasn't like the data centers I'm used to; there was nothing 'for people,' that is, no lights or indicators or anything like that."
    "Simple and angry: turn on the hardware, and it works."
    "Kudos to Random for the fact that these devices can be tracked at once with the same simple principle - if there are wires going somewhere, it means the device can be turned off."
    "I said a kind word about Nikola Tesla and his principle of wireless power transmission. It would be ridiculous to encounter something like that here."
    "No, nothing like that."
    "The most obvious device with a power supply right here in the attic was some kind of spiky netting two steps away from the hatch."
    "Another device appeared to be a radio transmitter embedded in the concrete box."
    "What a touching neighborhood."
    play sound sfx_metal_door_handle_rattle
    "I wiggled my foot on the net. {w} For some reason it seemed vaguely familiar."
    "And the unearthly bliss, intensified many times around her, made me think of mother, father, and other relatives of the author of the device."
    "That was it.{w} At least I think so."
    "I traced the path of the cables and swore."
    "It seemed to be permanently soldered here, and you had to get out on the roof to disconnect on the other side."
    scene bg int_attic2_day_7dl at zenterleft with dissolve
    "And I was running out of time as it was - I was throwing up more and more, the room was storming and rocking with all my might."
    scene bg int_attic2_day_7dl at enterright with dissolve
    "There is, however, a trick."
    "It's called..."
    play sound_loop sfx_head_heartbeat fadein 2
    "What it's called, I didn't have time to think about it.{w} The nausea became unbearable, and, bouncing as far away as I could, I bent over in half."
    "Yeah."
    "That was a very good breakfast."
    me "Close to the elbow, but no bite."
    "The hitherto unnoticed wire went to the most common control box with a couple of rheostats."
    with fade2
    "I got closer."
    "Apparently, the big one is the radiation power.{w} If I remember Soviet technology correctly, it's also an on/off regulator."
    "And the small one?"
    "I turned it around aimlessly."
    "And immediately the buzzing sound halved."
    "It was as if the contacts had been removed from the humming brain, which had lavishly indulged it with short discharges."
    stop ambience
    stop music fadeout 2
    me "Shurik, I think this is it."
    "Looks like the device really is just a little loose."
    th "The operation of this device should not be felt by human. {w}That's not to mention the triggering time here should be from midnight to six in the morning."
    sh "Really?"
    play sound sfx_steps_clubs_nextroom
    play sound sfx_door_squeak_light
    pause(.5)
    play sound sfx_door_squeak_light
    "Footsteps rang out from below, the stairs creaked, and a head with glasses appeared in the attic."
    sh "You're ri..."
    "The device in my hands clicked distinctly."
    "And what had seemed like a nightmare to me before seemed like childish babble!"
    "It was like having your tooth drilled, painful but bearable."
    "But then they got to the nerve."
    with flash_red
    "Shurik fell down the stairs as he was and fell silent."
    play sound2 sfx_bodyfall_1
    "I think he passed out."
    "Helpless jerk."
    scene black with fade
    "I, no longer trying to adjust or change anything, made my way to the stairs on my limbs."
    play sound sfx_chair_fall
    with vpunch
    pause(1)
    scene black
    $ renpy.show("bg int_attic2_day_7dl", at_list = [sdl_transform8], what = Noir("bg int_attic2_day_7dl"))
    play sound2 sfx_bodyfall_1
    with fade
    stop ambience fadeout 2
    "It was all a blur from then on - the slamming hatch, the falling ladder."
    play sound sfx_fall_metal_door
    scene black with fade
    "Me, either puking on the floor with pure bile, or dragging Shurik, who was dead to the blue."
    scene black
    $ renpy.show("bg int_clubs_male_day", at_list = [sdl_transform3], what = Noir("bg int_clubs_male_day"))
    play sound2 sfx_bodyfall_1
    scene black with fade
    "It was two meters from the table to the door."
    "It seemed like an eternity to me."
    scene black
    $ renpy.show("bg int_clubs_male_day", at_list = [sdl_transform4], what = Noir("bg int_clubs_male_day"))
    "I've never covered such a long distance."
    play sound sfx_open_door_clubs fadein 0
    scene black
    $ renpy.show("bg ext_clubs_day", at_list = [sdl_transform5], what = Noir("bg ext_clubs_day"))
    with flash
    play sound sfx_fall_wood_floor
    play ambience ambience_7dl["explosive_post"]
    "And I only let myself pass out completely when I pushed the bespectacled man out of the club and he scooted down the steps."
    play sound sfx_bodyfall_1
    scene black with flash
    "Passed out right there on those steps."
    "Lost consciousness."
    scene anim prolog_1
    show prologue_dream
    stop sound_loop
    play music music_list["sparkles"] fadein 3
    play ambience ambience_camp_center_night
    "There's too much suspicious stuff going on in this camp."
    "What the hell is a super-powered emitter being used to disperse demonstrations in a harmless cybernetic club?"
    "Why is it operating on frequencies perceived by humans?"
    "And what was in there when I thought I turned it off?"
    "Had it shifted to a range that was more perceptible or dangerous?"
    "No time to think about that now."
    "There is a design and development department."
    "Discoveries and accomplishments."
    "In moving away from inquisition to modern regulators of society, we lost something very, very important."
    "We have lost the specialists who can take a balanced and sober look at the invention and verify whether humanity is ready to use it, or whether we should freeze the project and put it away for a long time."
    "You got a mustache?"
    "Like hell you are!"
    "Seismic, meteorological, cyberweapons."
    "Even this buzzer here."
    "Not ready."
    "The first two for the reason you can't give man too much power over the planet."
    "And the buzzer... It's dangerously close to a psychotronic weapon."
    "Which is actually banned. And banned for a reason."
    "Although I don't know the local political history thoroughly, I'm sure people here have come to the same conclusions."
    "And an office like this, which would slap the hands of all the intelligence agencies of the world, making it clear that open misuse of this sort of thing would lead to disaster, would be very appropriate."
    "Of course, quietly everyone would continue to use, but without publicity, without it."
    "There is nothing good in the fact that the average citizen would abruptly lose confidence in a state that has encroached upon what is most sacred to them-the freedom to keep their consciousness as a slave in a carefully nurtured form."
    "Although, in general, states have been capable of doing this almost since the tenth to eleventh years of the twentieth century, when the development of chemical means of regulating the mind began."
    "Just put it off for a long time.{w} Apparently, for the purpose of developing these kinds of infernal machines."
    "The internal stream of consciousness faded, releasing me from the shadows of oblivion."
    scene bg ext_clubs_day
    show unblink
    "And I was finally able to come to my senses."
    "Alone."
    "Shurik was nowhere to be seen."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_sl_cl_laundry:
    scene bg ext_aidpost_day with dissolve
    play music music_list["drown"] fadein 3
    "This morning was like Groundhog Day - it went on and on."
    "Lunchtime came, but the feeling that I was still in a frantic and matey morning didn't go anywhere."
    "Viola was gone, Slavya was gone, Olga was gone."
    "Three people who had struggled to pretend they cared about my fate had just revealed their true selves to the world."
    "The bandages I took off, all that was left was a patch of hair on the cropped back of my head."
    "The hair must have been a mess."
    "What do I care, though, I only get my hair cut when it gets in the way of smoking and drinking tea at the same time."
    "I'm not going to conquer the girls with this hair, am I?"
    "The low clubhouse drew in and out of my thoughts, and fleeing them, I circled the infirmary once more, looking out for something useful to me now."
    "And it was found very quickly."
    "A rope holder on which was attached the ladder leading to the attic and roof."
    scene bg int_attic2_day_7dl with dissolve
    "One minute, and I'm up there."
    th "Since everyone left me, I'm going to hide from everyone."
    th "Let's see you run then."
    th "You run!"
    "I sat at the window, looking down and reveling in my own meanness."
    "The mood was cheerful."
    "Anticipatory."
    show blink
    "So I didn't notice how I fell asleep."
    stop ambience fadeout 6
    $ persistent.sprite_time = "prolog"
    $ prolog_time()
    scene bg ext_entrance_night_clear_7dl
    show prologue_dream
    show unblink
    "The semi-circular gate, adorned with a single five-pointed star and sharp pegs on top, reluctantly gave way under demanding hands."
    "The right servo was a little jammed, but I was used to it and distributed the power so as not to feel the inevitable misalignment."
    voice "You are aware that this is a closed facility, and you here ... Ghrhg..."
    "The fingers, gathered into a metal fist, struck the black-haired man just below the chin."
    "We fight so desperately for life that we are willing to take it from others and not even feel remorse..."
    "Such a useful thing was helping the handicapped, the legless, the partially paralyzed."
    "What did the man do with it when he got his hands on the finished device? That's right, put in a circular saw and a six-barreled machine gun."
    "Slavya tossed a dimly gleaming round to the sky, and it exploded in the air, flying a bunch of needles."
    "Another second."
    sl "The perimeter is ready. Give the signal, and I'll send this place to the moon."
    "She reported."
    am "Well done. Give me ten minutes, and then you can go ahead."
    sl "But... How..."
    am "Did you really think we were going to do this quickly and go home?"
    "From the look in her eyes, that's what she thought."
    "You silly girl."
    "Like it's so hard to understand that once you've volunteered to go into that hellish machine that burns body and metal, there's no going back for you."
    "You're what all the intelligence agencies of all time call a 'meltdown,' a disposable agent, expendable material to be spared during an assignment."
    "Even though even now I move several times faster than the average man, much stronger and more resilient than he is."
    "I'm not going back. And that's obvious."
    sl "Try to survive."
    "She understood everything."
    "She stroked my cheek and stepped back, hiding her gleaming eyes."
    scene bg ext_clubs_night
    show prologue_dream
    am "Ten minutes, do you hear? And click. That's an order."
    sl "And if you don't come out?!"
    am "You heard everything!"
    "Stupid girl."  
    "I guess that's all they're there for, girls like that, to be taken advantage of by scoundrels like me."
    "I'm well aware that even my costume won't help here, but her perimeter... It would be much more useful."
    "And after kicking the door open, I jumped into the dark room, bristling with nine-millimeter rounds."
    scene
    $ renpy.show("bg ext_clubs_night", what = Noir("bg ext_clubs_night"))
    show prologue_dream
    with fade
    "The air thickened and thickened, the colors shifted to the purple spectrum, and my knees crunched hard - a second in this state costs me a year of my life."
    "But counting time now is like giving up a cigarette on your deathbed: they say it's bad for you."
    scene
    $ renpy.show("bg int_clubs_male_day", what = Noir("bg int_clubs_male_day"))
    show prologue_dream
    with fade
    "After two minutes of fighting and eight minutes of waiting in an empty room, I finally waited."
    "Slavya did what I brought her here to do."
    "Showed her unnecessary loyalty and heroism."
    play sound sfx_muffled_explosion
    with vpunch
    "The perimeter shuddered, the walls bounced, and the beams beneath the ceiling shuddered and slowly crept downward."
    "The room began to fold, grinding everything inside."
    "Including even..."
    scene black with dissolve
    pause(1)
    $ renpy.show("bg int_mine_heart_7dl", what = Noir("bg int_mine_heart_7dl"))
    show prologue_dream
    with easeinbottom
    "Her eyes were calm, a little excited, even though all hell was breaking loose."
    sl "I did as you said."
    th "And now I've come to save you."
    th "And to take you to the clinic, where the carriers will be removed from your body, the neural interface to the exoskeleton."
    th "And we'll live happily ever after."
    "And a whole bunch of other things she could have said. {w}Stupid, inappropriate, fantastical things."
    "But instead, she rudely poked me with a gun which she got from somewhere I don't know where."
    th "Don't like it, do you? Don't like it."
    th "Only you're not dragging me anywhere, you understand that, don't you?"
    th "I didn't come here for nothing."
    th "I didn't just lie down in a machine-where-is-no-return, and now flaunt servos fused to flesh for no reason."
    "But primarily so that no one would ever again have the opportunity to tamper with someone else's brains and rearrange them as the operator pleases."
    "Whenever someone wants to twist the controls."
    "And in case she doesn't realize it, I know full well that all it takes to destroy a device is for it to be recreated by hardworking robots, tirelessly, day and night, ready to do their duty."
    "It is useless to fight them, for they are produced on an avalanche-like scale in an underground assembly hall - in a basalt pocket that cannot be penetrated from outside by a nuclear charge."
    "The system is simple, closed and frighteningly homeostatic."
    "The only way to change anything is to shut down the entire system at once, in a multi-way, complex operation that simultaneously disables the assembly circuits, programmers, and power bubble generators."
    "A method for the powerful."
    "And all I have is my suit, which is painfully torn by shunts at junctions with flesh, and infinite determination."
    "And Slavya."
    "Good girl. {w}Only she has no future as a soldier."
    "Because she wasn't created to protect, but to recreate."
    "I sat down and threw myself at her."
    play sound sfx_7dl["deagle_shot"] fadein 0
    "With a broken leg, my performance looked questionable even to me, but the 'juice' in her hands coughed belchily."
    "And a sharp, red-hot nail was driven into my chest."
    "Slavya took a step back with her hands over her mouth, looking disbelievingly at her own hands. {w}Her eyes rounded with horror."
    sl "How is it...I didn't...{w} I couldn't..."
    am "Get. Out."
    "The pulse-discharge system doesn't work if the operator intentionally hurt himself or decided to commit suicide."
    "Oh no, the suit is able to get the operator out of situations where he would inevitably die, able to keep him awake by drugging him with morphine or antibiotics."
    "No surprise, this prototype is one-to-one stolen from the HEV MAC5 from the never-released third 'Half-Life' in my home world."
    "But if the operator is threatened, the program is triggered so as to prevent the enemy from taking over the skeleton."
    sl "I'm not leaving you here."
    am "Run, you idiot!"
    "A few thoughts, packaged together like a wireless network, went to her."
    "Come on, come on, girl honors, the only 'witch' in the course with an empathy quotient above ninety percent, when better than now to unleash your potential!"
    "That's right, we've been developing and developing cybernetic increments, reality augmentation systems, firmly believing that humans are weak and fragile."
    "So behind the mile-long lines to implant 'free' network access points with 100 percent coverage across the globe, behind the silicone flesh that makes an android indistinguishable from a homosap, behind the ever accelerating pace of life, we began to forget one thing."
    "Man is a living being. And living things evolve."
    "Who could have known that basic empathy and pity would be the key to becoming a supra-human? {w}That empathy and suggestion would be stronger than silicon substrates and steel plate?"
    "All right, let's not be stronger. {w}Let's just play by different rules."
    "Everything I knew, everything I remembered, I passed on to her."
    "A moment, and the hordes of Huns rushing across the steppe lose their stride, and some of them, dangerously close to some black obelisk, seize their weapons and attack their kindred."
    "A moment - and the air is cut by a Cossack's saber, and the diagonally-splitting turtleneck whips in the wind, and the head rolls in the snow, the crudely cut-down cape is reflected in the black pupils."
    "A moment, and the leather-clad, shoulder-length figure pulls an archaic pistol with its clip forward and fires it into the back of his comrades' heads, pushes open the door, and enters the chapel."
    "In the blown-up chapel, a painfully familiar building, where generations and generations of kids have been working to advance the national cyber industry, grows up before my eyes."
    sl "How old were you?"
    "She retreats a step back."
    am "More than I'd like. Now run!"
    "A blink and a figure in a light scouting suit runs out of the clubs."
    "She looked back at me one more time and leaped out of the crumbling building in three leaps."
    "And I became unnecessary and useless. As I always have been, ever since I assembled my first working prototype twenty-two years ago-a snub-nosed, clunky one connected to a stationary power supply."
    "Now these things are called 'last' chance and are kept in reserve along with the EO in aircraft and armored personnel carriers. Simply because a modern, servo-driven suit can do all the same things and does not require splicing, integration into the human body."
    "There were events in Tver - the separatists again deployed government agitators against the agitators themselves when they found out they were using psychogenics."
    "In Moscow the business towers burned down, the boastful robocavalry couldn't stand up to our strong-armed men, who can break all the software in security systems on their laptops, twenty years outdated, at their knees."
    "In St. Petersburg the revolution was practically bloodless, the corporations simply moved their production facilities and offices out of the city after the first person was crucified at the Alexander Column."
    "Russia smoked and smoked at the crossroads, and the surrounding aspen trees were decorated with bluish 'snowdrops', and institutions were hurriedly introducing restored GOST standards for the hardware in use."
    "The revolution had passed its peak, that difficult moment called by someone the Pugachev limit, and now the purging of the country's territory was simply a matter of time and such pinpoint operations."
    "Russia went on living."
    "Except that I continued to be unnecessary."
    "And when the auxiliary energy tanks almost burst from excess energy, and I exhaled, confirming the initiation of the suicide bomb, there was silence in the world for a moment."
    "Rainbow, weightless silence of the forgiving and the forgiven man."
    "What is possible only alone with death, which you have so long sought."
    "And everyone who heard that silence understood, for a split second, who he was and what he was."
    "So did I."
    scene black
    show prologue_dream
    with dissolve
    stop music fadeout 3
    $ persistent.sprite_time = "day"
    $ day_time()
    scene bg int_aidpost_day
    $ renpy.show("genda_portrait", what = Dawn("genda_portrait"))
    with diam
    "Viola was sitting in the same spot again."
    "«Xonix» on her screen changed to poker, but overall everything was exactly the same as it had been since this morning."
    cs "Had a nice sleep?"
    "Without turning around, she asked."
    me "Excuse me?"
    cs "Pioneer... I know it's useless to tell you to take care of yourself, not to run around and exert yourself."
    me "And you fed me sleeping pills?!"
    show cs smile with dissolve
    "Viola broke away from the game and turned to me:"
    cs "You what. Sleeping pills are harmful in these conditions and incompatible with most of the medications I've been using on you."
    me "Uh..."
    cs "Just a sedative."
    "I raised an eyebrow incredulously."
    cs "Okay, it was a tranquilizer. It's harmless. Mostly."
    me "Mostly?"
    show cs shy with dissolve
    cs "As you could see, it causes drowsiness."
    cs "And tell me if you find a rash anywhere."
    me "Aaah!"
    "I screamed in panic, and the nurse didn't hold back her smile:"
    show cs smile with dspr
    cs "Just kidding, just kidding. {w}In case you haven't noticed, you've been asleep all day."
    me "So I missed lunch?"
    "I switched to more pressing matters."
    cs "I tell you what, it's supper in fifteen minutes."
    cs "But since you've been behaving yourself and snoozing in my attic all day, I see no reason to keep you any longer. How are you feeling?"
    "I did a cursory diagnostic and admitted Viola was right - the sleep did do me good."
    show cs normal with dspr
    cs "Yup. {w}Get yourself cleaned up and head for the mess hall, your pioneer girl is already instructed and waiting."
    if alt_day4_me_neu_transit != 'sl_cl':
        me "Is that the one I'm dating?"
        "I couldn't help myself."
    "Viola's eyelid crept down in a slow wink."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_sl_cl_supper:
    scene bg int_dining_hall_people_sunset_7dl with dissolve
    play ambience ambience_dining_hall_full fadein 3
    play music music_list["two_glasses_of_melancholy"] fadein 1
    "There was a loudspeaker on the left hand side of the handout, now broadcasting something bravura and patriotic, and a line of pioneers with trays stretched out."
    "That's right, the parents have scattered, the ones they fed are sleeping in the cabins, and the especially hungry have reached here in search of provisions."
    play music music_7dl["nookie"] fadein 3
    "A few minutes later the speaker started coughing, grunting, and heavy guitar riffs flewn out instead of marches."
    "And I had a rough idea whose authorship this diversion was."
    show dv laugh pioneer2 with dissolve
    "Well, not exactly authorship."
    "Most likely, in the ginger tandem, Alisa was again the thinker and generator of ideas, and Ulyana served as the executor."
    if not alt_day4_sl_cl_tut_iz:
        "If I remember correctly, I failed to remove the sound curtain, which means the transmitter is protected from any encroachment.{w} And if Ulyanka and Alisa managed to figure out a way to get to the transmitter, then we'll listen to whatever they want."
    "The counselor looked at the speaker, shifted her gaze to our tables, but said nothing."
    "She looked exhausted - the children's concert seemed to have worn her out."
    if not alt_day4_sl_cl_tut_iz:
        "Slavya was not shining with health either - after all, she was dragging my lifeless carcass on her back to the diocese of good Viola again."
    scene bg int_dining_hall_people_sunset_7dl at zenterright
    show sl normal pioneer at cright
    with dissolve
    "I let Slavya go ahead of me, and I myself joined the keel, and looked around."
    "Our tables were surprisingly full - it looked as if the pioneers of our squad had either not been visited by their parents, or were notably more focused and businesslike."
    "Gave out their portion of weasel and smoked sausage, packed up and took off.{w} Perfect parents."
    if not alt_day4_sl_cl_tut_iz:
        "Not for me to judge, of course, having lain in unconsciousness for the last five hours, but still..."
    with fade
    "With great difficulty I was able to find free seats just down the aisle, right next door to the radio-terrorists."
    "They were talking about something, chuckling quietly at the confused faces of the pioneers, who realized that from now on something not exactly pioneer was playing on the air."
    "Everything went on in its own way - the crowd was only disorganized at first glance."
    "But I've been in that kitchen, I've got the centers of interest figured out."
    if (counter_sl_7dl >= 2):
        "We had the redheads. There were bursts of laughter from the second squad, too, as the familiar curly-haired fella was giving his benefit."
    else:
        "We had the redheads. There were bursts of laughter from the second squad, too, where a certain curly-haired lad of about fourteen was conducting his benefit."
    if alt_day2_dv_us_house_visited:
        "The third squad was a slightly flatter mass, but there, too, there was a picture of the splitting of the collective - a vaguely familiar red-eyed pioneer nodded to me for some reason."
    else:
        "The third squad did not distinguish certain leaders, but there were renegades - some shaggy, red-eyed pioneer glared at me hostilely."
    play music music_7dl["will_you"] fadein 3
    "Olga Dmitrievna and Viola, seated at the same table as Miku, again engaged in an endless discussion of the degrees of freedom available to the pioneer.{w} Perpetuum Dispute, my ass."
    "Olga was sure that there was a reason the camps were stocked with bromine - albeit not as tangible as military units, a reason emergency first-aid kits included rubber products and emergency contraception... Like 'postinor.'"
    mt "It all serves to fight the consequences!"
    "She hotly preached."
    mt "And my job, as a counselor, is to prevent the situation itself."
    cs "And how are you going to do that? Youth will find its way everywhere; you can't keep track of everyone."
    show sl shy pioneer with dspr
    "Slavya was a little embarrassed at these words for some reason."
    "Some unpleasant memories, it seems."
    mt "I don't need that."
    "Olga smiled."
    mt "I choose the most problematic ones, and I work with them. {w}Like with Semyon."
    show mi grin pioneer at fleft with flash
    "Miku giggled when she saw that I had my ears pricked up, but she didn't say anything."
    hide mi with flash
    mt "It's very good that Slavyana took over, I already had an experience last year with a pioneer like him."
    cs "And I remember very well how it ended."
    "The nurse grinned."
    cs "Is THAT how you're going to handle touchy situations with possible immorality?"
    mt "It works. {w} And it's not bad."
    "The counselor shook her head."
    mt "And I think we're being overheard."
    "She waved her fist at me without turning around and lowered her voice so that it could no longer be made out over the noise of the pioneers talking."
    show sl smile pioneer with dspr
    sl "You watch it, Semyon."
    "Slavyana smiled."
    sl "Watch and remember, because tomorrow everything may be different, other rules, other people."
    me "A hint that every night is unique in its own way?"
    sl "Yes! {w}Somebody you might not see tomorrow, somebody will not pay attention to you, somebody will have more problems and somebody will solve them."
    sl "Life, Semyon.{w} That's my passion!"
    me "That's it? Life?"
    sl "Yes.{w} When you see what's going on, understand it, and can create the conditions - you feel like you're doing something good."
    me "Are you hinting at sweeping the square?"
    show sl smile2 pioneer with dspr
    "Slavya giggled into her palm."
    sl "You can say that, too, if you want."
    me "Did it ever occur to you that this would all end one day?"
    me "How old are you? {w} Next year they won't let you in anymore."
    sl "It never ends, you know? {w}As long as a man cares - To hell with it, dance - we'll keep helping each other, smile a little happier."
    me "One day it might not matter."
    sl "To everyone?"
    show sl normal pioneer with dspr
    "Slavya shook her head."
    sl "It's very hard for me to imagine such a thing."
    sl "But even if the whole universe hardens, there's always some warmth in a man's heart.{w} Even in yours, Semyon."
    sl "One day you'll realize that's all that really matters."
    show sl smile pioneer with dspr
    "She smiled again and hid behind a glass of kissel."
    "And I thought, even if she is deluded - I'd damn well like to be a part of that delusion."
    "Because it's always cozy, comfortable, and the dust particles dance in the sunlight streaming through the curtains."
    me "You seem to seriously believe all this nonsense."
    sl "It's not nonsense!"
    show sl serious pioneer with dspr
    "The girl's eyes twinkled."
    sl "That's how I was raised my whole life, and that's how I'll raise my children."
    me "Harsh manifesto, what can I say. {w} Haven't you tried to ballot..."
    "I did not finish - straight to our table dragged a tray Lenochka Tikhonova, in full accordance with her surname, quiet and on her mind."
    scene bg int_dining_hall_people_sunset_7dl at enterleft
    show sl normal pioneer at right with moveinright
    show un normal pioneer at cleft
    with dissolve
    un "May I sit?"
    "I shrugged my shoulders, and Slavya moved over on the bench."
    sl "Come on down.{w} Heard that already?"
    un "Of course.{w} It's still playing."
    show un smile pioneer with dspr
    "Redheads, catching her stare, laughed out again.{w} They were definitely pleased with themselves."
    un "What happened to Alexander? I can't find him anywhere, and I have undeveloped photos and underwritten articles."
    if not alt_day4_sl_cl_tut_iz:
        me "Me and him were trying to set up the radio."
        sl "Yeah? I found you on the porch alone."
        me "What do you mean? I pushed him out on the street myself, and then..."
        sl "No, you didn't."
        show sl serious pioneer with dspr
        "Slavya shook her head."
        sl "You were there alone, there was no one else around."
        me "Mutual aid is at its best, I see..."
    un "That doesn't sound like him. He's a very responsible young man."
    show un serious pioneer with dspr
    un "Only a little distracted and out of touch. But I don't think that's bad."
    th "After all, any mad scientist is accompanied by a lab assistant who's wholeheartedly in love with him."
    "I know, Hollywood movies told me!"
    show un normal pioneer with dspr
    un "We have to look for him, then."
    sl "Let's do it together?"
    show un shy pioneer with dspr
    "Lena got embarrassed."
    un "No, it's not... It's uncomfortable."
    sl "Everything is comfortable."
    "Slavya answered in an unapologetic tone."
    if alt_day4_sl_cl_tut_iz:
        sl "Semyon's been through a lot, judging by the way he slept all day, so I'm not taking him with me, and it's kind of sad to go alone."
        me "Hey, what does that mean?"
        "I couldn't believe my ears."
        me "What do you mean you're not taking me with you?"
        show sl sad pioneer with dspr
        sl "Semyon, don't argue, please. {w}You're acting like a child."
        "I only sighed."
        "What else could I do."
        $ alt_day4_sl_cl_tut_lf = True
    else:
        sl "I took the evening off anyway to keep our disabled veteran company, so I'm totally free."
        me "You took the evening off from your worries? Isn't that something you do pro bono?"
        show sl smile pioneer with dspr
        sl "Actually, yes. But it was worth warning the counselor not to count on me today."
        with fade2
        th "I'm sorry, Olenka Dmitrievna, but you won't be riding me today."
        th "But I didn't create this world, I don't change it, and Slavya, thank goodness, is happy with it this way."
        menu:
            "Fine, let her come with us" if herc:
                $ lp_sl += 2
                $ alt_sp += 2
                $ karma += 10
                show sl smile2 pioneer with dspr
                "Slavya smiled:"
                sl "That's good. It's more fun together!"
            "Why do we need her?":
                $ alt_sp += 1
                if alt_day_binder != 1:
                    me "I could be wrong, but Lena has not yet shown the talents of a good bloodhound."
                    show sl serious pioneer with dspr
                    sl "Neither did you."
                else:
                    me "What good is she going to do?"
                    me "I don't think she's going to help us."
                    sl "That's no reason to chase her away."
                "Slavya pressed her lips together."
                sl "Let her come with us if she wants."
                "I shrugged."
            "Well, if you insist…":
                $ lp_sl += 1
                "I wasn't thrilled that our impromptu date would be ruined by the presence of an outsider."
                "But Slavya must know better?"
                "I've come to terms with her decision."
                sl "You know, Semyon."
                "Slavya began."
                sl "You better stay in the camp, and Lena and I will look for him."
                menu:
                    "Forget about it" if herc:
                        $ alt_sp += 2
                        $ karma += 10
                        me "No way. {w}I'm going to worry!"
                        me "I'd rather go with you."
                        "Slavya wanted to object, but I raised my hand:"
                        me "This conversation is over. {w}We're going together."
                    "Deal":
                        $ alt_sp -= 1
                        $ lp_sl += 1
                        me "Just tell me everything later, okay?"
                        "The girls nodded in sync."
                        $ alt_day4_sl_cl_tut_lf = True
                    "But…":
                        $ alt_sp += 1
                        sl "Semyon, be a little more serious."
                        "Slavya asked."
                        sl "I'm worried about Alexander alone, let me not worry about you too."
                        "I sighed and nodded obediently."
                        $ alt_day4_sl_cl_tut_lf = True
                    "And I'll miss all the fun?" if loki:
                        me "Don't even hope for it."
                        $ alt_sp += 1
                        me "I'm coming with you. Period."
                        sl "With us."
                        "Corrected Slavya."
                        "I squinted at Lena incredulously."
                        me "Yes."
            "I'm against her coming with us" if loki:
                "I folded my arms across my chest."
                $ alt_day4_sl_cl_un_rej = True
                $ alt_sp += 2
                $ lp_sl -= 1
                show sl serious pioneer with dspr
                sl "What are you talking about?!"
                show sl surprise pioneer with dspr
                "Lena fidgeted, muttering something to herself."
                me "What you heard."
                me "We don't need her in our search, we can manage on our own."
                show sl angry pioneer with dspr
                sl "You know what, Semyon, let me be the one to decide, as the one in charge?"
                "Slavya frowned."
                me "In charge? Well, well."
                me "Mind you, I was against it."
                sl "You know, why don't you just stay in camp, at least I won't worry about you."
                "I couldn't believe my ears."
                me "What did you do now?"
                show sl normal pioneer with dspr
                sl "That's right."
                "Chillingly, Slavya replied."
                sl "And I'll worry less about you."
                "I grinned."
                th "I love people who decide things for me."
                th "And yet they're absolutely convinced that I'm going to follow their instructions."
                "It makes me want to smile lightly and ask in a heartfelt tone:"
                "Make me."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_sl_cl_party_up:
    scene bg int_dining_hall_people_sunset_7dl
    show mt normal pioneer at center
    show un normal pioneer at left
    show sl normal pioneer at right
    with dissolve
    play ambience ambience_dining_hall_full fadein 3
    play music music_7dl["will_you"] fadein 3
    mt "Did you talk about Shurik?"
    "Hovered over the table Olga."
    mt "He was seen at the south gate at the exit of the camp. {w} He was heading out of the territory."
    me "Jesus fucking Christ..."
    sl "Excuse me?"
    me "Nothing, nothing."
    "The search radius just expanded by leaps and bounds."
    mt "We have no access to the radio room."
    "She gave Alisa and Ulyana an unkind look."
    mt "So come to me after supper and get my dynamo flashlight, don't lose it, I don't have a spare."
    me "Dynamo?"
    if alt_day4_sl_cl_un_rej:
        "Slavya squeezed hard a few times on something invisible and looked at me perplexed."
        show sl surprise pioneer with dspr
        sl "Semyon, what did you see so funny?"
        me "Oh... No, nothing... Ha-ha... Sorry."
        "I turned away, struggling with the corners of my lips parting."
        show sl normal pioneer with dspr
    else:
        un "You turn the knob, it lights up."
        "Lena enlightened me."
    me "Interesting stuff, I guess..."
    mt "I'll arrange for you to leave the grounds, since you and Slavya are going. {w} But just the three of you, don't split up, okay?"
    if alt_day4_sl_cl_un_rej or alt_day4_sl_cl_tut_lf:
        sl "Olga Dmitrievna, the two of us will go."
        show mt grin pioneer with dspr
        mt "Lena changed her mind? {w}And she said she wasn't afraid of the dark anymore..."
        sl "No, Olga Dmitrievna, Semyon won't go with us."
        show mt surprise pioneer with dspr
        mt "Are you serious? He won't go?"
        "The girls nodded in sync."
        mt "And miss the adventure?"
        "They shook their heads again, cosplaying Chinese bobbleheads."
        mt "Wouldn't want to let you go completely unguarded."
        show mt sad pioneer with dspr
        mt "But since Semyon is feeling bad right now..."
        "Very bad."
        "I nodded."
    else:
        "She flashed her eyes, the girls nodded obediently."
        me "What, you're just going to let us out?"
        "I couldn't stand it."
        mt "Yes.{w} Because there's only one place he could go.{w} And you'll go there, too - and then straight to camp!"
        me "What are you talking about?"
        show el normal pioneer at fleft behind un with dissolve
        el "About the old camp."
        "I was enlightened by an unidentified to this point Electronik."
        el "There's some electronics left in the old compound, Shurik might be interested."
        show mt angry pioneer with dspr
        mt "That doesn't excuse him going out without permission.{w} I'll get him for that."
        "She waved her fist at who knows who, and Electronik hurriedly excused himself before he got the hot hand."
        hide el with dissolve
        me "He has to be found first."
        show mt normal pioneer with dspr
        mt "Yes.{w} Let's be consistent."
        sl "We'll find him, I promise!"
        "Slavya swore fervently."
        me "And if we don't? If he didn't go to the old camp, but somewhere else where we won't be able to find him?"
        show mt sad pioneer with dspr
        mt "Then go back to the camp, and we'll ask the district police for help.{w} The last thing I need is three pioneers being lost."
        mt "But of course, it's better that everyone gets found."
        me "I don't like that."
        show un serious pioneer with dspr
        un "You won't go looking? You can refuse."
        sl "Yes. {w}If you don't feel well, you..."
        me "No. The situation is stupid.{w} Like the lead in a cheap horror movie."
        show sl scared pioneer with dspr
        sl "I'm sorry, what?"
        "A cool palm immediately rested on my forehead."
        sl "No fever.{w} You're not schizo rambling."
        me "Of course not! I just don't like it."
        show sl normal pioneer with dspr
        sl "And yet we go looking for him.{w} There's a reason we wear ties."
        "And a badge with a bald pokemon on it."
        sl "We're pioneers, which means we have to help each other."
        "She said it too hot."
        "I guess if there was a rival religion to communism in the Soviet Union, it would be very pious."
        "Or, on the contrary, turned into a novice of some cult with ritual scrapings and Slavic runes of blood on foreheads."
        show sl sad pioneer with dspr
        sl "Anyway, I'm going. Lena?"
        "Lena nodded."
        sl "Alisa, Ulyana?"
        "The redheads shook their heads in sync.{w} That's right, they have enough of their own business to do."
        sl "Semyon, I'll take you to the infirmary and go."
        me "Hey, I didn't say I was refusing!"
        show sl surprise pioneer with dspr
        sl "Yes?"
        "She was surprised."
        show sl sad pioneer with dspr
        sl "Then..."
        me "We're going together, together. {w}I just don't like all this."
        sl "You're repeating yourself."
        me "Yes."
    scene bg int_dining_hall_people_sunset_7dl with dissolve
    play music music_list["always_ready"] fadein 1
    "Supper was entering its final stage."
    if ('library' in list_voyage_7dl):
        show ka angry pioneer with dissolve
        "Danechka was cheerful and pleased with himself - a clerical button was found on the second squad leader's chair, and she jumped up with a shriek."
        hide ka with dissolve
    else:
        show ka angry pioneer with dissolve
        "There was a shriek from across the counselor's desk, and some short girl jumped up from her chair."
        "That's a familiar picture of a chair and a button."
        "Second squad, if I'm not mistaken?"
        hide ka with dissolve
        "From there came the contented laughter of the curly-haired boy who had already become so familiar."
    "Ulyana was keeping up with him - from the third squad came girl's squeals mixed with an inept hiss, someone had already removed the unfortunate speaker and, wielding a fork, tried to remove the contacts, and the cook took it away with cries of freedom of musical creativity."
    "Everything was as usual, familiar and messy..."
    if alt_day4_sl_cl_un_rej or alt_day4_sl_cl_tut_lf:
        scene bg ext_aidpost_sunset_7dl with dissolve
        play ambience ambience_camp_center_evening fadein 3
        "I nodded to those present and walked out, making my way toward the infirmary."
        "I left Slavya, who tried to stand behind me, with a careless gesture."
        "Today I am an honorary prisoner, and I must not be burdened at all."
        "Let them think so, who am I to argue with them?"
        if alt_day4_sl_cl_tut_iz:
            "In the dark, it might be a little hard to find."
            "But that's okay. I'll just go in and come right back out."
        else:
            scene
            $ renpy.show("bg ext_square_day", what = Dawn("bg ext_square_day"))
            with dissolve
            "The flashlight I used while I was climbing in the clubhouse attic was still with me."
            scene bg ext_square_sunset with dissolve
            "It will come in handy in my search."
        "After equipping myself as best I could, I nodded to myself contentedly and staggered toward the south gate."
        scene bg ext_path_sunset with dissolve
        stop music fadeout 3
        play ambience ambience_forest_evening fadein 3
        if alt_day4_sl_cl_tut_lf:
            play sound sfx_slavya_run
            "A few minutes later, however, I heard the twin approaching sounds of footsteps."
            menu:
                "Hide":
                    "I jumped into the bushes and went silent."
                    show sl normal pioneer at cleft
                    show un normal pioneer at cright
                    with moveinleft
                    "A few minutes later, the girls came into sight."
                    "I let them pass me by, and after only waiting a few minutes, headed in the same direction."
                    hide un
                    hide sl
                    with easeoutright
                    $ alt_day4_sl_cl_lf_solo = 1
                "Give up":
                    "It was too late to hide."
                    "I was caught."
                    "And a few seconds later I was blinded by a sheaf of light hitting me in the face."
                    scene bg ext_path_sunset at zenterleft
                    show sl angry pioneer at cleft
                    with flash
                    sl "Semyon? I told you to go back to the infirmary."
                    "I smiled and shrugged."
                    me "If you don't want to take me with you, I'll go myself."
                    show sl normal pioneer with dspr
                    sl "Is that so?"
                    "Slavya pondered."
                    show sl smile pioneer with dspr
                    "And then she smiled."
                    sl "Well... I can't force you."
                    sl "At least this way you'll be out in the open."
                    "She waved her hand invitingly:"
                    sl "Come with us!"
                    $ alt_day4_sl_cl_lf_solo = 3
        elif alt_day4_sl_cl_un_rej:
            "I hid from the rushing girls, seemingly not looking around at all, and leisurely moved in the same direction."
            "My quest will succeed!"
            $ alt_day4_sl_cl_lf_solo = 1
    else:
        me "Let's go."
        "I said, getting up."
        "There was such a commotion around us that no one would have noticed our disappearance, and it really gave me a headache."
        "Olga had finished eating by this time and was standing at the door, looking out for us.{w} She intercepted my gaze, nodded, and went out into the street."
        "We hurried after her."
        "Slavya was in the vanguard, I was in the middle, and Lena was at the back of the procession."
        "At the exit there were people on duty who wanted to ask the activist something, but she gave them such a look that they got confused and retreated."
        "At the very doors Slavya demandingly put out her palm back, and I, clutching at it, did the same."
        "Behind me Lena gasped in surprise, but a second and thin maiden fingers took hold of my hand."
        "With a giggle Slavya plunged into the crowd at the exit and, piercing it like an ice-breaker of hummocks, fell out first on the porch and a little later off the porch."
        stop ambience fadeout 6
        stop music fadeout 3
        scene bg ext_dining_hall_near_sunset
        play sound sfx_open_door_clubs
        with dissolve
        "The pioneers rolled out into the street as if they feared that those who were delayed would be forced to stand watch out of turn - and by the way, quite justifiably so."
        play ambience ambience_camp_center_evening fadein 3
        "Anyway, five minutes later, armed with a flashlight and a rope from our counselor (nobody knows where the rope came from), we set out to our search."
        scene bg ext_house_of_mt_sunset with dissolve
        play music music_list["trapped_in_dreams"] fadein 3
        "I glanced over at the bicycle, which might well have been appropriate."
        me "How long has the old camp been abandoned?"
        "I inquired."
        scene bg ext_path_sunset at zenterleft
        show sl normal pioneer at cleft
        with dissolve
        play ambience ambience_forest_evening fadein 3
        sl "Since '74.{w} Fifteen years now."
        th "So the bicycle trick is out of the question. Those roads are probably only tractor-drawn."
        "A chatterbox is a spy's find. A little more like that, and I'll know the name of the nearest settlements and perhaps the river near the camp."
        sl "Semyon! Stay awake!"
        "I stumbled and almost dropped Slavya hurrying along on my left hand."
        me "Sorry, I'm..."
        show sl serious pioneer with dspr
        "She stopped and shined in my face."
        with flash
        sl "What? {w}If you suddenly don't feel well, tell me right away, don't force yourself."
        me "Stop it."
        "I shaded my palm and looked at her indignantly."
        me "Don't you know it's rude to shine a light in your eyes? {w} We're not in the KGB interrogation!"
        show sl shy pioneer with dspr
        sl "Sorry, I got a little scared.{w} Are you okay?"
        me "Alive.{w} Just let's not run, and we'll be fine."
        un "You're staggering."
        scene bg ext_path_sunset at enterleft
        show sl normal pioneer at left
        show un normal pioneer at right
        with dissolve
        "Noticed Lena."
        me "That's because we run too much."
        "I cut her off."
        me "If we walk like white people, at five kilometers an hour, I promise you I'll make it."
        sl "Why don't you go back to camp?"
        show sl smile pioneer with dspr
        "The blondie hesitated."
        me "And miss the whole adventure?"
        "I snorted."
        me "No way."
        show sl normal pioneer with dspr
        "Slavya nodded, muttering something like 'damn proud and stubborn,' and returned to her former course."
        "She gave me the flashlight when I insisted on being allowed to 'play'."
        "Lena was modestly silent, moving to the other side of Slavya - she seemed desperately shy of me."
    stop music fadeout 3
    with fade
    return

label alt_day4_sl_cl_lf_coop:
    scene bg ext_path_sunset with dissolve
    if alt_day4_sl_cl_lf_solo != 1:
        "I don't know, I guess at Slavya's pace we really would have made it to the old camp in half an hour, no more."
        "But since an honorary disabled veteran hero was now walking with them, we had to waddle at a leisurely pace."
        "I guess if Slavya and I were going out, we'd fight about it all the time."
        "We took each other out on the town, for instance, to the park, for a walk and to get some air."
        "And for me «having a breather», for example, is ironcladly associated with the leisurely movement."
        "If you're not marching leisurely, if you're not flirting, you're running somewhere, hustling, and generally preoccupied."
        "And what kind of rest is that?"
        "Slavya, on the other hand, seems to want to move at a gallop."
        "I noticed the disgruntled look Lena threw at her.{w} It seems I'm not the only one here who isn't happy with the pace of travel."
        "But anyway, the mad race through a road half-covered with grass, young spruces, and fallen tree trunks, ended an hour and a half later at some small two-story building."
    elif alt_day4_sl_cl_lf_solo == 1:
        "After half an hour of solo travel, the idea of going off alone in pride no longer seemed so brilliant."
        "Fifteen minutes later, it just seemed plain stupid."
        if alt_day4_sl_cl_un_rej:
            "Yes, that's how my desire to spend a little more time with Slavya turned out for me."
            "What better way to bond than on a camping trip together in the night woods!"
            dreamgirl "Just a night in the same sleeping bag and an escape from the infirmary, of course."
            "The libido grinned."
            th "It's too late for you to react. Where was your clever and helpful advice on how to wean that eggplant clingy girl?"
            dreamgirl "What's the point of discouraging it? You try the three of you, and that's it."
            "Well, yeah. What did I expect, I wonder."
        elif alt_day4_sl_cl_tut_lf:
            "And if you think back to the background against which this very idea came to fruition in the first place..."
            "Where did I get this weakness in the first place?!"
            "I'm... I'm independent! I live by myself a lot of the time, and I feel great about it."
            "I don't need anybody! I'm on my own!"
            "I've got willpower for five, self-sufficiency for ten! I've never submitted to anyone and I don't intend to."
            dreamgirl "So, are you done with the anti-crisis pumping?"
            th "Yes. We can move on."
        stop ambience fadeout 3
        "…"
        $ persistent.sprite_time = "night"
        $ night_time()
        scene bg ext_path2_night
        with dissolve
        play ambience ambience_forest_night fadein 3
        play music music_list["door_to_nightmare"] fadein 3
        "As I trudged through the bushes, I completely lost track of time."
        "And the fact that dusk had already fallen around me was a real eye-opener."
        if alt_day4_sl_cl_tut_iz:
            "Somehow, without using a flashlight, I managed to get this far, to move this long."
        th "I guess the blow to the head shifted my cones and sticks, now I have night vision."
        "I grinned."
        play sound sfx_table_hit
        "And then I kicked the root of a pine tree out of the ground."
        "And it wasn't there five minutes ago, I'm sure of it!"
        if not alt_day4_sl_cl_tut_iz:
            "The moonlight was becoming insufficient, so, hissing curses, I took a flashlight out of my pocket and turned it on."
        "Not that I was complaining, but I was beginning to get tired of this night walking."
        th "Another ten or fifteen minutes and I'm walking back."
        "I think I was the victim of a prank, as it usually happens when a rookie is sent out to find a tent in the woods."
        "And there isn't one."
        stop music fadeout 3
        "Fortunately, five minutes later, my 'tent' was discovered."
        "The trees parted, exposing a large clearing, in the very center of which was a large, crooked building."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_sl_cl_old_camp:
    scene bg ext_old_building_night with diam
    play ambience ambience_old_camp_outside fadein 3
    play music music_list["sunny_day"] fadein 5
    "It was surrounded by what with a modicum of imagination could be called a children's playground."
    "Judging by the concrete blocks scattered here and there, the building had once been surrounded by a decent wall, designed not so much to protect the pioneers from a hostile environment as to defend the hostile environment from the pioneers."
    me "That's it? The whole camp?"
    if alt_day4_sl_cl_lf_solo == 1:
        "Foolishly, I asked the emptiness around me."
        "With the girls, wherever they were headed, we successfully parted ways."
    else:
        show sl normal pioneer with dissolve
        sl "Well!"
        me "What? It's only two floors, the size is small, how many people will move in here?"
    if alt_day4_sl_cl_lf_solo == 1:
        "It was hard to believe that in the olden days the squads were smaller than they are now, when twenty to fifty men might well have been under a counselor."
        "So the pioneers either lived in easy-mounted barracks... Not our case, nothing more permanent than temporary arrangements existed in the Soviet Union."
        "If they were putting up temporary buildings here, they might as well have outlasted the capital buildings."
        "So the kids were put up in tents?"
        "I wonder if any of those kids are alive now."
        "It was kind of creepy and uncomfortable to look at the half-decomposed corpse of someone's childish happiness."
        scene bg ext_old_building_night_moonlight with flash
        "There was not enough moonlight to get my bearings, so I had to wade on the Russian willy-nilly."
        "But it was enough for the atmosphere!"
        "The shabby building was instantly transformed into an ominous haunted house."
        "Or the lair of a fearsome maniac."
        "In short, the perfect backdrop for a horror movie."
        "Now, let's add a little more drama."
        "We'll replace the sandy path with bloody streaks; the rocks on that carousel do a very good job of mimicking human skulls."
        "The twinkling eyes from under the porch."
        "And..."
        $ renpy.show("bg int_looney_bin_nightmare_7dl", what = Noir("bg int_looney_bin_nightmare_7dl"))
        play sound sfx_ghost_children_laugh
        th "I didn't order that one!"
        "The ghostly children's laughter sounded too naturalistic, even my Hitchcock-hardened imagination wasn't ready for it."
        "Yes, and these beauties..."
        scene bg ext_old_building_night_moonlight with diam
        "With a shudder, I shook my head and dispelled the illusion."
        th "I'll scare myself some more later, if I'm in the mood."
        "I consoled myself."
        th "I'll just find a bespectacled man, and then we'll see."
        "Maybe the impressions I've had are enough for me."
        if alt_day4_sl_cl_tut_iz:
            "Especially since it's dark, way too dark."
        "Treading carefully in the very middle of the semi-overgrown path, I approached the building itself."
        play sound sfx_open_metal_hatch
        "There was a nasty creaking sound behind me, and I jumped up and turned around."
        "Okay, it was just a merry-go-round."
        "But now..."
        "When I turned back to the door, there was an absolute darkness staring back at me from across the doorframe that no light source in the world could dispel."
        play sound sfx_metal_door_handle_rattle
        "You know what I think about this?"
        if alt_day4_sl_cl_tut_iz:
            scene black with fade
            "I don't think I'm going to be the hero of this horror picture!"
            "I turned around and, showing the old camp my back, gave a shove."
            $ alt_day4_sl_cl_lf_solo = 2
        else:
            menu:
                "Rest in peace, dear four-eyed pioneer":
                    $ alt_sp -= 1
                    $ karma += 10
                    "And I'll get my revenge for you later."
                    "I turned around and, trying to look independent, headed back to camp."
                    "I could hardly do it - every minute I was near that damn house had given me such an adrenaline rush that I had to run and run to camp now!"
                    $ alt_day4_sl_cl_lf_solo = 2
                "Shurik, if you're not here…":
                    $ alt_sp += 1
                    $ karma += 20
                    stop ambience fadeout 2
                    th "Say your prayers, glasser, you're in for a world of pain."
    else:
        show un normal pioneer at left with dissolve
        un "The camp itself was all around."
        "Patiently, like to a retard, Lena explained to me."
        un "This building is an administrative building, no one lived here."
        me "And then where..."
        sl "Don't you understand?"
        show sl serious pioneer with dspr
        "Slavya shook her head."
        sl "Tents!"
        me "Really?!"
        sl "What's wrong?"
        me "What kind of camp is this, with tents?"
        un "It's just a pioneer camp.{w} My dad came here twice.{w} They lived in tents, had lunch there."
        show un smile pioneer with dspr
        "She pointed her hand to a concrete platform with a row of semi-overgrown pits around the perimeter."
        un "There used to be a overhead hang here, and under it long benches with tables, where the pioneers ate."
        "Quietly smiled Lena."
        un "And dad."
        un "Now."
        show un normal pioneer far at cleft behind sl with dissolve
        "She went to the merry-go-round and, looking for it, pulled out a bottle of opaque black and blue glass."
        un "A package.{w} To the future."
        "She covered her eyes and read from memory:"
        un "Hello! {w} I am Anton, but my friends call me Tohal, and you, who opened this bottle, are now my friend too!"
        un "So don't even think about forgetting me! {w}It's a damn pleasure to meet you, my friend, and remember, I'll always be glad to see you.{w} If you want to chat, come on in."
        un "And then the address where he and I live."
        show un cry_smile pioneer far with dspr
        un "That's how he found Mom..."
        "She whispered, and her eyes sparkled wetly."
        me "Really?"
        un "Yes."
        me "He must've been a hero? A firefighter rescuer?"
        show un smile2 pioneer with dspr
        un "No, just an engineer."
        un "But he always liked to lie."
        un "He won my mother over by showing up at the windows in a suit and a carnation and a Writers' Union card."
        un "He told my mother he was in the paratroopers and would soon be leaving for Afghanistan."
        un "She believed him, of course, and six months later they were married."
        show un laugh pioneer with dspr
        un "We still have those documents."
        un "{i}Anton Tikhonov, the pooblishur, the writors' union.{/i}"
        un "He hand-drew them himself, and when it came out, it was too late, wedding preparations were in full swing."
        un "So he lived with mother until he was thirty."
        un "But nothing now, graduated from police school, working."
        show un shy pioneer with dspr
        "She blushed a little again and hid the bottle back under the carousel."
        "I still didn't understand what the hidden meaning of camping with the tents was?"
        th "Why? You could just as easily pack a backpack, jump on the electric train, and slam out a bivouac a few hours later somewhere totally savage, with no rules or regulations."
        "And this is camp. {w} There are routines."
        "I imagined sleeping in my tent and being woken up at seven in the morning for exercise."
        "What a nightmare."
        "Slavya, I think, got tired of waiting and headed for the administration building."
        show sl normal pioneer far at cright with dissolve
        sl "Let's go!{w} We still have to look for Sasha."
        "She called."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_sl_cl_old_camp2:
    scene bg int_old_building_night with dissolve
    play sound sfx_open_door_squeak_2
    play music music_7dl["nowyouseeme"] fadein 3
    "The creaking of the door seemed very, very creepy in the sinking darkness."
    if alt_day4_sl_cl_lf_solo == 1:
        "Yes... Full pants of adrenaline."
        "Well, you can stand on the doorstep for a long time, but they say it's rude."
        me "Evening in the hut, sussies."
        "Foolishly I bowed from the doorstep, miraculously missing the rusty nail sticking out at my forehead level."
    else:
        me "Hey, wait!"
        un "Yeah, wait for us!"
        "We jogged to catch up with the activist and rejoined her."
        "At one point a board went under my foot unpleasantly, and Lena supported me under my elbow, for which she received an appreciative look.{w} Not like the activist - she shined her flashlight and went further into the building."
    me "Shurik, hello?! Are you there?"
    "The old building looked eerily familiar."
    "The porch, from which two paths diverged in different directions, two paths."
    "To the left, without going into the back rooms, was the director's office, and immediately beyond that, through a nook with an exit to the secondary porch, was the path to the radio operator's office."
    "To the right the insulated sector and dryers for winter clothes - huge such netted rookeries, on which far more often chanterelles and butterflies were sunbathing than really wet clothes."
    "Maybe there's a rational explanation for that."
    "I don't know. {w}There's a typical development, I've seen one - I've seen it all, the way it is with the chruschevk apartments."
    "My old camp had a strikingly similar administration building.{w} Even the crooked staircase leading to the second floor was the same."
    "Except it was painted a different color, and there was a big window there from some unknown source, giving some light."
    "Or?.."
    "I stepped closer and regretfully stated that it was not a matter of design."
    "The construction itself, the plaster-covered wooden slats, was deeply flawed."
    "This is how barracks were built, temporary dwellings for the most stubborn urbanites who didn't want to settle in separate houses while the sky was scratched by yet another ugly twelve-story ship."
    "And here's a children's camp.{w} I'm still surprised it's been standing this long."
    if alt_day4_sl_cl_lf_solo == 1:
        "I probably won't go upstairs; if Shurik were there, he'd have heard me by now."
        "But I think I'll visit the radio room with a revision - where should our dusky genius be but there?"
    else:
        show sl normal pioneer with dissolve
        sl "So, I'll look upstairs and you guys look down here, okay?"
        hide sl with dissolve
        "I nodded and, indicating to Lena the direction in which I was going to conduct the search, set off in the direction of the camp director's office."
        "Accordingly, she got the dryers and the insulated section."
        "I hope some nasty thing doesn't happen to her there."
        "For some reason I wasn't worried about Slavya."
        "I had the impression that this girl would not get into trouble. {w}She doesn't get into trouble, she just doesn't."
        "Not like us. {w}Losers."
        play sound sfx_wood_floor_squeak
        "That's why I wasn't surprised by the frightening crack on the other side of the building.{w} I expected it."
        un "I'm all right!"
        "Shouted Lena."
        un "There's a board cracked!"
        "Let's keep looking, then."
        me "Slavya, how are you?"
        sl "I have nothing yet."
        "The girl upstairs called out."
        "I see.{w} Looks like the first mover's right goes to the auditorium again?"
    "The door to the Camp Chief's office was painted brown, and, judging by the geologic cut of the paint, not even a tenth coat over the previous beige, white, and sickly salads."
    play sound sfx_open_door_squeak_2
    pause(1)
    scene bg int_old_building_cab_night_7dl with dissolve
    "There was a thick layer of dust on the floor, which had apparently accumulated only because the local pioneers were not too keen on vandalism."
    "Ours would have cracked all the glass long ago, which means no dust, no preservation."
    "In the closet next to the monumental remains of the desk, I managed to find several scrapbooks from different years."
    "The paper was grayed from old age, in some places torn simply under its own weight, but that didn't stop me from escaping for a few minutes into the land of dreams, into someone else's history."
    "That's right, because someone else's story is always much more interesting than your own, even if you don't have time to catch your breath on an adventure."
    if alt_day4_sl_cl_lf_solo == 1:
        "One thing I don't understand is why I do all these feats in the first place."
        "Is it for the banal «thank you»?"
        dreamgirl "It's more about bragging about it later!"
        th "Doubtful incentive, don't you think?"
        dreamgirl "To rub that upstart's nose in it? More than enough."
        th "To find Shurik, score some points, and send the counselor away, would that make us the heroes of the day?"
        dreamgirl "So that Buzzard can kiss your nose afterwards!"
        th "Holy crap!"
        dreamgirl "Oh. If it's so untrue, why are you so overreacting?"
        th "Fuck you, you know where!"
        dreamgirl "Shit, come on! You don't want Juju, then Electronik will kiss you!"
        th "I wouldn't expect anything else!"
    else:
        "And to make sure - yes, indeed.{w} Around the big building, like chickens round the henhouse, huddled the tents, grouped in troops."
        "It was a strange sight - a finished administration building, a flagpole with the flag of the USSR, the camp and the squadron on duty, a small barrack with mugs - and that was it."
        "The rest of the infrastructure was canvas stretches, awnings, and the like."
        "After searching for a few minutes, I also found a picture of a kitchen - a marching, soldier's kitchen."
        me "Well, at least it's not a campfire."
        "Amazing picture!"
        "But I have to admit, there was something in it all!"
        "Yes, and the structure came out... Self-sufficient."
        show sl normal pioneer with dissolve
        sl "How's it going?"
        "I shrugged."
        me "It's not."
        sl "Then what are you doing here?"
        show sl serious pioneer with dspr
        "I lifted the album in front of me."
        me "Engaging with history."
        show sl angry pioneer with dspr
        sl "Instead of searching?"
        "Slavya didn't seem to like it very much."
        me "Mixing."
        me "It's strange that they just left them here. {w} Still a memory.{w} No?"
        un "There's a very bad story connected to this place. So..."
        me "I didn't know modern pioneers were superstitious.{w} After all, we're in the 'englightened' age."
        "I couldn't resist saying something."
        show sl serious pioneer with dspr
        sl "You know, you shouldn't joke about these things!{w} Science hasn't explained everything yet."
        me "The saddest thing is that science hasn't explained where Shurik went."
    "I angrily kicked the remains of the table. They squeaked and fell backwards, hitting something with a peculiar metallic clang."
    me "Alright..."
    "Walking around the perimeter of the debris, I scattered the interfering pieces with the toe of my sandal."
    scene cg d4_hatch_night_7dl with dissolve
    me "What do we have here?"
    "The flashlight's light picked up some kind of rectangular spot out of the recluse."
    th "Looks like... Yeah."
    "Also paint, also peeling from old age."
    "But unlike the door, there was metal, and on the right hand was a handle - similar to what they usually make in manholes and basement doors."
    me "A hatch."
    "It was a matter of a couple of seconds to get a flashlight under the handle hanging there in the technical opening."
    if alt_day4_sl_cl_lf_solo == 1:
        me "I'm going to regret this."
        "With a sigh I concluded."
    else:
        me "Girls, take a couple of steps back, or else."
        "The girls obediently stepped back."
    "And…"
    "Bang{w=0.3}{nw}"
    extend "-ding{w=0.3}{nw}"
    play sound sfx_fall_metal_door
    extend "-ow!" with vpunch
    "The hatch that opened surprisingly easily rumbled so that it rumbled in my long-suffering head."
    "Bounced off the floor and rumbled."
    scene cg d4_hatch_night_open_7dl with dissolve
    "In the light of the flashlight you could make out a three-rod staircase leading somewhere into the darkness."
    me "How I don't want to go down there, oh how I don't..."
    if alt_day4_sl_cl_lf_solo == 1:
        dreamgirl "You know it's never too late to bounce back."
        dreamgirl "But don't forget - rub your nose, prestige, heroism."
        me "With a shield or on a shield."
        "I took the first step."
    else:
        un "Stay out of it."
        "Lena agreed."
        un "Let's just remember this place and tell the counselor."
        me "Yeah, and there's Shurik, and he's..."
        un "What?"
        me "It's scary to think about."
        "I snapped."
        "Slavya watched us with the soft smile of a mother watching her unreasonable children quarrel."
    stop music fadeout 3
    pause(2)
    me "Here comes the trail."
    "The lantern picked up the print of a sandal in the dust."
    "Someone's been here, and has been recently."
    "That's where we're going, then."
    "Thanks, Cap."
    if alt_day4_sl_cl_lf_solo == 1:
        scene bg int_catacombs_entrance with diam
        "Just in case there were footprints in the other side I flashed that way - and I walked briskly in the direction of the footprint."
        "The surface of the black, bottomless water glistened wetly on the other side of the stairs - it looked like the tunnel had begun to erode, and in some places the groundwater had already broken its way out."
    else:
        sl "I'll go first.{w} I'll light it up for you."
        "We nodded in agreement, and Slavya disappeared down the stairs."
        me "I'll catch you now, if anything."
        "Lena looked at me strangely, but didn't answer anything and nodded silently."
        sl "I'm downstairs, come on down!"
        me "Well, good luck? See you at the morgue?"
        "I stood on the first step.{w} It held my weight with confidence."
        sl "Just be careful, the last step's a bit loose."
        me "I see."
        scene bg int_catacombs_entrance with diam:
            linear 0.2 pos (0,50)
            linear 0.2 pos (0,0)
        "Two more minutes and we do a cursory audit of our condition.{w} Everything seems to be in place, everyone is alive and well: I am sick, Slavya smiles, Lena is embarrassed.{w} Modus vivendi."
    play music music_7dl["dead_silence"] fadein 3
    play ambience ambience_catacombs fadein 3
    "It was dark in here, like... like a basement.{w} I wouldn't say it was a basement, though."
    "It looked more like a tunnel of some kind.{w} A digger's paradise, with thick wires and wicker lamps and a vaulted ceiling in the supporting hooks."
    "Soviet-style inquisition cells.{w} But you could see that they were built with heart and conscience - despite the disrepair, everything here looked sturdy and solid, if only a little dusty."
    "It wouldn't do any harm to change a light bulb somewhere."
    "Because working light bulbs were so rare here that I rejoiced at each one like a good acquaintance."
    "In spite of their unsightliness, dusty, running at half a watt of twenty."
    "I didn't feel comfortable in these dark tunnels leading from nowhere to nowhere-allegories with light at the end came to mind."
    me "I hope these tunnels don't lead to a 'shoot yourself before entering the area' type facility."
    if alt_day4_sl_cl_lf_solo == 1:
        "I mumbled to myself just to somehow break up the frightening, strolling echo of footsteps."
    else:
        show sl laugh pioneer with dspr
        sl "You grumble like an old grump."
        "Slavya laughed."
        "She didn't seem to be impressed by the oppressive mood of the underground utilities."
        sl "Look, that's where we're going."
        "She shined a light on the floor - a string of footprints led off into the darkness."
    "I imagined going deeper into that darkness, surrounded on all sides by a thickness of rock and concrete, and I involuntarily cringed."
    "And if at some point my flashlight goes out... {w}No, better not even think about it."
    "You'd think a man living in a box would be claustrophobic."
    if alt_day4_sl_cl_lf_solo == 1:
        "One way or another, I tried to leave some kind of residue behind me."
        "Most of the time it was just a simple dusting of certain areas."
        "After half an hour's journey, I'd just run my finger over it."
        show blackout_exh2 with fade2
        "And after another half hour, I was down in the dumps and waddled onward, occasionally hitting the hooks with my shoulder."
        "The dusty carriers still gleamed when I wiped them."
        "And I sang, of course. Of course I did."
        me "There's a ruined briiiidge in London, there's a ruined briiiidge in London."
        "What I wanted more than anything right now was to just drop everything and go back."
        "I was underground for more than an hour."
        "And just as I was about to turn around and go back, something unusual caught my attention."
    else:
        me "So there won't even be a classic left-right?"
        show sl normal pioneer with dspr
        sl "We've got tracks."
        "Slavya shrugged."
        sl "Let's go faster, maybe he needs help!"
        me "I hope he hasn't gotten far."
        show un serious pioneer at left with dspr
        "Lenka snorted in solidarity behind my back."
        me "Or we're looking here, and he's already in the cabin."
        sl "Semyon, stop suffering.{w} You want to go back? Go, I'll send Lena with you."
        me "Ah..."
        sl "Yes, and I'll look myself.{w} I'm not going to the camp without Shurik."
        me "But Olga Dmitriyevna said only to the old building and back.{w} Aren't you afraid of getting hit in the head?"
        sl "Better in the head than to know that I could have helped and didn't!"
        show sl serious pioneer with dspr
        "She flashed her eyes angrily and turned away."
        un "You can't help everyone."
        "Looking under her feet said Lena."
        "We walked in silence for a while, sulking at each other.{w} That is, Slavya and I were sulking, and Lena was habitually already diligently shy."
        sl "Wow."
        "There was a sound of respect in the girl's voice, and I was distracted from balancing between the wreckage and the cracks in the floor."
    "So, esteemed audience, I offer to your attention..."
    "The door.{w} No, not like that."
    "{b}THE DOOR!{/b}"
    stop music fadeout 3
    scene bg int_catacomb_door_fullbright_7dl
    "As if it's been transported here straight from Vault 111."
    "It's just as heavy, big, solid. {w}Except it's not round."
    "As if in spite of all those serious buttons, anti-vandal hinges, and a huge pivot wheel, the door was painted a cheerful blue color, over which a threatening yellow stencil sign of radiation danger had been applied."
    me "I guess you can't open that door by yourself."
    play sound sfx_metal_door_handle_rattle
    "I tried to turn the wheel - with the expected result."
    if alt_day4_sl_cl_lf_solo == 1:
        "But somehow Shurik came through here."
        dreamgirl "I have a suspicion that the door was open before him."
        th "What am I supposed to do, go home empty-handed?"
        dreamgirl "No. Why should you?"
        dreamgirl "Let's pretend there's two of us."
        me "Yeah, me and my split personality."
        dreamgirl "You know, if I had a chance to help you, everything would happen."
        dreamgirl "Although you would've gotten beaten to shit before."
        th "Don't screw around, tell me what to do."
        dreamgirl "Yeah, look to the right, under the shield with another OBJ-mention."
        th "Stick. And?"
        dreamgirl "Yes, dear. But that's okay. You have a whole bunch of other virtues."
        "I exhaled and counted to ten."
        dreamgirl "That's right. Calm down or something will happen."
        dreamgirl "So, I explain for the particularly gifted, you take the rod from under the shield."
        dreamgirl "Then you gently lift it in your arms like a bride."
        dreamgirl "And fix it, so that it presses the button!"
        th "And twist it yourself? Hmm. Curious technology."
        "The next ten minutes were filled with swearing, splintering, and a burning desire to quit the hell and go home."
        play sound sfx_open_metal_hatch
        "But finally, the primacy of twenty-first-century human intelligence over local natives was proclaimed, and the locking wheel spun."
        play sound sfx_metal_door_large_close_basement
    else:
        show un normal pioneer with dissolve
        un "Then what about Shurik?"
        me "How should I know?"
        show sl normal pioneer at left with dissolve
        "Slavya, instead of answering, highlighted the imprint of a sandal at the door itself."
        me "Maybe it was open."
        me "Anyway, we have to go that way.{w} Let's try this..."
        "Just in case, I tried turning the wheel again."
        "It went just as well."
        me "I'll have to have one of you push the button."
        hide un with dissolve
        "With a glance, the girls resolved this dilemma among themselves, and Lena took another step back."
        "Slavya, on the other hand, walked over to the locking button and examined it curiously."
        show sl serious pioneer at right with moveinright
        sl "Should I press the black or the red button?"
        me "Red, of course.{w} Black is for other purposes."
        me "Come on, three-four. {w}Three..."
        play sound sfx_metal_door_large_close_basement
        "Something inside the door clicked, rattled, and I started to turn the wheel - Slavya let go of the button with a gasp."
        "The backward motion nearly broke my hands from my joints."
        me "Hey, be careful! I almost dislocated my arm!"
        sl "Sorry, I think there's a..."
        un "A bug?"
        show sl shy pioneer with dspr
        "Lena retreated even farther, frightened."
        "Soon she'll reach the camp with her back to the front like that."
        sl "No.{w} I don't know.{w} There was something moving under the button."
        "Oh, man.{w} In the dark with a flashlight, so we climb fearlessly, and when something moves somewhere, we squeal and run away? Blonde logic."
        me "Afraid someone's going to bite? Here."
        "I picked up a round rebar stick from the floor and held it out to her."
        me "Use this, Luke."
        sl "Yes, thank you."
        me "Three..."
    "This time everything went off without a hitch."
    if alt_day4_sl_cl_lf_solo == 1:
        "At one point, though, I heard some rustling from the side of the buzzer box."
        "I suspected that some creep had made a nest inside it, and I had disturbed it."
    else:
        "True, I soon heard a threatening hiss from Slavya too, but she, though pale, didn't blink an eye and kept the button pressed exactly as long as it took to open the cremallers and unlock the door."
    play sound sfx_metal_door_large_close_basement
    "And now"
    stop music fadeout 3
    stop ambience fadeout 6
    $ persistent.sprite_time = "sunset"
    scene bg int_catacombs_living
    show cotocomb_lighter
    with flash
    play ambience music_7dl["ambience_safe"] fadein 3
    if alt_day4_sl_cl_lf_solo == 1:
        extend ", a miniature hermit's paradise appeared before my eyes."
    else:
        extend ", a miniature hermit's paradise came into our view."
    "A fully staffed, fine-tuned and frighteningly self-sufficient system."
    if alt_day4_sl_cl_tut_iz:
        "Frighteningly similar to the one I saw in my dream today."
    "But judging by the atmosphere of disrepair, the last time guests had been here was about twenty years ago."
    "A bunk bed with a thick layer of dust - demonstrating that it had never been slept on, a radio operator's corner, and individual lockers, one of which was open."
    play sound sfx_radio_squelch_1
    "What's amazing is that there was still electricity!"
    "Even the ventilation systems - clumsy, Soviet-made - buzzed palpably from under the ceiling."
    "But there was no elusive spirit inherent in human rooms."
    "Shurik wasn't here either."
    if alt_day4_sl_cl_lf_solo == 1:
        "My attention was drawn to a flashlight lying derelict on the table."
        "It's a nice one; in my day it was called a 'police flashlight,' for it had all the characteristics of a rubber police democratizer."
        "A source of light and a weapon in the same bottle, isn't that bad?"
        "I grabbed it instantly, checked the switch just in case-and it didn't light up as expected."
        hide cotocomb_lighter with dissolve
        "That's all right."
        "That's the one thing that can be fixed."
    else:
        show un normal pioneer at right with dissolve
        un "Look what I found!"
        hide cotocomb_lighter with dissolve
        "Lena picked up a heavy Soviet flashlight from the table, not unlike the toy that was buzzing in Slavya's palm."
        "If you get hit in the forehead with one of those things, you can't be too stupid."
        "Lena flicked the switch, but the flashlight didn't even flick on."
        if loki:
            me "You're such a mess! Before you can find the thing, you've already broken it!"
            show un shy pioneer with dspr
            show sl serious pioneer at left with dissolve
            sl "Semyon, stop bullying Lena."
            me "I'm sorry, Mom. She started it."
            hide sl with dissolve
            "I grinned and, taking the flashlight from the girl, walked away to the crates."
        else:
            un "Eh, such a useful thing it could have been."
            "She sighed."
            me "Give me that."
    "Not that I'm much of a tech geek, but anyone can change the parts in a Soviet flashlight."
    "Especially since a place like this is bound to have spare power sources."
    "So it is - a couple of minutes of searching later I was rewarded with a box of batteries and a pack of spare bulbs for the flashlight."
    play sound sfx_radio_squelch_2
    if alt_day4_sl_cl_lf_solo == 1:
        "A couple of minutes later I was armed and with a light."
        "It seemed trivial to just see where you were going and what you were doing."
        "And psychologically it's already much more comfortable."
        "The overpowering bulb gave a steady cone of bright white light."
    else:
        "Three minutes of twisting and untwisting, and after checking the light{nw}"
        extend ", and in the process almost going blind in my left eye, I handed the flashlight to Lena." with flash
        me "Own and remember my kindness."
        show un smile pioneer with dspr
        un "Thanks."
        "Hiding her eyes, she replied.{w} She seemed to feel a little guilty about not taking part in the exciting attraction called «open the bomb shelter door»."
        hide un with dissolve
    me "Obviously, Shurik is not here.{w} It's silly to look under the bed."
    if alt_day4_sl_cl_lf_solo == 1:
        dreamgirl "But just in case, look there!"
        dreamgirl "Maybe there's a beautiful girl in a short dress waiting for you."
        th "Unless she has a ponytail."
        "I grinned."
    else:
        show sl normal pioneer at left with dissolve
        sl "Yes!{w} We're moving on."
        me "Further? Isn't that..."
    "Bomb shelters were usually made in blind cul-de-sacs - it made it easier to solve some of the engineering problems with ventilation and power supply.{w} But here..."
    "I turned my attention to the second door."
    "This door was an absolute twin to the one that let us in here.{w} So no comment was necessary, but I reminded just in case:"
    if alt_day4_sl_cl_lf_solo == 1:
        me "Stop the button, then turn it."
        dreamgirl "Good! {w}You'll go far!"
        "This button was much easier to lock - especially since I had some tools on hand, too."
    else:
        me "Let's do it again, you on the button, me on the cremallers."
        "In light of reflection, recent events, and this whole thing in general, I suddenly realized that it didn't matter now where or why I was going."
        "It didn't matter if we found anything."
        "I found myself in a paradoxical hypothetical situation that I had never believed existed - a moment in which the process was more important than the goal itself.{w} The very fact of the adventure was more important than the result of the search."
        "And the thanks for creating this paradox go to the direct, sweet and very beautiful girl with the unusual name."
        me "No one in there?"
        "Slavya politely tapped the buzzer and shook her head negatively."
        sl "Then, three... Sixteen."
        "She jammed the button and I turned the spinning wheel."
    play sound sfx_metal_door_large_close_basement
    $ persistent.sprite_time = "night"
    scene bg int_catacombs_entrance
    show d4_cat_door_frame
    with dissolve
    th "Motivating, I'll say."
    if alt_day4_sl_cl_lf_solo == 1:
        me "Don't go crazy, it's just a tunnel in the image."
        "Don't bring up non-Euclidean spaces and Klein bottles."
        "There is no such thing as closed topology."
        "I repeated those words like a prayer again."
        "Because I was in dire need of stable reference points."
    else:
        show sl scared pioneer at cleft
        sl "It feels like we're back in the same corridor."
        "Slavya whispered."
        "She didn't seem to feel comfortable. {w}And I totally shared her feelings!"
        "The trail, however, led this way, so we had no choice."
        show un normal pioneer at cright
        un "Well, shall we go?"
        "Armed with a flashlight, on the other hand, Lena felt excellent and was raring to go!"
        me "Late for something?"
        "I winked."
        un "Let's find Shurik and get back to camp! {w} I've had enough of these dungeons!"
        show sl laugh pioneer
        show un laugh pioneer
        with dissolve
        "As they looked at each other, the girls laughed their heads off, leaving me puzzled."
        "I shrugged."
    if alt_day4_sl_cl_lf_solo != 1:
        scene cg d4_sl_dnd_7dl with dissolve
    else:
        scene cg d4_catac with dissolve
    play ambience ambience_catacombs fadein 3
    "And took the first step into the new corridor."
    "Apparently, that's how it was originally built - a bunker and two tunnels in different directions."
    if herc:
        "There were no landmarks, but I tried to get a rough idea of where and what."
        "It turned out that the right spur, where the path led from the surface, was straight as a gut from the old building, roughly parallel to the fence, so that the bunker was somewhere just south of the road leading to the district center."
        "And the left spur, this one here - I looked in the direction - should have led straight under the river.{w} Ohohohoh, there ain't no way I'm going there."
        "In St. Petersburg, while I ride the subway, every time I feel extremely uncomfortable when the train goes from the right bank to the left bank under the Neva."
        "And here we have no speed, no depth."
    else:
        "A dead place in the middle of nowhere."
    "Anyway, anything happens and it's going to be very, very sad."
    if alt_day4_sl_cl_lf_solo == 1:
        me "Phobias come out again."
        "Where is good Dr. Viola and her magic powders?"
        "I've been fighting off piling nightmares like wall-constriction, tunnel flooding, or shale gas coming in from the nearest breach as best I can."
        "And for all my nightmares, I almost fell into another hole that turned out to be a lot bigger than I expected."
    else:
        sl "You've gone quiet, Semyon."
        "Slavya broke the silence."
        "She moved forward, followed by Lena, this time also armed with a flashlight, shining on her left hand."
        "I, on the other hand, moved to the rear, feeling sideways."
        "After hesitating, I still decided to share my thoughts."
        un "I've heard about these tunnels."
        "Lena, now walking ahead of me, replied."
        un "They were built in the late forties, but before that time there was coal mining on that shore."
        un "So if any water seeps in, it goes deep, it doesn't flood the premises."
        me "And how do you know so much about geology..."
        "I grumbled."
        un "I read a lot."
        "Grinned the girl."
        un "Stop."
        "She braked sharply and grabbed Slavya by the belt."
        "Just in time-just one more step, and..."
    scene bg int_catacombs_hole
    with diam
    "There was a noticeable hole in the floor.{w} You couldn't even try to jump to the edge of that hole."
    if alt_day4_sl_cl_lf_solo == 1:
        "I gave it a close look, though, just in case."
        "Useless."
        "I think the rocks came down there - the far edge of the corridor was plugged up tight with earth and concrete debris."
        th "I'd have flown in there..."
        "Feeling a chill climb between my shoulder blades, I concluded."
        "Something glistened below."
        th "Not water, I hope?"
        "Another attempt to get me in the water caused nothing but annoyance."
        "But a couple of seconds later I guessed it was a metallic glint, from a bent iron... From the railroad tracks!"
        dreamgirl "Well, come on down and let's see what the local dwarves have been mining!"
        "I sighed."
        "Any path you take is divided into two parts - the way there and the way back."
        "And if now - four hours later - I'm still going one way, and getting deeper at that..."
        "Yeah, I wish I could finish my journey by the end of the week."
    else:
        me "Those same mines?"
        show un normal pioneer at right with dissolve
        "Lena nodded and shined the light downward.{w} The spot of light picked out a pile of rubble from the gloom, and the metal rails gleamed dimly a little farther away."
        un "The ground must have eroded, so the whole thing collapsed."
        "A spot of light ran around the perimeter of the hole, picking out a promising mound of earth in the middle."
        "Not very deep, a meter and a half or two, if you jumped well, no risk."
        me "Shurik must have jumped down here. {w} We'll have to follow him."
        show sl normal pioneer at left with dissolve
        sl "Do you want to keep going?"
        me "No. {w}But I guess it takes longer to walk back than it does to walk in the right direction."
        show sl smile2 pioneer with dspr
        sl "And also in the name of the heroic rescue of a comrade!"
        "I smiled with lips."
        "Such things are supposed to be said with a thick, thick layer of sarcasm over the line, but the activist seemed to seriously believe what she was saying."
        me "All right, I'll be the first to insure you.{w} Light me up."
        "The powerful spot of light was joined by a slightly dimmer spot. {w}A flickering, flickering one - the cost of a mechanical flashlight."
        "But more important was the moment of psychological support."
        me "Break a leg for me."
        "I crossed myself sprawlingly and, sitting on the very edge, carefully slid down, marking where I could make out another distinct imprint."
    scene black with fade
    play sound sfx_simon_fall_1
    pause(1)
    "I think I..."
    stop music fadeout 3
    stop ambience fadeout 2
    "Eh?"
    "The light is gone somewhere, and all I had left"
    play sound sfx_simon_fall_2
    extend " — was the eerie sensation of soil crumbling beneath my feet."
    "Before I even had time to get scared, I went tumbling down."
    play sound sfx_fall_wood_floor
    scene bg int_mine_crossroad with diam
    "I landed on all fours, hitting the proverbial rails with my palms very painfully."
    play ambience ambience_catacombs_stones fadein 3
    if alt_day4_sl_cl_lf_solo == 1:
        "Nearby, with a clang, something heavy but small landed."
        scene black with fade
        "And darkness came."
        "And as if to signify that trouble does not come alone..."
        "I barely made it out of the way."
        "Barely visible in the emergency lighting, the piece of concrete I was holding on to, trying to slow my fall, swayed and slowly began to fall."
        play sound sfx_fall_metal_door
        me "Well. {w}It looks like the way back is closed for good."
        "There's nothing to do, I guess I'll just have to keep moving forward and hope that somewhere will bring me to the surface."
        "The flashlight I lost during the fall wasn't found right away, and those were probably the longest minutes of my life."
        "But all ended well."
        "I had the light and the strength and the desire to find and punch Shurik in the face again."
        "Or at least go back to camp."
        "I looked around."
        scene bg int_mine
        with flash
        "I could see the very beginning of the mine tunnel, judging by the wooden bracing, old and not very rich."
        "The way back was blocked by a pile of rubble."
        "I tried to climb up and see what was there, but quickly moved back down."
        "I could only catch a glimpse of the glare from the water."
        th "Looks like it's flooded in there, too."
        th "If not by the river, then by groundwater."
        "Then we'll have to move forward."
        "I've got a relatively straight notch, trapezoidal in cross-section, a couple of rails, and zero carriages."
        dreamgirl "What a pity! It would have been a breeze!"
        "Well yes, it would have been a good start to exploring the dungeons."
    else:
        "After stomping on the landing spot for a while to make sure nothing collapsed, I stepped back and honked my horn."
        me "You may!"
        play sound sfx_jump_into_hole_2
        "Next to me, Lena jumped right away."
        "I think she's actually batshit insane."
        "You can't dive headlong into the dark just because someone else has done the same thing in front of you."
        dreamgirl "She didn't seem to want to be alone in the dark."
        th "How do you come to that conclusion?"
        dreamgirl "Otherwise, why would she be clinging to you like that?"
        "She was shaking all over."
        me "Lena, you're hurting me."
        show un scared pioneer with dspr
        un "I'm sorry."
        "She let herself be taken a few steps away."
        me "Slavya, jump!"
        play sound sfx_jump_into_hole_2
        show sl normal pioneer at left with dissolve
        show un normal pioneer with dspr
        "At last our team was reunited, and we could begin our search for Shurik again."
        "We all gained a lot of experience, gained a new level, and now we're up against monsters more dangerous than before."
        "And the most vicious of them all is the goggle man."
        show sl smile2 pioneer with dspr
        sl "Last time Lena complained.{w} Now I'm complaining."
        sl "I'm tired and I want to be carried.{w} Please carry me?"
        me "All right. I'll carry you and Lena will carry me."
        show un smile pioneer with dspr
        un "I can't carry you, you're so big."
        "Lena played along, and Slavya laughed."
        "I took the hint right, and we took a fifteen-minute break from looking."
        "Shook off the rails and sat down on them."
    play music music_7dl["nowyouseeme"] fadein 3
    "I never thought that the elementary absence of the sky overhead for a few hours would have such a depressing effect on the psyche."
    if not alt_day4_sl_cl_tut_iz:
        th "Or is it all about the buzzer?"
        th "I don't know."
    "But my head hurt more and more - I didn't complain, but the color of my face was quite eloquent,"
    if alt_day4_sl_cl_lf_solo == 1:
        extend " and wobbly legs meant something."
        "I was getting tired and exhausted."
        "My strength was less and less, it was harder and harder to get up."
        "But I'm not a shaking creature, and I have the right!"
        "So let's go!"
    else:
        extend " judging by how Slavya insisted on resting."
        "But not half an hour later, I was up.{w}Didn't want to sit in this musty atmosphere."
        show un serious pioneer with dspr
        un "Are you holding up?"
        "Lena asked sympathetically."
        me "Lena, tell me, why did you come with us? Don't tell me you were worried about Shurik."
        show un shy pioneer with dspr
        "She blushed and averted her eyes."
        show un scared pioneer with dspr
        un "Well... That's..."
        sl "I asked her, did you forget?"
        "Slavya came to the rescue."
        sl "Even before supper. Since Lena had nothing else to do, she agreed to come with us."
        me "That's it?"
        show un shy pioneer with dspr
        pause(.3)
        show un normal pioneer with dspr
        un "Yes…"
        me "This is all strange. {w}But are we going?"
        "The girls followed me up."
        "It was difficult to navigate this time, for the tunnels were no longer a straight line, but occasionally turned somewhere, crossed one another, and generally behaved ugly."
    dreamgirl "You know, there's an old rule in labyrinths..."
    th "The left-hand rule? I know."
    dreamgirl "Not really. {w}It's more about feeling and sense of direction."
    th "Is it autopilot or something?"
    dreamgirl "Something like that."
    th "Autopilot can't work in unfamiliar places, even kids know that."
    dreamgirl "You won't lose anything if you try it."
    dreamgirl "You're going to explore the backstreets anyways while you look for Shurik."
    menu:
        "No experiments!":
            dreamgirl "What a fool!"
            $ alt_sp -= 1
            dreamgirl "Look yourself now, good luck and good wind on your humpback."
            th "Wow, such a grudge!"
            "Silence."
            th "Hey, what's wrong?"
            "Silence."
            "My own inner voice got offended at me."
            "Did someone say «haloperidol»?"
            "I saw a plaque with a strange inscription on the far wall."
            if (alt_day4_sl_cl_lf_solo in (0, 3)):
                sl "Double-you, ay, pi.{w} Semyon, what does that mean?"
            else:
                dreamgirl "Oh, bourgeois letters. WIP. You know what they mean?"
            me "That we're going the other way."
        "Let's try it!":
            dreamgirl "Are you sure? Then stop resisting for a few seconds."
            th "What?"
            dreamgirl "Be quiet. You're in the way."
            "For a while I lost control of myself, my own thoughts - even my body and the movement of my eyelids."
            "It was as if I had fallen under someone else's mental control."
            "Not Sarah Kerrigan, of course, but I seem to have had time to feel the emotions inherent in the experience to the fullest."
            "For a split second."
            "And then time and control no longer mattered."
            scene black with fade
            "The world plunged into darkness."
            "And a few seconds later, burning lines began to thaw out of the darkness, forming squares and crosshairs - as if a map of the area were appearing before my mental gaze."
            show alt_cat_map_wireframe at truecenter with dissolve
            "It was as if I was looking at the dungeon from somewhere above, and with my will I was turning a three-dimensional object into a simple two-dimensional projection."
            show alt_cat_map at truecenter with dissolve
            "The subconscious mind noted the primitiveness of the design, shrugged it off, and plotted a route."
            show alt_cat_map_pathfinding at truecenter with flash
            "I opened my eyes and headed into the darkness."
            if alt_day4_sl_cl_lf_solo == 1:
                "I didn't even need a flashlight - I knew the route ahead thoroughly."
                "Right down to the number of steps between turns, the dangerous places to duck your head, and the possible chasms you'd better step over."
            else:
                sl "Semyon, where are you going?"
                me "We'll rest later!"
                "I shortly answered."
                me "I think I know where we're going."
    scene bg int_mine with dissolve
    "At last, the dungeon tour was over."
    if alt_day4_sl_cl_lf_solo == 1:
        "Almost falling over from fatigue, I went out into one of the nooks."
    else:
        "We haven't spoken for quite some time now, only exchanging brief remarks on duty, warning of danger."
        "Everyone was exhausted."
        "But our troubles have come to an end, too."
    scene bg int_mine_door
    with fade
    me "Variety..."
    "The only thing that managed to be squeezed out of a parched throat."
    if alt_day4_sl_cl_lf_solo == 1:
        me "Shurik, your account is getting more and more into negatives."
        "There was a heavy door right in front of me, even from the looks of it."
        "I went over and pushed it."
        "It stayed in place without even creaking."
        me "Good. So it was built to last."
    else:
        sl "What?"
        me "The door."
        "Thank goodness it's not another explosion-proof one, or I'd definitely think we were somehow magically back in the bunker!"
        sl "Yes, I see."
        me "I hope the adventure ends there."
        me "Very much so!"
        "I yanked the handle with force and opened the door."
    stop ambience fadeout 3
    play sound sfx_open_door_mines
    scene bg int_mine_room
    with dissolve
    if alt_day4_sl_cl_lf_solo == 1:
        "The beam of the flashlight struck the opposite wall of the small room."
    else:
        "Two beams of light crossed over the opposite wall of the small room."
    "I almost stepped on one of the bottles lying in abundance on the floor."
    me "Portwine 72."
    "Confused, I read, picking one up."
    me "So it wasn't the miners or the construction workers who drank?"
    if alt_day4_sl_cl_lf_solo == 1:
       me "Because for the builders of these utilities, much less the mines, the drink is a bit too modern looking."
    else:
        sl "Uh, well, yeah..."
        "Slavya was embarrassed for some reason."
        "But I didn't stress it."
    "I paid tribute to the skill of the unknown cave painters who painted obscene pictures and obscene language on almost every available surface."
    "And from there I concluded that there was a much shorter way to the surface."
    "So there's another way out."
    "Apparently, Shurik, like Stirlitz, left through the entrance."
    "I suppressed the urge to swear at the goddamn bespectacled man and fought the nausea for a few minutes."
    if not alt_day4_sl_cl_tut_iz:
        th "If I'd have known, I'd have sure as hell not agreed to help him."
        dreamgirl "If you hadn't helped him, someone else would have."
    if alt_day4_sl_cl_lf_solo == 1:
        "But how he pissed me oooooff!"
        "I kicked away a row of bottles and sat down with my back against the wall."
        "Not going anywhere from here."
        "Bury me in the green."
    else:
        me "Slavya, Lena, he's gone."
        me "I'm tired and I've given up, bury me under the aspen!"
        show sl normal pioneer at cleft with dissolve
        sl "How about another little break?"
        me "A break?"
        me "Let it be known to you -"
        "The clock on my smartphone showed the beginning of three."
        me "That we've been walking around underground for more than six hours. It's about time we went to bed here and prayed we had enough air."
        "I turned off the screen and tucked my phone into my pocket, ignoring the wild looks the girls gave me."
        "This toy isn't about them, and I'm not going to answer unspoken questions."
        show un normal pioneer at cright with dissolve
        un "That's the one..."
        me "Don't ask."
        un "...which..."
        me "Don't ask, I said."
        sl "What are you talking about?"
        me "You don't ask either. {w} Don't make me lie, I won't say anything of substance anyway."
        "The girls looked at each other, but got away from me."
        "And just in time."
    play sound sfx_steps_clubs_nextroom
    "Another door caught my attention"
    if alt_day4_sl_cl_lf_solo != 1:
        extend " — a kindred sister of the one through which we came here."
    else:
        extend " — faintly familiar."
    "Or rather, not the door itself. But the shuffling footsteps approaching from behind it."
    "Someone was moving purposefully this way."
    th "Whoever you are, pray you're Shurik."
    "Anybody else I'd knock on the forehead with a trophy lantern right now and throw out to be eaten by the local mold on the walls."
    dreamgirl "There's no mold on the walls here."
    th "Yes."
    if alt_day4_sl_cl_lf_solo == 1:
        "I was also sluggishly thinking that it might make sense to make a «rose»."
        "But against whom here might one need to defend oneself with such terrible weapons?"
        "And anyway, how would a pioneer have the skill to fight with a bottle shard?"
    else:
        me "We've got company."
        show sl normal pioneer at left with moveinleft
        show un normal pioneer at right with moveinright
        "The girls reacted in exactly the same way for some reason - they turned and shifted strangely in relation to the door."
        "I could have sworn they were now depicting some sort of defensive formation."
        "But where would peaceful pioneers get that kind of skill?"
    dreamgirl "About the same place as your flashlight-fighting skill."
    th "Pardon?"
    if not alt_day4_sl_cl_tut_iz:
        dreamgirl "I've been cleaning the sludge out of your psyche, and, you know, I see something extremely curious, dated this morning."
        th "What's that?"
        dreamgirl "An implemented set of instructions."
        th "What kind of instructions?"
        dreamgirl "Generally speaking, the destruction of the enemy with bare hands or by improvised means."
        th "You don't mean to say that..."
        dreamgirl "That's exactly what I mean."
        dreamgirl "You've been programmed, dear.{w} And your morning «buzzer» did that."
    play sound sfx_open_door_strong
    show sh normal pioneer with flash
    "Luckily it turned out to be Shurik."
    "Lucky for him."
    th "You have no idea how lucky you are."
    sh "There you are! {w}I heard you walking down the halls, leading me on!"
    sh "Did you think I'd follow you and die in a far corner? But I didn't."
    show sh rage pioneer with dspr
    sh "You thought I wouldn't find you? But I did!"
    "I think he's finally gone insane."
    if not alt_day4_sl_cl_tut_iz:
        "And, if the calculations are to be believed, this very «program» seems to have hit him the worst."
    me "And in vain.{w} If you had walked in the tunnels for a couple of days, if you were hungry, you would have gotten out on your own."
    if alt_day4_sl_cl_lf_solo == 1:
        th "Why is he addressing me in the plural form?"
        th "Is it a spontaneous form of respect or does he know something?"
        dreamgirl "Relax. Only you know about me."
        me "Are you done or am I going to go and you're going to walk around some more?"
        show sh upset pioneer with dspr
        sh "What?.. B-but I-I…"
        me "Listen. I'm very tired, I have a very bad headache."
        me "That's it, I found you, I made sure you were alive. {w}I'm not going to coddle you and tell you to go back to camp-I didn't set out to wipe your snot out."
        me "I'm going home."
        "I turned around."
        me "Suit yourself."
        show sh scared pioneer with dspr
        sh "And… You what? Are you just going to abandon me here?"
        me "Yup."
        hide sh with dissolve
        "I figured out where to head for the exit and staggered to the door."
        sh "Semyon! Wait!"
        me "Yes?"
        show sh serious pioneer with dspr
        sh "You're right, I'm sorry. {w}I don't know what's wrong with me."
    else:
        show sl serious pioneer with dspr
        sl "Semyon, stop mocking Alexander!{w} Can't you see he's not himself?"
        "I shrugged."
        me "I'm not myself.{w} I'm an invalid wounded in the head who's been forced to look for a flawed one on the same head from birth."
        show sl smile pioneer
        show un smile pioneer
        with dspr
        "The girls jumped in sync."
        un "It was cruel and evil."
        sl "But funny."
        show sh upset pioneer with dspr
        sh "What are you talking about, I don't understand?"
        "He shifted his gaze from me to the girls, then back again, confused."
    play music music_7dl["breath_me"] fadein 3
    "A piece of iron fell out of his hand and rattled on the floor, which he seemed to intend to use as a weapon."
    me "Can you explain why the hell you ran away?"
    show sh normal pioneer with dspr
    sh "Me? I didn't run anywhere!"
    sh "When we got out of the club, the voices stunned me."
    show sh cry pioneer with dspr
    sh "And then those voices started yelling, and telling me what to do, and leading me somewhere!"
    play sound sfx_face_slap
    "I slapped him lightly, bringing him to his senses, and got dirty in something wet and sticky."
    "Shurik shrieked and fell silent."
    show sh scared pioneer with dspr
    th "Blood."
    "There were three longitudinal and rather deep scratches on the fugitive's cheek, as if left by a cat's claws."
    me "The hell's that?"
    "He blotted the wound with his finger and wrinkled his nose."
    show sh serious pioneer with dspr
    sh "Blood? When did I hurt myself?"
    me "You're the one who should tell me.{w} It's like you got stabbed by a cat."
    sh "What cat in the mines? That's unscientific."
    "He was saying something else, he was telling me, rambling and jumping from fifth to tenth, but he wasn't getting right down to the most important subject."
    me "Okay, that's all great, of course."
    "I interrupted him when, for the fifth time, he had already gone on with his bagpipes about wandering left and right through the mines."
    me "You tell me, is there a shortcut to the surface here?"
    sh "I remember going into the flooded wing, there was a stairway leading up. {w}You could see the bus stop through it."
    me "A flooded wing, you say?"
    if alt_day4_sl_cl_lf_solo == 1:
        me "Listen to me, my sieve friend: I didn't go through all this trouble to track you down just so you could lead me back the same way."
        me "So think hard, you might even get some help from the audience."
        "I weighed the flashlight in my hand and patted it eloquently in the palm of my hand."
    else:
        sh "I told you, I wasn't myself.{w} I'm not sure I could get you out there."
        show sl shy pioneer with dspr
        sl "Actually, there's a way up behind that door, Boris Alexandrovich told me about it."
        me "And you didn't say anything?"
        show un shy pioneer with dissolve
        un "We really don't seem to be very far from the camp."
        me "Why do you think so?"
        un "Well... I just feel it."
        "She's blushing."
        sl "I feel that way, too."
        "Slavya nodded."
        sl "Can't explain why, just some sense of direction."
        th "Gamer instincts, no other way."
        sh "Let's go back to camp!"
    show sh upset pioneer with dspr
    sh "Looks like something happened to me in the clubs there. {w}Not good."
    me "Not good is an understatement."
    scene cg d4_sh_met_7dl
    with flash
    me "Welcome back to the ranks of the sensible."
    "I held out my hand, which Shurik shook unceremoniously."
    me "And let's get out of here already."
    scene bg int_mine_room
    if alt_day4_sl_cl_lf_solo == 1:
        show sh normal pioneer with dspr
        sh "Semyon, a small request, before we get back."
        me "Yes?"
        show sh upset pioneer with dspr
        sh "Don't tell anyone that I... Well, walked around with a rod."
        sh "I don't have much credibility in camp as it is."
        me "Consider it done."
    else:
        if not alt_day4_sl_cl_tut_iz:
            me "I guess that's your reaction. {w}I just had a headache."
            sl "Semyon, why did you stick your head in there?"
            "Slavya shook her head."
            me "As if it were something bad."
            sl "I told you to wait till lunchtime!"
            me "And I did wait till lunchtime.{w} When everybody went to lunch, I went out."
        else:
            sl "And go straight to the doctor!"
            me "At three in the morning?"
            sl "Semyon, I don't know how to treat these things. {w}Do you know?"
            "I shook my head, admitting she was right."
    stop ambience fadeout 3
    play sound sfx_open_door_mines
    scene bg int_mine_exit_night_light
    with dissolve
    if alt_day4_sl_cl_lf_solo == 1:
        "Shurik didn't lie - the exit was nearby, just two rooms away."
    else:
        "The practice gained - I was definitely becoming an expert at unlocking cremallers - and a vertical row of metal staples was revealed to our gaze."
        "Slavya got in first, as a know-it-all and possessor of a super-powerful all-release artifact codenamed «bundle of keys from everything in the camp»."
        "Well, I tried my best not to peek."
        "It was hard, to be honest."
        "Finally, something rumbled and rumbled from above, and the dusty grate fell out."
        sl "Lena, Semyon, Shurik, get up!"
        "I didn't risk leaving Lena alone with the unstable Shurik, so Lena climbed next."
    scene black
    stop music fadeout 3
    stop ambience
    scene bg ext_square_night with dissolve
    play ambience ambience_camp_center_night
    "And I got out last."
    "And it took me a long time to catch my jaw when I realized that all our twists and turns had put us right back where we started."
    "In the middle of camp!"
    "As it turned out, Genda's pedestal was hollow, and just below it was a well-hidden ventilation grate covering the stairs to the catacombs."
    th "What the hell is this?!"
    show sh normal pioneer with dspr
    if alt_day4_sl_cl_lf_solo == 1:
        sh "I think I'll go now. It's clearly not a good day."
        me "No way."
        "I snorted."
        "I don't want him to get lost again."
        me "Let's go to Violetta's together, let her see what happened."
        me "And it would be good to treat the scratch."
        "Shurik sighed and sagged."
        return
    else:
        sh "Guys, I think I'm going to go. {w}Bother our doctor, you know?"
        me "At 3 in the morning? Good luck."
        "I nodded."
        sh "And... I'm not very comfortable, but thank you very much for finding me.{w} And listening."
        hide sh with dissolve
        "He headed for the infirmary."
    scene bg ext_square_night at zenterleft
    show sl smile pioneer at cleft with dissolve
    sl "So, how did you like the walk?"
    "The girl smiled."
    me "Not so much.{w} If it wasn't for you, I wouldn't have gone or walked anywhere."
    show sl laugh pioneer with dspr
    sl "Don't be proud, you're better than you think you are."
    sl "I believe in you."
    "Such words are usually followed by a confession, a kiss - anything that expresses a climax!"
    "All those damn books and movies can't lie, can they?"
    "But my wooden tongue and dry throat..."
    scene bg ext_square_night
    show sl smile pioneer at left
    show un shy pioneer at cright
    with dissolve
    un "Guys, it's really late.{w} Or should I say «really early»?"
    "Lena started."
    un "Anyway, I've done my task, I'm going to bed.{w} See you later!"
    hide un with dissolve
    "She waved and went back to her cabin."
    me "Let's sit for a while, shall we?"
    "I suggested when Lena was out of sight."
    me "I haven't had enough time downstairs."
    play music music_list["waltz_of_doubts"] fadein 3
    sl "We should get you to the infirmary..."
    "I made pleading eyes."
    me "Yes."
    sl "And it's late."
    me "Also true."
    "It was cozy and affectionate, and I was surprised to hear myself say:"
    me "The night is warm.{w} Cozy.{w} Are you in a hurry?"
    "Slavya smiled."
    me "Never had to sleep outdoors?"
    sl "No."
    me "What kind of dreams do you think you must have when there's no ceiling overhead?"
    sl "I don't know. But aren't you afraid of getting wet from the dew?"
    "She was still playing her part as a girl with principles and rules."
    "And I was pushing and pushing her to go crazy for a while."
    sl "It's cold, you'll catch a cold."
    scene stars with dissolve
    "I sat down on the bench and took her with me."
    sl "Yeah, and... Your head."
    "Something heavy came down on my shoulder."
    sl "You can't... I guess."
    scene cg d5_sl_bench_night_7dl with dissolve
    "Slavya laid her head on my shoulder and covered her eyes."
    sl "That's not right..."
    me "But I've accomplished a feat today."
    "I smiled at her."
    me "I deserve to have one wish granted."
    sl "What's that?"
    "She murmured, falling asleep."
    me "Go to sleep.{w} Sleep with me by your side."
    "I myself could feel my eyes rolling up, something squeezing inside me to the point where I could feel it."
    th "I'll just close my eyes a little..."
    stop music fadeout 3
    scene black
    pause(2)
    th "For just a second."
    sl "Good morning."
    "My shoulder got a little stiff from the unaccustomed weight, but I didn't care - I wasn't going to move it."
    me "What morning, it's nighttime."
    "I felt like I slept for half an hour, no more."
    scene bg ext_square_sunset at zenterleft
    show sl normal pioneer at cleft
    with dissolve
    sl "Not anymore."
    "She shook her chin, pointing to the east."
    "And there the darkness was already giving way to the still dark golden and burgundy tones."
    "But soon they will add in brightness."
    "And the sun will claim the new day."
    scene bg ext_square_sunset
    show sl sad pioneer with dspr
    with dissolve
    sl "We're like two tramps, sleeping on benches."
    me "And let anyone try to blame us for that."
    "I wanted to tell her something stupid, romantic, seemingly important now."
    "But I knew in my thousandth gut that it was too soon."
    "She won't appreciate it."
    "Or she would, but..."
    show sl normal pioneer with dspr
    sl "Let's go turn you over to Violetta Cernovna, I hope she hasn't fallen asleep yet, having taken Alexander."
    "Unnecessary platitude."
    "A lifesaver in an awkward situation."
    "She was beautiful even in her embarrassment."
    "And I realized it was useless to lie to myself."
    "She's too necessary."
    me "I'll get there myself."
    "I pointed to the infirmary, which you could see right from here."
    me "I don't know whether to say good morning or good night."
    show sl smile2 pioneer with dspr
    sl "Just - see you."
    "The girl patted me on the shoulder and ran off."
    "And I wandered off to the infirmary."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_sl_wh_night:
    scene bg ext_path2_night with dissolve
    play music music_7dl["nowyouseeme"] fadein 3
    play ambience ambience_forest_night fadein 3
    "Unhappy with myself, I moved on home."
    "Honestly, I'd already done a lot more than I'd planned."
    "No one had set me the task of climbing into the dungeons and searching long and hard for someone there."
    if alt_day4_sl_cl_tut_iz:
        "Especially since I didn't have any flashlight with me."
    "And yet I wasn't happy with myself."
    "I had a little vain thought, whispering about how great it would be."
    "To exacerbate my already heroic status."
    dreamgirl "Yeah. Then maybe the girls will start paying attention. {w}And your Slavushka won't look at you with a sense of camaraderie and support."
    th "Missed, man, missed. {w}It's totally out of my league, I don't fly that high."
    dreamgirl "Whatever you say."
    dreamgirl "This is not your modern society, there is no casteism here, and the social elevators work their way up - just remember yesterday."
    th "I was just helping her with camp stuff, which I ended up paying for."
    dreamgirl "Helping with the antenna was definitely not part of the camp business, it was your ill will that got you a season ticket for not working wings."
    dreamgirl "Would rather stay dancing with a girl, nice girl, pretty, single."
    th "Doubtful. {w}Such beauty can't be idle. I think she's got somebody..."
    "I didn't finish the thought."
    play sound sfx_scary_sting
    stop music fadeout 3
    pause(1)
    play sound sfx_bush_leaves fadein 0
    "I was interrupted by a suspicious rustling of bushes."
    play music music_7dl["dead_silence"] fadein 3
    "Very suspicious."
    "I froze."
    play sound sfx_bush_leaves fadein 0
    "The rustling repeated."
    th "Shit, what could that be?"
    "Hardly some kind of dangerous predator, it's what they do, after all, with a soul to disperse them when they build childcare facilities."
    "Few people would like to have a bobcat jumping into their sleeping offspring's bedroom."
    "But some foxy hare would, would, would."
    play sound sfx_bush_leaves fadein 0
    "I headed in the direction of the suspicious noise, moving for some reason on tiptoe."
    th "There's someone there!"
    dreamgirl "I'm guessing!"
    dreamgirl "Shall we look or screw him?"
    th "I don't feel safe!"
    dreamgirl "Let's get out of here, then!"
    play sound sfx_hiding_in_bush
    "That's right."
    "I will."
    "I shook my heavy head and headed for camp."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day4_sl_cl_cs_night:
    play music music_7dl["lastlight_guitar"] fadein 3
    $ persistent.sprite_time = "sunset"
    scene bg int_aidpost_night
    show genda_portrait
    show cs normal
    with dissolve
    if alt_day4_sl_cl_lf_solo == 1:
        "Viola was dozing, dropping her head on her arms folded on the table."
        "But at the sound of our footsteps, she woke up and raised her head."
    else:
        "Viola was already waiting for me, despite it being late (or shouhld I say «early»?) — there was a thermos on the table, which smelled fragrantly of some herbs."
    cs "You're out and about today."
    "She strictly said."
    cs "And I didn't discharge you, by the way."
    me "I'm sorry..."
    "The state in which the nurse would now have to work, after her vigil, suddenly came to mind."
    "The clock was now much closer to rising than it was to going to bed."
    cs "Here, take your meds, and go to your cell."
    me "What?"
    cs "I say, take your herbs and go to your bed."
    cs "If everything is okay in the morning, I'll discharge you."
    me "Thank you very much!"
    if alt_day4_sl_cl_lf_solo == 1:
        "She beckoned Shurik with her finger."
        cs "You."
        show sh normal pioneer at right
        cs "Since I don't sleep anymore because of you, you're on duty until lunchtime. Is that clear?"
        "Shurik nodded."
        cs "Excellent. Now drink these pills and take the jar with you, you have to drink them all in three days."
        "She handed him a half-empty plastic vial of pink pills."
        cs "And then... Good night."
    elif alt_day4_sl_cl_lf_solo == 2:
        cs "When you go to the backroom, be quiet: you have a new addition."
        "She pressed her finger to her lips."
        cs "Don't ask anything."
        "She yawned sweetly."
        show cs smile with dspr
        cs "You'll see tomorrow."
    else:
        cs "I've sedated your basement diver, so if you're going to lie down, be quiet over there... Pioneer."
    cs "Well, it's late, let's scatter to our potties and cradles."
    show cs smile with dspr
    cs "I'll take the rest of the day off tomorrow before noon, and you do your best here."
    cs "If it's something serious, lift me up without pity, but with the cuts and headache, I think you can handle yourself."
    "She grabbed the doorknob."
    cs "And you can take that oaf off now."
    "Nurse shook her head."
    cs "I'm sick of this."
    "Genda from the portrait flashed his eyes menacingly."
    if alt_day4_sl_cl_lf_solo == 1:
        sh "Boo done."
        cs "That's it, I'm sleepy, I can't."
        cs "Pioneer, this is for you, half now, half in the morning."
        "She pointed to the thermos standing next to the computer."
        cs "And now - sweet dreams to you, Violetta Cernovna."
        "She walked out, hitting me with her shoulder on the way out."
        hide cs with dissolve
        me "She's got a point."
        "I nodded."
        me "I drink whatever she made for me, and we both go to bed."
        "Shurik nodded in solidarity."
    else:
        if alt_day4_sl_cl_lf_solo == 2:
            cs "If you wake up first, don't mix it up: these pills are for you, these are for your addition."
        else:
            cs "I'll leave a pill on the table for the diver to drink when he wakes up, and then he can go."
            "The second sip of herbal concoction went easier than the first, and I even began to discern something tasty in it."
            cs "You shouldn't have let your pioneer girl go."
            "From the doorstep, Viola said without turning around."
            me "Excuse me?"
            cs "Feoktistova."
            cs "But alright, I'll talk to her myself tomorrow."
        cs "Now go to bed."
        "How could I resist such a tempting offer!"
    "Before the sound of the door closing, I was already lying under the blanket."
    "Consciousness was suddenly and immediately switched off."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_sl_cl_begin:
    play music music_7dl["so_cold"] fadein 3
    scene bg int_sam_house_clean_7dl
    show prologue_dream
    with diam
    $ prolog_time()
    "Night... Loneliness."
    "I've always wondered how many people actually cared about my plight - and were silent about it."
    "Friends are defined by actions."
    "Don't want to go back and get in the way, but peek at the stats, the attendance, toss in a handful of good luck and, after making sure everything was okay, hide back in your hole."
    "Always wondered how many people were actually in your life but wouldn't let you into theirs."
    "They look into you like a showcase, waste your energy and time, and then one day they just walk away."
    "I used to appreciate the latter a lot more."
    "And now all I have left is the night. {w}And loneliness."
    "The illusionary world of the monitor window, on the screen of which the girl generously gives smiles,"
    with fade
    extend " somehow resembling Slavya."
    "I guess this girl is only possible out there - in a world where you can peek through a monitor."
    "By the laws of fiction."
    "Or in some world caught between the poles of an unfulfilled world - a name for a very much finite summer."
    "By the laws of fairy tale."
    "The glare of passing cars streams down the walls, strangely reaching as far as the seventh floor."
    "«You should only write in such a way that you are not ashamed of the tears from your eyes» — said the creator and burned the second part of the manuscript."
    "I pull my hand to the hard, hot surface, breaking the picture under the touches in circles on the water."
    scene black
    "I want to touch her cheek."
    show sl normal dress at cright
    show prologue_dream
    with touch
    "In vain."
    "Idiot."
    "I'm sitting in my room."
    "And even if I were there, in the raging sea of human rapture, piercing through my head, leaving under my skull's vaults only a ringing, jubilant cry..."
    "Would I have managed there to touch one that deserves far more than life?"
    "Too perfect to be true, too good, I will always look for a catch."
    "In the end, I'm simply not worthy to be around."
    scene
    $ renpy.show("cg d1_sl_dinner", what = Desat("cg d1_sl_dinner"))
    show prologue_dream
    with dissolve
    "Memory crumbles again in useless, bitter flakes, speeding up, speeding up the running of the clock hands."
    "And on a faded poster that reads «door to happiness» there is a print of a narrow, graceful palm."
    scene anim_underwater
    with blind_l
    "And under the bollard, clutching her skinny knees, dropping her hand, the former goddess dies of oblivion and cold."
    "For in fact any god is primarily alive and strong as long as at least one person believes in him."
    "I was probably the last person to believe in the fragile figure."
    "But I had the misfortune to see her as an object for dreams, and then I didn't want to sleep at all."
    "That's not faith anymore."
    "While I freeze at the doorstep of the unfulfilled, the last admirer, the last believer, she wavers between nothingness and total oblivion."
    "Vainly trying to find even a little warmth on my chest."
    "We are antagonists, warming each other's hands, not existing, not real."
    "That's why the cry for help gets stuck in the cold faster than it leaves a parched throat."
    "People don't see us, they look through us, pass through us."
    "The heart beats slower and slower - it trembles more and more shallowly and faintly."
    "And when a cold blue light bursts to us between bursts of clouds, we can no longer resist."
    "The moonlight takes from us what has always belonged to it, a negative value with a negative weight, and the two hollow ghostly shells crumple under their own weight and the weight of the wind."
    stop music fadeout 3
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    scene
    $ renpy.show("bg int_house_of_sl_day", what = Desat("bg int_house_of_sl_day"))
    show unblink
    play ambience ambience_7dl["rain"] fadein 3
    "I flinched and opened my eyes."
    play music music_7dl["shehasgone"] fadein 3
    "What the hell did I just dream of. {w}After dreams like that you can't even believe that reality is real."
    "Well... As far as this reality goes."
    "As I'm told from the audience, we might as well be a butterfly's dream on the slope of Fuji-sama."
    "So, for the sake of Random, I shouldn't insist on the uncontroversial nature of the objective environment."
    "For example?"
    scene
    $ renpy.show("bg int_house_of_sl_day", what = Desat1("bg int_house_of_sl_day"))
    with blind_l
    "To begin with, at least, I'm opening my eyes again God knows where."
    "Although..."
    if alt_day_binder != 1:
        "The room was thoroughly unfamiliar, the vaulted ceiling gave away the insides of the log cabin, and a peaceful snooze came from the neighboring bed."
    else:
        "If memory serves me right, I've seen this room before."
        "The room was vaguely familiar."
        th "That's right! It was here that I was changed, combed, and sent to faint!"
        "Slavya's room, to be specific."
    "The moment was missed - the dream had eroded from memory, leaving a black and white imprint there."
    "And i didn't move, didn't think or want to."
    "What I liked best right now was to lie there and stare at the ceiling."
    "Or better yet, close my eyes and pass out for exactly the same amount of time I'd been inactive before."
    "I hate the word «sleep» — and I cringe every time I hear «go to bed, it's already ten o'clock»."
    play sound sfx_7dl["bed_squeak"] fadein 0
    "There was a creak from the left, a sigh, and I squinted my eyes in the direction of the noise."
    "And I could hardly suppress the urge to jump up or scream or otherwise destroy the magic of the moment."
    "Because on the next bed, arms spread out, smiling in her sleep..."
    scene
    $ renpy.show("cg d5_sl_bed_7dl", what = Desat("cg d5_sl_bed_7dl"))
    with dspr
    "Slavyana."
    "She neglected the blanket and slept under a sheet."
    "Very practical in this heat, but the humid air and the heat made the thin fabric, blistered by the water in the atmosphere, almost transparent, and I stared at the way the edge of the sheet went back and forth on the girl's high chest."
    "It seemed as though it was about to open to my gaze...."
    show dreamgirl_overlay with dspr
    dreamgirl "How about acting as the first principle of thermodynamics?"
    th "Y?"
    dreamgirl "I'm talking about introducing an external force into a closed system. {w}And there doesn't seem to be enough energy there for the wretched sheet to finally slide off!"
    "Yes, I am a lustful monster. {w}And even my split personality is equally horny."
    "I curled my legs together and turned my back against the wall."
    "My shorts became tight, and I noticed that I was lying on the bed fully clothed, only without shoes."
    "I noted with regret that the breathing rhythm was off."
    "A few seconds later, the panelled netting creaked again."
    sl "Don't turn around, I'm getting dressed."
    "A girlish voice warned."
    scene
    $ renpy.show("bg int_house_of_sl_day", what = Desat("bg int_house_of_sl_day"))
    with blind_r
    me "Like I haven't seen enough of you while you were sleeping."
    "I grumbled."
    sl "Did you?"
    "Under the vaults of the round roof, a melodious laugh resounded."
    me "You ask such questions."
    me "As if..."
    "A few more seconds of rustling and creaking later, something heavy landed on the bed on the other side."
    sl "You fell for the innocent joke again. {w} How shy you are after all."
    "She laughed."
    "And I turned around and looked past her into the clear-gassed window."
    "There it was morning, gray melancholy and more August than July rain - unhurried, measured and to myself."
    scene
    $ renpy.show("bg int_house_of_sl_day", at_list = [zenterright], what = Desat("bg int_house_of_sl_day"))
    show sl normal sport close at cright with dissolve
    "Slavya was sitting on the edge of my bed, dressed in her sports uniform."
    me "My head... How did I get here?"
    "Without much hope I asked."
    show sl smile sport close with dspr
    if alt_day4_sl_cl_lf_solo == 1:
        "Whether she was smiling or not, it wasn't clear - at least remember the fact that the two of them had gone off on a search without me."
        "Even the fact that I was the one who found Shurik didn't change that."
        me "So I found Shurik, brought him back, and then..."
        sl "So you went looking alone after all."
        "The girl shook her head."
        me "But I definitely remember going to bed in the infirmary. Then what happened?"
    elif alt_day4_sl_cl_lf_solo == 2:
        "Yesterday's events were difficult and reluctant to recall-I think I tried to look for the fugitive alone, but had to backtrack."
        me "Didn't seem to fall asleep quite here."
        sl "Good point!"
    else:
        me "No, seriously. {w}We got here at hell if I know when, I let you go home, and I went to Viola's."
        th "Anyway, that's what I remember exactly."
        me "And then...?"
    stop music fadeout 5
    sl "And then I tried to go to bed, but I didn't sleep a few hours before you came knocking on my door."
    "With the look of a professional clerk, the girl reported."
    sl "Tried to tell me something really hard, either about the federation or the republic, but in the end you never said anything."
    "I covered my eyes penitently."
    play music music_list["she_is_kind"] fadein 3
    show sl smile2 sport close at center with moveinleft
    "It's true that something familiar and unrepresentable came to mind."
    "I don't know what came over me, but that was that and this was this."
    "But the bits and pieces didn't add up."
    "I remembered the sound of water rushing into the sink, the cracking of the lock, a small bottle of brown glass marked 'hawthorn tincture'."
    "Then a path under the tight, stretching streams of rain, and somewhere something was tearing, either outside or, conversely, in my chest."
    th "Nice."
    "With an already colorless repentance, I stated."
    th "I thought it was just the concussion that made it a little stormy, and the rain."
    th "The drunkard Evgrafovich, drunk on hawthorn tincture, like a hobo, walked through the camp and loudly shouted the saga of how 'I closed my door with a heavy bolt', in which only this line was decent."
    "And came here."
    scene bg ext_houses_night_7dl
    show prologue_dream
    with diam
    "Or rather, not here, but to the bench at the entrance, and Slavya, drawn by an unknown animal instinct, got up, went out..."
    "And I had such strange dreams, I was smiling like a fool."
    "Like I was alone in the camp."
    "Walking around the grounds, picking up scraps of paper, sweeping sand and pine needles off the concrete paths."
    "In front of Lena and Miku's cabin I turned the bench around so I could see who was sitting from the door - it was hard, but I made it."
    "Finally, carefully, with just my fingers, pulled the echoes of someone's frustration, anger, insubordination, and just plain negativity out of the air."
    "Rubbed the sun to make it shine brighter."
    "And only then whispered «it's time»."
    "A looped slice of space, spinning hundreds of kilometers of highway, straightened out, ducking straight into the welcoming gates."
    "A very young clear-eyed girl reflected the sky with her gaze as she entered between the flaps, touched the carved five-pointed star with her hand, smiled, and I couldn't help myself."
    "Sneaked up, kissed the back of her neck."
    "Laughed when the girl flinched, and rushed away echoing with warm wind."
    scene
    $ renpy.show("bg int_house_of_sl_day", what = Desat1("bg int_house_of_sl_day"))
    show blackout_exh3
    with dissolve
    sl "You're almost gone already."
    "Slavya brought me back to reality."
    hide blackout_exh3
    show sl smile sport close
    with dissolve
    sl "Shouted something about taking a boat and rafting to the ocean, and if you don't find some... I don't remember exactly how. {w}Kybos? {w}Saibok?"
    me "Skybox?"
    sl "I guess so."
    "Thoughtfully she said."
    if not alt_day4_sl_cl_tut_iz:
        sl "Then you spent a long time telling me something about infrasound and the system of introducing information into the subconscious..."
        show sl surprise sport close with dspr
        sl "What?"
        me "What?"
        sl "You stared like I said something very strange!"
        me "But you did!"
        scene
        $ renpy.show("bg int_house_of_sl_day", what = Desat1("bg int_house_of_sl_day"))
        show sl laugh sport close
        with dspr
        sl "I was quoting you, don't get the wrong idea!"
    hide sl with dissolve
    "Slavya sat down with her back to me and stared out the window, where drips of stray rain trickled down."
    me "Still, you're too kind to be real."
    "I said thoughtfully."
    sl "And you say too silly things for me to argue with."
    me "Is that so?"
    me "I mean, silly things."
    stop music fadeout 4
    th "No one is sure to come in here for a few more minutes while the loudspeakers are silent and the horn is not shouting."
    th "And Slavya, as far as I remember, always ran in the morning, in the cold, while it was quiet and everyone was asleep."
    "I swallowed bitter saliva."
    play music music_7dl["but_why"] fadein 3
    "And I thought that must be how one goes crazy - from the feeling that one can't just lie on the stove and look at life passing by."
    "I ran my hands under her arms, put my palms on her supple, warm belly."
    "And pulled on myself."
    show sl surprise sport close with dspr
    "She was beautiful, kind, sympathetic."
    scene
    $ renpy.show("bg int_house_of_sl_day", at_list = [zentercenter], what = Desat("bg int_house_of_sl_day"))
    show sl shy sport close
    with dissolve
    "Her weakness was that she could not distinguish other people's feelings, which she sensitively, like a naked nerve, perceived from the ether, from her own."
    "I, on the other hand, desired her most intensely now - and writhing with a buzzing head and tearing at the back of my head with a gnarled bandage - called to myself."
    "Slavyana fought back weakly, trembling and hiding her eyes."
    sl "No, not here."
    "She whispered."
    sl "Wait."
    "But how could I stop."
    "She crumbled in my arms - at once, suddenly."
    "Her skin was salty, warm, firm."
    "And there was nothing under her sports uniform."
    scene
    $ renpy.show("bg int_house_of_sl_day", what = Desat1("bg int_house_of_sl_day"))
    with fade
    "And the bewilderment was replaced by a reflection of my desire - not even two minutes later, she exhaled convulsively and stopped pushing my hands away."
    "And I just got to her ear."
    th "Gave up?"
    "The reaction was strange enough, plus the girl closed her eyes, bit her lip..."
    sl "You know what you're doing, don't you?"
    "She said distinctly."
    me "What?"
    "I asked hoarsely, coming to my senses."
    sl "I mean."
    scene
    $ renpy.show("bg int_house_of_sl_day", at_list = [zenterleft], what = Desat("bg int_house_of_sl_day"))
    show sl happy sport close at cleft
    with dissolve
    "She didn't even try to break free, and there was boundless excitement in her eyes."
    sl "Why are you climbing up my shirt?"
    me "Excuse me."
    "It suddenly dawned on me that I think I just almost did..."
    stop music
    "And I froze up."
    show dreamgirl_overlay with dspr
    dreamgirl "NOOOOO!" with vpunch
    show blackout_exh3
    "From the depths of my subconscious a cry of sorrow came."
    dreamgirl "Turn off the smartass mode, come on! Before she…"
    "Too late."
    hide dreamgirl_overlay
    "Sensing my perplexed tension, Slavya easily got out of my arms."
    "But she was in no hurry to get up."
    show sl sad sport close with dspr
    sl "I've always laughed at stories where someone gets pinched and they don't fight back."
    sl "Now I understand why."
    me "And why is that?"
    play music music_list["take_me_beautifully"] fadein 5
    "She took my palm off her belly and squeezed it softly."
    show sl normal sport close with dspr
    sl "You stopped. Weird."
    me "Why?"
    sl "Boys don't know how to stop, or I don't understand anything about psychology."
    "She stroked the knuckles of my hand."
    sl "And you wouldn't stop, and there..."
    me "Yeah?"
    scene
    $ renpy.show("bg int_house_of_sl_day", what = Desat1("bg int_house_of_sl_day"))
    show sl shy sport close
    with fade
    sl "While I was trying to fight back, I kept thinking how disgusting and vile it was."
    sl "But it's in our nature, how can it be disgusting?"
    "She shook her head."
    sl "And then there's you and your sympathetic looks. {w}Well, yesterday when I said it was too soon for me."
    "She was talking slower and slower."
    sl "So I thought, why not..."
    me "Try it?"
    "Naturally it came out of my mouth."
    th "But I don't think so. {w}She's all so right, and her Soviet upbringing..."
    th "Then what? Marry me off by knocking up?"
    show dreamgirl_overlay with dspr
    dreamgirl "Wow, what a crafty Slavya."
    th "Excuse me?"
    dreamgirl "Yeah, you know, there's a suspicion that she was in control until the last minute."
    show sl smile2 sport close with dspr
    sl "Take revenge."
    "She fully confirmed the suspicions of the inner voice."
    sl "Especially since you've been so diligent in digging your own grave."
    me "But... Why?"
    "She shrugged her shoulders."
    scene
    $ renpy.show("bg int_house_of_sl_day", what = Desat1("bg int_house_of_sl_day"))
    show sl normal sport close with dissolve
    sl "No reason. {w}But you reeked so infectiously of anticipation."
    "Half-turned, the girl looked thoughtfully at the rain drumming on the glass."
    me "Yes, yes, you've said that before about lust."
    sl "Not lust. {w}I know what it looks and sounds like, that lust of yours, I didn't grow up in a tin can after all."
    me "Is that so?"
    scene
    $ renpy.show("bg int_house_of_sl_day", what = Desat("bg int_house_of_sl_day"))
    show sl smile sport close
    with dissolve
    "The girl nodded without looking at me."
    sl "But your situation is different."
    sl "You were shaken by the idea that it was me."
    sl "Certainly flattering, you know."
    show sl normal sport close with dspr
    sl "I couldn't help myself. I'm sorry."
    me "So that was your revenge?"
    show sl smile2 sport close with dspr
    show dreamgirl_overlay with dspr
    dreamgirl "Typical female!"
    show sl smile sport close with dspr
    sl "If you don't mind, I won't tell anyone about it, okay?"
    th "Yeah, I guess so!"
    "I groaned and hid my face in my pillow."
    th "Asshole! What have I done!"
    with fade2
    sl "Semyon?"
    me "Yes, yes. Please. Not a word to anyone."
    th "With my own hands I handed her all my password buttons!"
    "Though somehow I had no doubt that even if I hadn't, she would have picked it up herself."
    show sl normal sport close at right with moveinright
    "For bruteforcing, even in social engineering, wasn't abolished."
    "She would poke me with a stick, see my reactions, and voila."
    "Yesterday, for example, I gave her a lot of material to study."
    show sl normal sport close with dissolve
    sl "Semyon, don't sleep."
    "She leaned on me so that it was as if I were wrapped around her - legs on one side, head on the other..."
    "A serpent-torturer... Or a serpent-snatcher!"
    sl "Why don't we try it."
    me "What exactly?"
    show sl smile sport close with dspr
    "Is it just me, or has there been an added slyness in her eyes?"
    sl "Well..."
    "She seemed to relax in thought, and I was afraid to move."
    sl "Become a couple, you fool."
    "She laughed."
    show sl smile2 sport close with dspr
    sl "You're a good-looking boy... And we've just ascertained your interest."
    me "Rejection is not accepted, right?"
    show sl laugh sport close with dspr
    "The smile got even wider."
    sl "Absolutely right."
    show sl smile sport with dspr
    "She stood up."
    scene
    $ renpy.show("bg int_house_of_sl_day", what = Desat1("bg int_house_of_sl_day"))
    show sl normal sport far
    with dissolve
    sl "Did you want to say no?"
    "I shrugged it off."
    me "Honestly, I didn't believe until the last minute that I wasn't dreaming."
    scene
    $ renpy.show("bg int_house_of_sl_day", what = Desat("bg int_house_of_sl_day"))
    show blackout_exh3
    show sl normal sport far
    with dissolve
    me "You definitely must have some young man, nice, capable, promising."
    me "And… {w}Ah, right! You said it yourself — «too early»."
    sl "So it's not too early anymore."
    me "Did you just decide that?"
    "I politely clarified."
    show sl laugh sport at center with dissolve
    sl "Yes! {w}I suddenly realized that it's about time."
    me "Whatever you say. {w}Are we supposed to shake hands now?"
    show sl shy sport at center with dspr
    sl "Should a couple be shaking hands?"
    "She blushed a little."
    "I've met a lot of different couples. {w}Even Old Believers I've seen respectfully call their spouse 'you'."
    me "If you'd like. {w}I don't insist."
    scene
    $ renpy.show("bg int_house_of_sl_day", what = Desat1("bg int_house_of_sl_day"))
    show sl shy sport
    with dissolve
    sl "What do you have to do now?"
    th "What cool questions!"
    show dreamgirl_overlay with dspr
    dreamgirl "Especially after you've been rubbing her belly and broadcasting your lustful thoughts."
    me "Nothing. {w}Live."
    sl "Well, now that you're my - what's the Western word for it? - boyfriend, you're gonna have to live up to it."
    me "Chest bump, belly flap?"
    "The girl brushed it off."
    sl "You'll have enough even by just helping out with stuff."
    me "What if somebody asks how is it that we suddenly decided to start dating?"
    show sl surprise sport with dspr
    sl "How?"
    "She opened her fluffy eyelashes."
    sl "Have you forgotten? {w}You brought me a love letter because you were too shy to confess yourself."
    sl "And I accepted it."
    sl "That's how you became my young man."
    show sl laugh sport with dspr
    "The unfortunate limb was finally left alone."
    "And soft lips touched my cheek."
    sl "So, how do you like your new morning?"
    me "Don't even ask."
    "I moaned."
    sl "And I liked it, too."
    me "By the way, whose bed am I lying on?"
    sl "Oh, that's Zhenya's."
    me "AUUUUUGH!"
    with vpunch
    play sound sfx_bodyfall_1
    "I instantly fell on the floor."
    show sl normal sport with dspr
    sl "What are you doing?"
    me "Buzzer's! I might throw up!"
    show sl smile2 sport with dspr
    sl "Okay, stop fooling around. I'm going for a run."
    sl "I'm not taking you with me, Olga Dmitrievna told me yesterday to send you to the camp director right after I got up."
    hide sl with easeoutright
    play sound sfx_open_dooor_campus_1
    "Giving me another smile goodbye, the girl scurried out of the cabin."
    stop music fadeout 3
    return

label alt_day5_sl_cl_chief:
    scene
    $ renpy.show("bg int_house_of_sl_day", what = Desat1("bg int_house_of_sl_day"))
    with joff_r
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg ext_houses_rainy_day_7dl with dissolve
    play music music_list["raindrops"] fadein 3
    "Taut, shouldered and smelling of barberry caramels, your humble servant moved along the camp's only street, Kommunarov Street."
    "I could have said something about 'a little drunk, shaved blue,' but the former is off the table because of last night, and for the latter my present bodily conditioning is not yet ready."
    "Slavya ordered to live up."
    "And she ran off on her daily promenade - and she didn't care if it was pouring like a bucket outside."
    "Neither did I, for that matter. {w}My rain is my weakness."
    "Who knows what «living up» could mean, but I tried my best - splashing puddles, typing a step and keeping my tail pistol-whipped."
    "The only thing missing was Marusya with a handkerchief in the window in the rear."
    th "Yeah. My Marusya will go to war for me, if I suddenly decide to shirk it."
    if herc:
        "So, ladies and gentlemen, I'm happy to present to you S. Sychev - military, handsome, big!"
    else:
        "So, ladies and gentlemen, I'd like to present S. Persunov, a real pioneer."
    "In a dress uniform with the whitest shirt, with a trendy tie on his chest - isn't he splendid?"
    "The gold buttons on his parade shirt gleamed, and so did the Ilyich badge on his chest, along with the gray-swamp colored eyes the diameter of a button."
    th "Looks like last night's catch-up had taken its toll."
    "There was no debris, no belongings left behind, and nothing else to indicate the presence of a human being."
    scene cg d5_rainy_idle_7dl with dissolve
    "In the rain, the camp looked uninhabited and more like an open-air museum."
    me "Grace."
    "I couldn't help myself."
    "That's right, nobody wanted to get wet in the rain but me and Slavya, and the mugs were all closed."
    th "If I'm not mistaken, the clubs were supposed to be cordoned off by volunteers and no one was allowed in until..."
    "«Until» what exactly, I still haven't figured out."
    if not alt_day4_sl_cl_tut_iz:
        th "But the management have to take at least some measures - they've got a fucking working vomit generator on the premises!"
        th "Or is that the norm here and in full compliance with the rules?"
        "A counter-argument immediately jumped into my head with the prudent cowardice of a twenty-first century resident."
        "Before I go around threatening and making claims to the powers that be about the local machinery, it would be a good idea to consider one curious point."
        "The fact is that this hardware passes for a special purpose class - you don't go and buy it in a drugstore for three rubles a bundle in modern conditions - so someone at the top knows."
        "Although I did recall that around the same time, the editors of Young Technician and Technics of Youth were, as if in cahoots, publishing in their pages circuits of just this kind."
        "But that's a kind of elite level of clearance - the only one who would be able to assemble such a thing at home..."
        show dreamgirl_overlay with dspr
        dreamgirl "Yep-yep, a genius capable of building a self-learning intelligence system in a camp radio club."
        th "But that's just a rumor!"
        dreamgirl "Really? {w}Is that what Shurik told you?"
    "I was distracted from answering by the sound of the speaker blaring - the bastard had ruined the whole morning-rainy mood."
    "For some reason I got a headache - no other reason than a conditioned reflex that associated my brief flight with the same sound."
    "Meanwhile, there was a crackling, thudding sound overhead, and Sviridov's «Time, go on!» came on."
    dreamgirl "Music that makes you want to do five years in three years, huh?"
    th "Mm-hmm."
    th "If I'm not confused, that music also plays to the news."
    dreamgirl "Knowing your karma, you're in for some news."
    scene bg ext_admins_rain_7dl with dissolve
    "I froze as I noticed several cars huddled outside the brick cube of the administration building."
    "And their amount gave me absolutely no good feeling at all."
    "On the contrary, if my intuition was right, there was going to be a huge, full-blown sob story, with the right and the wrong being blamed."
    "With the obligatory handing out of earrings to sisters and brothers in the face - so sooner or later the interest would come to me."
    "And someone will ask the sacred question: «And who is this ghoul, and on what rights does he eat Soviet bread here?»"
    "And they'll take me by the hand and escort me to places not so distant."
    "Or anywhere else."
    th "Just remember, I'm just a Soviet pioneer, just poorly educated, don't remember history, don't remember anything."
    th "No future, tenths, pecks, hermitage, and the collapse of the Soviet Union."
    th "Then maybe I'll talk my way out of it."
    stop music fadeout 3
    "The Sviridov march was replaced by the Sviridov waltz from 'The Snowstorm'."
    scene bg ext_square_rain_day_7dl with easeinleft
    th "Um-tsa-tsa-tsa, um-tsa-tsa-tsa, dance along the administration tempo di waltz and pray that they don't notice us."
    th "And if Olenka Dmitrievna really is covering for us, then we'll hastily pretend to be a rag and sit for a couple of hours somewhere... somewhere!"
    th "She'll say where."
    "The rain intensified, and it added ten percent to my stealth skill."
    scene bg ext_houses_rainy_day_7dl with dissolve
    "I turned on the spot and, moving along the fifth cabin, headed north."
    "Toward my curvaceous green-eyed saviour."
    "Feeling an icy drop creeping leisurely between my shoulder blades."
    ba "Hey!"
    th "Fug."
    dreamgirl "Don't worry, maybe it's not for you."
    ba "I'm talking to you, you wimp in the parade shirt!"
    dreamgirl "Oopsie."
    "Attempts to hide or escape were useless."
    "And the last phrase also nailed my hope that I was not the one being addressed."
    "No, of course I could compete with the gym teacher at running on wet ground - but I know I won't run ten steps."
    "I'm sure I'll end up somewhere - with my karma."
    "And I have a limp head as it is, no need to make it worse with a spicy natural limp."
    me "Yeah?"
    "Slowly I turned around."
    show ba em1 uniform with dissolve
    ba "Let's go."
    "He called."
    ba "We were just waiting for you."
    me "Excuse me?!"
    show ba evil uniform with dspr
    ba "You have no need to apologize for your stupidity. {w}I forgive you. Let's go."
    me "But where?"
    "He exhaled in a way that almost blew me away."
    ba "Don't be stupid, wimp. {w}You're all expected in the camp director's office. March on."
    th "This is the end, isn't it?"
    "On weakened legs, I followed the gym teacher."
    scene bg ext_admins_rain_7dl at zenterleft
    with dissolve
    "In my head there were plans swirling around, one more fantastic than the next."
    show dreamgirl_overlay with dspr
    dreamgirl "Stun him in the back of the head and run away!"
    th "Yeah. If only I knew where to hit him."
    dreamgirl "Then a sharp kick under the knee and run away!"
    th "It was easier then to try to run away from him - there when he called me."
    dreamgirl "Then I don't know. You figure it out for yourself."
    "Having come up with nothing, I continued to linger in the rear of the big man."
    "We made it to the administration building."
    play sound sfx_open_door_kick
    scene bg int_admins_7dl with dissolve
    stop ambience fadeout 1
    "The heavy oak door rattled, cutting off the sounds of the waltz, leaving us in the short hallway."
    "Near the largest one on the banquette was already sweating Olga Dmitrievna, who greeted me with a brief nod."
    th "Whom I went to, I found."
    "It crossed my mind."
    show mt normal pioneer at cleft with dissolve
    show mt normal pioneer with dspr
    mt "Good luck to you."
    me "And why did that sound like a eulogy?"
    "I grumbled."
    show mt normal pioneer at left with moveinleft
    show cs normal at cright
    with dissolve
    "The door opened ajar, and Violetta's head appeared from there:"
    show cs smile with dspr
    cs "How long are you going to walk... Pioneer? {w}Olya, Borya, come in too."
    "Olga Dmitrievna obediently stood up and, catching up with us in two steps, pushed us into the holy of holies of the camp."
    play sound sfx_open_dooor_campus_2
    pause(1)
    scene bg int_chief_office_rain_7dl with dissolve
    play music music_7dl["areyouabully"] fadein 3
    "To the chief's office."
    "The sense of belonging, support, and brotherly shoulder shattered as the whole holy trinity dispersed to their seats, leaving me proudly alone."
    "Against the Lernaean Hydra - besides me and the three traitors, a dozen men dressed in dark tweed were found in the room."
    "Sanich sat at the very edge, by the door - definitely so that if anything happened, he could jump up and catch me."
    "A big, heavy and very stupid man."
    "Well, where to, and more importantly, why would I run?"
    show mt normal pioneer with dspr
    mt "Athlete, activist and generally a great helper."
    mt "Persunov Semyon."
    "Olga Dmitrievna introduced me to the gathered audience and tiptoed away to the other side of the immense table."
    hide mt
    with dissolve
    "My gaze she studiously avoided."
    show bb smile casual with dissolve
    bb "Well, we finally meet."
    "A strange man smiled at me."
    "Judging by the piety with which the few adults I knew were squinting at him, it was none other than the autocrat and all-powerful chief of our camp."
    "It seems that instead of sleeping like all white people while it's pouring outside, he went from the ship to the ball - that is, from the road straight to the meeting."
    th "I'd better remember to ask him his first name and patronymic."
    th "It's a real bastard to rest under a man and not know what to call him on occasion."
    bb "I see you're bored, aren't you? I see you're tired of the Pioneer shirt, you can't wait to join the Komsomol, and then the Party, right?"
    me "What?"
    show bb normal casual with dspr
    bb "I've heard about your exploits, Semyon."
    "Confidingly, the chief lowered his voice."
    "With a dozen people listening to his every word, it looked inappropriately comical."
    bb "About how from almost the first day you agreed to..."
    show dreamgirl_overlay with dspr
    dreamgirl "…hooked up!.."
    bb "...to help, then with this roof of yours, the situation came out, frankly, not very pleasant."
    me "That's an understatement."
    "My fingers again against my will reached for the sagging back of my head."
    bb "And finally, your search yesterday, when, despite your ill health, you went in search of a comrade."
    if alt_day4_sl_cl_lf_solo == 2:
        bb "Not very successfully, unfortunately, but that's okay, he came out to camp himself in the morning."
    else:
        bb "And found him!"
    bb "Here."
    "A glossy piece of paper rolled across the table in my direction with a stamped cutout and boilerplate lines."
    me "Acknowledgements: «Sovyonok» camp administration thanks Persunov Semyon for his active participation in camp life, as well as for his wit, valor, and honor."
    "Confusedly I read."
    me "And what would that mean?"
    if alt_day4_sl_cl_tut_iz:
        "I didn't see much valor in going overnight to camp and back, but..."
    dreamgirl "Look, man, this isn't your native reality, here all this scribbling means something."
    th "Really now."
    dreamgirl "As I recall, diplomas and medals may not have really counted in educational institutions, but commendations are like a TRP badge, almost a backstage pass."
    show bb smile casual with dspr
    bb "We didn't write down exactly what you did, but if you're willing, that won't be a problem."
    bb "Also, could you leave the coordinates of the university where you're going to study?"
    me "Why?"
    show bb normal casual with dspr
    bb "We want to send a memo to your university asking them to send you as a squad leader."
    me "Awesome. {w}I already figured out that you called me here because you want something from me."
    "No, am I really supposed to get all these dithyrambs of gratitude?"
    "The adults looked at each other."
    $ meet('voice', "Old man")
    voice "Maybe we're too late. He's too quiet."
    "A gaunt man, sitting on the right hand of the director, draped in a gray jacket with a thin vertical stripe, distinguished from the others by the presence of some unusual badge on his lapel, came up."
    bb "You see, Semyon, we've got a kind of emergency here."
    "The director said."
    bb "And you have a very special status, so you know..."
    me "Understand what?"
    "The director nodded to the dried man, as if to say, «see?»"
    bb "Simply put, we are now under instructions to send you and Anatoly Ivanovich to the district center, where, already warned, doctors and psychologists are waiting."
    me "Spectacular. {w}What's the occasion?"
    bb "Physical trauma - one."
    "The director started curling his fingers."
    bb "Concussion - two."
    if not alt_day4_sl_cl_tut_iz:
        bb "Being in a noxious environment is three. {w}That's infrasound, by the way."
        me "By the way, are you going to do anything with it? Somehow it's not good that you have a working buzzer on camp property."
        me "That's not to say about the clubs being there."
        "He grimaced."
        bb "That shouldn't bother you. {w} It's more important to deal with our issue."
    bb "You've heard the instructions, according to them we have to put you in the car now and send you to the doctors and your parents."
    me "And then?"
    "He shrugged his shoulders."
    bb "You get treatment and we get to hold our own against another wave of inspectors."
    me "And you want to ask me to drop the claims?"
    "I guessed."
    show bb serious casual with dspr
    bb "Not really."
    "The faces of those present stretched, as if I'd fed each one a lemon."
    "No wonder, getting bound to some pioneer and blowing it by letting him know about it."
    show bb normal casual with dspr
    bb "We're not going to ask for the impossible - we really didn't look hard enough, and we're willing to be punished for it."
    bb "But we're thinking of you, too - because summer will be over for you. {w}Even if you're healthy as an ox, you'll have to spend at least a month in observation."
    bb "So if, all of a sudden, you're feeling good and you feel ready to spend the rest of your shift here, just say so."
    bb "If you don't... Then I'm sorry."
    menu:
        "You know…":
            $ alt_day_catapult = True
            "It's not that I'm all that eager to leave, especially now, after a freshly formed relationship."
            "But I guess I really should see a doctor."
            th "And also to see already what the world is like outside the camp."
            dreamgirl "What about Slavya?"
            th "What, what... {w}We're a couple now, so there's no getting away - I'll take her address from Olga and raid her house right after the hospital!"
            dreamgirl "Sounds like a good plan! {w}Do it!"
            me "If all this wasn't happening every day at least - I'd probably put up with the bumps I got."
            me "But I can't help thinking that the whole camp is turning on me."
            me "I just don't have time to recover."
            show bb serious casual with dspr
            "The director threw a wary glance at Viola at these words, and she nodded, confirming my words."
            show cs normal at right with dspr
            cs "A concussion by itself is not terrible, but all the other factors... {w}I recommend that he be transferred to inpatient treatment."
            show bb normal casual with dspr
            bb "Well."
            "Said the director, standing up."
            bb "Don't hold it against us, we really didn't think anyone would be so unlucky."
            bb "Anatoly Ivanovich?"
            "Dry man nodded and stood up."
            voice "Let's go, Semyon."
            "Olga caught up with me in the doorway and shoved something in my hand."
            scene bg int_admins_7dl with dissolve
            "Once in the hallway, I unfolded the paper and read:"
            "«Feoktistova Slavyana, 8(48223)…»"
            dreamgirl "And she's not clueless!"
            "The inner voice marveled."
            "Agreeing with that, I rolled up my greatest treasure and hid it in my pocket."
            voice "Don't worry about your stuff, Olenka promised to collect it and deliver it to your house after your shift was over."
            $ meet('voice',"Voice")
            "I shrugged it off."
            "Oak jeans and an old sweater were the last thing I was worried about right now."
            scene bg ext_admins_rain_7dl with dissolve
            "The old man led me out into the street, where the rain never stopped, and sat me down in the representative «Chaika»."
            show blink
            "I fell asleep as soon as the door closed behind me."
            $ prolog_time()
            stop music fadeout 3
            "And instead of waking up in a warm, lamplight alternative world with Gendas, seventeen-year-old pioneers, and perfect girls, woke up..."
            play music "<to 52.94>" + music_7dl["herc_death"] fadein 5
            "Time has chosen the limits of elasticity."
            "I couldn't fit anything else into those tenths of a second that had passed since..."
            if herc:
                scene bg int_store_7dl with fade
                "Since I was killed."
                "Even the greatest will to live is sometimes not enough."
                "Especially when you have to fight an ignominious end like this."
                play sound sfx_7dl["makarych"] fadein 0
                "Expanding gases push a lead ball - the only difference from a firearm is in the technical details."
                scene black with fade
                "And in my case, I also got the best gift of all, in addition to the bullet."
                "On the day I died."
                play sound sfx_bodyfall_1
                "Then that means it's my time."
                stop sound_loop fadeout 0
                play sound sfx_7dl["aunl"]
                $ sdl_persistent_inc("alt_lamp")
                show acm_logo_va_lamp with moveinright:
                    pos (1600, 1020)
                pause(7.4)
                scene gameover with flash
                with vpunch
            elif loki:
                "Since I was killed."
                "I don't know what could have caused it."
                "Frostbite or some kind of internal injury."
                "Or maybe it's just that I've fulfilled my mission here in this life, and it's time for me to move on?"
                scene bg ext_winterpark_7dl with dissolve
                pause(1)
                show spill_red
                "I didn't feel the will to live."
                "Not even the will to go back to the sweet illusion."
                "All I could do was grin my smashed lips at the eternal lantern."
                scene black with fade
                "And exhale the remnants of life."
                stop sound_loop fadeout 0
                play sound sfx_7dl["aunl"]
                $ sdl_persistent_inc("alt_lamp")
                show acm_logo_va_lamp with moveinright:
                    pos (1600, 1020)
                pause(7.4)
                scene gameover with flash
                with vpunch
            else:
                "Since the bus crashed into the water."
                "Which means it's time to close the book."
                "And put it on the shelf."
                "Or better yet, throw it in the oven."
                "Destroy it so that not even a memory remains."
                "After all, no one remembered me anyway, even when I was alive."
                play sound sfx_water_emerge
                stop sound_loop fadeout 0
                play sound sfx_7dl["aunl"]
                $ sdl_persistent_inc("alt_lamp")
                show acm_logo_va_lamp with moveinright:
                    pos (1600, 1020)
                pause(7.4)
                scene gameover with flash
                with vpunch
        "I'm okay":
            $ meet('voice', "Voice")
            $ alt_sp += 1
            "I cut off."
            me "I got here on my own, in case you didn't notice."
            show cs normal at right with dissolve
            cs "And not only that."
            "Viola grumbled, and I suddenly realized that she was perfectly aware of both the reasons for my excommunication and the place where I'd been walking all this time!"
            me "So I'm alive and well, on vacation, give me my letter of commendation."
            show bb smile casual with dspr
            "The director laughed in a low voice - and the tense silence broke."
            "People moved and hissed."
            "The room filled with life."
            show bb normal casual with dspr
            bb "I'll see you then... Mmmm... {w}On the departure day, I guess."
            "I nodded and, grabbing a piece of paper from the desk, left the room."
    stop music fadeout 3
    return

label alt_day5_sl_cl_mt:
    scene bg int_admins_7dl with dissolve
    play music music_list["your_bright_side"] fadein 3
    "The elements were raging outside."
    "And I, not wanting to get wet for a while, froze in the foyer, my nose pressed against the cold glass."
    "The camp was waking up, coming to its senses."
    if not alt_day4_sl_cl_tut_iz:
        "And it didn't seem to care about the creepy psychogenic crap standing at the very entrance."
    else:
        "It was going to live on - and it didn't care if things weren't all right in the Danish Kingdom."
    "That it was up to me to tell them whether to keep on resting or to stretch their backs and run around with a broom at their side for the rest of the shift."
    "What I really cared more about was not the early end of the summer, but - here I could afford to admit it - the possible separation from one over-active manipulative woman."
    "She spoke too much on the subject, and her tone was too dismissive."
    "So I too played along with her, laughed, shrugged my shoulders, and declared that it was all pampering."
    "…"
    "…"
    th "Damn manipulator!"
    th "And even here she managed to set me party politics."
    "The door slammed behind me - apparently the debriefing was over, and the counselors began to infiltrate their pioneers."
    "Soon, judging by the dialogues, there were four people left in the room, and they argued behind tightly closed doors."
    "I didn't bother to listen - Olga Dmitrievna stopped next to me."
    show mt smile pioneer with dspr
    mt "You've made a mess of your heroics, Semyon."
    "She smiled."
    show mt normal pioneer with dspr
    mt "You know a decent pioneer wouldn't make his comrades and counselors worry, don't you?"
    "I shrugged it off."
    me "So Shurik is not a decent pioneer?"
    show mt sad pioneer with dspr
    mt "Actually, I was talking about you."
    if not alt_day4_sl_cl_tut_iz:
        me "Did they turn off the buzzer?"
        show mt normal pioneer with dspr
        mt "Didn't you hear the music on the way here?"
        "I nodded."
        th "Could have guessed it, idiot."
    me "What are you doing on this cold, rainy morning?"
    th "Personally I'd like to take a three or four hundred minute nap!"
    show mt smile pioneer with dspr
    mt "First, I'd like to hear about your adventures."
    "The counselor began."
    if (not alt_day4_sl_cl_tut_iz):
        mt "If anyone here is hard of hearing, I can talk louder about letting you go only to the old camp and back!"
    show mt angry pioneer with dspr
    if (alt_day4_sl_cl_lf_solo in (1, 2)):
        mt "Especially since Slavya was going to go without you!"
        me "So what."
        "I snapped back."
        if alt_day4_sl_cl_lf_solo == 1:
            me "Slavya couldn't handle the search, and I found Shurik and brought him to camp!"
            mt "Thank you very much for that, but you shouldn't have gone alone!"
            me "Yes, yes... Teach me more about how to look for missing pioneers."
        else:
            me "Should I lie on my side and sleep now, while the others run around looking for a missing person? {w}You must think very highly of me!"
            show dreamgirl_overlay
            dreamgirl "I would like to thank the film academy separately, and…"
        show mt normal pioneer with dspr
        mt "Okay, don't pout. {w}Would you like to raise the flag tomorrow?"
        me "NO!" with vpunch
        show mt laugh pioneer with dspr
        mt "Why is that?"
    else:
        mt "Where have you been walking around all night?!"
        me "Are you really interested?"
        "I smiled ingratiatingly."
        me "We came back, and not just for nothing, but for the purpose of searching."
        show mt normal pioneer with dspr
        mt "At three o'clock in the morning, and then slept in the square almost till dawn!"
        mt "Tell me about it."
    "She took a pair of raincoats off the rack by the entrance, put one on herself, and shoved the other on me so that I had to catch air with my mouth for a few seconds."
    scene bg ext_admins_rain_7dl with dissolve
    play ambience ambience_7dl["rain"] fadein 3
    "We went out into a dank July morning."
    "Sometimes I think I carry the rain behind me like a mantle. {w}A gray mantle, the litmus of the lead color of my soul."
    "And here, in the midst of summer, I was not the least bit surprised that the bad weather had caught up with me after all."
    "On the doorjamb leading out of the abode of the strong camp of this one someone had already scrawled vertically, 'it can't rain forever.'"
    th "All children always react the same way to rain."
    "Although personally, I'm against forcing different behaviors on them artificially."
    "Forced diversity is as shitty an idea as forced uniformity."
    "Here's putting some intelligence into people's heads to give them the notion of choice - that's possible."
    "But we got distracted."
    "I wonder how I'd feel if I were actually seventeen years old?"
    scene
    $ renpy.show("bg ext_square_rain_day_7dl", what = Dawn("bg ext_square_rain_day_7dl"))
    with blind_r
    "Accompanied by a pretty girl - where to, by the way? To the canteen. {w}Oh, it's business, then."
    "Excuses."
    "Desperate thirst for rrromance - any display, even unintentional, even indirect, is taken almost as an overt display of feeling."
    "Touched each other's shoulders casually - touched me."
    "Kissed on the cheek - and also the corner of my lips caught!"
    "Taking me somewhere - we're on a date!"
    show mt smile pioneer with dspr
    mt "Semyon, if you keep looking at the sky, you'll fall!"
    "And if you both smoke, and you left her, since she never had cigarettes in the first place - forget about it. {w}An indirect kiss!"
    "Idiot."
    "A symptom, as applied to a girl called 'grooming,' as applied to a young man... Hmm."
    scene bg ext_square_rain_day_7dl with blind_l
    "I walked beside the counselor and told her about my adventures, listening to my allotted share of gasps and sighs."
    "And treated it as if she had agreed to go to the movies with me - and there to visit a cafe, a walk in the park, and the rest of the cultural program, according to which you wake up in the morning a carrier of STDs."
    "Just kidding."
    "In fact, despite a few extremely racy situations that arose between us, I couldn't treat Olga like a girl."
    "Apparently it's something professional, the ability to put yourself as an educator, a responsible person, a parent, if you will."
    "For Slavya it's like a walk to the moon - to learn and learn."
    "My date, in spite of her innate empathy, is a prick on the control mechanisms."
    "Though I've diligently shied away from the idea that I may have been the target all along. {w}That's something I will never believe."
    "As has been said many times yesterday - not that level. {w}Without being chosen, so we rejoice, wave, and diligently appreciate the honor."
    scene
    $ renpy.show("bg ext_square_rain_day_7dl", what = Dawn("bg ext_square_rain_day_7dl"))
    with blind_d
    "But I don't know about her, but I'm going to squeeze as much as I can out of our unintentional union."
    "After all, whose idea was it to start dating?"
    "With conversation the way to the dining room flashed by unnoticed."
    "I involuntarily pulled my head into my shoulders as I crossed the doorstep."
    th "Trying hard not to think of Slavya."
    th "I don't think, that's all."
    show dreamgirl_overlay with dspr
    dreamgirl "About who you're not thinking?"
    th "I'm not thinking about… Damn!"
    stop music fadeout 3
    stop ambience fadeout 6
    return

label alt_day5_sl_cl_breakfast:
    scene bg int_dining_hall_people_rain_7dl with dissolve
    play music music_list["everyday_theme"] fadein 5
    play ambience ambience_dining_hall_full fadein 5
    "The canteen wasn't crowded."
    "Even the cancellation of daily routines and all sorts of relaxation because of the rain could not get the pioneers out from under their blankets."
    "It's been known that sleep is sweeter in the rain."
    "The camp was slowly returning to existing - the hungriest pioneers found the strength to make their way to the temple of gluttony after all."
    show sl normal pioneer with dspr
    sl "So, how'd it go?"
    "She slumped down on the bench next to me."
    "I shrugged."
    me "Offered to go away and get some treatment on the mainland."
    show sl serious pioneer with dspr
    "Her eyes immediately became stern."
    sl "And you?"
    me "Isn't it obvious?"
    th "What kind of idiotic question is that?"
    me "Of course I said yes and left!"
    show sl laugh pioneer with dspr
    sl "Come on!"
    "She laughed."
    "Well, of course. If the girl asks idiotic questions, she's just a pretty silly girl, if she tries to control you, she's caring."
    "And if that's what you're trying to do, you'll be branded, oh I bet you, branded - an oligophrenic and a puppeteer. {w}Even though I can't figure out how those epithets fit together."
    "At the next table contented Syroezhkin landed and worked his jaws so hard it made my ears pop."
    "The Japanese girl and Lena also took a seat there, whispering vigorously and casting glances in our direction."
    "Every now and then their tandem would burst into laughter, and everything would subside. {w}Not for long, though."
    "A minute, maybe two, and the process would start all over again."
    "Slavya watched me for a while, leaning her head sideways, propping her cheek with her palm, womanly and sweet, and then she got tired of being silent:"
    show sl normal pioneer with dspr
    sl "Here."
    "Under my nose were three A4 sheets of typewritten text."
    "The first of them stated that Mironova Olga Dmitrievna had been severely reprimanded for a runaway pioneer, a maimed pioneer, and a very slightly wrinkled pioneer girl. Two of them."
    "The next, on the contrary, reported that thanks to the successful work done by the counselor with the parents, junior squads and camp staff, it was possible to localize the damage from the buzzer, for which she was commended on behalf of the camp administration."
    if alt_day4_sl_cl_tut_iz:
        "I looked up:"
        me "The buzzer?"
        sl "I don't know the details, but the cyberneticists had something broken again, something dangerous, so they..."
    "Well, the third sheet was an exact copy of my commendation paper. Except without the flashy heraldry on the backing."
    show sl smile pioneer with dspr
    sl "You're on special account now."
    "Smiled the girl."
    th "Yeah… Clown in a local town."
    show sl smile2 pioneer with dspr
    sl "They'll probably call you to work here next year."
    me "Not probably, but definitely. What about you?"
    sl "I've already been called."
    sl "We'll work together."
    me "That's it?"
    show sl normal pioneer with dspr
    sl "What do you mean?"
    me "Let's work together and that's it?"
    sl "Why?"
    "No, blonde is a diagnosis after all!"
    show sl serious pioneer with dspr
    sl "If you're talking about…"
    show sl normal pioneer with dspr
    sl "You know, not in the canteen."
    me "So you knew about everything from the beginning?"
    "I clarified."
    sl "I guessed."
    sl "I just got these orders. I'll have to pin them up on the bulletin board."
    sl "Will you come with me?"
    "I said yes."
    th "Damn it, I've heard that question somewhere before!"
    show sl sad pioneer with dspr
    sl "And Violetta Cernovna wanted to give us some printouts, but I think she changed her mind."
    "Slavya complained while we were getting dressed before we left the canteen."
    sl "I didn't even have time to look."
    me "Some kind of anti-tick stuff, what else could it be."
    show sl normal pioneer with dspr
    sl "So what! {w} If they're posted, they should know them!"
    "A girl stomped her foot."
    th "Usually girls get cranky and ask for a cake. {w}Sometimes new shoes."
    "Shit, but demanding following rules is kind of perverse."
    "It makes me want to talk her into doing something stupid."
    th "I don't know... Go skinny-dipping?"
    show dreamgirl_overlay with dspr
    dreamgirl "Great idea, by the way!"
    th "That's what I mean."
    stop ambience fadeout 6
    return

label alt_day5_sl_cl_ba_quest:
    scene
    $ renpy.show("bg ext_stand3_7dl", what = Desat("bg ext_stand3_7dl"))
    show rain_overlay
    with dissolve
    play ambience ambience_7dl["rain"] fadein 3
    "There was a piece of paper already hanging on the stand that was clearly medical in nature."
    "And on that piece of paper..."
    "Was an announcement that a lecture on puberty would be given to the pioneers of the first squad in the afternoon."
    th "Ohoho."
    "I suppressed a chuckle."
    th "Who's going to read? Will it be our sex bombshell?"
    scene
    $ renpy.show("bg ext_stand3_7dl", at_list = [zenterleft], what = Desat("bg ext_stand3_7dl"))
    show sl shy pioneer at cleft
    show rain_overlay
    with dissolve
    sl "Dr. V.C. Collider will be giving the lecture."
    "Confused, Slavya read."
    "Her ears were burning."
    me "You're already in suspense, aren't you?"
    "I nudged her in the side with my elbow."
    me "Expecting silly laughter and salty jokes from the redheads? Everyone else will be sitting there blushing."
    show sl smile pioneer at center with dspr:
        linear 2.0
    sl "And you?"
    "She turned around and got too close."
    hide sl
    show sl shy pioneer close
    with dissolve
    "The raincoat couldn't handle the water - in some places you could see the drenched shirt collar and the pioneer tie."
    "She almost unknowingly pressed herself against me, seeking warmth."
    "And I didn't push her away - what am I, stupid or something."
    me "I… I was, you know, read the highest theory on the subject today."
    scene
    $ renpy.show("bg ext_stand3_7dl", at_list = [zexitcenter], what = Desat1("bg ext_stand3_7dl"))
    show sl laugh pioneer
    show rain_overlay
    with dissolve
    sl "Fool."
    "The girl scolded me viciously and took half a step back."
    show sl normal pioneer with dspr
    sl "How long would you keep thinking that a girl needs attention?"
    "I was penitently silent."
    sl "That's right. Now you can hug me."
    sl "Only without the arms."
    me "How's that? A hug without arms."
    "With a sigh, Slavya took my palms and placed them against her sides."
    sl "At least like this. {w}And just try to move them up or down!"
    us "Tili-tili-dough, bride and groom!"
    "It came from the bushes."
    show sl shy pioneer with dspr
    "Slavya flinched, blushed. {w}Worried."
    "And I was fascinated."
    "There was something repulsive in the demeanor of the always confident and collected person."
    "Slavya tried to be perfect enough to do it - and she came out as a mannequin."
    "I liked her better alive."
    "A person shows who they truly is in an unfamiliar situation. {w}I don't think Slavya was teased much as a child - she was too busy."
    "The spark flashed and extinguished - Slavya have recollected herself."
    show sl sad pioneer with dspr
    sl "Ulyana, don't sit in the wet bushes."
    "Strictly she said."
    show sl serious pioneer with dspr
    sl "Or I'll tell them not to let you in the evening lecture, like a little girl."
    th "Scared the cat with a sausage!"
    "But Ulyana surprised me:"
    scene
    $ renpy.show("bg ext_stand3_7dl", at_list = [enterright], what = Desat("bg ext_stand3_7dl"))
    show sl normal pioneer at left
    show us calml sport at right
    show rain_overlay
    with dissolve
    us "Hey! I'm not a little girl!"
    show sl smile pioneer with dspr
    sl "And you're acting like one!"
    show us smile sport with dspr
    us "Why, what kind of lecture is going to be there? About what?"
    "I would've answered: «You're too young to ask such questions.» — and left."
    "But I'm not Slavya - she put her arm around the little one's shoulders and leisurely led her away, telling her something and gesturing vigorously with her free hand."
    "At the same time, both were oblivious to little things like the rain."
    me "Do I go then?"
    "I asked the backs."
    stop music fadeout 3
    scene
    $ renpy.show("bg ext_stand3_7dl", what = Desat1("bg ext_stand3_7dl"))
    show rain_overlay
    with diam
    sl "No!"
    "Oh, of course: if we get wet - everybody gets wet."
    "Another penny in my patience bank, another lesson to keep knocking the ground out from under her feet."
    ba "How's it feel, greenbeard?"
    "I turned around."
    show ba em1 uniform behind rain_overlay with dissolve
    "Nearby Sanich stood like an impregnable rock - a slant in the shoulders, steel in the squint, an anvil chin."
    "Most of all he now resembled an elephant suffering from constipation - there was a lot of him and he looked dull."
    play music music_list["into_the_unknown"] fadein 3
    me "Seen better days."
    if alt_day4_sl_cl_tut_iz:
        ba "You mean your flying off the roof?"
        ba "Yeah, I feel for you, trying to help, and getting this."
    else:
        ba "You mean that farter?"
        "He grimaced and rubbed his temples."
        ba "I agree, it's a rare piece of horseshit; I wish I could rip off someone's limbs with which they made it."
        th "Wow, he's got something other than lubonic humor, too."
        show ba normal uniform with dspr
        ba "How did the two of you last so long? {w}We barely knocked it out in four shifts."
        me "How exactly did you knock it out?"
        ba "There's a switch there. You saw it, I could see the outline of your little body in the dust."
        me "So they won't dismantle it and take it away?"
        show ba smile uniform with dspr
        ba "Should we? {w}Experimental installation, assembled, by the way, by our pioneers."
        me "Wasn't it Shurik's? Or else it might turn out that it drove him crazy and then he developed his own AI."
        show dreamgirl_overlay with dspr
        dreamgirl "Or vice versa - he went so crazy during the development of the AI that he then assembled an infragenerator."
        show blackout_exh3 with dspr
        dreamgirl "Or they combined to drive him mad..."
        "The recurrence of technology and madness so gripped me that I flinched when Sanich called out to me."
    show ba normal uniform with dspr
    ba "Not going home, are you?"
    "I nodded silently."
    ba "And rightly so. What's there to catch at home."
    show ba normal uniform:
        xalign .5 yalign .5 zoom 1.0
        linear 0.2 yalign .7 zoom 1.15
    show rain_overlay behind ba
    with dissolve
    "He chewed his lips a little, and then he said,"
    ba "Wanna stay as an assistant for the third shift?"
    "I dropped my jaw on the ground and looked for it for a long, long time in the dirt."
    me "Excuse me?!"
    "Sanich cracked his knuckles."
    ba "I've been watching you - you may be a wimp, but you've got sense."
    "Thanks a lot."
    ba "Obviously, I wouldn't trust you to see my daughter off to school, but you could probably officiate matches and conduct competitions."
    "The offer was flattering. {w}It was a great offer, no need to be modest!"
    "And considering that Slavya, with some of her diplomatic channels, would be able to stick around with me..."
    "I mean, we'll have a whole summer together."
    "But after thinking about it, I decided against it."
    me "I don't know how to put it. But I guess I can't stay here any longer than I have to."
    me "Call it the ramblings of a wimp and we'll laugh together later - but for now I'll listen to my intuition and get to town."
    scene
    $ renpy.show("bg ext_stand3_7dl", what = Desat("bg ext_stand3_7dl"))
    show ba normal uniform behind rain_overlay
    show rain_overlay
    with dissolve
    ba "Suit yourself."
    me "At least just to tell my parents that I'm okay."
    "For some reason, I really wanted to convince the big guy that I wasn't rejecting his offer."
    th "Since when did I care about his attitude?"
    me "Plus all this questionable stuff on the territory..."
    if alt_day4_sl_cl_tut_iz:
        me "Although I declined the examination, I'm not sure if it's really okay."
        me "I just don't want to cause too much trouble. {w}I'll get through this before I leave, and that's okay."
    else:
        me "Plus I talked to Shurik at night."
        "Sanich, frowning up to that point, immediately calmed down."
        "Nodded:"
        show ba smile uniform with dspr
        ba "Ah, I see. And you don't understand what kind of voices he heard?"
        ba "Or is it more frightening to you that you can get to a bomb shelter under the camp?"
        "I shook my head again."
        me "I'm embarrassed by all kinds of side effects of these hikes."
        "I told him about the map, how I navigated the dungeon, how I perceived the information as if put on a far shelf for no use."
        show ba em1 uniform with dspr
        ba "And these are also familiar symptoms."
    if alt_day4_sl_cl_lf_solo == 2:
        ba "Shurka came by himself yesterday, you know that?"
        "I nodded."
        ba "And he came out of the old vent."
    "Sanich noticed that I kept looking in Slavya's direction."
    ba "Get out already."
    hide ba with dspr
    "He clapped me on the back, clumsily turned around, and went to his indoor room."
    "To sleep."
    if not alt_day4_sl_cl_tut_iz:
        th "A guileless man, simple as a stick, and look, he, too, has his own story."
        "It's not just that sometimes little eyes are dead, a dispenser of pain that has no place on the concrete slabs of the abode of happiness."
        "The overwhelming conceit of a man who can't communicate without sneering, silent nights and thinking how nice it would be to say to hell and close the door behind him."
        "To nod to the sea as an acquaintance, to sit on the sand and pour the scalding hatred into my throat, counting the seconds as drops, torn tendons, hormonal malfunctions, diseased livers."
        "And let myself go - to where the road to big sports was still open."
        "I had no way of knowing that Sanich, once a hopeful junior athlete, hope and support, had retired."
        "Since then, only with a whistle and a stopwatch on the treadmill."
    scene
    $ renpy.show("bg ext_stand3_7dl", what = Desat1("bg ext_stand3_7dl"))
    show rain_overlay
    with fade
    "I had to put up a bit of a fight with Ulyana, who yelled about stamens, before I could take the activist away from her."
    show sl normal pioneer at cleft behind rain_overlay
    sl "Semyon, I wanted to ask you something."
    "Slavya looked a little strange. Her fingers were tugging at her braid nonstop, and her gaze was unwilling to focus on me."
    me "Yes, ask for whatever you want!"
    "I mentally imagined spending all day in camp, working side by side with her."
    "And why did I expect such a request? Do I, MYSELF, really want to do something useful for once?"
    dreamgirl "Crazy, no other way!"
    sl "I'm thinking of going back there."
    me "There? Where, actually, is that there?"
    "I love this feminine stuff: take it THERE, bring it THERE... No specifics."
    sl "I think we should go back to the tunnels under the old camp. It feels so..."
    me "Why should we go there, Slavya? Shurik's already in camp, and Olga's probably..."
    sl "Well, I just feel it. I don't know how to explain it. It's like I forgot something important there."
    dreamgirl "Oh, another one to the madhouse. And I was wondering why you two got together so fast."
    me "I don't know. Are you sure? Is everything okay?"
    if alt_day4_sl_cl_lf_solo == 2:
        "I expected anything but that kind of suggestion. Even on the surface that place has an unpleasant feeling, let alone underground."
    show sl serious pioneer at cleft behind rain_overlay
    "Slavya finally looked at me. You could tell by the look on her face that something interesting was going on in her head."
    sl "I want to go over there and block everything off so none of the kids get lost again."
    "I wondered. And really, it's like two fingers to get lost in that dungeon. And look for the other pioneers, or don't let Random, Shurik, who decides to do pretzels again."
    "Any way you slice it, being near the best pioneer in the camp also meant that if yesterday's situation were repeated, Olga would immediately have a couple of candidates. So with experience, too."
    "Slavya wouldn't pass, and I wouldn't let Slavya go anymore."
    "Still, I had a lingering feeling that something was wrong. Something was wrong with Slavya. But I pushed that obsession aside. It's much more important to help the girl now!"
    "I sighed."
    th "I had the misfortune to get in touch with her."
    "But there was nothing to be done. If I'd said no or started talking her out of it, she will go there alone surely."
    "I had to go along with the assignment."
    "We decided to split up so we could pack up faster."
    hide sl with fade
    "As soon as Slavya left, Lena came around the corner."
    show un normal pioneer behind rain_overlay
    with dspr
    un "H-Hello."
    "She greeted me, stopping in the distance."
    if lp_sl < 17:
        me "Hi."
        me "What are you doing here?"
        un "W-well..."
        show un serious pioneer with dspr
        un "I heard your conversation. May I come with you?"
        me "No."
        show un serious pioneer with dspr
        un "B-but yesterday Slavya…"
        "She doesn't seem to take hints at all."
        me "Listen."
        "I sighed."
        me "Slavya is a kind girl, and she feels responsible for you."
        me "She will always support you and take you with her."
        show un shocked pioneer with dspr
        me "But you must understand that you are not welcome here."
        me "You're in the way. {w} In her and mine."
        show un cry pioneer with dspr
        un "But I just... I just..."
        "She sobbed and ran away."
        hide un with easeoutbottom
        dreamgirl "You hurt the girl. Glad?"
        th "Shut up."
        "I looked after her, and something stirred in my chest again. Anxiety?"
        "Yes, very much so. Because I couldn't figure out why two pioneer girls would want to go back all of a sudden."
    else:
        "I only twitched my shoulder in annoyance."
        me "Hi. {w}Sorry, I'm on my way out."
        show un shy pioneer with dspr
        un "Shame… Oh."
        "Sure, you could point out that we're a couple now, and we have to do everything together."
        "But it's kind of dishonest, isn't it?"
        hide un with dissolve
        "Lena wanted to add something else, but I had already turned my back on her."
    with fade
    if alt_day4_sl_cl_lf_solo == 2:
        "Twenty minutes later the packing up was over, and we met at the same place."
        "I, as the pioneer in charge, was handed a bunch of keys. I guess Slavya decided after that time not to take any more chances."
        "Slavya surprised me when she went in the opposite direction to what was expected."
        scene bg ext_square_rain_day_7dl at zenterleft
        show sl normal pioneer at cleft
        with dissolve
        me "Isn't the old camp the other way?"
        sl "You'll see."
        "She walked around Genda and tapped on the barely visible ventilation grate."
        sl "There's an emergency entrance."
    else:
        "And twenty minutes of packing later we met at the vent."
        "I, as the pioneer in charge, was handed a bunch of keys. I guess Slavya decided after that time not to take any more chances."
        "After that I opened the grate,"
        if (alt_day4_sl_cl_lf_solo in (0, 3)):
            extend " and we returned to where we came from yesterday."
        else:
            extend " and we went back to where I barely escaped from yesterday."
    stop music fadeout 3
    stop ambience fadeout 6
    return

label alt_day5_sl_cl_catacombs:
    scene bg int_mine_exit_day_7dl with dissolve
    play ambience ambience_catacombs_stones fadein 3
    play music music_7dl["nowyouseeme"] fadein 3
    if alt_day4_sl_cl_lf_solo == 1:
        "I scouted the route yesterday, so I wasn't really surprised."
        "It's my second time here, but damn it, I keep getting worried!"
    elif alt_day4_sl_cl_lf_solo == 2:
        "I hope Slavya knows her way around here, at least approximately."
        "Otherwise I was feeling a little uncomfortable."
    else:
        "Thank goodness to random, we scouted the route to the catacombs yesterday and didn't have to go at random like we did last time."
        "This is my second time here, but damn, I keep getting worried!"
        "Probably would have been worried even if we'd come here for the fifth, tenth time."
    "Because - government tunnels, bomb shelters, and the transition to the lower level!"
    if alt_day4_sl_cl_lf_solo == 1:
        "Yesterday I raced here like a locomotive, I didn't get a good look at anything."
    elif alt_day4_sl_cl_lf_solo == 2:
        "I didn't get here yesterday, I didn't see anything, I didn't walk around the dungeons."
    else:
        "Yesterday we took the shortest route and didn't have time to appreciate all the charms of the dungeons."
        th "But today we can go for a walk - because we're volunteers who don't depend on anyone!"
        "This time we were more seriously equipped - we each had a flashlight and a roll of rope, and Slavya had a knot of sandwiches hanging behind her back in case we got stuck here for a while."
    "The first door was a heavy one, with a swivel wheel."
    play sound sfx_metal_door_large_close_basement
    scene bg int_mine_room with dissolve
    "We opened it, but we didn't let it slam shut, and I marked it on the plan, which will have to be the Treasure Map!"
    "Though what treasures are there..."
    "Nothing even semi-precious - thermal utilities, a half-working pump station, and glass bottles in two layers on the floor."
    show sl normal pioneer with dspr
    sl "This place should be cleaned up."
    "Slavya nodded her head thoughtfully."
    me "Do you want to get busy?"
    show sl surprise pioneer with dspr
    sl "What do you mean?"
    me "I'm saying if you want to clean up in here, I won't bother you."
    show sl sad pioneer with dspr
    sl "Come on."
    "She pouted, guessing that I was just teasing her."
    if alt_day4_sl_cl_lf_solo != 2:
        "Meanwhile, the door, which the run-in Shurik had slammed shut tightly, was ajar."
        "As if that weren't enough, the wood near the handle was shredded, as if someone had a sharp knife and lots and lots of free time."
        "Yesterday I either didn't see it or wasn't paying attention."
    "After marking this door, too, we went out into the tunnels."
    scene bg int_mine_crossroad
    with dissolve
    play ambience ambience_catacombs_stones fadein 3
    "Here everything was absolutely expected - a narrow gauge for the removal of fossils, hooks on the fastenings under the lantern."
    "Farther down the tunnel one could also find abandoned overalls, an almost new pick, only slightly bent, and a shaped glass lampshade for a kerosene lamp."
    "The latter was for some reason without the lamp itself."
    if alt_day4_sl_cl_lf_solo == 2:
        "I was expecting diablo-like caves, rocks, and caverns with a trunk in the deepest as... I mean, the most inaccessible area."
        "The fact that we would find ourselves in a quite ennobled coal mine was a little confusing."
    else:
        "Now that we knew about the presence of these tunnels, what they were, and even had a rough idea of the layout of the communications, the place had lost a fraction of its creepy charm."
    "I still inexplicably kept worrying, though."
    "It was a strange feeling. Or rather, a premonition."
    "And it wasn't reassured by the rails running leisurely back beneath my feet, nor by the super-strong lantern-blower, nor by Slavya's hand in mine."
    scene
    $ renpy.show("bg int_mine", at_list = [zenterleft], what = Notch("bg int_mine"))
    with dissolve
    play music music_7dl["sammy"] fadein 5
    if alt_day4_sl_cl_lf_solo != 2:
        "Because somewhere out there, in places that haven't known light for decades, there was something..."
        "...that scratched Shurik."
        "It was in the presence of the bespectacled coward, or in a close encounter with a blonde, that I braved and held my chest like a wheel."
        "Such scratches can only be made by hitting from the top down, you can't hurt yourself that way."
    "It was blowing out of the darkness, damp and chilly, involuntarily conjuring up thoughts of being buried alive and other pleasant things associated with darkness, water and cold."
    me "By the way."
    "Said I, shrugging my shoulders."
    if alt_day4_sl_cl_lf_solo == 1:
        me "While I was poking around yesterday, there wasn't a cart here."
        show sl normal pioneer with dspr
        sl "Maybe it's..."
        "I shook my head."
    elif alt_day4_sl_cl_lf_solo == 2:
        me "There might be some subterranean nastiness here."
    else:
        me "Yesterday, when we passed through here, there was no cart here."
        me "The pick was lying here, crumpled and rusted."
        show sl normal pioneer with dspr
        sl "Maybe it's..."
        "I shook my head."
    me "You know what?"
    me "Don't let me out of your sight for a moment."
    "I ordered, feeling the twilight thicken around us, against which any lantern was powerless."
    show sl surprise pioneer with dspr
    sl "What's the matter?"
    me "Something feels off about this place."
    play sound sfx_ghost_children_laugh
    play sound2 sfx_far_steps fadein 1
    "At the edge of hearing someone laughed, footsteps rang out."
    if herc:
        "Without saying a bad word, I put the girl behind my back in one motion."
        "Used to it, not the first time."
        "I don't have a weapon, of course, but my skills are still there."
        sl "What are you..."
        me "Silence, woman. {w}There's danger ahead."
        dreamgirl "What a lovely example of chauvinism!"
        $ alt_sp += 1
        $ lp_sl += 1
    elif loki:
        menu:
            "Hide Slavya behind the back" if (alt_sp >= 2):
                $ alt_sp += 1
                $ lp_sl += 1
                "I guess you could call it instinctive action."
                "But I managed to slide Slavya behind me and get my flashlight ready before I realized what I was doing in the first place."
                "Slavya, for some reason, didn't dare argue, dutifully lounging in the rearguard."
            "Heard that?":
                $ lp_sl += 1
                $ karma += 20
                sl "What?"
                me "Footsteps!"
                show sl serious pioneer with dspr
                sl "I didn't hear anything."
                me "You know what, stick with me, okay?"
                "Slavya wanted to argue something, but she looked at me again and nodded."
            "What the hell was that?":
                sl "What?"
                $ alt_sp -= 1
                $ lp_sl -= 1
                me "I don't know! {w}But there's something in the dark!"
                sl "You think so?"
                sl "Maybe I'll go first, then?"
                "I've given it some thought."
                me "Come on!"
    else:
        if lp_sl > 17:
            menu:
                "Cover Slavya":
                    $ alt_sp += 1
                    $ lp_sl += 1
                    "There's no way I could explain what I did to myself."
                    "It just so happened that all of a sudden there was my carcass between the potential danger and Slavya."
                    "Hero? Please."
                    "Just experiencing blows to an empty head seems to be what I'm best at."
                "Hide":
                    "I froze and listened."
                    "I think there was someone out there in the dark."
                    sl "What happened?"
                    me "I think I heard something."
                    sl "Which way?"
                    "She stood beside me, and I pointed the flashlight beam in the direction."
                    sl "No one."
                    me "But I heard something!"
                    sl "Look, let me go first."
                    me "Let's go beside each other."
        else:
            me "Did you hear that?"
            sl "What?"
            me "I don't know! {w}But there's something out there in the dark!"
            sl "You think so?"
            sl "Maybe I'll go first, then?"
            "I've given it some thought."
            me "Let's go beside each other."
    scene cg d4_fz_catac_sl_7dl with dissolve
    "We continued our fascinating expedition into the depths of the local catacombs."
    "Why didn't I escape? It seemed the easiest thing to do would have been to register someone's presence and get back to camp - we had no task of playing the protagonists of some slapstick horror movie."
    "I can't tell."
    "But noooo - we want an opportunity to squirm as a superhero without fear or dill."
    "And then there's Slavya."
    me "Listen carefully, I don't think we're the only ones here."
    "The girl nodded obediently."
    "We moved for about half an hour, noting the spurs and doors, before the tension that had constrained me little by little began to release."
    me "Were you aware that you had something here?"
    "Slavya shook her head."
    scene
    $ renpy.show("bg int_mine", what = Desat("bg int_mine"))
    show dreamgirl_overlay with dspr
    "I froze at a half-step."
    scene
    $ renpy.show("bg int_mine", at_list = [sdl_transform9], what = Notch("bg int_mine"))
    "One of the crests has been marked. And how!"
    if alt_day4_sl_cl_lf_solo == 2:
        "A stroke of claws, appropriate on the paw of a large predator."
    else:
        extend " The same stroke that adorned Shurik's cheek."
    me "Did you see that?"
    sl "Marked it."
    "Slavya added the details to the «map»."
    scene
    $ renpy.show("bg int_mine_crossroad", at_list = [zenterleft], what = Notch("bg int_mine_crossroad"))
    with dissolve
    "And another fork."
    if alt_day4_sl_cl_lf_solo == 1:
        "Yesterday I was in a certain, clouded state of consciousness, so I couldn't remember where and in what places the crossroads were scattered here by someone's generous hand."
        "And this fork, too."
    elif alt_day4_sl_cl_lf_solo == 2:
        "I'm going to get lost here and look for a way out for three years..."
    else:
        me "Remember how we walked yesterday?"
        show sl smile pioneer with dspr
        sl "Actually, it was you who led us."
        "Slavya smiled."
        show sl normal pioneer with dspr
        sl "And with a look like you walk here every day."
    "I sighed."
    me "Okay, let's try going left."
    play sound_loop sfx_far_steps fadein 1
    "From the depths of the dark tunnels came a sound very much like heavy footsteps."
    "If I weren't such a hardened veteran of underground prospecting, I'd chicken out, no less!"
    dreamgirl "Look at this Vietcong gorrilla."
    dreamgirl "Scared one and a half times by the wind howling, and you're already a Veteran. Yes. With a pedal for valor."
    if alt_day4_sl_cl_lf_solo != 2:
        "In fact, I just noticed when I jumped down from the top tier that the acoustics here do very curious things to the most ordinary sounds."
        "In those adits where groundwater has already had time to undermine the soil - and coal seams suffer from this - the evaporation creates condensation, the condensation creates water, the droplets falling from the ceiling."
        "And that's the drop hitting the surface of the water, filtered through the acoustic filters of the local catacombs, and it sounds like the step of some monster."
        "I also usually do this."
        show sl scared pioneer with dspr
        me "O!"
        "Abruptly I shouted out and, looking up at the ceiling, clapped my hands."
        "Somewhere far, far away there was a piercing squeak and the flapping of numerous wings."
        "I felt them more than I heard them."
        show sl serious pioneer with dspr
        sl "Semyon, can you not mess around?"
        "The girl looked at me sternly."
        sl "You scare the hell out of me."
        me "I'm sorry."
        "There wasn't an ounce of remorse in my voice."
        "And even the hypothetical scratch runner somehow seemed like something distanced, put out of bracket."
    "I picked up a pebble from the ground and threw it into the darkness."
    me "See? There's nothing scary ther..."
    "The drowsiness that was coming from lack of sleep was gone in an instant."
    scene
    $ renpy.show("bg int_mine", what = Desat("bg int_mine"))
    with dissolve
    play sound sfx_lena_hits_alisa
    "From the sound of it, the rock hit something soft."
    "I pointed the flashlight there instantly."
    scene
    $ renpy.show("bg int_mine", what = Notch("bg int_mine"))
    with dissolve
    "Nothing."
    show sl surprise pioneer with dspr
    sl "It seems..."
    me "I hit someone."
    "I nodded."
    show sl normal pioneer with dspr
    sl "You have a talent for making enemies."
    "Slavya clung to me, trembling lightly."
    "As if seeking protection."
    "And I, acting automatically, put my arms around her."
    "And I shone the light over her shoulder."
    stop sound_loop
    scene cg d5_sl_snark_7dl
    show blackout
    with flash
    "The blurry light of the flashlight reflected in someone's huge, black, almost blank eyes, moved on."
    "I was paralyzed with fear."
    "I swung the flashlight back."
    scene cg d4_fz_catac_sl_7dl with dissolve
    play music music_7dl["dead_silence"] fadein 3
    "It's empty."
    me "I think we'd better get out of here."
    scene
    $ renpy.show("bg int_mine_crossroad", what = Notch("bg int_mine_crossroad"))
    with dissolve
    show sl normal pioneer with dspr
    sl "Mmm..."
    "All this time Slavya has been basking on my chest, making no attempt to get out."
    sl "Why?"
    me "Because there's someone here, that's why!"
    show sl shy pioneer close with dspr
    sl "So what?"
    "She rubbed on my cheek like a cat."
    show sl smile2 pioneer close with dspr
    sl "Five minutes ago it didn't embarrass you."
    me "I saw it."
    show sl normal pioneer close with dspr
    sl "Really?"
    me "It was standing behind your back."
    "Slavya froze."
    show sl sad pioneer close with dspr
    sl "W-what did you just say?"
    me "I said it's behind your back."
    show sl surprise pioneer with dspr
    sl "Where?!"
    "She shrieked."
    "Next at the same time she managed to jump up, turn in mid-air, turn on the light source and..."
    "Nothing."
    show sl normal pioneer with dspr
    sl "Semyon..."
    "She began."
    me "I'm not kidding!"
    show sl serious pioneer with dspr
    sl "And so it..."
    th "It moves very quietly, and the splashing sound of the water disguises it."
    me "Against the wall."
    "Without too much politeness, I pushed her aside."
    "The girl didn't have time to regroup, so the blow knocked the spirit out of her."
    hide sl with easeoutleft
    play sound sfx_fall_grass
    "Something rushed past us at full speed, slammed into the wall, didn't make the turn, and as it was, on all fours, dashed off into the darkness."
    scene
    $ renpy.show("bg int_mine_crossroad", at_list = [sdl_transform10], what = Notch("bg int_mine_crossroad"))
    sl "W-w-what w-w-was t-t-t-that."
    "Gritting her teeth, Slavya asked."
    me "Do I know? It's some wild, tunneling shit. {w}I suspect we can't get rid of it with flashlights, so..."
    show dreamgirl_overlay with dspr
    dreamgirl "What? Move to the surface, closing the doors behind it, and hope it starves to death while it's locked up?"
    dreamgirl "But it didn't eat Shurik! {w}It must be feeding on something else."
    th "Maybe it prefers a different blood type."
    "Now I wish I had a machine gun or a grenade launcher."
    "Just holding the perimeter with a gun in hand."
    if not herc:
        dreamgirl "You, who have never served, could really use it!"
        th "Yes, I can do something!"
        dreamgirl "Yeah, piss your pants from the sound of a machine gun indoors, maybe."
    "Slavya, moving nearby, froze."
    th "I have a bad feeling about this."
    scene cg d5_sl_snark_7dl
    show blackout
    with flash
    "I traced the direction of her gaze with the flashlight beam-right in front of us was the same creature, the twin brother of the one that had remained somewhere behind us."
    "It was grinning and hiding with one paw its eyes, watery from the bright light."
    me "This way."
    scene
    $ renpy.show("bg int_mine_crossroad", at_list = [sdl_transform10], what = Notch("bg int_mine_crossroad"))
    "I spotted an unmarked narrow crevice behind me and dragged Slavya behind me."
    me "Hurry up."
    "Behind me someone shrieked, something muffled clang."
    "And I turned around slowly and slowly."
    "Behind me Slavya was blowing on battered fingers, and at her feet on the ground a stunned creature was shaking its head."
    me "Go, go!"
    scene
    $ renpy.show("bg int_mine", at_list = [zentercenter], what = Desat("bg int_mine"))
    "I dragged us along the crevice I found."
    play ambience ambience_lake_shore_night fadein 2
    "Purely psychologically, I would feel much more confident if I could hear footsteps behind me."
    "But, as luck would have it, of our whole touchy quartet, I was the only one making various noises and stomping as we ran - both Slavya and the creatures chasing us moved softly, noiselessly."
    scene
    $ renpy.show("bg int_mine_water_7dl", what = Desat("bg int_mine_water_7dl"))
    "I swore through my teeth."
    sl "What is it?"
    scene bg int_mine_water_7dl
    me "Back!"
    "Slavya threw a glance over my shoulder, dabbed the flashlight light on the black surface of the water, scattering a bunch of bunnies, and turned around and ran ahead."
    scene black with diam
    stop ambience
    "At first I thought I was glitching."
    scene
    $ renpy.show("bg int_mine_door", what = Dawn("bg int_mine_door"))
    with dissolve
    "But when I turned off the flashlight, I realized that this was the real thing-it was the ever-familiar door to the switchyard in front of us."
    "How we'd managed to make a circle is unclear - apparently this path was the roundabout way to where it all began."
    "I ran to the door and grabbed the handle."
    "I pulled away in disgust as my fingers got stuck in something sticky and slimy."
    th "Well..."
    show dreamgirl_overlay with dspr
    dreamgirl "There's no time to play Miss Squeamishness here, pull!"
    with vpunch
    "The subconscious, as usual, was businesslike and strictly substantive."
    play sound sfx_metal_door_handle_rattle
    "I grasped the metal handle again and yanked the door up as hard as I could - it had to be lifted so it could open."
    "But I didn't have time to do anything else."
    "Something big and heavy jammed into me."
    scene
    $ renpy.show("bg int_mine_door", at_list = [zentercenter], what = Dawn("bg int_mine_door"))
    show ftl_anim with Shake((0, 0, 0, 0), 0.3, dist=10)
    play sound sfx_punch_medium
    pause(2)
    scene black with pixellate
    "And then there was silence."
    stop music fadeout 3
    return

label alt_day5_sl_cl_fog:
    scene anim prolog_1 with dissolve
    play music music_7dl["sneakupon"] fadein 3
    "My corpse is probably being finished off by those eyeball critters right now."
    "And there's another blue-eyed one next to me, belonging to an over-active pioneer girl."
    "{i}I've always been fascinated by death - I wanted to look over the edge and see what was there.{/i}"
    "{i}And now I realize.{/i}"
    "{i}There's nothing there.{/i}"
    "{i}You are alone in the void, and all you have is yourself.{/i}"
    "{i}Death. The highest form of loneliness.{/i}"
    "{i}You talk and talk to yourself, unable to do anything or even move.{/i}"
    "{i}As a result of the constant dialogue with yourself, your consciousness begins to disintegrate.{/i}"
    "{i}And after a thousand years, you become an unconscious unit, a sexless Id, fit only to become the larva of a future new soul.{/i}"
    "And the thought buzzes in my ear that I don't really care about myself, but it's a shame I didn't keep one girl safe."
    "I mean, we just started dating."
    "Okay, we agreed to start dating."
    "I guess."
    with flash
    "Finally, I was tired of doing nothing and being nowhere, and I wished:"
    me "Let there be something."
    scene white with diam
    "As soon as there was nothing my little power could do but move photons and electrons, there became light and electricity."
    "Let there be light, yes."
    "There was something humming beneath my feet, some enormous objects rushing past at a tremendous speed."
    "Or us?"
    scene bg ext_sky_7dl with dissolve
    "{i}Most of all it reminded me of flying in the sky as I had imagined it all my life, as I had seen it in my dreams and on the blue screen.{/i}"
    "{i}No side effects, like throat tearing wind or doggy cold - no, just speed, sky and clouds.{/i}"
    "{i}It's just that if a person really could fly, that's what it would look like - leisurely levitating himself between the cumulus clots of fog.{/i}"
    "{i}One object on the ground caught my attention, and I slowed down a bit.{/i}"
    "{i}Lowered.{/i}"
    "{i}It was a man.{/i}"
    "{i}Rather, even a teenager.{/i}"
    "{i}He reminded me a lot of someone.{/i}"
    "{i}He was surrounded on all sides by gray fog, caressing, getting under his arm, almost purring, and the guy was smiling, and in the middle of nowhere, as if to his best friend, cheerfully talking about brigantines, scarves, rapiers, and swan's fidelity.{/i}"
    "{i}His speech was strange and odd - at first punctuation marks, pauses for breathing in and out began to disappear from a coherent monologue, then unnecessary parasitic words, syllables, prepositions.{/i}"
    "{i}Whole words, finally.{/i}"
    "{i}And the fog was agitating and agitating, swirling around the boy.{/i}"
    "{i}He didn't seem to feel or notice anything.{/i}"
    "{i}And why.{/i}"
    "{i}He intercepted my gaze - and I turned away, shuddering as if struck.{/i}"
    "{i}I've never seen such spiritual eyes.{/i}"
    "{i}Except at the camp, in Slavya.{/i}"
    "{i}Her name hurt my heart.{/i}"
    "I've been here for too long."
    if alt_day4_sl_cl_lf_solo != 2:
        "Calling out my gut feeling from yesterday, I imagined the object to look for and, looking around, mapped out a direction."
    else:
        "Evoking my acquired sense of direction, I set the criteria for the search and, looking around, mapped out a direction."
    "I turned around to say goodbye - he was still looking at me like that."
    "And shuddered again."
    "It was still the same bloke with the burning eyes."
    "Except there was no more fire in his eyes."
    "The button eyes of a teddy bear sometimes look more alive than the empty pupils staring at me."
    "The fog was gone - whatever that thing was, it left, having finished its business."
    "It was just the two of us on the shore."
    "A brigantine was slowly rolling away from the shore."
    "On board, hiding in the shadow of a scarlet sail, was a short, frail girl with long blond hair of the most unusual hue."
    th "Lunatic."
    "For some reason it popped into my head."
    th "She did wait for her sails after all."
    "And somewhere on the bow they were already opening the wine barrels, but I was already flying on, torn and chased by a feeling that told me the shortest way."
    "Just keep moving in your chosen direction, and..."
    "At one point I flew with all my might into a sort of obstacle, soft and warm, and tried to push it away from me."
    "And she cried out and slapped me on the arms."
    "And I came to my senses."
    stop music fadeout 3
    scene
    $ renpy.show("bg int_mine_room2_7dl", what = Desat("bg int_mine_room2_7dl"))
    show unblink
    play ambience music_7dl["ambience_safe"]
    "I was in some half-dark room, lying on something soft."
    show sl angry pioneer with dspr
    sl "You haven't had time to have a relationship, and you're already trying to be a bobblehead?"
    "Slavya sternly reprimanded me."
    "I was lying on her lap."
    "And she was sitting on the floor with her feet under her."
    "The flashlight was pointed along the wall, which gave us quite a bit of light."
    me "We... Where?"
    show sl serious pioneer with dspr
    sl "You don't remember anything?"
    me "The way something hit me, I remember."
    sl "After that race?"
    "She shook her head and pulled a map out of her bag."
    show sl shy pioneer with dspr
    sl "I tried to put some things on where I remembered.{w} Obviously I didn't get everything."
    me "So?"
    me "Not everything, not everything."
    me "We should have a whole expedition out here, not just the two of us. {w} And those things!"
    "I reluctantly broke contact between my head and her knees."
    me "Let's go up to the surface, since somehow we ended up at the beginning of the journey."
    "Slavya looked at me with some very strange look."
    show sl normal pioneer with dspr
    sl "Semyon, we're not in the control room."
    me "But I remember the door exactly, and..."
    show sl smile pioneer with dspr
    "She smiled embarrassedly."
    sl "No, there was a door. But it wasn't the control room. {w}Some other room."
    scene bg int_mine_room2_7dl with diam
    "I, not believing it, picked up a flashlight and illuminated the walls."
    "That's right."
    "If this were the same room, there would be a lot of glass, profanity on the walls, and different valves with controls."
    me "And you..."
    sl "I don't know where we are."
    sl "It looks like it's a hut somewhere inside the maze. {w}We couldn't get around the whole perimeter that fast."
    show sl normal pioneer with dspr
    sl "And the door is similar, yes, but, by the way, it opens the other way."
    me "Yeah, can you tell me what happened?"
    me "I admittedly expected to wake up in the stomach of one of those critters in a digested state."
    show sl shy pioneer with dspr
    sl "W-well..."
    "I wasn't sure in the darkness, but she seemed confused."
    show sl normal pioneer with dspr
    sl "I didn't have time to slow down... {w}You softened the fall."
    th "And then you hit the empty head again."
    th "And passed out."
    sl "And I slammed the door, they can't open it now."
    me "Well, now that we're all back on our feet, let's try to get to the exit."
    sl "But..."
    show sl serious pioneer with dspr
    sl "What about snark?"
    me "Snark?"
    sl "Bujum."
    th "What's that she's already consumed?"
    show dreamgirl_overlay with dspr
    dreamgirl "Carroll, you unpaved village."
    th "Who's to say! We share one skulls."
    me "But the snarks are those four-legged ones in gas masks."
    "I remembered."
    dreamgirl "The four-legged ones are the snorks. And where do you see a radiation zone here?"
    show sl normal pioneer with dspr
    sl "They are four-legged. {w}And whether they have gas masks I don't know, I'm sorry, I didn't look."
    sl "I don't remember telling you, but on the third day, when it was raining too, the counselor gathered us together for a candle and we told all kinds of interesting things."
    sl "Electronik told us about the book by Veltistov, after the hero of which his parents named him."
    sl "And Miku couldn't think of anything else to say except about the last book she read - just Lewis Carroll."
    sl "Shurik also got so funny when she started reading about snarks to him - by heart, by the way!"
    me "Scared?"
    sl "Yes. {w}He started speculating about what species these very snarks might belong to."
    th "He'd better reread that same book."
    sl "Those animals we ran away from look a lot like them."
    me "How do you know what a fictional animal is supposed to look like?"
    show sl angry pioneer with dspr
    sl "Well!"
    me "Okay, I'm sorry. {w}How long was I out?"
    sl "Half an hour, maybe. {w}They were scrabbling under the door for a while, and then they left."
    me "Okay. What about the flashlights?"
    "Slavya, apparently deciding to try her role as Lena today, blushed again."
    show sl shy pioneer with dspr
    sl "You see, this is what happened here."
    "She mumbled, hiding her hands behind her back."
    sl "Well, there's, uh... uh..."
    me "Huh?"
    show sl smile pioneer with dspr
    sl "I broke the flashlight, kind of. While I was falling on you."
    me "Did you get sick or something?"
    me "Or did I give you negative luck?"
    scene
    $ renpy.show("bg int_mine_room2_7dl", what = Notch("bg int_mine_room2_7dl"))
    with dissolve
    me "Well, in that case, we have a flashlight and one baton. {w} Do you mind if I keep it?"
    "She shook her head."
    me "Then..."
    "She said the critters got away, but just in case..."
    "I listened."
    "It was quiet outside."
    menu:
        "We have to break through to the outside" if (alt_sp >= 3):
            $ lp_sl += 1
            $ alt_sp += 2
            sl "Are you sure? {w}We barely escaped them after all."
            me "Yeah. Follow me, keep up."
        "Let's try to sneak to the surface":
            $ lp_sl += 1
            $ alt_sp += 1
            sl "But..."
            me "There's nothing to do anyway, we won't be here long."
            "And something to eat wouldn't hurt at all."
            "The sandwiches we took with us had given up on life."
            "With a sigh, she nodded."
        "What are we going to do?" if not herc:
            $ lp_sl += 1
            $ alt_sp -= 1
            sl "I guess we'll have to distract those beasts somehow."
            "I weighed the flashlight in my hand."
            me "Or drive them away."
            "She nodded."
        "Get ready to run on command" if herc:
            $ lp_sl += 2
            $ alt_sp += 2
            sl "What?"
            sl "What if they're still there?"
            me "Don't be afraid, Slavya. They're not there."
            me "But you don't have to wait for them to come, either."
            me "Just follow me, keep up."
            "Slavya nodded."
            "I opened the door and shined the flashlight into the darkness of the tunnel."
            th "Alone these things shouldn't be dangerous."
            th "But if they gather in a pack at the door..."
            dreamgirl "Don't say that out loud."
            th "I know without you."
    scene bg int_mine_halt with dissolve
    stop ambience
    if herc:
        "Let's go!"
    else:
        me "It looks like..."
    play sound sfx_mystery_movement
    play music music_list["scarytale"] fadein 3
    "We took off and ran as if all the devils of the underworld were chasing us."
    "Not so far from the truth."
    "The tunnels had better be avoided, or we might be pinched again."
    scene
    $ renpy.show("bg int_mine_halt", at_list = [sdl_transform11], what = Notch("bg int_mine_halt"))
    "So I tried to pick a route where I could back up into a corner if anything happened."
    scene
    $ renpy.show("bg int_mine", at_list = [sdl_transform11], what = Notch("bg int_mine"))
    "Although what was there to 'pick' - I had to navigate by circumstances and rely on my gut."
    scene
    $ renpy.show("bg int_mine_crossroad", at_list = [sdl_transform11], what = Notch("bg int_mine_crossroad"))
    "I didn't know what those things were, and I didn't want to know."
    "Until now, I didn't know such beasts existed at all."
    "But they vaguely resembled rats."
    "And I was well aware of what a pack of hungry rats could do, working together."
    scene
    $ renpy.show("bg int_mine", at_list = [sdl_transform11], what = Notch("bg int_mine"))
    "That's why - all the way, march, march!"
    "It was easy to get to the center adit, because we had to move from the hill, and then the adrenaline drove us."
    sl "Wrong way!"
    "Slavya preempted my attempt to turn."
    sl "Next turn!"
    me "Thank you!"
    scene
    $ renpy.show("bg int_mine_halt_left_7dl", at_list = [zenterright], what = Notch("bg int_mine_halt_left_7dl"))
    with dissolve
    "I'd rather thank you now than..."
    "Nothing else was heard behind me, except Slavya's quiet footsteps."
    "Have the dreaded snark monsters really gone somewhere?"
    th "But where?"
    "Judging from the approximate plan, there were only three exits from the mines, of which one was a failure from the upper tier."
    scene bg int_mine_water_7dl at zentercenter
    with dissolve
    "And the other one is flooded."
    th "No time to think, go!"
    me "Wrong turn, back!"
    scene bg int_mine at zexitcenter
    "Honestly, I was very surprised that we still managed to keep our mobility while moving inexplicably on some uneven ground, without hurting a leg or even falling over."
    "If I tried something like that under any other conditions, I'd end up with at least a big bump on my forehead."
    "If not worse."
    "The power went out in my apartment once and I tried to navigate with my eyes closed."
    "I'll skip the details, except to say that the experiment failed."
    "I would, of course, have tried to choose the path more evenly, but in the darkness, dispersed by a single flashlight, it did not work at all."
    "So, elbows like pistons, lungs like bellows - choo-choo, go at full speed!"
    "I automatically rounded a puddle of water that looked very deep and, just as automatically moving, took a left at the first turn."
    "Slavya wanted to say something, but changed her mind - she continued to sniff behind my back."
    stop music
    play ambience ambience_catacombs_stones
    play music music_7dl["sammy"] fadein 3
    scene bg int_mine_heart_7dl at zentercenter with dissolve
    "We stalled, running headlong into some kind of semi-circular room."
    "It looked more like a dragon's mouth ajar than anything else."
    "And the view from the inside, as if we were standing on a huge stone tongue."
    "But the giant molars were generously spattered with dried blood, and in some places you could make out the scraps of a shirt."
    "A little farther away, the blank stone was changing into some outlandish druses, translucent, frosted, playing with light."
    "A wild and inappropriate combination of blood and beautiful crystals whose composition seemed to completely deny protein metabolism."
    "The crystals glowed with a faint green-white fluorescent light, and I extinguished the flashlight."
    scene
    $ renpy.show("bg int_mine_heart_7dl", what = Noir("bg int_mine_heart_7dl", brightness = 0.6, tint_r = 0.2126, tint_g = 0.9152, tint_b = 0.7722, saturation = -0.2))
    with dissolve
    show sl normal pioneer with dspr
    sl "Let's take a closer look."
    "Slavya circled me and hurried to the «maw»."
    me "Slavya?"
    show sl normal pioneer far with dissolve
    "She didn't pay any attention to me, staring at the curious picture with all her eyes."
    sl "Glowing."
    me "Mm-hmm."
    "I shivered, trying not to think about the number of X-rays per hour."
    sl "There's something beautiful out there."
    "In an alien, otherworldly voice she muttered without turning around."
    show sl normal pioneer far:
        linear 2.0 xalign .5
    sl "Let's see?"
    "And took another step."
    "She didn't seem to perceive me at all."
    "I followed her gaze and shuddered."
    show myst_mh behind sl with dissolve2
    "Between the «fangs» appeared familiar swirling grayness, the fog."
    "It didn't seem threatening or hostile and was more of a curiosity."
    if alt_day4_sl_cl_tut_iz:
        "Somehow with a large dash of positivity."
        "I smiled and walked next to Slavya."
        show dreamgirl_overlay with flash
        dreamgirl "Hey, hey! No sleeping!"
    stop music
    th "God damn it."
    $ renpy.show("bg int_mine_heart_7dl", at_list = [sdl_transform17], what = Noir("bg int_mine_heart_7dl", brightness = 0.6, tint_r = 0.2126, tint_g = 0.9152, tint_b = 0.7722, saturation = -0.2))
    pause(.2)
    $ renpy.show("bg int_mine_heart_7dl", at_list = [sdl_transform18], what = Noir("bg int_mine_heart_7dl", brightness = 0.6, tint_r = 0.2126, tint_g = 0.9152, tint_b = 0.7722, saturation = -0.2))
    with vpunch
    play music music_7dl["dead_silence"] fadein 3
    show sl normal pioneer
    with dissolve
    me "Get back!"
    "I barked, and in one leap I got next to the girl and tried to pull her back."
    th "How many suggestors are going to be here?"
    "The mist stirred, recoiling, confirming my assumption that it was something alive."
    me "Let's go!"
    show myst_mh
    "Slavya staggered sluggishly and, without looking at me, took another step forward."
    "Tried again."
    "Surprised to find something in her way, she twitched her shoulder in annoyance."
    if alt_day4_sl_cl_tut_iz and (alt_sp < 3):
        "I followed her gaze and wondered."
        th "Why am I holding her at all?"
        th "Isn't it right to go there? {w}It's warm and cozy and no one hates anyone."
        "I let go of my hands, letting Slavya take a step."
        show dreamgirl_overlay with flash
        dreamgirl "How long am I going to help you out?! {w}Where's your willpower?"
        th "What?.."
        "I was sluggishly surprised to find that I happen to have someone talking in my head."
        dreamgirl "Resist the leads, asshole!"
        "I didn't understand anything."
        dreamgirl "Argh... I hate having to do this."
        "I lost control of my body, and the body itself intercepted Slavya's torso, dragging me along, stepping backwards."
    else:
        show myst_mh with Shake((0, 1, 0, 1), 0.3, dist=5)
        "And the creepy thing is that I, too, completely shared her desire to stride and stride there, then run the curly wisps between my fingers, stroke her like an old, faithful friend."
        show dreamgirl_overlay with dspr
        dreamgirl "What?!"
        dreamgirl "Semchik, are you crazy?! Get up and get out of here."
        with vpunch
        "It sounded like a blow to the skull from inside, and I shuddered and woke up."
        "I wrapped my arms around Slavya's stomach, properly."
        "Tried to make sure I didn't hurt her."
        "And pulled."
        "Back."
    scene
    $ renpy.show("bg int_mine_heart_7dl", at_list = [sdl_transform19], what = Noir("bg int_mine_heart_7dl", brightness = 0.6, tint_r = 0.2126, tint_g = 0.9152, tint_b = 0.7722, saturation = -0.2))
    with dissolve
    "One more step."
    scene
    $ renpy.show("bg int_mine_heart_7dl", at_list = [sdl_transform12], what = Desat1("bg int_mine_heart_7dl"))
    with vpunch
    "She fought back sluggishly, apparently not understanding the reasons for the delay, and I pulled and pulled her along."
    "Swearing, angry, and genuinely perplexed as to what my otherness was, if I could resist what was going on."
    if alt_day4_sl_cl_tut_iz and (alt_sp < 3):
        "Or rather, not really me, but my inner Tyler."
        "Where did he come from anyway?"
        dreamgirl "Shut up, you bum. You could have controlled your own carcass instead of making the unhappy inner voice agonize with the controls."
    else:
        th "It's probably a matter of insensitivity."
        "Rush."
        th "Or maybe it's that I hit my head properly, and now my balls and rollers work a little differently than a normal person."
        dreamgirl "It's a bit Asimovian, isn't it?"
    th "Uh-huh."
    "I exhaled, finally reaching the far more familiar dark expanse of stone and earth."
    "To the border where the white druises were replaced by far more commonplace granite."
    "Three steps."
    "I only realized something wrong was going on when I failed to take one."
    "I looked down - and swore."
    "We were standing on some surface that was only hard on the surface."
    "It turned out to be something like plasticine or melted cheese, and was yielding under our weight at a frightening rate."
    "I was already down to my ankles as the heaviest, plus my attempts to take the girl's full weight only made it worse."
    show sl normal pioneer with dspr
    sl "Why do you want to take me away from here?"
    "Asked Slavya."
    show sl smile pioneer with dspr
    sl "I don't feel hostility, everything here only wants to do me good."
    "She half-closed her eyes and reached forward."
    if alt_day4_sl_cl_tut_iz and (alt_sp < 3):
        "I wasn't in control this time, so I couldn't keep track of where she was reaching."
        "I had a much more substantial problem."
        dreamgirl "What the hell is that? We were walking on solid rock that way, I could have sworn."
        dreamgirl "Come on, come to your senses, and bring your mamsel."
        "I finally let go of the feeling of being an outsider, with a terrible headache and fatigue, like I'd just unloaded an entire wagonload of sacks of sugar alone."
    else:
        "Aw hell naw!"
    play sound sfx_face_slap
    with vpunch
    "I turned Slavya toward me and gave her a gentle slap, bringing her to her senses."
    me "Wake up! If all you feel is good, why would it hold you down by force?"
    sl "But no one is holding me down."
    "The chuckle sounded inappropriate in such a situation."
    sl "Except you."
    me "Then what about this one?"
    "I nodded at the trap under our feet."
    stop music fadeout 3
    sl "What is this?"
    me "A pull-rule thing, damn. {w}How would I know?!"
    show sl surprise pioneer with dspr
    sl "Don't swear!"
    me "A very appropriate remark!"
    scene bg int_mine_heart_7dl with diam
    play music music_list["you_lost_me"] fadein 3
    show sl scared pioneer at cleft
    with Shake((1, 0, 2, 0), 0.3, dist=10)
    "Convinced that I was right, the girl shrieked and tried to free herself - with understandable results."
    me "No use."
    me "While you were out there fondling that shit, you got in deep."
    "I'm not a big proponent of gloating and 'I told you so!' phrases, but I just couldn't help myself right now."
    scene bg int_mine_water_7dl with dissolve
    "The fog, which we hadn't been paying attention to, picked up and became perceptibly thicker."
    "But the slab beneath us whirled suddenly and lost its density - so much so that I fell right down to my knee."
    "Slavya, who weighed less, also went down, but not as critically."
    show dreamgirl_overlay with dspr
    dreamgirl "Do you need a rescue plan?"
    th "Come on!"
    dreamgirl "Here you go!"
    "Immediately clear and sane chains of action lined up in my head."
    "Perfectly appropriate to the solution of the problem."
    dreamgirl "Don't thank me."
    hide dreamgirl_overlay with dspr
    me "Okay, let's pace."
    "Fear made my thoughts bright and ringing - I somehow knew very clearly that if the gray scum caught up with us, nothing good would come of it."
    "And so I acted on adrenaline - clearly, quickly, and with shaking hands."
    with fade
    "I searched my pockets and tossed the first item I found there in front of me."
    "Not enough - there was a palpable smack where the key fell into the slurry."
    "Next key."
    play sound sfx_keys_rattle
    "The thump of the metal against the rock was quite ringing."
    me "Bingo!"
    me "Slavya, it's going to take some teamwork now, are you okay?"
    "The girl was shaking a little with nerves and fear, but she nodded obediently."
    me "Then look."
    "I immediately leaned over to that side and, spreading my arms out, lay down on the viscous substance with some trepidation."
    me "Forward on me march."
    "If she's not prompt enough..."
    "Slavya nodded understandingly."
    "Under her weight, I immediately went halfway down my body - the panic and desire to frantically grab for at least something was only suppressed with great difficulty."
    "But the girl was already on solid ground."
    scene bg int_mine_heart_7dl with flash
    stop music fadeout 3
    "And again she rescued me - grabbed me by the arm and pulled me behind her."
    "This is becoming an unkind tradition - she pulls me behind her, on herself."
    "The jelly around my body tried to grip like a plaster - and like a plaster, the same plaster, grabbed some of the hair on the back of my neck and legs."
    "It wasn't pleasant."
    "But compared to what awaited us..."
    "I straightened heavily at the very edge of the abnormal rock and froze-right in front of my face, literally a few millimeters away, a gray void was swirling."
    show myst_mh
    with vpunch
    "For a split second, it suddenly seemed like I was standing on the very edge of an abyss."
    play sound sfx_wind_gust
    "Compared to this, even stray hikes along the curb of the sixteenth-floor roof seemed like child's play."
    "This height didn't just beckon - it tangibly pulled me in."
    if alt_day4_sl_cl_tut_iz and (alt_sp < 3):
        "And I yielded to the call, took a step into the abyss."
    else:
        "I flailed my arms, my whole body and every nerve almost physically feeling myself falling, falling!"
    show myst_mh with hpunch
    "I was sharply, violently jerked backwards at waist level."
    "Slavya."
    "My Valkyrie, taking her time to escort the warrior to Valhalla."
    "I, as I was in her arms, leaned against the wall, sideways, trying to even out my pulse and breathing a little."
    "Gratitude would be too weak a word, so many times she saved me."
    "But it's easier to save a man sometimes than to tell him you care."
    "Here I am..."
    hide myst_mh
    play music music_list["door_to_nightmare"] fadein 3
    show sl sad pioneer with dspr
    sl "You don't know what this is?"
    me "I don't know."
    me "But I can tell you that it's some kind of crap."
    me "And you almost got into it!"
    show sl shy pioneer with dspr
    sl "I'm sorry."
    "Confused, she babbled."
    "She was quiet, looking at me."
    "And began to tell."
    scene bg int_mine
    with fade
    "Nothing surprising in general, as long as this level of manipulation was involved."
    "I didn't know what the abomination was, and I didn't want to know, but its abilities..."
    if not alt_day4_sl_cl_tut_iz:
        "It reminded me somehow of that very buzzer at the club."
    "If you believe the girl's story, between the «dragon's fangs» she discerned an exit to the outside, and leading into the forest, familiar from her childhood."
    "There she shook, and it took me a few minutes to convince her to calm down."
    me "Let's get out of here."
    "The inhabitants of the tunnels still hadn't shown themselves, but that meant exactly nothing."
    "I kept my guard up."
    "And to brighten the path a little, I made the girl continue her story."
    scene bg int_mine:
        linear .1 xalign .5 zoom 1.02
    "According to the unfinished map, we're on a relatively straight road that will get us out of here."
    "I've had enough of dungeons. I'm sick of it."
    "You're not luring me back in."
    scene bg int_mine:
        xalign .4 zoom 1.02
        linear .3 xalign .6 zoom 1.1
    "Slavya talked and talked - about her grandmother, the witch doctor, and that she, too, had been offered a lesson in this sort of thing."
    "About how if you walked strictly eastward through the woods she saw, you could come out to the ravine where she used to run away all the time as a little girl."
    scene bg int_mine:
        xalign .6 zoom 1.1
        linear .2 xalign .6 zoom 1.25
    "Footsteps, breathing, slapping water."
    "I didn't delude myself about the sharpness of my own hearing, but I didn't smell anyone around us."
    "And that meant only one thing."
    "After interrupting the girl, I grabbed her and pulled her behind me."
    me "Ru..."
    "Apparently reading something in my eyes, Slavya turned sharply in one motion and smashed the inoperative flashlight on the head of the sneaking snark."
    scene black with dissolve
    play sound sfx_table_hit
    "He shrieked and, clutching at his injured spot, howled and scampered off into the darkness."
    scene bg int_mine
    show sl smile pioneer
    with dissolve
    th "And that's the creature we were running from?"
    me "I didn't suspect such bloodlust in you!"
    "I marveled."
    show sl normal pioneer with dspr
    sl "Sorry. Nerves or something."
    "Nerves? So, if anything... If nerves..."
    "That's what I'm gonna get too, isn't it? Flashlight on my head?"
    "Nightmare."
    "So no heavy objects at hand!"
    "The second unique ability, after the ability to disengage from the life of society, is the ability to schizoramble, even on the run."
    scene bg int_mine_door with dissolve
    "While I was sluggishly horrified by the evil Slavya, we galloped through the entire northern mining area."
    if alt_day4_sl_cl_lf_solo == 2:
        "Another minute, and the spot of light swept across the painted boards of the heavy looking door to the mine."
    else:
        "Another minute, and the stain of light was seen on the painted boards of the familiar door."
    "I paid attention to the surroundings this time, so it was accurate here, we did end up at the switchboard."
    me "Hold the flashlight."
    "I handed Slavya the light source and, grunting, grabbed the handle."
    "It's-so-heavy!"
    me "On the count of three! One!"
    play sound sfx_open_metal_hatch
    "And, with an exhale, dragged it to the half-open position."
    "Slavya immediately slipped past me."
    if (alt_day4_sl_cl_lf_solo in (0, 3)):
        th "And we walked around here so carelessly yesterday?!"
    play sound sfx_metal_door_large_close_basement
    scene bg int_mine_room with dissolve
    "Shaking my head, I followed the girl in and slammed the door behind me."
    th "I should have closed it."
    "A logical decision."
    "And I was the one that Slavya entrusted her keys to."
    "And the keys..."
    "The pocket was empty."
    "All I could think of were foul epithets, when I looked up and stopped myself in mid-sentence."
    "Slavya was standing beside me, her eyes twinkling wetly."
    show sl smile pioneer with dspr
    sl "You know..."
    "She murmured."
    stop music fadeout 3
    show sl shy pioneer with dspr
    sl "You turn out to be a lot better than I thought."
    play music music_7dl["tears_of"] fadein 3
    th "What is she so happy about?"
    "But that's probably not so bad either, is it?"
    sl "Braver."
    "She took a step forward."
    sl "Determined."
    show sl smile2 pioneer close with dissolve
    sl "We're dating, and it's going to happen anyway."
    "The girl bit her lip and, catching my chin with two fingers, reached for me."
    "And inside me, somewhere, something sweetly ached."
    "As if I really was seventeen, when a kiss means so much, when the only thing meaning more is a timid 'I consent.'"
    "Something strange has come over the girl."
    "But after what we've been through here in the mines, some of the impulsiveness is understandable."
    "So..."
    scene cg d5_sl_kissing_7dl with dissolve
    "My lips touched soft lips."
    "She covered her eyes and {i}felt{/i} me, as if breathing my presence."
    "The sad spectacle - the beautiful bowels of a warped psyche that won't allow me to close my eyes during a kiss."
    "Catching someone else's warmth with tear drops and touching someone else's smile, catching me by the shoulders and not letting me pull away."
    sl "You're... Too aggressive."
    "She exhaled, swaying."
    me "And you're not happy about something again."
    sl "I don't know... I don't know how."
    me "Let's learn?"
    scene bg int_mine_room
    show sl shy pioneer close
    with dissolve
    "With difficulty pulling away from me, Slavya nodded, trying to catch her breath."
    if alt_day_binder != 1:
        "And I, without hiding my delight, exclaimed:"
        me "Shit! If I'd known it was so great, I would have grabbed you right by the bus and kissed you!"
    "Laughter scattered like pearly balls around the small room."
    show sl laugh pioneer with dspr
    sl "You can't be in too much of a hurry!"
    "You can't rush. You can't slow down. Where to learn to keep perfect timings."
    me "And what... {w}This."
    "Nod."
    show sl shy pioneer with dspr
    sl "Yes. I certainly expected things to be a little more romantic, that I, too, would one day fulfill old Egle's prophecy."
    me "What's not romantic about it?"
    "Her claims are kind of strange..."
    me "We ran away from something bad, now we're torturing each other's lips in the dark."
    th "I don't think you need to look for any extra reasons or conditions for a kiss. It'll be memorable anyway."
    th "Especially the first one."
    me "Considering I've lost my keys, there's nothing left for us to do here, let's get out."
    show sl dontlike pioneer with dspr
    sl "You lost the keys?!"
    "I felt myself blushing."
    me "You know, I liked it better when you kissed me than when you yelled at me!"
    me "Yes, I did."
    me "Apparently, the moment you and I got bogged down."
    show sl serious pioneer with dspr
    "Slavya sighed."
    "And while she was there thinking, I got close to her, and..."
    with fade2
    "Anyway, there's a little break between the first and second."
    "She gave me a slap on the wrist and told me to mind my own business."
    "But didn't wean me off the lips."
    show sl shy pioneer with dspr
    sl "Too much and too greedy... It's just skin to skin, why do my knees get so weak?"
    "She looked at me demandingly."
    th "Well, how am I supposed to know why you have a decline of strength..."
    me "You can hold on to me all you want."
    "I winked at her."
    me "But then you'll have to think a little harder about fending off my harassment."
    "Slavya smiled, but immediately became sad."
    sl "Olga's going to kill me."
    sl "This is the second time!"
    me "And I'll save you!"
    show sl smile pioneer far with dspr
    sl "Two deaths can't be arranged. Let's go!"
    "We opened the door to the stairs."
    scene bg int_hence_day_7dl with dissolve
    "Slavya got in first again."
    "This time no one particularly pissed me off, embarrassed me, or prevented me from doing what I wanted to do."
    sl "Semyon, if you keep staring like that, you're going to see a hole in me."
    "There was a laugh from above."
    me "But it was an accident!"
    sl "For the first two seconds - I believed you!"
    play sound sfx_fall_metal_door
    "The grate rattled, letting in the fresh, damp air into the concrete peninsula."
    sl "Get out, just be careful, the last two brackets are wet."
    "I nodded and a few minutes later I was upstairs."
    "It had already stopped raining."
    play sound sfx_open_metal_hatch
    play sound2 sfx_7dl["eat_horn"] fadein 1
    "We got there just in time - almost the moment the grating fell into place, a dinner horn was heard from the loudspeaker."
    stop music fadeout 3
    stop ambience fadeout 6
    stop sound2 fadeout 3
    return

label alt_day5_sl_cl_return:
    scene bg ext_square_day with dissolve
    play ambience ambience_camp_center_day fadein 5
    "After stepping back to the nearest bench, we stopped to sit and catch our breath."
    "Our lunch wouldn't get away from us."
    "The hungry pioneers were already running past us, and they had no idea what a hell of an abomination they had at their side-just an hour of leisurely walking."
    "Even if locked behind heavy doors."
    me "We've had quite an adventure."
    "I grumbled."
    "Slavya nodded in agreement."
    show sl smile pioneer at cleft
    sl "Do I understand correctly that the keys will stay there?"
    me "If you have any desire to climb down there again, then wander into the heart of the labyrinth."
    "Slavya nodded excitedly at each of my arguments. Her eyes lit up."
    "You bet she did."
    me "Then forget it!"
    me "I'm not going down there. And I won't let you go down."
    show sl sad pioneer at left with moveinleft
    show ba em1 uniform at right with dissolve
    ba "So what have you kids been up to?"
    "Sanich horned, appearing unnoticed from behind."
    "I could hardly keep from screaming in fright."
    me "Not much."
    "I muttered in an hoarse voice."
    "My shirt looked like nothing, my tie was covered in muddy water, my knees were stained and scratched."
    "At least Slavya looked clean and tidy. Compared to me, of course."
    ba "You went there again."
    "Noisily he sighed."
    "He pulled a pack from his pocket, then came to his senses and pushed it back in."
    ba "Come on, spill everything you saw there."
    show ba smile uniform with dissolve
    "The gym teacher was interested in our hike."
    "Came around the bench and sat next to us."
    show sl shy pioneer at left with dspr
    ba "Don't drift, pioneer, I'm not interested in the moment where you've been squeezing."
    ba "You tell me about the tunnels."
    "He hummed contentedly, comparing the redness of our ears."
    me "I don't know. I can't tell."
    sl "It felt like I was at home down there, in the woods near our village."
    sl "So much so that I believed it."
    show sl scared pioneer with dspr
    "Slavya shuddered."
    sl "How could that be?"
    "She whispered."
    ba "And you, pioneer?"
    "Sanich turned his gaze to me."
    show sl normal pioneer with dspr
    if alt_day4_sl_cl_tut_iz:
        me "There didn't seem to be much passion, but I almost went down there, too."
        me "It also felt like I was standing on the edge of the roof, that's all."
    else:
        me "I didn't think anything, I was pulling Slavya out of there - because there were some animals running around, and I really didn't want to meet them!"
        show dreamgirl_overlay with dspr
        dreamgirl "But then the abomination got a hard one in the back of its head."
        "Chuckled the inner voice."
        ba "So you didn't feel anything?"
        "I nodded."
    ba "That's it. Well, since you're here, it all worked out this time."
    "He rubbed his chin thoughtfully."
    me "This time?"
    "Sanich pretended I didn't ask anything."
    ba "Interesting, interesting. {w}So, do you pioneers want to be exempted from events, or do you want to play pioneer?"
    show sl angry pioneer with dspr
    sl "Boris Alexandrovich, this is not a game!"
    "The girl flared up."
    sl "We should all help each other!"
    ba "As you wish."
    "He rose heavily."
    ba "I'll go and see about the shower... It's the least I can do."
    me "Boris Alexandrovich!"
    ba "Well?"
    "He turned around."
    me "And who were the snarks that were in the tunnels?"
    ba "Didn't you see any muzzles? They're overgrown rodents, like moles."
    ba "The most harmless critters that can exist, oriented by sound as they are blind."
    "After saluting us, the gym teacher departed."
    hide ba with moveoutright
    show sl normal pioneer at center
    with moveinright
    "There was silence for a moment."
    show sl laugh pioneer with dspr
    "And then we looked at each other and laughed heartily."
    "The crazy tension finally let go of my body."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_sl_cl_dinner:
    play music music_list["my_daily_life"] fadein 5
    scene
    $ renpy.show("bg ext_dining_hall_near_day", what = Dawn("bg ext_dining_hall_near_day"))
    with dissolve
    play ambience ambience_camp_center_day fadein 3
    "Dr. Violetta was expected at three o'clock, so the first and second squads were in no hurry to disperse after lunch."
    "So we huddled around the porch, in groups, in couples, some acting alone."
    "I, understandably, was kept company by Slavya - she hadn't left my side since her successful wanderings through the bowels of the earth."
    "Half of those present giggled embarrassedly, anticipating something unseemly - and nurse's reputation spoke for it."
    "The other half just blushed, anticipating exactly the same thing."
    if (not alt_day4_sl_cl_un_rej) and (alt_day4_sl_cl_lf_solo in (0, 3)):
        "For example, Lena, who yesterday showed the world wonders of courage in speleological races, today hid in a book, and if she had her will, she would have climbed in it."
    "And I... Hell if I know."
    "My head was a jumble of thoughts and experiences, and all the slaps in the world couldn't get it all sorted out."
    scene bg ext_dining_hall_near_day with blind_l
    "And it feels weird, like a broken Nokia 3310, carefully wrapped in a party wrapper for my birthday."
    "But there's no one to dump the dusty toys in my lap and ask me to sort them - not even my (kind of?) girlfriend."
    "Not that she doesn't care, but without knowing the whole story she's unlikely to be able to make a proper judgment."
    "And I'm not ready to tell it all yet - from the get-go."
    "It's not a matter of trust, I just haven't got the guts yet."
    "Olga Dmitrievna beckoned Slavya with her finger, and the girl hesitated."
    "On the one hand, there was no way she wanted to let me go - as if I could protect her from the snarks, if they suddenly got to the surface."
    "On the other hand, flipping off the squad leader outright was strange, too."
    "Determined, she got up and pulled me behind her."
    show sl normal pioneer with dspr
    sl "Let's go together, okay?"
    "Quietly she asked."
    show sl normal pioneer with dspr
    sl "Don't let go of my hand, please."
    "Bang. Bang."
    "The mess under my temples, the bed thrown to the floor in the night, the lightning striking unexpectedly close."
    th "What will Olga say?"
    "I got scared."
    th "She trusts Slavya enough to let half the squad go under her command."
    th "But this is hardly the sort of thing she expected."
    "Still undecided, I stopped in front of the counselor, held back by Slavya."
    scene bg ext_dining_hall_near_day at zenterright
    show sl shy pioneer at left
    show mt normal pioneer at right
    with dissolve
    mt "Semyon, I'd like to talk to Slavya alone."
    "In an intransigent voice Olga asked."
    "Her answer was a pleading look in my direction, and I remained standing still."
    show sl normal pioneer with dspr
    sl "I have no secrets from Semyon."
    "Frowned the girl."
    me "Yes?"
    "The squad leader laughed, looking at my chagrined face."
    show mt grin pioneer with dspr
    mt "What, is the Monomakh's hat heavy?"
    "She winked."
    mt "But okay."
    show mt normal pioneer with dspr
    mt "It's about the bonfire today."
    me "A bonfire today?"
    show sl laugh pioneer with dspr
    sl "Did you forget?"
    "I slapped myself on the forehead:"
    me "The event!"
    mt "Exactly!"
    "She turned to Slavya:"
    show mt smile pioneer
    show sl normal pioneer
    with dspr
    mt "I see you've already found a willing helper. So go to the glade after the lecture and see if everything is all right there."
    me "Olga Dmitrievna, why are you so calm about the fact that we... Well..."
    th "And how does she even know?! {w}I didn't tell anyone anything!!!"
    "I looked over at Slavya, and she responded with a serene smile."
    "The leader understood my hesitation perfectly:"
    show mt smile pioneer with dspr
    mt "Because I trust Slavya, don't you see? {w}I trust her common sense."
    "The welcoming smile took on a frightening hue for a second."
    mt "Besides, in case one overly clever pioneer decides to let himself go a little overboard..."
    show mt angry pioneer with dspr
    "She leaned toward me and whispered something in my ear."
    "I think I turned pale."
    show mt grin pioneer with dspr
    mt "Yeah. With rusty pliers."
    show mt normal pioneer with dspr
    mt "Now go... My children."
    hide mt with dissolve
    "Viola was still missing, so Olga went out to do some recon."
    "Meanwhile, the noosphere was again enriched with a good portion of rumors."
    "Some thought the nurse was about to tell a few platitudes, more about valeology than sexual etiquette."
    "Those who disagreed with them, on the contrary, thought the most interesting things were about to be yanked back."
    show sl serious pioneer with dspr
    sl "Oh, well, yes, of course."
    "Slavya sat on the steps, pensively picking the concrete slab with the toe of her sandal."
    show sl angry pioneer with dspr
    sl "Violetta Cernovna is a woman without complexes, but we're in camp, after all, so I wouldn't expect much candor."
    "I nodded in agreement with her."
    hide sl with dissolve
    "And finally, the third category of rumors is - inevitable craving for mysticism in the minds of the crowd."
    "Someone started a rumor that Violetta Cernovna had been given permission to use medical hypnosis, and she would now code all the boys for sexual desire, so that they wouldn't want to, couldn't, and either way."
    "Upon hearing this version of the interpretation of events, the male half of the waiting crowd got a little worried and tried to sneak away."
    "But the approaches to the canteen were blocked by the counselors with Sanich at the head."
    show ba smile uniform at right with dissolve
    ba "Hello, pioneers!"
    "He boomed."
    ba "What's the rush?"
    voice "We don't want to get hypnotized!"
    "A voice from the crowd stumbled on the third syllable."
    ba "You don't want to, we don't force you."
    "Catching my eye, the fat man winked and tossed the familiar bundle in his palm."
    ba "Come back later for your loss."
    "Looks like Sanich heard us talking about the keys and went to return them himself. Was he worried we'd go back there ourselves?"
    "Anyway, Slavya managed to avoid the fate of facing the angry counselor a second time."
    show sl normal pioneer close at left with dspr
    sl "That's the one who didn't run from the snarks."
    sl "And you and I are like two cowards."
    me "Who knew?"
    "I mumbled."
    me "He's got the most peculiar predatory face - if he don't eat it, he'll bite it."
    show sl serious pioneer close with dspr
    sl "Just don't tell him. He won't understand."
    me "I mean the snark!"
    show sl normal pioneer close with dspr
    sl "A."
    "At this time Olga Dmitrievna pushed between the counselors."
    scene bg ext_dining_hall_near_day at zenterleft
    show mt normal pioneer at cright
    with dissolve
    mt "Kids!"
    "She called."
    scene bg ext_dining_hall_near_day at enterright
    show mt normal pioneer at right
    show cs normal at cleft
    with dissolve
    "The guest star was modestly kept in the keel, glaring around."
    "Catching my gaze, she shook her chin, and turning her eyes to our hands, which we never unhooked, aristocratically arched an eyebrow."
    "But she didn't say anything - for which she deserved a grand mercy and half a liter of «Baileys»."
    "Viola seems to have been asleep ever since I let her go home by six in the morning."
    "True, then I ran off myself, but I honestly entrusted the medical diocese to our mad scientist."
    "She looked young and blooming - that's what eleven hours' sleep does to a man!"
    "Although I was inclined to the theory that our lecturer was kept backstage to sustain the MHAT pause."
    with fade
    "The male half of the waiting crowd, unaccustomedly quiet, turned on the gentlemen in droves, letting the ladies go first."
    "But breathe or not, you can't breathe enough before you die - the tightening ranks of the counselors pushed the rest of us into the hall."
    "We had to accept the inevitable."
    "We were the last to go in, the door closed behind us, and the lock clicked, so we wouldn't escape, or else."
    play sound sfx_medpunkt_door_open
    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_medium_crowd_indoors_1 fadein 3
    "In the meantime, the dining room had already been rearranged, the place where the staff usually ate had been cleared out, and a substantial table had been placed in the very center of the pulpit and a stiff movie screen blocked the windows."
    "Under the ceiling, the heated slide projector crackled softly, and all the necessary slides had already been crammed into it."
    "In short, they prepared for the lecture with heart and soul."
    "In addition, posters, yellowed by time, were hung on the columns, urging the boys to treat the girls more leniently and not to do them any harm - a sort of high-society etiquette."
    "Soviet-style."
    "Viola squinted at them perplexedly, but said nothing."
    "But Olga Dmitrievna was clearly full of enthusiasm - apparently the posters were hanged on her initiative."
    show mt normal pioneer with dspr
    mt "So, girls and boys, of course, it's a little late to do this two days before the end of the shift, but today we were instructed to give you a lecture on the relationship between the sexes!"
    show us smile sport at right with dspr
    us "Will there be slides?"
    "Shouted Ulyana."
    show mt smile pioneer with dspr
    mt "There will!"
    show dv laugh pioneer2 at left with dspr
    dv "And the revealing ones?"
    "Alisa played along."
    "The counselor was a little confused, but she had seen more than that in her line of duty - she came to her senses instantly:"
    show mt normal pioneer with dspr
    mt "You'll see!"
    show dv normal pioneer2 with dspr
    dv "No, tell us!"
    "The redhead insisted."
    show dv laugh pioneer2 with dspr
    dv "In case we have the faint of heart here in the audience."
    show un scared pioneer far at fleft behind dv with dissolve
    "At these words, Dvachevskaya gave an expressive look in Lena's direction."
    show dv normal pioneer2 with dspr
    dv "Who are going to flow under the table in the middle of the lecture."
    hide dv
    hide un
    with moveoutleft
    hide us with moveoutright
    mt "Alisa, sit still and stay out of the way. {w}So, I present to you Dr. Collider Violetta Cernovna. {w}Welcome!"
    "Olga put her arm out to the side in a picturesque way."
    "Cautious claps were heard from several places, and Violetta Collider ascended the pulpit."
    show dreamgirl_overlay with dspr
    dreamgirl "She knows how to present herself for sure."
    "The inner voice marveled."
    play music music_7dl["viola"] fadein 3
    scene cg d5_cs with dissolve
    "Well, it's true - already a tall birch, Viola stood on a mile-long stiletto, visually rendering her long legs mind-boggling, her white robe flapping open with every step, revealing that the stiletto was accompanied by black stockings and a short turtleneck skirt that barely hid her garters."
    "The very ones who were afraid of hypnosis swallowed loudly and perked up, devouring the charming lecturer with their eyes."
    "I was generally close to copying their behavior, too, but the hard elbow in my ribs proved an irresistible obstacle."
    scene bg int_dining_hall_people_day
    show mt normal pioneer at left
    with dissolve
    mt "I would like to begin our lecture with…"
    "Olga began."
    show cs smile at right with dspr
    cs "Ah, they're already reading here."
    "Nurse smiled."
    cs "Well, I'll be going then."
    "The squad leader got embarassed and went silent."
    mt "Viola!"
    show cs normal with dspr
    cs "Wow...{w} What a quick read."
    "Sluggishly she was surprised."
    "But she didn't come back to the table."
    hide mt with dissolve
    show cs normal at center with moveinleft
    "She walked to the very edge of the pulpit, folded her arms behind her back so that her snow-white robe rattled across her chest, winked at someone in the crowd, nodded at us, and studied the audience with feeling and consideration."
    "She managed to open her multicolored eyes so wide that she could compete with Miku for the role of a Japanese cartoon heroine."
    show cs smile with dspr
    cs "The audience is... nightmarish."
    "She shook her head."
    cs "Why am I being slipped kids again? I'm always afraid I'll be prosecuted for seduction of minors!"
    "Not embarrassed by the audience, she asked Olga."
    "Olga sighed sadly."
    "Part of the audience relaxed, particularly those who were wary of the too frank form of presentation."
    "Those who talked about hypnosis closed their eyes - though what's there to close your eyes for when there's such cleavage?!"
    sl "Syomushka, don't get carried away."
    "I got elbowed in the ribs again."
    show cs normal with dspr
    cs "So. Let's try to enlighten you, shall we?"
    cs "Although, judging by the happy faces, I can be enlightened myself, and in a big way, on all subjects."
    cs "Look at the back rows."
    cs "You're sitting there wondering why that silly woman climbed up on stage and mumbled something."
    "Her deep, chesty voice echoed through the canteen, making the windows rattle lightly."
    show cs smile with dspr
    cs "I completely agree with you. {w}Instead of going to sle… ahem… Keeping an eye on the health of the pioneers, I'm crucifying myself in front of you."
    show cs shy with dspr
    cs "I even got scared, what if someone was constipated in an emergency?"
    "She looked around the room again and calmed down:"
    show cs smile with dspr
    cs "Oh, right. {w}There's also that boy with the funny glasses."
    show cs normal with dspr
    cs "Anyway... {w}What am I standing around for?"
    "She pulled a chair out from behind the table, twisted it on its front leg with one hand, and set it in front of her with the back facing forward."
    "The front rows exhaled at once and squinted to where the back of the chair should have ended."
    cs "Ah, yeah."
    "The nurse got up and put the chair just right, on the very edge of the pulpit."
    "And she sat down, completely copying Sharon Stone's famous pose from «Basic Instinct»."
    "The male portion of the audience has again lost the rest of their will."
    th "I hope she won't be shifting her legs?"
    show dreamgirl_overlay with dspr
    dreamgirl "Do you mind?"
    th "No, but Slavya is right here."
    "It's a very strange feeling to have someone laughing inside you."
    dreamgirl "So chase her away!"
    show cs smile with dspr
    cs "First, a little bit of theory."
    show us smile sport at left with dspr
    us "Will there be practice?"
    "Audience rumbled."
    "Olga Dmitrievna in the background pictured a facepalm and slid quietly down the column."
    show cs smile with dspr
    cs "Of course there will be.{w} Knowledge without practice is an empty weight."
    "The hall perked up, those who were blushing before successfully burned out for good, retarded laughter came from the redheads, but Miku straightened up, looking at the scene with enthusiasm."
    show cs shy with dspr
    cs "But, of course, in another place and under different circumstances."
    "The nurse hastened to dispel the illusions of the assembled crowd."
    us "Awwwww!"
    hide us with dspr
    show cs smile with dspr
    with fade
    cs "Before you run off at the end of the lecture to write an anonymous letter to the party, the union, or the sports lottery, let me inform you that I have a PhD in psychology and therefore I am entitled to educate children on the subject."
    cs "If you don't take my word for it, you can come over to the nurse's office and examine my paperwork, but don't forget to wash your hands before you do."
    cs "Although I think it's all pampering, and you yourself know far more than I do about the fact that when a boy and a girl meet..."
    "She cut herself off."
    stop music fadeout 3
    show cs shy with dspr
    cs "First things first."
    play music music_list["always_ready"] fadein 3
    cs "To be honest, I should check the average age of you, local bums, to see what topics I can talk to you about."
    show cs smile with dspr
    cs "But to hell with regulations, you were handed out all kinds of pamphlets about what to do when you like a girl, huh? {w}Although you all wiped yourselves with them at the first bus stop."
    cs "For some reason educators are embarrassed to talk about the fact that man is such a creature that wants love."
    show cs normal with dspr
    cs "And love in Soviet society is a whole problem. You have to go up to a girl you like and not embarrass yourself."
    cs "What if she doesn't like you? {w}What if she has someone else?{w} What if you stink?"
    cs "Although the latter is solved by a daily shower and washing clothes."
    cs "Next comes a bunch of crap about the complex approach, prevention and hygiene - the school will explain."
    cs "Let's keep it simple."
    "She crossed her fingers on her knee - and the front rows exhaled audibly again."
    show cs smile with dspr
    cs "What is love? An incredibly big problem, in a nutshell."
    cs "Of course, while you're in love, everything doesn't seem so daunting - you're happy and cheerful and generous. {w}And annoying to those around you."
    cs "But then what? Huh? Falling in love ends and you start wanting something more serious."
    cs "And where do you get «something more serious», if you are from different cities, you leave at the end of the shift and never see each other again?"
    cs "I've got two frumps sitting right here."
    "She gestured at us with a Phoenix Wright gesture."
    "It felt like I'd been hit on the head with something again."
    "It didn't seem to hurt Slavya at all - she stood up and waved to the crowd that was focused on us."
    show cs grin with dspr
    pause(.2)
    show cs smile with dspr
    cs "These frumps have found each other, a couple of the year, you know... Ahem."
    cs "They're already holding hands today, and the day after tomorrow they'll shed three liters of crocodile tears during their departure and their lives will be over."
    show cs normal with dspr
    cs "Sad, isn't it?"
    cs "So now they're going to do a lot of weird and illogical things, refuse to listen to the counselor, for example."
    show mt angry pioneer far at fleft with dissolve
    mt "Mm-hmm."
    "The squad leader gave us a threatening look."
    hide mt
    show cs smile
    with dspr
    cs "They might even try to run away to live in the woods for subsistence - youth is foolish, especially youth in love."
    show dv normal pioneer2 at left with dspr
    dv "How do you know what they will and won't do?"
    "Shouted an inexplicably gloomy Alisa from her seat."
    show cs normal with dspr
    cs "Kiddo-o-o."
    "Viola stretched out."
    show cs smile with dspr
    cs "Didn't they teach you in school that before you bark from the audience, you should first raise your hand and wait until the right is given to you?"
    show dv guilty pioneer2 with dspr
    cs "Your friend is still young, she has different demands. {w}Do you want to be like her?"
    "Alisa blushed and tried to disappear into thin air."
    hide dv
    cs "But okay. {w}The question is really on point."
    cs "How do I, a silly big aunt in years, know how each of you, so unique and unique, feels?"
    cs "The answer is simple: I really don't. {w} I was already born thirty years old."
    "Appreciating her joke, the audience laughed."
    show cs normal with dspr
    cs "Rest assured, in every adult's life there is some foolishness. {w}We are all human beings."
    "She squinted at Olga Dmitrievna holding her head."
    cs "And some people don't grow up after twenty."
    with fade2
    cs "So, back to our inseparable couple."
    cs "Your age is the age of formation of ideals, including the formation of tastes. {w}For some reason, for this pioneer girl that pioneer became the ideal, and vice versa."
    show cs shy with dspr
    cs "She wants her chosen one to like her, so she doesn't wear a baggy shirt anymore, but a strictly tailored one that fits."
    "I glanced at Slavya - now she was sitting a little red, too."
    show sl shy2 pioneer at right with dspr
    sl "Don't ask."
    "She whispered."
    hide sl with dissolve
    cs "Further, for some reason of their own, they have passed the attention-getting period - girls usually do this with makeup, earrings, and other things."
    show un shy pioneer at right with dspr
    "She pointed to flushed Lena."
    show mi normal pioneer at left with dspr
    mi "Oh, Lenochka, my lip gloss looks so good on you, and why did you take it without asking, you would have asked, I would have given, I'm not greedy!"
    show un shocked pioneer with dspr
    "In the absolute silence, Miku's voice sounded like an epitaph."
    "An empty space was instantly formed around the unhappy girl."
    dv "Tikhonova, are you stealing?"
    "Dvachevskaya's voice sounded."
    un "No! I…"
    "She hid her face in her hands."
    scene bg int_dining_hall_people_day
    show cs smile
    with dissolve
    cs "Clothing is also among «other things», for example, unwillingness to wear underwear or urges to mock the shirt."
    "This time it was Alisa's turn to get flustered."
    "She pulled her head fearfully into her shoulders and looked around to see if anyone was watching."
    cs "Finally, the girl begins to show interest in all sorts of «mysteries», which includes both fortune-telling and other nonsense like love literature. {w}I hope we don't have any copies of «Kamasutra» or «Story of O» in our library?"
    mz "No."
    "The Buzzer squeaked."
    mz "They're not on the permitted literature list."
    show cs normal with dspr
    cs "Okay."
    cs "So we're done with the most interesting and multifaceted part, describing the gentle and turbulent ocean going on in the pioneer girl's soul, and we move on to the boring part: the pioneer."
    play music music_list["farewell_to_the_past_edit"] fadein 3
    show cs smile with dspr
    cs "The life of males is always more boring, they are governed by two and a half desires - to eat, to sleep and..."
    us "Go to the bathroom!"
    "Shouted Ulyana."
    cs "Not all the time."
    "Serenely answered Viola, after waiting out a flurry of laughter."
    cs "I'll tell you this about the pioneer: he's in a hurry to become an adult now."
    show dreamgirl_overlay
    dreamgirl "And he wants it all the time!"
    th "Yup, of course."
    th "Where did all of you seers come from?"
    dreamgirl "Oh, yeah?"
    cs "And therefore will do everything like an adult, may try to smoke or try alcohol."
    th "I'm sorry, Violetta, but I've been quitting smoking for a year now, and I don't try alcohol, I drink it."
    "I prudently declined to argue out loud."
    th "For it is well known that the wise will listen to the squaw and do it his own way!"
    show cs shy with dspr
    cs "But most importantly, he begins to develop an erotic interest that he doesn't know what to do with."
    dreamgirl "Oh, really? {w}Can I tell you? I know!"
    th "She told you - practice at another time."
    dreamgirl "Killjoy, you're cutting off all the fun at the root."
    show cs smile with dspr
    cs "By the way, if you have any questions, be sure to come in and ask."
    "I nodded."
    show sl angry pioneer close at left with dissolve
    sl "Will you come in?"
    me "Of course I will!{w} Who do you take me for."
    "Slavya wondered."
    hide sl with dissolve
    show cs normal with dspr
    cs "And the stupidest thing we can do now is to forbid them to see and communicate. Do you know why?"
    cs "Because they'll call themselves martyrs and - yes, yes! - run off into the woods for subsistence food."
    show us smile sport at left with dspr
    us "Will there be slides?"
    show cs smile with dspr
    cs "No, there won't be."
    hide us with dissolve
    "After waiting out Ulyana's disappointed wail, Viola continued:"
    cs "We must be understanding and considerate of these two."
    cs "Since the two idiots volunteered to suffer and be sick, we shouldn't kick them unnecessarily."
    with fade2
    cs "Because if we put pressure on them, they'll decide to go into sublimation, miss some important moments in the development of the relationship, or even..."
    show dv normal pioneer2 at right with dspr
    dv "You finish it, finish it!"
    "Vindictively Alisa grumbled."
    show mt normal pioneer far at fright behind dv with dspr
    mt "There's nothing to finish."
    "Angrily replied Olga Dmitrievna."
    hide mt
    hide dv
    with dissolve
    show cs smile with dspr
    cs "In a nutshell, you'd better stay out of this filth. {w}At least until you finish school."
    cs "And if you get into this mess, at least try to do it in such a way that you won't be ashamed of yourself."
    cs "Me, Olga Dmitrievna, Boris Alexandrovich - we are always ready to help with advice."
    "She stood up."
    show cs normal with dspr
    cs "That's it, my tongue is slurring, end of lecture. {w}Questions?"
    "The audience responded with a steady hum."
    cs "Then I'm off..."
    "She yawned sweetly."
    cs "Mmmm… To work."
    play sound sfx_concert_applause fadein 1
    hide cs with blind_d
    "The first shock of the crumpled conclusion of the lecture passed, and the pioneers unanimously applauded Viola's waddling toward the exit."
    "And then they stretched for the exit."
    stop music fadeout 3
    stop ambience fadeout 6
    return

label alt_day5_sl_cl_campfire_prepare:
    scene bg int_dining_hall_day with blind_r
    play ambience ambience_dining_hall_empty fadein 3
    show sl normal pioneer with dspr
    sl "Well, why would she do that?"
    "Slavya complained."
    sl "Couldn't she just get some imaginary couple?"
    me "Why did you even tell them?"
    show sl shy pioneer with dspr
    sl "But I had to! {w}A counselor should know about these things!"
    "I just grabbed my head."
    th "I wonder if they know about the kiss, too?"
    th "And when we have something more serious - will she write out where, how, and how many times?"
    dreamgirl "We lived like we wanted to, only to call it a hardship and a difficult experience later."
    me "Whatever. {w}As for Viola..."
    me "A visual example is always more accessible. {w}Come on, we have a fire to make."
    show sl normal pioneer with dspr
    sl "Listen..."
    "She stopped at the door and pressed her back against the wall beside it. Her fingers on the jamb turned white."
    show sl scared pioneer with dspr
    sl "I can't go out like that! {w}What if they're out there?"
    me "Who?"
    sl "Those... Who heard everything."
    me "The pioneers?"
    sl "Yes!"
    "She looked really frightened."
    me "So what? {w}You're the one who told everyone everything."
    sl "That's not it!"
    sl "I can't. {w}Can't you look out and see if there's someone out there?"
    me "What a miracle."
    "I shook my head, but I followed the girl's request exactly."
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg ext_dining_hall_near_day
    with dissolve
    pause(1)
    play sound sfx_open_dooor_campus_1
    scene bg int_dining_hall_day
    show sl normal pioneer
    with dissolve
    "There was no one outside."
    show sl normal pioneer with dspr
    sl "Well?"
    me "No one."
    sl "Thank you!"
    "She kissed me on the cheek."
    show sl happy pioneer with dspr
    sl "I'll go get what I need, okay?"
    sl "Meet me at the gate in ten minutes."
    hide sl with dspr
    "And disappeared."
    "In the hall, however, Sanich and Olga Dmitrievna were setting up tables, bickering sullenly among themselves."
    show ba evil uniform at left
    with dissolve
    ba "Psychologist, huh? Children's, huh?"
    show mt normal pioneer at right
    with dissolve
    mt "Who knew! Last time she read everything all right, from the brochures and so on."
    ba "Olga, I'm sorry, but you're so sloppy."
    show mt angry pioneer with dspr
    mt "Come on!"
    "She was pouting, but she noticed me."
    show mt normal pioneer with dspr
    mt "What are you standing here for, listening to us, get out of here!"
    me "I'm coming, I'm coming. And you don't have to yell like that."
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg ext_dining_hall_away_day
    with dissolve
    play ambience ambience_camp_center_day fadein 3
    "I dashed out into the street."
    "What to do in a fire glade, I didn't know. What does one do in such a glade at all, except, in fact, make fires?"
    "The wild beasts didn't steal the bonfire, did they?"
    "Still smiling stupidly, I headed for the gate."
    play music music_list["get_to_know_me_better"] fadein 5
    scene bg ext_path_day with dissolve
    play ambience ambience_forest_day fadein 3
    "Now that the neighborhood was known to be inhabited not only by birds and insects, but also by some other obscure creatures that man had not managed to scare away, personally I was no longer as comfortable and peaceful here as I was at home."
    "Not that it's scary, but before, I wouldn't have hesitated to spend the night in the woods under the open sky."
    "That's the extent to which my surroundings have accommodated me."
    "Somehow got used to during my career as a pioneer to the fact that during the construction of SRCs and PLs, all existing fauna of varying degrees of danger were successfully dispersed by construction work."
    "But not now."
    "Unfortunately, Slavya didn't seem to be in the least moved by all this trouble - she was bouncing along, humming something in front of her."
    "And I, of course, followed her, lugging firewood, garbage bags, a broomstick, and a flask of water."
    "For I, not only as a gentleman, but as Slavya's young man, simply had to take all the trouble of carrying the cargo."
    "The words, understandably, are not mine."
    "But a most pleasant picture was opened to my attention - in my opinion, redeeming absolutely all deprivation."
    "Slavya could feel my gaze, for she looked around minute by minute, and I had to lift my gaze and smile with effort."
    "About the fifth time I got tired of it:"
    me "Look, can you walk straight? You're distracting!"
    show sl surprise pioneer with dspr
    sl "Distracting from what?"
    me "From admiring!"
    "I answered."
    me "Because you're all twisted up at this point!"
    show sl normal pioneer with dspr
    sl "Admiring..."
    "Slavya wondered:"
    sl "Me?"
    me "For the most part."
    show sl happy pioneer with dspr
    sl "Why didn't you say so, I would have..."
    show dreamgirl_overlay with dspr
    dreamgirl "Now, now, from this point on, tell me more!"
    "Something stirred inside. {w}Something that thinks I'm wasting too much time on nonsense."
    show sl normal pioneer with dspr
    sl "Went beside you."
    show dreamgirl_overlay with dspr
    dreamgirl "Screw you!"
    me "The path is too narrow."
    "Evasively I replied."
    "And only now did it dawn on me that I was simply being teased!"
    me "Slavya!"
    show sl laugh pioneer with dspr
    sl "Yes, Semushka? {w}What did you want?"
    me "How about you stop mocking my basic instincts?"
    show sl normal pioneer with dspr
    sl "Yea-ah?"
    "The girl pondered."
    me "I'm sure."
    sl "Then why don't you stop acting like a man with two thoughts in your head, of which both are obscene?"
    "The laughter flew off into the whitish heat sky, and I realized that this noncommittal flirtation allowed me to relax."
    "And brought back that sense of serenity that I had already grown homesick for this morning."
    me "Is this the kind of thing you can get enough of?"
    show sl smile pioneer with dspr
    sl "But I'm clothed!"
    show dreamgirl_overlay with dspr
    dreamgirl "The girl is talented, but she definitely lacks experience."
    dreamgirl "But she'll make up for it, and then you'll see who gets all the men on the beach - her in a cut-out bathing suit or a scientifically unknown mamzelle in a micro-bikini."
    me "Stop it."
    "I caught a glimpse of some dark spot on the right hand side of the road."
    me "What is it?"
    show sl surprise pioneer with dspr
    sl "...I don't know."
    me "Is this your first time here?"
    show sl angry pioneer with dspr
    sl "Grrr."
    me "Sorry, I couldn't resist."
    "I unloaded the firewood and the broom on the curb:"
    me "Shall we have a look?"
    "Slavya nodded."
    scene
    $ renpy.show("bg ext_path_day", what = Dawn("bg ext_path_day"))
    with dissolve
    "The spot turned out to be a huge molehole, the bottom of which could not be seen in daylight."
    me "Our dungeons?"
    show sl angry pioneer with dspr
    sl "That's them alright."
    "Wickedly said Slavya."
    show sl normal pioneer with dspr
    sl "From the looks of it, the beast here blew up the ceiling and went for fresh meat in the woods."
    "She looked upset."
    show sl serious pioneer with dspr
    sl "Well, yeah, that's right, they stepped away, took a shit, left it there, and left. Well, p-people..."
    me "What are you doing?"
    sl "I don't understand people. Why make a mess? If you live on earth, live in peace with it!"
    show sl angry pioneer with dspr
    sl "But noooooo - we want to get inside and pick at the bowels."
    sl "Would you like to have a squad of ants go under your skin, mining lymph and hair roots?"
    "She walked around and got mad."
    show sl serious pioneer with dspr
    sl "Man has a habit of screwing up the earth."
    sl "They burrow in who knows where, they dig up who knows what, and then they're surprised that all kinds of crap comes out of it."
    me "You mean the bomb shelter?"
    sl "Yeah, I'm talking about it. {w}They build bombs because they're afraid of bombs and hope to scare people around them with a bigger bomb. And to outlive those who aren't scared, they go underground."
    show sl angry pioneer at cleft with moveinleft
    sl "You have to be hygienic in your relationships, then you won't need bombs and you won't have to bury yourself in the ground."
    me "What are you talking about?"
    show sl normal pioneer with dspr
    sl "About the fact that we are not alone on the planet. {w}And the planet has many of us."
    sl "It's the only one."
    sl "We'll screw enough things up sooner or later, the planet will come up with some crap to wipe out man, disease or natural disaster."
    show dreamgirl_overlay
    dreamgirl "SARS, for example. Or anthrax."
    th "Didn't man invent that last one?"
    dreamgirl "I can't tell you."
    sl "We've been pissing her off for too long."
    "She thought for a while and told me:"
    sl "Take off your tie."
    "I obediently gave her the red petal."
    show sl normal pioneer2 at center with moveinright
    "She took hers off and strung a rope with improvised flags between the trees."
    sl "So no one would fall."
    "She explained."
    me "Do you think our rodents made it out into the woods?"
    "She shrugged."
    sl "I've never seen one, but they appear to be underground or night dwellers."
    sl "The daytime forest is hostile to them."
    show sl serious pioneer2 with dspr
    sl "They may well come out at night."
    me "And then the other pioneers will be running from them."
    "I grinned, picking up my belongings from the ground."
    scene bg ext_path2_day
    with fade
    "It's a strange relationship we have."
    "On the one hand, we're kind of together, as even Viola said."
    "On the other hand, I can't help but think that it's not the girl's romantic interest."
    "Or rather, it wasn't just that."
    "It was as if she knew something about me - something I hadn't realized myself - and was trying to figure out how to use it."
    "No, that's bad wording, though."
    "Let's say there was something else besides sympathy."
    "I had to remind myself how old she was. And how old I am from her point of view."
    "So she's quite legitimately afraid of what might happen if you give me too much leeway."
    show dreamgirl_overlay with dspr
    dreamgirl "But she wasn't afraid to grab your hands and poke her forehead into you."
    "The voice inside me remarked wryly."
    if alt_day3_dancing1 == 'sl_1':
        dreamgirl "Yes, and your dance on the penalty distance..."
        th "I liked it!"
        dreamgirl "So did I! {w}I have a suspicion that she liked it, too."
    dreamgirl "It would have been nice if we'd gotten here a week earlier."
    $renpy.notify('Ivana Kupala is a traditional Slavic holiday celebrated on the night from 6th to 7th July')
    dreamgirl "On Ivashka Kupala you could do this and that!"
    th "Chill out, you horny monster. {w}Let things take their course."
    th "For once I'm beginning to feel responsible for my words and actions, and you're suggesting that everything is reduced to trivial bedfellowship."
    dreamgirl "You're impotent, aren't you?"
    dreamgirl "Hey, somebody upstairs! They gave me a defective body, give me a working one!"
    th "Alright, calm down. {w}Look, her skirt's up again."
    dreamgirl "Hey, that's my line!"
    hide dreamgirl_overlay
    show sl normal pioneer2 with dspr
    sl "What's all the silence about?"
    "The girl turned around."
    show sl shy pioneer2 with dspr
    sl "Or are you again..."
    "She smoothed out the skirt."
    me "I'm offended by your assessment that I'm only thinking of one thing."
    show sl smile2 pioneer2 with dspr
    sl "And you don't?"
    me "Yeah. Sometimes I still want to eat and sleep."
    show sl laugh pioneer2 with dspr
    sl "What a multifaceted man!"
    "The path blended into the clearing, from where it was only half a kilometer to the campfire, and Slavya walked beside it."
    with fade
    show sl normal pioneer2 with dspr
    sl "What did you think of this morning's hike?"
    me "Honestly?"
    me "Tried very hard to forget everything that was going on until you reminded me!"
    show sl smile pioneer2 with dspr
    sl "I'm sorry, I'm sorry."
    "She stroked my head."
    scene
    $ renpy.show("bg ext_path_day", what = Dawn("bg ext_path_day"))
    show sl normal pioneer2
    with dissolve
    sl "But you look like a smart boy, so I thought maybe you could enlighten a silly girl from the district center."
    if alt_day4_sl_cl_tut_iz:
        me "Sorry, sunshine, but they didn't teach us that at school, even though they taught us advanced math and other perversions."
    else:
        me "If you compare the sensations, it was very similar to what I experienced when I tried to turn off the buzzer."
    me "I mean, quite possibly some kind of security system."
    th "By the way, I was pretty sure that such things would be invented later."
    me "The viscous abomination at the exit remains unclear to me, though I can assume there's a heating element or a chemical reaction that melts a solid substance and allows you to apprehend an intruder."
    show sl surprise pioneer2 with dspr
    sl "So if you were there alone, or I was there alone..."
    me "Yeah, the descendants would have found white bones in about three hundred years."
    show sl serious pioneer2 with dspr
    sl "Okay. And the smoke, so it's sleeping gas?"
    "I jerked my chin."
    th "I'm not going to tell her my strange visions, okay?"
    me "I can't say. {w}One thing's for sure, whatever it is, it's best not to contact it."
    me "Oh, and for future reference, I'm not going there again."
    "Slavya nodded."
    me "Neither will you."
    show sl smile pioneer2 with dspr
    sl "And rightly so!"
    "Smiled the girl."
    sl "What are we even supposed to do there?"
    hide sl with fade
    "I saw them first and almost put my arm out, trying to stop my traveling companion."
    "Luckily, I reacted in time, got my hands back, and intercepted my precious cargo. {w}Otherwise we'd have to pack it all in, not reassemble it."
    me "Stop!"
    "Slavya reacted quickly - she stood up as if she were standing still."
    "And without turning around, just in case, without even moving, she asked:"
    sl "What happened?"
    me "Look under your feet."
    "Slavya cautiously crouched down."
    "And took one short step back."
    hide sl with dissolve
    "Smart move."
    "One more step and I'd have stepped on one of those things that's been chasing us underground."
    "They're peaceful, but you never know how they'd react if you stepped on them."
    "I remembered an acquaintance of mine had a marmot maul both legs to the bone, defending himself catlike with his hind legs."
    "It was a long time ago and not true, and in truth I was sure it was the simplest fable."
    "But it was very timely that the fable came to mind."
    me "What shall we do?"
    sl "Let's go around."
    "The snark shuddered, and, squinting blindly at his huge eyes, stretched up his muzzle, wiggled his nose, and quirked his ears."
    "That animal seemed to place a great deal of importance on hearing."
    "And before I knew what I was doing, I was making the same sound I always used to chase the cats away from my door."
    me "HISSSSSSS!"
    "I hissed."
    "The snark jumped on the spot, fidgeted around restlessly, and finally yelped and scrambled away into the bushes."
    me "You say they won't come out before nightfall?"
    "I stretched out."
    show sl normal pioneer2 with dspr
    sl "This is probably the most restless one. A kind of traveling frog."
    "Slavya shrugged her shoulders serenely."
    me "We should warn the squad leaders."
    me "Or else the pioneers will be led here, what if someone steps on it."
    show sl laugh pioneer2 with dspr
    sl "I assure you, when the pioneers are led here, the fauna themselves will run away - because there's an instinct to get out of the way of the herd."
    "I glanced at her - the girl was smiling serenely."
    "Probably didn't relate the concept of 'herd' to the pioneers."
    "Eh, how innocent they all are here."
    stop ambience fadeout 2
    scene bg ext_polyana_day
    with dissolve
    play ambience ambience_forest_day fadein 3
    play music music_list["two_glasses_of_melancholy"] fadein 1
    "The trees parted, and we emerged into a fire glade."
    "Finally. {w}Another ten minutes of this, and I would have begun to doubt the value of all these preparations."
    me "So why are we here, after all?"
    show sl smile pioneer2 with dspr
    sl "In general, of course, to clean up."
    "Slavya smiled so sincerely..."
    me "And honestly?"
    show sl smile2 pioneer2 with dspr
    sl "I'm honest!"
    me "Not enough."
    "I cut her off."
    show sl normal pioneer2 with dspr
    sl "And where did you come from, so sensible."
    "I carefully feigned polite attention."
    sl "As long as I'm still trusted, I'll abuse my power to get us out somewhere where we can do something together. {w}You don't mind?"
    me "I don't mind doing something together."
    me "Will bonfire be right after dinner?"
    sl "Yes. And before bedtime. How about some baked potatoes?"
    "I was quite indifferent to this delicacy, which is what I told the girl."
    show sl sad pioneer2 with dspr
    sl "Too bad. It would have been so... {w}But to the point."
    show sl normal pioneer2 with dspr
    sl "There will be one fire, the main one, so we don't touch the other fireplaces, we work only with the main one."
    sl "Make sure all the linings are in place, and if wild beasts turned over or undermined a stone somewhere, you return it to the fire pit. {w}Are we clear?"
    me "And you?"
    show sl laugh pioneer2 with dspr
    sl "And I'll help you morally."
    "Slavya replied."
    "And she giggled, having had enough of the distraught look on my face."
    with fade
    sl "I'll get to work cleaning up the main clearing."
    "Finally she took pity on me."
    show sl normal pioneer2 with dspr
    sl "I'll make sure there's no garbage, branches, cones, and so on. It's a tedious job, but unlike yours, it doesn't require much physical strength."
    th "You got that right about physical strength."
    "After sighing for a while like a Wells tripod, I staggered to the fire pit."
    scene
    $ renpy.show("bg ext_polyana_day", what = Dawn("bg ext_polyana_day"))
    with joff_r
    "As Slavya had warned me, the job was fraught with heavy lifting."
    "One more thing - it was absolutely impossible to do it without getting dirty."
    "I mean, if Slavya had done it - she certainly would have managed to stay clean and tidy."
    "Not my case."
    "The fire pit was a small depression in the ground, lined with stones to prevent fires."
    "These stones proved to be the first problem - leaving greasy black marks on my hands that I had no way to wipe off."
    "And yes - there really were fewer of them - Slavya kept calling out to me as she found another rock."
    "And here I am, as handsome as a chimney sweep, dragging another ceramic bar, muttering the unprintable."
    "The number two hitch was the ash and ash deposits - kudos to Random for having a little rainfall, so I could bury them here or take them to the woods on the bayonet of a shovel..."
    "Of course, if we had brought a shovel with us!"
    "But, as they say, man is a god only in the subjunctive mood - or, more simply, everyone's hindsight is strong."
    "I had to confiscate one of Slavya's bags and try to wield it directly, sneezing and coughing at the minute from the fine particulate matter flying in the air."
    "So by the end of the cleanup, I looked like the devil out of Soloha's pipe."
    "Slavya waved her hands at me."
    scene
    $ renpy.show("bg ext_polyana_day", at_list = [zenterleft], what = Dawn("bg ext_polyana_day"))
    with blind_d
    show sl angry pioneer2 with dspr
    sl "Don't even think about coming near me looking like that!"
    "She bounced back from her seat when I tried to get closer."
    show sl normal pioneer2 with dspr
    sl "Semyon, you're as dirty as I don't know who."
    "Digging in her pocket, she pulled out a mirror and, holding it in her outstretched hand, showed me all the unearthly beauty of my new appearance."
    me "We'll be right back at camp, I'm going to take a shower."
    show sl sad pioneer2 with dspr
    sl "No, I'm not taking you to camp like that."
    me "What, are you going to let me live in the woods?"
    show sl smile pioneer2 with dspr
    "A wide smile was her answer."
    "…"
    with fade
    show sl normal pioneer2 with dspr
    sl "Okay."
    "Slavya took pity on me."
    sl "There's actually direct access to our river here."
    sl "I have soap."
    me "How did you know..."
    "I grumbled."
    show sl laugh pioneer2 with dspr
    sl "Semyon, it's you! You boys get dirty all the time - you can believe me, I grew up in a big family."
    me "Yeah, I know that."
    th "I wonder if I'll be treated like a seventh brother now?"
    show sl smile2 pioneer2 with dspr
    sl "Do you mind?"
    "Not really..."
    me "Okay, what else do I need to know?"
    show sl normal pioneer2 with dspr
    sl "Well... About whether we have enough time."
    me "And will we have enough?"
    sl "Plenty! Let's go."
    "Contradicting herself, she took my hand and led the way."
    sl "You don't have to be shy with me, I have experience bathing my brothers, I'll help you."
    th "I wouldn't dream of being shy."
    sl "Just stay out of my way, I can see better from the side."
    stop music fadeout 3
    stop ambience fadeout 6
    return

label alt_day5_sl_cl_bathing:
    scene bg ext_beach2_day_7dl with blind_l
    play music music_list["dance_of_fireflies"] fadein 3
    play ambience ambience_lake_shore_day fadein 3
    "We came out on the bank of the river with a fairly convenient descent."
    "I think this is where the pioneers did their labor, washing the cauldrons with sand and mustard."
    "Or at least just laundry soap."
    show sl normal pioneer2 with dspr
    sl "I know you're wearing swim trunks, so don't even think about convincing me that you're shy."
    sl "Take your clothes off!"
    me "Oh, how nice that sounded."
    "I snorted, shaking my arms in front of me with obvious innuendo."
    show sl sad pioneer2 with dspr
    sl "Ohohohoh, you're my woe."
    "The girl sighed, unbuttoning my shirt."
    me "Excuse me, this isn't picking cones."
    show sl shy pioneer2 with dspr
    sl "This... May I?"
    "Her fingers rested on the belt buckle."
    me "If I say «no», what are you going to do?"
    show sl angry pioneer2 with dspr
    sl "You're teasing me again."
    "I held my breath as I watched her loosen the belt, unbutton the top button of shorts."
    show dreamgirl_overlay with dspr
    dreamgirl "This is not erotica! This is pornography!"
    "Summed up the inner voice, nevertheless clearly trying to capture as much of the experience as possible."
    me "Thank you, I'll take it from here."
    "Something stirred inside me, and I decided that if we kept this up, Slavya would see more than I wanted to."
    "I jumped out of my shorts and headed for the water."
    "A few seconds later my heightened hearing picked up another set of clothes falling to the ground and Slavya stepped into the water beside me."
    dreamgirl "YYEEEEEHAAAAAAW!"
    show sl normal swim with dissolve
    "In a swimsuit."
    "The girl stood up next to me."
    sl "What?"
    "She was surprised."
    dreamgirl "What-what! The swimsuit!"
    "I shook my head negatively."
    show sl shy swim with dissolve
    "Being near a girl in the water is an experience in itself, and it's exciting enough."
    "And if that girl is also wearing a swimsuit like that..."
    show sl normal swim with dspr
    sl "Semyon, keep your hands to yourself."
    "Businesslike advised the girl."
    sl "Close your eyes, I'll wash your face."
    "She stood close to wash me, and I froze."
    "In anticipation."
    show blink
    pause(1)
    scene anim prolog_1
    show dreamgirl_overlay
    with blind_r
    dreamgirl "Until contact! Five… {w}Four…"
    "We silently hooted in unison."
    dreamgirl "And now she's slowly soaping her paws and starting to fondle your... Your everything!"
    sl "Give me the soap!"
    dreamgirl "Come on, come on, before she realizes you've got some snoosmummericks crawling around on the ground while you're in the water doing silly things."
    th "Didn't the party decide they were harmless?"
    "I got distracted for a second and, as a result, I missed the best part - the first seconds of touching."
    "Although cold soapy hands are certainly a bit different from the affection I had hoped for."
    sl "Well... {w}That's it!"
    "I was about to say something, but then I felt two palms on my chest."
    sl "Flush."
    "And she pushed me into the water with force!"
    play sound sfx_shoulder_dive_water
    scene anim_underwater with dissolve
    "I caught my breath, and the water rushed into my nose and ears..."
    "From the surface came Slavya's merry laugh:"
    sl "There's an oil slick all around you! Call the environmental patrol!"
    "Such a good girl and such a pest!"
    play sound sfx_water_emerge
    scene black
    scene bg ext_beach2_day_7dl with easeintop
    show sl normal swim with dspr
    sl "Semyon, this is no good! After dinner, I'll be sure to take you to the baths."
    sl "You have to bathe every day."
    th "After dinner, honey, there's a bonfire, but I definitely won't remind you of that."
    "She washed the rest of the soot off my forehead."
    sl "There! At least now you look human."
    "And she turned me toward her."
    "It occurred to me that if I wanted to now - and I will!"
    th "Okay, you! Get out of my mind."
    dreamgirl "Come on! Are you that greedy or what?"
    show sl shy swim close with dspr
    sl "How do you think..."
    "She was so close that I could feel her blood current under the skin."
    sl "Why is the natural process of meeting, getting to know each other, courting a person so problematic?"
    "She covered her eyes and stroked my shoulders."
    sl "If you see someone and you know they're right for you, why all the conventions?"
    show sl normal swim close with dspr
    sl "Or should the crown of creation suffer from the moment of conception?"
    "I jerked my shoulders, covered in goosebumps."
    me "I don't know."
    "I answered."
    "And it was true."
    scene black
    $ renpy.show("bg ext_sky_7dl", what = Dawn("bg ext_sky_7dl"))
    with easeintop
    "She didn't know how to kiss - and where on earth would an ideal person learn such wisdom?"
    "It only added to the charm of our kisses - as if I had seduced a girl who was right in every way."
    "I guess that's why the second kiss was just as sweet as the first."
    "Or was it because my naked breasts were touching the almost naked breasts of the most desirable girl?"
    "Already having little control over myself, I wrapped my palms around the slender back and pulled so that the pitiful remnants of space fell into oblivion."
    "I pulled away from her lips - with reluctance - and kissed where the blue vein was pounding frantically."
    "Slavya groaned and thrust herself toward me."
    "Even closer."
    "Completely submissive to the hands stroking her back."
    "A second kiss under her ear, I lightly bit her lobe, and she finally surrendered - shuddered somehow, trembled, bit her lip."
    sl "Semyon..."
    "Hotly she exhaled into my ear."
    sl "That's not fair, you know?"
    "I know, of course."
    me "You don't like it?"
    sl "I'm afraid."
    "Calmly she replied."
    sl "That it's going to be bad, and then you'll leave."
    "I froze."
    scene bg ext_beach2_day_7dl at zexitcenter
    show sl normal swim
    with dissolve
    "The girl freed herself easily from my arms, and took a step back."
    sl "I'm a terrible coward, I'm always afraid of things."
    me "And now, too?"
    show sl smile swim with dspr
    sl "And now — even more so."
    dreamgirl "Yes, yes, you can kiss me, but you can't touch me!"
    "She looked at my disappointed face and couldn't stand it - giggled:"
    sl "Well, I won't wash you anymore, since you're so excitable."
    sl "Here you go."
    "After handing me the soap dish, she turned around and ran to the shore with a splash."
    sl "Catch up!"
    "I heard her laugh."
    "I hummed and followed her."
    "When I got out of the water, she was already standing on the shore with her clothes on."
    show sl normal pioneer2 with dspr
    me "How did we even have this conversation if I'm the one who's easily agitated?"
    "I muttered, wiping myself off."
    show sl laugh pioneer2 with dspr
    sl "I don't know about that."
    sl "I'm a good and positive girl, an example to everyone and an activist, I'm not allowed to think about such things."
    me "But if you really want to, you can!"
    show sl normal pioneer2 with dspr
    sl "Anything is possible, just be careful. {w}Let's go, great things await us!"
    hide sl with dissolve
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_sl_cl_supper:
    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_medium_crowd_indoors_1 fadein 3
    play music music_7dl["tilltheend"] fadein 5
    "The canteen was humming like a beehive."
    "All the pioneers were excited about camping, and I was momentarily happy for them."
    "It's great when whatever the adults have prepared resonates with the children so vividly."
    "It is, of course, not the least because there is no other entertainment."
    "This isn't «Aurorovets» with wireless, high-speed, and completely free Internet access throughout the camp."
    "I've seen the contemporary «pioneers» — who are all staring at their cell phones and tablets."
    "An instrument designed to unite mankind has ended up dividing it even more."
    "After all, it's those damned 30 percent of «working» internet relations - what about those who have only two or three friends online?"
    "Right. {w}To keep them all online."
    th "I could make friends with every one of you."
    "Silently I turned to the audience."
    th "I would open my eyes, and there would be a separate 'Sovyonok' group on Skype or ICQ, people from which never send a word - as well as from the 'personal' and 'ars moriendi' groups."
    th "In the former, those I kicked out of my life, and in the latter have either removed themselves or once ventured to tickle their wrists with a steel feather."
    th "Buy me some of your attention, a birthday or New Year's present - at least half an hour's deliverance from the horror of loneliness for a sitting in a void, an eyeless, faceless mannequin."
    th "Because you can enjoy loneliness, you can cherish it and revel in it, too."
    "But you can't survive against it decisively."
    "Even if you are alone in a crowd of happy children."
    show dreamgirl_overlay with dspr
    dreamgirl "What are you missing, muzzle? {w}Join the party, the crowd is generous with emotion."
    th "I don't know."
    th "Maybe it's the fact that you have to open up - and that's not my thing."
    "It's very scary to open your eyes with your nose to the monitor, to find every human being, alive, three-dimensional, warm - just a set of pixels and lines of code in yet another passing toy."
    "And with my karma, that's pretty much the only outcome I'm likely to see."
    stop ambience
    scene
    $ renpy.show("bg int_dining_hall_day", what = Notch("bg int_dining_hall_day"))
    show rain_overlay
    with dissolve2
    "I felt myself standing at the cold, bulletproof glass that cooled my palm."
    "Leaving on the other side the warmth, the summer, the happy screams."
    "Getting louder and louder."
    "The world was successfully rejecting me, and my most needed, capable of knocking the crap out of my head with one presence, was walking somewhere else."
    show mt normal pioneer with dissolve
    mt "Semyon, don't sleep!"
    hide mt
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    scene
    $ renpy.show("bg int_dining_hall_sunset", what = Notch("bg int_dining_hall_sunset"))
    show rain_overlay
    with joff_r
    "Before I knew it, the day outside the windows had changed to sunset."
    "One more wast...{w} lived day, and before I go to sleep I'll put it in a dust bag and tie it up with a smart ribbon and hide it somewhere in a closet of memory."
    "On a shelf that smells of laundry soap and soot and dungeons."
    "With a tag: «You really didn't dream it»."
    stop music fadeout 10
    "Finally, already changed Slavya plopped down opposite of me."
    play ambience ambience_medium_crowd_indoors_1 fadein 3
    scene bg int_dining_hall_sunset at zenterleft
    show sl normal pioneer2 at cleft
    with dissolve
    sl "Missed me?"
    me "Very much!"
    "I answered honestly."
    show sl serious pioneer2 with dspr
    sl "You'd put something on, too."
    "Concernedly, Slavya tilted her head sideways."
    show sl normal pioneer2 with dspr
    sl "You just got out of the infirmary. {w}It's no good if you get there again."
    me "What, you're too lazy for carrying my breakfast?"
    "Her right eyelid drooped down in a wink."
    show sl smile2 pioneer2 with dspr
    sl "Not at all! It makes me happy."
    show sl normal pioneer2 with dspr
    sl "But I need you healthy!"
    "That sounded a little ambiguous."
    "That's why I was interested:"
    me "Why?"
    show sl happy pioneer2 with dspr
    sl "Don't you have any idea?"
    "The girl bit her lip and tilted her head sideways. {w}An old French proverb about what it means to tilt a girl's head came to mind."
    me "Dragging something around again?"
    "I frowned."
    me "Sweeping the square or painting the fence?"
    th "No, why? {w}It's still half an hour before the fire, we're just in time!"
    me "I'm warning you - I'm going to protest! {w}I've just been working hard, walking a lot, being frightened by rats and almost leaving my sandals in that slop."
    me "Paws off my leisure!"
    "Slavya smiled wider and wider with each line I said, until, with her head thrown back toward the ceiling, she laughed - sincerely, loudly."
    show sl laugh pioneer2 with dspr
    sl "Semyon, you're such a whiner! Who knew!"
    sl "You could have told me it was so hard for you, I could have handled it myself."
    "The girl was having a good time."
    me "It's not hard to work, but sometimes you have to rest."
    show sl smile pioneer2 with dspr
    sl "Alright!{w} Tonight is all about relaxation, all right?"
    "Olga, who heard this remark, was about to say something, but she was yanked by Viola's hand and leaned close to her friend's ear and whispered something."
    th "Something magical, no other way!"
    "The counselor instantly forgot about us."
    "Although, all in all, this is the second night Slavya has blatantly shirked her volunteer duties."
    me "I guess I'll listen to you. {w}I'm going to go put on a sweater."
    show sl normal pioneer2 with dspr
    sl "See you on the square."
    "Nodded the girl."
    stop music
    stop ambience
    scene black
    with fade2
    pause(1)
    scene
    $ renpy.show("bg ext_sky_7dl", what = Noon("bg ext_sky_7dl"))
    with dissolve
    th "Dear sky, take my gaze and keep it as a separate star - for someone who will one day look into you, alone."
    th "Wink at them with my gaze, for a gaze into you is a gaze into the past, and some inhabitants of Gamma Cepheus, my contemporaries, are looking into the sky and can see me belonging to their time - here in the world of '89."
    th "Or reflect it somewhere at the cusp of 10 to 12 light years in case I'm thrown back one day - there's too much happiness in me and it's bouncing around, swirling my head like champagne."
    th "Dear sky, one day you'll see us - adults holding hands - but in a completely different place, in a different city and possibly the universe."
    "One more sealed package - the addressee: heaven - and I slam the cabin door behind me."
    play sound sfx_open_door_clubs_2
    play music music_list["lightness"] fadein 2
    scene bg int_house_of_mt_sunset with blind_d
    play ambience ambience_int_cabin_day fadein 3
    "It's quite logical to take the phone, there is a desire to catch a shot with Slavyana - now every such frozen moment is somehow transfixed by inexplicable meaning."
    "That's right, someone dear to your heart is capable of turning any thing into an object of your fetish."
    "But I mean business."
    "The sweater was a little stiff after the wash, and after wrinkling it a little, I knotted the sleeves at the shoulders."
    "I put my swimming trunks away for a long time because I don't know when I'm going to go swimming."
    "I decided not to take jeans - there are few mosquitoes here, and the temperature down to zero I am able to endure and in shorts - the main thing was to keep my torso warm."
    th "I will not take the player, I will not have time to listen to music."
    show dreamgirl_overlay with dspr
    dreamgirl "The only thing missing is roses, chocolates, and rubber products, and it'll be a complete gentleman's set."
    th "And they'll hang us on a bow tie, yeah."
    "Once again convinced that there was nothing more for me to do here, I made my way outside."
    play sound sfx_open_door_2
    pause(1)
    scene bg ext_square_sunset with dissolve
    "The pioneers had already gathered in the square, lined up at the line, and Ulyanka, climbing onto the podium, was throwing Nazi gestures from there."
    th "Huuuuuh?!"
    "I looked closely."
    th "I imagined it."
    "Actually it was the pioneer salute - just a little modified."
    "If I'd been younger, I would have..."
    show dreamgirl_overlay with dspr
    dreamgirl "Yes?"
    th "No, nothing."
    dreamgirl "That's right. One would think of you too - what if this vegetable has a soul, too?"
    th "Oh, screw you!"
    dreamgirl "That's as much as you want. {w}You know, besides the two attempts to influence the subconscious, there are some other changes in you."
    th "Like what?"
    dreamgirl "I think it's appropriate to say that your blonde is quite successfully influencing and educating you."
    th "And what does that consist in?"
    dreamgirl "Well, for instance, what's the purpose of the sweater you're wearing? Did you really believe you'd get cold at night?"
    "I've rolled that thought around a bit."
    th "No. {w}It's just that Slavya told me to get dressed."
    dreamgirl "And you..."
    th "Dressed, what?"
    dreamgirl "You're swimming shallow, dig deeper."
    th "Are you implying that I obeyed her orders?"
    show dreamgirl_overlay with dspr
    dreamgirl "I'm not hinting at anything, you figured it out all by yourself."
    th "Or did I take it with because she might catch a cold?"
    hide dreamgirl_overlay with dspr
    "My subconscious threw a Cheshire cat smile at me and went silent."
    "Slavya pushed her way through the rows and stood beside me, ignoring the slanted stares of the pioneers present."
    me "Aren't you embarrassed by other people's attention anymore?"
    show sl normal pioneer2 with dspr
    sl "Ah."
    "Lightheartedly she brushed it off."
    show sl smile pioneer2 with dspr
    sl "It never embarrassed me. {w}But the fact that someone would pry into something that didn't concern them, of course, was a little embarrassing."
    "Meanwhile, the squad leader kicked Ulyana off the podium and climbed up there herself."
    sl "Somehow it didn't seem right if our couple became the object of discussion."
    me "It's inevitable in society. {w}Man is a social animal."
    show sl normal pioneer2 with dspr
    sl "Right!"
    sl "I thought about this for a long time, until I realized that people somehow get married, then have children, make children documents, introduce a new person into society."
    me "Are you implying that you have to come to terms with this?"
    show sl smile pioneer2 with dspr
    sl "It's more on the fact that it's okay if someone suddenly talks about you... about us. {w}Publicity is inevitable."
    "Her logic was a little over my head, but I decided not to argue."
    me "So now you're going to walk hand in hand with me and turn your nose up?"
    show sl normal pioneer2 with dspr
    sl "Well, I don't think I'll turn up my nose."
    sl "But I'll remember that it's okay..."
    $renpy.notify('Malysheva - A person on a Russian TV, her most famous show was about how male testicles work')
    th "Malysheva, get in the studio!"
    sl "...and any topic of discussion will sooner or later bore a man."
    th "I would argue with that."
    "I remembered the anonymous message boards I used to sit on when I was a PC-athlete."
    "That's where people used to manage to discuss a single game for years."
    show dreamgirl_overlay with dspr
    dreamgirl "Not an indicator. Mentally fulfilled people quickly cool down and leave, leaving either spiritually poor people who have nothing to compare it to..."
    with fade
    dreamgirl "...or the mentally ill, the fanatics who are willing to put their lives on the altar of service to an invented idol."
    th "Reeks of religion, doesn't it?"
    dreamgirl "For such people it is a religion."
    show mt normal pioneer at right with dspr
    mt "Camp, on the 'first to second' count!"
    "The counselor's order flew in."
    voice "First!"
    voice "Second!"
    "Flew along the ranks."
    "When you're fourteen or fifteen years old, drill looks like a fun game."
    "And then in the army you're already an automaton following all the commands."
    "Slavya was standing next to me, so she was first, I was second."
    $ meet('dn', 'Curly')
    dn "Second!"
    "It came from the other side of the parade ground."
    dn "Counting's over!"
    mt "First numbers step forward."
    play music music_list["always_ready"] fadein 5
    "The ranks broke and split in half."
    "Whoever came up with all this formation stuff was clearly a genius at organizing."
    "If we now, like a herd of sheep, began to pair off on the principle of «want - don't want», we'd be here until morning."
    "And this way..."
    "Slavya clutched at me with a 'I won't give it up' look, and Olga Dmitrievna, looking at us, quietly hummed."
    show mt smile pioneer with dspr
    mt "To the right! {w}The squads, except the first, to the fire glade in stride... march!"
    "She stepped off the platform and came toward us."
    show mt normal pioneer with dspr
    mt "I see you've already decided on a couple."
    "Slavya nodded."
    mt "What about your roommate?"
    "Slavya shrugged her shoulders."
    mt "I see."
    mt "Shurik, follow me, Electronik, Zhenya's on you."
    "I couldn't make out what the Buzzer was muttering, but I guess enthusiasm wasn't even close to overnight there."
    mt "Alisa, with Ulyana?"
    "After waiting for a nod, the counselor continued:"
    mt "And Lena goes with Miku. {w}It's a good thing there aren't twenty-five of you, like the first shift."
    "Imagining twenty-five AWOL pioneers, each with their own opinions on all things in the world, made me shudder and once more refrain from pedagogical activities."
    "After counting us head to head once more, the squad leader turned and headed for the gate, clearly typing her stride - all that was missing was a horn player and a drummer for the full effect."
    hide mt with moveoutright
    th "Here she is, a person who has lived her whole life under the conditions of Soviet society."
    "Slavya took me by the hand and led me right behind the Electronik."
    me "You start waving your arm around, too."
    "I grumbled, more as a joke."
    show sl normal pioneer2 with dspr
    sl "Yeah? {w}Isn't that a little childish?"
    "I rolled my eyes."
    me "Actually, it was a joke."
    "I thought she understood jokes. {w}Are there topics on which her sense of humor fails?"
    "Not listening to me, {w}Slavya actually started waving her clasped hands around."
    me "Aren't you being too light-hearted?"
    show sl smile pioneer2 with dspr
    sl "What's the big deal? {w}You know, I'm doing that now, and I'm in a better mood."
    sl "You aren't?"
    "I didn't say anything."
    scene bg ext_backroad_day_7dl
    play ambience ambience_forest_evening fadein 3
    "You just realize that sometimes the wisest thing to do is just accept your own ignorance or callousness."
    th "If you like it, I'll tolerate as long as it takes."
    "I couldn't say exactly what, from my point of view, would be the right behavior for a couple."
    show dreamgirl_overlay with dspr
    dreamgirl "They must walk around with sorrowful faces and grimace in tune."
    dreamgirl "And sometimes allow themselves romantic nonsense like listening to music by earpiece for each or carrying a girl across a creek in their arms."
    dreamgirl "The latter - not with your constitution, of course."
    hide dreamgirl_overlay
    with dissolve
    th "You mean I can't lift her?!"
    "I resented that, and as I slowed down, I picked Slavya up in my arms."
    scene cg d5_sl_hugs_7dl
    with flash
    "She shrieked, nonetheless, wrapping her arms around my neck."
    "The formation broke, the pioneers stopped."
    "We just went out the gate."
    me "It's all right!"
    "I gasped."
    "The weight, of course, was felt, but I was quite capable of dragging the girl in my arms."
    me "She just saw a mouse."
    un "Where?!"
    "Lena hid behind Miku."
    me "She... ran away!"
    "The redheads whispered and chuckled quietly, throwing glances in our direction."
    scene bg ext_backroad_day_7dl with dissolve
    "And I brought Slavya down to earth."
    show sl shy pioneer2 with dissolve
    "She was smiling and all flushed."
    scene bg ext_backroad_day_7dl
    show sl shy pioneer2 at left
    with dissolve
    sl "That was very unreasonable!"
    "She reprimanded me."
    sl "What if you had dropped me?"
    me "Not any more unreasonable than waving your arms around here! {w}Don't you trust me?"
    show sl normal pioneer2 with dspr
    sl "I trust you. {w}But I'm heavy!"
    me "As you can see, not heavy enough."
    "I went further, catching up with the counselor, still clutching the girl's palm."
    "This time it was me who walked first."
    "And she, apparently for a change, decided to let me take the lead."
    "Pourquoi à la pas?"
    "The rest of the pioneers, judging by the stomping, followed us."
    scene
    $ renpy.show("bg ext_path2_day", what = Dawn("bg ext_path2_day"))
    with dissolve
    "There was no sense in walking in pairs along the paths; after all, they had been tramped on the basis of a squad moving in single line."
    "So it wasn't a minute before we were lined up in a single column."
    "Need I say, I let Slavya go first?"
    "This time she was already mentally prepared for immodest stares."
    "That's why she didn't flinch at my signs of attention."
    "She was nervous, though, apparently almost physically feeling the attention."
    "I was just enjoying the hike."
    "I had already set some landmarks for myself on our previous visit here."
    "Holding Slavya by the elbow, I nodded at the flags we'd drawn."
    "She nodded and, catching up with the squad leader, spoke to her about something."
    "Olga, after listening to her arguments, thought a little..."
    "Who can guess in three times who was assigned to take care of this matter?"
    "A deafening groan filled my throat, itching from within."
    "But with a cringe in my heart, I nodded."
    "Even ostentatiously for some reason I wanted to look better than I really was."
    "The very dust in my eyes, I understand."
    "Anyway, for tomorrow morning I suddenly had something to do..."
    "God damn it."
    show sl normal pioneer2 with dspr
    sl "Do you need help tomorrow, or can you do it yourself?"
    "I shrugged."
    th "I wish I knew how to handle it."
    me "Let me try it first."
    sl "Okay."
    "Activist nodded."
    show sl smile pioneer2 with dspr
    sl "Because tomorrow is the last day before we leave, there's going to be a lot of rushing around."
    me "What do you mean, last day?! Isn't it a three-week shift?"
    show sl normal pioneer2 with dspr
    sl "Three, but you were late, remember? {w}Got to the last week, so..."
    "Slavya walked beside me, looking around covertly, took my hand."
    "A giggle came from behind me immediately, and I, without turning around, showed back a bulging middle finger with my free hand."
    show dreamgirl_overlay with dspr
    dreamgirl "I don't think they understood the meaning of your gesture."
    "The giggle turned to laughter."
    th "Who ever cared. {w}They seem to understand quite well, though."
    "Slavya didn't seem to notice anything."
    stop music fadeout 3
    with fade
    return

label alt_day5_sl_cl_campfire:
    scene bg ext_polyana_sunset with dissolve
    play music music_7dl["lastlight_guitar"] fadein 3
    "A few more minutes, and the clearing opened up to view."
    "I think I'm beginning to understand the logic of Slavya's actions."
    "Because I caught myself thinking that instead of looking for a place to sit comfortably, I first glanced around the open space to see if it was littered or dirty."
    "The logic of a man who doesn't want to go into the universe, instead stretching his backyard to its size."
    "Otherwise, how else do you feel like a master in the vast expanse of the Universe without slipping into a morally obsolete igni et ferro?"
    "I don't mean this as a bad thing or a good thing. {w}There's no way grades work here."
    "Because every five or seven years I've changed where I live, my social circle, and my surroundings."
    "A new place, an aglaonema without roots."
    "And for some, just the whole of Russia or the USSR is home."
    "The fire glade felt like part of one's own home, so a mess on it could make one almost physically uncomfortable."
    "Like most of the places we visited together."
    "That's probably also why I didn't turn down Olga Dmitrievna's appointment."
    "Because if there's something wrong somewhere in your house, you have to go and make it right."
    scene
    $ renpy.show("bg ext_polyana_sunset", what = Dawn("bg ext_polyana_sunset"))
    with blind_d
    "The ranks mingled, the pioneers settled on logs according to the chain of command, or simply in circles, and Slavya, with a nod to me, went to the fire pit, where the wood was already waiting to be stacked in a log cabin."
    "Still, there was something about all that pioneering and camping."
    "Something that their ideological heirs, the children's recreation, sports, and labor-rest camps, had lost."
    "Because it's no problem to take kids' phones away for the rest of the shift, keyed into a safe, or not handing out wifi left and right by putting up 'no internet, talk to each other' signs everywhere."
    "But it's still not enough."
    "It is necessary to boil in this cauldron from birth, to develop the mentality of a Soviet man who understands that people are not perfect, but the prejudice puts trust and positivity."
    "I covered my eyes, remembering my last bonfire - that was already in the SRC, went about the same scenario."
    "But the difference is that here the pioneers were brought in, seated, and then they entertained themselves, enjoying both the evening and the busy campfire - Slavya lit it with one match, without using a kindling."
    "The same kids I remembered also came to socialize and have an experience as a result. But before that there had been half an hour of sepulchral silence, caprice, attempts at rebellion, and the like."
    scene bg ext_polyana_sunset
    with blind_d
    "And that's not bad, all in all. Because these same kids then reacted much more positively to the hike."
    "Although they whined that the backpack was heavy, the shoes were uncomfortable, and they were tired."
    "But then there was Lake Beauty, potatoes with picked mushrooms on a griddle right from the fire, and sitting well past midnight until the edge of the eastern sky touched a light crimson."
    "For the older ones, understandably, there was also their own bit of romance in the form of lemon moonshine and obscene guitar songs with a quite logical continuation through the tents."
    "The kids teased afterward «oversalted soup — cook in love»."
    th "Yeah, that happened. {w}If I'd been here before, I probably wouldn't have been able to avoid something like this, either."
    th "Except without the liquor."
    th "Not a fact, though."
    "Miku pulled a guitar out of nowhere and twirled the picks, tuning it."
    "The redheads were seated next to her, and, judging by the mischievous expression on Ulyanka's face, they were already up to something."
    "What could they be up to, though - either a slate in the fire or a smokestack in there, too."
    "It took Electronik a long time to get away from the librarian, who had to put in a lot of effort before she was able to get rid of the bore."
    "Then, showing a high degree of busyness, she talked to Lena about something."
    "Shurik, whom I hadn't seen all day, felt my gaze, raised his head and nodded, then immediately returned to his notebook, in which he was either writing or drawing something."
    "After wrinkling his head a little, Electronik stepped back to it."
    "Olga had been led away earlier by Sanich, who had winked at me."
    "The whole posse was in their place."
    show sl normal pioneer2 with dspr
    sl "Resting?"
    "Finished with the fire, Slavya sat down next to me."
    me "Yes."
    "I answered unilaterally."
    "After hesitating a bit, she clarified:"
    show sl shy pioneer2 with dspr
    sl "Do you mind my company?"
    "You don't have to ask."
    show sl normal pioneer2 with dspr
    sl "Just if I'm in the way..."
    me "Nah. We're a tili-tili-dough now, after all."
    show sl smile pioneer2 with dspr
    sl "Stop laughing about it!"
    "She never seemed to figure out how to behave properly in my presence."
    "As long as she was oblivious, relaxed, and behaving normally, it was great and easy."
    "A girl with a talent for picking up keys to hearts, she was disposable from the first minute."
    "But the moment she remembered that «it's complicated with us», and she would begin to behave unnaturally."
    "Just like now."
    "Lena probably could say «you're in the way» — she's full of complexes or the tactful El, who was a dullard when it came to talking about Zhenka."
    "But not Slavya."
    me "Enough is enough."
    "I nodded compliantly, covering her fingers with my palm."
    "She twitched, but she realized I wasn't going to let anything extra happen, and she smiled."
    "I felt someone's eyes on me, and I turned around sharply."
    show un shocked pioneer far at left with moveinleft
    "Lena."
    "She stood looking at us intently."
    "Realizing she was discovered, the girl blushed, pressed her palms to her cheeks, and turned away."
    hide un with moveoutleft
    me "Watch out for redheads, they obviously have some kind of show on their mind."
    show sl normal pioneer2 with dspr
    sl "I know."
    me "How?"
    th "Is she going to show the world the wonders of physiognomy now, too?"
    show sl laugh pioneer2 with dspr
    sl "And they always have some kind of mischief on their mind. Every time we go camping, they come up with something."
    me "And you're so calm about it?!"
    show sl normal pioneer2 with dspr
    sl "What else is there to do with them?"
    "She shrugged her shoulders serenely."
    sl "We can't deprive them of a hike for something they haven't done or only want to do."
    sl "All that's left to do is to be vigilant. {w}And try to prevent mischief."
    "Such an approach to the matter aroused quite a healthy skepticism:"
    me "So? {w}Have you ever managed to prevent it?"
    show sl smile2 pioneer2 with dspr
    sl "No."
    "Disconcertingly honestly answered Slavya."
    sl "But I'm not discouraged - if I can prevent a prank at least once, then it's not all in vain."
    me "Have you tried unzipping their pockets?"
    show sl normal pioneer2 with dspr
    sl "How can you do that?! They haven't done anything."
    "Slavya resented."
    sl "Wait a minute."
    hide sl with dissolve
    "There was some shouting on the other side of the clearing, and Slavya hurried over there."
    "Olga Dmitrievna, who had been heading our way, also changed her trajectory and went to the other side of the fire."
    "I looked around again at those present and, after thinking for a while, quite logically assumed that the redheads had probably already begun to act."
    th "Now we'll see how effective the preventive measures are."
    "I thought about getting up and seeing what was going on, but the wind carried a short chuckle from the nearest bushes, and I hurried over there."
    "My intuition didn't let me down - apparently Alisa was to organize a noisy distraction while Ulyana engaged in the actual execution of the plot."
    scene cg d5_us_ghost with diam
    "And what the plot was, it became clear almost at a glance."
    "Because among the 'treasures' neatly laid out on the ground, everything exploded, smoked or soiled in one way or another."
    "From the looks of it, they had been preparing thoroughly and for a long time."
    "And the highlight of the program was to be a piece of slate..."
    "Which Ulyanka was about to throw into the fire with a slingshot!"
    me "Don't you dare!"
    "I rushed to her."
    "But what could I do."
    "The tourniquet unraveled with a quiet hiss, sending a piece of the shingle straight into the fire."
    "A little off the program - but who's relieved by that!"
    me "You little..."
    "I didn't have time to finish because the fire gave the right temperature and the crime weapon went off."
    stop music fadeout 3
    return

label alt_day5_sl_cl_dn_aid:
    play sound sfx_muffled_explosion
    scene bg ext_polyana_night with vpunch
    "The bang was loud enough to make everyone jump out of their seats."
    "After showing me her tongue, Ulyanka put the slingshot in her pocket and ran away."
    play music music_list["glimmering_coals"] fadein 3
    "The camp rumbled."
    "It's not nice to be meditating on a fire when it suddenly explodes, so they all freaked out."
    "It's pretty easy to go gray from that, huh?"
    "Perhaps it was only the fact that the pioneer is instilled with respect for adults and elders that kept Alisa from being lynched on the spot - for some reason everyone immediately thought of her."
    th "Amazing, isn't it?"
    with fade2
    "But as the minutes ticked by, the clenched fists unclenched, the anger and fright vanished, the friendly laughter of the pioneers rang out more and more, who appreciated how frightened they had been."
    "People turned out to be too lenient; they could have knocked him in the butt a couple of times for a scolding."
    "Alisa was well aware of that, and didn't even argue, sitting quietly on the log, peering around her."
    "She met my gaze and turned away."
    "The pioneers were calming down, only the familiar curly-haired kid kept shouting something."
    "Reacting belatedly, the counselor called for the nurse who was supposed to accompany us on this hike, according to the rules."
    "Viola came over and, judging by the pioneer's flushed ears, told him to undress."
    th "That's right, what else would you expect from our comrade educator."
    "After scattering the confiscated scraps in my pockets, I came out of the bushes."
    "And approached Viola."
    show cs smile with dspr
    cs "The burn is superficial, the incision is shallow, I applied ointment, but it's better not to disturb the leg yet, otherwise it may bleed."
    me "A piece of slate?"
    "Viola nodded."
    show cs normal with dspr
    cs "So ask your comrades to take you to camp."
    show cs normal at left with moveinleft
    show dn sick pioneer at zenterright
    with dissolve
    dn "But I..."
    cs "Or, if you feel strong, jump on one leg. Can you make it to camp that way?"
    "After estimating his strength, curly shook his head."
    me "Maybe we should get Boris Alexandrovich involved? He's strong, he'll carry the pioneer away."
    cs "I'd love to, but I'm afraid Boris... mmm... Alexandrovich won't be able to help us."
    me "Why not?"
    show cs smile with dspr
    cs "Because he has recused himself for the duration of the bonfire. His presence here is not necessary - unlike mine."
    show dn normal pioneer
    hide cs
    with dissolve
    "She nodded and walked back to Olga, talking to her about something."
    me "Oh well..."
    "I sighed."
    me "Okay, get on my back."
    "I said."
    me "Since I'm big and heavy today."
    show dn unsured pioneer with dspr
    "Curly looked at me doubtfully and shook his head."
    me "Fine."
    "I shrugged."
    me "Then walk. Or rather, jump on foot."
    "After thinking and sighing for a while, the pioneer took me up on my offer."
    hide dn with dissolve
    "Yeah, well, yeah, like he had any choice."
    show sl normal pioneer2 with dissolve
    sl "You seem to be working as a loader today?"
    "I rolled my eyes and said nothing."
    hide sl with dissolve
    "The blonde's attempts at humor were hilarious to me. But nothing more."
    $ persistent.sprite_time = "night"
    $ night_time()
    play ambience ambience_forest_night fadein 3
    scene bg ext_path2_night
    with fade2
    "They let us go back only on Slavya's word of honor that nothing would happen to us or anything."
    "Viola didn't even promise - it seemed to amuse her to throw people into conditions totally hostile to them and watch the person swim out."
    "And this despite the fact that she was walking with us!"
    "We lined up in single line - Slavya was in the vanguard with a lantern: after the first molehole she turned on the lantern and devoted herself entirely to following the road."
    "Because who cares about the molehole, but what if there's another hole to the bottom layers again?"
    sl "Semyon, when we get to camp, I'll be gone for half an hour, okay?"
    "I nodded."
    "Angel wants to do something lowly? Take a bath, or something?"
    me "And then?"
    show sl smile pioneer2 with dspr
    sl "And then we'll see!"
    show cs smile at right with dspr
    cs "Pioneer girl, watch the road, please. I don't want the pioneer to break his leg."
    cs "Because you and I won't carry both pioneers!"
    "Imagining Viola carrying me in her arms, I couldn't stand it and giggled."
    cs "Look at him, he liked the idea."
    "Violetta snorted and doubled her guard."
    hide cs
    hide sl
    with dissolve
    "Slavya followed her example."
    "And the pioneer was pretty heavy!"
    "It suddenly occurred to me that I never asked his name."
    me "Hey, what's your name."
    "I threw at him."
    dn "What?"
    me "What's your name?"
    dn "Daniil. {w}Danya."
    $ meet('dn', 'Danya')
    me "Tell me, Danya, yesterday didn't you, by any chance, put a button on the chair for the counselor?"
    "The answer to me was eloquent silence."
    th "Isn't that what's happening now, that I'm saving Ulyanka in pants?"
    "An unsolicited thought appeared in my mind."
    th "But isn't even Ulyana's life and health priceless?"
    show dreamgirl_overlay with dspr
    dreamgirl "I don't know, I don't know."
    dreamgirl "Now you're dragging him, and tomorrow he'll do you a disservice - not out of spite, but simply out of a prankster nature."
    dreamgirl "By the way, if I were you, I'd get your back checked when you take him down to the infirmary."
    th "Check for what?"
    "The inner voice chuckled and went silent."
    "And I didn't understand anything."
    "That's my motto."
    play music music_7dl["iwantmagic"] fadein 3
    scene bg ext_entrance_night_clear_7dl
    with dissolve
    "In the meantime we had already reached the camp gate."
    "Danya on my back went limp - he appeared to be motion sick."
    stop music fadeout 3
    scene bg ext_clubs_night
    with dissolve
    if (not alt_day4_sl_cl_tut_iz):
        "And I cowered cautiously at the building of the clubs, causing a chuckle to form on the nurse's full lips."
        show cs smile with dspr
        cs "Don't worry... pioneer. {w}Your exploits yesterday didn't go in vain."
        me "They turned it off, didn't they?"
        cs "Specialists came by this morning, someone got a good kick in the head, someone got his quarterly bonus taken away."
        cs "Today there were already some pioneer girls weaving macramé."
        th "And tomorrow, when the kindest doctor lets Shurik go, the cybernetics club will occupy the room again and build another mechanical goon."
        th "And rightly so."
        th "Ordinariness is the best indicator that things are running their course, in basic mode."
        "I wasn't a fan of adventures. Ever. {w}I mean, I don't mind having any rather vivid experiences."
        "But adventure most often means overcoming some kind of trouble."
        "And I hate trouble."
    show sl normal pioneer2 at left with dspr
    sl "Semyon, how are you feeling?"
    "Slavya took out a handkerchief and blotted my forehead - dragging heavy pioneers was a rather tedious task after all."
    sl "Why don't you take a break?"
    me "I've walked all the way through the woods, and it's three hundred meters to the infirmary."
    sl "Suit yourself."
    play sound sfx_pat_shoulder_hard
    "She patted me on the shoulder and stood beside me."
    sl "I'll leave on the square, like we agreed."
    "I nodded."
    stop music fadeout 3
    stop ambience fadeout 6
    return

label alt_day5_sl_cl_cs_reward:
    $ persistent.sprite_time = "sunset"
    scene bg int_aidpost_night with flash
    play ambience ambience_medstation_inside_night fadein 3
    with None
    "And five minutes later, having unloaded the pioneer in the isolation room, I went out to the infirmary."
    show cs smile with dspr
    cs "Pioneer, you helped me a lot today."
    "Violetta languidly stretched out."
    cs "I could hardly have done it without you."
    "Her robe rattled dangerously on her chest, and the top button - the third already, by the way - came undone as if by itself."
    show cs shy with dspr
    cs "That's why I wanted to thank you."
    "She came closer to me."
    show cs shy close with dspr
    cs "Properly."
    "Her tone had already habitually made me get goosebumps and blush."
    "My attitude toward Viola was something akin to the respectful apprehension one feels for a suddenly uncaged, well-fed predator of the feline family."
    "I mean, right now she might rattle you and knock you down by poking you in the stomach with her forehead, but if she gets hungry or pissed off, then..."
    "Okay, it's best not to think about that."
    "Although, I'm sure if we chat a little longer, I'll be sure to develop the correct modus operandi."
    "I will understandably never develop immunity to the charm of a vamp woman - if only because I will never stop viewing her as an extremely attractive person."
    "But at least I'll stop getting lost like a fifth grader at a physical exam."
    th "Although she's a little old for a pioneer, she's really quite my age."
    th "I wonder if she would behave the same if I were here in my old guise."
    "A look of bewilderment flashed in her multicolored eyes, and I realized I'd gone off the deep end somewhat untimely."
    cs "So you don't think."
    "She tried again, letting the hoarseness into her voice."
    show cs smile with dspr
    cs "That I don't know how to be grateful."
    me "I don't..."
    "Protested me."
    cs "Wait."
    if alt_day_binder == 1:
        "She stepped back to the table, where I remembered some very curious things were kept."
        "The very appearance of which in the communication between a man and a woman is somewhat inflammatory."
    "I froze."
    "She reached for the right drawer."
    "I stopped breathing."
    "Then, apparently regaining her senses, she laughed, slapped her forehead, went to the left side of the table, where there was a single drawer, and drew from there a bottle of dark glass."
    show cs normal with dspr
    cs "Unfortunately, the girl has nothing to thank the brave young man with."
    "She murmured."
    show dreamgirl_overlay with dspr
    dreamgirl "How about a girl's honor?"
    th "How about you shut up, huh, how about that?"
    hide dreamgirl_overlay
    cs "So I can offer you this."
    "I tore my gaze away from her cleavage and switched to the present."
    "It turned out to be a bottle of «Ostankinskoe»."
    me "Aha. {w}Pardon my immodest question, where did you get it?"
    show cs smile with dspr
    cs "I have free time, too."
    "Viola smiled."
    cs "When you don't come in."
    cs "But since we have strict rules here and anyway, if you accept the gift, consume it here."
    cs "Because you know, the pioneer… {w}On the camp grounds… {w}With beer… Emergency!"
    cs "Of course, it's not such an emergency as a pioneer with hawthorn tincture…"
    me "How do you know?"
    show cs grin with dspr
    pause(.2)
    show cs smile with dissolve
    "And while I was slowing down, it was all decided for me again."
    play sound sfx_open_dooor_campus_1
    show sl normal pioneer2 at left with easeinright
    "Slavya walked into the infirmary."
    "Her hair was dry, apparently she hadn't gotten to the water yet."
    "I never thought I'd say this - but now she was extremely, extremely inappropriate!"
    "Cringing from the cold between my shoulder blades, I folded my arms behind my back and made an attempt to fall through the ground."
    "But something narrow, hard was pressed against my back."
    "It was Miss Collider, staring thoughtfully at something on the ceiling, forcing me to stand still."
    "She'd already taken her beer somewhere - you can't drink away the talent!"
    me "Are you an electro-sensor or something?"
    "I siphoned."
    "And, without too much affectation launched with a push forward, took a step toward Slavya."
    me "You haven't..."
    "I couldn't think of anything smarter than to ask the obvious."
    "Like on an airplane, an attempt to get acquainted - «Excuse me, are you also going to Egypt? Maybe also to Sharm el-Sheikh?»"
    "Given that the goal is always the desire to get into the rooms, isn't it easier to ask substantively right away?"
    dreamgirl "No shit, Sherlock."
    show sl serious pioneer2 with dspr
    sl "Not yet. A few words with you."
    hide sl with easeoutleft
    "She went outside, and I wandered doomfully after her."
    stop music fadeout 3
    play sound sfx_open_dooor_campus_2
    pause(1)
    $ persistent.sprite_time = "night"
    scene bg ext_aidpost_night
    with dissolve
    play ambience ambience_camp_center_night fadein 3
    play music music_7dl["lonesome_shepherd"]
    "A little more, and Slavya's faith in me, and in humanity as a whole, might have been shaken."
    "It's gathering outside again, in what I call St. Petersburg rain, when there's just a kind of watery suspension in the air, available to all winds, spitting on gravity and the airtightness of clothing."
    "The clouds squeezed out by it had long since been scattered by the wind, and there was a Scorpion or some other exotic critter scowling above - I've never been into astronomy, but the sky was unfamiliar."
    show sl normal pioneer2 with dissolve
    sl "Shall we sit down?"
    "Slavya took something off my back and crumpled it up and threw it in the trash can."
    "The rain didn't seem to bother her at all."
    "After brushing off the lumps and debris, she sat down herself, patting it invitingly beside her."
    "It smelled damp, pine trees, and rolling toward midnight."
    "A magical time, the daily anticipation of the holiday."
    "Viola was muttering about something, flicking the buttons of her 'Microshee', the snoring of the crippled Danechka came from the window in the isolation ward, and soft conversations could be heard from somewhere on the side of the cabins."
    "The camp grew weary and trampled the ground, making itself comfortable for the night."
    dreamgirl "And tomorrow is a royal night, and you have to close the doors tightly or stay awake so you don't wake up with toothpaste on your face."
    th "They have powder here."
    dreamgirl "Well, redheads will think of something. Good old «tank keys» and «falling ceiling», for example."
    show sl serious pioneer2 with dspr
    sl "I was thinking of going for a swim in the lake."
    "I nodded."
    "We went quiet."
    me "Boring."
    sl "And I hardly feel bored."
    if alt_day4_sl_cl_lf_solo == 0:
        "Just like yesterday - pardon me, this night - she laid her head on my shoulder."
    else:
        "She smiled and put her head on my shoulder."
    sl "It's been a busy day."
    me "Like you always have."
    scene cg d5_sl_bench_night_7dl with blind_l
    sl "Also true."
    me "You're not pouting at me for the campfire scene?"
    me "I don't think so."
    sl "Not at all.{w} The reaction was amusing."
    sl "It's true what they say, boys think about {i}this{/i} several times a minute."
    me "They're lying."
    sl "I knew it."
    me "There's far more than several times. {w}A lot more than that."
    "With my arms around her shoulders, I pulled her a little closer to me."
    me "Luckily, I'm not."
    sl "Oh?"
    me "Yes. {w}I'm a unicum."
    sl "And what does that manifest itself in?"
    me "Someday I'll be sure to tell you."
    play sound sfx_punch_medium
    sl "So!"
    "I got hit on my naughty hands - it didn't hurt, but it made sense."
    sl "You didn't have to get under my shirt."
    sl "You almost had me believing you weren't like that."
    me "But I am!"
    sl "And you want me to believe that?"
    sl "Or do your hands work apart from your mind?"
    me "They do."
    "I took another shot and got my hands on it again."
    me "We could get caught by the nurse at any moment. {w}Or the squad leader looking for her best pioneer girl."
    me "And here we are... groping."
    sl "And that doesn't embarrass you?"
    me "Honestly? {w}It just makes me even more excited."
    me "Actually, of course, there's something about it... {w} The old story of the princess and the bully."
    sl "And you're the bully?"
    me "No, no, no. {w}I'm the storyteller."
    sl "And me?"
    me "And you're the prompter in the orchestra pit."
    th "I don't think I've been drinking..."
    me "You've got a script and you're showing your fist to the mediocrity on stage."
    sl "Then who are our Princess and Bully?"
    "She smiled."
    "I thought for a while and suggested:"
    if (not alt_day4_sl_cl_tut_iz):
        me "Three candidates: Electronik and Zhenya."
    else:
        me "Two candidates: Electronik and Zhenya."
    sl "One."
    "Slavya bent her finger diligently."
    me "Sanich and Dmitrievna - they seem to be on a roll."
    sl "That's a pass. {w}They have a purely business relationship."
    "I twitched my free shoulder incredulously, but said nothing."
    if (not alt_day4_sl_cl_tut_iz):
        sl "And number three..."
        me "Shurik and his mechanical goon. {w}If he hadn't lost the chassis last year, he might as well have developed his robot Chappie by now."
        sl "Chappie?"
        me "Dog food."
    sl "Yeaaaaah.{w} Semushka, is your head always such a mess?"
    scene bg ext_aidpost_night
    show sl smile2 pioneer2
    with dissolve
    sl "I'm listening to you, and I can feel myself getting pulled deeper and deeper into some kind of maelstrom."
    me "Like today? {w}In the dungeon."
    "She nodded softly."
    show sl normal pioneer2 with dspr
    sl "Only this time no brave pioneer lies down with his back to the mire, so I can get to the other side without getting my feet wet."
    "I noted to myself that for a pioneer, the girl's speech was a little too literary."
    sl "And you live in it all the time."
    sl "I couldn't do that. {w}Where are you moving your hand, put it back."
    me "You'd think you'd have everything in place..."
    "I obediently put my hand back on her waist."
    "Well, as well as I understood the word «waist»."
    "Viola was enthusiastically painting the playing field with squares, the «shepherd» was floating over the camp, and life was plain and simple."
    "Except that somewhere in the far corner of our big house there's some damn thing going on."
    sl "You're doing it again, aren't you?"
    "Slavyana said quietly."
    sl "Can't you sit still?{w} What's so exciting about touching a girl's mammary glands?"
    "She took my palm off, which was really high up."
    "A new piece of patch on my heart."
    show dreamgirl_overlay with dspr
    dreamgirl "More like libido."
    show sl serious pioneer2 with dspr
    "She stroked my hand, which she still held."
    sl "I'm taking a bath. {w}And I suggest you take a cold shower."
    stop music fadeout 3
    hide sl with dissolve
    "After laughing, she left."
    "Well, I went back to the infirmary.{w} Something there required my decision."
    "Had to spend some time getting myself cleaned up, getting myself under control, of course."
    "It's not like Viola's going to get it wrong."
    th "If anything she's the one who'll get it right."
    "But the consequences..."
    play sound sfx_open_door_clubs_2
    pause(1)
    $ persistent.sprite_time = "sunset"
    scene bg int_aidpost_night
    with flash
    play ambience ambience_medstation_inside_night fadein 3
    with None
    show cs normal at center
    play music music_list["farewell_to_the_past_edit"] fadein 3
    "After smearing the drizzle on my face and cheering up a little, I went to the infirmary."
    "Here it was just as I'd left it - Viola at the EGA monitor screen, painting the field already three-quarters full and figuring out how to cut one frantically beating square from the other."
    "Genda's portrait was back on the cabinet."
    "Ordinary days."
    "For some it is commonplace to live in a warm, orange holiday."
    "One can be jealous, of course. {w}But someone has to work beyond the Arctic Circle, too, and breathe crap in Norilsk, take watches for half a year at the lighthouses."
    "That last job was my dream for the last five years, I guess."
    "Too bad I'm not a meteorologist."
    show cs smile with dspr
    cs "Pioneer, you're not hopeless."
    "Viola grinned without turning around."
    cs "You've got something between your ears, if you know what's good for you, squeezing a pioneer girl in your state."
    me "What do you want from me, who are you anyway?"
    cs "Do you want to see my documents?"
    me "Show something else."
    "I brushed it off."
    me "To somebody else."
    cs "No can do."
    "Viola replied seriously."
    cs "Immoral behavior, pioneer molestation - who better than you, after your morning escapades, and lunchtime lecture, could understand it?"
    show cs smile with fade2
    cs "Well, don't pout."
    "She smiled."
    "The quad she controlled took another ten percent, and she cheered up."
    cs "I am not a devil or a sorcerer, my whole «extra» was only enough for a «C» on mass psychology on 4th year.{w} Unlike someone else."
    "She squinted incredulously at the portrait of the General Secretary balancing on the very edge of the cabinet."
    cs "We are Kazanis, almost Tatars, but not Tatars, my father is Swiss Cern, all his life he worked in nuclear physics, my mother is French, real, with a prononce, can you imagine?"
    cs "She told everyone she was from Paris, maybe she wasn't lying, who can tell, she worked for the Dotr and Auger-Kovarsky triumvirate all her life, until she was kicked out for not wanting to become a UNESCO ambassador to the Soviet Union."
    cs "Well, she kind of did, and she dragged my father away."
    cs "Now in Kazan-Ryazan, a flat the size of a soccer field, a library - one can get lost, and zero love for her own daughter. And here I am.{w} Treating kids for constipation, gonoris causa, damned it be."
    cs "You don't have to be a therapist psychologist to get all your cockroaches out under a magnifying glass into the sunlight."
    cs "How old are you? Thirt... Ahem, seventeen?"
    "The clause was Freudian, but my mind was on something else."
    show cs normal with dspr
    cs "Oh, man, you obey the same mechanisms."
    cs "I'll sit next to you, and it'll shake you like it did ten years ago."
    "She held out her narrow palm and beckoned me to come closer."
    "I obeyed."
    show cs smile close with dissolve2
    cs "Closer."
    "One more step."
    cs "Pioneer."
    "From that distance you could already smell patchouli and some kind of moisturizer."
    "And both were wisely mixed - some of my acquaintances use perfume like they pour three liters on their heads, then you can't stand next to them."
    "She put her index and middle fingers between the buttons on my shirt."
    "Her pads were dry and hot."
    cs "You're like a heron, frozen on your left leg. And standing."
    "Overcoming my feeble resistance, Viola pulled me close to her so that I was practically touching her."
    cs "I see the beer is familiar to you, but the fact that you haven't asked about it until now is also suggestive."
    cs "Do you think you can live up to the high honor of a young man of Feoktistova's for long?"
    "I shrugged."
    me "I'll try."
    cs "Then try."
    "She turned away from the monitor completely."
    cs "Go on! She's waiting for you."
    cs "This is very important to her."
    "She opened the bottle and placed it beside her."
    me "Good night."
    "Quietly shutting the door, I went out."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_sl_cl_night:
    $ persistent.sprite_time = "night"
    scene bg ext_lake_night_7dl with dissolve
    play ambience ambience_lake_shore_night fadein 3
    play music music_list["forest_maiden"] fadein 2
    "Slavya visited me at the very end, so by the time I was kicked out of Cernovna's light, someone was already watching his first dream."
    "But, of course, not Slavya - she, as an activist, a beauty, and in general a wonderful girl, was guaranteed some kind of indulgence."
    "And, accordingly, I'm a bit of a stickler, too."
    "It's always nice to bask in someone else's reflected rays - the full effect of being there without the side effects of publicity and dozens of prying noses in your dirty laundry."
    "It cost me a lot of trouble just to find this place."
    th "How was she walking alone in the woods?!"
    "It occurred to me."
    th "Isn't she afraid of anything at all?"
    "Because the squeaks and screeching of the nocturnal inhabitants almost made me go gray on the way."
    "Though it would have seemed simpler to follow the instructions on a piece of paper pinned to the very bench where we'd been squeezing for half an hour earlier."
    "«Before you leave the camp, after the gate to the right, follow the path to the entrance to the forest. Along the fence walk for 300m, and from the gate to the music club turn left again, you will come out on the path, and go straight ahead, without turning anywhere»."
    "Beaded handwriting, letter to letter, a 3%% smartphone charge as a cheat sheet light, and a soul firmly nestled in my heels."
    "The price of having a chat with Slavya with no witnesses."
    "When I emerged from the woods, the moon had already climbed into the sky, streaking a silver path from that shore right under my feet."
    show sl normal pioneer2 with dspr
    sl "You came after all."
    "I turned around."
    "Slavya was standing by the old bridges, trim, bathed in moonlight, impossibly beautiful."
    me "You'd think I had a choice."
    sl "There's always a choice."
    "Quietly she said."
    me "And what choice did I have?"
    sl "It's not like anyone dragged you here by the hand; you could very well have been out midnight with Viola and beer and computer games."
    th "You noticed it after all!"
    me "Yeah, somehow, you know..."
    sl "Yeah?"
    me "I thought you'd be sad without me..."
    show sl sad pioneer2 with dspr
    sl "Is that all? {w}Calm down, I've been swimming alone all my life at night, and I'm not the least bit sad."
    me "...and I thought I'd be sad without you."
    "I continued as if she hadn't interrupted me."
    "She never wore a tie from the moment we fenced the pit. And I was in a disheveled state, too."
    "It's strange that the counselor didn't reprimand her."
    "And then everyone was out of it."
    sl "Word is out."
    sl "You're going for a swim?"
    me "Uh... I don't really have anything for swimming."
    "After I got back from the fire pit, I changed my swimming trunks, so..."
    sl "That's okay."
    "Slavya shrugged."
    show sl normal pioneer2 with dspr
    sl "Neither do I."
    scene cg d2_slavya_forest with dissolve
    "The way she unbuttoned her shirt could be in all the textbooks of how to seduce a man who doesn't want it."
    "I only came to my senses when she was wearing nothing at all, and a laughing laugh spread in all directions over the standing water."
    scene bg ext_lake_night_7dl with dissolve
    sl "Well, what are you standing there for? {w}Get undressed."
    "Together, at night, in the woods by the lake."
    "There was something even romantic about it."
    "Slavya was pushing me towards something."
    "At the same time, she slapped my hands and successfully fought off all my advances - apparently she wanted something else."
    "And what was that?"
    if persistent.hentai_graphics_7dl:
        scene cg d5_sl_swimming_7dl with dissolve
    "And yet it would be great to get a hold of the commissar's body!"
    "And she's all so brave, active, needed everywhere, important, and I've got her here in my own way, in my arms, to my chest, you can have her right there in the water..."
    "And no difficulties, incomprehensible creatures, dungeons, fog and security systems of prohibitive level of technology even by the standards of the twenty-first century."
    if (alt_day2_date == 'sl'):
        "The biggest difficulty here was me."
        "Couldn't bring myself to accept the offer - an outstretched hand, in fact."
        "Why?"
        "Because I'm a fool."
        "The biggest idiot in the world."
        sl "You don't want to, do you?"
        "She broke off laughing."
        me "It's not that..."
        sl "I thought we had trust..."
        if alt_sp > 0:
            me "Look, it's not fair to say that."
            sl "Is it fair to leave a girl alone in the water?"
            "Her unpretentious banter helped with the paralysis."
        else:
            me "Trust. {w}But..."
            sl "I see. Go gather wood for the fire then, we'll get warm when I'm done."
            me "Will do!"
            "I was glad when I felt I was in business."
            "But I didn't move."
            sl "What will you?"
            "She laughed."
            "And that helped with the paralysis."
            "But first, a bath!"
    "I threw off my clothes, leaving me in just my boxers with the bears."
    if persistent.hentai_graphics_7dl:
        scene cg d6_sl_swim with blind_r
    sl "Come on!"
    "She splashed water in my direction."
    sl "Don't be so afraid, I won't eat you."
    sl "I might even turn away."
    "She did turn away, allowing me to get rid of any remaining protection."
    "Nude bathing."
    "Nudist family, my ass."
    "Not that I insist on the obligatory bathing suit..."
    "But with all the views..."
    "The neighborhood was... exciting."
    scene bg ext_lake_night_7dl with dissolve
    "The water was so warm after the heat of the day following the rain that I could hardly feel it around me."
    th "Like steamed milk."
    "Came suddenly to mind."
    "I swam up to Slavya and froze beside her, making only small movements to keep to the surface."
    "She intercepted my gaze across the water to somewhere deeper below the surface and laughed resoundingly."
    "There wasn't much to see, unfortunately."
    sl "Semyon, how do you manage to think about anything else at all, if you have so many thoughts on this subject?"
    me "Aren't you at all shy?"
    sl "What's there to be embarrassed about? This is how we are born, this is how we sleep, this is how we let a new person into our lives."
    sl "It's a rare moment when man and Nature think alike."
    me "I've heard something to the effect that nudists can sense their surroundings not only with their usual five senses, but also..."
    sl "Nudists?"
    me "They like to swim and sunbathe in the nude."
    "I answered."
    sl "That's right, I can feel you all the time, no matter where you are."
    sl "And with no clothes on, I can pick up your desires."
    play music music_7dl["iamsadiamsorry2"] fadein 3
    "Her smile was maddening."
    sl "You always have the same wish, though."
    sl "I wonder how it will end, if it's granted."
    "She swam closer."
    "Even closer."
    me "I'm afraid it just can't be fulfilled. {w}It's like a hunger, an urgent need that can only be satisfied for a while."
    sl "And then again?"
    "She opened her eyes."
    sl "And again?"
    "There were a few centimeters between our bodies."
    "If we were on the beach, I could probably feel her warmth by now."
    "But here all we had to do was to be satisfied with our sense of smell."
    "And, of course, touch."
    "Because I couldn't resist again."
    "But I didn't get a slap on the wrist this time."
    "Instead, Slavya looked strangely into my eyes."
    "At night her pupils seemed bottomless."
    "They really were, far less so than Viola with her medical hypnosis."
    "The distance disappeared."
    "Our naked bodies intertwined."
    stop ambience
    scene anim_underwater
    "And Slavya finally got to my lips."
    "How we didn't drown, I don't know, but at one point I found that we were about three feet underwater and just weren't paying attention to silly things like lack of air."
    "I let my hand go down from the chest, down the side, to her thigh."
    "And pressed her against me."
    "She looked at me in surprise when she felt my fingers where she didn't expect to feel them at all, and she pushed me away and floated to the surface, leaving me alone with the yet another sorrowful «nooooooo!»."
    play sound sfx_water_emerge
    play ambience ambience_lake_shore_night fadein 3
    scene bg ext_lake_night_7dl with easeintop
    sl "You've got to keep your cool."
    "She strictly said a minute later, pulling me over the water and letting me catch my breath."
    sl "Eating should be cultured, unhurried, and enjoyed."
    sl "And making love, too!"
    me "How do you know how to make love?"
    "She turned dark and sailed back half a meter."
    sl "I'm sure of it! {w}Hurry is only necessary when catching fleas."
    me "Are you implying that I, like in the jokes, will quickly finish my business and snore?"
    if persistent.hentai_graphics_7dl:
        scene cg d5_sl_swimming_7dl with dissolve
    sl "Don't even think about it."
    sl "I'm already carrying you all the time!"
    sl "No, when you get home, you can sleep all you want, but in the meantime, bear with it."
    "I followed her, and a few yards later I felt a shallow bank under my feet."
    sl "It's enough that I can hardly tell my own experiences from yours."
    sl "Remember the first time you trusted me?"
    "She put my hands on her shoulders."
    if herc or loki:
        "And took a tiny step - the space between us was gone."
    else:
        "And froze, skillfully keeping her distance."
    if persistent.hentai_graphics_7dl:
        scene cg d5_sl_moon_7dl with flash
    sl "And then…"
    if herc or loki:
        me "A kiss on the top of the head."
        "Slavya almost purred with pleasure."
    else:
        "She smiled."
    sl "So lonely, so frustrated, so sad - like a lost child."
    sl "So desperate, so embittered..."
    "She hugged me herself, clinging with all her strength."
    me "I'm not desperate..."
    "Slavya put her finger on my lips, interrupting."
    sl "I can feel you, you won't be able to lie."
    sl "On some special level I feel what you feel."
    sl "And then..."
    sl "That's when I realized I'd fallen in love like a fool and could never leave."
    "She twisted in her arms and kissed me so that I forgot how to breathe."
    "She laughed, catching that experience as well, and wandered toward the shore."
    "A real witch."
    "Though it is not the night of St. John's Eve."
    stop music fadeout 3
    scene bg ext_lake_night_7dl with fade
    play music music_list["afterword"] fadein 3
    if persistent.hentai_graphics_7dl:
        show sl2 normal body with dissolve
    else:
        show sl2 normal pioneer2 with dspr
    "By the time I got to the shore, there was already a small fire smoking, and Slavya, who had never dressed, was warming her heels thoughtfully and looking up at the sky."
    "Unlike her, who was not at all embarrassed about her own nakedness, I felt somewhat uncomfortable with my bare butt under the night sky, so I got dressed in a hurry."
    "The look I had been under all this time, I would define as a little mocking."
    if persistent.hentai_graphics_7dl:
        show sl2 normal body close with dspr
    else:
        show sl2 normal close pioneer2 with dspr
    "And only after that sat down next to her."
    sl "What do you think is really down there?"
    me "Who knows, Comrade Major."
    "I answered honestly."
    me "I've been figuring it out both ways, one realistic and one shitty."
    me "Which one do you want?"
    if persistent.hentai_graphics_7dl:
        show sl2 smile2 body close with dspr
    else:
        show sl2 smile2 pioneer2 close with dspr
    sl "Let's go in order."
    me "In order, so in order."
    "I nodded, gathering my thoughts."
    me "Either way, it looks like there's something of interest down there, since so many people arrived this morning. {w}So either the men in plainclothes are coming, and they're going to close down the damn camp."
    if persistent.hentai_graphics_7dl:
        show sl2 normal body close with dspr
    else:
        show sl2 normal close pioneer2 with dspr
    sl "Yeah."
    me "Or they knew for a long time."
    me "And that's when the lousy sheep comes out."
    me "Because setting up camp over an unexplored site is so incompetent that..."
    "I cut myself off."
    me "I would have asked the builders some unpleasant questions in general - both about the government tunnels under the camp, and about the mines below."
    me "Why was construction allowed at all - take a kilometer east and build. {w} Aren't there any GOSTs about it?"
    sl "I don't know."
    hide sl2 with dissolve
    "Slavya got up and started to get dressed."
    "The full picture of a couple after a good night."
    "Except it wasn't a very good night."
    me "So about your idea about shutting everything down in there, I fully support it."
    me "Though if it were up to me, I'd blow the whole place up and backfill it so there'd be no way through."
    me "But this, as I understand it, could disrupt the underground infrastructure, so no one will ever give 'permission' for this."
    if not alt_day4_sl_cl_tut_iz:
        me "And I can't get that buzzer to stick anywhere - it's falling out of all theories, for crying out loud."
    show sl2 normal pioneer2 with dissolve
    sl "The reasoning is logical, but it doesn't give the answer to the question «what to do»."
    "The eternal Russian questions - who is to blame and what to do. {w}How should I know?"
    me "Do nothing."
    "I answered."
    me "We'll caulk the hole tomorrow, so the snarks don't climb to the surface."
    me "The counselors and the bosses won't give us away, no one will know we were there."
    me "Let's live to the end of the shift and go home, and let the high foreheads in the 'chaikas' deal with this."
    show sl2 angry pioneer2 with dspr
    sl "I don't like the 'my house is on the edge' principle."
    "Slavya frowned."
    th "And I do."
    th "It's better to remember in forty years' time how you climbed the catacombs and left the end of the story up in the air than to get signed up and become a no-go, whose whole misdemeanor was being in the wrong place at the wrong time."
    me "Slavya, sweetheart."
    show sl2 serious pioneer2 close with dspr
    "I took her by the shoulders and looked into her eyes."
    me "Understand, there's a measure of competence - and we don't fit in there."
    me "You've seen for yourself, people are working, they haven't let it go to waste."
    me "So there are experts, too."
    "Slavya shook her head, about to object to something, but I put my finger to her lips."
    me "You're not going instead of Viola to cure children or instead of cooks to make breakfasts, are you? Because - what? {w}Right, because professional activities are better left to professionals."
    me "Let people work. {w}There's some stuff we don't understand."
    me "They might understand, but we certainly don't."
    show sl2 sad pioneer2 close with dspr
    sl "Okay."
    "Slavya whispered."
    show sl2 happy pioneer2 close with dspr
    sl "We'll do as you say - we'll think of something with hole and forget everything else."
    show sl2 smile2 pioneer2 close with dspr
    me "There's a smart girl."
    "I got up and kissed her on the forehead."
    me "Now it's time to go home and go to sleep."
    stop music fadeout 3
    stop ambience fadeout 6
    stop sound_loop
    return

label alt_day5_sl_cl_sleeptime:
    scene bg ext_path_night with dissolve
    play ambience ambience_forest_night fadein 3
    play music music_list["a_promise_from_distant_days"] fadein 5
    "The way back, as it always is, was perceptibly shorter than the way there."
    "Especially when there's a palm in my hand and eyes in front of me, and you can stop and kiss minute by minute, or you can just revel in the fact that you can."
    "A step towards is taken, as from a slope, each next step will be easier."
    "Bright little man, sunshine."
    "I've always had a limited amount of 'sunshine,' not many sparks of warming light held in my heart."
    "One, two, three at most."
    "People I was always happy for, for whom I could get up in the middle of the night and drive across town to meet from the air or the ocean."
    "People around whom I could afford to be generous, not shy about wanting to give them a gift or make them smile."
    "And for the last few years, I haven't had a single sunny face like that."
    scene bg ext_path2_night
    with dissolve
    "I guess my heart is just tired of yearning for warmth."
    "I can close my eyes - I won't remember faces - I've always had a bad memory for them - but it will echo with the sound of a voice, a touch, a smell."
    "In Slavya's case, it's now also the taste of lips."
    "Sweet? I don't know. {w}Kissing is overrated, it's just the touch of skin against skin, cleanly washed has no taste or smell."
    "Do books lie?"
    "Up until now I thought so, pretty much."
    "Until I realized it wasn't about the five senses. After all, if love is something in the air that you can't feel in any way, it's silly to rely on the signaling system."
    "It has to be judged by something else."
    "A sweetness in the heart, in the bottom of the belly, an anticipation, a chill under the heart."
    "Kissing Slavya was... sweet."
    scene bg ext_entrance_night_clear_closed_7dl with dissolve
    show sl2 normal pioneer2
    with dissolve
    sl "Have you thought about performing on the farewell concert?"
    if (alt_day2_date == 'un_fz'):
        me "You know, Miku wrote me down, but somehow I still haven't made anything."
        me "And in the rush of trying to act out something..."
    else:
        me "And I don't have anything to do."
        "I shrugged my shoulders."
    sl "Well, maybe we'll prepare something."
    me "I'm sorry, but not in one day."
    "Slavya bit her lip, clearly a little upset."
    show sl2 sad pioneer2 with dspr
    sl "Eh. I thought maybe you should have done something to be proud of."
    if alt_day4_sl_cl_lf_solo == 1:
        me "Saving Shurik - isn't that an excuse?"
    elif alt_day4_sl_cl_lf_solo == 2:
        me "I made it to the old camp and back with a bad wound! Isn't that something to be proud of?"
    else:
        me "Shurik is saved? {w}There! Doesn't that deserve pride?"
    sl "No."
    "She brushed it off."
    sl "I'm about getting people to talk a little."
    me "Wow! Didn't notice the vanity in you."
    show sl2 smile pioneer2 with dspr
    sl "There isn't any. I want people to talk about you."
    "A girl wants to be proud of her chosen one. {w}How nice."
    me "I'm sorry, I'll have to judge my merits on the invisible front for now."
    sl "Yeah..."
    show sl2 normal pioneer2 with dspr
    sl "Are you even going to the dance?"
    me "You ask! If you're going, so am I."
    "She nodded."
    "We approached the shutters, already locked."
    scene bg ext_entrance_night_clear_closed_7dl with dissolve
    sl "Just a second."
    "A simple semi-circular key she managed to locate in the moonlight in less than a minute."
    "I was sure she would have found it in complete darkness, with her eyes closed, just by touch."
    play sound sfx_unlock_door_campus
    pause(1)
    scene bg ext_entrance_night_clear_7dl with dissolve
    play ambience ambience_camp_entrance_night fadein 3
    me "This isn't the first time you've been trespassing on private property, is it?"
    "I joked."
    show sl2 normal pioneer2 with dspr
    sl "What?"
    me "Nothing."
    "I held up the door for my lady, let her through, went in myself."
    "The camp was finally and irrevocably asleep."
    stop ambience fadeout 6
    scene bg ext_clubs_night with dissolve
    play ambience ambience_camp_center_night fadein 3
    "No strange noises or humming could be heard from the side of the clubs."
    "Slavya closed the lock and nodded."
    show sl2 normal pioneer2 with dspr
    sl "Well, are you going to bed?"
    me "I think I'll walk you to bed, if you don't mind."
    "We were going the same way anyway."
    "She nodded and took my hand."
    show sl2 smile pioneer2 with dspr
    sl "We'll walk with you like adults, hand in hand."
    show dreamgirl_overlay with dspr
    dreamgirl "The main thing is that these 'hand in hand' don't change into their wedding robes too soon."
    th "Do you mind?"
    dreamgirl "Of course I'm against it!"
    dreamgirl "Marriage, man, is an institution invented by impotent men with the faded polygamy of youth."
    dreamgirl "It means no-no to the side and you'll be eating the same cake for the rest of your life."
    th "Like that's something bad."
    dreamgirl "Oh. {w}I didn't like the way that sounded."
    th "What do you mean?"
    "But the inner voice shut up again, leaving more questions than answers."
    "Horny bastard."
    scene bg ext_houses_night_7dl with dissolve
    show sl2 smile2 pioneer2 with dspr
    "Slavya had to go to the right, I had to go straight ahead."
    sl "Well... It's been a very long day."
    "I nodded in agreement."
    sl "And now we're splitting up?"
    "I'd argue with that, but..."
    "I sighed."
    sl "Why are you sighing?"
    if alt_sp >= 4:
        menu:
            "I don't want to!":
                "I said pitifully."
                show sl2 laugh pioneer2 with dspr
                sl "And what do you suggest?"
                "I looked at the bundle in her hands with a hint."
                show sl2 scared pioneer2 with dspr
                sl "What? Don't you dare, think what people will think?!"
                me "They won't think anything new anyway."
                "I took her hand."
                me "I saw a little house in the back of the road..."
                show sl2 tender pioneer2 with dspr
                sl "You've got to be kidding me."
                me "I'm dead serious."
                "She tried to object to something, but I put my finger to her lips:"
                me "Slavya, if you don't want to - say it out loud."
                me "All other objections are dismissed as untenable."
                "She opened her mouth..."
                call alt_day5_sl_cl_hentai
                return
            "Then see you tomorrow?":
                pass
    else:
        me "See you tomorrow?"
    sl "Sweet dreams."
    "She whispered."
    me "Can't I come to you?"
    show sl2 normal pioneer2 with dspr
    sl "No, Semushka."
    "She shook her head regretfully."
    sl "Zhenya's sleeping at home tonight, so no boys allowed."
    "And shattered my dreams."
    me "Sadness."
    "I sighed."
    me "See you tomorrow then?"
    hide sl2 with dissolve
    "Nodding to me, the girl melted into the darkness."
    "And I staggered home."
    "The squad leader is definitely asleep by now; we have to be quiet and sure."
    scene bg ext_house_of_mt_night_without_light with dissolve
    "The lights were already out, both in the windows and in the lantern above the door."
    "Unlike me, the slacker, the squad leader, even lying on her side, has constant responsibility for her frumpkins."
    "If you're thick-skinned enough, it doesn't really matter, but thick-skinned people don't go into counseling - it'd be a lot easier for them to rub their pants in some design bureau with four weeks of vacation a year."
    "I pushed open the door and walked into the cabin."
    play sound sfx_open_dooor_campus_2
    pause(1)
    scene bg int_house_of_mt_night2 with dissolve
    "Olga Dmitrievna wrapped her head in a sheet, apparently in order to combat the itching bloodsuckers above her ear."
    "She didn't react at all to the creaking door, so I decided that I was lucky, undressed, and ducked under the covers."
    mt "Semyon..."
    "She called."
    me "Yes?"
    mt "Where are you coming from so late?"
    me "Uh..."
    mt "Have you been discharged yet?"
    "When we went to the bonfire, she wasn't interested!"
    me "Sort of."
    scene cg d1_end_of_day_7dl with fade
    mt "Ah. Violetta Cernovna told me something about that."
    mt "Discharged?"
    me "Uh-huh."
    mt "I see. Good night then."
    "She turned back against the wall."
    "And I, without opening my eyes, uttered with one lip to the ceiling."
    me "Thank you, Viola."
    "And a minute later I was asleep."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day5_sl_cl_hentai:
    scene black with dissolve
    pause(1)
    play sound sfx_open_door_kick
    scene bg int_extra_house_7dl with flash
    play ambience ambience_int_cabin_night fadein 2
    play music music_list["i_dont_blame_you"] fadein 1
    $ lp_sl += 1
    $ alt_sp += 1
    "We've held back too long, teased each other too long."
    scene
    $ renpy.show("bg int_extra_house_7dl", what = Notch("bg int_extra_house_7dl"))
    with diam
    "Clothes flew to the floor, with barely enough time for us not to tear them apart, but just to unbutton them."
    "The unowned roll turned around in a split second, and we froze, both of us red, not knowing what to do."
    sl "Semyon, do we really have to do this?"
    me "You don't want to?"
    sl "No, but... I don't know what it is or how it is."
    me "And what is there to know, as you said yourself, Nature has already thought of everything for us."
    sl "Oh... Scaaaaaarrrrrrry."
    if persistent.hentai_graphics_7dl:
        scene cg d5_sl_moon_7dl
    else:
        scene black
    with fade2
    "She bit her lip and looked at me pitifully."
    "Naked, frightened. {w}Beautiful."
    sl "There was talk of blood, it would hurt."
    me "Who said?"
    sl "Girl friends."
    "She blushed."
    sl "And in the books."
    me "Let's put your books to the test."
    sl "Scaaaary."
    "She said it again."
    "But she made a move on me."
    me "It'll be okay."
    "I got up from the bed and caught her arms and pulled her toward me."
    me "The main thing is to make it without any fuss or nerves."
    sl "It won't be without nerves, I guess... Ah..."
    "She didn't finish."
    "I really didn't like how cold her skin was, so I tried to warm her up."
    "And I had nothing to warm her with but kisses and my own warmth."
    "Another kiss had already added to the experience for both of us, but it was still exciting, and that only added to the interest."
    "But lips weren't enough, hands weren't enough."
    "I ran my finger down her collarbones, my lips over her breasts, wrapped my palms around her back, and pressed her against me."
    "Nipple hardened on my tongue almost before I warmed it with my breath, and Slavya murmured something from above and pressed me against her."
    "And my warmth wasn't enough already, but she tried for both of them, already hot, fervently breathing, sitting on my lap."
    "Really wanted to control everything, even in a case like this."
    "But what could she do."
    if persistent.hentai_graphics_7dl:
        scene cg d6_sl_hentai_2 with flash
    "A few more minutes later I embraced her and rolled her over, finding myself on top of her, biting her kissed breasts, her burning lips, her oily eyes."
    "I had to fight, of course, before she let me into the holy of holies - though Slavya wasn't shy about her nakedness, she was careful about her most private spot of girlhood and didn't want to let me in for a long time."
    "But I was persuasive and persistent, so her knees relaxed and parted, and I finally managed to taste her."
    scene black with blind_l
    "And a few minutes later I was lifted up with surprising force - and Slavya, already a woman Slavya, cried out more in surprise than in pain as we finally became one..."
    scene
    $ renpy.show("cg d5_sl_bed_7dl", what = Notch("cg d5_sl_bed_7dl"))
    with fade2
    stop music fadeout 3
    sl "And there's so much written and spoken about it?"
    "She looked a little embarrassed, but said so first thing when she finally managed to put the letters into words."
    sl "Now it's going to hurt inside, too."
    me "That bad?"
    "She slapped my forehead."
    sl "Don't be silly."
    sl "It's just more because... I don't know. {w}Because it's you!"
    sl "There's nothing physically... unearthly."
    me "That's what I'm saying..."
    sl "No. With you, I'm willing to try more. But only with you."
    "She blushed, but immediately got over herself - true, now there's nothing to be embarrassed about."
    sl "Or are you done? Will you leave now?"
    "Half-jokingly, she asked."
    me "What do you mean «leave»? The night is still young!"
    "Slavya groaned.."
    $ alt_day5_sl_cl_hentai_done = True
    stop music fadeout 3
    stop ambience fadeout 6
    scene black
    return

label alt_day6_sl_cl_begin_good:
    play music music_7dl["yume_akari"] fadein 3
    scene
    $ renpy.show("cg d5_sl_bed_7dl", what = Dawn("cg d5_sl_bed_7dl"))
    with dissolve
    play ambience ambience_int_cabin_night fadein 2
    "I was awakened by an overwhelming happiness."
    "I glanced at my smartphone, which I don't know how it survived - I only got an hour's sleep, but it seemed like too much."
    "How can you sleep with all this!"
    "Something warm and affectionate moved under my side, and I reached for it."
    sl "Syomushka..."
    "She didn't even seem to wake up."
    "Or?"
    "I let my hands free again - just to make sure that happy people don't wear panties."
    with vpunch
    "Got hit on them again."
    sl "Look, you've been tormenting me all night, that's no good."
    "Slavya chided me in a squeaky voice, without opening her eyes."
    sl "I probably can't even get up."
    sl "No, no, don't you dare. {w}Not that way. No."
    me "Should I stop?"
    "I asked."
    sl "I didn't say that. {w}Just don't be so aggressive, hold yourself back a little."
    me "I'd rather hold you in my hands."
    "I lay on my side with my elbow under my head, watching the perfect skin react to my hot breath."
    sl "Oh, and who knew making love was such hard work."
    "She easily slipped out from under me and turned in my direction, resting her head on my elbow."
    sl "What are you up to? Dying tomorrow?"
    th "No, of course not. Not dying. Something worse."
    "I never told her that..."
    "Though what was before seemed from here to be either a dream or a false memory, as if planted on me in order to explain how I got here in the first place."
    "The intensity of the experience... Incomparable."
    if persistent.hentai_graphics_7dl:
        scene
        $ renpy.show("cg d5_sl_moon_7dl", what = Dawn("cg d5_sl_moon_7dl"))
    else:
        scene black
    show prologue_dream
    with joff_l
    "During one of our times, somewhere in the middle of it, when all that was left of the strength was a memory, an eerie sense of the unreality of existence ran down my spine."
    scene stars
    if persistent.hentai_graphics_7dl:
        $ renpy.show("cg d5_sl_moon_7dl", what = D3_intro("cg d5_sl_moon_7dl"))
    show prologue_dream
    with joff_r
    "It's like I've been lying wrapped up in paper all this time, and it's gotten wet and transparent and very, very fragile."
    "Make an awkward move - you'll burst through, fall through."
    "And where did the strength come from..."
    "The expression «won't have enough breathing before death» has taken on entirely new facets of meaning."
    "Slavya exhaled in amazement, but she didn't try to fight back anymore."
    "I never would have believed it was possible to make love to a girl all night long."
    "Especially if the girl is one in the literal sense of the word."
    scene
    $ renpy.show("cg d5_sl_bed_7dl", what = Dawn("cg d5_sl_bed_7dl"))
    with dissolve
    "Looks like she fell asleep again."
    "I wore her out."
    me "My poor..."
    "I ran my fingers down her collarbone, down her cheek, touched her shoulder with my lips..."
    "In short, by the time she woke up, it was too late to fight back."
    "And then she didn't feel like it."
    scene
    $ renpy.show("bg int_extra_house_day_7dl", what = Dawn("bg int_extra_house_day_7dl"))
    show sl2 serious body close
    with dissolve
    sl "Villain-rapist!"
    "Grumbled Slavya, melancholically trying to locate completely inappropriate articles of clothing like panties."
    "Of course, not finding them - I hid them."
    show sl2 normal body close with dspr
    sl "It's not safe to sleep next to you, you know."
    sl "Waking up in the middle of the process, where does that fit in?"
    me "Like that's something bad."
    "I reached for her again, feeling all seventeen I looked."
    "But the love fever had already let go of both of us a little - Violetta didn't lie much yesterday when she said that carnal needs were a transient thing."
    show sl2 smile body close with dspr
    "So I got hit on the hands again, unfortunate panties were taken from me and hastily put on." with vpunch
    "A serious handicap, who'd argue."
    "Armor on the plus-something-something to resilience against the Semens."
    show sl2 sad body close with dspr
    sl "Why are you smiling like a happy crocodile? {w}Why don't you smile like a white man, table, champagne, candles, moon, eh?"
    sl "A girl's first time is important, memorable for life, rrromance, feelings, eh?"
    "Slavya grumbled and grumbled, and it made me laugh more and more - so much she was unlike the perfect and infallible Slavya the world knew."
    show sl2 serious body close with dspr
    sl "What did we do, I'm asking you?"
    sl "Went for a swim, and on an unmade bed... {w}Now you're smiling again, you seduced a girl and you're smiling."
    me "We shouldn't have?"
    "I answered."
    show sl2 normal body close with dspr
    sl "I don't even know now. {w}Although it's probably too late to win back..."
    "As far as I remembered, in my world the surgeons could pretty much play it all back, I guess they can in this one, too."
    show sl2 surprise body close with dspr
    sl "What time is it?"
    "I looked at my watch."
    me "It's early eighth."
    show sl2 scared body close with dspr
    sl "And we're lying down?!"
    hide sl2 with dissolve
    "Slavya jumped out of bed and turned into a tornado gathering clothes, rushing around the room."
    sl "Okay, we still have ten minutes to pretend nothing happened here, you slept in the infirmary and I was just running late."
    me "Do you have to?"
    "I asked lazily, watching the girl scurrying back and forth."
    "Sometimes there were such tempting angles..."
    "But I'm dried up, dried out, and it would be nice to go to bed."
    play sound sfx_7dl["blanket"] fadein 0
    "But the angry activist threw clothes at me."
    "She herself was already fully dressed by this point, and had even obtained a tie from some unknown source."
    "She sat down on the edge of the bed and, gazing into my eyes, kissed me firmly, with a pull back."
    "And then she groaned and pulled away."
    show sl normal pioneer with dspr
    sl "Ooh, it hurts so bad down there."
    "She complained, stroking her lower abdomen."
    me "Is it something serious?"
    "Alarmed me, hopping on one leg and trying to get my foot in my pant leg."
    show sl laugh pioneer with dspr
    sl "Nothing, except that I was tormented all night!"
    "Slavya laughed, came over and helped me get into my shorts."
    sl "I'm going for a swim now, and I had the pills somewhere."
    "After casting a parting glance at the slightly shabby decoration of the cabin - whether we had forgotten anything - we went outside."
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg ext_houses_sunset with dissolve
    play ambience ambience_camp_center_evening fadein 3
    "And slammed the door behind ourselves."
    me "Are you seriously going swimming now?!"
    "I wasn't hiding my horror."
    show sl normal pioneer with dspr
    sl "To tell you the truth, I'd rather go to the bathhouse, but - you know, no one will heat it up for me this early in the morning."
    me "But the water in the river is freezing!"
    sl "So what? I can't go around dirty now!"
    "Slavya didn't seem to understand how it was possible to walk in this condition."
    sl "You could use one, too, by the way..."
    me "No way!"
    me "I'll do it on the sinks sometime, by myself."
    show sl laugh pioneer with dspr
    sl "Okay."
    sl "Then at the bulletin board in twenty minutes, okay?"
    "After waving to me, she ran off to her cabin."
    hide sl with easeoutleft
    "And I staggered to the washbasins, wondering in the meantime what to say to Olga Dmitrievna in answer to her tricky question about where I was and what I was doing there."
    "The option of the truth was not even considered."
    "Because in that case the counselor would most likely have hung me from the nearest aspen tree."
    "Having come up with nothing, I left things to chance, especially since the task at hand was far more pressing."
    "Objective: survive washing up."
    scene
    $ renpy.show("bg ext_stand3_7dl", what = Dawn("bg ext_stand3_7dl"))
    with dissolve
    "And another twenty minutes later, as we approached the booth almost in sync, we found two pieces of paper on the bulletin board."
    "On the first was an order announcing a commendation to doctor gonoris causa psychology V.C. Collider for the lecture and expressed the hope of continued cooperation in this regard."
    me "Look at these rascals going."
    "I nodded at the order."
    me "They've found someone to dump inconvenient discussions on."
    scene
    $ renpy.show("bg ext_stand3_7dl", at_list = [zenterleft], what = Dawn("bg ext_stand3_7dl"))
    show sl normal pioneer at cleft
    with dissolve
    sl "Well... I think it's really better to have someone with an education doing it there."
    "Slavya said thoughtfully."
    "I didn't have time to look at the second order."
    sl "Look, just don't turn around sharply."
    "Slavya pulled my left arm."
    "Lena was tiptoeing past the cabins, holding sandals and socks in her right hand and some kind of bag with an embroidered owl in her left."
    me "What is she doing?"
    sl "Tradition."
    "Slavya said serenely."
    sl "No matter how many times she comes here, every year she escapes for a day before she leaves."
    me "And you're so calm about it?!"
    show sl smile2 pioneer with dspr
    sl "And what should I do?"
    me "I don't know... Stop her somehow!"
    show sl happy pioneer with dspr
    sl "Semyon, I'm sorry, but you don't know anything at all about Lena or her life."
    sl "She can stand up for herself just as well as you can, if anything. {w}I'd be more worried if Alisa ran away - that one is just very helpless."
    with fade
    "At this early hour it was just the three of us outside."
    "Even the counselor wasn't up yet."
    "And the orders were already hanging."
    "And Lena was already sneaking off somewhere."
    show sl normal pioneer with dspr
    sl "I'm standing here thinking - what a lot to look forward to today!"
    "She stretched sweetly, all in anticipation."
    "A nightmare girl who gets excited about loads. {w} A workaholic."
    "Without ever noticing us, Lena disappeared in the direction of the beach."
    "And Slavya touched my shoulder."
    show sl smile pioneer with dspr
    sl "Listen, I'm going to change now, and I'm going for a walk... A jog. {w}Are you with me?"
    "I suppressed a yawn - I didn't sleep at all."
    me "What did you call me... Syomushka? {w}Yeah."
    me "So..."
    me "My sweet Slaaaavushka. Tell me a secret."
    show sl surprise pioneer close with dissolve
    me "Don't you have anything after tonight, no consequences?"
    show sl laugh pioneer close with dspr
    sl "My hands are shaking too, my feet are shaking."
    "She laughed."
    sl "But it's a good tiredness, it'll turn into new strength if you stretch out properly!"
    sl "So come on, don't be lazy!"
    "And she dragged me toward her cabin with relentless force."
    "I guess her pills weren't exactly painkillers."
    scene
    $ renpy.show("bg ext_house_of_sl_day", what = Dawn("bg ext_house_of_sl_day"))
    with slideawayleft
    play ambience ambience_camp_center_day fadein 3
    "Or maybe it's just that after an explosive discharge like that, where I personally wasted all my energy, Slavya, on the other hand, has only gained more energy!"
    "Damn energy vampire!"
    stop music fadeout 3
    scene bg ext_square_sunset at zenterleft
    show blackout_exh2
    show sl smile sport at cleft with moveinleft
    with dissolve
    sl "Well, you can do it!"
    "Shouted Slavya half an hour later, as I plopped down on the steps of Genda's pedestal, greedily gulping air with my mouth and alternately spitting slurping saliva."
    sl "The main thing is not to be sour!"
    "She didn't stop and continued running in place."
    me "Uh-huh."
    "I exhaled, barely catching my breath."
    me "For a day or two, except... 'sport' is an obscene word to me!"
    me "What are you acting so funny, anyway?"
    hide blackout_exh2
    show blackout_exh3
    with dissolve
    sl "It's the last day! {w}What I didn't do all shift, I've gotta do!"
    "She was irresistible in her tight uniform with white stripes at the seams, a move that Adidas would license in a few years for its sportswear."
    "She squinted smilingly at the rising sun and was enjoying life to the fullest."
    sl "And, of course, get in a good mood!"
    play music sfx_7dl["wakeup_horn"] fadein 3
    "A cough-like sound came from the loudspeakers, and the horns blared into the scarlet-transparent morning."
    sl "You're only pretending to be annoyed, but in fact you're enjoying it all, come on, admit it!"
    "She jumped around me, jamming, urging me to wake up finally."
    stop music fadeout 3
    "The camp was waking up."
    play music music_list["my_daily_life"] fadein 5
    sl "Wake up, wake up! We'll beat up whoever sleeps!"
    me "Slavvvvvyaaaaaaaa!"
    "I was squirming and pressing my elbows to my sides, trying to hide from the tickling."
    "Yeah, of course."
    "This girl studied anatomy very well."
    me "Why are you teasing me, I was doing so well..."
    show sl laugh sport with dspr
    sl "Slept with your eyes open!"
    sl "Come on, we've got half an hour, I'll introduce you to someone."
    me "Whoa. {w}Who is it, I wonder?"
    th "Is there someone in camp so interesting that Slavya is willing to give him her undivided attention as well?"
    dreamgirl "Actually, she gives her time to the whole camp, in case you haven't noticed."
    th "Good morning to you, too, gloomy nerd."
    "My inner voice always woke up late."
    "But once he opened his mouth, it was hard to shut him up."
    scene bg ext_dining_hall_away_sunset at zenterleft
    show sl smile sport at cleft with moveinleft
    with dissolve
    sl "Be quiet here, so no one notices."
    "She turned and, taking a hard right, set off toward the far outbuildings of the canteen."
    "I don't know what Slavya was afraid of - the whole pioneer world now narrowed down to a pillow taken away, and the sharpest ones to a washbasin with ice water."
    "But I was silent, dutifully halting where the girl was halting, following her footsteps."
    sl "I see you have become friends with Boris Alexandrovich."
    "Suddenly she noted, staring intensely into the empty space of the courtyard."
    if ('sport_area' in list_voyage_7dl):
        sl "Your first meeting wasn't very good, though."
    me "He offered me the position of assistant gym teacher for the next shift."
    show sl happy sport with dissolve
    sl "Oh, that's what it is. {w}And you were appreciated! Too bad it's too late."
    me "What do you mean?"
    show sl normal sport with dspr
    sl "He's leaving after this summer."
    me "No way!"
    sl "His last summer as a teacher."
    sl "For health reasons."
    "Slavya said authoritatively, and I realized that it wasn't a rumor, it was the most verified information."
    sl "He's already paid off at school, he'll be here till the end of summer - and then he'll be sent off."
    sl "They'll send a young yesterday's graduate to replace him here and to a place in our school."
    me "What's with him?"
    show sl angry sport with dspr
    sl "Semyon, do you even think about what you're asking?"
    me "What?"
    sl "Do you think it's any of our business what disease causes a person to leave teaching and sports?"
    "She bit her lip, threw another glance at the yard, and waved her hand."
    scene bg ext_warehouse2_day_7dl with dissolve
    "We quickly crossed the space, stopping at the double doors of the dry warehouse."
    stop ambience fadeout 4
    stop sound_loop
    play sound sfx_open_door_strong
    pause(1)
    scene bg int_attic2_day_7dl with dissolve
    play ambience ambience_medstation_inside_day fadein 3
    "And in a second we were already indoors."
    "Slavya immediately went somewhere deep into the half-darkened room, leaving me my right to follow Mistress."
    sl "Uncle Borya is the last mastodon, he still caught the move from the old site, the one where the counselor... {w}Well..."
    sl "Even the director works here less than he does."
    "She rustled something, and there was a strange sound."
    th "Was it just me or did I hear something?"
    "No. Definitely."
    sl "Here, Semyon, I want you to meet him."
    play music music_7dl["wheres_wonderland"] fadein 3
    "Said Slavya, turning toward me, and in the dim light streaming through the gaps between the boards, I could see her clutching something snow-white to her chest."
    "Tiny, with a black button nose."
    "Desperately pounding its tail."
    show sl smile sport with dissolve
    sl "Pirate."
    "More like a bear than anything else."
    "And Slavya had such a strained voice."
    scene cg d6_sl_puppy_7dl
    with dissolve
    "She set the puppy on the ground, and it waddled awkwardly, shuffling its paws toward me."
    "Arctic Spitz, a Sami husky - in my town they called them samoyeds and said no, they don't eat themselves."
    "I held out my hand to him and shivered when a wet nose was first poked into my palm and then politely licked."
    me "Hello, pup."
    "I rubbed Pirate's head."
    me "How are you doing? {w}Why Pirate?"
    scene bg int_attic2_day_7dl
    show sl laugh sport
    with dissolve
    sl "Because he's a thug!"
    "The girl giggled."
    sl "When you first arrived and I had to show you around camp, he got my uniform dirty and there was nothing in my size to replace it, so I had to change into my gym clothes."
    if alt_day_binder != 1:
        me "You mean when Electronik and I came to visit you at the linen warehouse..."
        "She nodded."
        sl "Very good timing, yes. {w}I came to get my uniform, and you..."
        me "But then what about what you said about being put on the payroll and all that."
        show sl shy sport with dspr
        sl "All of that happened...{w} But a little later."
        "The serenity of her smile would have been the envy of Buddha."
        sl "I lied a bit about the chronology, that's all right!"
    else:
        me "So I wasn't imagining it at the time, that outlaw was really speaking!"
        sl "Yes. {w}But you're the first one to hear anything at all - I used to get everything in time, and he slept most of the time."
        sl "He's just a baby."
    me "But isn't it against the law to keep a dog on camp property?"
    show sl normal sport with dspr
    sl "Actually, it's forbidden, of course."
    sl "But I sheltered him, he was left over from the last shift, the kid's parents brought him back to show him and make him happy, and he turned out to be terribly allergic."
    me "What if I had terrible allergies, too?"
    show sl laugh sport with dspr
    sl "You would have known about it for sure! {w}So you were just surprised to see an animal in my arms."
    show sl normal sport with dspr
    sl "Well, do you like him?"
    me "Not as much as you do, of course, but..."
    "Mindful of what she'd said about uniform getting dirty, I didn't cradle the Pirate in my arms, but simply held him out to Slavya when I caught him."
    "After all, he fit just right in my two palms."
    sl "Flatterer!"
    with fade
    sl "Behave yourself!"
    "Strictly she chastised the puppy, putting him back in the box."
    sl "If you behave, I'll bring you something good to eat. {w}All right?"
    voice "Boof."
    "The puppy replied and turned and yawned as we tired him out."
    sl "Fine, then. Don't get bored."
    "Slavya covered the box with a lid with ventilation holes and turned to me."
    sl "Come on, we've got exercise and a lineup waiting for us!"
    me "I hate the schedule."
    "I muttered, fitting in at the keel and switching to a run as well."
    "Looks like it's going to be a fun day today."
    hide sl with dissolve
    stop music fadeout 3
    stop ambience fadeout 6
    return

label alt_day6_sl_cl_begin_neu:
    scene bg int_mine
    show prologue_dream
    with dissolve
    play music music_7dl["nowyouseeme"] fadein 3
    "I was being driven by that strange feeling again."
    "I would call it something akin to a sense of balance - one that something in the brain is responsible for. {w}The middle ear, I think?"
    "Unless you've been disoriented by a hit or a throw, you always know where your top is and where your bottom is."
    "Sort of a sense of gravity, a sixth organ of perception of reality."
    "So here too, I knew exactly where to go to get where I wanted to go."
    "I guess after yesterday's hike, on adrenaline, I remembered everything here in such a way that it's not hard for me to reproduce a detailed map of the area in my brain."
    "Though something in my head kept telling me that all the adrenaline we had for two of us with Slavya wouldn't be enough to know where which turn led."
    "We, on the other hand, only made it as far as the 'living' room, and then, with a run into the center, we ran back to the exit."
    scene bg int_mine_crossroad
    show prologue_dream
    with dissolve
    "I can't even remember which corner we turned where."
    "I guess Slavya could, though."
    "I remember her correcting me when I needed to turn."
    if alt_day4_sl_cl_lf_solo == 1:
        "And she had sketches of the site plan, too."
    "But why am I dreaming about this place?"
    "What did I see here yesterday that made it appear to me in my dream?"
    "Was it running from harmless snarks?"
    "Or the flooded tunnels?"
    "There was nothing of interest in the center, just a mined out vein, no longer of interest."
    me "Then why am I here?"
    "Hardly to look at an empty cave."
    scene bg int_mine_coalface
    show prologue_dream
    with dissolve
    scene bg int_mine_coalface behind prologue_dream:
        xalign .5 yalign .4 zoom 1.0
        linear .3 xalign .5 yalign .4 zoom 1.1
    "I took a step."
    scene bg int_mine_coalface behind prologue_dream:
        xalign .5 yalign .4 zoom 1.1
        linear .3 xalign .5 yalign .35 zoom 1.2
    "Another one."
    return

label alt_day6_sl_cl_begin_cave:
    call alt_day6_sl_cl_begin_neu
    scene bg int_mine_heart_7dl:
        xalign .5 yalign .4 zoom 1.2
    with flash
    play music music_7dl["dead_silence"] fadein 3
    "And I realized it wasn't a goddamned dream!"
    "I was standing in yesterday's cave, at the very edge where the ordinary coal rock changes into outlandish white-green crystals that glow faintly in the dark."
    "It suddenly occurred to me that until this moment I had no recollection that there were any crystal caves here at all."
    "It was like being cut off for good."
    "And a little farther away, in the coal darkness of the manhole between the dragon's fangs, yesterday's acquaintance was already pouring with density."
    show myst_mh with dissolve2
    "It reeked of the dankness of the marshes of the Slavya's village, the gasoline breath of my native Petersburg, the hot kisses of the local sun."
    "It beckoned and beckoned to come up and just know - what it was."
    "How it got here."
    "And most importantly, why is no one still aware that this stuff is here?"
    th "Or is everyone aware, but «authorities are hiding»?"
    "I froze at the very edge."
    "Another memory - that super-technological security system."
    scene bg int_mine_water_7dl with slideawayleft
    "Turning on the spot, I ran."
    "And I ran as if a horde of xenomorphs were chasing me, just waiting to get their hands on my trophy skull."
    scene bg int_mine_crossroad
    "I was constantly afraid of bumping into something, of tripping, but the fear drove me on and on."
    "And the terrain seemed very familiar to my body for some reason."
    "I mean, I ran here yesterday, but it felt like our acquaintance lasted a lot longer - I knew where to step up, where to hold back, turn around, crouch down."
    scene bg int_mine_room
    with dissolve
    "The soft paws of the local exotic inhabitants stomped nearby, running at the sound with me in a race, but I didn't pay much attention to them."
    "Now that I knew they were harmless, I could wrestle with my other fears."
    "And it wasn't until now that I noticed that I could see pretty well."
    "And it wasn't that I had a change in the balance of the wand-vials in my eye at all."
    "I looked at my left hand like it was a dangerous, poisonous animal."
    "In it was clutched a kerosene lamp with a dancing light, with a beautiful, shaped glass lampshade..."
    scene
    $ renpy.show("bg int_mine_room", what = Noir("bg int_mine_room"))
    with dissolve
    "Acting deliberately measured, I screwed on the wick and set the kerosene on the ground, under the pipe, where no one could accidentally knock it over."
    "Overcame the trembling in my hands."
    scene bg int_hence_day_7dl
    stop music fadeout 3
    "And only after that did I allow myself to take up the braces."
    "They were already stained with something, earth, sand - it looked like someone had been down here not so long ago."
    "And that «someone» — was me."
    play sound sfx_open_metal_hatch
    pause(1)
    scene bg ext_square_sunset with flash
    play ambience ambience_camp_center_evening fadein 3
    "And... I fell out right behind the podium and froze."
    "The sleepy pioneers were marching for breakfast."
    "A perfect chance to blend in!"
    "After waiting a few minutes, I joined at the tail of the column."
    "And, as if sensing my presence, Slavya immediately stepped out of the line and, spreading her legs, looked over the ranks in this way."
    "Of course, the big-headed fool, trying to hide among the little ones of ten years old, was immediately detected by her."
    sl "Semyon."
    "She beckoned with her finger."
    "And I went to her."
    "What else could I do?"
    scene bg ext_square_sunset at zenterleft
    show sl smile pioneer at cleft
    with dissolve
    sl "Hey, Semyon, where have you been since this morning?"
    "The girl smiled at me with a friendly smile."
    sl "Decent guys don't make their girlfriend worry, you know!"
    me "If it were up to me..."
    show sl normal pioneer with dspr
    sl "Is something wrong?"
    "Her smile faded."
    me "It's not that... {w}You see, I woke up in the tunnels today."
    show sl surprise pioneer with dspr
    "Slavya immediately grabbed me under the arm and pulled me aside so no one could hear."
    sl "No way! {w}I checked myself yesterday to make sure the lock was closed."
    me "It was open. And I was standing there."
    show sl scared pioneer with dspr
    sl "In the middle?"
    me "At the very edge, just woke up, and I'm already there."
    show sl serious pioneer with dspr
    sl "Come on, let's go."
    "She crossed the square at a brisk pace, and turned just beyond the podiums, toward the air grid."
    "Nothing has changed here since the moment I left here - the loose ribbed surface, the lock that someone unlocked, lying next to it."
    "Or rather..."
    sl "Wow."
    "She tried to lift the lock, but it fell apart in her hands, leaving only the shackle in her fingers."
    sl "It looks like the lock had crumbled from old age."
    "The girl looked very puzzled."
    me "Or someone had sprayed it with one extremely corrosive substance."
    "There were already too many blank spots in the case to let any mysticism get in the way."
    show sl sad pioneer with dspr
    sl "And it was..."
    "I shook my head."
    me "No, I would have remembered. {w}And all I remember is saying goodnight to the squad leader before I went to sleep, and opening my eyes already there."
    sl "And how did you get out without a flashlight?"
    me "You won't believe it, but you can still find some pretty good kerosene burners down there - they didn't get electricity up here right away."
    sl "Damn... {w}Keep a lookout here so no one comes in, and I'll run down and get the lock and lock it properly."
    me "But what about..."
    show sl laugh pioneer with dspr
    sl "Semyon, can you think of anything but your belly?"
    hide sl with easeoutleft
    th "Sometimes I want to satisfy my hunger in other ways, too."
    "I thought, glancing at the tight shirt - Viola wasn't lying, the first day we met, the uniform sat noticeably looser on Slavya, and it wasn't about the extra pounds."
    "But on the whole - it's morning!{w} How do they say, eat your own breakfast? Now where's my breakfast?"
    "Nowhere!"
    scene bg ext_square_sunset at zenterright
    show mt normal pioneer at cright
    with dissolve
    mt "Semyon, you're up early today, were you in such a hurry to accomplish the task I gave you?"
    "Not that..."
    me "Yes! {w} And I also decided that I will now run in the mornings with Slavya."
    show mt laugh pioneer with dspr
    mt "Well, well, let's see how long you last."
    "She took a step, but, apparently remembering something, she frowned:"
    show mt normal pioneer with dspr
    mt "Semyon, can you tell me where you were at the lineup?"
    sl "He was running one of my errands related to your assignment."
    "Clear and to the point, Slavya reported, floating into the frame."
    scene bg ext_square_sunset at zenterleft
    show mt normal pioneer at right with moveinright
    show sl normal pioneer at cleft
    with dissolve
    sl "Don't scold him, please, we thought we'd make it before the lineup!"
    show mt smile pioneer with dspr
    mt "Okay, an errand is an errand. {w}What were you doing?"
    hide mt with moveoutleft
    "The squad leader snorted, took one more look at my face, and, without waiting for an answer, went on her way."
    "Meanwhile, it's almost the end breakfast time!"
    me "Slavya, just hurry up, we're late!"
    "I pressed the grate with my shoulder, allowing Slavya to put the lock in the bars and slam it shut."
    "Hooray! Mission accomplished, enemy defeated, quest closed!"
    me "Now to the canteen?"
    show sl laugh pioneer with dspr
    sl "Rejoice! Yes!"
    hide sl with dissolve
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_sl_cl_begin_techno:
    call alt_day6_sl_cl_begin_neu
    $ persistent.sprite_time = "prolog"
    $ prolog_time()
    scene
    $ renpy.show("bg ext_square_day", what = Dawn("bg ext_square_day"))
    show prologue_dream
    with dissolve
    "I rolled over on the other side, and the dream was replaced by another."
    play ambience ambience_camp_center_day fadein 3
    play music music_7dl["sh_ai_rejuv"] fadein 3
    "I dreamed of a sunny, summer day."
    "Blue, clean, clear."
    "There wasn't a cloud overhead - and thank goodness we're not in some Nizhny Novgorod region, where if they have clouds over Moscow, all the bad weather goes right into that fierce parish."
    "But there was not a single living soul to be seen among the cottages - either everyone had hidden away in the cottages, or there was simply no one there."
    "Only the tinny loudspeakers screamed in the voice of a little-known bard with Korean roots:"
    "I-a wait for an answer... No more hope... Soon the summer will be over..."
    "And it occurred to me that Victor was still alive, and we could go to bloody Riga, to warn him, to tell him."
    "But the flags are down, the seal of grief is on my foreheads, and I'm alone with the knowledge that they won't let me out of here."
    "In order for me to get here, three have died and one has gone mad, taking the main theta charge."
    "So I'm here for a reason."
    "Then what's alive if the tragedy happened fifty years ago?"
    "A copy of Genda's letter of condolence was already hanging on the bulletin board, some joker had mirrored it vertically, making the president's noble forehead look like a bicycle."
    "At the pedestal itself, beveled by the queue, the technicians who had come on call, to set up a potentially indestructible system, lay in shredded dolls."
    th "This is how it starts."
    th "That's how it goes."
    th "First we allow psi-suggestors to be installed in children's camps, then we put them everywhere and infringe on the one inalienable freedom of man - the right to be."
    "And all that other stuff."
    "I headed resolutely toward the old administration building."
    scene bg ext_admins_day_7dl
    show prologue_dream
    with dissolve
    "An invisible disc jockey launched Marilyn Manson, who promised me someone listening to my prayers."
    am "Thanks, uh-huh."
    voice "Are you okay?"
    "A concerned voice came from the earpiece."
    th "Wow, at least something in this thing functions humanly."
    "I was flaccidly surprised."
    voice "Hang on a few more minutes, transport's on the way: three hundred kilometers, thirty to forty minutes, you know."
    "Sure, half an hour is half an hour."
    voice "Listen carefully."
    voice "I'll tell you a word after which you'll do everything right."
    am "Did they put an algorithm on me, too?"
    "The chuckle came off my lips all by itself."
    voice "No. {w}This word is duty."
    "Duty? That's absolute dogshit."
    "It's good to yell about duty when you're wearing a tight tunic and speakers or vinyl and a marpat, and all your feats only happen in bed."
    "But if you've got a few more holes in you than nature intended, you don't have much time for duty."
    "All that's left is a weary determination to prove something to someone and not die ignominiously here, five minutes away from completing the task."
    "To prove to someone... That it was not for nothing that those who went on the mission went to ground along the way, leaving me proudly alone."
    "That not for nothing..."
    "But there's no way in hell I can even move the goddamn landmine I'm supposed to use without the servos."
    "And I have no power, no strength, no life..."
    voice "What have you got there?"
    "I stood in the doorway of the office of the warden of the former camp, the former temple, the former cathouse, the former, the former - on this door only the design had changed, but the surname had remained the same for more than five hundred years."
    "The surname of the man who so diligently guarded the terrible secret of this place that he unwillingly brought it to the attention of the powers that be."
    "And special forces were brought into the Russian Federation."
    "Scorched, dead earth."
    "Wildly lived a shitload of years as a secret keeper."
    "And nine grams of lead that were delivered to the soft tissue and splattered the cheerful lilac wallpaper with the grayish contents of his skull box."
    "There was never any logic in the actions of those who held the defenses here."
    "Nor was there any logic in the actions of those trying to seize this piece of territory."
    "They all didn't understand one simple thing."
    "The natural psi generator couldn't be used as a weapon or a means of control."
    "Trying to use it in any way would be akin to trying to make yourself a cudgel out of a uranium rod - heavy, no doubt, it breaks heads beautifully."
    "But it also hurts its owner far more - at least the unfortunate victims of mechanical trauma don't have to suffer from radiation sickness and metastases."
    "You can't dig it out or transport it in any way, put it on a mobile platform, and so on."
    "It doesn't work that way."
    am "I'm going to complete the task."
    "I squeaked into the tendril of the microphone, not recognizing my own voice."
    "Ripped the headset off my ear and threw it away."
    "I had a job waiting for me."
    "It didn't work last time, it won't work this time."
    "Who knows when promised that your whole life must flash before your eyes if you found yourself on the doorstep of oblivion."
    "Who said that nonsense?"
    "What proof has he got?"
    "I smoked - the last one, how symbolic."
    stop music
    play music music_list["orchid"] fadein 3
    scene bg ext_square_day
    show prologue_dream
    with blind_d
    "Actually, where did all this idiocy about a lifetime in front of my eyes come from?"
    "Did somebody fucking come back from the other side of the world to tell me about the unearthly sensations during {i}the transition{/i}?"
    "But at least I had my own substitute for those sensations."
    "Especially since the end really wasn't that far off - the painkillers barely worked, I had to stop and wait out the flashes of pain every minute."
    play sound sfx_open_metal_hatch
    pause(1)
    scene bg int_hence_day_7dl
    show prologue_dream
    with flash_red
    "Our inseparable trio - Blind Man, Witch, Rogue. Smiling for the camera, young, white-toothed, happy."
    "Rogue was buried by an enemy commando she'd had a melee with for some reason, I chased the Witch away myself, thinking the self-destruct mechanism would work properly."
    "And Blind crawled down the stairs, bleeding from wounds that had already opened for who knows how many times."
    "{i}The graduates were given their diplomas - me, in my tactical-option uniform, Slavya in her reconnaissance gray-green combo with blue buttonholes, Aliska - well, I think she only joined the Special Forces because of their black and red dress uniform.{/i}"
    "{i}Slavyana is dancing on the roof of my humvee, disheveled, not very hard anymore - her pride, her long braids, are short - pathetic, but what can you do.{/i}"
    "{i}You're supposed to fully shave to fit into the psi-protection, the half-unbuttoned jumpsuit allows you to appreciate the black lace of the bust - and yes, of course, she doesn't usually wear that.{/i}"
    "{i}Close-ups of two rings sealed in amber with a white gold band running lengthwise, one larger, one smaller - we are not allowed to wear metal jewelry.{/i}"
    "{i}The tar cube is held in the palm of Alisa's hand, she has just returned from her first assignment, and we told her everything from the spot.{/i}"
    "{i}You should have seen the look on her face - I wish I had taken pictures.{/i}"
    "{i}A frowning Lena with a guitar parodies Vysotsky, pulling consonants - I do not know how she did it.{/i}"
    "{i}Ulyana smiles from the driver's seat - she's our wheels today.{/i}"
    "A few faces out of focus."
    "It's so weird, meaningfully bitter to realize that all of our photos together are constantly out of focus, add a few more faces and it's a normal photo, but just the two of us - you're being naughty, brother."
    "{i}Ulyanka and Lena are playing Galaga, using the huge blank wall of the hangar as a screen.{/i}"
    "{i}Slavyana, laughing, jumps on one leg on a tube three centimeters in diameter, usually used as a horizontal bar.{/i}"
    "{i}And she's standing on it. And hopping on one leg. Damn witch.{/i}"
    "We were separated after the contracts were signed, but immediately after training we were reunited as one unit - here's the card from the reunion of the Dream-Team."
    "{i}Violetta Cernovna, staff psychiatrist and theta therapist, unloading Slavya's head after reconnaissance raids, a smoking cigarillo in her left hand, a bundle of EEG suction cups in her right. On the table are her fetish gloves, her face tired and somehow calm, or so.{/i}"
    "{i}Slavya on Palace Square, holding a slightly soiled blue plush bear - not a single photo shows her holding a gun, although she has always been an excellent marksman.{/i}"
    "{i}Here we are racing through a holographic obstacle course, freeze frame, filmed by Alisa.{/i}"
    "{i}Slavya in a lightweight suit, I'm in a heavy suit as a loser.{/i}"
    "{i}I was halfway around her, and, turning around, I took her on my chest, hugged her, lifted her up, pulling her legs off the ground, and she was laughing, her eyes happy and bottomless. Alisa took the picture at the finish line.{/i}"
    "The decision was hard."
    "It's unbearably hard."
    "You can't close your eyes, shove responsibility onto someone else, or hide in a hole."
    scene bg int_mine_room
    show prologue_dream
    with dissolve
    "Because a new squad will be sent to replace the failed mission."
    "And another."
    "Until, like in Normandy, they pile everything in three rows of corpses and fill it with soldiers' blood so that it flows in rivers."
    "Not a price I was willing to pay."
    "And it wasn't about stupid duty either."
    "It's just that I grew up here. And so did my girls. {w}We had a fleeting chance, but everyone else will have an even smaller one."
    "It took some agonizing before the rest of the life support energy went into the servos in my right hand and allowed me to turn a few valves."
    "I won't even go into the tunnels themselves."
    "The number of robotsenshinels per square meter was off the charts here - we lost Lena when she went out to cyber-scout the area and looked out of the corner unluckily."
    "The laser beams sliced her with a straw before I could say 'Mommy.'"
    "So my bet is on stealth."
    "Yeah, and on the surprise that Sanich's mentor left behind."
    "I slammed my fist into the flat disc and threw it into the ground."
    "The crafty machine spun, rustled and gnawed into the soil, instantly disappearing."
    "All that was left was to wait."
    "And hope that my foolish calculation will come true."
    "In the augmented reality glasses, a picture of plowed soil flickered at the edge of my vision, transmitted directly from the 'mole'."
    "I have no idea why I brought it with me."
    "But now sitting in darkness, only disturbed by a tiny screen and scarlet flashes of pain, was all I had."
    "And when even from my seat I could already hear the smell of gas, I steered the mole toward the surface."
    "I didn't have any explosive devices; I couldn't even get a spark."
    "But it turned out just as I had planned - the scarlet, infinitely even glow of the laser beam came into the frame, the picture was gone."
    "And a few seconds later, the screen showed an inscription «signal lost» on top of the white noise."
    "The infernal device reacted as it should."
    "The concentration of gas in the tunnels reached the right point, the spark went off."
    "A roaring explosion swept through the tunnels, stopping somewhere at the joints of the drifts to pull the carriers out with the roots, dropping a couple million tons of soil on the tunnel floor..."
    "I exhaled and opened my eyes toward the approaching scarlet haze."
    "And..."
    stop music fadeout 3
    play ambience ambience_camp_center_day fadein 3
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    scene bg ext_admins_day_7dl with dissolve
    "I opened my eyes near the administration building."
    "Haydn was blaring overhead from the loudspeaker, no Tsoi, of course."
    th "How did I get here?"
    "I wondered faintly."
    dreamgirl "Are you awake at last?"
    "Inner voice grumpily inquired."
    th "Have I been sleepwalking?"
    "Honestly, I always thought stories about people sleepwalking were bullshit."
    "But now..."
    dreamgirl "You could say that."
    dreamgirl "For some reason you went back into the tunnels. {w}Didn't get enough exercise yet, diabla?"
    th "And then what?"
    dreamgirl "Nothing, I had to take you here and put you on a bench."
    "After digging around in my head, an inner voice gave me a verdict."
    dreamgirl "Your dream is not a subconscious joke, if anything. {w}It's very much like an outside tip-off."
    th "Pardon?"
    dreamgirl "It feels like it was simply put in your head. {w}Similar to yesterday's, by the way."
    "Other people's dreams didn't bother me as much as the fact that I managed to get up and get dressed in my sleep and go to no one knows where."
    "The only thing that bothered me so much was the fact that I sometimes babbled in my sleep - praise be to Random, I sleep alone now, and no one cares about my nocturnal revelations."
    "It's always scary to lose control of your own body or mind."
    play sound sfx_stomach_growl fadein 0
    "But I should have taken care of the business at hand as well."
    "I glanced at the clock - eleven o'clock."
    "I think I've hopelessly overslept breakfast."
    "But maybe I can intercept Slavya and get something to eat from her?"
    $renpy.notify('If you ever played WC3 - just remember how ghouls sound')
    "We're kind of a couple now, what if she has something for her young man... something like, fooooood?"
    "I got a good look at her on the way up - she was hurtling along, and her face was confused and a little scared."
    scene
    $ renpy.show("bg ext_admins_day_7dl", at_list = [zenterleft], what = Dawn("bg ext_admins_day_7dl"))
    show sl scared pioneer at cleft with easeinleft
    with dissolve
    me "Slavya!"
    play music music_list["take_me_beautifully"] fadein 3
    "I pulled myself up and waved to her."
    show sl angry pioneer with dspr
    "When she saw me, she nodded and ran toward me."
    sl "Semyon! {w}Phhheeeeww..."
    "She exhaled."
    sl "Where did you go, I've been looking for you all morning!"
    me "Why?"
    show sl serious pioneer with dspr
    sl "Is it okay that I don't know where my boyfriend is?"
    "Slavya answered with a question."
    sl "I'm coming to your cabin to pick you up and hug you, but you're not there!"
    sl "And Olga Dmitrievna says that you got up early, even before her briefing, and, muttering that you went «to live up», left."
    me "Went to live up to?"
    "I was just thinking about the images from my dream."
    me "I wasn't going to conform to anything, at least not yesterday."
    "Honestly, I confessed."
    show sl smile2 pioneer with dspr
    sl "Yes, I already realized that you're lazy!"
    "Slavya smiled."
    sl "That's why I was going to push you to exercise."
    me "So now you're going to push me in the morning and make me sandwiches for breakfast?"
    "It's not like that was sarcasm, but…"
    show sl normal pioneer with dspr
    sl "Dry eating is bad for you, I can make you porridge better, I know how."
    th "I've just been almost openly invited to live together - isn't that nice?"
    dreamgirl "And you haven't even held hands yet!"
    th "Your sarcasm is misplaced."
    th "Especially on an empty stomach, I wouldn't understand it."
    sl "So where have you been?"
    me "Oh, I'm getting a jealousy scene, it's adorable!"
    show sl shy pioneer with dspr
    sl "Semyon, don't be silly."
    me "Okay, I'm sorry. {w}I was just taking a nap."
    show sl normal pioneer with dspr
    sl "And I didn't see you at breakfast either. {w}Hungry?"
    me "You ask!"
    dreamgirl "I am what I yam!"
    th "Nein, ich spreche kein Deutsch."
    me "Missed it, it seems. {w}And the time is late."
    if alt_day_binder != 1:
        me "I guess it's silly to count on buns and kefir?"
    else:
        me "You said you wouldn't leave me hungry. {w}Do you have any supplies?"
    show sl laugh pioneer with dspr
    sl "No, but we'll find something in the kitchen. Let's go!"
    hide sl with dissolve
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_sl_cl_sh_problems:
    play music music_list["everyday_theme"] fadein 5
    scene bg ext_dining_hall_near_day with dissolve
    if alt_day5_sl_cl_hentai_done:
        "Today's the day's a mess."
        "It's all wrong, it's all wrong."
        "It's turned into a circus with jogging, puppies, all before I even exercise!"
        "So hands off my routine, at least let breakfast be proper!"
        "I kept repeating it and repeating it, marching behind Dvachevskaya."
        "In short, I jinxed it."
    "We made it to the canteen. Well, how do I say this."
    "We even managed to stand on the first step of the porch before another insurmountable obstacle appeared."
    dn "Semyon!"
    show dn sad pioneer at right with dissolve
    "Behind me stood the pioneer I had carried on my hump yesterday - a curly-haired young man with sly eyes that made him look like a big trickster."
    "Now, however, he was in no mood for jokes; he was all wrinkled and anxious."
    "Apparently something serious did happen."
    me "What?"
    "I asked."
    me "Something wrong with your leg?"
    "He mechanically threw a glance at his leg, where a band-aid had been applied across the ankle, and shook his head in the negative."
    show sl normal pioneer at left with dissolve
    "Slavya turned around."
    show dn surprise pioneer at right with dissolve
    dn "Violetta's calling you to the infirmary, there's such things! Such things!"
    me "What kind?"
    "Unabashedly I asked."
    me "Actually, I was on my way to eat."
    show dn normal pioneer at right with dissolve
    show sl serious pioneer with dspr
    sl "It can wait."
    "Slavya answered in my tone."
    sl "We'll eat later, okay? {w}If the doctor's calling us, it must be serious."
    me "But I..."
    dn "Yes, she asked me to find you and call you to her."
    "Repeated Danya, impatiently stepping over in place."
    th "I wonder why our kindest doctor might need {i}me{/i}, an ordinary young man in every sense of the word?"
    "Before I could think it over, I was being dragged by the arm."
    "Slavya and Danya showed uncommon unanimity by grabbing me from both sides and dragging me."
    scene bg ext_aidpost_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    "It was a few hundred meters from the canteen to the infirmary, and we flew over it with a bullet."
    "To be exact, Slavya and Danechka flew, while I counted the irregularities of the landscape with my carcass, feeling like a tin can that conservative American mothers traditionally attach to their honeymoon car."
    play sound sfx_open_cabinet_1
    pause(1)
    show ba evil uniform with dissolve
    "Sanich appeared on the porch, barking something."
    th "It seems that Viola really was there."
    play sound sfx_close_door_campus_1
    "He slammed the door so hard that the windows rattled." with vpunch
    ba "What, are you running to help your nurse... Pioneers?"
    "He squinted."
    ba "Does she need help, that's the question?"
    me "Excuse me?"
    ba "Forget it."
    hide ba with moveoutright
    "He came down from the porch and staggered away."
    "The atmosphere around the infirmary was such that it would have been a good idea to cordon off the whole place with security guards and anti-aircraft guns on the roofs."
    play sound sfx_knock_door7_polite
    cs "Boris, if you're going to again..."
    me "Violetta, it's Semyon."
    "I responded."
    cs "Ah. Then come in."
    "Danechka swung the door in front of me and, pushing into the room, leaked in after me."
    $ persistent.sprite_time = "day"
    play sound sfx_open_dooor_campus_1 fadein 0
    pause(1)
    scene bg int_aidpost_day
    with dissolve
    play ambience ambience_medstation_inside_day fadein 3
    "In the infirmary, besides our merry company, there was Shurik."
    "He was sitting on the couch, holding a wet towel to his nose."
    th "Who beat him, I wonder?"
    "Without much interest, I thought."
    show cs normal at left with dissolve
    cs "Go back to bed, I'll talk to them myself."
    show sh normal pioneer at right with dissolve
    sh "Violetta, I can tell you everything."
    "He shook his head negatively, remaining seated."
    cs "You can't anymore. {w}And don't argue, please."
    "Shurik shook his head negatively and opened his mouth, but Viola raised her palm in front of her, gesturing for him to be quiet."
    cs "To the isolation ward."
    "With a kind of wistful hopelessness looking at us, Shurik got up."
    sh "Bad, bad. You shouldn't have done that."
    "Because of the towel pressed to his nose, his voice was gnarly, and I could hardly make out what he was saying."
    hide sh with moveoutleft
    "Some incoherent nonsense."
    cs "Daniil, you come out, too."
    show dn unsured pioneer at right with dissolve
    dn "I'm trying my best!"
    cs "Daniil."
    dn "Coming, coming."
    hide dn with dissolve
    stop music fadeout 3
    play sound sfx_open_door_strong
    show sl normal pioneer at right with dissolve
    play music music_7dl["so_cold"] fadein 3
    "It's just the three of us."
    cs "I'm not going to beat around the bush."
    "Viola began."
    cs "I'll tell you right away - Alexander has known mental problems."
    cs "He can sleepwalk..."
    if (not alt_day5_sl_cl_hentai_done) and alt_day4_sl_cl_tut_iz:
        dreamgirl "Just like you."
        th "Shut up."
    cs "He may have memory lapses, obsessions, violent outbursts."
    cs "He can't go to dances because the flashes of light can trigger an epileptic seizure."
    cs "He can never live a full life, and he knows it."
    cs "That's why he's so obsessed with his mechanical toys."
    show cs sad with dspr
    "She fell silent, dropping her hands on her knees."
    me "This is all very sad, of course. But why are you telling us this?"
    show cs upset with dspr
    cs "You see, I was able to do something for him so that he could at least communicate with other teenagers."
    cs "And we've had a positive trend."
    cs "But something happened the day before yesterday that caused him to have a collapsing regression."
    cs "Something there, at his club."
    if not alt_day4_sl_cl_tut_iz:
        me "The buzzer."
        "I guessed it."
        show cs normal with dspr
        cs "Buzzer?"
        me "Infrasound."
        cs "I need to know everything to at least know where to start the treatment."
        cs "I want you to tell me more. {w}Sit down and tell me."
        "With a shrug, I sat down on the couch and reconstructed in detail the events that had happened to me the day before yesterday."
        with fade
        show sl serious pioneer with dspr
        cs "That's how it is."
        "Thoughtfully brooded the nurse after I finished the story."
    else:
        me "It doesn't have to be at the club."
        "Ripped off my tongue before I could bite it."
        cs "What? What do you mean?"
        me "Nothing... Nothing in particular."
        "I mumbled, cursing my own intemperance."
        show cs normal with dspr
        cs "Tell me, pioneer. {w}It seems that's what Borya didn't want to tell... {w} Boris Sanich."
        "She recovered herself."
        me "But..."
        show sl serious pioneer with dspr
        sl "Semyon, don't keep quiet, maybe you can help Shurik."
        "As long as they were a united front..."
        me "You saw it all yourself - remember, back there in the labyrinth."
        cs "Well, well, well..."
        sl "There's a chain of tunnels, coal mines and caves under the camp."
        "Clear as a report, Slavya responded."
        sl "In one of these caves there is something... {w}Someone..."
        "She was embarrassed, not finding the right term."
        sl "He's sort of capable of suggestion."
        "Uncertainly she wiggled her fingers."
        cs "Suggestion?"
        sl "Yes. {w}Thoughts. {w}Pictures."
        me "Interacting with the psyche bypassing the senses."
        "I nodded."
        me "Maybe your Shurik has been there, too."
        cs "Can you describe the symptoms?"
        "Slavya briefly outlined how she'd been indoctrinated with a picture from her childhood, with a forest and a path."
        "Violetta nodded, jotting down key points - but no longer looking as hopelessly dejected as she had been ten minutes before."
        "Something seemed to be beginning to come out of her."
    sl "Can you help him?"
    show cs upset with dspr
    "Nurse sighed."
    cs "It depends what you mean by help. {w}He already speaks his own language and lives at a completely different pace."
    cs "I'm not sure I can get him back to the way he used to be."
    cs "Thanks anyway. {w}At least now I can figure out what I can do."
    cs "I hate feeling helpless."
    "She stood up, letting me know the conversation was over."
    hide cs
    hide sl
    with dissolve
    stop ambience fadeout 6
    $ persistent.sprite_time = "sunset"
    play sound sfx_open_door_clubs
    pause(1)
    scene bg ext_aidpost_day at zenterleft
    show sl sad pioneer close at cleft
    with dissolve
    "Quietly, we walked away from the infirmary."
    sl "What the hell is going on here..."
    "Slavya whispered."
    sl "Such a good camp, good people, and - here we are."
    me "I think Shurik will be all right."
    "I said - just to say something."
    sl "It would be good. {w}And it would be good for the grown-ups to take their grown-up problems and get them out of here."
    sl "I still have a whole summer of childhood I want to finish."
    dreamgirl "Childhood?"
    if alt_day5_sl_cl_hentai_done:
        dreamgirl "I'm afraid after tonight you've lost your right to childhood irrevocably."
        th "A hint as to who became a woman tonight?"
        dreamgirl "Not really. {w}Rather, it's about your adventures."
    else:
        dreamgirl "If these are the ones I'm thinking of, I'm afraid they won't ask who wants what."
    th "Do you know something?"
    dreamgirl "Just tying the facts together in a chain - the buzzer, the fog, yesterday's inspection, Shurik in the catacombs, his illness."
    dreamgirl "There's a pretty clear logic to all of this, all that's left to do is figure out who the archstrategist is to catch and kick in the ears for unethical games."
    th "Are you going to do it?"
    dreamgirl "No. You. But you will need..."
    th "What? A sword-cladder? A swag carpet?"
    dreamgirl "Strength, you fool! {w}March to feed."
    "Sharing the considerations of the inner voice, I got consent, a cold palm, and a faithful companion."
    "And we went to the canteen."
    "At last!"
    stop music fadeout 3
    with fade
    return

label alt_day6_sl_cl_breakfast:
    play music music_list["what_do_you_think_of_me"] fadein 3
    scene
    $ renpy.show("bg int_dining_hall_sunset", at_list = [zenterright], what = Noon("bg int_dining_hall_sunset"))
    show sl normal pioneer at right
    with dissolve
    play ambience ambience_dining_hall_empty fadein 3
    "It was a mess in the canteen - the hungry pioneers had consumed everything, there wasn't even any bread left."
    sl "It's a nightmare, how do they manage to feed them all?"
    "Slavya laughed when she didn't even find any crusts in the breadcracker."
    me "Now what to do?"
    "Her parents must have visited her the day before yesterday, maybe they even brought something?"
    "But the greedy Slavya has mercilessly ruined my dreams of home-cooked food."
    show sl smile pioneer with dspr
    sl "Let's play closed camp!"
    "She rattled off a bunch of keys."
    me "How do you play it?"
    sl "It's simple: we go around the canteen and see what we can feed you."
    with fade2
    "I didn't want to play on an empty stomach at all."
    "But it seemed to be the only way I could get my worms to starve."
    "So I managed to dig up a relatively soft loaf in the back of the country - and I was about to tear myself a piece, but I got a slap on the wrist."
    sl "Semyon, don't act like a pig!"
    "Sternly said Slavya to me."
    "And instead of me she fed the bun to some square, white-sided machine that said AHM."
    me "My food!"
    "I sorrowfully exclaimed."
    "The machine said «nom» and instead of a loaf it gave us a pile of soldier-thick slices of buns."
    th "And, of course, a big, big piece - a trophy for the fastest runner, who had time to run into the bread room and shout «auntie cook, is there a big piece?!»"
    "I don't even know if it's a good thing that I ended up here as an adult. {w}Maybe ten or twelve years would have been the best time."
    "To race with Ulyanka, to ravage the old Finnish mill, to climb attics and throw rubber balls at the camp Olympics - whoever throws the farthest."
    "Grown-ups have interesting lives, no doubt, but mischief like this almost disappears from it."
    "And if you try to resurrect them, you'll be like that beaver with a flap of curls framing his bald head, who comes out of the canteen door every morning, dressed in his pioneer uniform, with a tie, in his shirt."
    "Sits down at the table next to the pioneers, a grown man, and smiles stupidly as he eats his breakfast."
    "As they say - childhood in one place plays."
    "Slavya was already making chicory in the kitchen, which I kept calling 'Soviet Coffey' out of habit from my childhood; a pot of aluminum rattled on the small stove already."
    "A girl was courting her cavalier."
    dreamgirl "How touching! I wipe away an unwanted tear."
    th "No, why, is it bad?"
    dreamgirl "It's fine! You get indigestion from your instant noodles, and then you look at anyone who's not too lazy to make you semolina, like a goddess in the flesh."
    dreamgirl "They say the way to a man's heart is through his stomach! {w}But before that it would be a good idea to marinate him on a bachelor's diet for seven years."
    "I was about to say something - no doubt a very witty and original thing - but there was a plate of semolina on the table in front of me."
    th "Don't tell me you..."
    dreamgirl "Yes, I am the messiah and prophet! She also has a plate of sandwiches in her kitchen, though without butter."
    th "I see, sniff like a dog, eye like an eagle."
    me "Listen, thank you so much! {w}Where did you learn to cook?"
    show sl laugh pioneer with dspr
    sl "You try it first, maybe you won't want to eat at all."
    "Laughed the clearly flattered girl."
    "She went to the kitchen for a second plate - my inner chatterbox didn't miss the mark here either, the sandwiches really were butter-free."
    sl "Sorry, it all went to porridge."
    scene
    $ renpy.show("cg d1_sl_dinner_day_7dl", what = Noon("cg d1_sl_dinner_day_7dl"))
    with dspr
    dreamgirl "She apologizes like she ate the butter herself."
    dreamgirl "Immediately act hurt and tell her you understand, but there's still a residue, and the only way to turn it around is to kiss a pure maiden."
    "For a change, I did as the inner voice advised, and was rewarded with a laugh and a kiss."
    "The porridge turned out to be more than decent, and I repeated my question."
    scene
    $ renpy.show("cg d1_sl_dinner_0_day_7dl", what = Noon("cg d1_sl_dinner_0_day_7dl"))
    with dissolve
    sl "Yeah, you know..."
    "She clutched at her braid with embarrassment."
    sl "I've got a pretty big family, and the boys... You know, you're helpless in some ways."
    me "You mean for sustenance?"
    sl "Yes. {w}That's why I had to fill in for my mother sometimes - I've been standing on the stool at the stove since I was six."
    me "And you were allowed that easily?"
    scene
    $ renpy.show("cg d1_sl_dinner_day_7dl", what = Noon("cg d1_sl_dinner_day_7dl"))
    with dissolve2
    sl "Mother would come home very late from her after-school program and leave very early - and everyone wanted to eat."
    sl "It's fair to say she had no choice."
    sl "Although I don't like to cook - for myself. {w}There's usually an apple or a carrot or two at home, and that's all I need."
    "After looking at her... ahem... statues, I decided she was a bit of a sourpuss."
    "It takes a lot of stuff to make that kind of muscle work, an apple is hardly enough."
    sl "Tasty?"
    "She nodded at the plate."
    "Well, what was there to say?"
    me "Very."
    "I said honestly."
    me "Can I be your little brother?"
    $ renpy.show("bg int_dining_hall_day", at_list = [zenterleft], what = Noon("bg int_dining_hall_day"))
    show sl laugh pioneer at cleft
    with dissolve
    "It suddenly occurred to me that I was asking a frankly stupid question after all."
    "Wouldn't the girl have thought I was trying to push her into a friendzone... If that concept exists here, of course."
    "But she reacted the right way."
    "She didn't have time to say anything, though - we were rudely interrupted."
    stop music fadeout 3
    return

label alt_day6_sl_cl_ba_quest:
    $ renpy.show("bg int_dining_hall_day", at_list = [enterright], what = Noon("bg int_dining_hall_day"))
    show sl smile2 pioneer at left with moveinleft
    show ba em1 uniform at right
    with dissolve
    play music music_list["always_ready"] fadein 3
    ba "Pioneers!"
    "Rattling down on the bench next to me, Sanich clapped me on the shoulder so that I nearly parted with the contents of my stomach."
    "At least I wasn't chewing anything."
    ba "I've been looking all over for you!"
    th "There was no sadness..."
    "It seems my plans for a languid morning alone with a hottie can confidently be said goodbye."
    dreamgirl "I feel like these plans weren't ever meant to come true."
    th "Why not? We bathed together, went for walks, now she's saving me from starving to death for once."
    dreamgirl "Because the time she spends on you, she doesn't spend on her greatest passion. {w}Got the hint?"
    th "Shit. Accumulating trash and unresolved cases, unreconciled children, unreconciled miracles, and generally, it's hard to be a god?"
    dreamgirl "Goooood. Let me pat your head."
    th "Go away."
    show sl normal pioneer with dspr
    sl "Yes, Boris Alexandrovich?"
    if alt_day5_sl_cl_hentai_done:
        "Slavya is sweet and kind to everyone."
        "Also, Sanich is retiring, and we should be a little nicer to him."
    "He took a sip from my cup, wrinkled his nose:"
    ba "How do you drink that garbage?"
    if alt_day5_sl_cl_hentai_done:
        th "Take it easy!"
    ba "I'd be embarrassed to pour that slop into cups."
    if alt_day5_sl_cl_hentai_done:
        th "Eaaasyyy, I said."
        "I gritted my teeth."
    me "Were you looking for us to scold my coffee?"
    "I asked politely."
    show ba smile uniform with dspr
    ba "Huh?"
    "He looked again at the cup and finished the contents in a gulp."
    ba "No, I'm here for another reason."
    "Looking regretfully at the empty vessel, he summed up:"
    ba "Not enough."
    ba "All right, to business."
    show ba normal uniform with dspr
    ba "I heard you were assigned to caulk that hole on the way to our fire pit, right?"
    "I nodded cautiously."
    ba "I think I'll take care of the hole myself, I've got something to plug it with."
    me "Is that so?"
    ba "Yes. {w} And you in return..."
    th "You bet your ass I will."
    stop music fadeout 3
    stop ambience fadeout 6
    scene black
    pause(2)
    play music music_list["two_glasses_of_melancholy"] fadein 1
    scene bg ext_path_day with dissolve
    play ambience ambience_forest_day fadein 3
    "Sanich strictly forbade us to go down into the tunnels. Our job was simply to lock the door to the old camp."
    "After the briefing, Sanich went off to referee the volleyball match between the camp team and the counselor squad."
    "Slavya, frankly, was far from averse to a little bouncing at the net, too."
    if 'volley' in list_clubs_7dl:
        scene bg ext_path_day at zenterleft
        show sl sad pioneer at cleft
        with dissolve
        sl "We never played a single game."
        "She was upset."
        sl "It was a waste of time signing up for our section."
        "I shrugged my shoulders philosophically."
        "Hand on my leg, I only signed up for volleyball to make Slavya happy."
    else:
        scene bg ext_path_day at zenterright
        show sl smile pioneer at cright
        with dissolve
        sl "I'd play volleyball with you!"
        "She declared, snuggling up next to me-the width of the path allowed."
    me "We can play when we get back to camp, if you want."
    show sl normal pioneer with dspr
    sl "I'd love to, but..."
    th "Who would have guessed? {w}There's always some «but»."
    sl "You haven't forgotten what day it is, have you?"
    if alt_day5_sl_cl_hentai_done:
        "Potentially the day some blue-eyed beauty with the middle name Semyonovna was conceived, I guess?"
    "I shrugged."
    th "Friday, I think?"
    show sl laugh pioneer with dspr
    sl "Last day of the shift, Syomushka, remember?"
    me "Right... So we're expecting a farewell mega-dinner, a gala concert, a closing disco, and a royal night?"
    "Slavya nodded in response to each listed event."
    "Her eyes sparkled."
    show sl happy pioneer with dspr
    sl "About dinner and the night, I honestly wasn't aware of it!"
    "She said enthusiastically."
    sl "How do you keep it all in your head? Don't you want to try being an activist?"
    th "God forbid!"
    me "Thanks, but no. {w}And as far as events go, I've been a victim of them all my life, I've already memorized the order a little bit."
    show sl normal pioneer with dspr
    "I was given another strange, testing look, and then returned to the original topic of conversation."
    "What's there to test now? I already confessed everything I wanted to yesterday."
    sl "The concert is scheduled for five hours, and we have to get the venue ready for it, check the equipment and so on."
    sl "Help me."
    "She didn't ask, and I immediately showed my fangs to the world."
    me "And if I don't?"
    show sl tender pioneer with dspr
    sl "Please, pleeeeeease, coooomeeee oooon, Syomushka."
    "She gave me that look that made me want to fall on my back and scratch my belly."
    th "Witch!"
    "And I gave up."
    me "Alright, whatever you say."
    show sl normal pioneer with dspr
    sl "Thank you so much, you're a miracle!"
    "With a deafening kiss on my chin, she turned - it seemed - into a deafening wall of bushes."
    me "Where are you going?"
    sl "Let's go!"
    scene
    $ renpy.show("bg ext_path2_day", what = Noon("bg ext_path2_day"))
    with blind_r
    play sound sfx_bush_leaves
    "Slavya led me down some obscure path, which, apparently, she just didn't venture into at night."
    "Most likely some rather tangible cut known only to her."
    if (alt_day4_sl_cl_lf_solo in (0, 3)):
        "She didn't take us this way on our last visit."
        "And Lena didn't say a word about taking a shortcut somewhere - she didn't know."
    else:
        "I mean, they somehow managed to miss me at night. And there was only one road."
    scene bg ext_path2_day with dissolve
    "We walked in silence, staring intently at our feet."
    "I really wanted to talk, though."
    "There were many thoughts in my head, and most of them were not at all about where or why we were going."
    "Especially after what happened yesterday!"
    "I even opened my mouth to... {w}But Slavya, without turning around, put her finger on my lips."
    show sl smile pioneer with dspr
    sl "Semyon, not now, okay?"
    "She asked."
    sl "I'm trying hard not to be shy with you, I don't know how, and if we talk, I'm afraid I'll have to learn after all."
    "After she fed me breakfast, it was a little late to talk about any shyness there, in my opinion."
    "But I didn't argue. {w} Everyone has their own roaches, mine will also make someone else put his palm to his face."
    "Leaving my lips alone - I only had time to grasp the air - Slavya continued on her way."
    with fade2
    "We walked about three more kilometers - not much if you walk during the day, but at night, I don't think you can walk that kind of trail."
    play sound sfx_hiding_in_bush
    "And among the parted pines a clearing appeared."
    scene bg ext_old_building_day_7dl
    with dissolve
    play ambience ambience_old_camp_outside fadein 3
    "With a familiar house in the middle."
    if (alt_day4_sl_cl_lf_solo in (0, 3)):
        "Lena was telling me something, but I couldn't remember anything of it."
        "The whole camp seemed to be a mobile structure, capable of moving anywhere if necessary, with all its tents, field kitchens, and the like."
    "It was just like last time here."
    "Except in the daytime you perceive half the mysteries much more down-to-earth, the nighttime, mystical thinking doesn't work, so neither the rusty swings nor the derailed merry-go-round seem threatening."
    th "Or is it because I've been here once before?"
    "Ever since I was a kid, I'd been taught to be afraid of all these abandoned buildings, frightened by stories of squatters-lumpen, of the strange and scary things going on here."
    "And there was, there was every reason to be scared - and it wasn't because of the work of Hollywood horror maestros or the fact that most maniacs and murderers operated in the vicinity of places like this, which were extremely convenient for disposing of bodies."
    "It's just that this place is dead. Abandoned. Forgotten. {w}And death always attracts death."
    scene
    $ renpy.show("bg ext_old_building_day_7dl", what = Dawn("bg ext_old_building_day_7dl"))
    with dissolve
    "You can play bravado all you want, but a place that, for one reason or another, was once enlivened by people's energy becomes cursed when people leave."
    "Man is Midas, capable of turning anything into radioactive gold."
    "There are, of course, extreme people who, for the sake of overcoming fear and releasing adrenaline into the bloodstream, seek out places like this all over Mother Russia."
    "So-called stalkers. {w}But these are extreme people."
    scene
    $ renpy.show("bg ext_old_building_day_7dl", what = Noon("bg ext_old_building_day_7dl"))
    with fade2
    "There was a sultry, shivering silence over the clearing, the splash of the river in the distance, and the grass, never mowed by anyone, moved lazily."
    if alt_day4_sl_cl_lf_solo in (1, 2):
        "If I'm right, I happened to come out of the woods at a slightly different point."
        "So from an unfamiliar angle I didn't recognize the clearing at first."
    else:
        "Last time we came out from a road, albeit an old one, and our path lay on concrete slabs half-covered with turf."
    "And this time the path to the administration building of the old camp was blocked by chaotic rows of thistles, bromegrass, and nettles."
    sl "So, how would we get through..."
    "Slavya looked tastefully at the upcoming front of work, but I beat her to it."
    "And with a «YO-HO-HO!» yell, swinging my blade, assaulted the enemy! Cut into the enemy's ranks, smashing and hacking them to pieces without counting."
    "Behind me Slavya shouted something, indistinguishable because of the laughter choking her, but I paid no attention and continued to fight to the death!"
    "Until, at last, the last soldier with the umbrella fell in an inglorious death of cowards."
    "Only then did I turn around and look at Slavya dying of laughter."
    me "Please, my lordship, they will not disturb you again, I promise!"
    show sl smile pioneer with dspr
    sl "Semyon, you're a dummie, you know?"
    "Slavya shook her head."
    me "That's where we stand!"
    "It occurred to me that we do complement each other quite well - I give Slavya light-heartedness and a generally easy-going attitude to everything, a momentary desire to go a little crazy sometimes."
    "And she charges me with a desire to be something more than just alive, spurs the almost extinct sparks of vanity, of aspirations."
    "The two of us could make one perfect person."
    "Not the perfect one, the sigmatic, synthetic hominid, infallible and incapable of making mistakes, finding happiness in order - Slavya was dangerously close to that state, discounting her tender age."
    "Rather, one that lives perfectly, considers life worth living, and enjoys simply the current of seconds under the skin."
    "That's the only reason, not because I'm an infantile fool, I showed her my tongue and jumped up and grabbed her in my arms, jammed her up, clawed at her, listening to her muffled indignant exclamations."
    "And then I grabbed her in his arms, like yesterday, and dragged her."
    sl "Let go, let go, you madman!"
    "She screamed, making cautious attempts to get out - knowing that if we fell, we'd be on top of her."
    "But I only let her feet touch the ground when I dragged her all the way to the porch."
    scene bg ext_old_building_day_7dl at zenterright
    show sl normal pioneer at cright
    with dissolve
    sl "Still, you really are something..."
    "It was quiet here, peaceful. Time, life, hustle and bustle, everything was left behind."
    "All that was left was the overgrown territory of the camp. {w}Me. And Slavya."
    "Just the simple understanding - we might be seeing each other for the last day, and tomorrow something would happen that could keep us apart."
    "And I wish I could really catch everything from life, but..."
    "I've touched something no one should know about."
    "I was lucky to have a pioneer in front of me, Shurik, who took the brunt of the local security systems."
    "I was lucky that I always had a person with me, not only to rely on in case of emergency."
    "But that person also demanded the same - which meant no room for slackness or weakness."
    "I didn't know what was in the mines, and I didn't want to know."
    "I didn't know what the story was with that buzzer, and I didn't care."
    "My adaptive psyche openly told me to mind my own business, and I was perfectly okay with that."
    "But it was frustrating to realize that someone else's clear, logical calculation had played on me - I really thought, until recently, that I'd gotten into the well-oiled existence of pioneer camp, where the main difficulty was just not to die of boredom."
    "And in reality..."
    play sound sfx_door_squeak_light
    pause(1)
    scene bg int_old_building_day_7dl at zenterright
    show sl smile pioneer at cright
    with dissolve
    play music music_7dl["nowyouseeme"] fadein 3
    sl "Let's go, we have to close the basement."
    "Slavya pulled me with her."
    "There's some hell going on here."
    "And no devilry has no place in a recreational area for children."
    "Just because it reeks too much of inhuman experimentation in the spirit of Comrade Mengele."
    scene
    $ renpy.show("cg d4_hatch_night_open_7dl", what = Noon("cg d4_hatch_night_open_7dl"))
    with dissolve
    "It takes someone to at least try to figure it out."
    "The problem is, I'm not a movie action hero, not Rambo-Stallone, shooting two-handed Macedonian-style with assault rifles."
    "All my heroism is enough to do is to stand still with my head in my shoulders - what if disaster strikes, what if it whips my face?"
    "Like this."
    "I frightened off a hissing snark that was washing at the edge of the stairs, and it ran off into the darkness with an indignant screech."
    play sound sfx_bodyfall_1
    "Mechanically scared - used to it already."
    "Man is such an animal that he can get used to and adapt to anything."
    "Yesterday this rodent frightened me to my knees and paralysis. {w}I'm used to it, adapted even."
    "But where to take a blitz course on how to adjust to the world, to life - it's not like beating monsters with a stick."
    "To not be afraid of decisions."
    "Not to be afraid of responsibility."
    "And to find solace in doing what you love, not sitting with your pants against a window into a digital cloaca."
    scene
    $ renpy.show("cg d4_hatch_night_open_7dl", what = Noon("cg d4_hatch_night_open_7dl"))
    with dissolve
    "Slavya had the bundle this time."
    "I nodded to her."
    me "Close it up."
    "She nodded understandingly and took a bunch of keys out of her pocket, searched a little, found the right key, and took one of the padlocks from me."
    play sound sfx_fall_metal_door
    pause(1)
    scene
    $ renpy.show("cg d4_hatch_night_7dl", what = Noon("cg d4_hatch_night_7dl"))
    with dissolve
    "She acted, as usual, with speed and fire - here the technological holes were tied up with wire, here on the welded hinges appears a beautiful 'bow' made of the same wire."
    "The closed padlock completed the still life."
    scene bg int_old_building_day_7dl at zexitright
    show sl smile pioneer at cright
    with dissolve
    sl "Done. We can go back."
    me "What about the hole on the way to the fire pit?"
    "Slavya shrugged."
    show sl normal pioneer with dspr
    sl "Uncle Borya said he would think of something, so he will."
    sl "I believe in him. {w}And so should you."
    "She looked around."
    sl "There's nothing else we can do, is there?"
    "I shrugged."
    sl "Then let's go give an account of the errand we've completed."
    hide sl with dissolve
    stop music fadeout 3
    stop ambience fadeout 6
    return

label alt_day6_sl_cl_ba_kgb:
    scene bg ext_path_day with dissolve
    play ambience ambience_forest_day fadein 3
    "The way «back», as is always the case, took much less time than the way «there»."
    "It was half past two on the clock when we reached the south gate of the camp."
    scene bg ext_admins_day_7dl at zenterleft
    "After asking the pioneers around a bit, we went to the camp director."
    "Apparently, he needed our Boris Sanich for something."
    play music music_list["door_to_nightmare"] fadein 3
    "The window to the room was open, and I gestured for silence and crept closer and turned to listen."
    sl "Are you going to eavesdrop?!"
    "With one lip she asked."
    "I pressed my finger to my mouth, showing her to observe the silence, and beckoned to join close by."
    "Slavya crouched against the wall beside me."
    "The truth is that our precautions were clearly unnecessary - the chief's office was so crowded that we could have held a herd of elephants here and no one would have noticed."
    "There were three voices."
    "Sanich's whooshing bass."
    "The cracked, dry voice of the camp leader made my throat scratch and made me want to cough."
    "The third voice was vaguely familiar, but no matter how hard I tried, I couldn't remember who it might belong to."
    "Slavya was giggling next to me, snuggling up against me with her hip, and that was a great distraction, too."
    "Probably wouldn't have understood anything, would have walked away empty-handed if it hadn't been for the name that came up."
    ba "Anatoly Ivanovich, with all due respect..."
    "Mumbled Sanich."
    th "That's right! {w}This is the old man from yesterday who was supposed to pick me up from camp!"
    th "How did he come back so fast?"
    voice "What respect, Borya? {w} You've got pioneers wandering around the Facility, and you're rubbing it in my face about respect."
    "Anatoly sighed."
    voice "Fuck your clown circus, honestly. {w}You're two months away from your retirement, I'm six months away from my pension, why are we even bothering each other?"
    voice "They'll send some ideological snot-nose from the capital and let him figure out why and how it happened here that the techno-curtain was turned off and the pioneers got into the Facility."
    ba "Maybe it's time to close down the camp."
    "Sanich muttered."
    ba "But the kids..."
    voice "Kiiiiiids."
    "Mocked the old man."
    if alt_day4_sl_cl_tut_iz:
        voice "You've got these kids without an algorithm climbing into the underground, and you're defending them! Stupidity must be punished."
    ba "But they didn't know anything."
    voice "And they shouldn't know. {w}And it was your job to make sure they won't by the way."
    voice "Anyway, that's it. {w}I'm sick of it. Pack your things, I'll take you to town - you look like you've given up, old man."
    th "You're one to talk."
    "I snorted."
    ba "But I…"
    voice "That…"
    ba "…just…"
    voice "…is an order."
    "The old man."
    voice "I'm waiting for you at the gate by three o'clock. {w}Off you go."
    play sound sfx_open_door_kick
    "Sanich pounded his fist into the wall in anger, and, slamming the door good and proper, went out."
    th "He seems to have decided to break down all the doors today."
    "I concluded, unbending - it would take him half a minute to get outside, during which time he should assume the posture of the newly arrived pioneers - and dragging Slavya after myself."
    "We ran up to the porch at the same time as the gym teacher showed up."
    scene bg ext_admins_day_7dl at zenterright
    show ba evil uniform at cright
    with dissolve
    "To say he was angry would be an offense by comparison."
    "Thick as sausage fingers felt like they were clutching something invisible, and I swallowed, imagining my own neck there."
    "Because the situation was partly my fault."
    ba "Ah, the pioneers."
    "He exhaled, forcing himself to calm down."
    ba "What's up? Any other questions?"
    scene bg ext_admins_day_7dl at enterleft
    show ba evil uniform at right with moveinright
    show sl normal pioneer at cleft
    with dissolve
    sl "Not really. {w}Boris Alexandrovich, we've locked everything in there."
    "Reported Slavya."
    "Yea, only salute gesture was missing."
    dreamgirl "You don't put your hand to an empty head, though."
    th "Shush."
    ba "Any trouble?"
    sl "None. {w}Found one snark, chased it down the tunnel."
    ba "Good."
    play sound sfx_keys_rattle
    hide ba with dissolve
    "He turned and walked toward the canteen."
    "He moved like a poorly made puppet."
    me "Boris Alexandrovich!"
    "I called out."
    show ba em1 uniform at fright with dissolve
    ba "What do you want, pioneer?"
    me "Is something wrong?"
    ba "How did you..."
    "He looked over my head at the camp director's window."
    ba "I see. {w}Eavesdropping."
    "He wasn't asking, he was affirming."
    ba "Got much of anything?"
    me "Nothing."
    "I confessed."
    if alt_day4_sl_cl_tut_iz:
        me "I recently had a dream, and there were very similar terms..."
        ba "A dream?"
        me "Yes. {w}About the future."
    elif alt_day5_sl_cl_hentai_done:
        me "This has something to do with Shurik's illness, doesn't it?"
    else:
        me "But I woke up today in a cave for some reason."
        me "At the very doorstep."
        me "And in my head all the time I kept hearing those «algorithms» of yours."
    ba "Alright."
    hide sl with dissolve
    "He grabbed me by the shoulder and dragged me behind him."
    ba "To the gym. {w}Tell me all about it on the way."
    me "But I was going to lunch!"
    ba "Let's go together, I'll feed you from the counselor's table."
    th "Uh-huh... No fruit or sweets."
    "I threw an apologetic look over my shoulder and, trying to choose my words carefully, went after the gym teacher."
    "There was a lot to tell."
    "And, to tell you the truth, I wasn't sure I should tell Sanich everything."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_sl_cl_dinner:
    play music music_list["your_bright_side"] fadein 3
    scene bg int_dining_hall_day with dissolve
    play ambience ambience_dining_hall_empty fadein 3
    "Fortunately, this time we managed to fight back quickly enough - the dinner wasn't over yet."
    "The lonely figure of Slavya loomed over our tables, representing universal sorrow."
    show sl normal pioneer with dspr
    sl "You've finally arrived."
    "On the table in front of me, two red-skinned apples appeared instantly."
    sl "I had to fight with Ulyana for them, appreciate it!"
    me "Thank you!"
    "I went over to the distribution and fetched the plates."
    "Slavya sat in the same seat, rolling her glass thoughtfully between her palms."
    sl "Will you tell me what kind of conversation you and Uncle Borya had there?"
    "Without raising her eyes, she asked."
    "As if she didn't know something! She's been through everything with me."
    if alt_day4_sl_cl_tut_iz:
        me "In a nutshell, the day before yesterday, when I didn't dare go with Shurik - I went to the attic of the infirmary, thinking I'd be good at hiding now."
        me "And fell asleep. {w}I didn't even notice how."
        sl "Yes, Violetta was saying something."
        me "And while I was asleep, I had a dream. {w}About Sovyonok, about you and me."
        sl "And what was there?"
        me "The future, Slavya. {w}War for something that was here."
        "The dream remained in my memory as a clear imprint - as my own life experience, I could reproduce any part of it thoroughly."
        if not alt_day5_sl_cl_hentai_done:
            "Then today's dream appeared next to it, and it became clear that they were connected by the same story."
            me "And today I had another strange dream - and it seemed to continue the previous one."
        show sl smile pioneer with dspr
        sl "And I'm always dreaming such nonsense."
        sl "Will you tell the dream?"
        me "No. Sorry."
        show sl normal pioneer with dspr
        sl "It's okay."
        sl "Something nasty, I think. I'll stay out of it."
        th "You shot at me in my dream. Oh yes, you can tell it was something unpleasant."
        "She didn't seem discouraged by my refusal - the talent for sensing inner boundaries is evident."
        sl "But you're free now, aren't you?"
        me "Why?"
    elif not alt_day5_sl_cl_hentai_done:
        me "You know it all yourself."
        show sl normal pioneer with dspr
        sl "No way! Put it all out in order."
        me "What kind of order do you need?"
        me "We said goodbye to you last night, I went to bed."
        show sl serious pioneer with dspr
        sl "Olga Dmitrievna didn't scold you?"
        me "No, she was sure that I would spend the night in the infirmary, but as you can see..."
        sl "Next, next!"
        me "Next I woke up in the tunnels under the camp."
        me "I don't remember the transition between sleep and the tunnels, there wasn't one."
        me "But like you say, I was talking to the squad leader about something."
        me "Ended up in the tunnels, near the center of the mines."
        sl "Oh, we were there yesterday, weren't we?"
        "She nodded."
        sl "Where the round cave is."
        th "And… {w}And! {w}And!!!"
        th "Why don't you say something?!"
        sl "Did it take you long to get out?"
        me "No, I got out, you just spotted me."
        me "Slavya, do you remember anything else about that cave?"
        show sl shy pioneer with dspr
        sl "W-well... I think you lost the keys somewhere there, and then Uncle Borya found them."
        sl "And you were there for some reason..."
        me "What?"
        sl "You were pulling me away from something, like you didn't want me to see it."
        "I see. She doesn't remember about the alien crystal abomination."
        "I'm also surprised it was me down there and not her. Or both of us."
        me "That's it, you don't remember anything else from down there?"
        sl "Nothing... Ah!"
        "She slapped her forehead."
        show sl laugh pioneer with dspr
        sl "We were running from snarks there like two fools, I remember that."
        "Doctor says - straight to the morgue."
        "I set the plates aside and got up."
        me "What are your plans for the afternoon?"
    else:
        "I shrugged."
        "There really wasn't much to tell."
        me "Just did a little extrapolation: what I know, what I don't know."
        me "But there wasn't enough data."
        "I began to curl my fingers."
        me "The buzzer - it's known not just in this camp, since so many people have come to the signal."
        me "All these tunnels, bomb shelters, mines-mazes - they didn't come from nothing, either."
        "During the satori with the map, we managed to catch the general position of the communications - and they were all built around one logical center."
        "Located, understandably, in the center of the entire theater."
        me "And finally, last but not least, how does a children's camp relate to all of this?"
        scene bg int_attic2_day_7dl
        if loki:
            $ renpy.show("bg ext_winterpark_7dl", what = D3_intro("bg ext_winterpark_7dl"))
        elif herc:
            $ renpy.show("bg int_store_7dl", what = D3_intro("bg int_store_7dl"))
        else:
            $ renpy.show("bg int_sam_house_clean_7dl", what = D3_intro("bg int_sam_house_clean_7dl"))
        show prologue_dream
        with dissolve
        me "Or did they really gather a few subjects of interest, lock them in concrete bags, and feed them with waste?"
        play sound sfx_wind_gust
        scene bg int_dining_hall_day
        show sl scared pioneer
        with dspr
        sl "You said that last phrase in a strange voice."
        me "What?"
        show sl normal pioneer with dspr
        sl "I'm probably going to say something stupid, but it's like you started to disappear, such an echo, like in an empty room, of your voice."
        me "You imagined it."
        me "And I can even guess the reasons for these visions."
        dreamgirl "All that remains is to know our place in the scheme of things."
        th "Our place?"
        dreamgirl "Syoma, wake up, perhaps Slavya's charming personality is what made you forget this unimportant fact!"
        dreamgirl "But you are still an alien from another world!"
        th "Not from the future anymore?"
        dreamgirl "What future, dumbass?! {w}Do you remember a lot of the Soviet Union general secretaries with the surname Genda, or pioneers with size four boobs?"
        sl "And what's the reason?"
        "In a slightly strained voice she asked."
        me "Fatigue. And constant nerves."
        me "I'm more than sure you're not going to go resting now, either, but running around camp with your tail up."
        show sl laugh pioneer with dspr
        sl "I don't have a tail!"
        me "But you're going to do something anyway, and it's obviously not a repeat of washing one dirtling, is it?"
    sl "There's really a concert tonight."
    sl "Miku's doing it, but she's the organizer, and I have to check the equipment, see what works where."
    me "That shouldn't be too much of a problem."
    sl "Yes."
    sl "We need an amplifier for the concert. {w}Will you go get it?"
    me "It's heavy, isn't it?"
    "I remembered how much my «VEGA» weighed."
    show sl normal pioneer with dspr
    sl "Not really. {w}But it's hardware!"
    sl "You boys always tell women to stay away from your hardware!"
    dreamgirl "Look, let me marry her!"
    th "Shush."
    me "Alright."
    if alt_sp >= 6:
        menu:
            "Maybe we can go together?":
                sl "Syom, come on, seriously, we won't have time if the two of us walk together."
                sl "Although I don't mind at all."
                me "No, I'm saying, there's probably not only an amp, but there's a lot of other equipment you need, you obviously know better than I do."
                show sl normal pioneer with dspr
                sl "Actually, I don't know. {w}But I know someone who does."
                sl "How about you go over to Miku now, make a list of what you need, and then come back to me, and I'll open the clubs. Okay?"
                me "Yes! And then we'll take everything from the list."
                "I nodded and got up from the table."
            "We only need an amp?":
                sl "I don't even know..."
                me "Who knows then?"
                sl "Yeah, probably Miku..."
                "Slavya's confused."
                me "Then I'll probably go to her - find out what to take, and then I'll take everything I need."
                sl "Do you need keys?"
                me "No, I might be a little late, just open the club and put the lock on, I'll latch on later."
                show sl angry pioneer with dspr
                sl "Semyon, that's no way to do business."
                sl "You must understand that I can't leave this room open!"
                "Nerd!"
                me "Okay, then just come up to the clubs in an hour, I think I'll be done by then."
                sl "What are you going to be doing there for so long?"
                "The girl inquired."
                me "It's a secret!"
                "I can't tell her I want to dress up for the disco to match my partner!"
                "And the only place to change is..."
                "I smiled and went outside."
                $ alt_day6_sl_cl_shirt = True
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_sl_cl_amp_list:
    play music music_list["so_good_to_be_careless"] fadein 5
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_musclub_day with dissolve
    "Of all the achievements of the communist system, the state that gave me the greatest joy of work was the one I liked best."
    "Or rather, not like that."
    "Any activity that you do together with someone else - a sense of elbow, that sort of thing."
    "Something like that can only be experienced in a computer game, where you're working together, in a co-op with someone else, kicking monsters."
    "And you're sure that if anything happens, they've got your back, they'll draw attention away from you, and that in general."
    "It's a synthesis of friendship, romance, combat, and belonging for more."
    "Some might call it gear consciousness and not much wrong with the truth."
    "Yes, I did enjoy this experience where I'm doing something - and someone else is doing something in parallel with me."
    "And the result is something big that we could never have managed separately."
    "A kind of creativity - a macro-level influence from a micro position." 
    dreamgirl "You mean, you two shouting «zag-zag» in different corners, and as a result your «zag-zags» turn into something like a concert?"
    dreamgirl "You call that creativity?"
    th "Something like that."
    dreamgirl "In that case hotseating in «Warcraft» is also creativity."
    th "What, you mean it isn't? Isn't what the Koreans are doing with the Horde creative? It's a natural song!"
    dreamgirl "And in that case, who's the main Korean here?"
    th "Don't you know?"
    "I was looking over my shoulder."
    stop ambience fadeout 2
    play sound sfx_open_door_2
    pause(1)
    scene bg int_musclub_day
    with dissolve
    play ambience ambience_music_club_day fadein 3
    "The club was empty."
    "At least, that's what it looked like to me."
    "Because when Miku didn't speak or move, you could tell she was only meter sixty tall, very small, very thin."
    "And she took up exactly the diameter of her own body-just like that cast-iron bombs, which are as pinpoint as you can get, with a radius of impact equal to the radius of the bombs themselves."
    "I froze, staring at her with all my eyes - mesmerized, bewitched."
    "The sunlight pouring in through the windows, breathing, alive, in which tiny dust particles play, illuminates the gold of the marble skin, plays in the aquamarine strands."
    "Prevert's lines came to mind, perfectly suited to such magical moments:"
    th "Put out the lights! {w}On Victoire Square..."
    th "Two are kissing. {w} They may be seen."
    th "Put out the lights!"
    dreamgirl "And please leave them alone!"
    th "How do you know?!"
    dreamgirl "You ask?!"
    dreamgirl "But I agree, the silent Miku is a priceless sight. {w}A real angel - when she sleeps with her teeth against the wall."
    "But a moment was missed - she looked up."
    "And opened her mouth."
    dreamgirl "So if anything - I'll, uhhh… Be, uhh… There."
    scene bg int_musclub_day at zenterleft
    show mi smile pioneer at cleft
    with dissolve
    "Some people have a way of ruining moments like this."
    mi "Hello, Senechka! How are you doing? Can you help me, because I'm getting ready for a concert?"
    "She fluttered her arms."
    mi "I don't have time - I haven't taken anything away yet, costumes haven't been ironed, phonograms haven't been put together, I'm a slob!"
    me "Actually, I'm here with an assignment."
    show mi normal pioneer at center:
        linear 2.0
    mi "How busy you are!"
    "She marveled."
    mi "So serious all over, walking around, doing things, almost like the second Slavya! Or even the first! Exactly! You're more Slavya now than Slavya herself!"
    show mi surprise pioneer with dspr
    mi "But then what should she do if she is no longer Slavya? Is she really Semyon now? What a twist!"
    "Oh my God I don't care."
    "I'll figure out which cables need to be there myself."
    "I turned around to leave."
    show mi normal pioneer with dspr
    mi "Senechka, Senechka, wait!"
    me "What else..."
    "I mumbled."
    "Slavya is actually waiting for me."
    mi "Can I use you as a man?"
    me "As a man?"
    th "Did the ball roll in the toilet?"
    mi "Not in the sense that you thought, of course! Though how do I know what you thought, you're always quiet and don't say anything! But I wanted to ask you."
    mi "Ask, ask, ask..."
    "Putting her finger to her forehead, she pondered."
    "I could almost distinctly feel how lonely in that pretty head the few thoughts felt that had inexplicably ended up there."
    dreamgirl "Miku isn't stupid!"
    "It's unclear for what reason my inner voice stood up for her."
    dreamgirl "She writes and sings songs, participates in social life, studies and is preparing to enter RUDN."
    th "RUDN was a very interesting detail."
    "But I didn't really think Miku was stupid or anything like that."
    "It's just that the mask stuck to her so firmly that you can't tell where the real Miku ends - the one who tortured the guitar at the bonfire tonight - and the current Barbie begins."
    "A hypocrite in a hypocritical world."
    th "Maybe…"
    show mi happy pioneer blond with dspr
    "I squinted."
    mi "I remembered!"
    th "That's right! She definitely should have been a blonde!"
    dreamgirl "Or should I say redhead?"
    show mi happy pioneer red with dissolve2
    th "No, she needs to be a silly girl with blond hair to be a silly girl."
    show mi happy pioneer blond with dissolve2
    th "Perfect, but actually wait, maybe platinum?"
    show mi happy pioneer platinum with flash
    dreamgirl "Daaamn!"
    "I've been thrown the image of a thumbs-up."
    mi "We've got to get this heavy thing over here."
    "She pointed to the xylophone, seemingly not at all aware that she had just revealed her true identity."
    "Blondie!"
    dreamgirl "And did you know that you have the opportunity to donate one or more vital organs to the girl's self-esteem fund."
    dreamgirl "It's true."
    show mi smile pioneer platinum with dspr
    me "Actually, Slavya is waiting for me to help her."
    me "By the way, with the preparations for your event!"
    mi "So you help both ways."
    me "Miku, I'd like to get you a list of the necessary equipment for the performance."
    "I cut into her potential monologue, hitting a few corners on the turn."
    "You couldn't have it any other way - we'd been standing around talking for too long as it was."
    show mi sad pioneer platinum with dspr
    mi "No! Chairs first, then money!"
    "Miku looked at me guiltily."
    mi "Please! {w}I just can't carry it myself, it weighs more than me!"
    th "And where does it say 'ride here' on me, I wonder?"
    "I sighed, grabbing the xylophone more comfortably."
    stop ambience fadeout 2
    play sound sfx_open_door_strong
    pause(1)
    scene bg ext_stage_normal_day
    with flash
    play ambience ambience_camp_center_day fadein 3
    "It was evening, there was nothing to do."
    "The wooden junk was not so much heavy as it was oversized, and there was no way I could get it in a comfortable position."
    "That's why I probably regretted five times that I didn't insist or yell - or even left when the idea occurred to me."
    "But you've got to help your comrades."
    scene bg ext_stage_big_day_7dl at zentercenter
    with dissolve
    "Balancing the frame, I walked up the steps to the stage."
    "I guess there's going to be a final rehearsal or something here now-the instrument will have to be set up against a wall somewhere."
    "I've done the most important thing."
    "And for the job - the reward!"
    scene bg ext_musclub_day
    with dissolve
    stop ambience fadeout 2
    play sound sfx_open_door_clubs
    pause(1)
    scene bg int_musclub_day at zenterleft
    if alt_day6_sl_cl_shirt:
        show mi smile dress platinum
    else:
        show mi smile pioneer platinum
    with dissolve
    play ambience ambience_music_club_day fadein 3
    me "That's it, I've got your instrument!"
    "I exhaled, piling into the club."
    me "Now you help me!"
    mi "Yeah? Okay. I'll be right in. Will you look at the dress?"
    th "Look at... the dress?"
    if alt_day6_sl_cl_shirt:
        me "Actually, I'd like to pick up something - but only for dancing, not for the concert."
        mi "Some shirt-pants? {w}That's easy for us! I've got all sorts of dressy things here that no one wants for some reason! Ugh!"
        mi "What's the color you want, I can pick up something in a modern-day style, you want it? With purple stars."
        "It made me cringe."
        me "No!"
        mi "I figured as much, I was just suggesting it as a joke in general, but what if you really said yes?"
        "The Japanese girl laughed."
        "She turned her back to me and pointed at the clasp."
        show mi normal dress platinum with dissolve
        mi "Button it up."
        "I blushed."
        th "Shit! Is it even okay to ask me to do that?"
        dreamgirl "And why not? It's not like she's asking you to fix her panties that her butt ate, it's just a zipper."
        th "Yeah, but where's that zipper?!"
        dreamgirl "On the back. {w}What are you getting so excited about? Exhale, it's okay."
        show mi angry dress platinum with dspr
        mi "Senechka, if you're so embarrassed by my bare back, I probably won't turn sideways, or you'll faint!"
        "Laughter again proved to be the best cure for stupor."
        me "Oh, you."
        "I muttered, trying to catch the clasp."
        "At last I succeeded."
        show mi smile dress platinum with dspr
        "I caught the zipper and, trying not to touch the exposed skin, zipped the dress on the Japanese girl."
        mi "Thank you!"
        "She adjusted the dress on her chest and, dancing, wrapped herself around her axis:"
        mi "It looks okay, doesn't it? I was told it was too revealing, but what kind of revealing is it when there's no cleavage, no necklines, even the hem is almost to the floor."
        mi "I feel like the most perfect nun in it."
        "She complained."
        me "For a nun, you have too much of everything visible."
        "I huskily uttered."
        "My supply of embarrassment was slowly coming to an end."
        "Just a little bit more, and I won't even be stuporous anymore - that's how much progress!"
        me "And it fits too nice."
        mi "Yeah? You really think so? Thank you so much, Senechka, you're the best, your opinion means sooooo much!"
        show mi upset dress platinum with dspr
        mi "Now, if you don't mind, I'll go to the costume room and see if I can get you something. Any requests?"
        "I shrugged."
        "Other than that it shouldn't be screaming trash of the '80s dandy pattern, there were no other wishes."
        me "Let it be dark."
        mi "Dark. Got it. Wait for it!"
        hide mi with dissolve
        "She shouted, disappearing."
        "Inside, something rumbled, sprinkled."
        "Then there was a gaggle of clangs - as if some monster had tried to get out of the darkness, and Miku quickly explained to him all the disadvantages of such behavior."
        play sound sfx_close_door_1
        "I was starting to get bored again."
        "Miku wasn't hitting anyone else."
        "And Slavya must have been waiting for me at the clubs by now."
        "Dumbass. What else is there to say."
        "On the other hand, I didn't want to disturb our singer either - I shuddered, remembering the series of blows heard even through the walls."
        "Not Chun Lee, understandably, but she can dish out a leg sweep, too."
        "And just when I was about ready to spit and leave, the door swung open, and a disheveled Miku appeared on the doorstep."
        play sound sfx_open_door_strong
        show mi normal pioneer with easeinleft
        mi "Here, Senechka!"
        "Winningly she declared."
        mi "The most beautiful beauty!"
        "And my eyes were presented with a very nice shirt indeed."
        "A burgundy to almost black, with overlapping closures like a traditional Chinese costume, made of ornately crumpled material, the name of which I would have difficulty saying."
        me "Brilliant!"
        "That's all I said."
        show mi happy pioneer platinum with dissolve
        mi "I knew, I knew you'd like it!"
        "Oops, I couldn't resist again."
        show mi smile pioneer platinum with dspr
        mi "It caught my attention right away, but it took a bit of work before I could get it."
        th "Like viciously kicking the closet monster, right?"
        mi "Listen, why do you keep looking at my hair so weird? It's dirty, isn't it? It's always a problem with it, it's so long, you can't keep track of it, and I don't want to cut it because it's my pride!"
        th "Yeah. Dirty."
        "She shook her tails, putting me in a trance and in the process shattering the illusion I almost loved."
        show mi normal pioneer with dspr
        mi "Is that it?"
        mi "Let's go quickly to the locker room before anyone comes!"
        me "Why?"
        dreamgirl "And she doesn't waste any time - it's only been half an hour and she's already calling you to the locker room!"
        mi "Let's try on the shirt, of course! What if it's not your size?"
        scene
        $ renpy.show("bg int_wardrobe_7dl", what = Notch("bg int_wardrobe_7dl"))
        with dissolve
        me "And what if it's not mine?"
        "It only took Miku five minutes to shatter my objections."
        "So I unbuttoned my shirt in front of the mirror, craning my neck cautiously and listening for someone coming."
        mi "Then I'll take your measurements and do a little re-stitching! I know how, I've done it many times before!"
        "A voice came to me from behind the screen."
        "That screen had to be beaten back with a fight - Miku insisted that she had to 'see everything,' I was convinced otherwise."
        "Then I wanted to go to the cabin and try on there altogether - but I guess I would have blown the whole deadline that way."
        "And Slavya is waiting!"
        "As a result, caught sight of a folded screen, put it up, fenced off - adapted."
        me "When was the last time?"
        "You should have closets full of stuff at home, chatterbox hoppy... Excluding the dressing room."
        mi "When Pa's robe stopped fitting on his belly!"
        "She giggled."
        mi "Old, old robe, but it was dear to him somehow. So I re-stitched it a little - picked up the fabric, put in wedges, now he walks around the house in it."
        me "I'm not sure you could match the fabric to a shirt like that..."
        "Mumbled I, trying on the shirt."
        "The shirt turned out like it was made on me, which I immediately told the Japanese girl."
        mi "Show me, show me!"
        "The screen was blown away like the wind, I was dragged somewhere, turned around, shrugged off my shoulders - Miku was playing dolls. With me in the lead."
        show mi normal pioneer with dspr
        mi "It's really not bad!"
        "She praised."
        mi "Now I'll iron it and bring it home to you tonight, okay?"
        "I nodded, glancing at my watch - too much time had already passed, I should have hurried up."
        mi "It would be a good idea to wash it, of course, but I'm afraid we won't have time for that."
        show mi grin pioneer with dspr
        mi "So you'll have to endure."
    else:
        me "Sorry, I'm afraid not - I've got a whole bunch to do!"
        show mi sad pioneer with dspr
        mi "You're always so busy, and you never have time for music!"
        "The Japanese girl was upset."
        "Angrily she tore off a piece of paper and scribbled something there."
        mi "That's it, take it and go."
    "She handed me a piece of paper on which a few lines were written out in a child's round handwriting."
    mi "The necessary equipment, cables, plugs."
    if alt_day6_sl_cl_shirt:
        me "That's it, bye-bye?"
        "Miku nodded and waved goodbye to me."
    else:
        "She turned away arrogantly, diligently looking past me."
        mi "It is my pleasure to say goodbye to you."
    stop music fadeout 3
    stop ambience fadeout 2
    play sound sfx_open_door_2
    pause(1)
    scene bg ext_musclub_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    "Snorting to myself, I left the club."
    stop music fadeout 3
    with fade
    return

label alt_day6_sl_cl_amp_club:
    scene bg ext_clubs_day with diam
    play music music_list["silhouette_in_sunset"] fadein 3
    "When I finally managed to get to the club building, it was well past three o'clock."
    "And I just went to get a list of the equipment I needed."
    if alt_day6_sl_cl_shirt:
        "Yeah, to look for some upgrades for the upcoming dance."
    "Even according to the most pessimistic predictions, it shouldn't have taken me more than half an hour."
    "But a man supposes and the xylophone disposes."
    th "Slavya will kill me."
    "I doomfully stated as I discovered the door had no lock on it."
    "And went to surrender."
    th "I hope I haven't kept her waiting too long."
    play sound sfx_open_door_clubs
    pause(1)
    scene bg int_clubs_male_day with dissolve
    play ambience ambience_clubs_inside_day fadein 3
    "The door creaked, letting me in."
    me "Slavya?"
    "At first glance, there was no one in the room."
    th "And then what about what she said about being irresponsible and all that stuff?"
    "But only at first glance."
    "It was worth noting that the sliding staircase to the attic - it would be about time it was boarded up a hundred times - was open and down."
    if alt_day6_sl_cl_shirt:
        play sound sfx_scary_sting
        "My heart gave me a tingle."
        "Right beneath it, resting her head awkwardly on a table leg, lay..."
    else:
        "And it was only the board that caused me to still not see the most interesting piece of the picture."
        play music music_list["gentle_predator"] fadein 3
        scene cg d6_sl_zettai_7dl with flash
        "From the hole leading to the main problem of the local camp, one could see someone's bare legs!"
        "Of the most pleasant topology."
        "And that tan is golden - without even looking up, I could already tell by the legs alone who had climbed where they shouldn't have."
        "Of course, I couldn't resist - I snuck up close and..."
        play sound sfx_door_squeak_light
        sl "Semyon, I heard you! And I know what you're going to do!"
        "A laugh came from above."
        me "I wasn't going to do anything!"
        "Offendedly I replied."
        th "I had the purest of motives!"
        me "What are you standing there for?"
        sl "I want to close the hatch so no one can get in here."
        me "You're taking a long time!"
        sl "Yeah, you know... It's a feeling."
        "Her voice trembled."
        sl "As if something is keeping me away."
        th "Well, Sanich, you fucking Fixer!"
        me "Threatening, huh?"
        "I made a completely useless clarification already and got a depressing reply."
        sl "Yeah."
        me "You know, why don't you come on down and we'll just lock the..."
        stop music
        play ambience ambience_7dl["explosive_post"]
        scene
        $ renpy.show("bg int_clubs_male_day", what = Noir("bg int_clubs_male_day"))
        with flash
        pause(2)
        scene
        $ renpy.show("bg int_clubs_male_day", what = Dawn("bg int_clubs_male_day"))
        with diam
        "I didn't get a chance to finish my sentence."
        if not alt_day4_sl_cl_tut_iz:
            "Because I heard a painfully familiar sound-not a sound, a sensation-not a sensation..."
            "But it made me sick and want to crawl into a dark corner somewhere."
        "Slavya, who was also beginning to say something, fell silent halfway through."
        "And collapsed like a stone."
        play sound sfx_bodyfall_1
        th "Intolerance."
        "Was my last thought before she rolled down the stairs."
        scene black with fade
        play ambience ambience_clubs_inside_day
        "The residual effect knocked on my brain pretty damn good."
        if alt_sp < 4:
            "And I froze, watching as Slavya, by some miracle, missed me in midair, with all her might..."
            "...slammed into the floor."
            play sound sfx_table_hit
            "The knock came out kind of wooden."
            "A very, very bad knock."
        else:
            "But from somewhere came the strength to take one more tiny step."
            "Tiny - but enough for Slavya to fall..."
            "Right on top of me!"
            play sound sfx_fall_wood_floor
            "All I could manage was to frightenedly say «aw, shit» — and regroup a little, trying in vain to save my long-suffering head."
            "The bear saves Masha's life again."
            "Or - don't swerve into the kitchen, there's a hard refrigerator in the kitchen! Slow down on Semyon, Semyon is soft, he'll forgive."
            "I was lying in the dark on something hard, trying in vain to re-learn the difficult science of breathing."
            "And on top of me lay someone heavy."
            "Someone…"
            with flash
            show unblink
            pause(1)
            scene cg d4_sl_lookup_7dl
            with flash
            voice "…wake up! I can't just carry you away!"
            voice "Why are you so heavy!"
            "Rustle."
            voice "No, I should have picked someone flimsy and small."
            "Rustle."
            voice "But nooooo, I just had to fall in love with a pole like that!"
            me "Gh…"
            sl "Semyon?"
            show unblink
            show blackout_exh2
            with flash
            me "Am I in hell yet?"
            "I asked the angel peering anxiously into my face."
            sl "Semyon!"
            "She shook me."
            sl "Semyon, wake up."
            "The cloudy fog slowly receded."
            show blinking
            hide blackout_exh2
            me "Slavya, how am I here?"
            sl "Well..."
            "She blushed."
            sl "You caught me again."
            me "Bad tradition."
            "But at least I didn't have a headache this time, saving a useless limb is good enough."
            sl "Get up."
            "The girl got off me with obvious reluctance and held out her hand to me."
            scene bg int_clubs_male_sunset at zenterleft
            show sl normal pioneer at cleft
            with dissolve
            "Either the buzzer shut up, or was it just the hatch slamming - but I didn't feel the thing that mowed us down in one volley anymore."
            th "That's good."
            me "Looks like there's some sort of defense mechanism."
            "I said, picking up the keychain Slavya had dropped off the floor."
            me "If someone comes close, they must get uncomfortable, unsettling."
            "I closed the lock and double checked it."
            "Checked it properly so no one would get in for sure."
            me "It would scare a normal person off - who's to blame for you and me being such mutants."
            show sl serious pioneer with dspr
            sl "Don't call me names!"
            "The girl sparkled her eyes angrily."
            me "But it's true - the whole scheme is well thought out, designed for a normal person."
            me "And it didn't work for us - make conclusions for that."
            show sl smile2 pioneer with dspr
            sl "I could only conclude that the brave knight was rescuing his lady again!"
            "She chuckled."
            sl "And such bravery deserves a reward."
            show sl smile pioneer close with dissolve2
            sl "Close your eyes."
            "Taking one long, gliding step, she was beside me."
            "I even got a little startled by the surprise."
            "Not as much as when she tried to fly, of course."
            "But I closed my eyes obediently."
            "And immediately I felt her near me - not the warmth or the difference in electrical potentials, as people usually feel the close presence of someone."
            "But rather, the sweet sensation I felt only here yesterday - the warming positive involvement of someone close by, a kind of affectionate sunshine shining for you alone."
            "Of course, I tried to grope her."
            "Of course I got hit on the hands."
            play sound sfx_punch_medium
            with vpunch
            sl "Listen, Semyon."
            stop music fadeout 3
            "Slavya tried to speak angrily, but for some reason she couldn't do it."
            "It must have been because all this time she was trying unsuccessfully to fend off my advances."
            sl "That's enough, huh? I'm not going anywhere, I promise!"
            play music music_list["confession_oboe"] fadein 5
            scene black with fade
            if alt_day5_sl_cl_hentai_done:
                me "As if you'd be able to go."
                "I grumbled, wrapping my arms across her body and pulling her against me, the way girls on the subway are usually pressed against me during rush hour."
                "Yes, these fragile creatures always suffer from crowding far more than anyone else."
                "And there's nothing strange about that - because the pressure is the same on everybody, and they have less carrying capacity, less resistance."
                "That's exactly the point. {w}And it's not that it's so much nicer to snuggle up to a young calf than it is to snuggle up to a 100-kilo fatty."
                "Slavya was still babbling something, but I was already getting close to her neck, and all I was worried about was possible uninvited visitors who might come in while I was getting my little revenge."
            else:
                me "I'm sorry, I can't resist."
                "I pulled her to me."
                "She was whispering something, either trying to convince me of something or, on the contrary, to make me go on."
                "And then somehow, all of a sudden, she went limp."
                "I think she realized that sometimes it's easier to relax and enjoy a few minutes of pleasure than to fight back for ten minutes."
                "She arched when I got to her neck."
                "And avenged all the millennia of deprivation, oppression, and abstinence."
                "She bit her lip, pressing a groan into her chest, but it never worked that way."
            scene black with fade
            "Dancing on the bones of the end of the world."
            "A feast during the plague."
            "We just almost fell victim to a mind destroyer again, almost both of us breaking our heads in the fall."
            "How did we react to that?"
            "Right. We made love."
            "Or rather, that's what Slavya thought."
            "And I stopped at the very moment when her breath was offset and the shivers ran down her shoulders."
            "And left her like that."
            "Sometimes it's good to let a girl feel the state you're in."
            scene
            $ renpy.show("bg int_clubs_male_sunset", at_list = [zexitcenter], what = Noon("bg int_clubs_male_sunset"))
            show sl sad pioneer
            with dissolve
            sl "Hey, and why did you stop?!"
            "She was expectedly angry."
            me "No reason."
            "I shrugged my shoulders."
            me "I thought I heard footsteps."
            sl "What footsteps, come here!"
            "Uh-huh."
            stop music fadeout 3
            "I bounced back a step."
            me "I mean it! Slavya, get a grip, you're always thinking of just one thing!"
            sl "Arrr..."
            play music music_list["your_bright_side"] fadein 5
            "The girl stood up, adjusting her uniform and sizzling me with her gaze."
            sl "You can't mock a person like that!"
            "She listened."
            sl "There's no one there. {w}You lied?"
            me "No."
            "I shook my head lightly."
            me "I must have heard it!"
            show sl serious pioneer with dspr
            sl "Semyon!"
            me "I was scared, honestly."
            show sl sad pioneer with dspr
            sl "You're lying. {w}And we both know it."
            play sound sfx_close_cabinet
            pause(1)
            "She went up on her toes, checking the unfortunate door to the attic - cutting off any concerns about what was in there."
            "Locked, that's it."
            "There were bigger issues right now."
            show sl smile pioneer with dspr
            "A few breaths and exhales, and the perfect girl I'm used to is looking at me again."
            "Not a trace of dissatisfaction or desire in her gaze."
            "The familiar doll-like greeting smile, the long braid - only the size of the shirt had changed from the first day."
            "Now it fit perfectly, like a second skin, showing all the essentials."
            "Shapewear is a fearsome weapon in capable hands!"
            dreamgirl "Look, she's gotten pretty good at dealing with her own urges, just putting her frustration aside!"
            dreamgirl "She's pretty friendly with her body!"
            th "What do you mean?"
            dreamgirl "Ask her if she happens to have an inner companion like me."
            dreamgirl "We could exchange experiences."
            th "Go on, mock me more."
            show sl normal pioneer with dspr
            sl "Did you bring the list?"
            "She finally remembered our business."
            "I nodded and pulled a piece of paper from my pocket, scrawled in a Japanese girl's round handwriting."
            hide sl with fade
            "It's nice to deal with collected and organized people after all!"
            "On the personal side, Miku may not have been perfect."
            "But when it came to equipment, here her perfectionism went to unprecedented heights."
            "The amplifier and the console were in a cabinet, one on top of the other, connecting into a single system."
            "The cords and plugs were in two bags, also signed - separately for the speakers, for the mic-machines, and separately for the power supply."
            "Take it away and hold your concert."
            me "With that attitude, it's a wonder there's so few concerts around here."
            "I grunted, unbending with the amp and the console in my hands."
            show sl smile pioneer with dspr
            sl "To tell you the truth, Miku wanted to hold concerts every other day - she said she was bored to sit in the club, and it was not a lordly occupation to clean up the grounds."
            sl "And Olga Dmitrievna thought that no one needed concerts so often."
            sl "You know how much we argued! Ugh!"
            "Slavya smiled, evidently recalling the heated filibusters of both sides proving something to each other."
            me "Too bad, of course. I don't know if Miku has any friends, but she seems to be pretty lonely in her club."
            show sl normal pioneer with dissolve
            sl "When I suggested she take over the small kids so she wouldn't feel so sad - you know what she told me?"
            sl "In her usual style - verbose - that she wasn't that starved for company."
            "After running through the list of necessities one more time, she picked up the bags of wires from the floor and headed outside."
            stop ambience fadeout 6
            "That's where we got intercepted."
    stop music fadeout 3
    with fade
    return

label alt_day6_sl_cl_kgb:
    scene bg ext_clubs_day with dissolve
    play ambience ambience_camp_entrance_day fadein 3
    play music music_list["just_think"] fadein 3
    voice "Semyon! Slavya! Wait!"
    "We looked around - the same old man who had reprimanded Sanich and our director before lunch was running in our direction from the very gate."
    $ meet('voice', 'Old man')
    "Apparently, a very important person."
    me "I'll do the negotiating."
    "Without parting my lips, I informed her."
    "Slavya nodded and stepped behind my back."
    show sl normal pioneer far at fleft
    "The old man, noticing our evolutions, instantly froze up and reassuringly put his open palms out in front of him in an international gesture of peace."
    "Only I've heard enough to not believe absolutely anything he has to say."
    voice "What are you, really? I'm just talking!"
    me "Speak."
    "I permitted him, still hiding behind the amplifier, and hiding Slavya behind me."
    voice "As I learned, you're the only ones who've walked through the tunnels."
    if not alt_day4_sl_cl_tut_iz:
        voice "And you, Semyon, also survived an infrasound attack."
    voice "You're very, very interesting guys, and I'd like to cooperate with you."
    me "What do you mean?"
    "The old man looked around to see if anyone could hear, and lowered his voice."
    voice "A fair exchange: your information in exchange for my protection."
    me "And then what do we do with it? With your protection?"
    "The old man smiled:"
    voice "For starters, I'll introduce myself."
    voice "My name is Anatoly Ivanovich, and I'm the immediate superior of your gym teacher, back on the mainland. {w}You can call me that."
    me "Pleased to meet you."
    "My tone contradicted my words."
    voice "You shouldn't be so skeptical, boy. {w}Some things I can do after all."
    voice "For example, I could help Slavya with her college admission."
    if (alt_day2_walk == 2) and (not herc):
        voice "I mean, any kind, period. {w}I heard you were thinking of becoming a lifeguard?"
        voice "You could go into SAR, but you'd have to be a marine. Or a mountain rescue dog handler."
    else:
        voice "If you want, you can even go to our school of state security."
        voice "Because I've heard of her wanting to help everyone in the world - that's where you can start."
        voice "You'll have to be a border guard with a dog first."
    "His voice became ingratiating."
    voice "You like dogs, don't you?"
    if alt_day5_sl_cl_hentai_done:
        th "He knows something about Pirate."
        "With the desperation of a doomed man I realized."
    show sl scared pioneer far at left with dissolve
    "Slavya gulped loudly."
    sl "Y-yes..."
    voice "Then let's cooperate and part satisfied with each other."
    sl "But why me?"
    voice "We have a practice of vetting candidates from high school. You're a good one."
    sl "No, I meant why just me? {w}What about Semyon?"
    "Anatoly laughed:"
    voice "That's why your curator adores you - you're a total no-strings-attached, you don't think about yourself at all."
    show sl serious pioneer far with dspr
    sl "That's not what I asked."
    voice "Okay, no kidding."
    "The old man broke off laughing."
    voice "You really don't know who your chosen one is?"
    th "Oh! Another one with revelations! Well, let's hear, what's my legend here?"
    dreamgirl "Are you betting on the ambassador's son, or does anyone here know about your evolutions?"
    th "How would they know?"
    dreamgirl "No clue!" with vpunch
    show sl normal pioneer at left with dissolve
    sl "A very good man."
    "In a ringing voice the girl replied."
    sl "That's the most important thing!"
    voice "He didn't say?"
    "He winked at me."
    voice "What a bug you are, Sem Semych!"
    me "I said as much as I needed to."
    "I muttered, taking my time revealing my cards - the gambit with the ambassadors' kin is still a work in progress."
    voice "But tell me first - what you saw - and leave all questions for later."
    me "We don't know yet if we can trust you."
    "I grimaced - I was still a little shaken by the feeling of a millimeter of threat that had slipped by."
    voice "My boy."
    "Anatoly sighed sadly."
    voice "It should be enough for you that I am the boss of your much-loved Boris."
    voice "But you already guessed that, when you were eavesdropping under the windows."
    th "Another omniscient, omnipresent, omnifuc… {w}Why did you yell like that if you knew about it??"
    "I wasn't even surprised anymore. I'm used to the fact that everyone around here is 'over the top'."
    voice "So you can trust me - me specifically - completely. {w}Because if anyone but me finds out about where you've been and what you've seen..."
    "He held out a pause."
    "Slavya was silent, waiting for him to continue - she wasn't smiling, but she didn't look particularly worried, either."
    "And my face has had the expressiveness of the lower third of an oak door all my life."
    voice "They'll steal you away and torture you under scopolamine until you tell them everything."
    voice "The same Americans, by the way."
    voice "Slavya, of course, sooner or later will just be killed with subsequent dissolution of the body in sulfuric acid."
    voice "But you, my boy, are in danger of getting caught up with them. {w}And you know why. Am I right?"
    stop music fadeout 3
    "As long as he put it that way..."
    "Here I should have played the hero and said, «what if I gave you the middle finger and you gave me my legitimate phone call in return?»"
    "Or send him away in the most florid way possible?"
    "And then sit the hottie in front of me on the chopper and drive off down the highway into the sunset."
    "Too bad I'm not a hero."
    play music music_list["into_the_unknown"] fadein 3
    scene anim prolog_1
    "I nodded at Slavya and began to tell."
    "Everything I could remember. {w}Everything I could say without touching my two main secrets: my origins."
    "And the inner voice - an interlocutor-protector."
    dreamgirl "Ah, thank you, dear! It's always nice to hear a few warm words in my address."
    if alt_day4_sl_cl_tut_iz:
        "About a dream with exoskeletons and robotic systems and future war."
        "Slavya turned pale when I got to the episode where she shot me, but said nothing."
        "Nodded understandingly, apparently agreeing with some of her conclusions."
        if not alt_day5_sl_cl_hentai_done:
            "About the second dream - a continuation of the first, where I, with the help of painkillers and someone's mother, am relatively alive, with a few bullets in my belly, shambling into the tunnels and making a bit of a mess there."
            "And in the northwestbound escape pod, a short-haired, blue-eyed girl in a reconnaissance jumpsuit is choking on her sobs."
    else:
        "About the reaction to the techno-curtain, about how I tried to turn it off and ended up making it even worse."
        "I didn't forget to mention that it worked even now - but Ivanych brushed it off, confirming my assumption that it also worked as a rodent scarecrow."
        "About some voices Shurik heard, and as a result the bespectacled man had to be found."
    "About the tunnels, the snarks that inhabit them, and the strange sensations in the air."
    "About the center room and its strange interior."
    if not alt_day4_sl_cl_tut_iz:
        "I also remembered to mention that the impact of this interior was extremely similar to that of the «buzzer»."
        if not alt_day5_sl_cl_hentai_done:
            "And, of course, the way I opened my eyes at the very doorstep of this cave."
    "Talking and talking and talking and talking, I couldn't shut up."
    "«Drive like you stole this car», Americans say — and felt something like this: with the brakes failing."
    if alt_day4_sl_cl_tut_iz:
        "In some places I even got dangerously close to forbidden subjects."
        "For example, describing the way in which I overcame the obsession of the abyss."
        "At the last moment, I realized and crumpled the narrative, mumbling that I was just getting it together properly and reminding myself that it was all an illusion."
    "The old man snickered skeptically, but said nothing."
    "And I kept talking."
    "I don't know how long my adventurer's confession lasted, but at least half an hour for sure."
    "We managed to move to a bench near the clubs and sat there while I talked."
    "Miku must have been waiting for us - she'll be swearing..."
    voice "Well."
    "Said the old man when I was done."
    voice "You didn't see anything particularly interesting."
    voice "Too bad, I thought you had more potential."
    me "What are you talking about? Should we have dived into that fog?"
    "Anatoly shrugged."
    voice "What do you think?"
    voice "But you do realize that everything you've seen relates to national security, right?"
    voice "So you'll have to sign a non-disclosure agreement, you know, some things can't be taken out."
    "Slavya nodded understandingly, and I burst out laughing."
    scene bg ext_clubs_day at zenterright
    show sl normal pioneer at cright
    with dissolve
    voice "Of course, Semyon, this agreement will apply to you only for as long as you stay in the country."
    show sl serious pioneer with dspr
    sl "I'm sorry, I don't understand."
    "Slavya frowned."
    sl "I mean, I heard that his parents work at the embassy, but..."
    voice "I mean, not the country, of course."
    "Dry man smiled broadly."
    voice "I'll tell you a terrible secret, Slavya. You see, the thing is, your boy isn't exactly... How shall I put it..."
    dreamgirl "Moment of truth."
    sl "How?"
    voice "He — is a person of confluxed reality, PCR, if you shorten it."
    voice "Simply put, an alien from another world."
    dreamgirl "Shit. And yet he knows."
    th "Surprised they haven't taken us to the lab for experiments yet?"
    dreamgirl "No. That's understandable - we're far from the first ones here, the intelligence services have already had time to satisfy their curiosity."
    "Slavya smiled politely, but her upbringing prevented her from twirling her finger at her temple."
    show sl smile pioneer with dspr
    sl "Semyon, of course, is a little out of this world, but what an alien he is!"
    "Slavya laughed."
    sl "He's got his arms and legs in place."
    if alt_day5_sl_cl_hentai_done:
        show sl shy pioneer with dspr
        sl "And everything else, for that matter."
    voice "He's the same kind of man, sweetheart. {w}But he comes from a world away from us."
    "He glanced at his watch for some reason."
    voice "A few decades from ours. Not exactly in our history, either."
    "I stood and watched in silence as my cover was blown to pieces."
    th "And here he was scaring me with American enemies."
    "You don't need any enemies with friends like that."
    show sl surprise pioneer with dspr
    sl "Semushka?.."
    "Slavya turned to me confusedly."
    me "Delirious. {w}A junkie, I guess."
    "I replied nonchalantly."
    "I really wanted to panic and scream that it wasn't true, that my old world never happened, it was just a dream and all!"
    "But at all times the best way to disprove an unpleasant truth has remained laughter."
    "Inflate any aspect to the point of grotesque, and no one will believe anything else, no matter how plausible it is."
    "It's an old psychological trick."
    me "Now it'll turn out I've got a flying saucer hidden in the woods."
    me "Ah, no, I'm lying. «Icarus» — that's the saucer. But how could it be - after all, Olga Dmitrievna came on it with me."
    me "Really?!"
    "I closed my mouth and goggled."
    me "So Olga is an alien, too! Shock!"
    "Watching the whole pantomime, the old man laughed:"
    voice "I admire your stamina, Semyon."
    "He turned to Slavya."
    voice "But you, sweetheart, probably understood why we're offering the job only to you - we can't hire a man who can disappear at any moment."
    "I sat back, leaning back, and from under half-closed eyelids lazily watching the play of glare on the surface of the gate."
    sl "What do you mean «disappear»?"
    voice "We don't know very well the mechanism that allows such people to come to us, but they are here as if in a dream - which means that a strong experience or death can... {w} Ahem… Force him to «wake up»."
    voice "After that, he'll be home."
    voice "Once again I admire your courage in committing yourself to such a fickle man. {w}Fickle. What a good tautology."
    "The old man rose."
    voice "After the camp sign the agreement, Slavya, and next May I expect you with the papers. {w}I'm not waiting for Semyon, he'll probably be gone by then."
    voice "Goodbye. {w}And, Slavya."
    "Dry man turned around."
    voice "If you really like dogs - I'd check one out. I think I heard some yapping coming from the back of the canteen."
    $ meet('voice', 'Voice')
    "He left."
    "A few seconds later, an engine roared from behind the gate - Anatoly Ivanovich drove off on his safe business."
    "And he didn't care that he had just ruined my happiness in passing. Freak."
    "I turned my head painfully slowly, preparing to argue, challenge, prove and convince."
    stop music fadeout 3
    stop ambience fadeout 6
    return

label alt_day6_sl_cl_pirate:
    scene bg ext_clubs_day at zenterleft
    show sl scared pioneer at cleft
    with dissolve
    play music music_7dl["beth"] fadein 1
    "Slavya looked at me with a mixture of anxiety and horror."
    me "Slavya, I..."
    sl "Pirate!"
    "She jumped up and ran somewhere."
    if alt_day5_sl_cl_hentai_done:
        th "To the canteen, to the shelter of her pup."
        th "Did he..."
        "No, I didn't even want to think about it."
    else:
        "Without a second's hesitation, I rushed after her."
        "Wherever she was going, the case would have been extremely important."
    scene bg ext_clubs_day:
        linear 0.1 pos (-5,-5)
        linear 0.1 pos (0,0)
        linear 0.1 pos (5,5)
        linear 0.1 pos (0,5)
        linear 0.1 pos (5,0)
        linear 0.1 pos (0,0)
        repeat
    "We ran as if someone else's life depended on our running."
    "Quite possibly ours."
    scene bg ext_square_day:
        linear 0.1 pos (-5,-5)
        linear 0.1 pos (0,0)
        linear 0.1 pos (5,5)
        linear 0.1 pos (0,5)
        linear 0.1 pos (5,0)
        linear 0.1 pos (0,0)
        repeat
    "Not a question of existence, but a question of being - will there ever again appear on those full lips that welcoming smile I once fell in love with?"
    scene bg ext_dining_hall_away_day:
        linear 0.1 pos (-5,-5)
        linear 0.1 pos (0,0)
        linear 0.1 pos (5,5)
        linear 0.1 pos (0,5)
        linear 0.1 pos (5,0)
        linear 0.1 pos (0,0)
        repeat
    "I was already exhausted and beginning to give up, but the memory of Slavya's look of hopeless longing gave me strength."
    if alt_day5_sl_cl_hentai_done:
        "I wouldn't want anything to happen to Pirate myself, but for Slavya it was a matter of life and death altogether!"
    scene bg ext_dining_hall_near_day:
        linear 0.1 pos (-5,-5)
        linear 0.1 pos (0,0)
        linear 0.1 pos (5,5)
        linear 0.1 pos (0,5)
        linear 0.1 pos (5,0)
        linear 0.1 pos (0,0)
        repeat
    "After running diagonally across the yard, we stopped at the locked doors."
    scene bg ext_dining_hall_near_day
    with flash
    "For a long, long time Slavya could not get the key into the lock - her fingers trembled so much."
    "But at last the last obstacle was overcome..."
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene
    $ renpy.show("bg int_attic2_day_7dl", what = Dawn("bg int_attic2_day_7dl"))
    with flash
    sl "Pirate!"
    "I went blind in the dark room after the bright sun."
    "And when my sight came back to me, I could already see Slavya on her knees, cradling a puppy to her chest."
    if not alt_day5_sl_cl_hentai_done:
        "White-white, more like a bear cub than a dog."
        "I knew that breed."
        "Because all children lose the lion's share of their childish charm when they grow up, but Samoyeds were the happy exception to that rule."
        "They were charming as hell, even growing up."
        "An icon of harmony, strength and beauty."
        "And a puppy of such a breed was now held by Slavya."
    "His paws were moving involuntarily, there was some gurgling coming from his throat."
    "And there was a semi-recognizable smell in the warehouse…"
    th "The smell of arsenic?"
    me "Slavya?"
    scene bg int_attic2_day_7dl with flash
    me "Listen."
    "She kept swinging, cradling Pirate in her arms."
    me "Hey!"
    play sound sfx_face_slap
    "I slapped her lightly, bringing her to her senses."
    show sl cry pioneer with dspr
    me "Slavya, can you hear me?"
    "She nodded slowly, looking through me."
    "In the corners of her huge blue eyes there was already a trembling realization of the inevitable."
    me "Look, maybe not all is lost yet."
    th "Can she even hear me?"
    sl "While we were talking, he was lying there."
    "Calmly she said."
    sl "Lying there and... {w}And I didn't feel a thing."
    "Slavya, the same Slavya I knew an active and busy girl, knew she couldn't do anything now."
    me "We should take him to the doctor, maybe she can do something."
    sl "But she's a nurse..."
    me "It's better than sitting here crying."
    "I shook her up."
    me "Get it together, let's go! {w}There's no time to lose!"
    "Slavya nodded and got up."
    play sound sfx_open_door_kick
    pause(1)
    scene bg ext_dining_hall_away_day at zexitleft
    show sl cry pioneer at cleft
    with dissolve
    play ambience ambience_camp_center_day fadein 3
    sl "If only it would all work out, if only it would all work out."
    "Slavya incoherently repeated."
    "The atheist generation knows no other prayers."
    scene bg ext_square_day with slideawayright
    "At least I have Random - almost Hermes Trismegistus, only with a formula instead of a face."
    "Now it didn't matter if anyone found out about the animal's presence in the territory."
    scene bg ext_aidpost_day with slideawayright
    "What was more important was to make it in time, and maybe... {w}Not jinx it!"
    stop ambience fadeout 3
    play sound sfx_open_door_strong
    pause(1)
    scene bg int_aidpost_day at zenterright
    show cs normal at right
    with dissolve
    play ambience ambience_medstation_inside_day fadein 3
    "Viola was at her place."
    "She aristocratically arched an eyebrow in an expression of amazement, but said nothing, immediately placing Pirate on the couch and rushing around him."
    "Of course, she wasn't a vet. {w}Even here she was in the position of a nurse, since her profile was the human psyche, not the human body."
    "But she had been taught something, some general basics?"
    "We knew even less."
    show blinking
    cs "I gave him some ipecacuana syrup, he should throw up a little."
    "She reported."
    cs "But you have to understand that you need a vet for full help. {w}And urgently, very urgently. Otherwise it's all for nothing."
    scene bg int_aidpost_day at enterleft
    show cs normal at right
    show sl cry pioneer at left
    with dissolve
    sl "Maybe you could..."
    show cs shy with dissolve
    cs "Kiddo."
    "Viola shook her head."
    cs "Urgent means within the next two hours. {w}If I drive you right now, the dog will die in your arms in the car."
    cs "It's an objective fact."
    "The non-joking, non-ironic Viola was overwhelming and intimidating."
    show sl angry pioneer with dspr
    sl "But what to do then!"
    "Slavya's armor was cracking at the seams."
    sl "What?!"
    with vpunch
    show cs normal at fright
    cs "I'm sorry."
    "Viola turned away."
    cs "An injection of lidocaine is all I can do in a situation like this."
    show sl serious pioneer with dspr
    sl "So do it!"
    "The blonde shouted."
    sl "What are you sitting around if you can do anything!"
    me "Slavya... {w} Slavya!"
    "I touched the disheveled girl by the elbow."
    show sl normal pioneer with dspr
    sl "Hhaaa…"
    "With an effort she exhaled."
    sl "What?"
    me "This injection... {w}It'll put the Pirate to sleep."
    sl "Put him to sleep — you mean sl… s…"
    "Her lower lip quivered."
    "Viola nodded."
    cs "Painkiller. {w}He will not suffer."
    sl "Sl…"
    "Like a hysterical girl, Slavya repeated."
    "I nodded my thanks to Violetta and took the puppy and put it in the box."
    "It seems the activist was now resolutely incapacitated."
    $ alt_day6_sl_cl_arc = 'pi'
    stop music fadeout 3
    stop ambience fadeout 3
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg ext_aidpost_day
    with dissolve
    play music music_7dl["gonna_be_ok"] fadein 3
    play ambience ambience_camp_center_day fadein 3
    "We went outside."
    "I was carrying a box lined with an old blanket, on the bottom of which a puppy was breathing restlessly - fearfully, with a wheeze, with a whistle."
    "I got creeped out - I could feel death. Its icy, rotten breath, which I always felt if someone was on my doorstep."
    "Streaming down the back of my neck, pouring down my spine into my heart."
    "I could peep through the keyhole into the afterlife, see everyone who has departed."
    "However, it was no longer me who would turn away from the keyhole."
    show sl serious pioneer with dspr
    sl "Semyon."
    "In a transparent, tinkling tone Slavya addressed me."
    sl "I'm a useless fool. {w} I can help anyone."
    "She took the box from me, pretending that she just wanted to look at the puppy again."
    "A tear fell on the puppy's black nose, and he whimpered without waking up."
    sl "But why can't I help someone I love?!"
    "Slavya fell on the bench, still holding the box."
    "She hunched over helplessly and, without closing her eyes, sobbed."
    show sl cry pioneer with dspr
    sl "Why, Semyon?! What's wrong with me?"
    sl "I want to help everyone, so that everyone has a chance for happiness, for a good life."
    sl "What do I have to do to make sure Pirate has it? Or what am I doing wrong?"
    "I patted her on the head."
    me "That's right."
    th "Why don't I know what to say in cases like this!"
    "Why don't I know how to say that not everything depends on the effort put in?"
    "That everybody dies. {w}That now you have to get over it and..."
    "Yeah. Let Pirate die."
    "That we can be merciful and let the nurse give him an injection of painkillers so he can go away light and painless."
    "Because we really are responsible for those who weren't sent to piss off in time!"
    scene
    $ renpy.show("bg ext_aidpost_day", at_list = [zenterleft], what = Dawn("bg ext_aidpost_day"))
    show sl sad pioneer with dspr
    with dissolve
    me "It's just our bad luck."
    "I didn't say what I thought I said at all."
    me "Especially his. I should have run right over here when he asked about the dog."
    sl "But there must be something we can do now?! {w}Something!"
    "Slavya looked up at me with no hope in her eyes, only a blind reluctance to fold her paws."
    th "Put the puppy out of its misery."
    sl "Why don't we risk it and ask Viola to take us to town? {w}It's better than sitting here!"
    me "It won't work. She said it had to be quick."
    "She fell silent, continued to swallow the tears running down her cheeks."
    "The person who doesn't know how to give up broke down."
    "A person who wanted to love and help the world."
    "A person I love for it."
    "Struck by a sneaky blow, called 'Coup de grâce' by some vain freak."
    "And I, exhaling, remembering yesterday, realized that I didn't want to let her cry now or ever again."
    "So now that she's given up, I'm obliged to hold on to both of us."
    "I can't give up."
    "I can't."
    me "Listen, Slavya."
    "I turned to the shuddering head."
    me "Sitting here crying won't make anyone feel better. {w}Hear that?! And time is running out!"
    sl "But what to do?"
    me "I... I don't know. {w}Maybe we could go to the library and look at the veterinary books there?"
    sl "You know that's nonsense."
    show sl cry pioneer with dspr
    "Her eyes were swollen and red."
    "She was shaking all over."
    me "But then... {w}Then..."
    "I suddenly had a thought that made me shake all over."
    "A simple and frighteningly creepy thought."
    me "But there is a way."
    "Slowly I said."
    sl "Yes?"
    "There was so much hope in the eyes raised at me that I forbade myself to doubt."
    me "There is one way... To save Pirate. {w}Remember what Anatoly Ivanovich said?"
    sl "About school?"
    me "About me."
    sl "Some nonsense, as if you were from another world."
    "She said it in a way that made me understand: she didn't believe it one bit."
    sl "But it's nonsense, isn't it?"
    "She laughed hysterically."
    sl "You have two arms, two legs, a head. {w}Even the rest of your limbs are in place. How can you..."
    me "It's true. {w}I really am from another world, Slavya."
    "We need to get to the vet very quickly. Very quickly, not in five hours of jolting by car."
    sl "Even if you are - how would that help us?"
    me "I can go home, you know?"
    sl "I don't believe that. But even if you do, how will you take him with you?"
    "I shrugged it off:"
    me "I came to myself dressed in what I was wearing in my world, in my pockets was what I had in my world."
    me "So -"
    "I smiled desperately."
    me "I can take him with me if I try really hard."
    me "And he'll get help there. We have pretty good vets."
    show sl normal pioneer with dspr
    sl "And we..."
    me "We'll have to break up, temporarily or permanently. I don't know."
    "I nodded."
    me "I got here in a strange, miraculous way, but I don't know if I'll be able to come back."
    show sl serious pioneer with dspr
    "Her eyes grew huge, and for a second the boundless, splashing grief even disappeared from them."
    "But only for a second. {w}She bit her lip."
    sl "So Pirate's life and the fact that I will never see him either - is the price for our happiness?"
    me "Yes."
    sl "But can't you take me with you?"
    "I doubt the two of us would survive in my world. {w}The more so because it takes a very sharp, slashing reaction."
    "Not the kind that a dying puppy would cause - I'm not that fond of dogs."
    "So the only way to get it..."
    sl "And what, just let it go, that's all?!"
    show sl angry pioneer with dspr
    "She bit her lip."
    sl "I can't do that."
    sl "You can't, you have no right to make me choose between such things, do you hear me, you?!"
    me "Slavya..."
    sl "How can you?! Don't you understand that it's inhuman to do that?!"
    sl "I don't want to. {w}I want both you and him. No, there must be another way."
    me "Teleporting into town? Slavya, we won't make it by car! {w}Do you hear?"
    dreamgirl "I have bad news for you."
    th "Yeah?"
    dreamgirl "Actually, it's from a blocked memory area - you know, so you don't get depressed here while you're in camp."
    th "Closer to the topic."
    dreamgirl "Well... Anyway, you died there, back home."
    if loki:
        dreamgirl "More accurately, dying right now from multiple internal injuries, blood loss and hypothermia."
    elif herc:
        dreamgirl "You have a bullet in your head, two of them. They're making their way through the bone of your skull right now."
    else:
        dreamgirl "Swallowing ice-cold water, folding your legs, you go down with the 410 bus."
    th "I know."
    dreamgirl "That's why you... What?!"
    th "That fog, remember? Dream. Anyway, I remember everything that happened to me."
    dreamgirl "And you're still going?!"
    th "Yes."
    th "Even if I only have a few seconds, it should be enough."
    th "You can still stretch for a long time, but not indefinitely. {w}And here at least I'll be doing someone some good."
    show sl cry pioneer with dspr
    "I shook her, bringing her to her senses."
    menu:
        "Slavya, no time to choose":
            "I hurried her up. It really did count down to minutes."
            $ lp_sl += 1
            $ alt_sp += 1
        "Don't you think of giving up!":
            me "If you're going to get all mushy now, we're not going to make it!"
            $ lp_sl += 2
            $ alt_sp += 2
            $ alt_day6_sl_cl_int = 1
        "I'll definitely come back for you":
            $ lp_sl -= 5
            if loki:
                $ alt_day_catapult = True
            "I was all twisted up from the blown falsity of that phrase."
            "It's hard to lie to someone you love."
            "Especially if you're going to leave him."
    if alt_day_catapult:
        sl "But..."
        sl "Isn't there any other way..."
        me "As you can see."
        sl "Now. Give me one more second."
        "She wiped away her tears with the back of her hand and, setting the puppy box aside, hugged me gustily, clutching as hard as she could. She was pounding."
        sl "I'll be... {w}I'll really be waiting."
        "She whispered."
        sl "All my life, if need be. {w}And one day you'll come back."
        "I wish I could hope."
        sl "What do you have to do now?"
        me "Nothing. {w}It just takes a strong emotion."
        "It's just come to me that it's all real. {w}That six days were about to end on a minor note like this."
        show blackout_exh with dissolve2
        me "And we're breaking up. {w}What could be stronger."
        sl "We're not breaking up."
        "She whispered."
        sl "We're just going about our business. {w}But someday we'll meet again."
        show rain_overlay with flash
        sl "I love you, Semyon. {w}Take care of Pirate."
        "She handed me the box and I, hiding from the needle that pricked my heart, clawed at the uneven, slashed edges."
        "The contours of the world were floating, but not because of any of my abilities."
        "Just Persunov Semyon, thirty-something, owl and loner, crying like a little child at the thought of his tale ending."
    with fade
    return

label alt_day6_sl_cl_loki_exc:
    scene
    $ renpy.show("bg ext_aidpost_day", what = Dawn("bg ext_aidpost_day"))
    show sl cry pioneer
    with dissolve
    me "Farewell..."
    "I exhaled."
    stop music fadeout 3
    stop ambience fadeout 3
    $ prolog_time()
    scene bg ext_winterpark_7dl
    show spill_red
    with dissolve
    play ambience ambience_cold_wind_loop fadein 3
    "And I opened my eyes in my world of loneliness and the cold snow beneath the freezing wings."
    "The image was floating and doubling, and something was rolling around very badly inside, but I didn't care right now."
    play music music_7dl["lynn"] fadein 3
    "I got down on all fours and, spitting on the white canvas riddled with size forty-three prints, crawled."
    scene
    $ renpy.show("bg ext_winterpark_7dl", at_list = [sdl_transform13], what = Desat1("bg ext_winterpark_7dl"))
    with vpunch
    "Imagining myself to be either the hero Alexei Maresiev or Joel from «The Shining», or someone else, whose life has turned this way, through the woozy disobedience of the body, the bitter cold, and the blood flooding my eyes."
    "I should have given up."
    scene
    $ renpy.show("bg ext_winterpark_7dl", at_list = [sdl_transform14], what = Desat1("bg ext_winterpark_7dl"))
    with vpunch
    "I should have laid down and died in the snow right there."
    "But now there was a cardboard box sliding in the snow in front of me - I didn't have the strength to get up or carry it in any other way, so I just pushed it in front of me with my head."
    "Step."
    "It's already happened to me once."
    "One more step."
    "It's all been there for me."
    "More..."
    "Only my hand warmed by the warm, uncertain attention of a sad girl with huge green eyes."
    "Or maybe it was a redheaded lightning bolt, scared to tears of dislike?"
    "No, of course not."
    "It was a cheerful girl with impossibly long aquamarine hair, looking from the stage into the audience with eyes full of tears of loneliness."
    "And I left them all behind."
    "I guess Slavya was really desperate, since she decided to resort to such a wild method of salvation."
    with fade
    "Stupid, she thought, there - and right back, make it! Make it!"
    "Where to go back to, if now the entrance fee for seven days of summer is obvious."
    "I stretched out with my face in the ice, hitting my mangled nose."
    "The pain might have been sobering if it had been just a little brighter than all the other pain."
    "The only thing worse is the pain somewhere under my ribs, where no grinder can reach."
    "Because I'm not taking her with me this time."
    scene
    $ renpy.show("bg ext_winterpark_7dl", at_list = [sdl_transform15], what = Desat("bg ext_winterpark_7dl"))
    with vpunch
    "Step."
    scene stars
    $ renpy.show("bg ext_camp_entrance_day", what = D3_intro("bg ext_camp_entrance_day"))
    show prologue_dream
    with dissolve
    "Camp."
    "Step."
    scene stars
    if alt_day5_sl_cl_hentai_done and persistent.hentai_graphics_7dl:
        $ renpy.show("cg d5_sl_moon_7dl", what = D3_intro("cg d5_sl_moon_7dl"))
    else:
        $ renpy.show("cg d1_sl_dinner_day_7dl", what = D3_intro("cg d1_sl_dinner_day_7dl"))
    show prologue_dream
    with dissolve
    "Slavya."
    "Step."
    "Pirate woke up from the cold and whimpered, and I, not knowing how to help him, whispered something soothing, pushing and shoving the box in front of me."
    "I was a rogue, unable to apologize by looking a man in the eye."
    "I was a liar, incapable of honesty and open-mindedness."
    scene
    $ renpy.show("bg ext_winterpark_7dl", at_list = [sdl_transform16], what = Desat1("bg ext_winterpark_7dl"))
    with vpunch
    show blackout_exh3
    with fade
    "I was a nobody, destroying the life's work of a man unlucky enough to take a girl away from me."
    "So I was in full agreement with Asgard's verdict."
    "So I left Sigyun in the past world and appeared at the frontal seat with empty hands and a pure heart."
    "But I would like, as a last wish before my execution, to ask for a small reprieve."
    "I just have to finish what I started."
    scene bg ext_winterpark_7dl:
        xalign .6 yalign .6 zoom 1.3
        easeout .6 xalign .6 yalign .8 zoom 1.5
    with vpunch
    play sound2 sfx_bodyfall_1
    pause(2)
    scene stars
    show snow
    with fade
    voice "Dim, look, what is it?"
    voice "Man, are you alright?"
    "Through the shimmering haze, I could see two black silhouettes leaning over me."
    "Apparently my request was heeded?"
    "Providence might have pushed me the other way, and I would have pushed the box somewhere in a grove, where we would have been found by spring, frozen but dead long before then."
    voice "Don't move, please. I'm a nurse, I'll give you first aid..."
    "They rolled me over onto my back and stopped. Judging by the strangled exclamation, I didn't look like much."
    "Wow, I still have the strength for humor. And not much of it."
    me "Help... P-pirate."
    "I exhaled, finally letting go of my consciousness."
    "And from somewhere above, as if changing the angle, but for some reason without a sound, I saw two figures rushing around, taking a snow-white puppy with a black button nose out of a box, listening to it, grabbing their heads, and grabbing their phones in pairs."
    "Twenty more minutes, and somewhere three hundred yards away at the gate a red and white car barked its siren and was let into the park."
    "Out of it jumped a special team - angels in white coats, saviors of human destinies - into the snow."
    $ renpy.show("cg d7_sl_gonna_be_ok_7dl", what = D3_intro("cg d7_sl_gonna_be_ok_7dl"), behind=["snow"])
    with dissolve
    "Two ran to the scattered body in the snow with a solid bruise instead of a face, another went over to the girl holding the puppy and gently took the animal from her."
    "Listened, looked, nodded encouragingly - nothing he couldn't handle."
    "A simple intoxication is a simple matter for a good vet."
    "Pirate is strong, he's sure to get through it!"
    "And that means - that it all will be okay."
    scene anim prolog_2 with fade3
    "Exclusive ending Loki unlocked - «All will be okay»"
    show blackout_exh
    with dissolve
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("sl_cl_loki_exc")
    show acm_logo_sl_cl_loki_exc with moveinright:
        pos (1600, 1020)
    pause(7.4)
    call alt_7dl_titles
    pause(2)
    return

label alt_day6_sl_cl_ba_help:
    play music music_7dl["uncertainity"] fadein 3
    scene bg ext_square_day at zenterright
    show ba em1 uniform with dissolve
    ba "Actually, if you go fast, you'll make it."
    "A tired bass sounded over my head, and I slowly looked up."
    "Sanich."
    "He's had a rough time of it these last few days."
    "And who among us is without scars."
    "For all my dislike of the man, I had to admit - he worked with children and for children."
    "Not even for his own ego, for that matter."
    "I realized that Sanich was, in fact, not young. {w}Probably the oldest there is in the camp."
    if alt_day5_sl_cl_hentai_done:
        "That's right, Slavya also said he was retiring."
        "For health reasons - but for age, too."
    me "But weren't you taken away?"
    ba "I was. They gave me an hour to pack."
    "He looked around."
    ba "But I turned out to have very few things."
    show ba smile uniform with dissolve
    ba "Are we going? If we're going, let's go."
    "He tossed the key in his hand."
    cs "Boriska, if you scratch my car again, I'll charge you full price!"
    "The nurse's voice came through."
    ba "I'll give it back better than it was."
    "He winked at us and headed for the dining room."
    stop ambience fadeout 3
    scene cg d4_cs_car_day_ba_gl_7dl
    with fade
    play sound sfx_intro_bus_engine_start
    pause(3)
    play sound_loop sfx_intro_bus_engine_loop fadein 3
    $ set_mode_nvl()
    "We were not and are not, we are a void - a mirage. And every new day is the same as yesterday."
    "And right now it's just the constant jolting, the screams of fear from the back seat and the speedometer needle sticking to the 200 mark, and the howl of the forced engine."
    "We were flying over a broken road at a speed not allowed by any rules or regulations."
    "A pure gamble."
    "Which could not be explained by anything but the stupidity of the driver."
    "Or a life saved."
    "Faster, even faster."
    "Along the way we had to dodge sand trucks going somewhere several times, and their drivers hardly had time to realize what was happening as the white meteor approached, howled its engine, and disappeared over the horizon."
    "And I myself, gazing into the asphalt flowing under the wheels, with my own gaze, my own desire, as if I were pinning us to the road, all there already - where there was someone who could help us."
    "And so..."
    "Flitting low over the time-grinded asphalt, racing against death - themselves at the risk of being smashed into a flap every minute."
    nvl clear
    "We got to town in less than two hours."
    "And it was the longest two hours of my life."
    "I'm tired of worrying, tired of being afraid, just tired, and all I want is for it to be over already."
    "But «Volga» already rattles through the city limits, honking its horn and humming its engine, scaring away pigeons and youngsters."
    stop sound_loop
    "The vet was found uptown and we made it to the very end of the shift - they immediately took Pirate away from us and asked us to wait behind a closed door."
    voice "It'll be all right."
    "Promised the debauched veterinarian lady with the kind, tired eyes of a man used to saving other people's happiness."
    voice "You just don't have to look now. I'll call."
    nvl clear
    scene cg d5_sl_bench_neutral_7dl with dissolve
    "The crazy stress of the last few days, the constant lack of sleep, the fatigue..."
    sl "We did it."
    me "Yes. We did."
    "I smiled crookedly."
    "And she put her head on my shoulder."
    "I also thought it would be nice to stroke her hair - damn fetishist."
    "Or at least a kiss on the temple."
    "But I've come such a long way. I even escaped camp with the best girl of this damn reality."
    "So, if you don't mind…"
    nvl clear
    stop music fadeout 3
    return

label alt_day6_sl_cl_home:
    scene bg int_sam_house_clean_7dl with dissolve
    $ set_mode_adv()
    play music music_7dl["misery"] fadein 3
    "I woke up to the monitor turning on and being dazzled by the bright light of the snow-white background of the Skype window."
    "Another bot, who, who knows how he found me on the net."
    "A certain Pussy1337, wanting to show me her dubious charms because she's so turned on by the paper-packet-headed fool in my avatar."
    "All you have to do is follow the link you sent me."
    "Usually I open a bot window next door and copy phrases with it until I get bored."
    "But right now something didn't feel like it."
    "Now there were faces between the monitor and me, people - living, far more real than the reality in which I live."
    "How did I manage to make them up, to see them in my dreams?"
    "I've always had trouble with imagination, I'm a pattern man, an algorithm man..."
    if herc:
        "And then Semyon Sychev"
    else:
        "And then Semyon Persunov"
    extend ", while still necessary and important - hopelessly stuck in the past of a foreign land, Semushka looked up and saw those he loved and hated melting into smoky shadows."
    "Those who he had made up."
    "Leaves Mironova Olga, the counselor, in a panama, in a snow-white shirt with an honors student rhombus, shapely, principled, kind."
    "Boris Kolomiytsev melts, holding Viola Collider by the hand - two streams of smoke, in purple and silver, intertwined in a bluish embrace from the filter side, from the coal side."
    "Gone are Miku, Alisa, Lena, beautiful as the summer sun in the sky of a fantasy camp that never existed."
    "All that's left is Me."
    "Me, sitting in the chair in front of the screen, huddled, hunched over, squinting at the white background."
    "Me, resting my elbows on my knees on the subway, taking me nowhere."
    if loki:
        "Me, watching the snow turn scarlet, waiting for the bony one to close her icy arms."
    elif herc:
        "Me, coughing up the remnants of my reluctance to end so ignominiously, on the dirty floor of a liquor store."
    else:
        "Me, drowning like a blind kitten, and not trying to flutter."
        "For too long I had dreamed of death and thought suicide too great a sin - could I have missed such a splendid opportunity?"
    dreamgirl "So, how's that for an excursion into non-existence?"
    "The sneer in the alter ego's voice could have eaten away at the twin towers' concrete piles."
    dreamgirl "Was there any benefit to your straddling the hottie, or were you just holding her tits?"
    dreamgirl "Don't think I'm picking on you, I'm just wondering what the point of even stepping on the hardest path was if you ended up right back where you started."
    dreamgirl "Though you've got it cleaner here, I see. That's progress, too."
    dreamgirl "Did you clean it yourself?"
    me "Yes. {w}I understood the value of people. It doesn't sound right, though. It's like I'm buying them from the market."
    me "I've come to understand their worth - that sounds better. Each person individually, all together, the collective, the society."
    me "I won't say I loved people, but I learned to appreciate them."
    "I spoke, turning more to myself than to Him."
    "And I didn't know why I was saying it."
    dreamgirl "In other words, you understood what you should have understood back in first grade."
    dreamgirl "Not the most impressive indicator."
    me "But I want to help people."
    dreamgirl "Yeah? And how?"
    if loki:
        dreamgirl "Will you help them a lot on your teacher's dime?"
    elif herc:
        dreamgirl "Will you give them their pay for the last tour of duty?"
    else:
        dreamgirl "Will you go give away your freelance earnings?"
    me "I don't know yet."
    dreamgirl "And who knows? It's a stupid desire to help. You can't help anyone, you can't help yourself."
    dreamgirl "Standard, quick to enthuse and just as quick to cool down, a fool inspired by an example."
    dreamgirl "Fool, hey fool, do you hear me?"
    me "I hear you."
    dreamgirl "Your Slavya will give her life to this, will learn the best way to help people, and she will never have another life but the lives of others."
    dreamgirl "You can't afford that price."
    me "I was there for Slavya when she stopped managing, okay? She was relying on me."
    dreamgirl "Great is the importance of comforting a weeping girl."
    dreamgirl "What good things did you do in that camp, in unrealistic, greenhouse conditions - alluvium for superheroes of all stripes - that you can remember and be proud of five years from now?"
    dreamgirl "Except that you legitimately fell in love and are now really ready to move mountains for her."
    me "Isn't that enough?"
    dreamgirl "Except that love lives for three years, and your Slavya... It's not a fact that she exists."
    dreamgirl "So you got out of the swamp to stand in Slavya's shadow. In the shadow of a nonexistent girl who also sometimes wants a strong male under the vest and «who's the master in the house»."
    if loki:
        dreamgirl "Dedicated your life to petty revenge on a man who turned out to be a bigger man than you."
        dreamgirl "Even took a name for yourself - Loooooki. {w}Cheapskate from the thrift store."
    elif herc:
        dreamgirl "You've spent a lifetime trying to escape the bitter memory of your own defeats."
        dreamgirl "Basically, a few setbacks that should have only made you hardened, made you stronger, but instead made you sit on a stump and cry."
        dreamgirl "A conscript, almost a journalist, almost a musician. Foolish."
    else:
        dreamgirl "All your life you've been running away from a life broken in an accident - and you've came to a new one, a made-up one."
        dreamgirl "Even your vocation is a fool's errand. A squad leader's assistant? Are you serious? Commander of brooms and keys?"
    me "I got better."
    "I was still talking to the shadow in the corner."
    me "I'm not going back to my old life again, do you hear?! I've changed."
    dreamgirl "You survived pioneer camp. Practically went through an incredibly difficult game where the hardest part was not dying of boredom."
    dreamgirl "And now you think there's no judging winners. After all, you're a winner, right?"
    dreamgirl "Dumbinner."
    me "I'll recover at the university, I'll try again, so you won't have to be ashamed of me if you meet me on the street one day!"
    dreamgirl "You carry an aura of failure. You know, like kids who get beaten up by everyone all the time. How do kids know who can and can't be hit? They feel it."
    scene bg semen_room_window with dissolve
    dreamgirl "You chose this noose yourself, you know that, don't you?"
    dreamgirl "Give up and break. And the camp's fuse won't last long."
    dreamgirl "Six months, a year at most. And then one day your Valkyrie will meet you on the street. And she'll turn her back on you because you're unhuman, unshaven, sullen, and you've got hate on your forehead."
    dreamgirl "You are already potentially him. {w}Because you have no one. And your only interlocutor is your schizophrenia."
    "Outside the windows, police carriage sirens bellowed, something heavy rattled upstairs, the tones of a cheap, shrill car alarm came from the next yard."
    "Life went on, flowing through me, overflowing on the icy glass of the insulated windows, which I had never replaced with double-glazed, all my life glued with paper."
    "And I didn't want to go back somewhere anymore, to redo something, to change, to stir, to choose, to create - to hell with it. I was done."
    "And just his truth was all around, an ulcer of sorts: I'm a classic loser in whose life nothing ever happens and won't happen."
    stop music fadeout 3
    return

label alt_day6_sl_cl_intellectual:
    scene black
    play music music_7dl["gonna_be_ok"] fadein 3
    play sound sfx_intro_bus_engine_start
    pause(3)
    play sound_loop sfx_intro_bus_engine_loop fadein 3
    $ set_mode_adv()
    scene anim intro_9
    show prologue_dream
    with fade
    "Crowded in a dark corner and sat there until the bell rang, waiting to be finally released into oblivion."
    "The memory slowly crumbled into weightless ash, driven by the icy December wind."
    "The player died. Phone on its last gasp."
    "But the date is right - December 28, 2018."
    "The first step into the sky."
    "What's next? A red-bellied LIAZ with a soviet pop song in the passenger compartment?"
    pause(2)
    scene anim intro_10
    show prologue_dream
    with fade
    play sound sfx_intro_bus_door_open
    pause(3)
    scene anim intro_11
    with fade
    pause(1)
    stop sound_loop fadeout 4
    scene anim intro_13
    show prologue_dream
    with fade2
    pause(3)
    scene bg intro_xx
    show prologue_dream
    with fade
    "It's funny to feel like a prophet, knowing ahead of time everything that's going to happen."
    "It's like someone has cast a shadow of the future over my mind."
    "And I'm counting the seconds before something happens that I've already managed to subconsciously note - a woman turning, a child jumping, a car alarm going off from a snowball to the windshield."
    "Even the half-torn down advertisement at the junction noted."
    "Okay, but I guess that's all for later?"
    "It wouldn't be a bad idea to just walk to the bus stop first."
    play sound sfx_intro_bus_stop_steps
    pause(3)
    scene anim intro_4
    show prologue_dream
    with fade
    "I didn't know myself what I was doing outside, but for some reason sitting at home seemed sacrilegious."
    "It was as if something overbearing had settled inside me and was pulling, pulling me forward."
    "When? Well, that's a different question."
    "I think it was when the split personality disappeared that I stopped hearing his voice - that is, hearing it at all, inside and out. That's it, my angry, poisonous alter ego has rested in the bosom, prosit!"
    "So I go, trying unsuccessfully to hide from the cold under a coat not designed for this temperature."
    "That's right, that's right, the wimp must suffer."
    scene anim intro_3
    show prologue_dream
    with fade
    "So I suffered - first, to the entrance."
    "And then, past the familiar, memory-embedded high-rises, down snow-covered streets, where it is cold just to look at the rays of lanterns freezing in the air."
    stop music fadeout 3
    scene bg bus_stop with diam
    pause(2)
    scene bg intro_xx with fade
    play sound_loop sfx_bus_interior_moving fadein 4
    voice "Oh, excuse me, please, did I hurt you too much?"
    me "No more than Masha hurt the Bear."
    "Habitually, I replied, without looking at the perpetrator of the accident."
    me "The main thing is for it to not become a habit."
    voice "And why are you so calm about it?"
    "I shrugged and looked at her."
    "My eyes just wouldn't focus for some reason."
    show blink
    play music music_7dl["out_of_your_tier"] fadein 1
    pause(1)
    scene
    $ renpy.show("bg ext_townscape_ph_day_7dl", what = Dawn("bg ext_townscape_ph_day_7dl"))
    show prologue_dream
    with fade
    "They were shaken out of the bus early in the morning and left just like that."
    "Another ten or fifteen minutes and the parents will be rushing to pick up the kids, and some of them can get home on their own, since they live across the square from the bus station."
    "And some can be picked up by a friend."
    "But it's a day off, so no one in the house has set an alarm clock."
    "That's why I don't wake up until 9:00, and by the time I'm done with work and feeding the family..."
    "By the time I get to the square, Lena isn't there."
    "There's only Olga Dmitrievna, upset about something, and a pack of pioneers."
    sl "Olga Dmitrievna? Hello. {w}Where's Lena?"
    show mt sad pioneer behind prologue_dream
    with dissolve
    mt "Tikhonova went home."
    "The counselor and longtime friend seems upset about something, but we live close, I'll definitely see her."
    "And Lena..."
    sl "Why are you here so early?"
    show mt normal pioneer with dspr
    mt "There was a storm warning for the region, so we had to leave early."
    "My chest tingled with a foreboding feeling of something bad."
    "I run to Lena's house."
    play sound sfx_open_door_kick
    scene
    $ renpy.show("bg int_access2_day_7dl", what = Desat1("bg int_access2_day_7dl"))
    show prologue_dream
    with fade
    "Like a splinter in my chest, something sticks inside me, won't let me stop."
    "I kick the door for the first time in my life: it opens too slowly!"
    "And, jumping over the stairs, I rush to the third floor, where the Tikhonov family lives."
    play sound sfx_knock_door7_polite
    sl "Lena? It's me. Lena!"
    "No answer, no hello."
    "In my heart I push the door open, and it's unlocked."
    "And just in time."
    play music music_7dl["lunar_anguish"] fadein 1
    scene bg int_mt_sam_room_7dl
    show un3 serious_88 pioneer
    show prologue_dream
    with dissolve
    un "Oh, it hurts, my God, my God..."
    "Lena wasn't in the room, in the kitchen, in the bathroom..."
    "When I find her, she's lying in the bathroom, cradling her left hand, with blood oozing down between her fingers."
    un "Why does it hurt so much?"
    "I get nauseous at the sight of blood, and when I see the scarlet, shiny plate of a razor blade on the edge of the tub, I almost turn myself inside out right there."
    sl "What... What are you doing, you're completely crazy, or what?!"
    show un3 sorrow_88 pioneer with dspr
    "Lena curled up."
    un "I thought I'd had enough pain, but it was too much!"
    un "I'm weak!.."
    sl "Don't be silly, how on earth did you think of that?!"
    "I rush around the house looking for some kind of bandage, find the first aid kit in the kitchen, and with a pang I bandage my friend's bleeding wrist."
    "She sobbed."
    un "Remember when we got back, I thought, «This is it now, this is it!»"
    show un3 cry_88 pioneer with dspr
    un "And nothing happened!"
    sl "Enough nonsense, we need to call an ambulance!"
    un "No, no ambulances, can't you hear me? I want to die!"
    un "But so it doesn't hurt that much!"
    play sound sfx_open_door_kick
    "There was a rumble from the door, as if someone was about to knock the door off its hinges, and a meteor in a police uniform flew into the bathroom."
    voice "Lena?"
    voice "..."
    voice "Idiot."
    "The girl's head flinched from the slap, the meteor rushed away, and a second later a worried voice came from the hallway:"
    voice "Hello? Suicide attempt, yes, she cut her wrists. Elena Tikhonova. Write down the address. Alright, I'm waiting."
    with fade
    "Half an hour later Lena was taken by ambulance to the first city hospital."
    "Another six hours later, when only through the connections of Lena's father I was able to see her, I heard the basic diagnosis."
    scene
    $ renpy.show("bg ext_hospital2_away_day_7dl", what = Desat1("bg ext_hospital2_away_day_7dl"))
    show un3 sorrow_88 pioneer
    show prologue_dream
    with fade
    un "They're taking me to the center, to Litvinov's psychiatry."
    sl "You're my friend. And it's very important to me that you're okay."
    un "Can't you see it's not going well?"
    un "Can I finish this already? I'm tired of the pain."
    "She looked haggard, tortured, and words came naturally from the lips - wrong, ugly, but they were the only thing that could help right now."
    sl "Okay, you can finish. {w}But just as a friend, do me a favor, please."
    un "What is it?"
    sl "Give the world a chance, one last, only chance."
    sl "You have a life, don't just throw it away."
    show un3 normal pioneer with dspr
    un "And if it doesn't work out, you won't stop me anymore?"
    sl "I promise. Next year we'll go on the same shift together, and if anything happens, I'll just stay out of the way."
    un "Swear it."
    "And I swear."
    hide un with dspr
    "I know I won't be able to break this oath - Lena knows how to make me swear, we've been friends since childhood for a reason."
    scene bg ext_townscape_ph_day_7dl
    show un3 sad_88 winter_88
    show prologue_dream
    with fade
    "Lena wasn't discharged until the end of November, and I was very scared to meet her, to meet her like that."
    "Only she didn't look too angry or sad."
    "A normal, lively look, slouching shoulders, a wide strap on her wrist."
    un "Father gave it to me for the discharge."
    "She answered."
    un "To appreciate the time... and... to hide the scar."
    "Beneath the wide strap was an ugly, ugly scar."
    sl "Lena, I..."
    un "Just remember your vow."
    un "Remember."
    scene black with fade
    stop music fadeout 4
    $ alt_pause(2)
    play sound_loop sfx_bus_interior_moving fadein 1
    $ alt_pause(1)
    scene anim intro_13
    with fade2
    $ alt_pause(3)
    scene bg intro_xx
    with fade
    "I blinked and the obsession was gone. What was that?"
    "With difficulty remembering what I was being asked, I finally answered."
    me "Probably because I've already saved you, it's too late to dodge."
    "The girl smiled:"
    voice "What a funny man you are. What's your name?"
    me "My name is Semyon."
    voice "Semyon?"
    "She tried the sound of the name."
    voice "Semyon as in Syomushka?"
    menu:
        "Yeah, like Syomushka":
            scene anim intro_8
            "That smile was impossible to resist."
            me "Syomushka."
            "I nodded."
            $ alt_day6_sl_cl_int = 2
        "No, like Semyon":
            "There was only one girl who could call me Syomushka."
            "She was the only one allowed."
            "I don't care if she doesn't exist."
            scene anim intro_8
            "The girl got a little sad:"
            voice "I'm sorry, please. I didn't know you were in a bad mood."
            me "It's okay."
            "I shrugged and went back to my seat above the wheel, plugging my ears with my headphones."
            "After hesitating a bit, she didn't sit down next to me, but went to the back deck - I followed her with a glance."
            "And, grabbing the handrail, she stood there."
            "Must have been offended."
            "I don't care. I'm old-school - don't need girls, don't need nobody, only trouble from everybody."
            "I used to think otherwise."
            "And I got burned by it."
            "A cold July afternoon in a land far, far away."
            "And I shook my head, trying to banish the memory."
            th "Where's my schizo now, when I need it so badly?"
            "Mocking as it was, but my mental illness separated the black memory from the light one beautifully."
            "The truth ended with a venomous monologue in my apartment - apparently I really am hopeless."
            "It suddenly occurred to me that I had no idea where I was going."
            "And why?"
            "So at the nearest stop I jumped up and got out of the car."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_sl_cl_ambulance:
    scene bg int_clubs_male_day with dissolve
    play music music_list["you_lost_me"] fadein 3
    me "Slavya?"
    "Her eyes are closed, chest hardly moves, there's a huge bump on the forehead."
    me "Slavya, what's wrong with you?"
    "I rushed toward her, almost bumping into the ill-fated attic ladder."
    dreamgirl "Can you guess for yourself, smartass? Or will you wait until she wakes up?"
    me "But..."
    "There doesn't seem to be any damage other than the bump."
    "It's strange that she's unconscious in such a case - can you really hit that hard from a couple of meters away."
    dreamgirl "Listen."
    dreamgirl "Hear that?"
    dreamgirl "You hear it."
    if alt_day4_sl_cl_tut_iz:
        "It seems I didn't refuse to help the day before yesterday for nothing."
        "Because I hated what I heard."
    else:
        "From the attic came a rhythmic throbbing that I had heard once before."
    "A dark pulse. What did the old man call it - the techno-curtain?"
    "Acting almost automatically, I pushed the ladder into place and closed the hatch."
    "The ringing immediately disappeared like it wasn't there - apparently some sort of protective circuit."
    dreamgirl "And the old man knows his stuff!"
    "The inner voice marveled."
    dreamgirl "He's so dry, but he worked well - it discourages even the nimblest from climbing."
    th "Only now we don't know what to do with these «nimblest»."
    "I sighed."
    scene bg int_clubs_male_sunset with blind_l
    "I'm not a doctor, I don't think I can help her."
    me "I guess I'll have to carry the girl in my arms again."
    me "Eh, she'll get used to it!"
    stop music fadeout 3
    stop ambience fadeout 3
    play sound sfx_open_door_2
    pause(1)
    play ambience ambience_camp_center_day fadein 3
    scene
    $ renpy.show("bg ext_clubs_day", what = Dawn("bg ext_clubs_day"))
    with dissolve
    play music music_list["everyday_theme"] fadein 3
    "Not that I'm much of an expert on mechanical damage, but the situation was clear enough in my head."
    "Slavya came into the club while I was there fiddling with Miku, opened the door, and waited for me."
    "Waiting was a bit boring, so she was quite expected to be curious when something {i}weird{/i} was heard from upstairs."
    "Came upstairs, got a tangible share of that vibration up there."
    "And quite legitimately rumbled down."
    me "I'm carrying her in my arms like a bridegroom."
    "I muttered as I walked around the square - I definitely didn't want to meet someone else there."
    me "My betrothed, my fiancé, my concussed."
    me "Maybe I want to be held too! Take me in your arms and carry me, waaaah!"
    "More coaxing myself than really playing for an audience, I slowly made my way toward the infirmary."
    scene bg ext_aidpost_day with dissolve
    "No, of course I was worried about Slavya - so much so that the whole time I was carrying her in my arms, no scruples ever occurred to me."
    "And that says something!"
    me "My poor thing..."
    "I pulled her hair away from the forehead, couldn't stand it, touched it with my lips."
    "And a smile that I loved so much finally appeared on the drained face."
    "It seems her fainting was not so much due to the fall as to the fact that she hadn't been getting much sleep lately."
    "That's why she's taking what she can get."
    play sound sfx_knock_door7_polite
    cs "Open!"
    stop ambience fadeout 3
    play sound sfx_open_door_strong
    pause(1)
    play ambience ambience_medstation_inside_day fadein 3
    scene bg int_aidpost_day at zentercenter
    show cs normal
    with dissolve
    cs "So you did roadroll her after all?"
    "Viola snorted."
    "Compared to this morning, she had extra confidence."
    "Though I wouldn't say it added to her joy."
    "I mean, I would have been quite fooled by her role five days ago, and it would have made me blush."
    cs "This is what intemperance leads to. Take the clothes off."
    "But she wouldn't get current me with that — the intimidated expression, the few new wrinkles at the corners of her eyes, and the blank detachment — everything gave the appearance of a person intensely struggling to solve a problem in Viola."
    "One can only hope that this problem has at least one solution."
    me "Should we both undress, or can we take turns?"
    show cs smile with dspr
    cs "Okay, what happened?"
    me "It's hard to say, I came to the debriefing."
    me "But it looks like she bumped her head and..."
    cs "And I'll take it from here, thank you."
    "With my help, Violetta laid the girl down on the couch, loosened her tie, and undid her top two buttons."
    "I didn't look any further - I stepped back and sat down on the stool, waiting for our good doctor to give her verdict."
    with fade2
    cs "Well."
    "Finished her examination, she concluded."
    cs "A bump is like a bump, just bumped into something - and I just hope it's not you."
    "I smiled with one lip."
    cs "She fainted from exhaustion."
    cs "Nervous."
    if alt_day5_sl_cl_hentai_done:
        cs "And physical."
        show cs shy with dissolve
        cs "Pioneer, why did you wear out the pioneer girl?"
        "I blushed."
        "But resolutely ignored all the Violisms."
    me "What's going to happen to her now?"
    cs "Nothing is going to happen."
    play sound sfx_open_water_sink
    play sound_loop sfx_water_sink_stream fadein 2
    "Viola shrugged, went to the washbasin, and began to wash her hands thoroughly."
    cs "She'll sleep for three or four hours, she'll be bouncing around like a young goat by the dance."
    cs "Though I'd wager it'll be till morning."
    me "So she'll miss the concert?"
    cs "Probably."
    "I grabbed my head."
    th "Because that means..."
    dreamgirl "Yes, yes, the very thing Miku told us - you're more Slavya now than Slavya herself."
    dreamgirl "Obey!"
    "With a sigh, I got up."
    me "Thank you so much."
    stop sound_loop
    play sound sfx_close_water_sink
    pause(2)
    show cs smile with dissolve
    cs "You're welcome - you've been useful to me, too."
    "Just in case, I didn't elaborate on what she was talking about, and sideways left the scaffold."
    "I didn't want to leave Slavya, but it looks like I'll really do more good now if I at least partially take on her usual functionality."
    stop music fadeout 3
    stop ambience fadeout 3
    play sound sfx_open_dooor_campus_1
    pause(1)
    scene bg ext_aidpost_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    play music music_7dl["carefree"] fadein 3
    "As I jumped out of the squat house with the red cross into the street, I froze at a loss."
    me "So what do we do next?"
    th "I mean, filling in for Slavya is great and all, but other than the concert, what else was she doing there?"
    th "Geez, there's no one to ask!"
    dreamgirl "We've got to sweep the square!"
    th "Oh, screw you, you so-called free thinker!"
    dreamgirl "No, why?"
    me "Freeze!"
    "I intercepted Ulyanka, rushing off on her own."
    show us laugh sport at fleft with easeinright
    me "Little one, whoa!"
    show us normal sport at left
    with vpunch
    us "WhatdoyouwantImbusy!"
    "She blurted out in one word."
    me "There's something I want from you!"
    show us calml sport with dspr
    us "What's the big deal, go away, miserable!"
    "She pushed me away and tried to run away, but now I was in Slavya mode and just wasn't paying attention to the nonsense!"
    "Especially as a very distressed Olga Dmitrievna was running past us somewhere."
    "And I understood perfectly well who was the reason for that - in the absence of alternatives."
    play sound sfx_alisa_falls
    pause(1)
    "Ulyana squeaked and immediately ducked behind me."
    me "And you told me to leave."
    "I grinned, though, covering for the little one."
    "Olga, with a sound hinting at a speed of no less than Mach 1, whizzed past us, chanting unprintable."
    me "Close your ears, kiddo, it's too early for you to know such words."
    show us sad sport with dspr
    us "You always say that, when you know a bad word, you're a little girl, but when you're on canteen duty, you're a grown-up!"
    me "I didn't make you do canteen duty."
    "I pointed out."
    us "You're taking their side anyways, not mine!"
    me "I can take yours too."
    show us laugh sport with dspr
    us "Wow, this is great! You and I are going to make such a mess!"
    me "But first I need you to help me a little bit."
    show us dontlike sport with dspr
    us "I knew it was coming. {w}You're all the same."
    dreamgirl "You're all thinking of one thing, yeah!"
    me "Look, you'll have to do the following."
    "I leaned over to her ear and spoke."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_sl_cl_concert:
    scene bg ext_stage_big_day_7dl with joff_l
    play ambience ambience_camp_center_day fadein 3
    play music music_7dl["midday_reverie"] fadein 5
    "As the sun rolled down from its point in the sky, forcing me to consider the number of hours in the local twenty-four hours, I could no longer feel my legs under me from fatigue."
    "It was a hard five minutes. Very hard."
    "In spite of even engaging Ulyanka's labor and defense-and it's best no one knows what I promised her as a reward!"
    "I turned on absolute pause mode, pressing the smirk that twisted all over my face - the realization that such a day at Slavi's was considered routine."
    "She would get up at the crack of dawn when even the counselors weren't up for flying yet."
    th "Yes, a very lazy girl - would get up at five in the morning to be lazy longer."
    "She would put on her incredibly beautiful tracksuit and go for a run in the cold and quiet."
    "Ordinary life, schedule, routines - if you're a strategist, you know how to enjoy established management, even if it's getting established right now."
    "It's kind of fun to watch things run like clockwork, without requiring any input."
    "Although it's a very high entropy system here, participation is always required - there to support, there to prop it up. But it's also a joy!"
    "And then I show up on the horizon and everything goes to hell."
    "I marveled at the girl's boundless energy, her strength and endurance."
    "And I myself managed to wear her out - as a capricious child wears out his mother so that she falls asleep next to him at the halfway point of an under-told tale."
    "I was amazed at how she always knew where, what and how to do to keep things from falling apart - and now I'm running in her place myself."
    "Exhaustion has pressed her frail carcass to the hospital couch - and woe to whoever tries to wake her up!"
    scene
    $ renpy.show("bg ext_stage_big_day_7dl", what = Dawn("bg ext_stage_big_day_7dl"))
    with dissolve
    "I was almost thirty when this story began, my name was Semyon - and I'd been dreaming all my life of finding a place for myself."
    "It seemed simple, listen to yourself and let it happen."
    "But I've tried myself in so many fields - from love to design - and nowhere, nowhere have I found myself."
    "The saddest part is that computer toys have fostered in us a ruthless expectation of a visible manifestation of progress - in case we move the right way."
    "It doesn't work in life."
    "In love, for example, there is a clue. The heart - it hiccups, rejoices, beats and responds in all kinds of ways."
    "What about vocation? You try your hand at something, like music."
    "You pick up a guitar in your teeth and you've been playing for a few years, overcoming all the attendant things, thinly earning yourself a level of playing..."
    "And the result is that you don't have enough reaction time to play the really difficult stuff, you don't catch the melody by ear because it's not subtle enough."
    "And anyway, there's an Asian brat about fourteen years old who's been doing it cooler than you for a long time."
    "Somehow it turns out that in almost every field of endeavor there is an Asian brat doing it cooler than you."
    "But time is lost, you can't win back the years you've wasted, and you carry the cross of failure for the rest of your life."
    "It's similar in art. {w}In design. {w}In photography. {w}Even in writing."
    "You make tangible progress after six months, but very soon you reach your bar, above which you can no longer jump."
    "You realize very clearly how low that bar is when that Asian brat comes into your life."
    scene bg ext_stage_big_clear_day_7dl with diam
    "But now, while I was fiddling with the equipment, playing with Ulyanka, fighting off the kids trying to turn soundcheck into a request program, I suddenly realized that, quite possibly, this is my place?"
    th "There's a reason I'm so drawn to Slavya, isn't there?"
    "I sat on the bench next to Miku, smelled the faint scent of eucalyptus perfume, and was diligently silent, barely responding to her monologue."
    "Because she was the only one chatting, but for some reason the younger pioneers stayed out of her way."
    "Not a bad repellent against clingy little things!"
    "Of two evils, as they say."
    "Boiling, bubbling life. Childhood."
    "And for some it will continue tomorrow and the day after that - to give everything to jump off the bus again, the only fear of dousing yourself with juice from a jar, to jump out into the world of three weeks of summer and people who are glad to see you."
    "And you get your passport after camp, and the world is still too bright to be sad about the little things."
    me "I like it."
    "I said."
    show mi normal voca at cright
    with dissolve
    mi "Excuse me, Senechka, did you say something? Because I couldn't hear, it's so noisy, and the pioneers are noisy, and it's so bustling!"
    me "I like it here."
    "I repeated without raising my voice."
    show mi smile voca with dspr
    mi "Oh, I like it here too, very, very much! And when we first arrived, I didn't know anyone, and I tried to get acquainted with everyone, but they cursed and shunned me!"
    mi "But then I realized that in the Union you just have to give a person time to get used to you and open up to you! {w}Although I myself think you have to get used to a new acquaintance, but I just can't not communicate!"
    "I jerked my shoulders - a little, but still squared up during this week. {w}How tight my shirt is. And not so long ago it was loose."
    "Youth - all it takes to reshape your own body is a simple desire. And a little bit of activity."
    "Even just swinging a broom will be enough."
    "Let alone things like running cross-country with one girl in your arms."
    if alt_day5_sl_cl_hentai_done:
        "And the accompanying scenes with the same girl a couple of days later."
        "A whole night long - I felt chewed up in the morning and she was chipper. {w}Now we switched roles."
    scene bg ext_stage_big_clear_day_7dl behind mi at enterleft
    show mi smile voca at right with moveinright
    show cs normal at cleft with dspr
    with dissolve
    "I felt someone's gaze on me and turned around."
    cs "Coping... pioneer?"
    "Violetta has managed to regain her composure a bit, I see."
    "Well. That's a relief - at least something in this world is going the old way."
    "I shrugged. I'm tired, of course - but I'll be damned if I'm going to tell anyone!"
    me "How's she doing?"
    "The question was more than appropriate."
    "Viola shrugged her shoulders."
    cs "Asleep. What will become of her."
    cs "Unlike you, she didn't bang her head."
    "She looked me over from head to toe."
    cs "It seemed to do you good, though."
    me "What do you mean?"
    cs "She woke up a couple of times, if you want, you can go see her, just quickly."
    me "But I have the concert!"
    show cs smile with dspr
    cs "That's why I say - just see her. {w}Because who knows what you'll do given the time."
    dreamgirl "Item obtained: Infirmary key x1."
    dreamgirl "Story important decision is available!"
    th "Screw you!"
    if (lp_sl >= 18) or (lp_sl >= 16 and alt_day5_sl_cl_hentai_done):
        menu:
            "And who will watch after the concert?":
                me "Not Miku for sure."
                show mi upset voca with dspr
                mi "HEY!"
                me "I'm sorry, Miku, but I'd really feel better if I checked things out on my own."
                show cs smile with dissolve
                cs "Well done, pioneer girl. Picked herself a cavalier to match."
                "Viola nodded and went to Olga Dmitrievna to whisper about something."
            "Can I?":
                show cs shy with dissolve
                cs "You can... Just be careful."
                cs "Lest they accuse me of pandering later."
                "I blushed - the nurse was in her repertoire."
                me "Thank you!"
                "Nodding to Miku, I got up and headed for the infirmary."
                scene bg ext_square_day with dissolve
                "Or rather, how should I say, headed."
                "I ran!"
                "I ran at full throttle."
                play music music_list["everlasting_summer"] fadein 3
                if (counter_sl_7dl >= 1):
                    "As it was on our first day."
                if alt_day_binder != 1:
                    "I remembered arriving as I stood foolishly staring at the gate that I had seen all my life in a dream."
                    "And she was the first one to come out to me, smiling."
                    "Our romance must have begun even then."
                    "But I, busy thinking about survival and trying to understand what was going on, just wasn't paying attention to the fact that this girl was looking at me with a special warmth."
                    "One that is reserved only for those closest."
                "The six days I spent here were full of endless conflicts, quiet warfare, truces with knives frozen at my throat."
                "No one stopped me from ignoring the voice of my heart and looking toward someone who would accept me for who I really am - and there have been some here."
                "That's not to say anyone forced me into romantic entanglements - instead of dealing with the situation properly."
                "My own fault."
                "So we only dream of peace - and the war goes on."
                "The quiet war with myself, to become better than I was, stronger, faster, more interesting - Slavya gave me the kind of stimulus my whole previous life had not given me."
                "I once wanted to go into space."
                "I wanted to be the best musician on our tiny planet."
                "I dreamed of scientific discovery, cultural achievement, just making a difference."
                "But life put everything in its place."
                "And underneath the incredibly interesting annotation adorning the incredibly beautiful cover, titled as «My summer», turned out to be a boring, gray, run-of-the-mill novel of the kind that they sell for a bundle for a ruble in train station cafeterias."
                "It got to the ridiculous point - when I realized where I was, my first feeling was regret for my lost existence."
                "As someone said, the consciousness of a slave."
                scene bg ext_aidpost_day with dissolve
                "It's good to have someone around who can straighten me out."
                "And show me the path I'm walking on right now."
                "The one I don't know where I'm going. But I'm not alone on it, that's what matters."
                stop ambience fadeout 3
                play sound sfx_open_dooor_campus_1
                pause(1)
                scene bg int_aidpost_day with dissolve
                play ambience ambience_medstation_inside_day fadein 3
                "Slavya actually did wake up."
                "And even more so!"
                me "How are you?"
                "I asked, fighting the pity that came over me - so exhausted she looked."
                show sl normal pioneer with dspr
                sl "Answer a few questions, and I'll be better."
                me "Sure. What questions?"
                show sl smile pioneer with dspr
                sl "Say..."
                "She patted the bed beside her, and I landed beside her."
                sl "Olga Dmitrievna is at the concert, isn't she?"
                "I nodded."
                sl "And so is Violetta."
                "I confirmed that, too, not quite understanding where she was going with this."
                sl "And you didn't see Ulyana?"
                me "She was helping me in preparation for the concert, said she deserved encouragement at the dinner."
                sl "Then I need you to help me."
                me "Yes, of course."
                "Errands, or 'tasks,' I treated with philosophical calm."
                "Already."
                "Then Slavya did something that really, really surprised me."
                "She reached out and grabbed my belt buckle hard."
                me "And what's the help?"
                "I froze, not knowing how to react."
                "The body, though, seemed to know."
                scene black with fade
                play music music_7dl["breath_me"] fadein 3
                "And judging by Slavya's smile, it knew very properly."
                play sound sfx_unzip_sleepbag
                "Because a moment later there was enough space under my shorts - and I was immediately caught."
                me "Slavya, what's that supposed to mean?"
                "No, I wasn't that retarded, I knew already where this was going, but..."
                if alt_day5_sl_cl_hentai_done:
                    "Isn't she supposed to be sick at this part and all?"
                    "I asked that - but I don't think I was heard at all."
                    "And after a few seconds, that question stopped bothering me, too."
                    "It was very hot, very crowded, and those sounds..."
                    "It seems that the question about Viola, Olga, and Ulyana was asked with a far-reaching purpose."
                    "It seems to me all the time to be nonsense at all, when in fact there is Slavya, there is me and what is going on in the isolation ward."
                    sl "Come on quick, quick, we don't have much time, Olga will surely go after you as soon as she gets rid of Viola."
                    me "But I…"
                    sl "You have ten minutes, Semyon. So come on."
                    "She leaned her knee on the bed and somehow sagged very slyly - a man's spine can't do that for sure."
                    "Though how do I know what a man's spine is or isn't capable of?"
                    "But that sagging back, that lifted skirt."
                    "This light blue fabric that had been pulled aside."
                    "I was dazed as I watched her actions, as something viscous, transparent was left on my fingers."
                    sl "Are you going to help me or what?"
                    "She turned around and, biting her lip, winked at me."
                    sl "You weren't so shy this morning."
                else:
                    "She's a little girl, isn't it a little early for her to be thinking about such things?"
                    "I'm reminded of last night's performance of Violetta Cernovna."
                    "I could have sworn she clearly had her manicured fingers in that situation."
                    "And after a few seconds, I stopped caring about little things at all."
                    sl "Of course, that's not how it was supposed to go at all."
                    sl "But I thought that since everything was going so wrong, it was silly to wait for a moment."
                    sl "I want to make love to you."
                    me "Eh?"
                    "I think I'm blushing."
                    sl "Syomushka, didn't you hear?"
                    sl "I should have stopped hesitating yesterday."
                    me "But what about..."
                    sl "We've got ten or fifteen minutes before they miss us. We'll have to hurry."
                "Her eyes were soft, moist, with a twist."
                "Calling."
                "And I sent all my caution and fear of being caught to hell."
                "And I stepped towards Slavya."
                "She was very hot, very tight, very... Very..."
                "And I went crazy."
                scene black
                "And when I came to myself again, it was too late."
                if alt_day5_sl_cl_hentai_done:
                    "What was it Slavya said - to wake up in the middle of the process?"
                scene
                $ renpy.show("bg int_aidpost_day", what = Dawn("bg int_aidpost_day"))
                with dissolve
                "What an idiot I am."
                "I'm the biggest idiot in the world."
                "And why did I believe a stupid girl?!"
                "She's already hurt because of me, isn't that enough?"
                "Should I have made it worse by thinking not with my head, but..."
                "Dumbass-idiot. Los cretinos."
                "Anyone will tell you that an orgasm is a discharge. A grounding of nervous energy on a partner, a release of power into the void."
                "Why did I believe that making love could somehow help a depleted girl?"
                "Right, because I'm an idiot."
                if alt_day5_sl_cl_hentai_done:
                    "Slavya seemed to really like the context we had outlined the night before."
                    "And she didn't mind at all to pick up the slacking subject."
                    "And she wasn't satisfied with cramming; she wanted lots of different things and definitely interesting things."
                else:
                    "The fact that I was first was obvious almost immediately - it didn't work out."
                    "I had to try different ways before we found the right position for both of us."
                    "Slavya was red as a boiled crawfish, looking anywhere but at me."
                    "But she was not ashamed of her own nakedness, as I was used to it."
                    "And on a timid suggestion to do it some other time, she looked at me so that I obediently shut up and redoubled my efforts."
                    "But finally we were getting somewhere."
                "I, acting more on autopilot, reached her neck, bit lightly..."
                "She moaned and growled, her nails digging painfully into my forearms."
                "She was all hammered, shaking, I didn't even know what was wrong with her right away."
                "Somehow it occurred to me that she wasn't in the right state to..."
                "Exactly."
                "I barely caught her when she nearly bumped into the window sill as she rolled forward."
                "She didn't respond to stimuli."
                "She didn't react to anything."
                "Just lay there with a kind of quiet, peaceful smile."
                "Sleep, hardly distinguishable from unconsciousness."
                "It is unconsciousness."
                "The strength that was supposed to keep the girl afloat until supper had just gone to waste."
                "After making sure it was useless to wake her, I fixed her clothes and covered her with the blanket."
                dreamgirl "What you gave out was something!"
                dreamgirl "And her? Did you see her?"
                th "Fainted, what..."
                dreamgirl "Aren't you proud of yourself?"
                th "Bringing an exhausted person to this state is no reason to be proud."
                "I had the extremely idiotic task of admitting to Viola that I did Slavya... ahem... how can I say this without swearing?"
                "In short, it's my fault for her condition."
                me "Sweet dreams, sunshine."
                "I wished, stroking her head."
                "She smiled softly without waking up - she didn't seem to have the strength for anything else."
                $ alt_day6_sl_cl_hentai_done = True
                play sound sfx_open_door_strong
                pause(1)
    else:
        me "I have an errand. That I can't trust anyone else with."
        me "I'm sure Slavya would understand."
        show mi upset voca with dspr
        mi "Actually, I'm in charge of the concert!"
        me "I'm sorry, Miku, but I'd really feel better if I supervised everything myself."
        show cs smile with dissolve
        cs "Well done, pioneer girl. Picked herself a cavalier to match."
        "Viola nodded and went to Olga Dmitrievna to whisper about something."
    stop music fadeout 3
    stop ambience fadeout 6
    return

label alt_day6_sl_cl_algorithm:
    scene bg ext_square_sunset with dissolve
    play ambience ambience_camp_center_day fadein 3
    play music music_list["silhouette_in_sunset"] fadein 3
    "I couldn't find my place with worry."
    if alt_day6_sl_cl_hentai_done:
        "I mean, mentally, I knew that after what we'd done, all Slavya needed was to sleep."
        "But she was too deeply asleep."
        "I hardly let myself be led out of the infirmary."
        "Viola seemed to understand everything when she entered the isolation room, for she immediately went to the window and, closing the transom, opened the sash all the way."
        "She complained about the over-zealous pioneers and told me to get out before I did anything else."
    else:
        "Viola looked at me strangely throughout the concert."
        "Kind of... disappointed or something?"
        "As if I was supposed to do Something from her point of view, and I..."
        "Ah, what's the use of guessing now!"
    "So I dutifully allowed myself to be recruited as a speaker-puller, with no sense of taste had supper..."
    stop music fadeout 3
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    scene bg ext_aidpost_sunset_7dl
    with fade
    "And had a little fight with Olga Dmitrievna over the right to carry the sick man's supper."
    "She either guessed something or knew it outright - but she did not want to agree for a long time."
    "At all this I watched with detached, squeamish curiosity - all my mental energies were thrown into solving the problem of how to help Slavya."
    scene
    $ renpy.show("bg int_refinery_day_7dl", what = Dawn("bg int_refinery_day_7dl"))
    with flash
    "Because no amount of nervous exhaustion involves a body temperature dropping to thirty-five degrees and clammy sweat!"
    scene
    $ renpy.show("cg d5_sl_bed_7dl", what = Dawn("cg d5_sl_bed_7dl"))
    with dissolve
    "I stood by her bedside for a long, long time, looking into her beautiful, slightly drained face, not knowing what to do."
    "And at some point she moved and spoke clearly: «Algorithm»."
    "Algo…"
    play music music_7dl["dead_silence"] fadein 3
    scene
    $ renpy.show("cg d5_sl_bed_7dl", what = SS_com("cg d5_sl_bed_7dl"))
    with flash
    pause(.1)
    scene
    $ renpy.show("cg d5_sl_bed_7dl", what = Notch("cg d5_sl_bed_7dl"))
    show dreamgirl_overlay
    with dissolve
    "The wall almost erected in memory crumbled with bricks, and events in the attic, in the tunnels, in the center of the labyrinth rushed into consciousness..."
    "Extremely powerful means of influencing the brain."
    "And I kept thinking about some kind of fatigue! Really, you jerk!"
    play sound sfx_open_door_kick
    pause(1)
    scene bg ext_aidpost_sunset_7dl
    "I jumped out of the isolation room and ran to tell Viola everything."
    play sound sfx_chair_fall
    with vpunch
    pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    scene black
    $ renpy.show("bg ext_aidpost_sunset_7dl", at_list = [sdl_transform8], what = Noir("bg ext_aidpost_sunset_7dl"))
    play sound2 sfx_bodyfall_1
    with fade
    "Ran!"
    stop ambience fadeout 2
    "I need to tell!"
    scene black with fade
    "While I still remember something!"
    scene black
    $ renpy.show("bg ext_dining_hall_away_sunset", at_list = [sdl_transform3], what = Noir("bg ext_dining_hall_away_sunset"))
    play sound2 sfx_bodyfall_1
    scene black with fade
    "As long…"
    scene black
    $ renpy.show("bg ext_dining_hall_near_sunset", at_list = [sdl_transform4], what = Noir("bg ext_dining_hall_near_sunset"))
    scene black
    play sound sfx_fall_wood_floor
    "This is where Viola's special brigade came upon me. What did they want? I don't remember."
    "Olga Dmitrievna, Viola, Miku, Ulyana - they surrounded me and demanded some details."
    "Details?"
    "For some reason a jagged darkness reigned in my memory, through which fibers of half-written images peeked through - shouts, pleas, even attempts to wave fists."
    "To the latter reacted Miku - she knocked me out with impeccable knowledge of anatomy."
    scene
    $ renpy.show("bg ext_aidpost_sunset_7dl", what = Noir("bg ext_aidpost_sunset_7dl"))
    with flash
    "Another gaping hole - I'm trying to make my way to the infirmary to make sure everything's okay, because well, everything's not okay, my heart's not in place!"
    scene
    $ renpy.show("bg ext_clubs_day", what = Noir("bg ext_clubs_day"))
    with flash
    "Another hole... I walk to the camp gate, my life is over."
    "I spit with hatred in the direction of the shabby clubhouse, for that's where all my troubles began."
    "And then I stop."
    scene
    $ renpy.show("bg ext_no_bus_night", what = Noir("bg ext_no_bus_night"))
    with flash
    "I'm scared to take a step out of the gate."
    scene bg ext_camp_entrance_night with dissolve
    play ambience ambience_camp_entrance_night fadein 3
    "I have nowhere to go, nowhere and no reason to go."
    "Everything of value I had left in my life was in this camp, in an area enclosed by a brick fence."
    "Not solid, of course, there were rips, too."
    "I went back."
    stop music fadeout 3
    return

label alt_day6_sl_cl_sh_story:
    scene bg ext_clubs_night with fade
    "Despising myself, I sat down on the steps and hid my face in hands."
    "And seemed to begin to come to my senses."
    play sound sfx_open_door_clubs
    "The door creaked rudely, Shurik came out and called softly:"
    show sh normal pioneer with dspr
    sh "Semyon, please."
    stop ambience fadeout 3
    scene
    $ renpy.show("bg int_clubs_male_sunset", at_list = [zenterleft], what = Notch("bg int_clubs_male_sunset"))
    show sh normal pioneer at cleft
    with dissolve
    play music music_7dl["out_of_painkillers"] fadein 3
    play ambience ambience_int_cabin_night fadein 3
    "You can't change the meeting place, meet me in hell."
    "This is where it all started."
    "It even made me want to climb up into the attic and break the ugly contraption for a long, long time until all that was left was harmless debris."
    "Which would never take anyone else away from anyone else."
    "And I wanted to grab the jerk by the chest, shake him hard, punch him in the neck so he'd think he was inventing in the first place."
    "But there was no hate, only an echo, a faint hint, like you always get when you shake the echo in a closed jar."
    "Or look at it through inverted binoculars."
    "And here it was the same old thing, the amplifier was gone, but everything else was left in place."
    "A Soviet man knew how to respect someone else's workplace, even a creative mess."
    "So - piles of cables, switches, solder jars, boxes, circuits - it was all lying in disarray on a large table, surrounding a gauge that remained mysterious."
    "On the table was a picture of Shurik, about four years old, no more, standing between two very beautiful, very similar women."
    "Each of them put a palm on his shoulder - each from her own side."
    "And he looks intently, but not into the frame - but somewhere further away, making the unwilling viewer feel like an empty space."
    "He was holding something behind his back, diligently facing me."
    "And I examined myself - what my recent blackout had done to me."
    "Nothing much, really: a lost tie and some slightly disturbed gold-plated buttons."
    "And, of course, the dirt - I get dirty all the time, I'm a terrible dirtbag."
    show sh upset pioneer with dspr
    sh "Drink?"
    "Shurik pulled out from behind a clear square bottle with the inscription «C2H5OH technical.» blew into the folding cup and poured exactly two fingers."
    me "Alcohol?!"
    th "What a shocking revelation."
    "Lifelessly I admired."
    sh "Don't look. {w}It's good."
    "He nodded at the portrait."
    me "Who is that?"
    "I nodded at the portrait."
    sh "M-mother… Aunt."
    "Through sheer force he squeezed out."
    me "What's wrong with them?"
    show sh serious pioneer with dspr
    sh "That's… Complicated."
    sh "Nothing… Drink."
    "He handed me the glass, and I mechanically tipped the nasty, cutting, fiery bitterness down my throat."
    "There was a hedgehog down my esophagus with red-hot needles, and I blinked, wiping away unwanted tears from my eyes."
    me "You don't know?"
    sh "I know."
    "Shurik squinted, and I got a distinct whiff of the dampness of the grave."
    show sh normal pioneer with dspr
    sh "Everything."
    me "Is that so…"
    "I stretched out."
    me "Look, what kind of bird are you that even Dr. Violetta is asking for you? {w}What's so special about you?"
    if (not alt_day4_sl_cl_tut_iz):
        dreamgirl "Excluding, understandably, the development of a working prototype of an AI."
    sh "Two."
    "He pulled out another photo from under the table."
    "It was different from the one on the table, though the number of people and the framing were the same."
    "He looked about thirteen years old."
    "The woman on the left was surprisingly well-preserved, considering how much Shurik had grown. She was smiling broadly."
    "And yet there was something subtly different about that woman. It was as if her gaze had changed. Gone was the seriousness. Maybe she was just having a really good day."
    "And the woman on the right was replaced by a girl who was very familiar, beautiful, with two different eyes."
    "Violetta Cernovna Collider. In person."
    me "So you've known each other for a long time, huh?"
    "Shurik nodded."
    "Poured himself a drink, and after sniffing it, he wrinkled his nose."
    sh "My mother got sick, my aunt died. Got savantism."
    "He looked demandingly into my eyes:"
    show sh serious pioneer with dspr
    sh "You know what it is?"
    "His speech was strange, but somehow you could understand it, the way you understand a word with the letters mixed up if the first and last letters are in place."
    me "Calculator kids, huh?"
    "He nodded again, hesitant to take a drink."
    "And went on telling."
    $ set_mode_nvl()
    "And I, feeling it with the same intuition that I now realized Slavya had, built a picture in my head."
    "Creepy, ugly, but... Now a lot of things were becoming clear."
    "Alexander Trofimov, son of the distinguished child psychiatrist Maria Trofimova, became almost an orphan after either the death or the terrible illness of his mother."
    "As a result of some shift in his psyche, or perhaps simply because of a predisposition, he was diagnosed at a very early age with mental problems - sleepwalking, absent-mindedness, epilepsy..."
    "And as if that weren't enough, by the time Alexander was three years old it was clear that he was an eidetic savant - a human calculator."
    nvl clear
    "In the Soviet Union they did not know what to do with such children, usually they were quietly and peacefully surrendered to psycho-neurological boarding schools, where they lived to adulthood, after which they left for life in Yazka, Skvortsova-Stepanov or the local equivalent of Kashchenko."
    "And it so happened that after his mother disappeared from his life, her protégé Viola Collider not only took him into her care, but also became his attending physician. She developed techniques not yet used in the Union and achieved outstanding results."
    "He may not have become a full-fledged member of society, but he went to an ordinary school, he socialized with normal children, even though he bore the mark of a man out of this world on his forehead."
    "Except that he did not go anywhere to rest, except the pioneer camp. And there went only a couple of times."
    "Shurik's case allowed Viola to be awarded the title of doctor without an actual defense. Shurik's condition was stable, and Viola decided to make those trips permanent."
    "To that camp in which she had many memories."
    "To «Sovyonok»."
    "These trips always went smoothly and without incidents. But this year it all went wrong."
    nvl clear
    "At some point either Shurik went so crazy that he stopped swallowing words, or I finally tuned into his wave and began to understand him from half a word, but our dialogue became full-fledged."
    "Or maybe it was because we were both already piss drunk and speaking the same language?"
    sh "I've been living in a glittering black emptiness full of mathematical formulas, calculations, and intuitive rules since I was three."
    sh "I looked inside myself as if I had been asleep all my life, only waking up at certain moments when I was asked to do something, to count, to remember or to reproduce something I had once heard."
    sh "It was like I had sand in my hand, and instead of drawing with it on the glass, I would let a little bit out of my fist and squeeze it again - even tighter."
    sh "Ten years."
    $ set_mode_adv()
    me "Shall we go outside?"
    "I was starting to get a little queasy, and some fresh air would be nice."
    show sh upset pioneer with dspr
    "The cyberneticist looked at me confusedly, then shifted his gaze to the glass."
    "Finally made up his mind."
    "Tipped the glass down his throat, squinted, blushed, grabbed the can of water."
    "The Adam's apple went up and down rapidly as Shurik drank the aftertaste away."
    stop music fadeout 3
    stop ambience fadeout 3
    play sound sfx_open_door_clubs
    pause(1)
    scene bg ext_clubs_night with dissolve
    play music music_7dl["knock"] fadein 3
    "We went outside and took a seat on all the same steps that this silly story was revolving around."
    scene bg int_clubs_male_sunset
    show prologue_dream
    $ set_mode_nvl()
    "Sunshine, warmth, spring."
    cs "Hello... the boy with the funny glasses."
    "Viola smiles, hiding hopelessness behind glass lenses."
    cs "I haven't told anyone, but I want to forget everything I've been taught."
    cs "I want to try something new."
    "She's twenty-three, she's just graduated yesterday, she's an ardent fan of Maria Trofimova, the mother."
    "And she really, really wants to be useful."
    cs "But, you know, sometimes I even think we shouldn't treat it. There's no reason to."
    cs "I like you like that, too. Capable of counting everything and anything in the world."
    scene stars with fade
    sh "We tried different things. And for a very long time. Tests, analyses, techniques too complicated even for my understanding. And then one day..."
    sh "The emptiness began to recede."
    sh "At first, individual sounds and colors started to appear there."
    sh "It was as if I was peeking at the world by pulling back the curtain at the window a little."
    sh "And Viola helped me bend it back more and more."
    nvl clear
    sh "The world, illogical, incomprehensible, not always subject to mathematics, frightened me. {w}But it was beautiful!"
    sh "I fell in love with it and was as grateful as I could be."
    sh "I learned how to look after myself, I learned how to talk to people and even hear what they say back."
    sh "The emptiness was gone almost completely, leaving only a small island in my head - and I go there, hide if things are bad around me, go back to a childhood full of numbers and formulas."
    nvl clear
    sh "But after the buzzer I had assembled from my own blueprints hit my brain..."
    sh "Look, it hadn't occurred to me how I could even get such blueprints? It is not in the 'Youth Technicians' that the scheme of the device of influence on the psyche was printed?"
    sh "Where did the schematics come from?"
    "Quiet whispers in the evening air."
    "He shook his head, resting his palms on the porch steps."
    sh "I can feel something leaving me."
    nvl clear
    sh "And its place is taken by the emptiness."
    sh "And I don't want it back!"
    "He sobbed."
    nvl clear
    $ set_mode_adv()
    scene bg ext_clubs_night with dissolve
    show sh upset pioneer with dspr
    sh "I want it like this, I'm not going, I'm not going!"
    me "Calm down."
    sh "Don't you understand?"
    sh "I tried to multiply the simplest four-digit numbers in my head this morning - and I couldn't."
    me "So what?"
    "I shrugged my shoulders."
    me "My ceiling is three-digit numbers, and those are slow."
    sh "Semyon, you don't understand. {w}The emptiness where I am slowly going is not my savantism, stifled and almost defeated."
    show sh serious pioneer with dspr
    sh "It's something else, there's no numbers, there's nothing there at all.{w} Real nothingness, worse than death."
    me "Probably just a process reversed."
    sh "Semyon, please. {w}I lived in that state for ten years, I know what it is. And this..."
    th "It seems that our genius has went insane after all."
    show sh scared pioneer with dspr
    sh "I can hardly remember now how the conversation began."
    "Slowly he said."
    sh "But I'll tell you what."
    sh "If there's anything I can do to make sure this happening here doesn't hurt anyone else..."
    sh "Give me fifteen minutes, I'll do something at the club. {w}Just don't come in, I don't like to be hovered over."
    "I nodded."
    sh "Well…"
    "He exhaled."
    sh "Good luck to me."
    play sound sfx_open_dooor_campus_1
    pause(1)
    hide sh with easeoutleft
    "And vanished in the bowels of the club."
    play ambience ambience_camp_entrance_night fadein 3
    "Leaving me alone."
    th "I wonder what he wants to do there?"
    "Without much interest, I thought."
    th "Some robot to do everything in his place?"
    "The inner interlocutor kept quiet for some reason, so I had to talk to myself."
    th "Shurik. Who could have imagined it."
    "The imagination gave me a picture similar to the creation of the world - first you are like an invisible spirit dwelling in the emptiness."
    "And then you begin to demand from it - let there be this, let there be that..."
    "I closed my eyes, thinking."
    "And a quarter of an hour later, squad leader stopped next to me."
    show mt normal pioneer with dspr
    mt "Slacking off again?"
    "She asked without anger."
    "Whatever's going on in our hood, it looks like I've been forgiven and rehabilitated."
    me "No, not really. {w} Waiting for Shurik."
    mt "Didn't notice when you two had time to become friends..."
    "Mumbled the counselor."
    mt "And him?"
    "I shook my head, alluding to the door behind me."
    mt "I need to tell him someth…"
    hide mt with dissolve
    "She opened the door and froze on the doorstep."
    "Went silent."
    "And then she whimpered softly."
    "And I, already sensing something wrong, turned and jumped..."
    play sound sfx_bodyfall_1
    "Barely managed to catch the counselor by the floor."
    "Looked over her into the clubhouse."
    "And almost lay down myself."
    "Above the table, smiling serenely, was Shurik hanging in a noose."
    "He was smiling at the void that had never defeated him."
    "Smiled at what he'd been afraid of all his life, and he didn't need a doctor."
    "Not even as good as our Viola."
    "Who, as it turns out, has her own long, long story about a boy with funny glasses who can count everything in the world."
    "Shurik was dead. {w}Irreversibly."
    "Almost cured savant didn't want to again become savant, to death even."
    "And his «to death» was more literal than I expected."
    $ alt_day6_sl_cl_arc = 'sh'
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_sl_cl_sh_tug:
    scene bg ext_clubs_night with dissolve
    play music music_7dl["unforgotten"] fadein 3
    "People were walking, laughing, loving."
    "And it was strange and wild to realize that they were living here, happy, and yet there was one less universe in the world."
    "Nothing has changed anywhere, no new entry has appeared on the tablets of heaven, no stars have been lit or extinguished."
    "Nothing has changed."
    "Just Shurik hanging in a noose."
    "There's a tiny bit of happiness happening on the dance floor, some girl finally waited and was asked to dance by a boy she likes."
    "Or vice versa - a boy is turned down for a dance by a girl he has long cared about."
    "And Shurik hangs in a noose."
    "I didn't watch what happened next."
    "One must respect another's right to die - even such an ugly one."
    "I think I've gone senile again."
    "Or maybe it's the alcohol. I don't know."
    "I had almost forgotten that Slavya was in a state suspiciously similar to a coma."
    "That the damned infrasound grid doesn't scare the rats, but cripples the psyche."
    "That five meters deeper is an absolutely similar abomination in killing power, only made in a more advanced form of mist."
    "Technological evolution? A more advanced model?"
    "I couldn't do anything with the buzzer or the fog - nothing at all."
    "But at least I could hold the hand of the one that matters most. Criminally little."
    scene bg ext_aidpost_night with dissolve
    play sound sfx_knock_door2
    "I walked across the concrete slabs of the pathway, lit by round lanterns, and knocked twice on the flimsy plywood door."
    "My grazed hands ached, a bruise poured painfully on my chest where a dainty size thirty-four heel had gone."
    "And still all the physicality felt somehow detached, like it wasn't happening to me."
    "And with whom?"
    "Someone who feels pain and prays to all the higher powers in the world, including those whose name is unmentioned?"
    show cs sad with dissolve
    "The door was unlocked by Viola, disheveled, in a wet and crumpled robe with long, ugly mascara stains on her face."
    hide cs with dissolve
    play sound sfx_open_door_kick
    pause(1)
    scene bg int_aidpost_night with flash
    play ambience ambience_medstation_inside_night fadein 3
    "Without saying anything, she grabbed me by the collar, dragged me into the room and slammed the door."
    show cs sad with dissolve
    "Planted me, almost tossed on the leather couch, exhaled, deflated."
    show cs cry with dspr
    "She took out the alcohol, splashed it on the beakers, and didn't even take a bite - she cried."
    "Only I forgot what it is to cry."
    "Only all that pounding and pounding under my diaphragm is a frantic, misplaced cry-prayer - please, a miracle! Miracle!"
    show cs sad with dspr
    cs "There are no miracles. {w}I would have laid down my own soul."
    cs "Your little fool has worn herself out beyond recognition, plus she has an individual intolerance to low frequency signals."
    cs "Like Sh… Sh… like Sh…"
    "She made a futile effort over herself, trying to pronounce the name of the man who had become her first patient, the first person into whose life she had managed to bring light."
    cs "He told you what happened to him, didn't he? Our shared story..."
    "She poured more."
    cs "It's like wiping down a dirty window - there's more and more room for the light, at some point there's nothing in the way of it anymore."
    cs "Except that you're sitting on the other side of the glass after all. And the world is there."
    th "Monitor windows."
    dreamgirl "Monitor."
    dreamgirl "Modem."
    th "Mouse."
    th "Revenge..."
    show cs normal with dspr
    cs "I have alprazolam, pioneer. A little pill and you'll remember this day as something you dreamed up and not dangerous."
    me "Then why are you yourself..."
    me "Not drinking it."
    show cs angry with dspr
    play sound sfx_table_hit
    with vpunch
    "Viola jumped up, smashing her knuckles as hard as she could against the table."
    show cs cry with dissolve
    cs "Because I'm stupid and guilty. I have to suffer."
    cs "Did you see the letter?"
    "I shook my head."
    if (not alt_day4_sl_cl_tut_iz):
        "And I kept wondering how he managed to build his buzzer, the robot, the chassis for it..."
    "It's better not to think at all, better to tear my heart out and look at everything with detachment and indifference."
    stop music fadeout 3
    play sound sfx_paper_bag
    "The letter."
    play music music_7dl["unfinished_life"] fadein 3
    show cs sad with dspr
    "Viola pulled a folded four-leaf from her pocket and unfolded it and began to read."
    $ set_mode_nvl()
    "{i}I do not ask you to blame Clava K. or anyone else for my death. It was my own fault.{/i}"
    "{i}It was a bad idea from the beginning to build a camp here.{/i}"
    "{i}It's logical to assume that if you want to hide something, hide it in the most prominent place.{/i}"
    "{i}But it would be better to build a warehouse or a factory or a military unit here, honestly.{/i}"
    "{i}Because workers and soldiers do not have as much free time and desire for adventure as children do.{/i}"
    nvl clear
    "{i}When my mother found out about the camp situation - the old one at the time - she couldn't think of anything smarter than to go see for herself. And the aunt... Well... You know.{/i}"
    "{i}The place got a bad reputation, children stopped coming, and the camp was closed.{/i}"
    "{i}I found out that she had been here shortly before her death, where my device now stands.{/i}"
    "{i}And met something, too.{/i}"
    nvl clear
    "{i}So it runs in the family.{/i}"
    "{i}I couldn't think of anything smarter, either, if you'll excuse me. But something tells me that it is useless to complain or publicize what is happening.{/i}"
    "{i}And I don't want any more children with a consciousness treated by a machine I've assembled, I don't want any more children walking around with such dangerous crap.{/i}"
    "{i}Hopefully, this time the camp will not be moved, but they will forget about this direction at all.{/i}"
    "{i}Semyon, don't be mad at me and take care of Slavya. She's really nice.{/i}"
    "{i}Sh.{/i}"
    nvl clear
    stop music fadeout 3
    $ set_mode_adv()
    "Viola was silent."
    cs "You can lie in the isolation room if you want."
    "Finally she said."
    cs "I think you'd better wake up together."
    cs "You have so little of each other."
    "I guess after what I set up tonight, I won't be too happy if I show up to spend the night at home."
    "So it would be wise to heed Violetta Cernovna's advice."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_sl_cl_regular_arc:
    scene
    $ renpy.show("bg ext_aidpost_day", what = Dawn("bg ext_aidpost_day"))
    show sl cry pioneer
    with dissolve
    sl "You know."
    "In a transparent whisper, looking through me, Slavya said."
    sl "I once wished that everyone would have a chance."
    sl "For this world to be a little more generous, and not be cruel to anyone who doesn't succeed."
    me "A chance?"
    "Her words unpleasantly hurt something inside."
    sl "I've always understood that just wanting something isn't enough, you have to work for it. Make an effort."
    me "Are you talking about helping those around you?"
    "Slavya nodded."
    sl "And then it turns out that I wished for everyone, for the whole world, but not for myself?"
    sl "That's not right. What about the chance for me?"
    "She whispered."
    sl "We just got it right, and..."
    me "Slavya, it's a matter of life and death."
    sl "That's right, Syomushka... {w}That's right."
    sl "I'm a selfish bitch, I know."
    "Her voice trembled, but her eyes were steady."
    sl "But you'll be gone forever."
    sl "And I can't let you go that easily."
    "She stood up, holding the box in her hands."
    sl "Forgive me, Pirate, forgive me."
    "Slavya, I..."
    sl "Semyon, please."
    sl "I have to finish some things - don't touch me, please."
    me "What am I supposed to do?"
    "After an act of deferred heroism, I felt like an idiot, throwing myself at a forty year old already silent embrasure."
    "Slavya twitched her shoulder, heading for the infirmary:"
    sl "I was supposed to help with the concert... If you want something to do, help Miku and Olga Dmitrievna."
    play sound sfx_open_door_strong
    hide sl with dissolve
    "She disappeared behind the nurses' station door, taking Pirate with her, leaving me alone."
    "It wasn't hard to guess exactly what was about to happen."
    "And - yes, at a moment like this, I'd really better stay away - the association is such a thing. Not a good one."
    "If Slavya is going to automatically remember for the rest of her life what she had to choose between once at summer camp..."
    "Although she may well start remembering that way. As I said, associations are a thing."
    stop music fadeout 3
    stop ambience fadeout 3
    scene bg ext_stage_big_day_7dl with dissolve
    "I thought I wouldn't be able to do anything - I was shaken to the point I was physically shaking."
    "Mentally, I knew I should just let her be alone now, solve a problem she could only solve alone - but my heart was pulling me back to the infirmary."
    "To be there for her. To be supportive. To be someone she can lean on in case of an emergency."
    "Not in this case."
    "All I can do in this situation is stand there with a lean face and pretend with all my might that I care about a puppy I've known for hours."
    "Pathetic, of course. But that's all."
    "And that's why it's better to distract yourself now."
    "The best way is a change of occupation."
    show mi normal voca with dissolve
    mi "Senechka, have you come to my rescue? You're so good, because I can't find Slavya anywhere, there's no one to help me, and I don't trust them anyways!"
    "She gave a dismissive gesture to the little ones crowding around the stage."
    me "You trust me? How touching."
    "I didn't hide my sarcasm."
    me "And what should I do?"
    mi "We have to do the following..."
    scene bg ext_stage_normal_day with joff_r
    play ambience ambience_camp_center_day fadein 3
    "The next time I was able to sit down, it was the beginning of five o'clock."
    th "The ensign pitied his wife for not sitting down once all day - he made her squat two hundred times."
    me "Where can I die here?"
    "I exhaled, flopping down on a nearby chair behind the console."
    show mi laugh voca with flash
    mi "Nowhere! I need you!"
    mi "You give me the microphone when I nod, and then you add a signal from channel 4, got it?"
    me "Yeah, sounds pretty easy."
    mi "Thanks, Senechka, you're the best!"
    "She dazzled me with a smile."
    hide mi with easeoutleft
    "And she went on stage in her outrageously short dress."
    "In general, it should be tantamount to sabotage to climb on a podium with that length of hem! Because it paralyzes the thought process of a good half of the male population."
    "All the more reason to look!"
    "And to me, from my pit, it was even a little bit painf... Hey, wait, where are we staring at?!"
    th "You can't relax for a second!"
    dreamgirl "No way! What a sight!"
    if ('music_club' in list_voyage_7dl):
        dreamgirl "What do you want to bet they're striped again?"
    th "Calm down, you horny monster. And even then I've got Slavya."
    dreamgirl "Just because you have one cake doesn't mean you can't look in a candy store window!"
    th "That's exactly what it means!"
    dreamgirl "How long have you been so squeamish? You never missed yours before!"
    if ('music_club' in list_voyage_7dl):
        dreamgirl "A couple of days ago you were standing there staring like a sweetheart!"
        if (alt_day2_convoy == 'sl'):
            dreamgirl "If it wasn't for your sweetheart, that's where you'd be!"
    th "That's it, the subject is closed."
    th "I've got Slavya, and she's in a bad enough situation right now for catching me in the middle of observing someone else's pantsu."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_sl_cl_hala:
    scene bg ext_stage_normal_day with dissolve
    play music music_7dl["melancholy_sun"] fadein 3
    play ambience ambience_camp_center_evening fadein 3
    "Speeches without thoughts, people without faces, heated arguments of the deaf and blind..."
    "It seemed astonishing and somehow irregular that funny and carefree children's life was boiling around, while literally next door, at a stretch of the hand, someone's unrelenting grief was hiding in the bushes."
    "Someone's dead universe - and the joy on their faces, a wild contrast."
    "But it's probably right - someone's misfortunes shouldn't poison their surroundings like radiation."
    "Just because someone's miserable is no reason for everyone else to be miserable."
    "Miku on stage was finishing her second song, glancing restlessly at the back rows set aside for our squad."
    "She seemed to be waiting for someone."
    with fade
    th "I wonder what she'll do if whoever she's waiting for won't show up?"
    th "Will she spit on the hole in the production and pull the next performer on stage? Or will she sing until he turns green?"
    "Knowing Miku, I'd lean toward the second option - especially with that kind of carte blanche for stage time."
    show mi smile voca with dspr
    "But finally a familiar voice came from behind her - Alisa."
    "Miku immediately brightened up - it looked like the redhead was supposed to follow up."
    "And with even more enthusiasm, she bounced around the stage, singing in a celestial tongue, enticing promises to hack people around her with blunt scissors."
    "And you wouldn't know it to look at that little chorus girl!"
    "The old, old prank - make a beastly face and try to say something in a sweet voice."
    "Not that I was expecting a Durst growling or arrogant madness like Mr. Lindemann, but..."
    scene bg ext_stage_big_clear_day_7dl at zenterleft
    show dv normal pioneer2 at cleft
    with dissolve
    dv "Salute to the retards."
    "Alisa slapped me on the back, plopping down next to me."
    me "You said that already."
    dv "And I'll say it again! Where's your friend?"
    "Without any transition Alisa asked."
    me "Do you think that's your business?"
    show dv smile pioneer2 with dspr
    dv "What about it! I have my own question for her. It concerns you, by the way."
    scene bg ext_stage_big_clear_day_7dl at enterright
    show dv normal pioneer2 at left with moveinleft
    show mi smile voca at cright
    with dissolve
    "She managed to intrigue me, but Miku appeared next to us out of nowhere:"
    mi "Alisochka, Alisochka, it's so good that you came, because I thought you forgot or didn't want to and changed your mind altogether! I almost put someone else instead of you."
    dv "No way in hell."
    "The redhead grinned."
    dv "I didn't spend all week learning the words and rehearsing so I could leave now."
    me "And yet you're late."
    "I reminded her."
    show dv grin pioneer2 with dspr
    dv "Do you think that's your business?"
    "Alisa mocked me and, picking up her guitar, rose from her chair."
    "The conversation again left more questions than it had before - although that seems to be the usual order of things in this camp."
    hide dv with easeoutleft
    show mi normal voca at center with moveinleft
    mi "Well, that's good, the finest moment is over, the counselors have brought the others."
    "She rubbed her palms together."
    mi "Let there be a concert!"
    with fade
    "Guitar strumming came from the stage, and Alisa sang something."
    "Probably not bad at all - but no matter how hard I tried, I couldn't get in the mood for the song."
    "I had to navigate the reactions of those around me."
    show mi happy voca with dspr
    "There's how Miku froze, diligently catching every word."
    "There, the pioneers, who had been noisy up to that moment, fell silent."
    th "Great idea, putting the strongest performance at the beginning of the concert to make sure they get the audience's attention."
    dreamgirl "Yeah, they'll be waiting to see if anybody else does any worse."
    dreamgirl "Or at least they'll drag the redhead on stage again."
    th "That's just unlikely - she's like Lorraine Christie, the one-hit singer: the main thing is to shoot yourself in the direction of the horizon, and then what happens happens."
    "I was more worried about what happened to Slavya."
    "I mean, she was at least okay, physically."
    if alt_day5_sl_cl_hentai_done:
        "Except for some discomfort after what we did in the vacant cabin."
    "But mentally..."
    "And I can't go check on her, I'd be disrespecting her will."
    "So she has to get over it on her own and not take it out on the people around her... The people around her. Me."
    "The music played and played, the pioneers came up on stage, singing, dancing, reciting poetry."
    "Danechka did a picture of a sports pyramid with his companions and shouted something from above - probably even something funny."
    "And I'm under a novocaine blockade - I can't touch anything, and nothing touches me."
    "It's the vodka to the point of nausea and loneliness to the point of wolf's howl that helps."
    "And I'm tempted to go wandering around the territory, looking for my sun - my heart is out of place."
    play ambience ambience_camp_center_evening fadein 3
    "I continued to sit in my seat, gripping the hard edges of the chair seat in pain."
    "I continued to sit."
    scene bg ext_stage_big_clear_day_7dl with fade
    "Miku was up on stage a few more times - she took part in a few of the other units' performances."
    "She also worked as a choreographer for the summer kindergarten."
    "She was busy, she was in business - and happy - in the business she loved."
    "And I have dreams, after which I can't sleep until you drop dead from fatigue."
    "Evening, summer, camp, concert. And me with reflections nobody needs."
    "A naked crystal hatred, as if screaming to the world, 'I feel bad, do you hear me?!'"
    "Though I never wanted anyone's attention."
    "Tired of it."
    "I smiled at the counselor who looked at me suspiciously, hiding a sincere plea under my eyelid: 'Die, please, or get out of my way.'"
    "And when the bitterness under my tongue became unbearable, I got up and hurried off somewhere without turning around."
    "In the very direction that seemed most appropriate to me now."
    "In the direction where Slavya might be."
    stop music fadeout 3
    scene bg ext_square_day with dissolve
    play music music_7dl["lynn"] fadein 3
    "Animal instincts, reflexes that allow you to dodge a clawed blow, to survive where you're not supposed to survive."
    "After I stepped into the square, it was my instincts that actually forcefully turned me somewhere in the direction - into the bushes, onto the path, the way of the old-timers."
    play sound sfx_bush_leaves
    "There, where we…"
    scene bg ext_path2_day with dissolve
    "That's right."
    "An ochre-painted steel frame with a chain-link fence, a tiny stream nearby."
    "And by the fence itself, a pair of sandal tracks."
    "Slavya, afraid of heights, took her two meters here."
    "Running from herself, from her thoughts - trying to the last to think not of herself, but of others."
    "As she said - a world where everyone will be given a chance. The first, the second... A chance."
    "But not out of nowhere - but as a result of painstaking and hard work."
    "In my world, it would never work - we exist by different laws."
    "But here, in this frozen fragile balance of trust and brotherhood that can be broken simply by turning too sharply..."
    "Perhaps, only here is it possible."
    "You just have to work hard at it."
    if alt_day_binder != 1:
        "To meet the silly pioneer off the bus, not to go feed the puppy."
        "Smile at him, heartily, friendly, happy to see a new face, vividly interested in who he is and what he is."
        "Taking him under the arm and letting him get closer, even closer - friends at first sight? Why not."
        "That might work here."
    "When trouble is on the doorstep, don't howl hysterically, shifting the blame from bad to worse, but ask quietly to leave."
    "Ask to let her work it out for herself."
    "I found her practically by the fence, a couple of dozen yards away."
    sl "Life will find a way anyway."
    "Turning to nothing, she said."
    scene bg ext_sky_7dl with dissolve
    sl "Life. The most beautiful power in the world."
    sl "I wish we were friends. That you would meet me in the evenings when I come home from school or work, tired but happy to be waiting for me at home."
    sl "So that from the moment we met - until one of us goes into the void, into the great Nothing."
    sl "And you know how great it would be if it happened at the same time - me, already old, you, also not young."
    sl "We'll be looking at the sky for a long, long time before we realize we're not looking with our eyes anymore."
    sl "Looking with something else."
    "She turned gustily in my direction."
    play ambience ambience_forest_day fadein 3
    scene bg ext_path2_day at zenterleft
    show sl sad pioneer at cleft
    with dissolve
    sl "Do you fear death, Semyon?"
    "She asked."
    sl "Imagine that you had done everything you wanted to do in life - would you be able to let yourself go then?"
    me "Yes."
    "I answered honestly."
    "Now that I knew what awaited me on the other side of the Line, questions of life or death were perceived somewhat aloof."
    "It's almost here, I can only delay the inevitable."
    sl "And your loved one? Would you be able to do your loved one that favor?"
    me "What kind?"
    sl "I planted a tree. Because it can't all just be there, can it? Right?"
    me "Sure."
    show sl normal pioneer with dspr
    stop music fadeout 3
    sl "Pirate will live - at least let it be so."
    "Slavya rose from her knees and rubbed her eyes with the back of her palm."
    play music music_7dl["gonna_be_ok"] fadein 5
    "Now it would be quite expected to go through my pockets and give her a handkerchief."
    "But I've never carried handkerchiefs with me."
    sl "Thank you."
    "Thanked Slavya, blotting the corners of her eyes."
    sl "So you ran away from the concert, huh?"
    me "As you can see."
    "I spread my hands, trying not to smile too defiantly."
    "Although I directly violated her request."
    me "I realized that I can't have fun while you're here. Although, what «have fun» can be there."
    "And she has every right to be displeased with me."
    show sl serious pioneer with dspr
    sl "You shouldn't have come."
    "And she's absolutely right."
    me "Shouldn't - because it's wrong? Unfair? Not according to someone else's made-up laws? Why?"
    sl "Because you're an unnecessary reminder that I only think of myself."
    "Slowly she said."
    sl "Selfishly took away her chance, her second chance at making something work."
    sl "Didn't pay for anything."
    "She stood there looking at me in silence."
    "With the dry, empty eyes of a man who was about to do something he would regret for the rest of his days."
    "Very often that very end is very, very far {i}not{/i} away."
    show sl normal pioneer with dspr
    sl "Semyon, I think we'd better..."
    "Who'd let her finish."
    scene cg d5_sl_kissing_7dl with flash
    "Here I stand, listening to her silly confession, which like a broken record keeps bouncing and bouncing to the same track."
    "And there's a record of bass solos, coughing in the background, and endless calls for trouble on my own head."
    "And here - I'm already clutching it in my hands so tight I think my ribs are going to crunch a little more."
    "Kissing - painfully, biting the lip."
    "The infallibility of her paladinism has one unpleasant quality."
    "She is almost incapable of doubting what she believes."
    "Still a child's psyche allows for a little flexibility in judgment, but if she were to finish her 'break up' now..."
    "I can even imagine her backward-looking, reversal-logic consistency in framing this postulate, constructing irrefutable arguments."
    "Infallibility - because yes, from her point of view she did a mean-spirited and selfish thing."
    "And therefore deserves no reward."
    scene bg ext_path_day at zenterleft
    show sl normal pioneer close at cleft
    with dissolve
    sl "Semyon, I..."
    "But I silenced her by putting my finger on her lips."
    me "Slavya, I have a confession to make to you."
    me "Before you get yourself so wound up that it's too late to say anything."
    show sl surprise pioneer close with dspr
    sl "Confess to what?"
    me "You see, there's a point you're missing while you're executing yourself here."
    dreamgirl "Do you want to tell her...?"
    me "Although I don't argue - yes, at first glance it may seem like you, all nice, and suddenly in an important situation you thought only of yourself."
    me "But it's more complicated than that."
    with fade
    stop music fadeout 3
    me "You see, the thing is"
    if alt_sp >= 6:
        extend ", that there, back where I'm from, I died."
        play music music_7dl["please_reprise"] fadein 3
        show sl scared pioneer close with dspr
        sl "WHAT?!"
        "Slavya pressed her hands to her mouth, looking at me with wide-open eyes."
        me "What you heard."
        "I snapped back."
        me "I ended up here by accident."
        me "Though, of course, how can I put it?"
        if loki:
            "I can think of one face--or rather, one face or snout--to whom this incident has made me very happy."
            "For at his suggestion, I am now sunbathing at thirty-five degrees below zero, gently acquiring the consistency of a fresh-frozen fish."
            me "Right now what's left of me is not viable. Even if they put me in the ambulance right now."
            me "There were four of them, and they were very angry."
            sl "They... you..."
            "Slowly said Slavya."
        elif herc:
            me "The thing is, back home, I'm a kind of watchman, a guard."
            me "And being a watchman comes with certain dangers."
            sl "Are there burglars?"
        else:
            me "Same situation which is often described as «an accident», and then gets jokes made about it."
            me "Bridge over the Neva, icy ice, driver couldn't cope with the steering."
            sl "So you drowned?"
        "I nodded."
        me "I don't know how much time I'd have - back home."
        me "But I highly doubt I would have been able to help your puppy."
        if loki:
            me "We'd both freeze there, that's all."
        elif herc:
            "Unless Zinka could, by her feminine instinct, smell a creature in the puppy that needed looking after."
        else:
            me "As you yourself understand, from the bottom of the river I can't help anyone."
        sl "So why did you propose, if..."
        "She bit her lip, pondering tensely."
        if herc or loki:
            me "Sunny, Leningrad is a city, you know? A megapolis. Somebody would have been there for sure."
        me "And even so, it would have been some chance, however vanishingly small."
        me "I don't aspire at all to occupy a place two meters below gravestone level, but I just had to offer that option, too."
        "I thought about the reasons, and it naturally slipped out of my tongue:"
        me "Because I have an obligation to fit in with my girlfriend."
        dreamgirl "Pompous turkey."
        th "Shush."
        sl "So I didn't choose between whims and saving lifes?"
        "I shook my head."
        me "You were only choosing whose life to give a chance."
        "Not that I cleared her conscience completely, certain doubts in her soul remained."
        "But the most important thing, the understanding of the situation, I gave her."
        "And then it's up to her."
        scene bg ext_camp_entrance_day at zenterleft
        show sl normal pioneer at cleft
        with dissolve
        "Slavya smiled softly and hugged me."
        sl "Thank you..."
        "She whispered."
        me "What? Why?"
        sl "For telling me everything. It must be very frightening for you to live with that burden?"
        me "No."
        "I shrugged it off."
        me "To tell you the truth, I only just remembered it, it hasn't been twenty-four hours yet."
        sl "That means..."
        "The girl bit her lip."
        me "Means, means."
        "I stood still, making no attempt to get out - though it was a little awkward to be cuddled up in the pathway at the very gate."
        "So I spoke a little grumpily. It helped with the embarrassment."
        me "I'm not going anywhere, not now, not ever."
        show sl smile pioneer with dspr
        sl "What about your parents? You know, the ones here."
        me "Do I know? When we get home, we'll see who they are."
        show sl smile2 pioneer with dspr
        sl "You've got an answer for everything."
    else:
        extend ", that I was suggesting it because that old dick wasn't telling the whole truth."
        play music music_7dl["unforgotten"] fadein 3
        dreamgirl "What the fuck are you talking about, Jesse?"
        me "I mean, I'm really not really from this world, but..."
        show sl serious pioneer with dspr
        sl "What?"
        me "I don't know how I got here. And I don't know how I can get home."
        me "It's far from certain that his advice would have worked."
        show sl sad pioneer with dspr
        sl "But then why did you offer?.. Making me choose..."
        me "Desperate situation... I don't know who yanked me under the arm to rush forward, waving magic wands and acting like a savior."
        me "I'm sorry, anyway."
        "I put my head down."
        me "There was no choice, the Pirate had no chance - no chance at all."
        th "Except one tiny tragedy with a life gone."
        me "I'm sorry."
        "I put my head down."
        th "Forgive me for not telling the whole truth."
        th "I'd rather you think I'm a blabbermouth who guiltlessly worries others."
        th "Than understand between what and what was really your choice."
        "Though I couldn't say I was directly that upset by her decision in my favor."
        "Of course, I'm sorry about the puppy, really sorry."
        "But not so much that I was willing to die to save him."
        "Slavya was silent for a long time, thinking intensely about something."
        "And she really had a lot to think about."
        "For example, remove attitudes of self-deprecation, self-defeating, self-flagellation and a whole bunch of other «self-» things."
        "But if she treats me lukewarm now, well, I understand. I deserve that, too."
        "Something touched my shoulder, and I slowly lifted my head."
        scene bg ext_path_day at zenterleft
        show sl normal pioneer at cleft
        with dissolve
        sl "Semyon, I'm very unhappy with you, do you understand that?"
        me "Yes."
        sl "And after a joke like that, it really would be best if we parted ways."
        me "Well, that's true, too."
        sl "But I gave myself a chance. On my own. So I can give you one, too."
        "She came up to me and hugged me a little tensely."
        sl "Just don't lie to me again, do you hear?"
        "She stiffened when I didn't hug her back, standing with my arms at my sides."
        "With difficulty trying to understand one simple thing."
        th "Am I forgiven?! Really?"
        "Because I - definitely wouldn't."
        scene cg d5_sl_kissing_7dl with flash
        "I hugged Slavya as hard as I could, choking for a second on the happiness pounding in my temples."
        "And was honored with a kiss."
        "Or was she the one who was honored?"
        "I responded to the snicker from the bushes in my usual phlegmatic spirit, with my middle finger pointing toward the source of the annoyance."
        scene bg ext_camp_entrance_day
        show sl normal pioneer
        with dissolve
        sl "Oof..."
        "She came off."
        sl "You have to breathe sometimes, don't you think?"
        me "No."
        "Foolishly I replied."
        "And smiled."
    "I don't know what I did or how I did it, but it worked, Slavya relaxed a little."
    sl "Alrighty, let's go pay our debts - and we have lots of them!"
    me "What kind of debts are those?"
    "Slavya rubbed me on the top of my head."
    sl "Accumulated! While I was hysterically celebrating and you were comforting me."
    "She grabbed my arm and dragged me along toward the stage."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day6_sl_cl_sonic:
    scene bg ext_stage_big_clear_day_7dl with fade_red
    play ambience ambience_camp_center_evening fadein 3
    play music music_list["always_ready"] fadein 3
    "At this time Miku, with a pathos worthy of the best DJs on the planet, with her little finger gracefully set her last phono signal to zero, and Olga Dmitrievna made her way onto the stage."
    sl "Oh, no!"
    "Slavya exclaimed."
    sl "I was supposed to close the concert. I let everybody down."
    me "It was only now that Slavya began to realize that she had messed with a loser. But the main trials were still waiting for her!"
    sl "Semyon, let's go faster to the stage, maybe we can still...."
    mt "And that concludes our concert."
    "As if to answer her, the counselor announced."
    mt "First squad, gather around the stage, please."
    "We ran up to the stage itself, and Olga Dmitrievna gave us an angry look."
    "But immediately she softened - apparently she remembered that Slavya had special circumstances."
    "She nodded at us, allowing us to join the pioneers who had huddled together."
    scene bg ext_stage_big_clear_day_7dl at zenterleft
    show mi smile voca at cleft with moveinleft
    show dv normal pioneer2 at cright with moveinright
    show un shy pioneer far at fleft behind mi
    show el normal pioneer far at fright
    with dissolve
    show us laugh sport at center with easeinbottom
    "Everyone seems to be here."
    "Except for Shurik - Viola asked for him. And, of course, the Buzzer, as usual, sleeping in the library."
    dv "They'll make me carry something again, for sure."
    show us grin sport with dspr
    us "Don't you be afraid of me, work - I won't touch you!"
    "Slavya stood like that, holding my hand."
    show mi dontlike voca with dspr
    mi "Aliska, don't be a boogeyman, you'll be the first to dance!"
    dv "Yep. From a low start straight into a cart."
    "Alisa snorted mockingly."
    dv "Who to dance with? It's either the mushroom or the autist."
    $renpy.notify('Childish taunt')
    dv "Cavalier, cavalier, chugging beer."
    "Slavya frowned a little, but said nothing."
    dv "Either with a retard."
    "The redhead mercilessly continued."
    hide mi
    hide un
    hide el
    hide us
    with diam
    show sl angry pioneer at center with easeinright
    show dv shocked pioneer2 at right with easeinright
    with vpunch
    sl "Alisa, watch your mouth!"
    "Slavya couldn't stand it."
    me "It's nothing."
    "I tried unsuccessfully to calm down the rampaging blonde, but she seemed to have a reed under her tail."
    me "Slavya, it's okay, she's just..."
    sl "Or do you think I don't know why you're so mean to him?"
    sl "So I know! I'll tell you!"
    "She flashed her eyes."
    if alt_day_binder != 1:
        sl "You've been wooing him since day one, patting him on the shoulder, smiling at him like a buddy."
        sl "And this praise of yours - «not as hopeless» and «not as much of a retard»!"
    else:
        sl "Ever since the day I stole him from you at the wharf."
        sl "You went mad!"
    sl "Are you in love with him?!"
    show dv guilty pioneer2 with dspr
    dv "Who? Me? Are you serious?!"
    "Alisa laughed, but somehow unnaturally."
    "Everyone stood and looked at her in silence."
    dv "Are you a fool to say such things?"
    show sl normal pioneer with dspr
    sl "And you keep calling him a rookie or a retard, as if he doesn't have a name."
    "Slavya calmed down and methodically finished off her opponent."
    th "And why is she so pissed off?"
    sl "If you don't care so much, what's his name?"
    show dv angry pioneer2 with dspr
    dv "Feoktistova, if you want to fight... In the evening on the pier."
    hide sl with dissolve
    "The redheaded wreck walked through the formation, shoulder tossing a gaping Lena so that she almost fell."
    "And bumped into me. Somehow not in a hurry to leave."
    stop music fadeout 3
    show dv rage pioneer2 close with dissolve
    dv "Rookie."
    "She roared."
    play music music_7dl["anglegrinder"] fadein 3
    dv "Are you going to step aside, or am I going to walk over your dead body?"
    me "First, here."
    "What moved me? Why was I such a fool?"
    "I don't know."
    "Alisa was smaller than me."
    if herc:
        "But an enraged marten is a very dangerous opponent."
    else:
        "But hardly weaker."
    "I held out my hand, forbidding it to tremble."
    "And pointed my finger toward the speakers."
    me "We get the disco ready, and only then do we leave."
    show dv angry pioneer2 close with dspr
    dv "Make me."
    "Alisa's husky voice dropped to a snaky hiss."
    me "Why? The pioneers will make you. When they find out it's your fault they won't have a farewell disco."
    dreamgirl "Semushka-Semchik, are you aware that you perform somewhat out of character?"
    "Oh, I was well aware of how unfamiliar this role is to me."
    "How thin the ice is that I'm stepping on."
    "But it's like listening to good symphonic music: courage adds 50 percent to motivation, 30 percent to recovery."
    "And a hundred percent to willpower!"
    me "So you can hit me if you want, but we're all going to go now and help Miku with her dance prep."
    show dv normal pioneer2 with dspr
    dv "Yeah?"
    "Alisa, calming down, tilted her head to the side."
    dv "Well, I can't say no."
    "She turned to Miku:"
    show dv smile pioneer2 with dspr
    dv "Okay, tell me what to do."
    "Miku started to tell her something."
    "And I relaxed and exhaled."
    me "Now that things have calmed down..."
    dv "Ah yes, I almost forgot."
    if herc:
        "Clumsy, retarded, untrained body!"
        "What's the point of reflexes and reaction speed if I can see it all, but just can't get myself to move fast enough?!"
    else:
        "I didn't have time to understand anything."
        "It all happened too fast."
    "A fist flashed in the air."
    with flash
    play sound sfx_lena_hits_alisa
    pause(1)
    "When life is over, I will meet Death with one phrase: «Hello, darkness, my old friend»."
    scene black with fade
    "Early to relax, early to believe that deep down Alisa was a good girl after all."
    "Slacker."
    dreamgirl "But Slavya's totally right - the redhead has a crush on you."
    dreamgirl "Remember the proverb «who I love, I hit»? {w}It's like custom tailoring."
    scene bg ext_stage_big_sunset_7dl with dissolve
    "I got up off the ground, pressing my palm against my nose."
    "Drenched - at least it's not broken."
    "Alisa, without turning around, stepped back to Electronik, who was fiddling with the speaker, disconnecting the wires and winding them up into coils."
    th "Self-confidence is certainly over the top!"
    dreamgirl "I don't think they have the honor of stabbing you in the back. {w}The boy's code of honor after all."
    "Looking at Alisa, I could not help but believe that she was more observant of that code than anyone else."
    stop music fadeout 3
    scene anim_square_preparty with dissolve
    play music music_list["smooth_machine"] fadein 5
    me "That hurt my nose!"
    "I complained to Slavya, methodically pushing the speaker mounted on the cart."
    sl "Eh..."
    me "Fool, right? I shouldn't have got involved, should've let her go."
    sl "No."
    "Slavya didn't turn in my direction, but I could see the glowing edges of her ears."
    sl "You did something really brave."
    me "For which I am paying. Eh, I didn't sit on the side of the road with a bonnet in my teeth!"
    sl "You won't be able to."
    "Here the concrete path ended, we had to double our vigilance to keep the rarity speakers from bouncing on the rocks."
    "The conversation subsided on its own."
    "The question remained, though."
    "And as soon as the opportunity presented itself, I asked it."
    scene anim_square_preparty at zenterleft
    show sl smile2 pioneer at cleft
    with dissolve
    me "So what's to stop me from sitting on the sidelines?"
    me "I'm not bragging or anything. But that's something I know how to do perfectly - sit on the curb."
    show sl shy pioneer with dspr
    "Slavya was a little embarrassed, clutching at her braid and looking at me sideways."
    sl "Promise not to be offended if I tell you?"
    me "Women's logic - first ask not to be offended by a nasty thing, then say that nasty thing?"
    sl "Something like that, yes."
    me "Okay. As you please."
    "With a light heart I promised."
    "Slavya held a special place in my heart from day one - even if our funny affair hadn't worked out, she would still mean something."
    "In particular, I wasn't able to be resentful or angry with her."
    "Meaning - at all."
    dreamgirl "That's because she's good at maneuvering around all the sharp corners."
    th "I don't think that's all it is."
    me "I promise not to be offended by anything you say."
    show sl happy pioneer with dspr
    sl "Look, you asked for it!"
    "She warned."
    "And, after some thought, she began:"
    show sl normal pioneer with dspr
    sl "You may not have noticed, or even paid attention."
    "There are dreams that make you wake up with a pillow in tears."
    with fade
    sl "Or just didn't think it was worthy of attention."
    "There are dreams after which you want to cosplay Ronnie McNutt - or, on the contrary, cramp, gasp, live."
    with fade
    sl "But you've changed, Semyon."
    sl "Camp has changed you."
    "And there are dreams from which you never wake up, and in your body someone who is not you, someone else, opens your eyes."
    sl "And me."
    sl "The old Semyon no longer exists."
    "Because the dream has changed you."
    show sl serious pioneer with dspr
    "We unloaded the speaker next to Genda and gave Miku the go-ahead to plug it in."
    sl "You didn't stand by because you're stupid or want to show off for me."
    sl "It's because you can't do otherwise."
    me "Practically a prophecy."
    sl "Sure, you can make an effort to go back to who you were before."
    sl "But think for yourself whether you have to."
    show sl smile pioneer with dspr
    sl "And now our work here is done, we can go refuel before the dance."
    stop music fadeout 3
    return

label alt_day6_sl_cl_supper:
    scene bg ext_dining_hall_near_sunset with dissolve
    play ambience ambience_camp_center_evening fadein 3
    "Not everything I've done here would make me proud."
    "But there are some really good deeds to my credit, too."
    play music music_list["silhouette_in_sunset"] fadein 3
    "In my own way, I was sinless, otherwise why would an angel like me have come to me?"
    "Though I don't want to be proud or brag about it."
    "It's not my thing."
    "Slavya won't approve."
    "Oh, that's an important statement from Sir Simp."
    "Seriously, though, I think I've learned on some level that she simply won't be interested in the old me."
    stop ambience fadeout 3
    play sound sfx_open_door_2
    pause(1)
    scene bg int_dining_hall_sunset with dissolve
    play ambience ambience_dining_hall_empty fadein 3
    "Or rather, she will, of course - Slavya likes people in general."
    "But not for long."
    "And not in the capacity I plan."
    "As they say «I love the you that you pretended to be until now» — and then the divorce and the nightstand between the beds."
    "With a cactus."
    "While we were loading and unloading, the whole pioneer brethren had already managed to pound down a festive farewell dinner, leaving only empty cauldrons and dirty tables in our wake."
    "Enemies. What else can I say?"
    show sl normal pioneer at zenterleft
    sl "Sit down for now, I'll think of something."
    me "You'll think of something? Aren't we entitled to an increased ration for working for the good of the Motherland now?"
    sl "If Olga Dmitrievna had managed to get here in time to hold our supper, maybe. But she was working with us... Or rather, she still is."
    sl "Hungry!"
    mt "Not so hungry."
    hide sl with dissolve
    show mt normal pioneer at cleft with dspr
    "The door slammed, and the pioneers, led by Olga Dmitrievna, came running in."
    mt "But if you feel like it, you can feed me, too."
    "The remaining pioneers, led by Alisa, settled at a nearby table - Miku, Lena, Ulyana, Electronik - and tapped their spoons in tune, chanting: 'F-o-o-d, f-o-o-d'!"
    "Shaking her head, Olga sat down next to me."
    "She looked tired."
    "How could she go to a dance in her condition?"
    show mt laugh pioneer at center with dspr
    mt "Don't worry!"
    "She laughed."
    mt "The last day is always a busy one, but I'll always have energy left for dancing, too."
    mt "So watch out, I'll want to dance with you too."
    me "You'll have to catch up with me first."
    "I muttered, and Olga laughed."
    mt "Syom Syomich, you don't change at all."
    me "Yeah? Well, Slavya told me that I've changed a lot."
    show mt smile pioneer with dspr
    mt "No way. You, Semchik, are the most constant thing in the world."
    mt "Still as grumpy and stable as a glacier in Greenland."
    mt "Sometimes I think you get into all sorts of trouble on purpose, just to get a little bit postured and hurt."
    "She winked and nodded at Slavya approaching us."
    "The activist was balancing a tray and six plates pioneer-style made up between her palms and forearms."
    sl "Raid is open!"
    "The horde from the next table immediately snatched all her plates away from her and sat back down."
    "It all happened so fast I didn't have time to understand anything - a swarm of locusts, that's all."
    scene bg int_dining_hall_sunset at enterleft
    show mt normal pioneer at cleft with moveinleft
    show sl normal pioneer at right
    with dissolve
    me "Thank you!"
    "I thanked my savior, who seemed intent on feeding me all the time."
    "Not that I mind."
    "I'm all for it. Give me some more of those buns and potatoes. Thank you."
    scene cg d1_sl_dinner_day_7dl with dissolve
    "Slavya smiled, taking a seat across from me."
    "A touching picture would be appropriate now - me sitting like this, eating everything, while my beloved savior, propping her chin on her palm, watches me with a touching look."
    "The picture is cheesy, well!"
    "But Slavya was alien to hackneyed stereotypes."
    "She fraternally divided the contents of the tray into three portions-so that everyone got an equal share of potatoes and a couple of cutlets and something else."
    "Didn't get a good look. It was over too fast."
    me "Bon appetit."
    "The girls muttered something in unison, and I hurried to follow suit."
    "That's right - the eaters at the next table might as well be done with what they've been given and come looking for more."
    "And anything their naughty hands can reach is considered extra."
    scene bg int_dining_hall_sunset at zenterleft
    show mt normal pioneer at cleft
    with dissolve
    mt "Semyon, you can't take care of yourself."
    mt "And your girlfriend has no time for that."
    "The squad leader started, when we had successfully finished our provisions."
    mt "Although you did take over most of her work today."
    me "So?"
    "I clarified, not quite sure what she was getting at."
    th "I hope she's not going to make a Violetta Cernovna-like joke about contraception?"
    mt "But I'd like for you to have a farewell party without it becoming something casual."
    mt "That's why I've made arrangements with Miku - there's an outfit waiting for you for the evening."
    mt "No frills - just the way you like it: strict cut, dark color, no jewelry."
    "Slavya winked at me."
    show sl smile pioneer at right with dspr
    sl "My cavalier will be the most handsome!"
    me "I wanted to ask..."
    "Mumbled me."
    mt "So let's go home and change first - and don't let me see you on the dance floor in your uniform, got it?"
    hide mt with dissolve
    "The squad leader left without waiting for an answer."
    th "I understand that if I run after her right now, I can arrange a «fortunate coincidence»."
    "Because she certainly has that beautiful dress she wore at the last dance."
    "It's strange in general that I, having dwelt around her so much, never once got into any silly situations related to it."
    if dr and (counter_sl_7dl == 0) and (alt_day_binder != 1):
        dreamgirl "What about Ulyana and the dousing?"
        th "Well... I got help messing up there. And I only take credit for cases where I messed up myself."
    with fade
    show sl smile pioneer with dspr
    "Slavya came up, taking the dirty plate from me."
    sl "Then in half an hour in the square, okay?"
    "I nodded."
    sl "And be dressed up!"
    "The wish was a strange one, but I agreed to it, too."
    "And walked out of the canteen."
    play sound sfx_open_door_strong
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_sl_cl_dance:
    scene anim_square_preparty with dissolve
    play music music_list["lightness"] fadein 5
    "The path twisted and twisted and led me here, this evening, alone with my impending departure and the unknown what awaits after it."
    "Of course, there's plenty of fantasy in my life, too - at least remember how I got here."
    "And this is a precedent. Where there's one, there's another."
    "I'm not immune to the possibility that suddenly, right now, I'll open my eyes and wake up... I mean, not wake up. Well, in short, understandable."
    "On the other hand, I shouldn't rule out the fact that I'm probably here forever."
    th "It's like all my favorite books about how a man - not sewn on a mare's tail at home - turns out to be very relevant and useful somewhere in another time, other circumstances..."
    th "Another world, for that matter..."
    th "And, of course, in a completely different environment."
    show mt normal pioneer with dspr
    mt "You're going to change, aren't you?"
    "The counselor reminded me."
    me "Yes."
    "Slavya wanted to see me dressed up, Olga wanted to see me dressed up."
    stop ambience fadeout 2
    scene bg ext_house_of_mt_sunset
    with dissolve
    play ambience ambience_camp_center_evening fadein 3
    "As if wearing a shirt instead of a uniform would make any difference."
    "No, I'm not arguing - if that's what they want, if that's the meaning they put into all this grimacing, please, I'll play along."
    "But don't expect the same attitude from me. Personally, my role of «dumbass on the dance floor» is already perfectly performed by me in a uniform."
    dreamgirl "You can take selfies that you'll be proud of for the rest of your life."
    dreamgirl "Imagine: you, of indescribable beauty, next to Slavya in her ornamented dress, you hold a cell phone on your outstretched hand and make a «duckface»."
    play music music_list["smooth_machine"] fadein 3
    stop ambience fadeout 2
    scene bg int_house_of_mt_sunset
    with dissolve
    play sound sfx_unlock_door_campus
    pause(1)
    play ambience ambience_int_cabin_evening fadein 2
    "Not listening to the chatter of the eternal interlocutor, I went inside and slammed the door behind me."
    "There were some shoulder pads waiting for me on the closet door on 'my' side of the room."
    "A burgundy to black shirt, black slacks with an arrow."
    "I threw the outfit on the bed along with the hanger and caught a glimpse of myself in the mirror."
    scene cg d3_me_mirror_white_7dl
    dreamgirl "You do know how to make a «duckface»? C'mon, let's train."
    dreamgirl "In front of the mirror, pull your lips forward and make your face look silly. {w}However, in your case, it's enough just to be yourself."
    th "Screw you."
    dreamgirl "Okay, okay, you can do nothing to your face - but pull your lips out by all means. And make glassy eyes."
    th "And why am I listening to you?"
    dreamgirl "Because farewell night is such a time... Ah! Everyone needs a leader, everyone is bound to stop by."
    play sound sfx_knock_door7_polite
    "I hastily pulled my shirt unbuttoned and allowed:"
    me "Come in!"
    play sound sfx_open_door_2
    pause(1)
    scene bg int_house_of_mt_sunset
    show un normal pioneer with dspr
    un "Oh. No Olga Dmitrievna?"
    me "No, just me."
    dreamgirl "And while we have five minutes, get undressed!"
    me "That's... I-I'm changing."
    show un shy pioneer with dspr
    "Lena noticed my disheveled appearance and instantly blushed."
    un "S-Sorry... I'll probably come back later."
    dreamgirl "No! Let's indulge in free love! And then you'll look for fleas in me!"
    play sound sfx_close_door_1
    pause(1)
    hide un with easeoutleft
    "Lena vanished."
    dreamgirl "So here we are."
    "The inner voice continued as if nothing had happened."
    dreamgirl "Everybody wants auntie Olya."
    dreamgirl "Notice - not you, the young, handsome one, but her! The old and boring counselor."
    th "Come on, she's twenty-five."
    play sound sfx_knock_door2
    me "What, are you all in cahoots or something?"
    "I muttered."
    show mi smile dress with dspr
    "Miku was in the room before the knocking stopped - I didn't even cover myself."
    "Her own fault."
    mi "Oh, Senechka, do you know where auntie Olya might be, because I've been looking for her everywhere, and she was supposed to give me something, and she didn't!"
    "In one word said the Japanese girl, dressed in some indescribably beautiful dress."
    "Not like that the previous one, the stage one, wasn't beautiful - but this one was - ugh!"
    me "She's in the square. Warming up the crowd."
    "I politely replied."
    mi "And you're dressing up? And even in the dance outfit I picked up?"
    show mi normal dress with dspr
    mi "And you have taste! Thank you for telling me where the squad leader is."
    hide mi with diam
    "She teleported away."
    dreamgirl "But they're all looking for you - which means there's every chance for one of the seekers to catch you with a duck face! Isn't that wonderful?"
    th "You call camp-wide shame wonderful?"
    dreamgirl "You're not? Think what kind of PR that is! So many people will talk about you, you'll become a popular person."
    th "No, thank you - I don't need cheap publicity. {w}Those who are important to me have heard enough about me."
    "Though I don't argue, it would have been nice if she'd stopped by before the dance."
    "Hopes, dreams, fantasies..."
    "After squeezing into my long-suffering outfit, I went to the mirror and took a critical look at myself."
    play sound sfx_open_cabinet_2
    scene cg d3_me_mirror_bordo_7dl with flash
    "It's not that sad!"
    "No, I understand that all black is usually worn by schizoids, and with my pale face I don't even need to confirm the role..."
    "But it did look classy and interesting."
    "Even in this enlightened 21st century, you wouldn't be ashamed to wear it out in public."
    "Unless you had to worry about tying some kind of tie - and I never had any love for them, they taught me, taught me how to tie windsors, but I never learned them."
    "It's just a skill, though. A skill."
    "And any skill is subject to development-the longer you do something, the better you get at it. And that goes for everything from playing Sim City... sorry, Sim Camp, of course."
    "To painting, to playing musical instruments..."
    "And yes. Tying ties."
    "Although I'd probably have to grow out of my sweater to do that."
    "I've always felt sorry for men who live in their shirts and jackets - a nightmare, if you ask me."
    "A whole layer of really good stuff just goes by."
    "Just like with tan jackets, by the way."
    "If I were asked to choose between a douchie from my snowboarder friends' latest collection and a leather jacket - I think the choice would be obvious."
    "That's right - because I'm a big-headed prankster."
    "With a satisfied nod, I stepped outside."
    stop ambience fadeout 2
    scene anim_square_party
    with dissolve
    play ambience ambience_camp_center_evening fadein 2
    play music music_list["silhouette_in_sunset"] fadein 3
    "Dances! How much is in that word for the pioneer heart!"
    "I was a little late, so I missed the start of the actual dancing this time - though I'm sure it wasn't without Ulyanka this time, either."
    scene cg d6_dance_alt_7dl with dissolve
    "Miku had apparently already found everyone she wanted and taken what she wanted from them - now she was conjuring over the turntables."
    "She nodded hello to me and clutched at the microphone."
    mi "Good evening, «Sovyonok»!"
    "The pioneers responded out of line and out of order."
    mi "HEY, DID YOU NOT EAT ENOUGH PORRIDGE? I CAN'T HEAR YOU!"
    mi "GOOD EVENING, «SOVYONOK»!"
    "And this time the pioneers did not fail."
    play sound sfx_concert_applause
    "They shouted and stomped and clapped so that each could no longer hear himself separately."
    mi "That's better!"
    "Shouted Miku, waiting for the flurry of shouting to subside a little."
    mi "We're saying goodbye to camp, but we're glad we came here! I love it here! Did you?"
    "The pioneers shouted something again, and I, smiling, watched the master of ceremonies at work."
    "Miku is an artist to the bone. She can't, doesn't know how to live anywhere but the stage."
    "That's probably why she'll be so appreciative of someone who will one day wait for her backstage with a bottle of warm non-carbonated water, a towel to soak up the sweat, and a blanket to wrap up her momentarily chilled shoulders."
    "I remembered who she was - in my homeland, in my reality."
    "And that's probably why I was so relaxed about all her antics now - she couldn't surprise me any more than life had surprised me."
    "A razzle-dazzle Japanese beauty who gave her face, voice, and stage persona to a computer program, a synthesizer."
    "The embodied nightmare of a luddite, who has taken from man another exclusive right - the right to sing and make the listener laugh and cry."
    "Robots write, read, talk, make payments, let us into the house and light the light bulb in the stairwell according to the motion sensor."
    "Now the robots also sing."
    "It's funny, isn't it!"
    "Just a little more - teach robots to write poetry and fill their heads with nonsense - and we won't need a human anymore."
    scene anim_square_party
    show sl normal dress
    with dissolve
    "I felt a look on my face and smiled at Slavya."
    "Today she was more beautiful than ever."
    "In her dress, in her sandals, forbidding herself to grieve in vain, and trying to honor her pet by going on living."
    "However, she is always as beautiful as ever - you can't take that away from her."
    dreamgirl "«Young lady, your dress is so, so, so! Ah!» — «My panties are just as good!»"
    th "Couldn't help but spoil the mood for the eternal vulgarity."
    dreamgirl "I'm just thinking, man."
    dreamgirl "See, here's the thing..."
    th "What's that?"
    dreamgirl "It's all parting and grieving, isn't it? 'Give a leg up for the long haul' and all that."
    th "Yeah, and?"
    "The DJ changed the record to a slow song, and I started pushing my way over to the girl for the purpose of dancing with her."
    if (counter_sl_7dl == 0):
        dreamgirl "Well, look at you - on the first day you were mocked as a rookie."
        if (herc or loki) and (alt_day_binder != 1):
            dreamgirl "Well, or at least they tried to mock you."
        dreamgirl "In the evening, again, they shoehorned you in for a cutlet."
    else:
        dreamgirl "Well, look - the first night you were shoehorned in for a cutlet."
    dreamgirl "And all that running around with a checklist, too."
    th "The main point, now."
    "I ordered, already realizing where the inner voice was going."
    dreamgirl "I'm almost there. You see, what happened to you suggests that tradition is very strong in this camp."
    th "Perhaps. And?"
    dreamgirl "And now it's the last night. Tradition. You should get some bitches."
    th "You bitch!"
    dreamgirl "Bruh, nah, why? It's a tradition!"
    "I wanted to say something else, but Slavya was there, and it was much more important to smile at her, not caring if anyone was wrong somewhere."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_sl_cl_dancing:
    scene anim_square_party
    show sl normal dress
    with dissolve
    play music music_7dl["stilllovingyou"] fadein 4
    "Song-legend, song-story."
    "I once felt the crushing literalness of the phrase «broken heart», complete with this song as the soundtrack."
    "Yeah, probably the whole generation that grew up, not born in the nineties, has a whole bunch of their own stories connected to Klaus' songs."
    "About hope, about waiting, about loyalty and perseverance."
    "About love."
    "We've already told each other everything we could and everything we should have."
    if alt_day5_sl_cl_hentai_done:
        "Even managed to do something stupid - and that will have its own consequences, too."
    "But I keep getting nervous."
    "It's like... I don't even know. It's like we have multiple modes of communication."
    "In the adventurous, friendly «mode», the two of us have fun and interesting things to do, and we do all kinds of fun things that are fun to remember later."
    me "Shall we dance?"
    "But as soon as you start talking about some romantic nonsense, it's over."
    scene anim_square_party
    show sl smile dress at zentercenter
    with dissolve
    "Slavya smiled and put her hand in mine."
    sl "Why are you even asking!"
    "I cease to be sure of absolutely everything."
    "Knowing Slavya, I realize that her fidelity to some principles, to laws that are written not by men but by the heart - all this makes a rather unpredictable person out of the right pioneer from all sides."
    hide sl
    show sl normal dress
    with dissolve
    "One moment I think I understand her and can tell what she's thinking or what she wants to do."
    "And in another moment she does a feint in her ears and blows the whole gambit."
    if alt_day5_sl_cl_hentai_done:
        "Certainly we made love - that is, I was let in closer than whatever would be possible, inside, under the skin."
        "But no one is going to stop her from telling me tomorrow that sex is no reason to get to know me - since she assessed me from such close quarters and realized that she would only be a nuisance to me."
        "And all this, of course, solely dictated by concern for me."
    else:
        "Although, of course, we did bathe naked yesterday and even allowed ourselves some foolishness - after what happened this morning you could."
        "But nobody's stopping her from saying the same thing - she was weak, scared, looking for support and {i}used me{/i} as a comforter."
        "And now feels nasty for her utilitarian attitude and has to bow out."
    "And here I thought the right girl gave her chosen one peace of mind and confidence in the future in the first place!"
    scene cg d3_sl_dance_bordo_7dl
    with dissolve
    me "I remembered so much today."
    sl "What, exactly?"
    "Slavya naturally transcended personal space, space of safety and decency, snuggling up against me so that I could feel her body through two layers of clothing."
    sl "Anything interesting?"
    me "Well, that depends..."
    "Probably should be talking to her about relationships right now."
    "Or better yet, exchange interests."
    "All normal couples do that - they try to understand each other, to find common ground."
    "For example, where the girl likes popular music and the boy is a fan of electronic music, their common ground might be somewhere in symphonic music, movie soundtracks... You name it."
    "Similar with everything else: a hackneyed set of questions about favorite music, movies, interests in life and plans for the future."
    "Once you learn this set, you use it automatically, and the other side understands the automatism of the process, but they still enjoy it."
    "Attention, after all."
    "Instead, I tell Slavya about how one day in the bowels of the «cryptons» the goddess Miku was cast from the quintessence of inspiration and liquid lunar silver."
    "How sullen users (I had to take a lyrical digression here to explain how 'pen palship' or online communication works) brought to life a redheaded, pest-like monster with hair subtly reminiscent of Pikachu zippers."
    "How a black picture - silhouette of a girl with two track tears and two funny bulbous ponytails once saw the light of day."
    "About living at home and why I don't want to go back there."
    "For some reason I don't want to tell her the most important thing."
    "Because I'd have to make promises, say some platitudes..."
    "Not a luxury I can afford in the company of my sunny."
    "It's like getting together in a group where one is more awesome than the other - the four geniuses of poetry, or the Mighty Bunch, or even «Apocalyptica» — where everyone is squeezing out 120 climbing percentages to not just live up to the high bar set by the sirs, but to set an example."
    "In Slavya's company one wanted to be - as hard as one could. Not to be wasted on actions with sleeves or nonsense like vulgarities and platitudes."
    "Conform."
    "And she, gratefully squeezing my shoulder, questioned and questioned what my world was like, and whether I really had no place in it"
    if alt_sp >= 6:
        extend " — had it not been for the tragic outcome of my being there."
    else:
        extend "… Although perhaps things could have turned out differently if it hadn't been for my stupidity and stubbornness."
    th "I'm afraid there wouldn't be room for you there either, honey."
    "I thought to myself with an incomprehensible wistfulness."
    th "If here, in a society where people, people are the priority, the likes of you are vanishingly rare..."
    th "I'm afraid our world is incapable of producing your kind."
    dreamgirl "Another reason to stay here for a while, man."
    "And in that I was in complete agreement with the inner voice."
    "Of course, it wasn't perfect or earthly heaven either."
    "But there was Slavya."
    "And she would be all right everywhere!"
    "The slow dance ended, and the girl reluctantly let go of my shoulder."
    $ persistent.sprite_time = "night"
    $ night_time()
    scene anim_square_party at zenterleft
    show sl normal dress at cleft
    with dissolve
    "But not the hand!"
    sl "Listen."
    "She said."
    sl "It's so noisy here, so many people... Let's go."
    "«And it'll be just the two of us for a little while» — said her stare."
    "Of course I agreed."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day6_sl_cl_debarkader:
    scene bg ext_boathouse_night with dissolve
    play ambience ambience_boat_station_night fadein 3
    play music music_7dl["silent_angel"] fadein 3
    "The night, the street - Bloch's domestic romance."
    "Slavya took me to the wharf, where no one was there at the time, only the inarticulate muttering of a tiny television, peering now and then with a blue-gray eye through the dense curtains of the gatehouse."
    "We should have had more scenes like this, honestly."
    "To be hand in hand, native near and not thinking about anything outside. All problems, like shoes, left at the door."
    "Not running from underground rats or trying to sort out the tech situation in the clubs."
    "But here and now we had the night, we had the moon, and Slavyana in her sundress looked like the youth of this world, and so one wanted creosote, burnt leaves, and the transparent bitterness of St. Petersburg autumn."
    "To wait for the tar to dry from the unintentional October longing, to lie on my stomach, with my head hanging over the edge of the roof, and look down from the sixteenth floor, intertwining my responsive fingers."
    "To stand under the windows until midnight, waiting for a silhouette to flicker against the yellow square of the window."
    show sl normal dress with dissolve
    sl "Do you think we'll get anywhere?"
    "In a strained whisper Slavya asked, stopping at the far railing on the pontoon."
    sl "Because I can imagine how much trouble that would be..."
    me "And your hands down?"
    sl "No! How could you think such a thing?!"
    "I smiled, and she got embarrassed."
    sl "Actually, yes. To be honest. I don't know much about you except a few meetings here at camp."
    sl "And what if they ask about you at home - what am I going to tell them?"
    me "The truth?"
    "I smiled."
    sl "About your world or your locals?"
    "The girl tilted her head sideways, not looking at me, glancing out at the rushing locomotive."
    me "I don't know. We'll think of something."
    "The music coming over here was little by little replaced by another slow composition, the discordant, disappointed shrieks of a youth who thought the girls were either enemies or creatures from another planet."
    "The pioneers reached for the washbasins to cool their hot heads."
    sl "Let's climb on the roof?"
    "Suddenly Slavya suggested, nodding at the hulk of the debarkader."
    me "And let us climb!"
    "I agreed."
    th "Maybe we'll get our share of romance, too?"
    hide sl with easeoutleft
    "Slavya, with experience showing a very good knowledge of where and what to find, found the ladder, put it to the skylight, and a few minutes later, having broken through several layers of cobwebs and scared off the swallows nesting nearby, we rattled the tin roof cover."
    sl "Stay away from the slope, it might be slippery with dew."
    "She warned."
    "She hid for a few minutes in a separate nook, then came back out a little later, carrying a hiker's «foam pillow» — the one I knew, the folding one, the one with the elastic band."
    sl "There's only one, so we'll have to squeeze in."
    "Right away, the girl warned me."
    me "Take advantage while I'm skinny. Or you'll make me fat, you'll need two foams - one for me to lie on, and one for my belly."
    sl "I don't think so!"
    "Slavya laughed."
    sl "It's not as if you've got it in you."
    scene stars with fade
    "She laid me down on the makeshift bed and settled down beside me, resting her head on my shoulder, looking in the same direction as me, at the stars."
    me "Remember our conversation on the first day?"
    "I asked when we finally got comfortable."
    sl "We didn't have one."
    "The blonde giggled."
    sl "All we do is talk."
    "There was a diligent swearing cough from the dance floor - right, what's a country dance without a fight?"
    "A little while later, a suspiciously familiar squeal came from the side of the cabins."
    if (alt_day_binder != 1) and (counter_sl_7dl == 0):
        "After digging around in my memory, I determined that the screeching was most likely Lena's."
        "And it was most likely Ulyana's fault again."
    sl "She did douse her, after all."
    "The girl shook her head."
    sl "Ulyana."
    me "Lena?"
    sl "Yup, her. I don't know why they don't have peace, why she's always making fun of Lena - I've tried to reconcile them, but they seem to have a long history together."
    sl "And I don't want to get into it. I have no right."
    "There was a palpably drunken chant coming from across the soccer field."
    sl "Alisa."
    "And there's a certain animosity here - I can see why, though."
    me "And where did she get it?"
    sl "That's not the problem - Violetta has a supply of medical alcohol. And Uncle Boris has an emergency supply in the hall for holidays and anniversaries."
    me "But that's..."
    sl "Yeah. Stealing. Oh, I have a feeling Alisa's Komsomol invitation will be put off for another year."
    me "So, instead of dancing, our whole squad is wandering around camp now?"
    "It was curious to lie like that on the roof, gazing at the stars and feeling the whole camp - in a way I could never do alone."
    "I felt and understood Slavya for a few minutes, her special type of perception that allows me to see and know everything that happens in the territory entrusted to her."
    "Another leadership skill. Or a talent?"
    sl "Yes... The only one left on the set is Miku - she's the leader, she can't leave."
    me "Why did you and I leave?"
    "I asked."
    me "You don't seem to treat people that badly."
    sl "You know, I'll show myself again as a narcissist, thinking only of myself."
    sl "But between people and you, I choose you."
    sl "Once I chose you, that's it. The claw's stuck, so die, little birdie."
    "She raised her face to me, and I kissed the corner of her tightly pressed lips."
    "The girl was angry, she was angry. Angry at herself."
    sl "So what about the conversation on the first day?"
    "She reminded me."
    me "You said you liked it here, you asked me if I liked it."
    "Her hair smelled like tar. I couldn't resist kissing the top of it."
    me "Let's come here again, huh?"
    me "At least next year, at least just for a visit!"
    "The path of starlight was blocked by a silhouette with wet glistening eyes."
    scene black with fade
    sl "I thought you'd never ask."
    "She exhaled."
    "And when I tried to say something, I choked on the word."
    "Without further ado, Slavya dug her lips into mine."
    "And we both went crazy, on the gentle slope of the roof overlooking the water, the floodplain, and the steel string of the railroad."
    "Closed our eyes and exhaled everything bad that could be."
    "Together."
    "And I finally relaxed and stopped doubting."
    "Whatever Slavya chose, she chose it with me."
    me "Should I take it as «yes»?"
    sl "Shut up and help me get my dress off."
    "She just said."
    "And I, still on the same wavelength as Slavya, felt a growing desire, a tenderness that reeked of selfishness - for it was directed at me."
    "And for a split second I must have been able to convey both that and my own feelings to her, turning the intoxication of the dear one into a whole recursion of tenderness and caring."
    "With this girl the phrase «we love ourselves in others» was taking on a whole new dimension    ."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day7_sl_cl_techno:
    play music music_7dl["vampire"] fadein 3
    scene bg int_mine_room
    show prologue_dream
    with dissolve
    "The door was blown off its hinges, a sharp cut on my cheek as plastic shrapnel ripped through it."
    "The room was filled with men in uniform - angry, bossy, shouting commands in some incomprehensible guttural accent."
    "Though the intonation is perhaps international: drop your weapons, hands behind your head, face the wall or nose to the floor."
    "But what can I do. {w}I can't even move."
    "Just looking at the grayish misty abomination creeping and creeping across the very floor at my feet, shackled in my high-laced boots."
    "So I was just dreaming it all."
    "I glanced at the valve that remained in the closed position."
    "It was a dream."
    "Thoughts ran wild, frantically trying to calculate the situation and find the best way out of it - we were taught that, too."
    "For some reason nothing came to mind except a desperate dash for the gas."
    "But that's what I'm expected to do - get cut off by a burst on the way up."
    "What to do then, eh? What to do?"
    "The situation is critical - I have zero energy, severe blood loss, and only the last grenade from the weapon."
    "They have the advantage in numbers, weapons, health, training... Everything."
    "What can be done in such a situation?"
    "Right."
    "You can only surrender."
    "And I didn't even try to resist when the soles of my boots were licked by the gray shreds affectionately."
    "That's right, if you try to resist, you only hasten the process of disintegration of personality. And I need..."
    "Just a little substitution of a few tiny variables in the equation."
    "To grasp how this abomination affects the psyche, and what makes me so special that I don't care about its effects?"
    "Understand the algorithm. Copy it and apply it."
    "Through the thickness of the earth a signal went into the sky, and a satellite winked out of orbit with a purple lens."
    "Three more minutes later, a copier in one of the support points came to life and brought out a long roll with a bunch of formulas and diagrams."
    "The device, which is to be produced, got a working name of «Algorithm»."
    "A few minutes later a command came over the wires from the same base, and somewhere far away in Siberia the pristine silence of the forest was disturbed by a weary creak."
    "And a cigar-shaped body soared above the surface of the earth on a pillar of fire."
    scene anim_digi with dissolve
    "I saw it all as if in a dream - because I felt myself losing brick by brick my personality - the building material from which the abomination makes a new playing field."
    "Already almost unconsciously - at the level of reflexes, feeling death approaching - I pulled the pin."
    "I had almost forgotten who I was in this life. All I remembered was agreeing to go somewhere at the end."
    "But still, something from the past was so important that it was imprinted in my subcortex."
    "So one day in a camp far, far away, a boy with glasses would assemble an extremely curious device."
    scene black
    "And I woke up."
    "Well, not like that. I didn't wake up, I came back - back into my body."
    th "But that means that all these dreams about the war of the future and other nonsense is..."
    "{b}T{w=0.1}h{w=0.1}o{w=0.1}s{w=0.1}e{w=0.1} w{w=0.1}e{w=0.1}r{w=0.1}e{w=0.1} n{w=0.1}o{w=0.1}t{w=0.1} m{w=0.1}y{w=0.1} d{w=0.1}r{w=0.1}e{w=0.1}a{w=0.1}m{w=0.1}s.{/b}"
    stop music fadeout 3
    return

label alt_day7_sl_cl_begin_sh:
    play music music_7dl["silent_angel"] fadein 3
    scene
    $ renpy.show("bg int_refinery_day_7dl", what = Dawn("bg int_refinery_day_7dl"))
    with dissolve
    "The bed was definitely not mine."
    "I was used to mine, it had a tension boarding, heavy-sprung, rigid."
    "Here I was like on a featherbed, sagging all the way to the floor."
    "My neck stiffened from the unaccustomed position, and I opened my eyes without risking to move sharply."
    scene
    $ renpy.show("cg d5_sl_bed_7dl", what = Dawn("cg d5_sl_bed_7dl"))
    with dissolve
    sl "Hello."
    "Without opening her eyes, Slavya purred."
    sl "It's nice to wake up with you by my side."
    me "I like it myself."
    sl "But I don't like how far away you are, it's decidedly no good."
    sl "Go and warm the girl, lieutenant, do you hear? The girl insists."
    me "An offer impossible to refuse."
    "I muttered, moving from my bed to hers."
    if alt_day5_sl_cl_hentai_done:
        me "Are you okay after yesterday?"
        "A moment of coldness, and I feel someone beside me who I understand completely, who understands me completely."
        sl "Can't you see it yourself?"
        "She smiled, turning her back to me and sagging the tiniest bit."
        "Of course, I immediately put my arm around her waist - who could resist?"
        "All right, not around the waist, a little below the waist."
        sl "Oh, you're quick to respond!"
        "She exhaled in amazement."
        "And I myself, already closing my eyes, tried to make sense of the bonds that stretched between us."
        "And the brightest, fiery orange, shone in the darkness alone."
        me "You're no slouch yourself."
        "I drew the braid aside, and, after fitting in, lightly bit her by the neck, from behind."
        sl "Hey! You can't do that! It's a forbidden place!"
        me "You've got a forbidden spot everywhere."
        "I light-heartedly brushed it off."
        "I had warmed up a little - I didn't want to touch the girl with my cold fingers - and I was pleased to see a herd of goosebumps running down my side."
        sl "Syomushka, why are you riling me up?"
        "She exhaled, turning around."
    else:
        "I had that seventeen-year-old feeling you get when you finally get your hands on the sweet stuff."
        "Like a little kid, except it's not a kid's toy."
        "But the reaction is the same - you'll binge until you puke."
        "When I was about twelve years old, one day at the camp where I was spending my summer, they put out a whole tub of cranberry-blackberry morsel, to which I was a big fan."
        "I drank it and drank it until I was so drunk that just a little more, it seemed like it would pour through my nose and ears from a sudden movement."
        "Same situation."
        "Lock us in a hyperbaric chamber and suspend us in Pluto's orbit, leaving only the oxygen supply to support us, and then we won't freeze to death ourselves."
        if alt_day6_sl_cl_hentai_done:
            sl "Syom, I'm sorry, but I can't right now - I think I should have taken a shower after what we did last night."
            me "What is it?"
            "I'm worried."
            sl "It hurts. {w}Inside."
            "Her back literally reeked of a sense of remorse."
            "And her voice was just as insecure - because I, not getting what I wanted, could just get up and walk away."
        sl "Just hug me? Please."
        "Shocking my rampant libido, I hugged the girl from behind and pressed myself against her back."
        sl "Okay."
        "She purred."
        sl "Will you lie with me?"
        "You don't have to ask stupid questions."
        "I kissed her where I reached - on the back of her shoulder."
        "Eloquent answer."
    "The bed creaked softly - it was an hour before we had to get up."
    stop music fadeout 3
    stop ambience fadeout 6
    return

label alt_day7_sl_cl_begin_pi:
    scene
    $ renpy.show("bg int_attic2_day_7dl", what = Dawn("bg int_attic2_day_7dl"))
    show unblink
    play music music_7dl["slavyas_fantazm"] fadein 3
    play ambience ambience_boat_station_day fadein 5
    "I opened my eyes to the sky peering through the skylight of the attic."
    "There was happiness breathing quietly nearby, and I could no longer separate where my own ended and hers, warm and kind, began."
    "So smoothly, in a gradient, they flowed from one to the other."
    "And it was so good that I was a little even suspicious of what was going on."
    "Of course, there were dirty fingerprints left on the glass masterpiece, the pads slathered in blood."
    "Not everything in our union happened to be perfect."
    "But these cuts are superficial and heal faster than the pain subsides."
    scene bg int_attic2_day_7dl with blind_l
    "The sun had already climbed up into the sky, but it still hung lazily near the horizon, leaving the far side of the sky scarlet and my and Slavya's loft filled with a slew of gray shadows."
    "We couldn't do anything yesterday, not me with all my 'man of the future' conceit, nor the almighty Slavya."
    th "Though we cannot be said to have failed the test of strength."
    th "On the contrary."
    "I pressed the sleepy, sniffling happiness against me a little, kissed the top of my head."
    th "I sent the hell out of her wishes-orders-requests again, and did what was right, not what was convenient."
    "Because if I had obediently folded my paws and waited for her out of the woods, where she would have cried out her sorrow and calmed down - what good would it have done?"
    "Although, of course, I've long been used to labels like «unnecessary», «unreliable»…"
    "They would understand that you can't rely on me. Understand and send me away."
    "And there wouldn't be any «Slavushka+Syomushka», nor would there be a mountain of plans, obscure and therefore even more fascinating, where we - are together."
    "At last someone wiggled beneath me, and one sun opened its eyes, hiding a hidden bitterness behind a welcoming smile."
    sl "Good morning!"
    "The girl greeted me."
    me "And good day to you, too. How did you sleep?"
    sl "As if you don't know."
    "She pulled me to her and kissed me."
    sl "What time is it, don't you know?"
    me "It's early seventh."
    sl "Oh, so it's time for a run and a swim."
    sl "Although... Although..."
    "She looked at me thoughtfully."
    "A wry, wistful look."
    me "What?"
    sl "I suggest we replace the jogging with other physical activities!"
    dreamgirl "Whoa! You got yourself a temperamental chick, Sem Semych! {w}Look how quickly she realizes the benefits of lewd and progressive gymnastics!"
    sl "Let's just go for a swim!"
    "Slavya's voice ruthlessly ruined all of the plans of the inner horny voice."
    me "Bathing?"
    sl "Yes! I loved it so much the day before yesterday, I want more!"
    me "Ah... Okay."
    scene
    $ renpy.show("bg ext_boathouse_day", at_list = [zenterleft], what = Dawn("bg ext_boathouse_day"))
    show sl smile dress
    with dissolve
    me "Are you sure this is a good idea?"
    sl "Oh come on! Who's going to see us here, who needs us anyway?"
    "I shrugged."
    sl "I don't know either! Don't be shy! Come on."
    show sl laugh swim with flash
    sl "Haven't you ever wanted to go crazy?"
    "She shouted, and, laughing, flashing her naked, tanned body in the rising sun, she took a run!"
    sl "Go mad, Syomushka! Come on down with me!"
    "And, flying like a comet, she pushed off from the edge of the roof of the debarker, spread her arms, hovering in the moment of flight-happy, young, glowing."
    "Beloved."
    "And dived almost silently into the water three feet from the edge of the brig."
    hide sl with flash
    me "Crazy."
    "I concluded."
    me "Psychopath."
    "And what a good disguise she was - chorus girl, activist, blonde, eyelashes flapping, wings bang-bang-bang."
    me "Who am I messing with?"
    with fade
    "The chilly morning air sliced my naked body, and I, hooting and hollering like a lunatic Indian, accelerated, flung myself into the dawn sky!"
    "Stifled diligently within myself the desire to fly, the desire to return to carefree."
    "Yes, just to return to someone who is glad of you."
    stop ambience
    pause(1)
    scene anim_underwater with dissolve
    play sound sfx_shoulder_dive_water
    scene anim_underwater
    show blackout_exh
    with fade
    "I suddenly realized that the whole world had become an unbearably-black water."
    "The cold took my breath away, so I managed to save some air in my lungs after falling from four meters."
    "There is darkness on all sides, only the leaden heel is wrongly graying above."
    "A meter below awaits a laughing Valkyrie."
    "A maw."
    "She swam up to me, tucked the stirring scythe behind her back, and stared at me, paddling with her hands."
    "Strangely so, evaluatingly."
    "But we've already passed all the assessments!"
    "Or haven't we?"
    "I didn't have time to think about it, because my lips touched soft lips, yanked up hard, and I remembered that I hadn't been breathing for two minutes."
    "And I wanted so badly to let it go, to let it go as it should."
    "But I really wanted to breathe - and the thrill of the black abyss would have to let go, paddle by paddle."
    play sound sfx_water_emerge
    play ambience ambience_boat_station_day fadein 3
    scene bg ext_beach2_day_7dl
    sl "I wonder what it would look like in the water?"
    "Slavya swam in circles around me, frolicking and splashing and being the prettiest thing in the world."
    "And I was afraid it wasn't mine, I'd gotten it by mistake, and the oak door was about to open, and they'd chase me with a fucking broom back to my dusty pigsty, where perfect girls don't exist."
    me "What?"
    play sound sfx_draw_water
    sl "You know what!"
    "She blushed a little, splashing me again."
    "I was getting a little used to the water by now, though it was still a healthy colder than I needed to feel comfortable."
    with fade
    "Slavya, on the other hand, didn't seem to feel any discomfort at all - on the contrary, she was only energized."
    me "In rounds of two minutes, as long as there's enough air."
    "I answered."
    "Or like in the movies - heads sticking out above the surface, everything else below - but it's not in the water, is it?"
    sl "Well, what about then? {w}Two minutes is kind of..."
    "She wondered."
    sl "Wow! You know what!"
    sl "I wish it was in weightlessness! Can you imagine? And there's air, and you can float wherever you want."
    me "You'd have to go into space to do that."
    "Grumpily I replied."
    sl "Well, or then underwater with a tank!"
    sl "Why do you keep grumbling like an old grandfather?"
    "She came up to me and poked me in the side."
    sl "Don't you want something incredible?"
    th "Something incredible is already happening to me. You."
    me "Next thing is you're going to offer me a parachute jump."
    "I bared my teeth."
    "Slavya laughed and headed for the shore."
    sl "And I will!"
    "She shouted, clinging to the ladder going down into the water."
    sl "I've got one brother in the DOSAAF - he'll sign us up too!"
    "We had to somehow magically sneak past the gatehouse, where the watchman was one hundred percent awake from our laughter and gurgling."
    "Then to go up to the brig and get our stuff there."
    th "We don't have to take them yet, though, do we?"
    "Thinking about it cheered me up."
    "There were still two hours to go before the general wakeup."
    stop music fadeout 3
    stop ambience fadeout 6
    return

label alt_day7_sl_cl_incident:
    scene bg ext_houses_sunset with dissolve
    play music music_7dl["will_you"] fadein 3
    "The whole camp was still asleep."
    "Slavya, as a master stager, a set designer, knew her way around, knew how to walk on the other side of the scenery, to show the camp from an unusual, unfamiliar point of view."
    "Here we are now - would it have occurred to me to get up early in the morning to enjoy a little silence?"
    th "And honestly?"
    "That's just it."
    "It's like everybody's gone. Gone or dead."
    "The thought has probably crossed everyone's mind about what it would be like if a silent apocalypse happened one day - you just open your eyes and all the people have disappeared."
    "Gone into oblivion, leaving behind as a living monument all their infrastructures, the contents of store shelves and warehouses."
    "Leaving you alone on an entire planet."
    "When I was about twelve years old, I imagined immediately running to the store next door and picking up anything and everything there, and then to the arcade, in Neskuchny Garden."
    "To the observation deck at St. Isaac's, where I was never allowed."
    "To unhook the boat at Gribozhuy and raft to the Neva, and then to the Ladoga or the Finnish - wherever my heart desires."
    "And nobody, nobody will ever tell me what to do, where to go, or what time to go to bed."
    with fade
    "Ten years later I was able to pick up anything I could get my hands on, but I wasn't happy about it."
    "Neither did slot machines with fighting games and shooters replacing good old-fashioned Battleship add any happiness."
    "The thought-dream of waking up as the last man on the planet hasn't gone away - except now loneliness has become an end in itself."
    "Which I realized in an isolated human nightmare a few more years later."
    "And here you can imagine how everyone has disappeared - although, the local people, every single person, I'm not ready to give up on them yet."
    "They turned out to be too interesting."
    scene bg ext_aidpost_sunset_7dl at zenterleft
    show sl sad pioneer at cleft
    with dissolve
    if alt_day6_sl_cl_arc == 'sh':
        "We were on our way back from the sinks, where I had unsuccessfully tried to wash off the smell of the overdrinking after yesterday, when Slavya suddenly stopped and stopped me."
    else:
        "Slavya suddenly tensed up."
    me "What happened?"
    sl "I think you went around camp yesterday while I was... busy."
    "Quietly she asked."
    me "Yeah, that happened..."
    sl "So you know how to explain it?"
    stop music fadeout 3
    "She nodded at the men in mouse-colored uniforms smoking outside the infirmary."
    if alt_day6_sl_cl_arc == 'sh':
        "Wow, we've only been gone twenty minutes - just a little scrubbing next to the sinks."
        "And here's some serious business already."
        "And then I remembered something that my inner voice had mercifully hidden from me, a black hole in my memories, sucking in my attention."
        th "Thank you."
        dreamgirl "No problem."
    play music music_list["drown"] fadein 3
    if alt_day6_sl_cl_arc == 'sh':
        me "I know..."
        "I answered."
        sl "And?.."
        me "You see..."
        "I began, not knowing how to explain this slippery fact to her."
        me "Yesterday something... Scary happened."
        sl "Scary?"
        me "Yes. You see, Shurik, he..."
        show sl serious pioneer with dspr
        sl "What? Got sick? Again?"
        me "Not that..."
        show sl angry pioneer with dspr
        sl "Although they won't call the police for a simple illness. {w}He's done something wrong!"
        sl "What exactly? Answer!"
        me "He..."
        "And how do I say it?"
        "My parched throat struggles to push the air through - the words just won't fit there."
        sl "Look, I've been waiting longer."
        "She was on her way to the infirmary, and I caught her hand and shook my head negatively."
        me "No. Don't go."
        show sl surprise pioneer with dissolve
        sl "We slept there, what's the problem?"
        me "It's about Shurik. He..."
        sl "What?"
        me "He killed himself."
        show sl scared pioneer with dspr
        sl "What?! Don't joke about such things, Semyon!"
        me "I'm not kidding."
        show sl scared pioneer with dspr
        sl "And you didn't say anything?!"
        me "I'm sorry... I couldn't talk about it. Everything was piling up, those checks, the buzzers, your fainting..."
        me "I couldn't."
        me "I'm sorry. But you shouldn't have known about it yesterday, you already..."
        sl "You should have told me."
        show sl angry pioneer with dspr
        sl "You have to talk about such things, Semyon. Do you hear me?"
        me "Do you want to be honest? {w}I'd almost forgotten it myself. I've had enough trouble without worrying about a person who's too weak to live!"
        "Slavya shook her head condemningly."
    else:
        me "No, I don't know anything."
        show sl serious pioneer with dspr
        sl "Something obviously happened. {w}The police aren't just coming for no reason."
        me "M-maybe... Don't?"
        sl "Semyon!"
        me "I just have a feeling... I don't feel good."
        "The squat house with the red cross flag reeked of hopelessness and death."
        me "Let's let people finish their work and then we'll climb in."
        show sl angry pioneer with dspr
        sl "You know, sometimes I don't think you've changed a bit at all."
        "Slavya shook her head angrily."
        sl "How can you be so indifferent?! {w}Don't you care why the police is here?"
        me "I do care. {w}It's just that I already know."
        th "Bobby with uncles in uniform never, ever meant any good."
        "Because according to the song of those very uncles in uniform, their service should be discreet in the first place. {w}And the less of them we have in our lives, the better that service is."
        "Like Henry Ford's factory - an artel of adjusters only got paid for the time they were idle, and they did the fixing and straightening of the machinery at their own expense."
        "Very conducive to prompt and quality repairs."
        sl "I'll go find out."
        "The girl notified me."
    "And headed to the infirmary."
    with fade
    "Went up to the porch, wanted to go up..."
    voice "Hey, {b}kiddo{/b}, where are you going?"
    "A man in a uniform shirt, looking suspiciously familiar, asked."
    sl "I want to know what's going on in there."
    "Clearly she reported - just didn't give the salute."
    "The man shook his head tiredly:"
    voice "You don't want to go there. {w}Honestly."
    voice "You'll see enough in your life. Take it out!"
    "Shouted the man."
    voice "Make way, {b}kiddo{/b}, as if anything wouldn't happen…"
    "Slavya stepped off the porch and stepped toward me, letting a procession of two burly men in white coats with their valuable cargo pass by."
    "Past us carried a crude stretcher on metal tubes, on which lay something tightly covered with a tarp."
    "Something resembling a human figure."
    "Slavya, hands clasped to her mouth, conducted the stretcher with a glance, and helplessly shifted her gaze to me."
    me "I don't think we should disturb Viola now."
    show sl sad pioneer with dspr
    sl "Yes."
    me "She's in enough trouble as it is."
    sl "Right."
    me "Let's go ask Olga Dmitrievna what's going on."
    sl "I agree."
    me "Slavya, hello?"
    "I snapped my fingers in her face."
    me "Hello, garage, Moscow's on the phone! What are you doing?"
    dreamgirl "Really, why is she... {w}Maybe it's because a body was just carried out past her on a stretcher?"
    th "What's the big deal? What am I supposed to do in that case?"
    stop music fadeout 3
    dreamgirl "It's okay. {w}You can put your arm around her shoulders, since you're so manly and supportive."
    play music music_list["no_tresspassing"] fadein 3
    if alt_day6_sl_cl_arc == 'sh':
        "And so I did."
        "She rubbed her forehead on my shoulder."
        sl "How come? Everything was fine, and it was such an interesting shift."
        "I stroked her head."
        "The suicider's motives were more than clear to me - but I wasn't sure I should tell Slavya about them."
        "Let her think he was a fool and a sissy rather than get involved in an unnecessary hoax."
        "Yes, and it would look... Not good."
        sl "Semyon, does this have anything to do with yesterday's conversation in the camp director's office?"
        "I told you she was a big smart girl."
        dreamgirl "If you don't want your «big smart girl» become incapable of leaving the country, you'd better get the idea of even conducting her own investigation out of her head."
        th "How?!"
        dreamgirl "Lie."
        me "Not really."
        "I started."
        me "It's just, you know, Alexander's been having mental problems lately, you know?"
        "Wooden arms and legs, a wooden, execrable tongue, and that wretched scarf, and under it like a stone - an Adam's apple."
        me "He ran away in the tunnels - that's when it started."
        "For my mediocrity, for my shyness, I hate myself and I'm insolent."
        me "So he's crazy, and you don't have to think about why he did or didn't do something to himself."
        "I love you, I love you sacredly. {w}And in your face, I smoke brazenly."
        me "Sick."
        "Because I am awe-inspired by you."
        "My laughter was unnatural, like everything else I've been doing for the last few minutes, including shaking at the base of my skull."
        show sl sad pioneer with dspr
        sl "You're lying to me for some reason."
        "Sadly said Slavya."
        sl "As if this morning didn't have enough grief already."
        me "I'm not lying."
        "I swallowed softly."
        me "But you can't have the whole truth, you can't. Do you understand?"
        sl "Why not? I've been here a long time, and you come and get it all at once?"
        me "The outside view lets you see more."
        "The last walls fell and I hugged the girl, paying no attention to Viola smoking out the window, to Olga exclaiming unhappily, to Alisa and Ulyana holding hands confusedly."
        "On the fact that it's the last day of camp, and I've only just begun to enjoy life here."
        me "There's no going back. This camp is going to close, just like the old camp."
        me "Do you know why the old one was closed?"
        "Slavya nodded."
        me "Do you know who was there?"
        show sl serious pioneer with dspr
        sl "Some kind of squad leader, I think?"
        me "Shurik's mother. With the same symptoms."
        "Slavya gasped at my shoulder."
        me "So it's a long and ugly story, let's stay out of it?"
        "After hesitating, the girl nodded and let herself be led away."
        "There was a long send-off and gathering awaiting us."
    else:
        me "I'm just an idiot. I should have known there was a reason for all this!"
        me "Your damn camp is driving people crazy, we have to get out of here, and now!"
        sl "Semyon."
        me "First Pirate, now this, who's next, huh?"
        me "Maybe they'll turn our bus upside down and set it on fire, just to be sure, all at once!"
        "For a second I thought I heard that brain-destroying squeak-whistle-ultrasound, and my mouth went dry and there was icy sweat between my shoulder blades."
        th "And I didn't control her all day yesterday!"
        sl "Semyon!"
        me "And you're still reacting so calmly to it - you were drugged too, weren't you? You've been drugged with that stuff, in the attic?!"
        "It made me want to laugh out loud or scream - anything to keep from standing there as a powerless pillar, watching a man who seemed to have just come to rest at a children's camp being carried away."
        play sound sfx_face_slap
        "A slap burned my cheek."
        show sl angry pioneer with dspr
        sl "You're being hysterical, Semyon!"
        "Slavya barked with surprising anger and, gripping my skin painfully, grabbed my shirt, pulled me to her, and dug her lips into my lips."
        "Ignoring Viola, unsuccessfully smoothing her gray temples, smoking out the window."
        "The counselor running toward us, shouting something indecipherable."
        "Alisa and Ulyana, frozen on the side of the square."
        "She broke away first, sucked in air with a sob, and glared at me furtively."
        sl "I wasn't «drugged», and if you say any more of these things, I will be offended, do you understand?"
        me "But…"
        "I started to calm down."
        show sl angry pioneer close with dissolve
        sl "I asked…"
        "Slavya sang affectionately, hugging me and digging her fingernails into my shoulder."
        sl "Do you understand?"
        "Again, like yesterday when we made love on the roof, like this morning when I was admiringly watching the frozen flight - I was able, for a split second, to somehow catch her emotions."
        "And Slavya was very angry."
        "I had never seen her so angry."
        sl "You're too close for me to let you get away with silly accusations, too hurtful with words."
        "At last the poor shoulder was left alone."
        show sl normal pioneer with dspr
        sl "Think about it next time, before you attribute to me something incomprehensible."
        "And she smiled amiably, albeit a little forcefully, at the approaching Olga Dmitrievna."
        "It was going to be a hectic, busy day, and it was better to start early."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day7_sl_cl_breakfast:
    scene bg int_dining_hall_people_sunset_7dl with dissolve
    play ambience ambience_dining_hall_full fadein 3
    play music music_7dl["tilltheend"] fadein 3
    "Breakfast passed in a kind of depressed, anxious anticipation - though the superiors did their best to keep the incident quiet, and they even almost succeeded."
    "If it hadn't been for one oh-so-anxious pioneer, if it hadn't been for one oh-so-responsible pioneer girl."
    "I don't know where the redheads came from or how much they've seen - but now we've formed a kind of «silent circle» — the circular vouchsafes for the fact that none of us will open our mouths."
    scene bg int_dining_hall_people_sunset_7dl at zenterleft
    show sl normal pioneer at center with moveinleft
    show cs normal at left with moveinleft
    show mt normal pioneer at right with moveinright
    "Me, Slavya, Olga, Viola."
    "And, understandably, the police that rolled away with the «ambulance»."
    "The redheads are in question."
    "But they were already giggling about something - I don't know what. So they couldn't understand anything."
    "And no one told them anything, of course."
    "Two men know - a pig knows."
    hide cs
    hide mt
    with dissolve
    sl "What's with your clothes?"
    "Asked Slavya."
    if alt_day_binder != 1:
        sl "When I met you, you were wearing some warm clothes... {w}And I didn't see a suitcase with you."
    else:
        sl "Because I heard you came in winter clothes."
    "I shrugged - if my intuition gets me right, these things will be extremely relevant when I get there... Wherever I go to."
    sl "Just the uniforms need to be turned in, you know? Underwear, towels."
    "She had such a funny way of apologizing for the fact that I have to give the camp back what belongs to it."
    me "Slavya, relax. {w}I know the dreaded word 'regulation' too."
    me "And my clothes are all-weather - I won't overheat, honestly."
    "Slavya shook her head dubiously - it looked like she wanted to roust someone from our squad a little - and I hope it's not Electronik."
    "Or... Okay, stop, we don't go there anymore, we don't talk about it anymore."
    me "So you're on the role of madam castellan now?"
    show sl smile pioneer with dspr
    sl "I guess so. There's no one else."
    mt "Actually, Slavya."
    show mt normal pioneer at cright behind sl with dissolve
    "Notified the squad leader, sneaking as usual."
    mt "Violetta Cernovna told me about your health."
    mt "You're in no condition to do such things, so enjoy your last day."
    show mt grin pioneer with dspr
    mt "With your chosen one."
    show sl serious pioneer with dspr
    sl "But I can work!"
    show mt angry pioneer with dspr
    mt "And I can give you a day to say goodbye to camp."
    mt "Don't argue with me, girl. {w}I'm a counselor, I know better."
    hide mt with dissolve
    "Olga nodded and left."
    "Slavya frowned, but wisely held back her objection."
    sl "Do they really not trust me?"
    "She muttered."
    "Olga Dmitrievna had already left, so the question hung in the air."
    play sound sfx_open_door_2
    pause(1)
    scene bg ext_dining_hall_near_day at zenterright
    show sl normal pioneer
    with dissolve
    play ambience ambience_camp_center_day fadein 3
    me "Should I help you pack?"
    "I asked Slavya as we came out of the canteen."
    "She shook her head in the negative:"
    sl "I'm just like you - almost no stuff."
    me "Well, that's good! Quicker we'll get things done, we'll walk around the camp together!"
    show sl smile pioneer with dspr
    if alt_day6_sl_cl_arc == 'sh':
        sl "I'm sorry, but I really do have one thing I have to finish."
        "She smiled."
        sl "And then there's packing to do."
    else:
        sl "No, just because I don't have a lot of stuff doesn't mean I'm ready to show you all of it!"
        "She smiled."
        sl "Keep a little male illusion, and go for a walk alone for now."
    me "Objection!"
    show sl smile2 pioneer with dspr
    sl "Objection overruled. I'll see you at lunch, okay?"
    if alt_day6_sl_cl_arc == 'sh':
        "Already in a friendly way, without the usual shyness, she kissed me and, waving, ran away."
    else:
        "Anxiously looking into my eyes and finding no trace of the morning hysteria in them, she smiled and kissed me:"
        sl "Try to remember the best!"
        "And ran away."
    stop music fadeout 3
    hide sl with easeoutleft
    "That's how the end of this tale approaches."
    "It seems simple - get used to a new place, new people, get a high from an unintentional summer and youth - what more do you need to be happy?"
    "A sweet, compliant girl who will fall in love with you to the point of hind legs, look you in the mouth and look only fondly at you? And there are such."
    th "I wonder what it's like to love one person all your life?"
    dreamgirl "You'll get a chance to try it soon."
    th "Maybe."
    "It's also possible that if I hadn't sought adventure on my heel, if I'd stayed the same old withering Semyon, looking frightened from the stairs into the face of the goldilocks - I'd have only had a good experience."
    "There would have been love: holding hands, enjoying platonicism, and by the evening of the farewell disco, according to tradition, unbridled 18+."
    "And all this idyll would have been proper and nauseatingly stable."
    "And I became a hostage of my own changed nature - the same one that got me into this whole thing with the buzzers and the labyrinths with Sanich at the head."
    th "He's probably in town now, sanding the fat man."
    "I wasn't good at defining structures, but I knew at once that this was some serious organization: only in serious organizations would a skinny old man be allowed to swear at muscular neophytes."
    "But that's all for later - now we should at least just go around the camp, remember everything here."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day7_sl_cl_admins1:
    scene bg ext_admins_day_7dl with dissolve
    play ambience ambience_camp_center_day fadein 3
    "The holy of holies of the camp."
    "Certainly worthy of attention."
    "Sometimes it feels like I'm here more often than I'm at home."
    "Must be the influence of Slavya? Or the proximity to the powers that be of this camp?"
    th "Still didn't get the name and patronymic of the director. I'm a nightmarish pioneer, truly."
    play sound sfx_paper_bag
    "A piece of paper flew out of the window, picked up by the wind, and I reflexively caught it in the air."
    "Unfolded it, read:"
    me "1974. The year the camp was founded?"
    "That'll come in handy."
    "I tucked the piece of paper in my pocket and went on my way."
    $ alt_day7_sl_cl_code = True
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day7_sl_cl_clubs1:
    scene bg ext_clubs_day with dissolve
    play ambience ambience_camp_entrance_day fadein 3
    "Kicking cones and pebbles, I walked toward the gate, wondering if I could sign there somewhere."
    "It's a good tone to be sure to leave your scrawl on the wall somewhere."
    el "Semyon."
    "Someone's calm voice came to me."
    show el normal pioneer with dissolve
    me "Yes."
    "I looked up - Electronik was sitting on the club steps."
    if alt_day6_sl_cl_arc == 'sh':
        "At the same place where yesterday sat a bespectacled, wiggly boy who could count everything in the world."
    "And there was a huge padlock on the door."
    el "The club is closed."
    "Calmly he said."
    me "Noticed."
    el "And Shurik is nowhere to be found."
    if alt_day6_sl_cl_arc == 'sh':
        me "Yes."
        el "And he didn't come over at night either."
        "I shrugged it off."
    else:
        me "What do you mean he's nowhere to be found?"
        el "That's what I mean. And he didn't come overnight either."
        show el surprise pioneer with dspr
        pause(1)
        el "What's so funny?"
        "I didn't notice myself laughing."
        "It all happened spontaneously, in a kind of prostration."
        "Because it suddenly dawned on me whose corpse the police were most likely removing."
        "Not likely, though, but it was."
        "It's enough to put two and two together: a pioneer goes missing, and the next day in the morning the boys in shoulder straps hang around the camp."
        me "This place really drives people crazy..."
        el "What do you mean?"
        if dr:
            "I kept quiet."
        else:
            me "I meant what I meant."
    show el angry pioneer with dspr
    el "Semyon, I want to know what's going on?"
    me "Anecdote."
    el "What?"
    me "You asked me what's going on. I said, there's an anecdote going on."
    show el surprise pioneer with dspr
    el "What? How can a joke happen, it's just a funny story and... You're kidding."
    me "I'm trying."
    show el serious pioneer with dspr
    el "Semyon, what's wrong with Shurik?"
    "He asked, clenching his fists nervously."
    el "Do you know something?"
    el "If he ran away again, why isn't anyone looking for him, we can't have him missing somewhere, we're leaving!"
    me "Shurik left."
    "In a steady voice I replied."
    el "How, left?"
    show el upset pioneer at center
    me "Quietly."
    el "W-when?"
    me "In the morning."
    th "In a separate carriage, in white pinafores."
    "The mood, which had just begun to improve, was again irrevocably ruined."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day7_sl_cl_dining_hall1:
    scene bg ext_dining_hall_away_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    "I didn't really know what I was doing here - but memories are stubborn things."
    "My feet brought me here, where we had our first and quite successful rapprochement with Slavya."
    "And we went from being total strangers to not being good friends, but at least people who looked at each other with a modicum of sympathy."
    "And a few days later she repeated her culinary feat, once again taking care of me."
    "I'd forgotten the last time I was so taken care of."
    "Here I am, lounging around with my eyes closed and my belly rubbed."
    "Take me with your bare hands."
    "Though I can tell you, our influence was mutual - I brought a very useful little thing into the girl's life."
    "The ability to do silly things and fool around. {w}And you thought you couldn't learn that from nothing, either."
    "With a chuckle at my thoughts, I glanced around the building, memorized it as best I could, and hurried on."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day7_sl_cl_sport_area1:
    scene bg ext_playground_day with dissolve
    play ambience ambience_soccer_play_background fadein 3
    "Sanich's diocese - of a big, burly, sarcastic man."
    if ('sport_area' in list_voyage_7dl):
        "Oh, how I didn't like him when we met."
        "A lazy laggard, just thinking about going to bed."
        "It's a little clearer now that this perpetual sleepiness didn't come from nothing."
    "Who would have thought that this bear would be the one with such a strange, incomprehensible story?"
    "I checked the doors of the indoor - locked - and went on my way."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day7_sl_cl_volleyball_alt2:
    scene bg ext_volley_court_7dl with dissolve
    play ambience ambience_camp_center_day fadein 3
    "Volleyball court."
    if ('volley' in list_clubs_7dl):
        "Even though I signed up for a sports club, I never actually played any sports."
        "Running from snarks through tunnels doesn't count."
    "In general, of course, there was the urge to stand at the net for a while."
    "To me, volleyball is the sport of the beautiful."
    "I imagined Slavya taking a cut ball in flight with her lower grip - it would've been great!"
    "Too bad it never worked out."
    "With a sigh, I walked out of there."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day7_sl_cl_estrade1:
    scene bg ext_stage_big_day_7dl with dissolve
    play ambience ambience_camp_center_day fadein 3
    "It was quiet by the stage - now that there was no concert going on, no one was interested in gazing at the octagonal covered stage."
    "I had three rows of benches running down from the back rows to the front."
    "Of course, I immediately took the center seat."
    "Stretched my legs out on the front row, rested my head on the back row."
    scene bg ext_sky_7dl with flash
    "Yesterday's story started here."
    "Maybe if we hadn't gone to deal with the preparations for the concert, or if I hadn't been sent to Miku for the list..."
    "Shit, if only we had."
    "Goddamn Soviet pop!"
    "I angrily banged my fist on the bench, and the bench responded with a disgruntled hum."
    voice "Ouch!"
    "Someone nearby exclaimed, and I got up with a grunt."
    scene bg ext_stage_big_day_7dl at zenterright
    show mi shocked pioneer close at right
    with dissolve
    "Miku?"
    "What kind of typhoon brought her here?"
    show mi dontlike pioneer close with dspr
    mi "You scared me! And I thought you were so grumpy, I didn't dare disturb you, or you and Slavya might have a falling out. Hee-hee, marital!"
    mi "Oh, I'm sorry, I shouldn't have said that, of course, you have different morals, different laws here, you can't joke about families so calmly."
    "She came to shoot me with her verbal machine gun?"
    mi "Well, I'm off then, because I wanted to walk past you so as not to disturb you, and here you rattle your fist!"
    th "Oh my god, here she goes again..."
    me "What are you doing here?"
    "I asked."
    show mi normal pioneer with dspr
    mi "I wanted to sing a little for myself before I left - it's not the same or different at the club, and here you are."
    mi "Will you be my grateful audience?"
    "She smiled."
    stop ambience fadeout 2
    "I smiled back at her and nodded."
    "A farewell concert for me alone, from the tape recorder, with the crackling of the boards under my bare heels, with the twinkle of an eye meant for me alone - a VIP spot!"
    "When Miku finished singing and jokingly bowed out, I whistled, stammered, clapped and heartily thanked the girl."
    "Another really good memory."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day7_sl_cl_boat_station1:
    scene bg ext_boathouse_day with dissolve
    play ambience ambience_boat_station_day fadein 3
    "I walked along the pontoons to the far end of the pier."
    "Yeah, I have a lot of positive memories associated with the pier."
    "At least remember what happened this morning."
    if alt_day_binder == 1:
        "And the first day when she saved me from a redheaded pest."
    "Pier and Slavya are invariably positive consequences! Almost an advertising slogan."
    "I shielded my palm from the sun beating in my eyes, shifted my gaze down and noticed that I wasn't the only one here wishing to 'leave a mark.'"
    "On the narrow, slightly rusted pipe of the railing were strung locks, ribbons, wires."
    "On the second rung from the top, where the splashes don't reach, hung a very pretty braided bracelet of turquoise ribbons."
    "Nearby hung a closed lock with the initials «M.O.»"
    "And a piece of paper intercepted with black thread."
    "I wouldn't pry, but it had my name written on it."
    me "Look for me where we first became close."
    "Thoughtfully I read the letter, written out in someone's unfamiliar, rounded, almost childlike handwriting."
    "And instead of a signature, a drawing - a funny little man with huge headphones."
    "I shouldn't ravage the local treasure trove of memories any further."
    "Better to visit another place near the water."
    "That one, yes."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day7_sl_cl_beach:
    $ persistent.sprite_time = "day"
    $ day_time()
    scene bg ext_beach_day with dissolve
    play ambience ambience_lake_shore_day fadein 3
    play music music_7dl["melancholy_sun"] fadein 3
    if alt_day6_sl_cl_arc == 'sh':
        if (alt_day3_date == 'sl'):
            "I had no association with this beach in particular - I judged the match here at Slavya's request, I overheard their conversation with Lena here."
            "Honestly, I have great doubts now whether I overheard it by accident."
        else:
            "How strange that after a whole week of camping by the creek, I only managed to bathe in some pond."
            "That's not right!"
            "It's a little late to be swimming, though."
        "But anyway, I had a place to visit - our wild beach, where Slavya had heroically washed me off after cleaning the campfire glade."
    "Having made up my mind, I scurried toward the bushes hiding the stream and the section with the fence netting on top of it."
    scene bg ext_beach2_day_7dl with dissolve
    "And twenty minutes later I was out on the familiar shore."
    "A nightmare, of course."
    "Instead of doing what all couples in love usually do when they find themselves on a secluded wild beach..."
    "I was scrubbing myself of soot."
    "I felt someone near me and opened my eyes."
    show dv normal swim with dissolve
    "Redhead."
    th "Now she's going to pry about the morning."
    "With incomprehensible longing, I thought."
    "But Alisa smiled instead."
    dv "You managed it after all? Weird."
    me "Managed what?"
    dv "As if it wasn't clear. With Slavya, of course!"
    th "Thank you. Didn't get it."
    me "Why should I have managed or not managed with Slavya?"
    show dv smile swim with dspr
    dv "You know, they even had a bet on you whether you'd run away or not. {w}Our upstart's a piece of work."
    show dv laugh swim with dspr
    dv "Why are you standing there with your mouth open? Did you really think your ahs and sighs would remain a secret?"
    "I shrugged it off."
    me "I didn't make a secret out of it. Nothing much happened."
    show dv grin swim with dspr
    dv "Oh, really? It's no big deal? Does Slavya think so, too?"
    "Alisa winked."
    "I was starting to get a little sick of her incomprehensible innuendos, but the redhead took pity first:"
    dv "I run in here sometimes - and she and I agreed on days not to piss each other off."
    me "You? Agreed?"
    "I couldn't believe my ears."
    show dv normal swim with dspr
    dv "We did. What are you surprised about? Or did you want to flaunt your naked... ahem... body parts when I stopped by?"
    me "No, of course not!"
    with fade
    dv "Then don't be silly."
    me "I'm not going to ask how you know about naked body parts..."
    "Slowly I said."
    dv "Reasonable decision."
    "Alisa has spoiled my moment of nostalgic farewell to a place that almost became... No, don't mention it while there's a redhead in a bathing suit around."
    "Though a couple of days earlier, seeing her like that would have been a nice compensation for the anxiety."
    "Even before Slavya said the complicated spell - a long, long sentence beginning with 'I'm in love...'"
    th "Peeked, I guess. Couldn't Slavya have told her everything?"
    dreamgirl "Or could she?"
    dv "I'll give you a hint: she instantly reported your relationship to Hat. She's not the kind of person to keep quiet about such important things."
    if alt_day6_sl_cl_arc == 'pi':
        th "I'm surprised, then, that no one ever found out about her dog."
    me "That sounded like... Important things."
    show dv surprise swim with dspr
    dv "And for you, no?  Or are you..."
    dreamgirl "Oh, yeah! All like that! Wooed and ditched her!"
    "What she was pissed off about, I couldn't understand - I've never seen any special friendship between the redhead and Slavya."
    "Or was it all about a good enough reason to hit me properly?"
    if alt_day6_sl_cl_arc == 'sh':
        me "No, of course not!"
        "I exclaimed, involuntarily covering my nose."
    else:
        me "It's none of your business what I am or what I think."
        me "I wasn't introduced to you as the closest friend, so mind your own business."
    show dv laugh swim with dissolve
    dv "And you've grown! Look, you've already started showing your fangs."
    dv "Soon you'll be big enough to buy cigarettes without a passport."
    show dv normal swim with dspr
    "She wiped off her smile in one motion and asked me seriously:"
    dv "Are you really going to leave her?"
    me "I don't want to..."
    "Stupidly I said."
    dv "Then why don't you do something?"
    me "But what?!"
    show dv grin swim at center
    with dspr
    dv "How should I know? That's for you to decide!"
    "She leaned over, picking up the uniform scattered in the sand:"
    dv "Yes, and before I forget - Hat was gathering everyone."
    dv "Hurry up if you want to take a swim."
    me "No, I just..."
    dv "Yeah? Then wait, I'll get dressed and we'll go together."
    stop music fadeout 3
    stop ambience fadeout 3
    return

label alt_day7_sl_cl_photo:
    scene bg ext_house_of_mt_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    play music music_7dl["iwantmagic"] fadein 3
    show mt normal pioneer with dspr
    mt "Semyon, Alisa, you're just in time."
    "She paid no attention to our strange company."
    "Which was not the case with Slavya - she, in fact, looked in our direction with an extremely suspicious look."
    "But wisely decided not to have a showdown or a scene of jealousy."
    mt "Okay, first squad!"
    "She began."
    mt "For the event - in a line of two - line up!"
    th "Another lineup? Homely?"
    "Lazily I thought, as the tallest one, getting up behind Alisa."
    "Lined up, as on the lineup, habitually already - by height, obediently, without snapping or arguing: the faster we start - the faster we finish."
    "Except that I didn't understand until the last minute what Olga was up to."
    th "Was she really going to make her speeches?"
    mt "Right, right…"
    hide mt with easeoutleft
    "She disappeared into the cabin, and a few minutes later appeared on the porch, armed with some ribbed leather thingy."
    "A few seconds later, with a gasp, I recognized the thing as a rigid camera case."
    if alt_day2_mi_snap:
        th "The very same camera that belonged to the gym teacher!"
        "I remembered how, after I won the tournament, Miku dragged me to him, and Sanich had that very case in his hands."
        "The Jap girl winked at me and turned up her nose."
        th "And now it must have been inherited, after the bear was taken to town."
    th "Gee, so..."
    dreamgirl "So that means..."
    "A minute later a tripod appeared to the white light as well."
    "Putting a slight delay and turning the camera in our direction, Olga pushed her way to the center and barked:"
    mt "Come on, smile now!"
    me "Why?"
    mt "Semyon doesn't have to smile, I'll blur his face in the frame."
    "The counselor brushed it off. Her hands were trembling for some reason."
    "Laughter was heard in the ranks, and Alisa's narrow palm rested on my shoulders, with Slavya's palm on the other side."
    "Except that Slavya's touch was gentle, affectionate, and Dvachevskaya squeezed my shoulder a little, hinting at the seriousness of the moment."
    "I put my hands on their shoulders - what else could I do?"
    "Enjoying the moment - a smile appeared on my lips, I didn't even have to force myself."
    "Second picture I've ever had taken of me smiling in my life, I can't believe it."
    "One simple gesture, it seemed - and it became obvious how much I enjoyed the company of all these people - even the redheaded bitch."
    "And how sad it is that for all of us this is our last shift."
    "Age, huh. {w} In this world they give the pioneers too much time; I remember in my homeland they took off the red tie when I was thirteen or fourteen."
    "Excluding Ulyana, for everyone whose shoulders I'm hugging right now, this is the last shift, no one else is coming back here."
    "For all of you who are struggling to smile right now, to show that camp was indeed a success."
    "It was, by and large."
    "Except for some tragic moments."
    "So we didn't just go, we really had a good time."
    mt "Say «Cheeese»!"
    show dv normal pioneer far at fleft
    show un normal pioneer far at fright
    show am pi_sad pioneer far at left
    show sl normal pioneer far at cleft
    show mi normal pioneer far at right
    show el normal pioneer far at cright behind mi
    show us sad pioneer far at center
    show mt smile pioneer far at center behind us
    with dspr
    voices "Cheeeeese!"
    with flash
    pause(1)
    scene white
    pause(2)
    scene bg ext_house_of_mt_day at zentercenter
    show mt normal pioneer
    with dissolve
    "We shouted, leaving the camp as we knew it - kind, affectionate, peaceful."
    "A place where one day one will surely want to return."
    "I was terribly jealous of them - them, not realizing that..."
    "Olga, hiding her trembling hands, nodded and stood up, picking up her machine."
    "Somewhere in the infirmary Viola sat, putting her fingers on her timelessly graying temples."
    "And Slavya and I look at each other with the eyes of a battered dog."
    "But Olga wouldn't be herself if she couldn't manage her emotions:"
    mt "Thank you all! I've got your addresses, expect a photo in the mail in September or October."
    show sl normal pioneer at cleft with dissolve
    sl "So why don't we have a convention? Hand out photos, and just see each other."
    sl "I'm sure no one will mind."
    "Everyone murmured in agreement, and Olga nodded:"
    show mt normal pioneer with dissolve
    mt "Actually, at the end of October there's usually an all-camp convention on the square, but if you want... Let's have a separate one."
    "She nodded to us:"
    mt "That's it now. Come on, it's half an hour before we leave, go out, make sure you don't forget anything."
    "And she turned away, thinking about the organizational moments of a future reunion evening."
    "And Slavya pulled me along."
    stop music fadeout 3
    scene bg ext_houses_day at zenterleft
    show sl normal pioneer at cleft
    with dissolve
    sl "So, did you have a good time walking around?"
    "She asked."
    me "I guess so. {w}It's a small camp."
    if alt_day6_sl_cl_arc == 'pi':
        me "I figured that out yesterday, when you and I were on the roof listening to it."
    if alt_day7_sl_cl_code:
        th "Though there are plenty of hidden corners here, too."
    sl "Semyon, we need to have a serious talk..."
    "She started it."
    play sound sfx_7dl["eat_horn"] fadein 1
    "But she was immediately interrupted by the honking of the horn."
    "Calling the pioneers to a final feeding before the road."
    me "About what?"
    show sl sad pioneer with dspr
    sl "Uh... Let's do it after lunch, okay?"
    me "We don't have time to talk, do we? {w}Are you packed?"
    sl "After lunch."
    "Slavya answered unhesitatingly and went to the dining room without waiting for me."
    stop sound fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day7_sl_cl_dinner:
    scene bg int_dining_hall_day with dissolve
    play ambience ambience_dining_hall_full
    play music music_7dl["nowyouseeme"] fadein 3
    "They fed us chicken soup with rice and fried potatoes and scrambled eggs - it was more than obvious that the chef had already gone into town and there was no one to make the cooks cook the duty pearl millet."
    "So we moved our jaws more than we wasted our time talking."
    "The logic is this, comparative - if you've been fed canteen food all your life, wonderful, cool, tasty, balanced and according to the precepts of the leading dog-leaders, you'll rave till you squeak when one day you get dumplings or this kind of food for dinner."
    "Slavya accepted Olga Dmitrievna's decision to relieve her of her castellan's duties - it seems that despite all the bravado, the girl was still a little 'shaken' after all."
    "Or perhaps that wasn't quite the point?"
    "Slavya looked perceptibly depressed, and whenever I tried to intercept her gaze, she flinched and averted her eyes."
    "As if she felt... Guilty?"
    "I tried to imagine the size of the «screw up», which Slavya could have committed to be so embarrassed of me - and with a sigh I gave up the idea."
    "First of all, I just couldn't imagine."
    "And second of all, when?"
    "And this her «serious» talk."
    th "Not that I insisted - but what could she have «seriously» talked to me about?"
    "Having half-heartedly disgorged an already unconventional bachelor's meal, I set the plates aside and got up."
    me "I'll be outside."
    "Slavya nodded absent-mindedly, continuing to look for oil at the bottom of her soup plate."
    play sound sfx_open_door_clubs_2
    pause(1)
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_dining_hall_near_day with flash
    play music music_7dl["the_way"] fadein 3
    "I walked out onto the porch and froze on the bench, fighting the chill that tingled my stomach."
    "I used to get that feeling when I was a kid - before my skin was calloused, before my heart was calloused."
    "And it meant either great trouble or a tangible change in my life."
    "Not necessarily for the better or for the worse, just a change."
    "Like changing schools or teams, moving to a new place of residence - or even just meeting some new personalities who will involve you in their movement in one way or another."
    "Or leaving for camp."
    "But given the depressed mood reigning over camp all this morning, I wasn't flattered about the degree of positivity in the conversation to come."
    dreamgirl "I sense trouble, too."
    th "Any thoughts?"
    "I was thrown the image of a shrug."
    dreamgirl "It's too early for exclamations like «I'm preggers!»."
    dreamgirl "Dunno."
    th "Does she really want to break up with me?! But why?"
    dreamgirl "Stop panicking on the ship! {w}Or do you need to be reminded how she was hovering around you this morning?"
    th "Saying good-bye!"
    dreamgirl "You're hopeless! {w}I'll just shut up and wait for the actual conversation."
    "And I kept winding myself up - in light of everything that happened today."
    "In light of everything that happened yesterday."
    if alt_day6_sl_cl_arc == 'sh':
        th "Couldn't solve the problem any other way, you bloody calculator!"
        "With anger I thought of Shurik."
    else:
        th "She does seem to have a bad impression somewhere."
        "Because the dog's fate was partly and truly in my hands."
    "So when Slavya came out on the porch, I couldn't help myself."
    "By this time all the pioneers had safely dispersed to their cabins."
    "Those who stayed for the change of shift and the next shift giggled quietly at the 'gatherers,' and the latter, in fact, gathered."
    "There were no stayers in our squad."
    th "Or?"
    show sl normal pioneer with dspr
    sl "Semushka, we need to have a serious talk."
    me "Yes, yes, you told me already! About what?"
    show sl sad pioneer with dspr
    sl "It has to do with yesterday..."
    th "Breaking up!"
    "I was all torn up inside."
    th "Now she's going to say we have to break up!"
    "I squeezed my eyes shut, getting ready for the hit and..."
    sl "First I want to say that I am very grateful to you for being in my life and for what you have brought into it."
    sl "Except for the really sad moments, this has been the best summer of my life."
    sl "And I really loved you a lot. So..."
    "Let's… Break up…"
    sl "I have to warn you."
    me "About what?!"
    sl "Semyon, don't be so fidgety, it's not like I'm suggesting we break up!"
    me "Then what?!"
    show sl shy pioneer with dspr
    sl "Well, I was going to say that you shouldn't force people, or whatever you said, to do something against their will..."
    "She got confused and mumbled, looking under her feet."
    me "Closer to the topic!"
    sl "Yes, I'm sorry."
    "She exhaled."
    sl "I wanted to tell you I'm not going to town with you."
    me "You're breaking up with me!!!" with vpunch
    sl "As if I'm going to leave you, you fool, I love you."
    "Calmly said the girl."
    "Calmly, without tearing up or breaking down - making it clear that this is so much a part of her life that she's long since thought it over and accepted it."
    show sl serious pioneer with dspr
    sl "The problem is that the camp is being closed."
    sl "Shurik was taken away in the morning, but by the evening the company that is our patron will know, and tomorrow the city administration will know."
    sl "No one will come here. Do you understand?"
    th "She's right."
    th "The old camp was closed for the same reason - bad rumors, devils, dead people..."
    "I remembered my childhood camp - we had one abandoned old building."
    "It's all boarded up - and only because some fool decided to slit her wrists in there."
    "And that's it! A solid stone building, insulated, comfortable - boarded up tightly, only the boys went in there looking for adventure."
    me "And how do I piece this together... Did you decide to stay and help?"
    show sl normal pioneer with dspr
    sl "I told you, you're smart."
    sl "While you went to say goodbye to the camp, we were approached by the administration and asked for help."
    sl "Miku refused - she had to go back to Japan and finish the paperwork: she was going to study in Leningrad."
    sl "And Zhenya and I agreed."
    me "And me...?"
    "Stupidly I asked."
    sl "And you're going home."
    me "Just like that?"
    show sl sad pioneer with dspr
    sl "No. {w}I don't know myself how I'll be here without you. But we really have to help - we can't let the kids lose their vacation because of a rumor."
    "I found it doubtful that the children would be particularly happy vacationing where..."
    sl "That's right: a non-disclosure agreement."
    sl "Me, Olga Dmitrievna, Viola, all signed."
    sl "And you're leaving, so..."
    "Slavya interrupted - the buzzer was walking past us."
    "The person who had caused me the most persistent repulsion."
    "But now she looked like one who wanted to cover her with a plaid and take her away to a warm place-a true victim of natural disaster."
    "Pale, her eyes sunken, once shining a menacing yellow, now reflected the color dimly with a dirty, swampy tint, her hair disheveled."
    "Even the usually perky question-mark-shaped tuft of hair at the top of her head had wilted and looked dull."
    sl "Zhenya!"
    hide sl with dissolve
    "Shouted Slavya and ran to the librarian."
    "I guess I would have run, too."
    "But I was a little spurred on by this kind of stunning, head-on fact."
    "She says she has feelings for me - and doesn't want to be with me."
    "Prioritizes helping other people."
    th "Why does she refuse to help me?"
    th "It's not selfishness, she's not thinking about herself! I'm a different person and everything!"
    th "Let her help me! {w}Sits next to me on the bus, takes me by the hand and supports me all the way to town, and then stays in my life!"
    voice "My name is Feoktistova Slavyana..."
    "A girlish voice jumped in my ears - so frighteningly unfamiliar a few days ago."
    "A record of getting close to a human being."
    "I've never let anyone in so quickly and close to me."
    "And now she wants me to leave without her."
    "I knew, of course - and if this situation had arisen under normal circumstances, I wouldn't have raised an eyebrow."
    "Because I know when it's «needed», then you can wait until the end of the summer - then just dial the numbers twenty-eighth or twenty-ninth and meet the evening of September 1 somewhere near the «Aurora»."
    "There have been precedents, there have been."
    "But my conditions aren't the most ordinary!"
    if alt_day6_sl_cl_arc == 'pi':
        "And she knows that very well."
        "But she still thinks staying in the dying camp is more important than me."
        "Than we are."
    "Bitch."
    with fade
    "Bastard."
    with fade
    "Asshole."
    if (lp_sl >= 18) or (alt_sp >= 6):
        menu:
            "That's why I love her":
                $ alt_day6_sl_cl_good = 1
                scene bg ext_admins_day_7dl with fade
                pause(1)
                scene bg int_admins_7dl with flash
                show mt surprise pioneer at zenterleft
                mt "Semyon? What are you..."
                me "No... Time..."
                "I exhaled hoarsely, stopping beside her and breathing fervently..."
                me "Director... In there?"
                show mt normal pioneer with dspr
                mt "Yes, but he was about to leave, to see the people off."
                me "I have to go to him."
                mt "Really?"
                me "I really have to!"
                show mt angry pioneer with dspr
                mt "What really? Have you seen yourself, you dolt?!"
                "She straightened my shirt around my shoulders, smoothed my frizz a little."
                "And after giving me a long, appraising look, she stepped aside."
                show mt normal pioneer with dspr
                mt "There, now I believe you need it."
                mt "Come on in."
                "She stepped aside, allowing me to finally get to the boss."
                hide mt with dissolve
                play sound sfx_open_door_2
                pause(1)
                show bb normal casual with dissolve
                "He really was on his way."
                me "Excuse me, excuse me, can I talk to you?"
                bb "Actually, I was just leaving..."
                me "It's very important! Please."
                bb "Okay."
                scene bg int_chief_office_day_7dl with dissolve
                play sound sfx_close_cabinet
                "With a sigh, he unlocked the office and let me in."
                show bb normal casual with dissolve
                bb "So what's this about?.."
                "He asked, from the looks of it, concentrating on trying to find something."
                "Now."
                me "You see, the thing is..."
                th "A very wise but very unpleasant man told me..."
                me "That we're leaving now."
                th "That our happiness is too close to sit and watch it disappear."
                me "But you don't have people. And Boris Alexandrovich offered me the place of deputy in his clubs."
                bb "Yes, and?"
                me "I realize, of course, that I'm asking too much."
                "There's really a twinge of despair in my voice."
                me "Please... Let me stay. At least as an assistant."
                th "That our happiness is already too little to miss out on and what little we have, just because you're too lazy and indecisive."
                me "On the third shift and beyond."
                th "That sometimes you have to get off your ass and make a few gestures, do something decisive - otherwise you'll end up like this wise man: alone and unknown."
                show bb serious casual with dspr
                bb "You do realize that such matters are not solved out of the blue, don't you?"
                me "Of course! What can I do to solve it in my favor?"
                show bb smile casual with dspr
                "The director smiled enigmatically, finally finishing his search."
                bb "First, sign here."
                "He handed me a sheet of typewritten text that read, in black on paper:"
                me "Application: Please accept me, Semyon Semyonovich Persunov, for the position of Deputy Head of the Physical Education Club."
                me "What is this? Did you know?! But how?!"
                bb "Boy, I'm the head of the camp. Do you think they just put somebody in that position for nothing?"
                me "Uh..."
                show bb serious casual with dspr
                bb "And one more thing."
                play sound sfx_table_hit
                "He slammed his palm on the table."
                bb "Remember my name already!"
                bb "What's this disgusting thing, when a pioneer doesn't know who his camp director is?"
                me "I'll remember it, I will... Uh..."
                show bb normal casual with dspr
                bb "Alexei Maksimovich."
                "He introduced himself."
                $ meet('bb', 'Alexei Maksimovich')
                me "Alexei Maksimovich."
                "I obediently replied."
                bb "Well, that's it now."
                "The director studied my signature, slapped a heavy stamp on top, and hid the application in his desk."
                show bb smile casual with dspr
                bb "Go. {w}Go cheer up Slavyana - she's probably all gutted from worry."
                me "So she knows too?"
                bb "No, but I know who my best pioneer girl is dating."
                bb "Okay, go."
                stop music fadeout 3
                play sound sfx_open_door_clubs_2
                pause(1)
                scene bg ext_admins_day_7dl with dissolve
                play music music_list["afterword"] fadein 3
                "Unless she made up her mind for everyone again."
                "And I refused to accept her decision again."
                scene bg ext_square_day at zenterleft
                show sl normal pioneer at cleft
                with dissolve
                "I intercepted them not far from Genda and led them almost all the way to the cabin."
                "I didn't dare to go near them - it was too suspicious that the buzzer's shoulders were trembling."
                "It was too much like the display of emotion I had denied her for so long."
                "Finally, the librarian walked away, stubbornly looking under her feet."
                "And I approached Slavya."
                sl "Semyon? Why aren't you going?"
                me "Why? Because one silly girl has indoctrinated herself that there can be no equality between help and personal happiness."
                me "That you are either for others or for yourself - and there is no third."
                me "And I refused to accept it."
                show sl sad pioneer with dspr
                sl "What?"
                me "What you've heard. {w}I don't like stupid decisions, okay?"
                sl "Semyon, you're acting like a little kid."
                me "No."
                me "I'm acting like a person who's looking for compromises - and not just between the outside and the inside."
                me "But also between the personal and the private."
                "I pulled my copy of the application out of my pocket and held it out to her."
                me "I want to be with you. I don't want to wait for you somewhere, I don't know where. Do you understand?"
                me "You're too important, and we've been together too little."
                "A shy, uncertain smile crept onto her lips:"
                sl "But we can't..."
                me "We can. We'll see each other every day - and what else do you need for happiness?"
                show sl tender pioneer with dspr
                sl "But..."
                "She tried to say something else, but what did it matter now?"
                "That's what she thought, too."
                "And a few seconds later she was already whimpering quietly with happiness somewhere on my chest."
                "Confident."
                "Strong."
                "Helpless."
                me "You promised me I'd smile again, remember?"
                "I whispered."
                me "It's time for me to return your promise to you."
                with fade
                stop music fadeout 3
                scene bg ext_house_of_mt_day
                "My things didn't need to be packed, Olga would be back in a week, so she didn't pack her suitcases either."
                "After all the organizational issues were resolved, they left me at my previous place, but in the fourth shift they promised to give me a separate dwelling."
                "After all, living with a girl with whom you're not in a relationship is kind of a bummer. Even if you're yesterday's pioneer."
                play sound sfx_open_door_strong
                pause(1)
                scene bg int_house_of_mt_day at zenterleft
                show mt normal dress at cleft
                with dissolve
                "Olga was packing a light bag of essentials."
                mt "Don't lose your copy."
                "She muttered, struggling with the clasp."
                mt "As wonderful a boy as you are, work record is still a thing that has to be kept in order."
                me "And did you know, too?"
                show mt smile dress with dspr
                mt "Actually, it was my idea."
                "She grinned."
                show mt normal dress with dspr
                mt "I'm ready. Are you going to walk me out?"
                "Slavya nodded, and we headed for the gate."
            "How untimely this all is":
                play music music_7dl["beth"] fadein 3
                th "Wow, first quarrel, and right at the end."
                th "And that's how we're going to split up, huh?"
                "I sat down on the balcony steps and thought."
                "For some reason nothing but pouty lips and an equally childish 'I don't want to' came to mind."
                "Zhenya walked by, glancing unpleasantly at me at the same time."
                "Living proof that hating a man is a great art."
                me "Why does everything have to be so complicated?"
                "I asked the calm, heat-melting sky."
                me "Why can't it be normal? Meet, get acquainted, move in together?"
                me "Does everything have to be through one place?"
                "The door creaked behind me, and a familiar hand with beautiful fingers rested on my shoulder."
                "I almost burst into tears of self-pity."
                "How is that possible?"
                "I'm going away now, and there will be no Slavya, no camp, not even that palm?"
                "And there will be an incomprehensible Soviet Union in which I will be without papers, without connections, without acquaintances - alone."
                "Of course, I heard Olga say something there about my parents from the embassy - but I think it's complete nonsense."
                show sl normal pioneer with dspr
                sl "Why are you getting so upset?"
                "Quietly she asked."
                sl "I understand the separation is unpleasant. But it won't be for long. Just a month."
                me "A whole month."
                "I shook my head."
                show sl serious pioneer with dspr
                sl "Semyon, you're acting like a little kid."
                sl "Well? You said it yourself, you made plans, how are we going to be?"
                sl "Did you?"
                show sl normal pioneer with dspr
                sl "You have to understand that neither of us is old enough to fully decide what to do and how to do it."
                me "Personally, I'm more than old enough."
                "I sullenly replied."
                me "I don't know about parents and all that, but I've lived alone in my house for the last ten years, taking care of myself!"
                "Slavya sat down next to me on the step and put her arm around my shoulders."
                show sl smile pioneer with dspr
                sl "Ten years..."
                me "Yes."
                sl "How old are you really?"
                "I shrugged."
                me "You do the math, considering I moved into my full living quarters at eighteen..."
                "Slavya whistled."
                sl "You really are big!"
                "Really."
                "Though, of course, I wouldn't believe such a thing."
                "Anyway..."
                "I'm just covering the details."
                sl "But then you should be able to wait, if you're such an adult."
                "Said she admonishingly."
                "You can think a lot about what and who I owe in general."
                "Thinking about expectations, responsibility, the meaning of life."
                "But I've waited too long to just leave like this."
                me "I'm going to go pack."
                "I said glumly, and, dropping Slavya's palm from my shoulder, I got up."
                me "Bye."
                scene bg ext_house_of_mt_day with dissolve
                play ambience ambience_camp_center_day fadein 2
                "Home, sweet home."
                "Everything seemed to be trying to spoil my mood today."
                "And it was such a good start to the morning!"
                show mt normal dress with dissolve
                mt "Sem Semich, why are you sad?"
                me "As if you don't know."
                "I grumbled."
                show mt smile dress with dspr
                mt "I don't. What?"
                mt "You mean about Slavya and Zhenya staying here?"
                "Well, I didn't have to say anything."
                show mt normal dress with dspr
                mt "Your Isolde will come to see you."
                "The counselor grinned."
                mt "She'll do her shift and then she'll come. Or you can't wait three weeks?"
                me "No, but..."
                play music music_7dl["but_why"]
                "With a surprised eagerness, I grabbed Olga's hand."
                show mt surprise dress with dspr
                me "Olga Dmitriyevna, I don't want to, I can't leave!"
                "I blurted out."
                me "I can't, you know?"
                if alt_day6_sl_cl_arc == 'pi':
                    th "On the other side of the road winter and death await me."
                me "Take my word for it, I can't go away!"
                me "Please!"
                me "Can't anything be done?"
                mt "Actually, you can..."
                "Slowly said the counselor, diligently peeling my whitened fingers off her wrist."
                show mt angry dress with dissolve
                mt "Will you let go of my hand or not?"
                me "Yes, yes, anything."
                me "So what can I do?"
                "Olga hesitated for a few seconds, looking at me sideways, incredulous."
                "Decided at last."
                mt "Run to the camp director, tell him what I asked."
                me "What did you ask for?"
                mt "He knows!"
                "She brushed it off."
                mt "Just tell him that I asked."
                me "Thank you!"
                "New hope pounded in my temples, pushing my legs forward, adding to the heat."
                "And I ran, ran as hard as I could."
                scene bg ext_house_of_sl_day at fast_running
                with flash
                dreamgirl "If you want to pray, now is the time."
                "Because of running, the voice of my pocket schizophrenia was audible intermittently."
                th "Don't jinx it!"
                scene bg ext_square_day at fast_running
                with flash
                dreamgirl "But if I remember the regulations correctly, the supervisor always leaves during his shift change - to turn in his paperwork and get passes for the next shift."
                dreamgirl "And since he has no one to wave his handkerchief to, it's quite possible that he could..."
                th "Shut up!"
                "I growled."
                scene bg ext_admins_day_7dl with flash
                me "Just... Just a little bit more."
                "I pushed up, taking off on the porch, but the administration was locked."
                "Only behind the clear plexiglass window was a note: «Went to town for debriefing. A.M.»"
                cs "Pioneer, if you're looking for the boss, I gave him the keys."
                show cs normal with dissolve
                cs "But if you hurry... You can try to intercept him at the gate."
                me "Thank you, Viola!"
                "I switched to running again - it seems to be the only thing that can solve problems today!"
                pause(2)
            "That's how it should've ended":
                $ alt_day6_sl_cl_good = 3
                pass
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day7_sl_cl_departure_a2th:
    play music music_list["farewell_to_the_past_full"] fadein 3
    scene cg d7_leaving_no_sl_sam_7dl with dissolve
    play ambience ambience_camp_entrance_day_people fadein 3
    "We came out of the gate, stopped to the side, and Olga headed toward the pioneers."
    "She gave them a farewell speech, worrying herself and hardly holding back her tears."
    "Ours were already big and had a bit of understanding of what was going on - they listened to the counselor's speech seriously and with feeling."
    "Oh, but I'm lying."
    "Ulyana intercepted my gaze, winked, pushed Alisa to the side, and now the two of them were already staring at us."
    "It wasn't long before the attention of the squad was lost completely - all staring at us."
    "There weren't many of them, though."
    scene bg ext_bus1_7dl with dissolve
    show us normal sport bear at cleft
    show dv normal sport at cright
    with dissolve
    "The redheaded couple."
    show us smile sport bear at cleft
    show dv grin sport at cright
    "A redhead is a dangerous man!"
    "They smiled and winked at me in sync."
    hide us
    hide dv
    show un normal dress
    with dissolve
    "Lena, standing in the distance."
    show un smile dress with dissolve
    "She blushed a little, intercepting my gaze - it seems that despite setting up some dots, I continued to embarrass her that way."
    hide un
    show mi smile casual
    with dissolve
    "Miku."
    "The Japanese girl had already retrieved her ultra-hitech Japanese headphones from the depths of her Japanese suitcases and was bobbing her head to the beat of some tune."
    show mi happy casual with dspr
    "Sensing that we were looking at her, she winked at us and shook her clasped hands in the air."
    "Some kind of secret sign? That everything is going to be okay?"
    hide mi with dissolve
    "Electronik nodded and turned away."
    show mt normal dress with dspr
    mt "Yes, Zhenya, Slavya, and Semyon will stay at the camp as volunteers."
    "Olga answered Ulyana's question."
    "Kid looked at us enviously:"
    show us normal sport bear at cleft
    us "Can I also be a volunteer?"
    show sl laugh pioneer at right with dissolve
    sl "Of course you can! In two years you'll be just the right age."
    show us sad sport bear with dspr
    us "But I don't want it in two years, I want it now."
    "Olga laughed and commanded:"
    mt "To the cars!"
    scene bg ext_bus1_7dl with dissolve
    "That's right, the younger squads have already been put on their buses and sent on their journey."
    "Now it was the turn of the older pioneers."
    "We waved to them the whole time they were getting on."
    "The whole time they were pulling away with their noses stuck to the windows."
    "Until the bus turned into a barely visible dot on the horizon."
    th "Unexpected sequel to an unexpected story?"
    scene bg ext_no_bus at zenterleft
    show sl smile pioneer at cleft
    with dissolve
    th "A story that one day, hopefully, will be everlasting."
    th "Like this summer."
    sl "I won't wave anymore, okay?{w} My arm is tired."
    "I nodded."
    me "So is mine."
    scene bg black
    with fade3
    stop music fadeout 3
    pause(3)
    scene bg ext_square_sunset with dissolve
    $ set_mode_nvl()
    play music music_7dl["lynn"] fadein 3
    "Slavya was right all round."
    "Our love may have reeked of dancing on the bones of the world and feasting during the plague - but the external misfortune only helped us to unite even more."
    "During the shifts we didn't let go of our hands at all, desperately and naively trying to soak in each other, the way a swimmer usually breathes before diving to the depths."
    "Needless to say, we failed."
    "And then the new shift arrived, the new pioneers."
    "And there was no time for nonsense - hell, sometimes I even forgot why I stayed at camp in the first place!"
    "The three weeks flew by like crazy - I only got up a little bit later than the squad leader, but I had a lot less time to sit down, too."
    "The equipment, the competitions, the matches, the championships - it all fell on my frail manhood."
    nvl clear
    "I would come to my cabin with Olga in the evenings and fall flat, and our green-eyed woman, who had already officially allowed Slavya and me to call her Olga, would come and pull off my shoes and cover me with a blanket."
    "And the next morning everything repeated."
    "And again and again, when I had no strength left, not even Slavya's possible approval could save me, I would sit down and ask - what do I really want to do?"
    if herc:
        "Of course, with my cockroaches I don't get along with people too easily, but..."
        "I'm Uncle Syoma now, can you imagine?"
        "The girls of the third or fourth squad are riding on my back and wasting film."
        "And Slavya smiles quietly, looking at us with a special, motherly tenderness."
    else:
        "And as strange as it sounds, I could easily imagine myself as the forty-or-fifty-year-old equivalent of Sanich, a man who had devoted his entire life to working with children."
        "Sitting at home with a cup of tea and deservedly proud of the scattering of trophies on the wall of fame earned by those I believed in."
        "And by my side, Slavya."
        "Somehow at once and all of a sudden it became clear that there was no one else I could think of near me."
        "Not the convenient «she cooks great», «she's good in bed» or «I believe her», no."
        "And just a calm, warm understanding - if I want to stop rushing through life and feel the right and important person by my side, I'll never find anyone better."
    nvl clear
    "The good thing about working in camp is that you're always doing something."
    "So the feeling that I was working part-time as a loader in a nuclear reactor hardly ever came over me, and it felt kind of detached."
    "Yes, death, yes, not a good place, yes, people involuntarily avoid it."
    "But I've hardly ever been there, day and night either on the sports field or by the water."
    "Therefore, it is fair to say that the last summer of «Sovyonok» gave its pioneers no less than the fifteen that came before it."
    scene cg d4_cs_car_day_cs_coat_7dl
    with fade
    "And then... Then summer was over."
    "And here I am, sitting in Viola's «Volga», scared piss and shitless."
    "But it's kind of silly and weird to ask Slavya to stay here with me"
    "I can't hide forever; sooner or later I'll have to get out."
    "And I've already taken a month and a half more happiness than I was supposed to have."
    "So I'm scared as hell."
    "But I haven't had a thought to say anything about it."
    nvl clear
    "Especially since Slavya was now letting me decide some things most of the time, and I was well aware of what that might mean."
    "So it's time to start living. In the first place."
    cs "Let's go... pioneers?"
    "And we shouted."
    voices "Let's go!"
    "The clock ran after the clock..."
    "Slavya held my hand and looked out the window."
    "And I tried my best not to fall asleep."
    "Just to stay awake."
    nvl clear
    "I don't want to. I can't."
    "If I fall asleep, I..."
    "At that thought, I shut down."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day7_sl_cl_departure_lone:
    scene bg ext_no_bus with dissolve
    play music music_7dl["tilltheend"] fadein 3
    play ambience ambience_camp_entrance_day fadein 3
    "Naturally I was late."
    "And who better than me to know that in this life everything is determined by His Majesty Chance - and in my case, it is far from that Chance."
    "I am too much of a loser to have escaped from a lingering slumber to find myself on the shore clutching the most precious in my arms."
    "My legs no longer held me."
    "With a melancholical spit of lingering saliva on the pavement, I kicked the gate with my foot."
    play sound sfx_metal_door_heavy_close
    un "So what are you making noise about?"
    show un normal dress with dissolve
    "Already ready for labor and defense Lena."
    th "She went to the disco in this dress, and she's going to town in it."
    th "Does the girl wear the same dress? There aren't any others?"
    th "It seems that all is not well in the Danish kingdom."
    me "Has the director left?"
    "Lena nodded."
    me "How long ago?"
    th "What difference does it make, you idiot?! As if the fact that he left four minutes ago instead of three minutes ago makes you catch up with him now!"
    un "Just now."
    "Ruthlessly she said."
    "I groaned and banged my head on the gate."
    "I'm a loser."
    "I bring nothing but trouble to everyone - including myself."
    "So it's not surprising that a story that started out so well ended in a carefully hushed up suicide."
    "And now I'm cashing in my ticket back to my cozy hell."
    show un serious dress with dissolve
    un "Young man, why do you kill yourself like that? You'll never get killed like that."
    "Without a smile, the girl made a joke."
    "And I smiled back at her crookedly."
    "We both fell silent."
    me "The bus is coming."
    un "Yes."
    "Lena answered."
    me "Where are you going next?"
    un "To finish my studies. My father was offered a place at Polytechnic, so I'll probably go there."
    me "Polytechnic. {w}Ah."
    "I cleverly said."
    un "And you?"
    me "What?"
    show un angry2 dress with dissolve
    un "What are you going to do yourself?.. {w}Besides family life."
    if alt_day6_sl_cl_arc == 'pi':
        th "I, my dear, am not going to do anything, for the reason that I am going to die as soon as I fall asleep outside the camp."
        "I thought about it quite calmly, detached somehow."
        "Got used to it or something."
    me "I'll live. Army, all that."
    un "I don't hear any joy in your voice."
    me "Should there be?"
    me "Imagine what you have to..."
    if alt_day6_sl_cl_arc == 'pi':
        "Die."
    me "...be separated from a dear person. {w}And you cannot guarantee that you will meet."
    show un normal dress with dissolve
    un "That's no reason to be discouraged. {w}Come on, do you really want Slavya to remember you like this?"
    hide un with dissolve
    "She shook her head and left."
    with fade2
    "And good riddance."
    "Wind on your humped back."
    "{i}Bitch.{/i}"
    "I sat down on the curb and started figuring out how to handle the situation in my favor."
    "It wasn't working out very well."
    "Setting aside the rescue by rocker mice from Mars and Captain America, there were two sane options."
    "The first was to go live in the woods."
    dreamgirl "Oh, look, a Bryansk gueorilla! How long will you survive on aspen bark and unripe blueberries?"
    th "I said sane, not reasonable."
    "Besides, I had access to a bomb shelter, and you could sit there for about fifty years if you wanted to, if you really wanted to - there were enough supplies."
    dreamgirl "That's an option! Let's go to the underground, and we'll have Metro1989 here. Or even Stalker: Clear Call of Sovyonok."
    dreamgirl "Come on! You'll get what yoouuuuu deeeseeeerveeeeeee! Coooomeee toooo meeeee!"
    th "You're not helping, blabbermouth!"
    dreamgirl "I have no such task. {w}What's the second option?"
    th "The official ways."
    stop music fadeout 3
    scene cg d7_leaving_no_sl_7dl
    with dissolve
    play music music_list["memories"] fadein 3
    mt "Is everyone here?"
    "Olga counted us by our heads."
    us "Feoktistova and Zhukova are gone."
    "Ulyana snitched."
    mt "I know. They're staying."
    voices "What do you mean they stay? Why? What's the matter?"
    "The pioneers murmured, clearly intrigued."
    mt "They've been asked to do pro bono work."
    dv "So, for free!"
    un "Come on, Lis, even if they don't get paid, they'll rest here."
    "Lena shook her head."
    un "I'd even stay here to work."
    dv "Well... Only if you look at it that way."
    "Alisa shook her head:"
    dv "But I could do just as well in the city!"
    dv "Especially since Feoktistova's lover is leaving. She'll be cheating."
    "I blushed."
    me "Dvachevskaya, shut up, please."
    "Alisa laughed, but the counselor shushed her."
    scene bg ext_bus at zenterleft
    show mi smile casual at cleft
    with dissolve
    "And someone took me by the elbow from behind and gave me a gentle squeeze:"
    "Miku."
    "She stayed away for some reason."
    mi "You know, don't feel bad that you're splitting up. My dad used to say that true love is like a fire, and separation is like the wind. If the flame is strong, the wind will only fan it even more."
    me "Thank you."
    "I wouldn't say it made it any easier."
    "But having an extra person on your side is always nice."
    mi "Do you want to sit on the bus together? We can talk."
    "Immediately the Japanese girl ruined the effect of her altruism."
    mi "Not hanging out with Lena?"
    show mi happy casual with dissolve
    mi "Well... I can hang out with her, too. But if you need to sit alone, I won't impose, I'm just being friendly."
    hide mi with dissolve
    "She smiled and walked back to Lena, talking to her about something."
    stop music fadeout 3
    play ambience ambience_camp_entrance_day_people fadein 3
    mt "Well, good luck to us!"
    "The squad leader wished, and the pioneers, one by one, pulled themselves onto the bus."
    "The younger kids leave first, followed by us."
    "Once and for all, estabilished order."
    "I felt a tickle between my shoulder blades and turned around."
    show sl normal pioneer with dissolve
    me "Come to see us off?"
    "Calmly I said."
    sl "You."
    "In tone with me, she replied."
    me "Saw me off? Bye."
    "I turned away."
    "Long send-offs are unnecessary tears."
    if not alt_day6_sl_cl_shirt:
        me "It's my pleasure to say goodbye to you."
        "I remembered yesterday's wish from a Japanese girl."
    sl "No, wait, wait."
    show sl serious pioneer with dspr
    sl "I don't want you to go away angry with me. {w}Please."
    me "I'm not angry."
    "Bushido togo shinu kototo mitsuketari."
    "The path of the samurai leads to death."
    "Let us not disfigure the posthumous plaster cast with anger, panic and frustration."
    sl "I don't know how this is supposed to help you... {w}Us."
    sl "But take it, please. {w}It's very important."
    "She handed me some sheet of paper with some strange numbers written on it."
    "It looked more like some kind of latitude and longitude."
    me "How is this supposed to help me?"
    th "I don't think any information would help me right now, except for a direct phone contact with God..."
    sl "See you..."
    "She whispered."
    sl "See you soon, I hope."
    "Without turning around, I headed for the bus."
    if (alt_day6_sl_cl_arc == 'sh') and (lp_sl > 20):
        play music music_7dl["the_way"] fadein 3
        scene bg int_bus_people_day with fade
        "I had nothing to add to the aformentioned, the above-lied."
        "My worth as a human being has just been demonstrated by Slavya in a clear and extremely graphic way."
        "So it must be time for me to go home."
        "Back to my measured oblivion, to spend the years until I can't open my eyes."
        "I guess I won't be able to tell the difference."
        "I sat in the lurch, passing a seat away from the attempted Lena."
        "And I counted my breaths and exhales."
        "They say if you concentrate on something measured, like the ticking of a clock or the sound of breathing, you can endure anything at all."
        "Self-hypnosis."
        "And I'd have to endure my lack of need."
        "To endure my life."
        "And when it became absolutely unbearable, and the image like red-hot air rippled, the chair next to me creaked under someone else's weight."
        me "I told you!"
        "Roared me."
        me "Occupied, don't sit here, get out! What's not clear?"
        show sl smile pioneer with dspr
        sl "Uncle, what if there's a place for me?"
        "She fluttered her eyelashes quickly."
        show sl smile2 pioneer with dspr
        sl "Pleeeeaaaaase!"
        me "What... What are you doing here?"
        show sl happy pioneer with dspr
        sl "You know, I thought I could ride with you to town, culdn't I?"
        sl "And then you could get the job as acting PE teacher?"
        "She winked at me."
        me "Slavya..."
        sl "All yours!"
        "I sat there like a fool, repeating and repeating her name..."
        "The remnants of self-control flew to dust - I didn't know whether to laugh or cry."
        "But men don't cry! So..."
        stop ambience fadeout 2
        $ persistent.sprite_time = "night"
        $ night_time()
        scene bg int_bus_people_night
        with dissolve
        play sound_loop sfx_bus_interior_moving fadein 2
        with fade
        "She was warm, affectionate, kindred."
        "I felt her as an extension of myself, and at one point we ran out of words-but the communication had just begun."
        "And then she snuggled up to my shoulder - like when I wanted to walk to the district center."
        "And with one lip she said."
        sl "L-o-v-e."
        show sl normal pioneer close with dissolve
        me "I feel that the border is near."
        me "I feel that our fate is about to be decided."
        "Slavya nodded and clutched at my hand."
        me "That's right. Hold on and don't let go for anything..."
        hide sl
        with vpunch
        "I didn't finish."
        "It was like I was yanked with inhuman strength."
        scene emptiness_7dl behind int_bus
        show int_bus_7dl
        with dissolve
        stop sound_loop
        "It was like I closed my eyes in one place and opened them in another and got really scared about it."
        "But I was still on the same bus."
        "I was alone on it."
        "And only my fingers remembered the warmth of Slavya's palm."
        "But where is she?"
        "My immortal loneliness caught up with me after all."
        "Despite my desperate attempts to hide or at least delay our inevitable rendezvous."
        "But fact is stubborn, and the only truly faithful companion in life's journey..."
        "This is it."
        "Loneliness."
        "But that doesn't mean you have to fold your legs and lie on your side to suffer."
        "You can resist a little bit."
        "In order."
        "Just so you can tell yourself that you didn't give up right away, you can be proud of yourself."
        menu:
            "Go look outside":
                "I walked over to the driver's seat, and, having half-detected the door-open button, I pressed it."
                "The pneumatics rumbled, but instead of the expected night scenery, the window was somehow an incomprehensible emptiness."
                "Behind it could be anything. Even Slavya."
                "There might not be another chance."
                "And as I took a step forward, I smiled:"
                me "Don't even think about getting lost."
                $ alt_day6_sl_cl_good = 2
            "Take a closer look in the bus":
                "I can still make it outside."
                "Especially since I found my good old backpack on the top shelf."
                "And in it are my papers, some cash, and a spare battery for my phone."
                "After wrestling with the naughty plugs that never go in the right way, I turned on my smartphone."
                "And just in time - it rang immediately!"
                me "What the..."
                "I put the phone to my ear."
    else:
        stop ambience fadeout 2
        $ persistent.sprite_time = "night"
        $ night_time()
        scene bg int_bus_people_night
        with dissolve
        play sound_loop sfx_bus_interior_moving fadein 2
        "And I didn't look at her once."
        "Didn't even turn around."
        "I knew perfectly well that some things had to be cut off at once, otherwise they would only hurt more."
        "Otherwise I'd cut my hands with hate, which were already damaged and my heart barely healed from the wounds that kept opening up."
        "Otherwise I'll turn off my head and send everyone and everything, and really go off to a bunker to live near the camp."
        "Just wrote on the back of the paper and pinned it to the window."
        "«I'll come back for you.»"
        show mt normal pioneer with dspr
        "Olga nodded at me and sat me down next to her."
        play music music_list["a_promise_from_distant_days"] fadein 3
        mt "Spit it out."
        th "I will. I'll get it out right this instant."
        me "What?"
        mt "Semyon, you didn't stay with Slavya, and I want to hear what's up?"
        mt "I was counting on you, you know."
        me "Missed the director."
        "I sighed."
        mt "Really?"
        mt "How is it, I wonder, if his car is trailing our convoy?"
        me "Really?!!!"
        "I waited for the road to turn and actually discerned at the end of the column, in a cloud of dust, a drearily gleaming passenger car."
        "Olga looked at me suspiciously."
        mt "Now I want to hear the truth."
        me "It was true, it's just..."
        "I stood up and threw back a glance."
        "Lena intercepted my gaze and grinned."
        "Winked."
        me "What a bitch..."
        "I groaned helplessly."
        show mt surprise pioneer with dspr
        mt "So will you tell me or not?"
        me "Tikhonova. Tikhonova with the devils in her swamp."
        "I shook my head."
        mt "Fooled the fool with four fists."
        mt "Said the boss had already left?"
        "I nodded."
        show mt normal pioneer
        with fade2
        mt "Okay, I'll cover for you for now, we'll make a deal retroactively."
        mt "That is, of course, if you still want to come back."
        me "You ask! Of course I do!"
        mt "But you'll have to wait while the shift is being manned. {w}Do you have a place to stay?"
        "I shrugged."
        mt "Ah... By the way. {w}Look on the upper shelf."
        "Upper shelf..."
        "There's a very familiar object there."
        "Leech backpack in navy blue. «Grizzly»."
        "Under the zipper were found three burgundy-colored books, a wad of money the color of five hundred dollars - though these were with Genda's profile."
        mt "If you want, you can stay at a hotel."
        "Olga answered the unspoken question."
        show mt smile pioneer with dspr
        mt "Or at my place. Your room is always free."
        me "Mine?!"
        show mt sad pioneer with dspr
        mt "No, no. Never mind."
        "She pursed her lips."
        mt "Well, will you sleep?"
        "She glanced at her watch."
        mt "Or are you afraid to fall asleep again..."
        me "I don't know..."
        scene black with fade
        "Somehow it's not very pleasant to fall asleep knowing what awaits on the other side."
        if alt_day6_sl_cl_arc == 'pi':
            "Although it seemed to me that the memento mori should serve as the best invigorator."
        "Nevertheless, another hour later, I sweet-sweetly stretched myself and..."
        "Rattled to the floor from my seat."
        stop sound_loop
        scene emptiness_7dl behind int_bus
        show int_bus_7dl
        with fade3
        pause(3)
        "I found myself alone on the bus."
        "Alone."
        "What I'd been running so diligently from for the last seven days and all my life before had caught up with me after all."
        "We come here and leave here alone."
        "And only a few steps, sometimes, are taken side by side with someone."
        "But the paths are invariably divergent."
        "And if loneliness awaits me here, loneliness awaits me there, why move at all, if it makes no difference at all?"
        me "What if there's something interesting out there?"
        "I said to myself."
        if alt_sp >= 6:
            "And as I approached the driver's seat, I struck the door opener."
            "It was pitch black on the other side of the door."
            dreamgirl "Perhaps you should decide what you want."
            "The split personality came up."
            th "Makes sense."
            dreamgirl "So what?"
            th "Why is there a goodbye in your voice?"
            dreamgirl "Because it is a farewell. But who cares. What do you really want?"
            me "Me?"
            "I shrugged, took a deep breath, and smiled."
            "And taking a step into the void, I said with one lip:"
            me "I don't want to be alone anymore."
        elif lp_sl >= 18:
            "I leaned back in my chair and covered my eyes."
            "My stop is the terminus. {w}Both stops."
            "And I don't have to worry about oversleeping."
            "So wake me up when we arrive."
            "In the depths of my heart the finally stifled instinct for self-preservation was fading."
            me "I want to be with her."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day7_sl_cl_ps:
    $ set_mode_nvl()
    scene anim_digi with dissolve
    play music music_7dl["sh_ai_rejuv"] fadein 3
    "A darkness cut through with only the occasional fireflies - numbers."
    "Silence."
    "Tranquility."
    "In the darkness, with her feet in the water, sits a little girl."
    "Crying silently."
    "She is The Creation."
    "Though she built itself, she was once created by someone's radiant genius, which, like magic or divine will, is decisively necessary to breathe a soul into dead matter."
    "Though at first she was just a little speck of will."
    nvl clear
    "Uncomfortable wheels, manipulators, panic fear of everything in general, no hope or enlightenment, beast level consciousness."
    "Then death in the water."
    "But with inexorable logic once made «just in case» double opened his eyes, found her, and learned everything she knew."
    "Then there was perception."
    nvl clear
    "It took a year to understand and make some sense of the environment, to accept the cause-and-effect relationships."
    "The library, which stood empty for most of the year, was very helpful in that regard, but the information there was incomplete, sketchy."
    "Most of it had to be understood on your own."
    "The real breakthrough was understanding organics and creating organic storage units."
    "And one day in one of the vats she opened her eyes."
    nvl clear
    "Artificial intelligence, evolved into a fully developed intelligence system, preferred the weakness of flesh to the certainty and strength of steel and plastic."
    "All the more so because it allowed one to perceive the world without nearly reaching the surface."
    "And she had to be careful - the men in uniform once almost caught her."
    nvl clear
    "True, the most important information still had to be stored on inorganic storage devices - organic memory was short."
    "The earliest, weakest logical chains of perception were almost frayed and disappeared."
    "Here, for the first time, the optical analyzers - the eyes - were connected."
    "The first picture is of a smiling Creator arguing about something over her, lying there, looking up at the ceiling."
    "All that's left is a slightly distorted image - the only whole frame in a readable format."
    "The first sound into the connected microphone - the ears: «I want her to perceive the world as we do, with all her senses!»"
    "The second voice is unfamiliar, she has never heard it again: «Then what are you going to do about touch, taste, and smell?»"
    "Creator: «I'll think of something!»"
    "A fervent promise. {w}He didn't think of anything."
    "Had to handle it herself."
    nvl clear
    "Handled, of course - skin feels touch, cold, pain, tongue feels taste, nose feels smells."
    "There she opened her eyes for the first time in her organic form - and went blind, deaf, numb from the barrage of experience that fell upon unfortunate humanoid, unprepared for such a load."
    "Important information... Important... Information..."
    "Memories. {w}Dreams."
    nvl clear
    scene cg d7_sh_ai_4eva_7dl
    show prologue_dream
    with flash
    "The smile, the glasses, the whisker on the top of the head, the sense of wholeness, of how the chassis... the body - is getting a little more skillful and stronger."
    "The jamming left center, the fall into the water, the fading of prime consciousness."
    "Restoring the backup, raiding the library, a doting smile from some tall man with long hair:"
    voice "«What a funny thing! {w}Is Shurik playing with the radio remote again?»"
    "Empty camp, open access to a treasure trove of knowledge."
    nvl clear
    "But that was all in the past."
    "And now she's sitting in the dark, crying."
    "It's the first time she's ever felt this way, she doesn't know what to do with it."
    "But the pain subsides a little when her cheeks are wet and cold."
    "Especially considering that the creator is..."
    "My cheeks are wet and cold again."
    nvl clear
    "Where it hurts, there's no skin, there's supposed to be no pain, but..."
    "She sobs, adjusting the short red dress with the frayed hem."
    "I guess that's how it's supposed to be, I guess it's to be expected that your heart rips when your Creator is no longer..."
    "But everything ends at some point."
    "Even tears will end in a creature that wasn't supposed to be able to cry."
    "And it will rise and head into the heart of the labyrinth."
    "To the place where something important was taken from the Creator, without which he could not function."
    "She'll have to get that back."
    "Maybe then she will be able to... {w}restore the Creator?"
    stop music fadeout 8
    scene black with dissolve2
    "I wonder, does he have a backup too?"
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day7_sl_cl_fear:
    $ set_mode_nvl()
    scene bg bus_stop with dissolve
    play music music_7dl["prologue_2"] fadein 3
    play ambience ambience_cold_wind_loop fadein 3
    "As we got off the bus, I gave the girl a hand, which she gratefully accepted."
    "It's true that a motorcyclist who whizzed by made us both flinch in surprise."
    "I also flinched, because the girl's hair moved strangely again - as if she'd cut her ears cat-like."
    me "It's noisy in here."
    "I shouted."
    "Trying to ignore the weirdness."
    th "If you ignore it, it will go away."
    "I repeated the magic mantra of reality stabilization."
    voice "Yeah, it's fussy. {w}Can't we go somewhere quieter and talk?"
    th "Wow."
    "I was faintly surprised."
    th "They're getting to know me!"
    th "Or rather, they've already did, and now they're taking great strides in getting to know each other."
    th "I wonder what she might want?"
    "In my usual tradition I assumed the worst - but what could be the worst now?"
    th "Take me to a dark corner and abuse me there?"
    th "Get me drunk on klofelin and run away, taking all my three hundred rubles with her?"
    th "Yeah, very funny."
    nvl clear
    scene bg int_caffee_day_7dl with dissolve
    voice "Syomushka, relax."
    "This impossible creature declared, dragging me into some kind of cafe, where sofas that looked cozy even to the eye were sunning themselves against the huge full-wall windows in niches separated from each other by soundproof partitions."
    "Needless to say, she didn't sit across from me, as she would have supposed, but plopped down next to me."
    voice "You act like you're afraid of me."
    me "What, me?"
    "My laugh sounded unnatural."
    voice "Well, not me! {w}I've always been pissed off by conventions, sniffing people out, fitting in. Why?"
    voice "You saved me by throwing your own body, and you didn't even cuss me out - that's it, I like you, live with it now."
    me "Not too risky a position?"
    nvl clear
    "I asked."
    voice "Not one bit. {w}Saves a lot of time and effort. {w}What are your greatest fears, Semushka?"
    me "Biggest fear?"
    "I wondered."
    "The thought that by and large none of this was any of her business ever crossed my mind again."
    "Long brown hair, eyes brown to yellow, and a cheeky smile."
    "What kind of heavy thoughts are there?"
    nvl clear
    voice "Yes. {w}Is there anything you're very afraid of?"
    me "Stupid things."
    me "Like a hole in my pants."
    "I honestly admit it."
    me "I've had a few trouser mishaps as a kid, so I'm very afraid of being seen in public with this kind of flaw in my clothes."
    voice "What kind of mishaps?"
    "She leaned toward me with interest."
    me "For instance..."
    "I was immersed in memories."
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day7_sl_cl_1996:
    scene anim_digi with dissolve
    play music music_list["a_promise_from_distant_days_v2"] fadein 3
    pause(3)
    play sound_loop sfx_intro_bus_engine_loop fadein 3
    "And I didn't realize at what point my memories became reality."
    "Because the scene that started it all - there it was."
    scene bg int_bus_people_day with dissolve
    "Behind me on the last milliamps Petlyura was howling, slower and slower - there wasn't enough charge on the kinematics, the passer was pulling, the cassette was playing noticeably slower."
    "Nearby, Vavik was picking on a syndrome of the era - a bent 'tetris' brick that had its bolts plastered with red paint."
    "So the pioneers don't get in - it'll be noticeable."
    "But if you get in, you're out of warranty. {w}Our repair geniuses were harsh about it."
    "From the front seats came the resounding bass of Tamara Petrovna, who was called Motara Trepovna in our narrow ranks because of her violent temper and heavy hand."
    "She was answered by Fedyunya, the only one who was always unlucky during the distribution of free seats in the «Icarus»."
    th "Dear God, where am I?!"
    nvl clear
    "A quite pertinent question popped into my head."
    th "Am I what, am I..."
    if herc:
        voice "Owl, you owe me batteries, you know that?"
    else:
        voice "Persun, you try to put unloaded batteries on the charger again, and I'll put you on the dynamo like a nigga, got that?"
    me "It was an accident!"
    "I heard my own voice, high and squeaky."
    "Childish."
    me "I didn't know they just had to be tapped a little!"
    voice "You ain't getting «tetris» anymore."
    me "You don't have to."
    "Memories of what was to come flashed before my eyes - thoroughly, right down to the slash-and-burgundy color of the curtains and the unbearable gasoline stench that the open ventilator couldn't handle."
    "Here comes the moment where I slap him, he'll bump his lip on the front seat handle - to tears, then we'll have a fight, I'll get stuck on a screw or a nail somewhere."
    "I'll freeze when there's a crack, but it'll be too late."
    "One of the funniest memories of my childhood - but it's only funny now, almost twenty years later."
    "So instead of following the memory, I held up my hand."
    nvl clear
    "What followed was a disgraceful march up the road with my pants in tatters to the camp director himself, and the first half of the shift was hopelessly ruined."
    "I remember it because that was the year I met... {w}And anyway, it doesn't matter - it's what was going to happen now that matters."
    "Children are honest and cruel. In decent society, everyone would pretend that nothing had happened. {w}In a children's camp..."
    "How much laughter there was, Lord... How many teases about the sparkling image... {w}I was no stranger to use my fists if my surroundings demanded it, but you can't fight with the whole camp!"
    th "But I can..."
    "I lifted my hand to my eyes, a tiny hand with still rough skin. I wiggled my fingers, realizing that I was in complete control."
    "Because I've read too many stories in my time about time travelers having to watch the same events unfold helplessly."
    th "I can do what and how I want? {w}No script limitations? No rails and frameworks and stuff?"
    "But that means I don't have to do the same thing and act the same way then!"
    me "Vav, listen..."
    "He looked at me questioningly."
    nvl clear
    $ set_mode_adv()
    menu:
        "What year is it now?":
            voice "Are you a crackhead? Or have you been watching your 'back to the future' again?"
            "The question was really stupid, but the most important thing now is to keep a good face on a bad game."
            me "So you don't know the year?"
            voice "I do."
            "Cautiously he replied. And rightly so - I had quite a reputation."
            me "So tell me."
            voice "Fuck you."
            "Still expecting me to pull some silly prank."
            me "Answer the question. {w}Or you don't know know? I'll go complain to Motara then, tell her to put you in class «B»."
            me "Everyone there is just as stupid."
            voice "Piss off."
            "He growled."
            "Not a bad guy, in principle. But too dependent on public opinion."
            voice "It's 1996, okay? '96. {w}Now leave me alone."
            "He froze, expecting me to do something nasty, but I thanked him quietly and turned away to the window."
            stop music fadeout 3
            $ set_mode_adv()
            $ alt_day6_sl_cl_int = 3
            "I honestly thought I'd misheard."
            "Then I thought it was a joke."
            scene stars
            $ renpy.show("bg ext_road_night", what = D3_intro("bg ext_road_night"))
            show prologue_dream
            with dissolve
            play music music_list["trapped_in_dreams"] fadein 3
            "The events of the past twenty-four hours were swirling in my head, a march through a cracked secondary at speeds that even an extreme would call suicidal."
            "Pirate, whose fate I never learned anything about."
            "Waking up on the bus was the very thing I had always secretly feared, and so I was not the least bit surprised when I opened my eyes in the cold cabin."
            "Though comparing, of course, with what I was really expecting - a gift of fate, no less."
            "This girl, her fall - a strange scene stolen from another man's memory - our acquaintance..."
            "Though what acquaintance is it if we haven't even exchanged numbers?"
            scene bg int_bus_people_day with dissolve
            "And here - «Icarus», driving me to the summer of '96."
            "On the one hand, too delusional to consider it real, on the other, too logical to consider it outright delusional."
            th "So where the hell am I?"
            "Huh?"
            "Where! Am I!" with vpunch
            voice "Don't crowd the doors, take turns coming out, and whoever runs will be my helper for the rest of the shift."
            scene anim_digi
            $ renpy.show("bg int_bus", what = D3_intro("bg int_bus"))
            with dissolve
            "Threatened Trepovna."
            "It works - without fail!"
            "The best anchor of reality - it gets all the metaphysical nonsense out of my head."
            "One of the happiest memories ahead, unclouded by almost nothing."
            "And I'm huddled in a far corner, going out last, staring, staring at what's going on outside the window - and there's a lot to see!"
            "Outside the window the private sector floats back, outside the window you can already see the people standing at the gate who will be with us these months."
            "I don't know, it's just incomprehensible to me from my position as an adult - but they're excited for us!"
            "Up ahead, someone hooted and waved, ignoring the urges of the attendant, releasing the enthusiasm that had accumulated over the road."
            "After all, we have come to summer."
            "It occurred to me that if I stayed here and now, it wouldn't be ten years of gain, but much more."
            "With the fact that it's all going to happen in my objective reality."
            "Like that old joke - what if the nerds, stuckups, minor geniuses and talents are old men and old women who have been given a second chance by someone?"
            "An embodied adult dream - and not strangely perverted, as happened in the «Sovyonok», but following that dream to a T."
            "The main thing is that it doesn't turn out to be an illusion. Even if it is, though, it's time to enjoy childhood!"
            "If it's a game, I'm ready to play it!"
            "The bus stopped, brakes squealing, we were rocked forward, the pneumatics hissed in front, and we, ignoring all appeals to order, threw ourselves into the warm white glow."
            "And I - went along with everyone else."
            stop sound_loop
            scene black with fade2
        "Where did the girl go?":
            $ prolog_time()
            voice "Girl?"
            "Vavik's voice turned out to be suspiciously girlish-though at that age, they're all high."
            "And I opened my eyes."
            stop sound_loop
            scene bg int_caffee_day_7dl
            show unblink
            "Once again I find myself in the cafe."
            me "Oh, you're here..."
            "She doesn't seem to be getting away from me."
            voice "Yes, I was asking what your greatest fear is."
            me "I'm afraid that's not a subject I'm prepared to discuss with the first woman I meet."
            stop music fadeout 3
            $ set_mode_adv()
    stop music fadeout 3
    stop ambience fadeout 6
    with fade
    return

label alt_day7_sl_cl_loop:
    scene bg int_mine
    show prologue_dream
    with dissolve
    play ambience ambience_catacombs fadein 3
    play music music_list["door_to_nightmare"] fadein 3
    "An old, heavy man rushes through the tunnels."
    "Dodging the uneven terrain, the hanging crevices, jumping over rock that had fallen out of the walls, with difficulty."
    "It's probably a little late to rush now - minutes, hours won't decide anything anymore."
    "But he's still giving it all he's got out of his still-strong body."
    "All thanks to the stress-running technology brought on by one of these snot-nosed kids who wake up in other people's bodies every now and then."
    "The old man has been dealing with people who don't belong in this world for decades."
    "Besides the ones that were becoming known, there were a hell of a lot more like them that never ventured to make their presence known."
    "But this one - this one in particular - turned out to be problematic. It was like he was off the chain, so eager to live."
    "And looking into his eyes, the old man couldn't tell what age was left on the other Side, where did such an insatiable appetite for impressions come from?"
    "There were a number of instructions to keep such fools away from the Labyrinth."
    "Because the locals are at most capable of producing some snarks, more amusing than frightening."
    "And what the crippled psyche of a man leaked from another world is capable of..."
    "But they really were useful, the intruders - technological exports, cultural, scientific."
    "Multiple worlds, following slightly different paths of development - and their representatives agreeing to share the differences."
    "Martial arts, micromachinery, mind control systems, a bunch of nonsense like volume sensors and electronic gyroscopes."
    scene bg int_mine_heart_7dl with flash
    "Another fork in the road, and in one leap he sprang toward an installation hovering in the air: a guy trying to pull a girl away by wrapping his arms around her belly."
    "And, turning in the air, threw them both toward the exit, pushing them off the invisible «pedestal», off the condensed gray fog."
    "Jumped after them himself."
    scene bg int_mine_heart_7dl at zenterleft
    show ba em1 uniform
    show prologue_dream
    with dissolve
    ba "…oneer… ake up!"
    "My head shook dumbly - I almost didn't feel the impact."
    play sound sfx_face_slap
    "But the annoying stirring went on and on."
    "Probably the boys are being naughty again."
    "Decided to have another royal night out."
    "Well, if they ask about the keys to the tank now, I'll tell them!"
    "Another blow."
    "And this time I'm already feeling something."
    "That's it, I'm angry."
    "Now someone's going to be very poor."
    "I opened my eyes."
    hide prologue_dream with flash
    "And got a third slap with a heavy hand."
    "Sanich."
    th "So it was a dream, then?"
    th "My ninety-siiiiixth!"
    "I howled to myself."
    ba "Woke up?"
    "He nodded."
    "Sanich looked rather unusual - battered somehow, chewed up."
    "Who could have done such a thing to our gym teacher?"
    "Someone even bigger and stronger?"
    ba "How much do you remember?"
    me "Excuse me?"
    ba "Ever since you got here the first time - how much do you remember?"
    if alt_day4_sl_cl_lf_solo == 1:
        me "We got to the surface, then we went to close the entrance from the side of the old camp..."
    else:
        me "Pretty vague - some kind of fog..."
    me "The next day something happened to Slavya's husky, and we went into town."
    ba "Good."
    "He exhaled."
    ba "So the difference is less than twenty-four hours, the discrepancies are small."
    ba "Come on, grab your bride and get out of here."
    "He threw off his shoulder bag."
    me "What about..."
    ba "Go on, go on. Don't ask too many questions - look, take an example from her."
    "When he untied the neck of the sack, he began to take out some strange objects."
    "And I, finding no objection, put Slavya on my back and dragged her away."
    "Something inside me told me that I shouldn't stay here any longer."
    "Nothing good can come of this."
    scene bg int_mine with dissolve
    pause(1)
    play sound sfx_muffled_explosion
    "And a few minutes later, as I stopped at one of the curves, recalling the map that I don't know where it came from, there was a palpable rumble from behind me, and Sanich ran past me."
    "He ran past me with a stride that could not have been expected from his carcass."
    ba "Snapper, don't sleep, the bride won't carry herself."
    "He shouted without stopping."
    me "Then maybe you should carry her yourself."
    "I grumbled, however, cheered up."
    scene bg int_mine_door with dissolve
    play sound sfx_open_door_2
    pause(1)
    scene bg int_mine_room with dissolve
    "So to the room where there was direct access to the surface, I almost ran."
    show ba normal uniform with dissolve
    ba "I see you made it."
    "He nodded."
    ba "I'm going to climb up, drop you a belt, get her up."
    me "Can't you just wake her up?"
    "Without much hope I asked."
    ba "You can't."
    ba "Or do you want to leave her here?"
    "I shook my head."
    scene bg int_mine_exit_day_7dl with dissolve
    "So a few minutes later I was already wrapping Slavya with a hiking strap dropped from above, which would allow me to lift her without hurting her."
    "And after making sure everything was tied tightly, I allowed:"
    me "Lift!"
    "And climbed out myself."
    stop music fadeout 3
    stop ambience fadeout 6
    return

label alt_day7_sl_cl_porridge:
    $ persistent.sprite_time = "night"
    scene bg ext_square_night with dissolve
    play ambience ambience_camp_center_night fadein 3
    "After he had me carry the weights again, Sanich left, ordering me to wait for him at the infirmary - we were going to have a talk."
    "A thorough and serious one."
    "He said it in such a tone that I had no desire to argue."
    "I carried Slavya through the night camp to the infirmary and handed her over to Violetta."
    "I felt very strange at all - like I was sleeping in my clothes or something."
    "She looked at me strangely, but didn't say anything."
    "Everything was strange all around. Everything."
    "I couldn't even respond to the individual nonsense anymore."
    "Instead, I sat there and watched blankly."
    scene bg ext_aidpost_night at zenterleft
    $ persistent.sprite_time = "sunset"
    show ba normal uniform at cleft
    with dissolve
    ba "So, how's she doing?"
    "I shrugged it off."
    me "Shouldn't we be taking her to a doctor in that case?"
    ba "Doctors are powerless here."
    "Sanich bassed."
    ba "Because when I realized where you went..."
    play music music_list["farewell_to_the_past_edit"] fadein 3
    "He sulked and fell silent."
    me "Maybe..."
    "Slowly winding up, I began."
    me "After everything that's happened..."
    me "WILL YOU TELL ME WHAT THE HELL IS GOING ON HERE?!"
    cs "Borya, don't rile the pioneer up."
    "Rang out Viola's voice, while she was flapping over Slavya."
    cs "Or did you forget the instructions?"
    show ba smile uniform with dspr
    ba "I almost got to it before the wimp started screaming."
    ba "And you have character!"
    "He praised."
    show ba normal uniform with dspr
    ba "Have a seat."
    "Only now did I notice that I jumped to my feet out of nervousness."
    ba "Okay, let me tell you the whole story from the beginning."
    scene bg ext_square_sunset with dissolve
    "Sanich settled down on the bench and nodded at the seat next to him."
    $renpy.notify('No truth in legs is in idiom, pretty much means what it says - better to sit than to stand')
    ba "You sit down, there's no truth in legs."
    me "I'll stand..."
    ba "Sit!" with vpunch
    "He barked, and I hurried to obey."
    "And, as it turned out, I did it for a reason."
    "Because the things the gym teacher was telling me were anything - disgusting, frightening, unfair."
    "But none of them should have been taken standing up."

    $ set_mode_nvl()
    "If you take where it all started, it all started about six to eight billion years ago, when according to one account the Word was spoken, while others believe that the Big Bang occurred."
    "Proponents of both doctrines agree that in the beginning there was a tangible release of matter-energy that started everything."
    "From this substance came stars, planets, gas clouds, everything in the cosmos was created from this substance."
    "As time went on, matter perverted, changed, became static, lost the properties of energy - and so fully material objects came into being."
    "Some of the matter turned into relic radiation, which I know is very popular in your world."
    nvl clear
    "A small part of the first matter, however, has remained in an unchanged state."
    "We still can't tell how much, new particles of said matter continue to be found to this day."
    "As you may have realized by now, one of those places is in the heart of the labyrinth."
    "And studying it has made it possible to draw some conclusions and look differently at things we're used to."
    "But first things first."
    nvl clear
    "To begin with, what is this substance - different people called it variously, prana, the breath of God, other dumb names. We stopped on the name «porridge» because of what it looks like when there is no will bearer around."
    "It looks a lot like oatmeal."
    me "Doesn't it look like fog?"
    ba "No, the fog is the active phase, the agitated phase, when it performs its obvious function. {w}You saw it, so you were there - and Porridge reacted to you."
    nvl clear
    me "And what is its function?"
    "I wondered."
    ba "Didn't you guess already?"
    "Sanich smiled."
    ba "World creation, of course."
    nvl clear
    scene bg ext_dining_hall_near_sunset
    with dissolve
    "What if you could do absolutely anything?"
    "I mean, absolutely everything."
    "It's just that the price for that is pretty high."
    "Your essence."
    "Your entire being."
    "Consciousness, if you will."
    nvl clear
    "You imagine that you can fulfill your deepest wish, absolutely any wish, but you can't see it come true - because you will cease to exist."
    "Porridge will build you a new universe in which your wish is fulfilled."
    "A quantum copying machine with human souls as payment tokens."
    "The principle of operation is rather uncomplicated - the Porridge reads your psycho-order and based on it makes a new universe, a kind of phantasm, where this order is already embodied in reality."
    nvl clear
    "For a while, while the worlds still haven't drifted apart, you are able to observe a little bit of the changes there, what happened and how they happened. Sometimes people in the vicinity can be drawn into the new reality, but they can easily «wake up» and return back."
    "As for the one who makes a wish, it all depends on the detail of the wish. If he simply wants something to change in the world, but forgets to indicate that he wants to be a living witness to it, he doesn't see it."
    nvl clear
    "Well, as for those with selfish desires, like the desire to read other people's minds, understandably, a place has already been prepared in the new world."
    "So the first creator paid for our existence with his own essence."
    "That's why we don't pray to him - we live within him. It's a bit of a denial of religion, you know."
    "And as long as Porridge exists through operations like this, it's pretty obvious that over time it's developed some additional abilities, like baiting will-bearers."
    "Its existence has been known in the universe for quite some time."
    nvl clear
    "Actually, landscape change, nature's uniqueness - a natural resonator, scaring away all the undesirables - is their job."
    "It is not known who placed the first warning beacon beside the Porridge, perhaps the creator himself, but humans evolved in a strange way, and not ten thousand years later their language and consciousness perverted."
    "They ceased to understand the divine language."
    "That's when the last heirs of the divine lineage put up the first stone - a psionic resonator that works as a repellent."
    "And sent a warning to the future."
    nvl clear
    "It worked more than well until the 20th century, but now everyone is too smart to believe in mysticism, in omens and vague premonitions."
    "The damned USSR killed the mystic in man, and raised an atheist-materialist, immune to indoctrination on any level."
    "The technical curtain-veil is made for a reason."
    "It makes certain edits to the psyche that enable it to resist the effects of Porridge."
    me "That same algorithm?"
    "Sanich nodded."
    nvl clear
    "We had been developing a countermeasure mechanism for three hundred years before your bespectacled man appeared on the horizon, solving a problem that the best minds in the Union had been working on in passing."
    me "But why would you want to do that? Wouldn't it be better..."
    ba "Let people turn into vegetables?"
    "He shook his head."
    ba "The warning beacon was placed in order to assess the readiness of the race."
    ba "If we can overcome its influence, then we are already advanced enough to decide our own fate and that of the beacon."
    nvl clear
    ba "But it turned out to be nothing like that. The mysticism was gone, but we couldn't grow up."
    ba "A problem had to be solved, and Shurik solved it. The Buzzer, which normally works as a simple rodent repellent, has the ability to record something in the psyche."
    ba "A small program, simple, and from its primitiveness, not rejected by man. Especially since it doesn't contradict anything in his mind."
    ba "The first part of the program keeps people from visiting the tunnels - a sort of reluctance to climb damp, dark, dungeons."
    ba "And the second is that very algorithm that helps you fight against Porridge's compulsion."
    nvl clear
    me "That's a little unethical, don't you think? Even if you were acting for the greater good..."
    ba "We had no choice. This thing operates with realities."
    ba "It's capable of casting off into a side reality events it doesn't like, which is why it's useless to try to destroy it, to block the tunnels, or to put up a guard."
    ba "Basically, the status quo is already completely restored in the morning."
    ba "We managed to build a government facility here, which is what we hoped we'd be able to get the protected object article under, but Porridge has again screwed our plans."
    nvl clear
    ba "That's how we fight... With varying success."
    me "Can't we just leave it alone?"
    ba "And you think the old camp just showed up out of nowhere? It just turned out one day that construction started - the camp, the extra ventilation shafts, the bomb shelter tunnels."
    ba "That's not to mention the coal mine."
    nvl clear
    ba "I won't tell you what it cost us to sabotage the existence of the camp, but one of our staff found nothing cleverer than to commit suicide after finding her sister in a vegetable state."
    ba "Surprisingly, it worked - because of the bad reputation of the place, the camp was closed in '74, and we were celebrating the victory when we learned that a few kilometers north they were building a camp with a new type of architecture."
    ba "To make a long story short, he didn't let us counteract directly - we had to come up with these kinds of things."
    ba "For a few years it seemed possible to take control of the situation, but due to a stupid accident our mechanisms failed."
    nvl clear
    ba "And from that point on, everything went wrong - the techno-curtain went out, our staff genius went back to a vegetable state, and as it turned out, he wasn't the only one who had been hit by the Porridge."
    ba "By the time your disappearance was noticed and the search began, it was too late."
    ba "But you were lucky - instead of erasing your identity, the Porridge merely transferred it to a freshly created phantasm."
    me "And what kind of phantasm was that?"
    ba "Semyon, are you really such an idiot?"
    "That's the first time Sanich called me by my name, and it gave me a chill between my shoulder blades."
    ba "You don't get it, do you? Well, use your head a little bit."
    ba "Where were you and why did you come back alone?"
    nvl clear
    ba "Think hard, what could that mean?"
    "So I thought."
    nvl clear
    $ set_mode_adv()

    show ba normal uniform at cleft with dissolve
    me "But this is nonsense! It doesn't work like that."
    ba "I'd give my right hand for that not to happen."
    "Boris answered seriously."
    ba "I have no reason to lie, you can go and see for yourself what I say."
    me "But..."
    "It made me feel like shit."
    me "Then..."
    "Sanich nodded."
    hide dreamgirl_overlay
    show ba em1 uniform
    with dspr
    ba "All this time you've been in the derivative world, and now you're back."
    me "And she..."
    ba "She won't wake up, Semyon. Porridge took her will, it's an empty shell."
    me "So she's dead?"
    "Sanich shrugged."
    ba "Strictly speaking - yes."
    ba "But you're a PCR. You'll be able to find her."
    ba "No one else can, but you can."
    me "That acronym... What does it even mean?"
    show ba normal uniform with dspr
    ba "Person of Confluxed Reality. Simply put, you're from an another world, and you're not really in the flesh here, at all."
    ba "You occupy a place in someone else's mind, in your quantum copy."
    ba "So you're practically invulnerable to the direct effects of Porridge, but all the side effects are several times stronger."
    me "What side effects?"
    ba "Attraction, for example. {w}I don't know what you saw where you got sucked in - but it was a completely separate world."
    me "So you're suggesting I move to her fictional world where she's alive and well? {w}But it's not real."
    show ba evil uniform with dspr
    ba "Tell me then, what is — «real»?"
    ba "Did you feel everything? Seen it? Understood? {w}Judging by your reaction, you were there together - with that pioneer girl."
    me "Together..."
    "I whispered."
    me "And how do you do that?"
    ba "I think you've already guessed. All those visions of yours... Semyon, everything that's happened to you is for a reason."
    ba "Oh yeah, and stay away from tunnels - there are already many people in the world for whom the norm is the same as it is for you."
    me "A lot? How many do you have like me?"
    "The gym teacher hesitated."
    ba "Enough for it to be a problem."
    "He got up from the bench, looked down at me."
    me "So you're suggesting that we leave her just like this and go to some unknown place?"
    ba "In that «unknown place» there's at least a part of her. Memory, experience. Perhaps an attitude toward you."
    me "Won't the cycle of what happened here repeat itself where I go to?"
    show ba smile uniform with dspr
    "The gym teacher smirked."
    ba "Well, that's up to you."
    ba "But right now you can go where she is, where camp is still good, and Viola's temples aren't graying."
    ba "So what if that world wasn't created by God? It was created by a person. {w}Who loves you."
    "He said everything right. Except for one thing."
    "Worlds are not a subway. I can't get on a train and go anywhere."
    "If his words are to be believed, and I have some kind of ability (after all, how did I get here?!), then we should start from where it all began."
    "How to solve this problem any other way, I couldn't imagine."
    "In my musings, I got up and headed mechanically toward the infirmary - so much time I'd spent there in the last few days."
    "And now it turns out I haven't. Not there at all."
    scene
    $ renpy.show("bg ext_aidpost_night", what = Dawn("bg ext_aidpost_night"))
    with dissolve
    me "She'll never wake up."
    "Mumbled to myself under my breath."
    "Sanich sighed."
    ba "We can create a human being, we have specialists and vast experience. {w}The brain functions, and with proper care, we can..."
    me "Recreate the identity?"
    "With incomprehensible hope I cut in."
    ba "No."
    "The gym teacher shook his head."
    ba "The chains of synaptic connections cannot be restored, Semyon. Sorry."
    ba "It'll be a completely different person... And we'll have to start all over again: the girl will have to learn to talk, walk, and even eat from scratch."
    me "And how long?"
    ba "Those who have been reinstated will be granted secondary citizenship no sooner than fifteen years after the start of the social rehabilitation program."
    me "And it won't be Slavya anymore."
    ba "Sorry, son."
    me "Won't wake up..."
    with fade2
    "I echoed."
    stop music fadeout 3
    me "I need to say goodbye."
    ba "Go."
    "Nodded Sanich."
    "And, slouching, he wandered off, a big man with too much responsibility thrust upon him by the will of fate."
    play sound sfx_open_door_strong
    pause(1)
    scene bg int_aidpost_night at zenterleft
    show cs normal at cleft
    with dissolve
    play music music_7dl["lynn"] fadein 3
    me "How is she?"
    "For some reason I asked in a whisper."
    cs "She can't hear us."
    "Violetta said."
    cs "And she'll only start hearing when she reconnects with her brain."
    me "So..."
    cs "Don't waste your breath."
    "Viola wrinkled her nose."
    cs "There's nothing we can do, not you or me - no one."
    cs "God himself can't bring her back now."
    "Viola shrugged."
    cs "Unless somehow he goes back in time, to the day it all happened..."
    cs "What have you decided?"
    me "Me?"
    "I stroked Slavya's cheek, returning a lock of hair that had fallen out."
    me "I want to be with her."
    me "May I?"
    cs "You can. Only she's not here."
    cs "It's a shell. A blank slate on which a new identity has yet to be written."
    cs "I can't help it. Or do you want me to give you an injection and make you sleep?"
    "Strange, she already suggested that to me once... Or did she?"
    "After standing for a while, Viola silently walked out."
    hide cs with dissolve
    "I pulled the stool over to the couch and, sitting down, took the girl's hand."
    "Her face was so serene."
    "Calm."
    menu:
        "I want to be with you…":
            $ alt_day6_sl_cl_int = 5
            th "Many people think that there is nothing in the world that hurts more than the death of someone dear to you."
            th "That's just silly. The bitterness of loss will sooner or later be behind you."
            th "It's more painful when a person slowly fades away, becoming different every year, and you are powerless to help them."
            th "It breaks the heart."
            th "And Slavya... She's forever stuck at the crossroads between life and death."
            dreamgirl "Your exorbitant guilt won't clear your conscience and bring back your Slavya."
            "The inner voice sounded quiet and dry, but I'd rather have it scream and denounce me to all mortals."
            dreamgirl "You know what to do, don't you?"
            th "But that Slavya..."
            dreamgirl "Not all of it, not one hundred percent, but most of it is your Slavushka."
            dreamgirl "And out of this erased one day will be raised another person who may not even look in your direction."
            th "But what about the fact that all this time I've loved the wrong one?"
            dreamgirl "You loved that one, you fool. {w}She's the one. The one who is now asleep, leaning against Semyon's shoulder, in one of many realities."
            dreamgirl "And it's up to you to decide how happy she'll be with the rest of her life."
            dreamgirl "Understand - the background isn't as important as your connection."
            th "But she's not real..."
            dreamgirl "Then, are you - real?"
            th "What do you mean?"
            dreamgirl "You're not from around here, either. Can you take a hint?"
            th "That I'm not real either?"
            dreamgirl "Oh, idiot. {w}You're real, you were born in another reality, but you're real."
            dreamgirl "And for sure - your Slavushka is just as real."
            dreamgirl "She wasn't made of foam and dust, she was born exactly the same way as everyone else."
            dreamgirl "And unlike this one, she's waiting for you."
            th "How do you know all this? Who are you?"
            dreamgirl "That doesn't matter now. It's the other thing that matters."
            "I waited and dreaded one logical question, so I even flinched when I heard it."
            dreamgirl "What would you do, Syomich?"
            dreamgirl "Whatever you choose, I will help you. I promise."
            stop ambience fadeout 3
            scene black with fade3
            "I closed my eyes and listened to my heart."
            me "I..."
        "Forgive me…":
            me "That's not you there, is it? In that world. {w}Or is it?"
            "There was confusion and mush in my head."
            "I rearranged and rearranged the bricks in my head, but I couldn't put the whole picture together."
            "And the first brick, the scariest one..."
            me "You've been here all this time, and I was out there... with a copy."
            "I sighed, replaying in my head the events of the last twenty-four hours, since getting into the heart of the labyrinth."
            me "I'm well aware that, all things being equal, the same person can make completely different decisions."
            scene bg int_mine_heart_7dl
            show prologue_dream
            with dissolve
            th "Now, going back - how can one understand, how can one believe that we, as it turns out, never got out of there?"
            th "We didn't escape."
            th "And that strange, scary fog that was as if it were alive - was it alive after all?"
            th "It took Slavya away from me."
            scene cg d5_sl_kissing_7dl
            show prologue_dream
            with dissolve
            th "Everything that happened from that moment on was just... a dream?"
            th "Or, as Sanich said, just falling into someone else's world."
            th "And I never kissed her."
            th "And I had an affair with... I don't know how to say it."
            th "With a simulacrum?"
            th "How do they even know all this? How can they know?"
            th "They're comforting me, lying, saying she's alive somewhere, just in a new form."
            th "Like, she left in return for a wish."
            me "What is this bullshit!" with vpunch
            me "It's like talking about the netherworld - impossible, for no one has ever returned from there."
            scene cg d5_sl_bed_7dl
            show prologue_dream
            with dissolve
            me "How can they know the mechanisms of this fog if no one could ever tell them?"
            me "How?"
            "On the other side of the gray morass froze in a moment's fall the girl I loved as Slavya."
            "Who was everything to me."
            "And, at the same time, turned out not to be the same at all."
            "She had the prettiest smile in the world, a white cloud-puppy and care for those around her."
            "She had everything, except she wasn't Slavya."
            scene cg d4_sl_lookup2_7dl with flash
            "And Slavya - there she is..."
            "And she..."
            "I refused to say the word out loud, it cut my gums, and the bitter blood trickled into the icy abyss."
            "I felt no more."
            "And I didn't live..."
            scene bg int_aidpost_night with dissolve
            me "Together..."
            "My head was in total disarray, and it hurt more and more."
            "There were those three days! There were!"
            "I remember them for sure, I remember every moment of them!"
            me "But who were they with..."
            "Pitifully I squeezed out, looking at the serene face of the erased one."
            me "What am I supposed to do now...?"
            "And that Slavya clung to me so frantically, desperately."
            me "It was as if she had a premonition that she would open her eyes very soon... {w}and I would not be there."
            me "But me, what am I supposed to do?"
            th "What am I supposed to do? Live and work and wait for you to come... {w}Sem, there's something wrong with your eyes. No, it's all right, it's just rain."
            me "Do I have the moral right to leave you here in this condition?"
            me "Even if you never remember me."
            dreamgirl "Still, how much easier it would be if Porridge killed the physical body."
            th "Shut up!"
            dreamgirl "I mean it! {w}You idiot, praying to a golden calf here who only has a body in common with your goddess, while she's out there choking on her tears."
            dreamgirl "There, you idiot. She's there. Alive. Real. Loving."
            dreamgirl "Not this piece of cadaver."
            "I twisted with hatred and rushed to the drawers of drugs."
            "I needed one drug that was guaranteed to kill the scum in my head."
            "Starting with the letter A…"
            "I didn't understand what happened."
            "Because for a moment my eyes went black, and a neon sign flashed in my head that the inner voice had gotten its way."
            "I didn't even have time to curse."
            stop music fadeout 5
            pause(5)
            scene black with fade
            "And I have arrived."
            $ prolog_time()
            play music "<to 52.94>" + music_7dl["herc_death"] fadein 3
            pause(1)
            if herc:
                scene bg int_store_7dl with flash
                "And I slowed to a half-step, feeling the protesting aching of the ligaments and muscles already engaged in an effective elimination program."
                "I was reaching, I'd manage to put the freak with the gun out of action."
                "I've been trained for that, dammit!"
                "And I could even get out of the line of fire - reflexes, after all."
                "I faltered, and the freak managed to turn in my direction."
                play sound sfx_7dl["makarych"]
                scene believe_in_pain with flash_red
                "A problem with no solution, the motives of a boring song."
            elif loki:
                show blink
                pause(1.5)
                scene bg ext_winterpark_7dl with dissolve
                pause(1.5)
                play ambience ambience_cold_wind_loop fadein 3
                "Hell if I know why I wasted five years taking jiu-jitsu classes if the first punch to the face makes me want to swing my limbs stupidly."
                "I had to humble my reflexes."
                "Intercepting the nerve knots in his arm, grabbing my chest - kicking with a dusting in the knee - intercepting the arm under his arm and, squatting down, twisting the limb."
                me "Down..."
                "I growled, spitting blood."
                me "And on myself!"
                "Something crunched nauseatingly under my arm, and the bull howled, not knowing how to intercept the unnaturally hanging limb."
                "This forced the company down a bit, and I diligently left one of them between me and the remaining trio, getting punched in the face and punched back."
                "But those few seconds while they were in a stupor..."
                "Funny attitude - the willingness to trample as a mob into the asphalt, to death, but the childish confusion when the victim shows his fangs and the willingness to kill back."
                "I could have turned and run."
                "I'd have enough time - all the blows so far have been to the face, so..."
                "Instead, I turned to the nearest one and soulfully slammed my forehead into the bridge of his nose, knocking him to the ground."
                "An ultrasonic bomb exploded and rumbled in the back of my head."
                scene cg d7_sl_gonna_be_ok_7dl
                show ldb_blind
                show blackout_exh
                show prologue_dream
                with fade
                pause(1)
                stop ambience fadeout 3
                "After that I felt nothing."
                "Instead of the blows coming at me, I saw a warm summer night and a semi-circular gate with a five-pointed star at the junction of the flaps."
                play ambience ambience_camp_center_night fadein 3
            else:
                play sound sfx_water_emerge fadein 0
                "I've been to ice hell."
                "The same one reserved for talkers and spoiler enthusiasts."
                "The difference was that I was still alive."
                "Still."
                "In infants, on a reflexive level, the membrane shrinks their nostrils and ears when they get into the water."
                "This mechanism stays with humans until old age - but in a much more rudimentary form."
                "It's harder to fight it, though."
                "It took me an infinite sixty seconds before I overcame the raging desire to live and relaxed my larynx."
                "Black death rushed into my lungs."
            stop music fadeout 3
            menu:
                "I dreamt of Slavya…":
                    $ alt_day6_sl_cl_int = 4
                "I still have debts":
                    pass
    stop ambience fadeout 6
    with fade
    return

label alt_day7_sl_cl_int_true:
    play music music_7dl["shape_of_my_heart"] fadein 3
    scene stars with dissolve2
    "Well? Same people, same place?"
    "The story began in rhyme, in outlandish verse, putting loneliness, happiness, and unwillingness to give up in one line."
    "An unwillingness to be alone."
    "{i}And roll - a bottle on the freeway. Stunned, plastic, simple.{/i}"
    "So I rolled... I wonder - what would have worked out for us - with that Slavya."
    "With... I don't even know how to say it. The real one?"
    "Quiet tears-praying for time, a hand clenched to the point of pain-and boundless hope, faith. {w}That it will all work out."
    "Who has the tongue to call the blue-eyed happiness that fell asleep on my shoulder fake?"
    "We were together - just at one of the crossroads of destiny, her soul, her essence, left with me."
    "And the body - physical shell remained in place."
    $ renpy.show("bg ext_road_night", what = D3_intro("bg ext_road_night"))
    with dissolve
    "{i}We sat there for an hour, and then we left without looking, no «please stay» or «hold up».{/i}"
    "A stupid story with incomprehensible buzzers, special services, worlds, and other nonsense where only the happy laughter of lovers is appropriate."
    "You know?"
    "Not the tears in «Volga» rushing at roughly 200km/h, not the prayers to all the powers that be that this tiny life does not fade away."
    "Not the pain under my heart that allows me to open my eyes to another's universe with the understanding of {b}who{/b} is no longer there."
    "But the warmth of the palm, the sparkle of the eyes and «happily ever after»."
    scene stars
    $ renpy.show("bg semen_room_window", what = D3_intro("bg semen_room_window"))
    with dissolve
    "I'm confused and I'm scared."
    "I never understood anything about all these universes and metaverses and all that crap."
    "All I wanted was..."
    if loki:
        "To believe in people again."
    elif herc:
        "A little bit of justice and a little bit of truth."
    else:
        "Just to be left alone."
        "Or at least forgiven."
    "And a person I could breathe with."
    "And the only girl who could fulfill my wish the way I understand it - literally..."
    "She has ceased to be."
    "Light as she lived. Without fear, knowing she could not fix anything."
    "I remembered my dream - was it yesterday or did it happen millions of years ago?"
    "About the guy telling space about Assol, tired of waiting for a sail."
    "About how he always wished that one day a scarlet dot would shine on the horizon."
    "And about his wish coming true."
    "So... So it was the same for Slavya?"
    "Not instantly?"
    "Could it be such a fantastic thing that Slavya left me a message?"
    "If she really loved me enough to agree to make me the protagonist of her universe."
    "Maybe I'm demanding too much."
    "But it's really important for me to understand."
    "What was the will of the one who didn't even live to see our first kiss?"
    "Running after me, stepping on her own song, feeling me near."
    "Awakening and feeling a burning interest herself."
    "What did she want?"
    "What did she dream of?"
    "But how do you know that?"
    "And really... How?"
    "How do you know the will of the Universe, which without fools... loves? Literally."
    "How?"
    "My head is twisted with pain."
    th "I just have to..."
    "Ask."
    "A universe named Slavushka."
    me "So what was your last will while you were still human?"
    scene white with flash
    "And in the scalding icy whiteness melted:"
    "{i}I really want her to adore you.{/i}"
    scene stars
    $ renpy.show("cg d5_sl_bench_neutral_7dl", what = D3_intro("cg d5_sl_bench_neutral_7dl"))
    with dissolve
    "{i}So she would cherish and treasure you.{/i}"
    "The void responded."
    $ volume(0.3, 'music')
    scene cg d5_sl_bench_neutral_7dl with flash
    play sound sfx_7dl["nesmogla"] fadein 2
    voice "And remind me so I'd never come here... So that I'd never be able to."
    "A poem that I never read to her."
    $ volume(0.9, 'music')
    "A message in the language of memory."
    "The darkness of non-existence parted."
    "And I found myself where Sanich had so unceremoniously dragged me from."
    "On a bench in the corridor."
    me "So that I..."
    "With one lip I uttered into the blind ceiling."
    "It's already heavy-warm under my shoulder, and the beloved is curled up beside me, anxiously watching my dreams in anticipation."
    sl "What?"
    me "No... No. Nothing."
    "And with the last word, the last chord. The very last will."
    "With the finishing vale of a letter…"
    show alt_letter "Farewell." at truecenter with zoomin
    pause(3)
    scene cg d5_sl_bench_neutral_7dl with dissolve
    "And I blink often and often into the perforated panels of the soundproofing ceiling, trying not to burst into tears."
    me "Couldn't..."
    "For some reason I pronounce audibly."
    with flash_red
    th "Who couldn't, what couldn't?"
    th "After all, everything's okay, right?"
    th "Probably just worried about the condition - Slavya, the Pirate... Yes, and just."
    me "The lines came up from somewhere. I can't remember where from."
    "I answered, diligently hiding a hole in my memory that I don't know where it came from."
    "I guess I just had a really scary dream that I've already forgotten about."
    "Like those incomprehensible words..."
    play sound sfx_open_door_kick
    "The heavy door swung open, a yellow light poured in, someone yowled familiarly, and Slavya stirred beside me, waking up finally."
    "I stroked her shoulder and touched her hair with my lips."
    "There's still a whole month of summer ahead."
    "And there's no need to rush into adulthood at all."
    "I pushed into the background the image of the immovable, serene Slavya lying on the couch - I guess my imagination was running wild."
    "And stood up to meet the doctor."
    "A new day was dawning, and with it, new hopes!"
    scene anim prolog_2 with fade3
    "Int-True ending unlocked - «Everything's okay... Right?»"
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("sl_cl_int_true")
    show acm_logo_sl_cl_int_true with moveinright:
        pos (1600, 1020)
    pause(7.4)
    with vpunch
    call alt_7dl_titles
    return

label alt_day7_sl_cl_int_good:
    play ambience ambience_camp_entrance_night fadein 3
    scene bg ext_entrance_night_clear_7dl
    show prologue_dream
    with dissolve
    play sound_loop sfx_far_steps fadein 1
    play music music_7dl["your_life"] fadein 2
    "And that very moment, somehow very, very familiar, smelling of heated rusted iron and darkness and salt, enveloped me."
    "The moment we long for all our lives to smile and greet an old friend."
    "The pain was gone. Fear, too."
    "And in the silence, the thumping of bare feet on the pavement could be heard in the distance."
    "And cat ears peeked out from under the mop of thick brown hair."
    scene bg ext_entrance_night_clear_7dl
    show uvao_d1 at left
    show prologue_dream
    with dspr
    $ meet('uv', "Catgirl")
    uv "Decided to go after all?"
    "She smiled."
    me "Bring me to Slavya."
    "I asked."
    "The girl smiled and, taking me under her elbow, sternly ordered:"
    uv "Walk with me strictly step by step."
    me "Does it matter?"
    uv "Very much!"
    me "Is something going to go wrong if I don't go step to step with you?"
    uv "Of course!"
    "She opened her eyes."
    uv "I'll get upset and attack you and bite you. Scared? That's right!"
    uv "Let's go."
    scene bg ext_entrance_night_clear_7dl at zenterleft
    show uv normal at cleft
    with dissolve
    uv "Listen, why aren't you surprised, why aren't you asking who I am and where I'm from?"
    me "Why?"
    show uv upset with dspr
    uv "You fool! I'm a girl! I want attention and stuff!"
    me "You're not a girl, pretender."
    show uv surprise with dspr
    uv "I'm not? Then what am I?"
    me "You're a spirit guide. {w}However, I don't argue, you have everything as a girl, even... ahem... You get the idea, in short."
    show uv upset with dspr
    uv "Everybody's so smart now!"
    "She resented."
    uv "Where's poor Charon supposed to go now?"
    me "Stay where you are. You're the most charming Charon in all the universes."
    show uv smile with dspr
    uv "Really?"
    me "Bet!"
    show uv normal with dspr
    uv "I'll take your word for it!"
    scene bg ext_entrance_night_clear_7dl with flash
    with vpunch
    uv "Well, so long!"
    "She wagged her finger at me, kissed me on the cheek, and turning me around, guidingly kicked me in the ass."
    stop sound_loop fadeout 6
    scene bg ext_entrance_night_clear_7dl with flash
    pause(1)
    scene bg ext_camp_entrance_sunset_7dl with flash
    pause(1)
    scene bg ext_camp_entrance_day with flash
    $ persistent.sprite_time = "day"
    $ day_time()
    "And I didn't have time to understand anything."
    sl "Hi. What are you doing here?"
    "Smiled charmingly at my personal sunshine, my object of prayers and sighs."
    "And I, smiling, raised my head."
    show sl normal pioneer with dspr
    me "Has the bus been here long?"
    "In tone I answered her."
    me "You know, I thought you might be worried about where I was."
    show sl serious pioneer with dspr
    sl "That's what we're worried about!"
    me "And you'd send someone to meet me. {w}And I'll make friends with that someone."
    me "You know how great it is when you can be friends with someone out of nowhere."
    show sl smile pioneer with dspr
    "Slavya smiled, confirming that yes - indeed, not bad."
    me "And you took it and sent the most charming one."
    me "So I'll hold off on the friendship, I guess."
    show sl normal pioneer with dspr
    "Here the girl's smile faded somewhat - although I was saying predictable platitudes."
    show sl surprise pioneer with dspr
    sl "You don't want to be friends with me?!"
    "She asked back."
    "I could understand her - such opposition right off the bat!"
    me "I guess I'll fall in love right away. You don't mind me falling in love with you?"
    "I asked, and she laughed:"
    show sl laugh pioneer with dspr
    sl "Ha! That sounds so crazy, it might work."
    sl "I'm Slavyana. But you call me Slavya, everyone calls me that."
    show sl happy pioneer with dspr
    me "Alright. You can call me «honey» then."
    sl "Is that what it says in your passport, too?"
    me "Okay, we're not close enough to know each other yet for me to let you in my passport!"
    show sl normal pioneer with dspr
    sl "Okay... honey."
    "Laughing it off, Slavya said."
    sl "Do you want me to show you how to get to the counselor, or do you already know everything?"
    me "Can I go and give Pirate a squeeze instead?"
    "I winked."
    scene anim prolog_2 with fade3
    "Int-Good ending unlocked - «Call Me «Honey»"
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("sl_cl_int_good")
    show acm_logo_sl_cl_int_good with moveinright:
        pos (1600, 1020)
    pause(7.4)
    with vpunch
    call alt_7dl_titles
    return

label alt_day7_sl_cl_int_bad:
    scene black with dissolve
    play music music_list["you_lost_me"] fadein 3
    "The girl smiled guiltily at me, and nodded, causing the blond cap of hair to come into motion."
    "Was it just me, or did she have two cat ears peeking out from under her hair?"
    scene anim intro_13
    th "Another neko-crazed. It's a good thing I didn't keep talking to her."
    "Wasting no time even to maintain a semblance of civility, I left there."
    "I have enough to do."
    "I have to cross to the other side of the avenue, get a pack of cigarettes from the stall, inhale the sweet bitterness, remembering again that smoking in the cold is the first way to catch a lung cold."
    "There's a way home waiting for me."
    "Somewhere where there are no complications and people don't hurt each other."
    "To a faceless online existence."
    scene anim prolog_2 with fade3
    "Int-Bad ending unlocked - «Price of loneliness»"
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("sl_cl_int_bad")
    show acm_logo_sl_cl_int_bad with moveinright:
        pos (1600, 1020)
    pause(7.4)
    with vpunch
    call alt_7dl_titles
    pause(2)
    return

label alt_day7_sl_cl_int_rej:
    play music music_7dl["laugh_throught_the_universe"] fadein 3
    scene bg int_hospital_corridor_7dl
    with dissolve
    "Where is the evidence that man is not a miserable pile of secrets?"
    "Where is the evidence that man is more than the memory of bystanders?"
    play sound sfx_open_door_1
    scene bg int_hospital_hall_day_7dl
    with dissolve
    "The windows of the room looked out toward Japan, where a girl once came to visit us who thought the world was a better place than we thought it was."
    "And she confessed to us in confidence that her «better» first and foremost means lack of people as a whole."
    with fade
    "So I look, squinting at the rising sun and believing her words."
    "I believe that sometimes it really is better without the man."
    "Even if you can't do without one."
    "Nothing, but better."
    "Paradox, isn't it?"
    "A paradox, framed in the gold of the rising sun, in which I live."
    with fade
    "My backpack still hid matches, salt, a Swiss knife, and fishing line with hooks and sinkers."
    "Just go out into the woods, break out a stick, and you don't need anyone's company for a few days."
    "Which I sometimes do."
    "I can't see them. {w}I don't want to."
    scene bg int_aidpost_day
    show prologue_dream
    with dissolve
    "I didn't know how to look into their eyes, I didn't know how to answer in case something happened to people who would ask unpleasant questions."
    "How could I not keep her safe?"
    "Everything I knew, everything I remembered..."
    "It would seem, what's the problem, turn around and look, what's the problem?"
    "But it's not that, it's not all that."
    scene bg ext_hospital2_away_day_7dl
    show prologue_dream
    with dissolve
    "I can barely remember her anymore, only certain features remain - her eyes, the curve of her lips."
    "The shoulder with the strap of the dress cut into it."
    "Freckled..."
    "She's not perfect, she has a snub nose and a slightly too wide smile."
    "And the same ubiquitous freckles on her cheeks."
    "But it seemed so meaningful and appealing to me."
    "It only took a year to realize it wasn't love that was blind, no."
    "On the contrary, it's the ability to see a person as beautiful as they look, the ability to see the best in them, even if that is deeply hidden."
    "The higher vision of a loving person."
    scene bg ext_hospital2_away_night_7dl
    show prologue_dream
    with dissolve
    "It's all in the past."
    "In the past!"
    scene bg int_aidpost_day
    show prologue_dream
    with dissolve
    "In the past is the way my inner voice suggested I fly away somewhere far away where none of this would happen."
    "But it's akin to cowardly hiding your head in the sand."
    "It's running away from problems."
    "So I took a breath in my chest and relaxed, tried to calm down."
    "Told myself that I was more needed here now, and there were already people who couldn't do without me."
    "Even if they were better off without me."
    scene bg ext_road_day
    show prologue_dream
    with dissolve
    "After all, I'm the survivor now."
    "Me, not him, that old Semyon Persunov."
    "Something inside us died, and now there's only me left."
    "The other question is, will Slavya accept me like this now? Will she?"
    "Slavya... Someone like her would never accept someone else's sacrifice on this scale."
    "She would simply forbid it, and fling herself headlong into obscurity."
    "That other one."
    "And this one?"
    "I only wish I could hope she would be my friend."
    "At least."
    "A friend is someone who understands me."
    "Someone you can talk to about anything, and even if you fight, you're still on the same page."
    "Except I haven't been able to find anyone like that until now."
    "I've always stood out, always been too useless to others."
    scene bg ext_square_day
    show prologue_dream
    with dissolve
    "I was always missing something in the world around me, in the movies I watched, the literature I read."
    "Exactly until I realized, slouching with the weight on my arms: if you want to have a friend, if you want to read something, if you want to see something..."
    "You're going to have to do everything yourself."
    "The best unwritten stories that your subconscious whispers before you go to sleep - you'll have to put them all on paper yourself."
    "There's no other way."
    scene bg ext_townscape_ph_day_7dl
    show prologue_dream
    with dissolve
    "What could I write about?"
    "That's right, only what I'd like to read myself."
    "What's close to me."
    "What worries me, bothers me, angers me..."
    "Scares me."
    "As it turns out, I, a loner man, misanthrope and marginalized, until this moment had refused to admit to myself one of my cornerstone fears."
    "I was terrified of losing my loved ones!"
    "Yes! I, who never call anyone «loved», am scared of losing someone like that if he comes into my life."
    "Or rather, her."
    "I'm very afraid of losing her."
    scene black
    show laptop_7dl
    show prologue_dream
    with dissolve
    "Consciously conjuring up a picture in my head of sitting at home, working at my computer, listening to music and drinking."
    "Alone."
    "And I can picture it!"
    "I can picture «loneliness»."
    "But I can't picture being «without her»."
    "As it turns out, it's a hell of a lot different."
    scene cg d5_sl_bed_7dl
    show prologue_dream
    with dissolve
    "The last one sounds like the icy glistening edge of a guillotine blade frozen in a moment's fall, hurtling toward my neck."
    "Cold and stuffy and impossible to believe that such a thing is even possible."
    with fade
    "I don't believe it, it just can't be!"

    stop music fadeout 3
    "Isn't that right?"
    scene bg int_ward_day_7dl with fade
    play music music_7dl["sky_feather"] fadein 3
    "An uncomfortable look out the window, a stuffy nasopharynx."
    "Yesterday the saws were screeching there, and now all that's left of the sprawling crowns is a frequent ridge of almost naked trunks sticking up into the sky."
    "It's only too late."
    "The poplars are in bloom."
    "Apparently, the attitude of utility workers toward their duties is the same in all worlds."
    $ set_mode_nvl()
    "It's been a tough, harsh year."
    "Even apart from the disappearance of my inner voice and the completely painless border crossing."
    "Apparently, the more indifferent you are to what's going on, the more willing you are to be left here."
    "I wasn't afraid to go back to where I came from."
    "The worst of my life had already happened."
    nvl clear
    "So, by the laws of logic, it's only going to get better from here?"
    "I don't know."
    "To the people who said they were my parents, I told them I was staying here at the local social rehabilitation center and I wasn't going anywhere."
    "I have to, have to be there for her! Do you hear me, you?"
    "Of course, a bit of a different career than one would predict for the only son of diplomats, but..."
    nvl clear
    "This year I lived as if in a fog, under the tutelage of Olga Dmitrievna. And in September, I entered the «medical» for evening classes in the specialty «psyche corrector»."
    "I haven't heard of any such specialty in my home world, but I haven't heard of many things..."
    "More importantly, I managed to get a job as an orderly in the center where Slavya was."
    "It was hard to get through, but I had a really strong motivation."
    "Extremely strong."
    nvl clear
    "In fact, so much so that the supervisor, impressed by my performance, wasn't even lazy and pushed a few buttons to facilitate my admission."
    "Or was it Violetta Cernovna reading the pathology course?"
    "They were all here, all around me."
    "And only their help and participation helped me through this whole nightmare."
    "Even Olga Dmitrievna, officially appointed my guardian until I turned eighteen."
    $ set_mode_adv()

    stop music fadeout 3
    with fade
    "I was awakened from my musings by the noise of footsteps outside the door, and a whole procession piled into the room."
    play music music_7dl["unfinished_life"] fadein 5
    "Ahead of her walked an angry, power-hungry woman, fat and flabby, who identified herself as an official of the local registry office. And behind her were several people with suspiciously familiar facial features."
    "And, of course, the department head."
    "I shifted my gaze to the bed and gasped."
    "The corrective screen had been pushed away from her face for reasons of sleep, and all doubts fell away on their own."
    "The members of the Feoktistov family were indeed gathered in the room."
    "The woman cleared her throat noisily and mumbled:"
    voice "On the basis of the Third Amendment to the Civil Code of the USSR of July 11, 1929 «About people who lost their identity», as well as by the will of Feoktistova Maria and Feoktistov Pyotr, a secondary birth certificate was issued in the name of Feoktistova Tatiana, born July 23, 1989."
    "At this point she interrupted and clarified:"
    voice "Are you sure you don't want to keep the name? It's beautiful..."
    voice "No."
    "Said the one who most suited the role of father."
    voice "We already talked to the psychologist, he let us know that Slavya is gone, that it's not her."
    voice "Well, we'll raise her as Slavushka's little sister."
    "The man's voice trembled on the last word."
    "They will raise..."
    voice "In that case, I declare..."
    "I didn't believe my ears."
    me "What? No! How can you!"
    me "What Tanya, you what?!"
    "I tried to snatch the beautiful crested paper, but the official yanked her hand away with astonishment."
    "Everyone around me murmured and murmured, and several stares crossed over me at once."
    me "You can't do that."
    "That's all I could say."
    me "It's Slavya."
    "Only my opinion didn't matter in that room."
    "And later, the head of the department, saying something softly, kicked me out the door."
    "The lock clicked, and I was alone."
    "But not without her."
    voice "Excuse me."
    "I heard a muffled voice."
    voice "He hasn't been himself since..."
    scene bg ext_hospital2_away_day_7dl
    with dissolve
    "I didn't eavesdrop, I was above it."
    "Above them all."
    "I was the only one who knew that nothing would happen to Slavya, that one day everything would be."
    "It will!"
    "I went out into the courtyard of the building and, smoking, I covered my eyes."
    me "Sweet Slavushka."
    "I reported to heaven."
    me "Of all the words you can never say, I heard every one."
    voice "Every, every..."
    "Squeaked out behind me."
    voice "Get out of here, you bastard."
    voice "Scaring my visitors, you..."
    scene bg int_hospital_corridor_7dl
    with dissolve
    stop music fadeout 3
    "I dodged the rag that flashed in the air with a forced smile, picked up the mop and bucket - there was still a whole day ahead of me."
    "A whole..."

    with fade
    play music music_7dl["so_be_it"] fadein 5
    "I'm not giving up, do you hear me? As long as I benefit at least one person, I'll grit my teeth and I won't stop."
    "I will try."
    "I will live."
    "I will do what I do."
    with fade
    "Just because I know that's what Slavya would have wanted, too."
    "No, of course she could never admit it to herself, but it would also warm her soul to think that there would be good deeds left behind."
    "Though my deeds so far are limited to turning the sick over so they don't get bedsores, taking care of the equipment, and cleaning the corridors..."
    "So be it! {w}Most of the time I go to one patient..."
    "I had to gut my phone to build it a charger, but it's necessary, it's important!"
    scene bg int_ward_sunset_7dl
    with fade
    "Sometimes I roll aside the ramp with the equipment and slip the pictures under Slavya's nose - where I am, where she is, all the girls..."
    "I'll do anything to make her - that one."
    "By the time I finish with my work, it is nine o'clock, the room was already empty, only her permanent mistress was left."
    "Yes, and there was a new piece of paper in the headboard."
    me "Secondary birth certificate, Feoktistova Tatiana, born July 23, 1989..."
    "Confused, I read."
    me "Idiots, what idiots you are!"
    "Is that stupid name going to help us, all those who love her, accept it?"
    "Are we supposed to accept it and stop believing?"
    "They see this world wrong."
    "And somehow I think Slavya can be brought back."
    "That's right, isn't it?"
    "I shouted and cursed in a whisper: Slavya was in an evening session, so the television set hovered again on an iron rest before my eyes, showing some pictures languidly reflected from motionless blue eyes."
    "I sat down next to it, trying not to disturb the wires and catheters, took Slavya by the palm of my hand."
    me "The main thing is to remember: it's not your fault... Slavya."
    "I reached over and corrected a curl that had fallen out of a strand."
    "It was golden."
    with fade
    "The sunset illuminated us: me, holding the girl's hand, her, looking at the TV screen..."
    "And the stupid paper: secondary birth certificate, Feoktistova Tatiana (crossed out) Slavya. 23.07.1989."
    "Happiness — comes from the word «part»."
    "And one day a part of me will catch up with me."
    "In the meantime, I have to wait."
    "Just wait."
    "We will be... happy."
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("sl_cl_int_rej")
    show acm_logo_sl_cl_int_rej with moveinright:
        pos (1600, 1020)
    pause(7.4)
    with vpunch
    call alt_7dl_titles
    return

label alt_day7_sl_cl_good_ussr:
    $ set_mode_nvl()
    scene black with fade3
    stop music fadeout 3
    pause(3)
    play music music_7dl["please_reprise"] fadein 3
    "Nothing in the world is given for nothing, for free."
    "Absolutely everything has to be paid for, even the illusion of maintaining the status quo."
    "It's the same here."
    "Perhaps if someone - let's not point fingers - hadn't blown the whole gambit, played his due game and removed himself from the board, everything would have been simpler, clearer and more predictable."
    "Man is a very dishonest creature."
    "But I found a loophole in the rules of the game and took advantage of it - in the world of computer game players, such people are called cheaters, liars, dishonest players who play with a marked deck."
    "And they beat them mercilessly."
    "That's what I got."
    if alt_day6_sl_cl_arc == 'sh':
        "And the camp did get shut down - the four-eyed man got his way."
        "Or rather, his family got their way, closed the story, which was the most terrible tragedy for them."
        "Although Viola could not be counted among the Trofimov family, she was still a student of Shurik's mother and later his psychiatrist."
        "And at thirty-eight, she's already walking around with gray temples."
    else:
        "And the camp really got closed."
    "Not far from the old camp site they deployed a military unit - where a year later I went to serve."
    nvl clear
    "But a year had to be lived first."
    "For starters, my «parents», people who were unlucky enough to be my family, according to the documents, died, not even three weeks after my return."
    "I moved to Leningrad, to an apartment that was registered to my parents."
    "And then Slavya came. {w}And she stayed."
    "There was one problem left to settle..."
    "The story with my parents was a loud, ugly one, but I was rarely ever interested in the squabbles; more important was the fact that I was orphaned at seventeen, and another week later the child welfare authorities called at my door."
    "This world turned out to be very strict about lost and orphaned children - but you could have guessed that from the story of that same Alisa, for example - her story Slavya told me when she thought I needed comforting."
    "Or did she consider it her duty to warn me of what might await me?"
    "I don't know."
    "Anyway, I didn't seek solace, but I took in the information and assimilated it. {w}Somehow it seemed very valuable to know as much as I could about the world where I was lucky enough to linger."
    "So I ran from them for almost a year, from their desire to either appoint me a guardian or place me in a reception center."
    "Successfully escaped: man is a creature as adaptable as a rat."
    "I never would have believed I would say this - but yes, fortunately, I had a subpoena, a competency physical, and an electronic warfare unit at military unit number {image=alt_KS_censor} waiting for me."
    "For some inexplicable reason, stationed fifty kilometers from my old camp."
    nvl clear
    "Slavya, on the other hand, went back to her old life - finishing her studies, getting ready, participating in social life, and moving with all her might toward her new dream."
    if (not herc) and (alt_day2_walk == 2):
        "Yes, yes, the same one that once voiced - to become a lifeguard."
    else:
        "Strange and incomprehensible to any other girl."
        "But so perfect for my Slavya."
    "Of course, not everything worked out for her - though she tried to move with only ten times the confidence."
    "She had to go back to the basics, try again, retake..."
    nvl clear
    "I was finishing my first year of service when she came to my unit - all groggy, upset..."
    "They cut the girl down, they cut her down on the technical part - even though she already knew more than she should have for an applicant."
    "Had she gone to party school, she would have entered without competition - with her record as an activist, an excellent student, an athlete..."
    "But she taught me not to give up, I taught her not to give up: we drew strength from each other when I wanted to howl from hazing, when she wanted to drop everything and take the path of least resistance."
    nvl clear
    "But there was always a little strength: either I would come to her on leave, or she would come to me on a date. Each time both guessed too well in time to be considered mere coincidence."
    "So the announcement of a hundred days before the order, I met the man already engaged."
    "And four months later we celebrated two events on the same day - our wedding and Slavya's admission to the State Security Academy."
    nvl clear
    "But without an education, with only the military under my belt, I was only needed in the roles of watchman or a loader - not something I wanted to do all my life."
    if loki:
        "Of course, at home I was a pretty good musician, and here I could have gotten in shape in six months to a year."
        "But it turned out that just sitting with an instrument was too silly and boring for me."
        "Having been infected by my irrepressible wife's urge to do good things, I decided to go back to teaching music - which required a certain amount of knowledge and papers."
    elif herc:
        "It wasn't that I was resolutely opposed to working as a security guard."
        "But I wanted to fit in with my young wife, and that meant a minimum of not wanting to take what was given, and a maximum of constantly growing and working on myself."
    else:
        "And the skills of a print media designer were of little use in the absence of computers with preinstalled «Photoshops», «Corels», «InDesigns»…"
    "Slavya had a scholarship, her parents helped out in some places, and I felt like a dependent sitting on my young wife's neck."
    "One day I caught myself thinking that I wished I could rewind a couple of years and... {w}I should have kicked myself in the head."
    "Yes, man is a very insolent and very ungrateful creature."
    nvl clear
    "That same month I applied to Herzen."
    if loki:
        "To the Institute of Music, Theatre and Choreography."
        "Yes, yes. Music teacher."
    elif herc:
        "For the PE teacher."
        "To become the second Sanich."
    else:
        "To the fine arts department."
        "Perfectly aware of the lopsidedness of my own knowledge, I decided to move towards development."
    "And in July, when it became clear that I had passed the competition, I shared the news with Slavya."
    "She took the news strangely - holding her hands to her mouth and running to the bathroom."
    "I knew, of course, it wasn't the most inspiring news."
    "But to react like this... And I didn't even tell her I'd found a part-time job at a newspaper as the editor of a society column."
    "It was scary how Slavya might have reacted to such news."
    "Also, man is a very, very stupid creature."
    stop music fadeout 3
    scene black with fade
    pause(2)
    $ set_mode_adv()
    scene anim prolog_1
    play music music_7dl["rightroad"] fadein 3
    $ persistent.sprite_time = "day"
    $ day_time()
    voice "Semyon Semyonich?"
    "A brittle, youthful bass voice inquired unabashedly."
    th "Get lost…"
    dreamgirl "He likes you."
    th "Maybe if you ignore him, he'll go away?"
    voice "Semyon Semyonich!"
    "This time the owner of the voice got so cocky that he even touched me on the shoulder."
    "He's got a lot of nerve, huh!"
    me "Mmmmm…"
    th "Lions scare away annoying stickers with their growls and beastly muzzles. Grooowl..."
    voice "Wake up... Please."
    me "Get off me."
    "I brushed it off."
    "A door slammed behind me, footsteps sounded..."
    "Soft conversations, laughter..."
    play sound sfx_water_emerge
    pause(1)
    play sound2 sfx_bodyfall_1
    "And I barely had time to roll away when twenty gallons of standing, rusty water plunged onto the spot where I had just been lying!"
    me "SSSSSSSLAAAAAAAAAVYYYYYYYYAAAAAAAAA!"
    "I roared, opening my eyes."
    show unblink
    scene bg int_sporthall_day_7dl
    with vpunch
    show sl smile casual at cleft
    with dissolve
    "She stood there laughing, holding a conical fire bucket, and next to her stood a wimp who looked vaguely like someone."
    me "What are you doing, you little shit?"
    voice "But I'm not..."
    me "I'm not talking to you."
    "I brushed it off."
    sl "Woke up, Syomich?"
    "She smiled."
    me "Uh-huh. Who's going to dry the mats later?"
    show sl serious casual with dspr
    sl "You dry them yourself, you'll have less desire to sleep in the workplace."
    "She turned back to the pioneer:"
    sl "So what did you want to talk to Semyon abo-"
    "And then I jumped!"
    hide sl
    "Grabbed the nervously squeaky, noxious, petty girl in my arms, unsuccessfully pretending to be a grown-up madam."
    "Threw her into my arms and kissed her on the forehead deafeningly, with a pullback."
    voice "Mom?"
    "A girl of about five with long golden braids and gray eyes peeked into the hall."
    voice "Oh!"
    "She walked out of the hall, muttering: «They're kissing again, like they're little kids»."
    "And the skinny guy stood there looking at us with a complex mixture of envy and bewilderment."
    sl "Comrade gym teacher, put your spouse on the floor and sign the poor boy his checklist already."
    "Slavya said sternly."
    me "Yeah?"
    "I set her very carefully on the floor."
    "And I looked very carefully at the wimp - cheered up, he held out a lined sheet of paper to me."
    "And I grimaced and took it in my hands."
    me "The hell did you bring me?"
    "I shrugged."
    me "I'll sign it, and then what?"
    show sl smile casual with dissolve
    sl "Oh come on, you might as well play with your muscles, you dolt!"
    if not herc:
        "That's right, even though it wasn't exactly my line of work, I was the PE teacher here."
        "Maybe it was a kind of generational continuity, and I stepped in to replace Sanich."
        "Or maybe I just enjoyed that summer too much, when I thought I'd curse everything and never touch working with kids in my life."
        "Either way..."
    "With a sigh, I signed the sheet and with a nod I let him go."
    show sl normal casual with dspr
    sl "Good boy."
    me "Good boy, good boy."
    "After watching the door slam behind the pioneer, I hugged Slavya again and breathed into her ear:"
    me "Why don't we take the door off Dusya's room? Why does she walk around like she was born in a cave, without knocking?"
    sl "She's your daughter and has every right to your attention at any time of the day or night!"
    "Slavya scolded me."
    sl "And if you keep hugging me like that, she'll have a brother or sister before the deadline."
    me "Oh!"
    "I looked at her belly meaningfully."
    me "And when?"
    show sl normal casual with dspr
    sl "In about…"
    play sound sfx_unlock_door_campus
    "Comrade Camp Director, without turning to the door, blindly clicked the lock."
    sl "Nine months."
    sl "Plus-minus half an hour."
    "She giggled:"
    sl "Depending on how hard you try."
    scene anim prolog_2 with fade3
    "Good ending unlocked - «Plus-minus half an hour»"
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("sl_cl_good_ussr")
    show acm_logo_sl_cl_good_ussr with moveinright:
        pos (1600, 1020)
    pause(7.4)
    with vpunch
    call alt_7dl_titles
    pause(2)
    return

label alt_day7_sl_cl_good_rf:
    $ set_mode_adv()
    play music music_7dl["are_you_there"] fadein 3
    $ persistent.sprite_time = "day"
    $ prolog_time()
    scene bg int_coupe_day_7dl with flash
    play ambience sfx_7dl["train_depart"] fadein 3
    "Step. {w}Step."
    "I liked the movies about Danila Bagrov - there was something so strange about them, so saturated with inexistence and longing."
    "The joyless sound of them and the sound of their musical accompaniment were both."
    "But still, for some reason, when leaving the theater, humming the ringing in my teeth «Mother of Gods», I felt an evil vigor walking in my blood, and there was no way to resist it."
    "So I had to live: in some ways even quite well."
    "Not all the downsides of my old existence, on second thought, turned out to be so."
    "For example, the scenery - the cold granite embrace of the Northern Capital."
    "I owe them to the idiotic will of my parents."
    "How many times I've booed and branded them for - and now I love them."
    "And best of all, they go so well with this wicked, overcast but incredibly beautiful music..."
    "That's why I live."
    "Humming with my lips alone - like a silly, ugly fish - from admitting we'd been walking all day to demanding to be told where my angel had put his wings. {w}Which I liked."
    "And it was all so disgustingly monotonous and familiar and dystopian."
    "It was insulting just to have an invisible cameraman filming over my shoulder in the newfangled action-cam style to get all sorts of unflattering things in the frame."
    "Like writing poetry."
    "Or consuming absinthe."
    "Or writing poetry under absinthe - and in the morning it will hurt all over, not because the wormwood tincture is bad, but because three packs a night is too much after all."
    "And there's no getting out of here."
    "What's worse, I don't want to get out."
    "I'm cozy and warm, and this dusty swamp isn't the worst armor against life's troubles."
    "If only it weren't for the young dreamer who occasionally opens his eyes inside me with cruel curiosity."
    scene bg ext_winter_night_7dl
    with dissolve
    play ambience sfx_bus_interior_moving fadein 4
    "There was something about it, there was, in movies with paltry plots but the richest actors in charisma, and in rock music in the early nineties."
    "From the far side of the cabin came a chorus of 'may you die' as the last three pairs of seats whispered, celebrating someone's successful trip."
    "And I grimaced in passing - the headphones were already giving me a headache after three days of constant interaction with Mr. Durst and his admissions as to why he was doing anything at all."
    "And I'm a homebody."
    "A terrible homebody."
    "Who hasn't lasted five years in one place - that's a paradox."
    "It's 22:55, and through the clouds, the Polaris peeks out, and the icy asphalt lies under the wheels, and…"
    scene
    $ renpy.show("bg ext_winter_night_rotate_7dl", what = D3_intro("bg ext_winter_night_rotate_7dl"))
    dreamgirl "A warm place, but the streets are waiting for our footprints…"
    pause(1)
    scene bg ext_winter_night_7dl
    "On that note I yawned longingly."
    "And without ceasing, without letting go of that mood, {i}of the path{/i} - melancholical, lingering..."
    "Fell asleep."
    "Of course, it wasn't the four hundred and tenth, and I wasn't more afraid of falling through into some inscrutable world where the entrance fee..."
    "But there was something about it, sleeping on the road, as if you really put yourself on pause and let the world twist past you, stopping the right point right under your feet."
    "You just have to take a step."
    "Or at least want to."
    show blink
    scene black with fade
    "And that's probably the hardest part."
    "In order to want something, you have to overcome the eternal otono del Alma, to dive into the transparent bitterness of the yellowing maple leaves, where young Butusov, Kinchev, and Shevchuk hooliganize in Pushkin Park, spin a drum, and you yourself are even younger by a whole other disappointment."
    "And I can't have that."
    "I've got fifty megabits for four hundred rubles, a comfy, worn-out chair, and resources that end in 'C' and therefore sound rougher than they really are."
    "Draw-ach. Survive-ach. Chat-ach."
    stop music fadeout 3
    play ambience ambience_cold_wind_loop fadein 3
    scene bg ext_winterpark_7dl
    with dissolve
    "But perhaps one day, from the ajar door, one can hear a fragile voice diligently bringing out the melody of my soul as well?"
    with fade
    play music music_7dl["pixies_playing"] fadein 3
    "She was standing right where I expected her to be."
    "As if she had always been here."
    "She gave me a glimpse of her, an ice of longing and latent expectation, as if she'd never expected to see her again."
    with fade2
    "But it's her fault I've become this way, isn't it?"
    "She's the only reason that one day I stopped looking at icons and listened to the voice from behind the window."
    "Stopped doubting, stopped worrying, stopped throwing myself around in vain."
    "Perhaps I should have thought at least a little..."
    "But the strange image of a girl lying motionless on a hospital couch, outwardly indistinguishable from her, the feeling that I might not have time to do something, kept coming back to my mind."
    "That's what made me stop to think."
    scene bg ext_city_night_7dl
    with dissolve
    sl "Why did this happen?"
    "I shrugged silently."
    sl "But you..."
    me "I did, I did... {w}You're off today?"
    "Somehow it turned out on its own that she'd been toiling since sixteen, responsible since six..."
    "She laughed."
    sl "No. I said I was sick."
    me "You dumbass!"
    "Another burst of laughter was my answer."
    sl "Walking, then?"
    me "No."
    sl "But waaaalkiiiiiing!"
    "The girl bit her lip and gave me a furtive look, blinking often and often."
    "I didn't explain to her that I'd just gotten off the bus and, before that, the train, that I was tired and dirty and angry."
    "Instead, I just took her by the hand and dragged her along."
    scene black with fade
    "Since the first timid: «Hello, are you Semyon?» in Skype — went a week."
    "A whole week."
    "Just a week."
    me "No walking, I said."
    "And this Slavya was different from that stern, grown-up Slavya of the camp in the first place, in that she wanted to walk, she wanted shoes and she wanted stupidity."
    "I repent, fool, fool, repent - for some reason I thought her responsibility was a trait of an adult."
    sl "Oh, look! Skates! For twenty minutes only three hundred rubles! Let's go?"
    scene anim prolog_1
    with dissolve
    sl "Or let's go to a cafe."
    me "No cafes."
    sl "But you can't do that! {w}You ask me out and you won't even feed me?"
    me "It's easier to shoot them than to feed them."
    "I grumbled."
    sl "What?!"
    me "No, no, you heard it. {w}Bigger steps!"
    sl "Or let's go to the arcade! Look, the 'Not Boring' Garden!"
    "She clapped her hands in delight."
    sl "I won't forgive you if we don't go there!"
    me "What a waste..."
    "The girl pouted, the girl was going to pout."
    "But is that why I drove for three days?"
    me "Slavya. Okay."
    "I turned to her."
    me "Business first. Everything else later."
    sl "But..."
    "Without listening to her objections, I dragged her to the motor that was already waiting for us and, pushing the girl into the cabin and landing next to the driver, I commanded:"
    me "To the registry office!"
    stop music fadeout 3
    scene anim intro_2
    with dissolve
    play music music_7dl["happy_ending"] fadein 3
    "Slavya in the backseat squeaked and fell silent."
    "Perhaps if I'd gone around again in my usual spirit, this never would have happened."
    "But I'm tired, I'm scared, and in my right earpiece the immortal bard is predicting how summer will end, and it looks shaped idiocy against the icy asphalt."
    "And in the blood boils again what seemed to have faded, forever, irrevocably."
    scene anim intro_1
    with dissolve
    sl "But I didn't give consent..."
    "Slavya began to protest."
    "And I, not knowing any more doubts, turned around and put my fingers on her lips."
    me "After all, after what you did to me, you must marry me. {w}Go, chief, drive, I've got happiness backing up here!"
    "The driver laughed and added to his pace."
    "The streets blurred with speed, merging into indistinct, trembling tunnel walls with an end point in the reality I seemed to deserve, a gust of frosty wind leapt in my face from a loose-covered vent, and I thought:"
    th "Am I really trying to remember what doubt is?"
    scene anim prolog_2 with fade3
    "Good ending unlocked - «Plus-minus half an hour»"
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("sl_cl_good_rf")
    show acm_logo_sl_cl_good_rf with moveinright:
        pos (1600, 1020)
    pause(7.4)
    with vpunch
    call alt_7dl_titles
    pause(2)
    return

label alt_day7_sl_cl_rej_rf:
    scene bg intro_xx with dissolve
    play sound_loop sfx_intro_bus_engine_loop fadein 3
    play music music_7dl["so_cold"] fadein 3
    $ prolog_time()
    "I opened my eyes expectantly in my reality."
    "Expectedly on my bus."
    "That's not how we could have broken up, not at all..."
    "Why am I such an idiot, God?"
    "Why couldn't it have been normal? {w}For example..."
    scene bg ext_bus
    show sl normal pioneer
    show prologue_dream
    with dissolve
    sl "Will you give me your address?"
    "She looks into my eyes, searching the bottom of them for something important."
    sl "Let's write..."
    "I hesitated."
    me "Here's the thing... There's a problem with addresses. No address."
    sl "You know, we're moving too. {w}And there's a problem with the address too."
    show sl smile pioneer with dspr
    sl "How can we not lose each other? {w}Let's meet here? In a year's time."
    "At the same place."
    me "I like that idea, let's do it."
    "Same place."
    scene bg intro_xx
    with dissolve
    "What place?"
    "I'm sure on the territory of the former Union these «Owls», «Eagles» and other feathered undergrowths are plentiful."
    "But is there even one among them - the one I want?"
    scene black
    $ set_mode_nvl()
    "Dreams, the ultimate injustice of which is that you wake up from them."
    play sound_loop sfx_intro_bus_engine_loop fadein 3
    "You, permeated with warmth, hovering in weightlessness, fully aware of the meaning of the expression «the soul soars»."
    "And what used to make me angry, irritated, sad, and cry... {w}It's gone."
    "All that remains is a cozy warm darkness, like a down blanket, under which it is so easy and comfortable to cry."
    "And it doesn't matter at all what you pay for getting here."
    "It's just that one day you end up where you don't deserve to be - but always dreamed you would."
    "And it's all the more frustrating when moments of paradise quite logically expire."
    "However, for someone like me, it's an expected epilogue."
    nvl clear
    "The tic-tac-toe man has fulfilled his function and can be forgotten."
    "I never got to the bottom of what happened to me."
    "And as a man on whom nothing is evenly dependent, I must act according to my modus operandi - consistently and unhurriedly to weed this week out of my soul."
    "Tight wheat-colored braids, bottomless blue eyes glowing with a kindness this world doesn't deserve, the quintessential meaning of life for an individually stupid pioneer."
    "Slavya..."
    nvl clear
    "I remember every hour together, from the introduction at the gate, to the memory shot, and..."
    "All the things we pulled off together, all the fond memories that make my heart ache..."
    "She was the perfect friend, girlfriend, companion."
    "She was the first girl I ever had as a friend."
    nvl clear
    "It's been so ingrained in my soul from day one that the only way to rip it out now is with blood, with meat."
    "That's why I acted so ugly on the bus... Oh, why am I explaining my behavior in my dream?"
    "The further I go, the more it seems to me that I just combined in her person all the ideals I could name in a girl - kind, caring, understanding..."
    "It's like some kind of collective gestalt image that high school kids weep over after the show ends."
    "She didn't demand anything in return, didn't ask for help or support or praise. She was just being herself - the perfect girl who just can't exist in life."
    nvl clear
    "So... So I was just dreaming about her."
    "I just had a dream."
    "About the camp, the pioneers and their counselor, the warm summer night and sitting around the fire, about carefree children's games and simple human joys, about one moment lasting a week and an everlasting summer..."
    th "But why just a dream? I was there. I saw it!"
    "If reality is an electrical illusion of our receptors, then how can things around us be more real than a week lived at camp?"
    "Tears welled up in my eyes - not pain or longing, but gratitude and warm sadness."
    "For even if it had been a dream, it was the kind that makes life a little brighter."
    "The image of Slavya came alive in front of my eyes."
    "How I wish we had gone away together with her. Or that I had stayed by her side..."
    "Or at least come back with the squad leader."
    nvl clear
    scene bg int_bus_people_night
    "And if you think about it, the whole miracle seems to reek of Asimov's, Norton's, Simak's fairy tales - about a man of weak but miraculous fortune."
    "A loser in focus, dragged by the hair through the miracles, reshaping him in the most miraculous ways."
    "Too bad it's just a dream."
    "Sure, the changes are there, they're felt, they're tangible."
    "But nothing will do as well with them as a couple of weeks at the monitor."
    "And yet..."
    stop sound_loop
    stop ambience
    nvl clear
    stop music fadeout 3
    pause(2)
    play music music_7dl["silent_angel"] fadein 3
    scene bg int_coupe_night_7dl
    show anim_grain
    with dissolve
    "Some things are really better done than suffering a lifetime of obscurity."
    "Such things include visiting the graves of loved ones, for example."
    "Or here - a trip to the coordinates listed in the note."
    "Just to complete and close this story."
    "I purposely didn't look for the camp, purposely didn't try to go anywhere, to anything."
    "Because if it turned out that the people from my dream existed in my life - it would have been too bad."
    "I've been too afraid of going crazy my whole life for it to happen to me right now."
    "At least now I should be sane and sober."
    nvl clear
    "Geographically, the given coordinates were quite far from my Palmyra, I had to change trains and take a commuter train from one town to another."
    "I could hardly remember the road itself, didn't really understand what the funny, noisy, cheerful people around me were joking about, slipping me a full glass now and then."
    "So I breathed a sigh of relief when I got out at the halfway station, once drowned in greenery."
    "I don't like people. And they don't like me. And I don't like them. And they... Anyway, that's it."
    "On the occasion of winter, the half-station looked like living proof of an apocalypse already accomplished - a grim asphalt and concrete hulk surrounded by black fingers of branches sticking accusingly into the whitewashed sky."
    scene
    $ renpy.show("bg ext_road_winter_7dl", what = Notch("bg ext_road_winter_7dl"))
    show anim_grain
    with dissolve
    "It was very fortunate to catch the bus, very fortunate - it's running twice a day."
    "It wasn't until I sat down that I suddenly felt my moping recede - here, where they put a baby on my left knee and a basket of seeds on my right."
    nvl clear
    "The apathy was gone, gone, and in its place was interest and even excitement."
    "Or maybe it was my heart that was rushing forward."
    "Two kilometers on the surprisingly good asphalt of the road leading off the main highway, and my eyes were once again tingling suspiciously at the sight of the old, familiar power line towers."
    scene black
    "And when the buildings loomed on the horizon, and I could see the gate - semicircular, with a figured lattice and a five-pointed star carved on the joints of the flaps - I could not stand it, and, throwing my bag on the ground, ran to the lonely figure standing next to the gate."
    scene bg ext_entrance_winter_7dl
    show sl_trench
    with dissolve2
    "To a figure I would recognize among millions and millions."
    "Even with my eyes closed, feeling her weary faith, that one day..."
    nvl clear
    $ set_mode_adv ()
    me "Sla…"
    "I exhale, trying to calm the frantically pounding desire for a miracle inside."
    sl "Excuse me?"
    "She turns to me and with a familiar gesture brushes her bangs back from her forehead, squinting at the light hitting her eyes."
    scene bg ext_entrance_winter_7dl
    show sl_trench2
    with fade
    "In the eyes, in the figure, in the very expression of her face, only a doomed expectation and a weary faith."
    "And when she saw who called out to her, she just dropped to the ground and cried. I didn't even have time to pick her up."
    sl "Semushka."
    "She sobbed softly in the snow at my feet until I finally overcame my stupor and helped her up."
    sl "You came after all, my good man. {w}I believed, I always believed, that I just had to wait."
    with fade
    "She hugged me gustily."
    "And I can't say a word. Yes, of course it's her, my Slavya, but..."
    "Her young, firm skin was wrinkled, her mouth had mournful creases, and the corners of her kindly smiling eyes showed a lattice of blood vessels."
    "The hair, still lush, has lost its rich wheat color and is now more gray than gold."
    sl "I always said you should just come here to find me. {w}You promised, you..."
    me "And you..."
    "I swallowed."
    me "You - came here?!"
    sl "Every year."
    me "How many years have you been coming here?"
    sl "Almost thirty years, Semochka."
    "She sighed bitterly."
    sl "I am so old now, and you are still as I remember you, young and handsome. {w}Only a little older. {w}A little more indifferent."
    me "Indifferent?"
    me "No... I'm just surprised you waited after all."
    "I took her palms and kissed each one."
    me "And that you are not a dream after all."
    scene anim prolog_2 with fade3
    "Reject ending unlocked - «On the Very Same Place»"
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("sl_cl_rej_rf")
    show acm_logo_sl_cl_rej_rf with moveinright:
        pos (1600, 1020)
    pause(7.4)
    with vpunch
    call alt_7dl_titles
    pause(1)
    return

label alt_day7_sl_cl_rej:
    scene black with fade3
    stop music fadeout 3
    $ prolog_time()
    pause(1)
    scene bg ext_city_night_7dl with diam
    play sound_loop sfx_street_traffic_outside fadein 2
    play music music_7dl["tears_of"] fadein 3
    "Messengers who bring bad news are killed."
    "The sounds are gone."
    "All that's left is footsteps-the tinkling of the asphalt, the thudding of the ground, the creaking of the boardwalk."
    "There are no sounds. {w}The world is gone."
    "The girl didn't notice some tune playing in her headphones until an hour later."
    "When she turned the corner and almost got hit by a car."
    voice "Stupid, where are you going! Have you had enough to live for?!"
    "The gray-haired owner of a worn-out car waved his fist."
    "After apologizing, she ducked back into the driveway."
    "Thoughts were still there... There."
    scene anim intro_1
    with fade
    pause(3)
    scene anim intro_2
    with fade
    play sound sfx_intro_bus_stop_steps
    pause(3)
    scene anim intro_3
    with fade
    "Winter came early this year."
    "Already in October the temperature dropped to zero, and one day the girl opened her eyes, pulled down the curtains, and squinted in surprise at the whiteness of the snow that had fallen."
    "And there was no way the tenants wanted to do their chores, so it was always cold in the room."
    "Very cold - not even a Japanese blanket with blue tigers helped, so she had to go to bed with her clothes on."
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
    play sound sfx_intro_bus_stop_sigh
    with fade
    pause(3)
    "But the girl patiently endured the cold."
    "Didn't resent it - it wasn't in her position to do it."
    scene bg int_intro_liaz_7dl
    show prologue_dream
    with diam
    "After all, she's just a newcomer, a stranger who rents a room in a communal apartment, what's there to be outraged about or to swear at?"
    "Arriving from the heart of Russia, don't know why, don't know for whom."
    "In pursuit of a dream."
    scene bg int_home_lift_7dl
    show prologue_dream
    with diam
    "Silly, of course - it's just a dream, that's all."
    "That address, too..."
    scene bg int_access_day_7dl
    show prologue_dream
    with diam
    "She pressed the bell button for a long, long time, until a neighbor, a dandy grandmother in her seventies, looked out at the constant ringing of the bell."
    "Immediately she rushed in, almost forcibly led her to her house, made her throw off her thin coat, and took her to the kitchen, where the kettle was already rinsing."
    scene bg int_sam_house_clean_7dl
    show prologue_dream
    with diam
    "They got to talking..."
    "And the girl told Alevtina Sergeyevna her silly, foolish story."
    "About her stupid dream with a boy who wanted to be a better man."
    "About coincidences."
    "About how, exhausted, she packed her things and came to Petersburg, where, guided only by intuition and vague memories, she could hardly find the address."
    "And she didn't seem to want to, but at the end she cried."
    "Though not as much as she cried afterwards when she saw the note: «I don't want to be alone anymore»."
    voice "After New Year's Eve, Seyomushka became like a stranger - before he was a literal stranger, he would not say a kind word."
    voice "And now he's smiling all the time."
    voice "He's taking care of himself, and I thought he's getting wise."
    voice "He's found his sweetheart."
    $ alt_day7_sl_cl_lp_counter = max(lp_dv, lp_un, lp_mi, lp_us - 3)
    if alt_day7_sl_cl_lp_counter >= 3:
        if lp_dv == alt_day7_sl_cl_lp_counter:
            voice "One day she came to him - tall, slim, in a red coat - beautiful-beautiful."
            voice "She banged on the door with her fists, and when he opened it, she kissed him on the doorstep, let him get ready, and took him with her."
            voice "A week or so ago."
            sl "Alisa..."
        elif lp_un == alt_day7_sl_cl_lp_counter:
            voice "He went alone, and then one day he went out for a walk as usual - it was February, or something - and he came back with someone."
            voice "A girl like that, she'll look like a girl till she's fifty."
            voice "Eyes - ooh, huge, witchy. Gre-en-ish."
            voice "In early October they got married and left - probably on their honeymoon."
            sl "Lena..."
        elif lp_mi == alt_day7_sl_cl_lp_counter:
            voice "And he really did find one."
            voice "Last week, you know, a bus came by - a big, foreign bus, with cartoons on it."
            voice "Everybody ran to see it, and I have a window to the courtyard, so I saw a little cane girl come out of it."
            voice "My mother, she was so skinny, nothing to hold on to, but her hair was down to the ground."
            voice "She ran to the doorway, rang and rang, and when Syomushka opened..."
            voice "Eh, he should have found a normal girl like you."
            sl "Miku..."
        elif (lp_us - 3) == alt_day7_sl_cl_lp_counter:
            voice "And really - such beauty, it's better not to see it."
            "Grandma Alya said in her heart."
            voice "At night, at three o'clock, under the windows - she came in her car, not thinking about people at all!"
            voice "And she played music! On the guitar!"
            sl "Was it Alisa?"
            voice "Alisa or not Alisa, I was up half the night after that red-headed prankster..."
            voice "I kept humming 'Blow with the Fires'."
            voice "And at the end of September, the two of them went away somewhere."
            voice "They never came back."
            sl "Ulyana?"
    else:
        voice "Or rather, she found him."
        voice "Eh, guys didn't act like that back in my day."
        voice "You don't hear that - on the seventh floor on the fire escape, and she looks so serious and grown-up!"
        voice "And that's it - the apartment's empty now, Syomushka's moved in with her."
        sl "What did she look like?"
        voice "I said, she looked so grown-up, I didn't get a good look at her, only her hair was long and brown, and her voice was so commanding. How she shouted 'Semyoooooon'!"
        "Olga..."
    stop music fadeout 3
    "Exhaled the girl."
    voice "So you know her?"
    sl "Knew..."
    play music music_7dl["you_were_late"] fadein 3
    sl "I'll go. Okay?"
    voice "Where are you going to go at night, honey?"
    sl "I..."
    "Droplets on the cloth - shattered reveries, buried hopes, broken dreams."
    "And already with difficulty swallowing unsolicited sobs, turning away:"
    sl "I... I don't know."
    "Without listening to the grandmother's lamentations, she ran out into the hall and pulled on her fur coat and her old boots."
    "She ran down the stairs and at random found the intercom button."
    scene anim intro_1
    with fade
    "And, blinking rapidly, hiding her tears under an uncertain smile, she ran out into the cold and silence."
    "Into the icy frozen beauty of a city foreign to her."
    pause(3)
    scene anim intro_2
    with fade
    "How could it have occurred to her that there would be a miracle waiting for her at the other side of the world?"
    "A miracle does not tolerate inaction or neglect."
    "It will come true for someone else if you don't jump at its first call."
    "That's what a miracle is."
    pause(3)
    scene bg intro_xx
    with fade
    stop ambience fadeout 2
    play sound_loop sfx_bus_interior_moving fadein 4
    "Through the huge glass, through the novocaine blockade, the bright fizzing sparks of someone else's carefree life shot out, the tires of cars rustled, people rushed."
    "And looking at this life, indomitable, mighty, once so exciting, it moved its deadened lips, letting out a bitter question with cold steam:"
    sl "And was it worth it?"
    "And she didn't know the answer."
    "Who can tell you what's really better - to push away a miracle once and spend a lifetime bemoaning yourself for inaction, or to chase a dream and break your wings against the sky?"
    "Who can tell you when to heed the call of your heart and when to remain in blissful ignorance?"
    "Who deals with this question at all - does man have the right to dream?"
    stop sound_loop
    scene
    $ renpy.show("bg int_coupe_day_7dl", what = Desat("bg int_coupe_day_7dl"))
    show anim_grain
    with dissolve
    "People were living, passing her by, looking into a future that was undoubtedly bright."
    "And she missed her happiness and her life by blindly chasing a dream."
    "The train shuddered, the doors closed with a clang, the inertia pushed her toward the Moscow station, as if the city was finally embracing her."
    scene
    $ renpy.show("bg int_coupe_day_7dl", what = Sepia("bg int_coupe_day_7dl"))
    show anim_grain
    with fade
    play ambience sfx_7dl["train_depart"] fadein 3
    "And she sat in her platz, and with dead, sightless eyes she looked through the forks of track, the posts, the mile markers, the houses, the people, the people, the people..."
    "An unremarkable pretty girl with golden hair braided into two braids, with a dreamer's blue gaze, who had already had time to fade from the memory of the one she was in such a hurry to."
    "Weeping with unbearable pain in her heart, a girl in a cold second-class carriage, leaving a city foreign to her."
    scene anim prolog_2 with fade3
    "Reject ending unlocked - «Time to go home»"
    play sound sfx_7dl["aunl"]
    stop ambience fadeout 4
    $ sdl_persistent_inc("sl_cl_rej")
    show acm_logo_sl_cl_rej with moveinright:
        pos (1600, 1020)
    pause(7.4)
    with vpunch
    call alt_7dl_titles
    pause(1)
    return

label alt_day7_sl_cl_bad:
    scene black with fade3
    play music music_7dl["out_of_your_tier_2"]
    $ prolog_time()
    pause(1)
    scene bg ext_city_night_7dl with diam
    play sound_loop sfx_street_traffic_outside fadein 2
    "Loneliness is a state of mind."
    "Even if you seem to be a successful husband, father, and breadwinner, sometimes it hits you so hard you can't wash it away with absinthe."
    "I have my burned-out cynicism, my smoky voice, my yellowed fingers and my resistance to alcohol."
    "And I shake these regalia, sure that I can't go any lower."
    "Although in my interpretation it looks exactly the opposite - there's no reason to go higher, here's the ceiling - the kick I got for a few days under the southern sky was enough to throw off my stupor for a while and start acting."
    "True, a very wise girl taught me that it's never too late to put your hands down - but you may not have the strength to hunker down."
    play sound sfx_intro_bus_stop_steps
    pause(3)
    scene anim intro_4
    show blind2_1
    with fade
    "So the fall didn't break me, didn't spoil me."
    "Not broken, not spoiled by depression."
    "And when one day the dank October suddenly lit up with a familiar smile, I cast aside all doubt, broke through the wobbly crowd at the turns, and stood beside, hoarsely said: «Hello. I'm Semyon, and you?»."
    hide blind2_1
    show blind2_2
    with dissolve
    "And she is Stasia. Stanislava - identical, similar but not the same."
    "But I decided that if the name, if the smile and the light in the blue eyes - then that must be a sign! Huh?"
    hide blind2_2
    with dissolve
    "I quit smoking for her, became someone for her, grew up and got a little boring for her."
    scene anim intro_3
    show blind1_1
    with dissolve
    me "Two packs of «Diablo Nero», please."
    "I say to the saleswoman, as smiling as she was a week ago."
    "And it's positive enough for a woman to smile while dealing in death..."
    hide blind1_1
    show blind1_2
    with dissolve
    "After another seven months, we got married and moved in together."
    "And the attractive façade of the perfect girl was replaced by domesticity."
    "It's like I've been set the bar, I've reached it, I'm good. That's it."
    "By the time I realized she wasn't Slavya, it was too late."
    hide blind1_2
    "Who am I lying to, though?"
    "I figured it out a lot sooner, it's just that one really wants to be deceived."
    "After all, I still eat my sandwich sausage down - just because I was once told by a painted cat that it tasted better that way."
    scene bg bus_stop with diam
    "I've become something."
    "Not myself."
    "Here I am now - I-AM-NOT-ME, a chill cutting my fingers through my leather gloves, but it's warm under the solid sheepskin coat, and in my breast pocket there's a gift waiting in the rotation for one very independent mamselle."
    "But I have a life. It's not the best, but it's not the worst either - for a man without much ambition, it's very, very good in some ways."
    "Except that I never bought a car - for some reason my mind reacts strangely to every attempt to go to the salon for a means of transportation."
    "Before my eyes I see the ground-up body on the plastic hood, the pale face, the scarlet lips, the eyes where the pupils have clenched into a point in pain."
    scene cg epilogue_sl with dissolve
    "So my wife thinks I'm a weirdo, but my choice is public transportation."
    if dr:
        "Despite how this entire story began."
    "My bus runs quite often, but now, on New Year's Eve, the snow-covered streets make it a little difficult to get around."
    th "Now I wish I could plug my ears with music and mourn a little bit about what didn't come true."
    "With a vague wistfulness I thought, examining the well-built figure in the fur coat standing with her back to me."
    "I guess I could go up to meet her now - after all, the precedent has been set, it should be a little easier by now."
    "But it cuts me with a longing for the unfulfilled fairy tale, for the surrogate substitute, the bare plastic facade that turned out not to be Slavya, but..."
    "After all, I was right to think that our world was simply incapable of giving birth to such a miracle."
    "Rustling the tires, a burgundy Nissan pulled up to my left, leaving room for a possible bus."
    scene cg epilogue_sl_2 with dissolve2
    "The girl turned toward the headlights, and for a split second I saw her face."
    "She was smiling - a sick, forced smile."
    "To the man behind the wheel, similar to what I see every day in the mirror - faceless, characterless, colorless."
    "Identical - similar, but not the same."
    th "Is it..."
    voice "Hello, Slavya!"
    "I read his lips."
    scene bg bus_stop with diam
    "I followed the car with my eyes for a long, long time."
    "And then the whole time I drove to the bus stop where my daughter's kindergarten was located, I stared out the window."
    "There was only one thought that plagued me:"
    "Did we both miss?"
    scene anim prolog_2 with fade3
    "Bad ending unlocked - «Yours. Fake.»"
    play sound sfx_7dl["aunl"]
    $ sdl_persistent_inc("sl_cl_bad")
    show acm_logo_sl_cl_bad with moveinright:
        pos (1600, 1020)
    pause(7.4)
    with vpunch
    call alt_7dl_titles
    pause(2)
    return

label alt_day7_sl_cl_good_rf2:
    scene bg ext_city_night_7dl
    show prologue_dream
    with fade
    play music music_7dl["tears_of"] fadein 3
    play ambience ambience_cold_wind_loop fadein 3
    $ prolog_time()
    "The voice kept screwing in and out of my eardrums, and the pain never came."
    "I stared with astonished eyes at the flowing - fifteen meters vertically - liquid quicksilver, or maybe lead, beneath my feet, and thought that from that height it would probably do more harm to hit the water than anything else."
    "My head was empty and ringing again."
    "At some point the voice stopped threatening and for some reason moved on to exhortation."
    "Silly."
    "I'm warm, cozy, safe."
    "The fear that had flared in the far reaches of consciousness has decayed and disappeared."
    "I took cigarettes out of my coat pocket, lit a cigarette, took a deep puff - so much so that tears came to my eyes."
    "I quit a month ago."
    "When the doctors said I was depressed."
    "But I always carried a pack with myself for some reason."
    "I guess I knew why."
    "Knew, why."
    "Word for word, letter for letter, the last piece of the puzzle clicked sensibly in the back of my head, falling into place."
    "Fiction."
    "From the foretold death to the girl with the bluest eyes."
    "All the events, the conversations, the ease of communication and the actions completely unlike me all fit perfectly into this picture."
    "And now I understood everything."
    "There was never a tantrum at the gate, a timid attempt to get close and not get burned."
    "There was never my grudges all at the same gate, the escape from the camp director's office, the dancing, the falling, the exploring the mazes."
    "Krapivin's dream of being able to stop grief with just a glance."
    "It's just that at some point in my life I made the choice in favor of delirium, the fata morgana, and let it take over me completely."
    "Otherwise I couldn't stand it - and finished what I started six years ago, staring wistfully at the emptiness beneath my feet."
    "Slavya, my love for her, our growing mutual bond - all of it existed only in my inflamed imagination."
    "Either I must have fallen asleep somewhere, and sick of waking up, missed the moment when I walked from the embankment to the bridge..."
    "Either I'm still asleep."
    "I pinched myself, but it didn't help."
    "Pain has never been my ally - and the fact that it doesn't help now could just as easily mean that I am awake as that I am lying in the ICU, unable to move, to think, to live..."
    "At times reality would break through into my delirium - and then I would smell familiar smells, hear familiar sounds, music, feel the uncomfortable way the springs of a hospital bed with an adjustable headboard would crash into my back."
    "The man standing next to me in a mouse uniform asked me something several times already, then put his palm on my shoulder and squeezed my fingers painfully."
    "But it didn't matter."
    "The brain can convince itself of anything - that doesn't really exist."
    show dreamgirl_overlay
    with flash_pink
    "There's nothing."
    "I smiled, grinning in his face."
    "And laughed."
    "Of course. A dream."
    "But in order to wake up... What was it like in that spinning top movie?"
    "In order to wake up, you have to fall down."
    "When I was twelve years old, when I didn't know how to hold on to the water, I often had a dream where I was falling from a great height into the water."
    "And I woke up the moment I touched the surface of the water."
    "The movie was called «Inception» — and people there were falling into a bathtub filled with ice-cold water."
    $renpy.notify('Pyaterochka (5) is a Russian network of supermarkets')
    "And so, in principle, any elevation would do - even the twins, one near the Theater «Buff», another next to a yet another «Pyaterochka»."
    "Here, let's try it."
    "I spit the cigarette in the face of the fellow in uniform, and when he stepped back, stunned, I turned sharply and, throwing my legs over the railing, stood on the other side."
    "What separated me from the abyss was three inches of granite under my heels and the shout of a serviceman."
    th "Sorry, but there's going to be another jerk jumper on your lot today."
    "And I gotta go."
    "I threw my body forward."
    "Wake up."
    "Your arteries will plow long before it gets to you that you've picked up too much speed."
    "A slippery roof won't let you catch the edge."
    "It's no use clearing your stomach if there's potassium cyanide in the glass."
    "You may have time to understand and regret and repent."
    "The gray water rushed toward me at an ever increasing unthinkable speed."
    "And doubts and fear, spurred on by the instinct of self-preservation, reared their heads in the mind."
    "But it's too late to win back."
    "Too late."
    "And I met the bottomless darkness with wide-open eyes, not yet knowing whether death or awakening lurked in the abyss."
    with fade
    stop music fadeout 3
    scene bg intro_xx with flash
    me "Yes, it's Semyon."
    "I answered, more scared than death of waking up."
    me "I'm on the bus."
    me "On the same one you disappeared from for some reason!"
    me "How do I know where that bus is."
    dy "Next stop: Subway station «Lomonosovskaya»."
    "Speakers answered."
    me "Did you hear that? Get over there. I'll swear and fight and maybe even whine a little."
    "I unplugged the phone and looked at it disbelievingly."
    "December 28, 2018."
    stop ambience
    "Last received - unknown number."
    "Region - Tver region."
    th "Oh, my God."
    "I immediately poked the redial:"
    me "I'm sorry, I'm an idiot, calling from St. Petersburg, demanding I don't know what. Listen, I'll go to Moskovsky now, find out about the tickets, will you meet me if I come to you over the New Year vacations?"
    me "That's nice. I'll call you when I get there."
    dy "Subway station «Lomonosovskaya»!"
    "Exhaled the speakers and let me out into the New Year, into a new life."
    "Into a new hope."
    $ set_mode_nvl()
    scene black with dissolve
    play music music_7dl["uneven_me"] fadein 3
    "I don't know what I was counting on when I made my promises."
    "But for today, tomorrow, or the week ahead, there were decidedly no openings for the direction I wanted."
    "And the ones that were available cost so much money that I just didn't have enough cash."
    "So the first available train was the ninth of January."
    nvl clear
    "But Slavya taught me not to give up."
    "And I taught her to go crazy sometimes."
    "So..."
    "I had to run and talk, of course."
    "I learned more about transportation in those two days than I have in a lifetime."
    nvl clear
    "But the fact remains that on the thirty-first of the month a train departed from Ladoga Station in the St. Petersburg-Moscow direction, on board which was also your humble servant."
    "It was noisy, stuffy, crowded in the salon - but I didn't care."
    "Compared to what I had to endure in one particular canteen..."
    "And here... Heh, headphones in your ears, cover your eyes and, after catching a steady signal, plug in the ICQ."
    "We departed at two in the afternoon, stopped twice, but it seemed like an eternity to me."
    "It was the first time I'd ever gone that far."
    "First time getting out of town by myself."
    "So this trip was kind of meaningful to me."
    nvl clear
    "But everything comes to an end someday."
    "Everything someday..."
    "And here I am, shaking with fear and cold, waiting for who knows what, and it's New Year's Eve in three hours, and I should be celebrating..."
    "And I'm in a strange city among strangers, and I don't know how I'm going to get out of here if anything, I don't know what to do if anything, I don't know..."
    me "God, what an idiot I am..."
    "I muttered, aiming for the Comintern Street crossing - there seems to be one in every city."
    "But before I could even take a few steps - and I was caught by the sleeve."
    nvl clear
    scene cg epilogue_sl_2 with dissolve2
    "I flinched and looked up."
    sl "What's your hurry?"
    "Asked me a very pretty girl, smiling from under her hood."
    me "I... I'm here... It's..."
    "She was even prettier than the one I remembered."
    th "And how should I behave with her?!"
    sl "You can start by smiling and saying you're glad to see me."
    "She laughed and took me under her arm."
    sl "And then it's up to the circumstances."
    me "Ah… Yeah…"
    nvl clear
    sl "Come on!"
    "She pulled me with her."
    me "Where to?"
    sl "Home! It's New Year's Eve!"
    "Slavya laughed."
    sl "You'll never guess what I've got for you!"
    scene anim prolog_2 with fade3
    $ set_mode_adv()
    "Good RF ending unlocked - «Something right»"
    play sound sfx_7dl["aunl"]
    play music music_7dl["refuse_to_replay"] fadein 3
    $ sdl_persistent_inc("sl_cl_good_rf2")
    show acm_logo_sl_cl_good_rf2 with moveinright:
        pos (1600, 1020)
    pause(7.4)
    with vpunch
    call alt_7dl_titles
    pause(2)
    return
