# ================================================================================================
#                                            начало турнира
# ================================================================================================
label alt_day2_cards_tournament:
    play sound sfx_close_door_1
    scene bg int_dining_hall_day with fade
    play music music_list["i_want_to_play"] fadein 1
    play ambience ambience_medium_crowd_indoors_1 fadein 1
    "And the inside was all set!"
    "The tables were placed like the playoff table, the winner would move to the next table, the loser would just get up from his seat."
    "Everyone's mood was upbeat and festive."
    "I took a closer look, looking at the opponents and figuring out the odds."

    show sh normal pioneer far at right
    show us laugh2 pioneer far at left
    with dissolve
    "Shurik, like me, not quite sure what he was doing here, was sitting next to Ulyana."
    show sh serious pioneer far
    show us laugh pioneer far
    with dspr
    "The kid swayed impatiently in her chair and tried to get some information from Shurik about the upcoming game, to which he only frowned grudgingly and pretended that he was not with her at all."
    hide sh
    hide us
    with dissolve

    show sl normal pioneer far at right
    show mz normal glasses pioneer far at left
    with dissolve
    if ('library' in list_voyage_7dl):
        "The next table was occupied by the buzzkill from the library, confronted by Slavya."
    else:
        "The next table was occupied by the same Zhenya, with Slavya playing against her."
    "I, catching her gaze, smiled encouragingly:"
    me "Good luck."
    show sl smile pioneer far with dspr
    sl "Thank you."
    "She smiled back."
    hide sl
    hide mz
    with dissolve

    show dv smile pioneer2 far at left
    show mi normal pioneer far at right
    with dissolve
    "Alisa got Miku as her prey, and I felt sorry for the poor Japanese girl for a moment."
    "The way Alisa's eyes burned with excitement told me only one thing - that the predator was determined to win and nothing else!"
    if alt_day2_dv_ultim == 1:
        show dv laugh pioneer2 far with dspr
        pause(0.3)
        show dv smile pioneer2 far with dspr
        "Catching my gaze, Alisa winked, reminding me of the bet, and I nodded back."
    elif alt_day2_dv_ultim == 2:
        show dv sad pioneer2 far with dspr
        "When she met my eyes, for some reason she flinched and{nw}"
        hide dv with dissolve
        extend " immediately looked away."
        "The scene at the door seems to have made a lasting impression on her!"
    else:
        "She didn't even look at me."
    hide dv
    hide mi
    with dissolve

    show un normal pioneer far with dissolve
    "There was an empty seat across from Lena. It looks like I have to play with her."
    "The rest of the space was occupied by fans and spectators."
    show un smile pioneer with dspr
    me "Hello again."
    "I sank into the chair across from her."
    me "Looks like we're going up against each other."
    show un shy pioneer with dissolve
    un "Yes..."
    "The attention of the audience clearly made her feel out of place."
    me "So good luck to both of us."
    "For a second I suddenly felt like giving up the game to cheer up that sad girl a little. You have to do good deeds sometimes, don't you?"
    hide un with dissolve

    $ persistent.sprite_time = "day"
    $ day_time()
    with dissolve
# ------------------------------------------------------------- ADD загоняем БГ зала на нижний слой
    python:
        renpy.scene('underlay')
        renpy.show('bg int_dining_hall_day',layer='underlay')
        renpy.scene('master')
        renpy.transition(dissolve)
# ------------------------------------------------------------- /ADD
    show el smile pioneer at right with dissolve
    "Finished counting the cards, Electronik turned in our direction and turned to us with an unhealthy animation, even for him:"
    el "We have the cards, everyone is in place. Let the tournament begin!"
    show el normal pioneer with dspr
    me "Hold the horses, speedster."
    "I grumbled."
    me "What about the rules? Or are we playing Texas Hold'em?"
    show el surprise pioneer with dspr
    el "Oh, the rules. Right."
    show el normal pioneer with dspr
    "Electronik took the marker with which he had been drawing the game diagrams, and plunged into thought, biting the cap mechanically."
    show el serious pioneer with dspr
    el "So."
    "He pointed to the diagram."
# ------------------------------------------------------------- ADD Показываем схему турнира на фоне зала
    python:
        renpy.show('alt_tournament_bg',layer='underlay')
        renpy.transition(dissolve)
# ------------------------------------------------------------- /ADD
    el "This is the tournament scheme, and…"
    show dv angry pioneer2 at left
    show el normal pioneer at cright
    with dissolve
    dv "We're not dumb. We know the loser is out."
    "Alisa interrupted him."
    dv "About the rules of the game, come on."
    hide dv
    show el sad pioneer at center
    with dissolve
# ------------------------------------------------------------- ADD Убираем схему турнира
    python:
        renpy.hide('alt_tournament_bg',layer='underlay')
        renpy.transition(dissolve)
# ------------------------------------------------------------- /ADD
    el "Okay."
    "The embarrassed Electronik instantly picked up his usual pace."
    show el smile pioneer at center with dspr
    el "The basic rule is that the loser is eliminated. So no second chances, re-matchings, or anything else!"
    "He waved off the reaching hand of Ulyanka, and continued."
    el "Each round consists of two games, if even after them the players have a draw, the outcome will be decided by the third game. After that, the losers of the round are eliminated, and the next..."
    me "I'm begging you."
    "I couldn't take it."
    me "Enough about the playoff system! We all know how it works! Let's talk about the rules of the game!"
    el "I'm almost there."
    "Electronik's got it."
    el "Since the volunteers..."
    "He threw a glance in my direction and instantly corrected himself."
    el "There will be eight contestants, so there will be three rounds."
    show el laugh pioneer with dspr
    "Then the star in his forehead lit up, and he held up his index finger."
    el "The winner of the last round gets a huge prize!"
    show dv angry pioneer2 at left
    show el surprise pioneer at cright
    $ meet('we',"Semyon | Alisa")
    we "Tell us the rules already!" with vpunch
    $ meet('we',"Chorus")
    "We barked together with Alisa."
    el "I'm almost there. Why, really!"
    "He hid his confusion, pretending to clear his throat."
    hide dv
    show el normal pioneer at center
    with dissolve
    el "So, all the combinations are from poker, you have to collect a combination stronger than your opponent's. Two, three, four..."
    show us grin pioneer at cleft
    show el normal pioneer at cright
    with dissolve
    us "Five!"
    "Shouted Ulyana, apparently tired of being ignored."
    el "In case anyone isn't aware of the value of the combinations."
    "Electronik ignored her retort."
    hide us
    show el normal pioneer at center
    with dissolve
    el "You can see them on the table."
    "And he pointed to the other half of the paper sheet."
# ----------------------------------------------------------------------------------- ADD Показываем правила игры
    if persistent.altRulesRead_new:                            # если правила игры уже прочитаны
        menu:
            "Show combinations":
                jump alt_day2_poker_rules_reading
            "I know combinations, but wouldn't mind a hint":
                $ alt_hint_poker_contractual = True
                jump alt_day2_poker_rules_known
            "I know combinations, no hints required":
                $ alt_hint_poker_contractual = False
                jump alt_day2_poker_rules_known
    else:                                                       # если ещё правил не читали — читаем.
        jump alt_day2_poker_rules_reading

label alt_day2_poker_rules_reading:
    $ alt_hint_poker_contractual = True
    $ set_mode_nvl()
    "{size=35}{u}Possible card combinations in order of increasing value:{/u}{/size}{nw}"
    ""

    "- {b}High card{/b}: no combination,{nw}"
    if persistent.font_size == 'small':
        "for example: {b}{color=#FF6600}Т{image=suit_2ch_S} 10{image=suit_2ch_S}{color=#009833} 9{image=suit_utan_S} 5{image=suit_uvao_S} 4{image=suit_uvao_S}{/color}{color=#FF6600} 2{image=suit_ussr_S}{/color}{/color}{/b}."
    elif persistent.font_size == 'large':
        "for example: {b}{color=#FF6600}Т{image=suit_2ch_L} 10{image=suit_2ch_L}{color=#009833} 9{image=suit_utan_L} 5{image=suit_uvao_L} 4{image=suit_uvao_L}{/color}{color=#FF6600} 2{image=suit_ussr_L}{/color}{/color}{/b}."
    "The above combination is called «ace high»."
    "If the opponents each have a high card,{nw}"
    "the winner is determined by the highest card in hand."
    "If the players' high cards are equal, a draw is declared.{nw}"
    ""

    if persistent.font_size == 'small':
        "- {b}Pair{/b}: two of the same card: {b}{color=#FF6600}9{image=suit_ussr_S}{color=#009833} 9{image=suit_utan_S}{/color}{/b}."
    elif persistent.font_size == 'large':
        "- {b}Pair{/b}): two of the same card, example: {b}{color=#FF6600}9{image=suit_ussr_L}{color=#009833} 9{image=suit_utan_L}{/color}{/b}."
    "If two players have this combination, the one with the higher{nw}"
    "the value of the cards that make up the pair has the advantage. If the pairs are identical, a draw is declared.{nw}"
    ""

    pause(1)
    nvl clear

    if persistent.font_size == 'small':
        "- {b}Two pairs{/b}: two pairs, example: {b}{color=#009833}8{image=suit_uvao_S} 8{image=suit_utan_S} {color=#FF6600}4{image=suit_ussr_S} 4{image=suit_2ch_S}{/color}{/b}."
    elif persistent.font_size == 'large':
        "- {b}Two pairs{/b}: two pairs, example: {b}{color=#009833}8{image=suit_uvao_L} 8{image=suit_utan_L} {color=#FF6600}4{image=suit_ussr_L} 4{image=suit_2ch_L}{/color}{/b}."
    "If there are {b} three{/b} pairs in hand, the pair of cards of the lowest value does not count,{nw}"
    "{i}There are no «Three pair» combinations in the game{/i}."
    "When two players have two pairs in their hands, the senior pair is the one that,{nw}"
    "which includes the two highest-ranking cards."
    "In the case when the highest pairs of cards are identical, the seniority{nw}"
    "of the combination as a whole is determined by the lowest pair of cards."
    "The winner will be the player whose lowest pair consists of the highest cards.{nw}"
    "If both players have completely identical card combinations by value, a draw is declared.{nw}"
    ""

    "- {b}Three of a kind{/b}/Set/Triplet:{nw}"
    if persistent.font_size == 'small':
        "three cards of the same value, example: {b}{color=#009833}7{image=suit_uvao_S} 7{image=suit_utan_S} {color=#FF6600}7{image=suit_2ch_S}{/color}{/b}."
    elif persistent.font_size == 'large':
        "three cards of the same value, example: {b}{color=#009833}7{image=suit_uvao_L} 7{image=suit_utan_L} {color=#FF6600}7{image=suit_2ch_L}{/color}{/b}."
    "When two opponents simultaneously have triplets, the winner is{nw}"
    "the player who has a three of cards of higher value."
    "Identical threes, as well as pokers and full houses, cannot be in the game.{nw}"
    ""

    pause(1)
    nvl clear

    "- {b}Straight{/b}: five cards of any suit in order,{nw}"
    if persistent.font_size == 'small':
        "example: {b}{color=#FF6600}5{image=suit_2ch_S} 4{image=suit_ussr_S} {color=#009833}3{image=suit_utan_S} {color=#FF6600}2{image=suit_2ch_S} Т{image=suit_2ch_S}{/color}{/color}{/b}."
    elif persistent.font_size == 'large':
        "example: {b}{color=#FF6600}5{image=suit_2ch_L} 4{image=suit_ussr_L} {color=#009833}3{image=suit_utan_L} {color=#FF6600}2{image=suit_2ch_L} Т{image=suit_2ch_L}{/color}{/color}{/b}."
    "If there are {b}six{/b} cards in order, the lowest card does not participate in the combination.{nw}"
    "Ace can both start and end the combination."
    if persistent.font_size == 'small':
        "In the above example {b}{color=#FF6600}Т{image=suit_2ch_S}{/color}{/b} finishes the combination and is{nw}"
        "valued at 1, and {b}{color=#FF6600}5{image=suit_2ch_S}{/color}{/b} is considered the high card."
        "The above combination is the smallest straight; the biggest straight —{nw}"
        "is a straight from ace: {b}{color=#FF6600}Т{image=suit_ussr_S} {color=#009833}К{image=suit_uvao_S} {color=#FF6600}Д{image=suit_2ch_S} В{image=suit_2ch_S} 10{image=suit_ussr_S}{/color}{/color}{/b}."
    elif persistent.font_size == 'large':
        "In the above example {b}{color=#FF6600}Т{image=suit_2ch_L}{/color}{/b} finishes the combination and is{nw}"
        "valued at 1, and {b}{color=#FF6600}5{image=suit_2ch_L}{/color}{/b} is considered the high card."
        "The above combination is the smallest straight; the biggest straight —{nw}"
        "is a straight from ace: {b}{color=#FF6600}Т{image=suit_ussr_L} {color=#009833}К{image=suit_uvao_L} {color=#FF6600}Д{image=suit_2ch_L} В{image=suit_2ch_L} 10{image=suit_ussr_L}{/color}{/color}{/b}."
    "If two players have simultaneous strings, the winner is determined by the highest{nw}"
    "card in the combination; if the high cards are the same - a draw is declared.{nw}"
    ""

    if persistent.font_size == 'small':
        "- {b}Flush{/b}: five cards of the same suit, example: {b}{color=#009833}К{image=suit_utan_S} В{image=suit_utan_S} 8{image=suit_utan_S} 4{image=suit_utan_S} 3{image=suit_utan_S}{/b}.{nw}"
    elif persistent.font_size == 'large':
        "- {b}Flush{/b}: five cards of the same suit, example: {b}{color=#009833}К{image=suit_utan_L} В{image=suit_utan_L} 8{image=suit_utan_L} 4{image=suit_utan_L} 3{image=suit_utan_L}{/b}.{nw}"
    "Such a combination for evaluation is called «flush from king» — highest card in the combination."
    "The highest combination is with an ace.{nw}"
    "If there are {b}six{/b} cards of the same suit, the lowest card of the combination is ignored."
    "If both opponents have this combination in their hands, the advantage goes to,{nw}"
    "who has the highest card in the combination is higher in value."
    "If it turns out that the value of the high cards is the same, a draw is declared.{nw}"
    ""

    pause(1)
    nvl clear

    "- {b}Full house{/b}:{nw}"
    if persistent.font_size == 'small':
        "one triplet and one pair, example: {b}{color=#FF6600}10{image=suit_ussr_S} 10{image=suit_2ch_S} {color=#009833}10{image=suit_utan_S} 8{image=suit_uvao_S} {color=#FF6600}8{image=suit_ussr_S}{/color}{/color}{/b}{/b}."
    elif persistent.font_size == 'large':
        "one triplet and one pair, example: {b}{color=#FF6600}10{image=suit_ussr_L} 10{image=suit_2ch_L} {color=#009833}10{image=suit_utan_L} 8{image=suit_uvao_L} {color=#FF6600}8{image=suit_ussr_L}{/color}{/color}{/b}{/b}."
    "If there are two threes in hand, the three of the lowest ranking card counts as a pair of cards;{nw}"
    "{i}there is no combination of «Two triplets» in the game{/i}."
    "If the opponents have the following combinations in their hands at the same time,{nw}"
    "the better is the one in which the three cards are higher in value,"
    if persistent.font_size == 'small':
        "example: {b}{color=#009833}В{image=suit_uvao_S} {color=#FF6600}В{image=suit_2ch_S} В{image=suit_ussr_S} {color=#009833}9{image=suit_uvao_S} 9{image=suit_utan_S}{/color}{/color}{/b}{/b} bigger than {b}{color=#FF6600}7{image=suit_2ch_S} 7{image=suit_ussr_S} {color=#009833}7{image=suit_utan_S} Т{image=suit_uvao_S} {color=#FF6600}Т{image=suit_2ch_S}{/color}{/color}{/b}."
    elif persistent.font_size == 'large':
        "example: {b}{color=#009833}В{image=suit_uvao_L} {color=#FF6600}В{image=suit_2ch_L} В{image=suit_ussr_L} {color=#009833}9{image=suit_uvao_L} 9{image=suit_utan_L}{/color}{/color}{/b}{/b} bigger than {b}{color=#FF6600}7{image=suit_2ch_L} 7{image=suit_ussr_L} {color=#009833}7{image=suit_utan_L} Т{image=suit_uvao_L} {color=#FF6600}Т{image=suit_2ch_L}{/color}{/color}{/b}."
    "Two full houses, like two quads, cannot be the same (there are no jokers in the deck).{nw}"
    ""

    "- {b}Four of a kind{/b}Quad: four cards{nw}"
    if persistent.font_size == 'small':
        "of equal value, example: {b}{color=#FF6600}8{image=suit_ussr_S} 8{image=suit_2ch_S} {color=#009833}8{image=suit_uvao_S} 8{image=suit_utan_S}{/color}{/b}{/b}, rest of the cards don't matter."
    elif persistent.font_size == 'large':
        "of equal value, example: {b}{color=#FF6600}8{image=suit_ussr_L} 8{image=suit_2ch_L} {color=#009833}8{image=suit_uvao_L} 8{image=suit_utan_L}{/color}{/b}{/b}, rest of the cards don't matter."
    "If, in addition to the quad, the player also has a pair, it does not count;{nw}"
    "{i}there is no combination «4+2» in the game{/i}."
    "Two quads fundamentally cannot be the same, so when two players have{nw}"
    "such combinations, the winner is the one with the four of a kind of higher value.{nw}"
    ""

    pause(1)
    nvl clear

    "- {b}Straight Flush{/b}: any five cards of the same suit in order,{nw}"
    if persistent.font_size == 'small':
        "example: {b}{color=#009833}9{image=suit_utan_S} 8{image=suit_utan_S} 7{image=suit_utan_S} 6{image=suit_utan_S} 5{image=suit_utan_S}{/color}{/b}. Ace can both start the combination (royal flush),{nw}"
        "and finish it: {b}{color=#009833}5{image=suit_uvao_S} 4{image=suit_uvao_S} 3{image=suit_uvao_S} 2{image=suit_uvao_S} Т{image=suit_uvao_S}{/color}{/b}."
        "Card combinations of {b}{color=#FF6600}2{image=suit_ussr_S} Т{image=suit_ussr_S} К{image=suit_ussr_S} Д{image=suit_ussr_S} В{image=suit_ussr_S}{/color}{/b} or {b}{color=#FF6600}4{image=suit_2ch_S} 3{image=suit_2ch_S} 2{image=suit_2ch_S} Т{image=suit_2ch_S} К{image=suit_2ch_S}{/color}{/b} — are not straight flushes.{nw}"
    elif persistent.font_size == 'large':
        "example: {b}{color=#009833}9{image=suit_utan_L} 8{image=suit_utan_L} 7{image=suit_utan_L} 6{image=suit_utan_L} 5{image=suit_utan_L}{/color}{/b}. Ace can both start the combination (royal flush),{nw}"
        "and finish it: {b}{color=#009833}5{image=suit_uvao_L} 4{image=suit_uvao_L} 3{image=suit_uvao_L} 2{image=suit_uvao_L} Т{image=suit_uvao_L}{/color}{/b}."
        "Card combinations of {b}{color=#FF6600}2{image=suit_ussr_L} Т{image=suit_ussr_L} К{image=suit_ussr_L} Д{image=suit_ussr_L} В{image=suit_ussr_L}{/color}{/b} or {b}{color=#FF6600}4{image=suit_2ch_L} 3{image=suit_2ch_L} 2{image=suit_2ch_L} Т{image=suit_2ch_L} К{image=suit_2ch_L}{/color}{/b} — are not straight flushes.{nw}"
    "If a player has {b}six{/b} cards in order, the lowest card is ignored."
    "If two players hold a straight flush at the same time, the winner is the one,{nw}"
    "whose combination begins with a higher value card."
    "If both players have identical straight flushes, a draw is declared.{nw}"
    ""

    "- {b}Royal flush{/b}: is not a separate combination,{nw}"
    "but is a special case of straight flush, the highest of all possible, and consists of 5 senior{nw}"
    if persistent.font_size == 'small':
        "(ace, king, queen, jack, ten) cards of the same suit, example: {b}{color=#FF6600}Т{image=suit_ussr_S} К{image=suit_ussr_S} Д{image=suit_ussr_S} В{image=suit_ussr_S} 10{image=suit_ussr_S}{/color}{/b}."
    elif persistent.font_size == 'large':
        "(ace, king, queen, jack, ten) cards of the same suit, example: {b}{color=#FF6600}Т{image=suit_ussr_L} К{image=suit_ussr_L} Д{image=suit_ussr_L} В{image=suit_ussr_L} 10{image=suit_ussr_L}{/color}{/b}."
    "If at least one of the five cards is not the same suit as the others, then the resulting{nw}"
    "the combination will be considered a straight from the ace."
    "This combination comes out quite rarely; maybe someone will get lucky…{nw}"
    ""

    pause(1)
    $ set_mode_adv()
    $ persistent.altRulesRead_new = True

label alt_day2_poker_rules_known:
# ----------------------------------------------------------------------------------- /ADD
    el "Now, to learn the material better, let's play a test game."
    el "Six cards per side..."
    show us dontlike pioneer at left
    show el angry pioneer at right
    with dissolve
    extend " I said six, not twelve!"
    "He shouted, glancing obliquely at Shurik and Ulyana's table."
    "No wonder - the redheaded beastie had taken all twelve cards and was looking at them, picking out the prettiest ones."
    hide us with dissolve
    "After a few minutes of arguing and swearing, Ulyanka snorted and returned the cards to their homeland, then, after shuffling the deck, dealt herself and Shurik six cards each."
# --------------------------------------------------------------------- ADD Блокировка роллбэка включена
    $ d2_cardgame_block_rollback = True
# --------------------------------------------------------------------- /ADD
    stop music fadeout 2


    if persistent.altCardsDemo_new:
        menu:
            "Do the tutorial":
                jump alt_day2_demo_play_new
            "Skip the tutorial":
                jump alt_day2_cards_continue_new

label alt_day2_demo_play_new:
    python:
        dialogs = {
                        (3, 'rival_select','call'): 'alt_day2_demo_play_intro_new',
                        (3, 'me_defend_1','call'):  'alt_day2_demo_play_me_defend_1_new',
                        (3, 'me_defend_2','call'):  'alt_day2_demo_play_me_defend_2_new',
                        (3, 'me_select_1','call'):  'alt_day2_demo_play_me_select_1_new',
                        (3, 'rival_defend','call'): 'alt_day2_demo_play_rival_defend_new',
                        (2, 'rival_select','jump'): 'alt_day2_demo_play_after_loop_new'
                    }
        generate_cards_alt('bg hall', dialogs)
        rival = CardGameRivalWiseUsual(un_avatar_set, u"Test game", 'foolplay', 5)
        alt_name_my_rival_r = "Lena"
        VISIBLE = False
        alt_whose_first_move = 'rival'
    jump cards_gameloop_wise_alt

label alt_day2_demo_play_intro_new:
    play music music_list["get_to_know_me_better"] fadein 2
    show el normal pioneer at cleft with dissolve
    $ show_cards_alt()
    $ renpy.transition(dissolve)
    el "These are not just cards."
    if alt_day2_walk == 1:
        th "This is also your way of leaving your opponent without pants."
        th "If we played for money..."
        dreamgirl "Or undress..."
        "Well, let's not talk about sad things."
    el "These are your special forces. {w}Elite!"
    el "You treasure each of them, for their lives are unrepeatable."
    el "The loss of every one of them is critical."
    el "Now turn the cards over and look."
    $ VISIBLE = True
    $ alt_hint_poker = True
    if alt_day2_walk == 1:
        $ INVISIBLE = True
    $ show_cards_alt()
    $ renpy.transition(dissolve)
    "As you might expect, Ulyanka turned over Shurik's cards and studied them thoughtfully."
    show el angry pioneer at cleft with dspr
    el "Your cards!"
    "Electronik yelled."
    el "Yours! Not someone else's."
    us "I was just doing recon! There!"
    "Compared to the impenetrable Shurik, Ulyana was a model of the unruly element."
    "With a sigh, Shurik gathered up his cards and, shuffling carefully, dealt himself another six cards."
    show el normal pioneer at cleft with dspr
    "Meanwhile, Electronik continued his explanation:"
    el "So you are at the head of the elite troops."
    el "But the battle itself is yet to come. In the meantime, you need to fortify your lines."
    "To entrench, that's what I'm saying."
    el "And to do that... you have to lure the enemy elite to your side!"
    us "Lure them in as in 'steal'?"
    "Ulyana's voice had an unconcealed enthusiasm."
    show el upset pioneer at cleft with dspr
    el "Kind of, y-yes..."
    "The presenter was a little embarrassed by the epithet, but there was no cover-up, so he agreed."
    show el normal pioneer at cleft with dspr
    el "In general. But it's not that simple."
    el "The first move you make is to set yourself a target, and try to bait it."
    el "You don't see who it is, so luck works here."
    us "My grandfather is an officer!"
    "Declared Ulyana."
    show el smile pioneer at cleft with dspr
    el "So the enemy is reaching for the card, but you mustn't doze off either!"
    el "You have two attempts to confuse the enemy by swapping cards!"
    show el serious pioneer at cleft with dspr
    el "Or you may not change if a card you don't need is under attack. Just skip your turn, and the card goes to the attacker."
    el "Naturally, the defender sooner or later becomes the attacker - and that's when he can return a card or take the card he needs from his opponent."
    show el grin pioneer at cleft with dspr
    el "But from words to deeds. It's easier to understand in practice, isn't it?"
    el "So... Let's play!"

    hide el with dissolve
    me "The first move is yours..."
    "I laid the cards out as comfortably as I could."
    "And Lena, even more embarrassed than usual, reached for my cards..."
    return

label alt_day2_demo_play_me_defend_1_new:
    "But then her hand froze halfway."
    un "Y-you'll be..."
    th "Right! I'm supposed to protect my card!"
    "I remembered what Electronik was saying there..."
    th "To try to confuse your opponent, you can switch cards - and so twice. Or you don't have to swap..."
    th "Should I protect this card or not?"
    return

# ============================================ добавлена одна метка
label alt_day2_demo_play_me_defend_2_new:
    th "And Lena may or may not change her choice, taking another card."
    th "Little by little, things were beginning to make sense!"
    return
# ============================================ добавлена одна метка

label alt_day2_demo_play_me_select_1_new:
    me "Now it's my turn."
    th "I can return the stolen card or choose any other..."
    if alt_day2_walk == 1:
        th "And knowing your opponent's cards, it's easy to choose the right one..."
        th "I never thought I would cheat in a tournament, but maybe that's what will save me..."
    return

label alt_day2_demo_play_rival_defend_new:
    th "Lena can try to protect her card."
    th "But if I'm careful, I'll still take the one I picked from the beginning..."
    return

label alt_day2_demo_play_after_loop_new:
    $ show_cards_alt()
    $ renpy.transition(dissolve)
    th "Got it!"
    window auto
    $ ui.jumpsoutofcontext('alt_day2_cards_continue_new')

label alt_day2_cards_continue_new:
    scene bg int_dining_hall_sunset with dissolve
    python:
        renpy.scene('underlay')
    $ persistent.altCardsDemo_new = True
    play music music_list["my_daily_life"] fadein 5
    "Electronik, who had been watching us until then, nodded contentedly."
    "Looks like we've really figured out his game now."
    show el normal pioneer at center with dissolve
    el "So, during the game the opponents exchange their fighters three times and then reveal the cards."
    el "And we see whose army is stronger."
    hide el with dissolve
    "Electronik stepped back to his paper sheet, and Ulyana couldn't stand it and shouted."
    show us laugh pioneer with dissolve
    us "My army will be the strongest!"
    show us grin pioneer with dspr
    us "Let's play already!"
    hide us with dissolve

label alt_day2_tournament_prep_new:
    scene bg int_dining_hall_sunset with dissolve
    show mt normal pioneer with dissolve
    mt "Let's spice the game up a little bit!"
    show el surprise pioneer at left with dissolve
    el "What do you mean by that?"
    show mt laugh pioneer with dspr
    mt "I see that someone here is very determined to win, so let's introduce an element of chance."
    hide mt with dissolve
    "She took some papers out of her pocket and, quickly scrawling them, wrote numbers on them, poured them into her panama hat, and circled around to those present."
    show el sad pioneer with dspr
    el "Oooh, extra trouble."
    "The guy sighed."
    show mt normal pioneer with dissolve
    mt "It's okay! {w}Let's draw lots and pair up."
    mt "I know those match-fixing games of yours!"
    "Not five minutes later, and we're already paired up."

    if persistent.altCardsWon1_new or persistent.altCardsFail_new:
        menu:
            "Play tournament":
                pass
            "Win in finals" if persistent.altCardsWon3_new:
                $ alt_day2_detour_1_tour = True                         # Пропускаем 1 тур
                $ alt_day2_detour_semifinal = True                      # Пропускаем полуфинал
                $ alt_day2_detour_final = True                          # Пропускаем финал
                $ alt_day2_tournament_fast_win = True                   # Победа в финале на халяву
                $ karma += 10
                menu:
                    "Against random enemy":
                        pass
                    "Against Lena":
                        $ alt_day2_detour_number = 1
                    "Against Slavya":
                        $ alt_day2_detour_number = 2
                    "Against Alisa":
                        $ alt_day2_detour_number = 3
                    "Against Miku":
                        $ alt_day2_detour_number = 4
                    "Against Ulyana":
                        $ alt_day2_detour_number = 5
                    "Against Shurik":
                        $ alt_day2_detour_number = 6
                    "Against Zhenya":
                        $ alt_day2_detour_number = 7
            "Lose in finals" if persistent.altCardsWon2_new:
                $ alt_day2_detour_1_tour = True                         # Пропускаем 1 тур
                $ alt_day2_detour_semifinal = True                      # Пропускаем полуфинал
                $ alt_day2_detour_final = True                          # Пропускаем финал
                $ karma -= 10
                menu:
                    "Against random enemy":
                        $ alt_day2_detour_number = 0
                    "Against Lena":
                        $ alt_day2_detour_number = 1
                    "Against Slavya":
                        $ alt_day2_detour_number = 2
                    "Against Alisa":
                        $ alt_day2_detour_number = 3
                    "Against Miku":
                        $ alt_day2_detour_number = 4
                    "Against Ulyana":
                        $ alt_day2_detour_number = 5
                    "Against Shurik":
                        $ alt_day2_detour_number = 6
                    "Against Zhenya":
                        $ alt_day2_detour_number = 7
            "Lose in semifinals" if persistent.altCardsWon1_new:
                $ alt_day2_detour_1_tour = True                         # Пропускаем 1 тур
                $ alt_day2_detour_semifinal = True                      # Пропускаем полуфинал
                $ karma -= 10
            "Lose in first round":
                $ alt_day2_detour_1_tour = True                         # Пропускаем 1 тур

 # ---------------------------------------------------------------------------------
label alt_day2_tournament_tour_1_new:
    $ alt_tournament_state = "1_round_start"                                                # устанавливаем начало 1-го раунда
    $ alt_day2_gamblers_begin = alt_gamblers_shuffler()                                     # вызываем рандомизатор — получаем список игроков, отсортированный по уcловным номерам.
    $ alt_my_rival_1_tour = alt_get_me_rival(alt_day2_gamblers_begin)                       # узнаём своего соперника
    $ alt_name_my_rival_i = alt_my_rival_1_tour.name['i']                                   # узнаём ИМЯ своего соперника (в именительном падеже)
    $ alt_name_my_rival_r = alt_my_rival_1_tour.name['r']                                   # узнаём ИМЯ своего соперника (в родительном падеже)
    $ alt_name_my_rival_d = alt_my_rival_1_tour.name['d']                                   # узнаём ИМЯ своего соперника (в дательном падеже)
    $ alt_name_my_rival_v = alt_my_rival_1_tour.name['v']                                   # узнаём ИМЯ своего соперника (в винительном падеже)
    $ alt_name_my_rival_t = alt_my_rival_1_tour.name['t']                                   # узнаём ИМЯ своего соперника (в творительном падеже)
    $ alt_spr_my_rival = alt_my_rival_1_tour.take                                           # получаем спрайт соперника — заголовок
    $ alt_emo_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][0]                 # эмоция (строка)
    $ alt_acc_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][1]                 # аксессуар (строка)
    $ alt_clot_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][2]                # одежда (строка)
    $ alt_pos_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][3]                 # положение
    $ alt_nick_my_rival = alt_my_rival_1_tour.nick                                          # получаем характер соперника (для диалога)
 # ---------------------------------------------------------------------------------
    scene bg int_dining_hall_sunset with dissolve
    $ renpy.fix_rollback()                                                                  # фиксируем выбор — "откатом" поменять будет нельзя
    "Random sent me the opponent in the face of {nw}%(alt_name_my_rival_v)s.{w}"                             # называем своего соперника

# ------------------------------------------------- ДИАЛОГИ
    if alt_my_rival_1_tour.take == 'un':
        show un shy pioneer at cright with dissolve
        me "Good evening once again."
        show un smile pioneer with dspr
        "She smiled embarrassedly, but said nothing."

    elif alt_my_rival_1_tour.take == 'sl':
        show sl smile2 pioneer at cright with dissolve
        sl "You know, I'm not very good at cards."
        me "I don't know anything about this game at all."
        "Slavya smiled at me and sat across from me."

    elif alt_my_rival_1_tour.take == 'dv':
        show dv grin pioneer2 at cright with dissolve
        dv "So, ready for a crushing defeat?"
        "She grinned, sitting down in the opposite seat."
        if herc or loki:
            me "Of course. {w} I'll bring two gladioluses to your grave."
        else:
            me "Alisa, maybe we shouldn't...?"
            dv "We have to, Syoma, we have to."

    elif alt_my_rival_1_tour.take == 'mi':
        show mi smile pioneer at cright with dissolve
        if ('music_club' in list_voyage_7dl):
            mi "Hello again, Senechka."
        else:
            mi "Oh, hello, Semyon!"
        if loki:
            me "Well, hello, Miku."
        elif herc:
            me "And good day to you, too."
        else:
            me "Hello."
        show mi laugh pioneer with dspr
        mi "How great that I got you as my opponent! I really wanted it to be you!"
        "I was a little taken aback."
        me "Why?"
        show mi grin pioneer with dspr
        mi "Well, well, well!"
        "Exclaimed Miku."
        if ('music_club' in list_voyage_7dl):
            show mi smile pioneer with dspr
            mi "You're the new man at camp, and you and I haven't really talked to each other yet!"
            th "So that's what she means."
            "To tell you the truth, I'd gladly trade a card game for a conversation with Miku."
            "She may be a chatterbox, but she's a beautiful chatterbox."
            "The main thing is to be able to filter out the flow of her words and pick out the main thing."
            "And then I'll see something else in her."
            "However..."
            me "Let's do it after the game, okay?"
            me "Now that we're in the game... and so on."
            show mi happy pioneer with dspr
            mi "We can have a conversation in the process."
            "Continued to insist hafu."
            show mi smile pioneer with dspr
            mi "As my Pa says - nothing prevents you from combining useful things with pleasure!"
            "I wouldn't call the tournament 'useful'."
            me "Deal."
        else:
            show mi laugh pioneer with dspr
            mi "You're the new person at camp, and we haven't really gotten to know each other yet!"
            "Without stopping to chat, she sat down at the table and folded her arms."
            th "This game is going to be oh-so-long."
            if dr:
                dreamgirl "You're a wimp, so you have to suffer."
                th "Go to hell."

    elif alt_my_rival_1_tour.take == 'us':
        stop music fadeout 2
        show us laugh pioneer at cright with dissolve
        us "Ready to give in?"
        play music music_7dl["carefree"] fadein 1
        me "Don't dream of it."
        show us calml pioneer with dspr
        us "And don't! But we'll play by my rules!"
        me "What rules is that?"
        us "You'll see!"

    elif alt_my_rival_1_tour.take == 'sh':
        show sh normal pioneer at cright with dissolve
        sh "Well, may the best man win?"
        "I silently shook his hand."

    elif alt_my_rival_1_tour.take == 'mz':
        show mz normal glasses pioneer at cright with dissolve
        mz "I am your opponent."
        "She squeaked, taking a seat across from me."
        "I nodded silently in response."
# ------------------------------------------------- /ДИАЛОГИ


label alt_day2_participate_new:
    $ alt_day2_gamblers_1_tour = alt_gamblers_arrange(alt_day2_gamblers_begin)      # получаем список игроков, рассаженных по столам попарно (1 тур)
    $ renpy.fix_rollback()                                                          # фиксируем выбор — "откатом" поменять будет нельзя
    $ places_my_table = alt_get_my_table(alt_day2_gamblers_1_tour)                  # Стол Семёна = [место Семёна, место соперника, № их стола]

    if not alt_day2_detour_1_tour:                                                  # если НЕ пропуск 1 тура
        scene bg int_dining_hall_sunset with dissolve
        "While this was going on, I decided to find out what the disposition was on the field of play."
        $ alt_mstt = 9
        call show_tournament_table                                                  # показываем турнирную таблицу — ПУСТУЮ


    $ alt_table_no = 1                                                              # № стола = 1 (начинаем с первого)
    $ alt_mstt = 0                                                                  # обнуляем глобальный счетчик таблицы
    $ alt_random_box_1 = range(1,len(alt_table_affiliation)+1)                      # черный ящик — список от 1 до длины представлений столов +1
    while alt_table_no <= 4:                                                        # перебираем столы от 1 до 4
        if not alt_day2_detour_1_tour:                                              # если НЕ пропуск 1 тура
            $ sitting_at_table,gambler_upper,gambler_lower,must_taunt = alt_declare_tournament_tables(alt_table_no)  #расссадка, игроки, таунты — по номеру стола
            "%(sitting_at_table)s"
            call show_tournament_table                                                  # переход по метке — вызов очередной фишки
            extend " %(gambler_upper)s"                                                 # выводим в окно имя верхнего игрока
            call show_tournament_table                                                  # переход по метке — вызов очередной фишки
            extend " and %(gambler_lower)s."                                              # выводим в окно имя нижего игрока
            if must_taunt != None:                                                      # если таунт есть
                "%(must_taunt)s"                                                        # выводим его

            if alt_table_no == 1 and alt_table_no != places_my_table[2]:
                "The first table is dealt with, one of them won't make it to the finals tonight."
            elif alt_table_no == 2 and places_my_table[2] == 1:
                "The second table is dealt with, one of them won't make it to the finals tonight."

        if alt_table_no != places_my_table[2]:                                                       # если номер стола — НЕ свой
            $ alt_day2_gamblers_1_tour[2*alt_table_no - renpy.random.choice([1,2])].winner = True    # тогда один из игроков (рандомно) — победитель в этапе
            $ renpy.block_rollback()                                                                 # блокируем роллбак
        $ alt_table_no += 1                                                                          # следующий стол
    if (alt_day2_detour_number != 0):                                                                # если выбрали конкретного соперника для финала
        $ alt_day2_gamblers_1_tour[6].winner = False                                                 # его соперник в первом коне проигрывает
        $ alt_day2_gamblers_1_tour[7].winner = True                                                  # а он сам выигрывает в первом коне
    if not alt_day2_detour_1_tour:                                                                   # если НЕ пропуск 1 тура
        "In this uncomplicated way it was possible to sort out a little bit about who is playing against whom."
        "Well..."
        if alt_day2_dv_ultim == 1:
            "May I get lucky, and one red-headed snooty doesn't!"
        "I nodded, signaling my readiness."

    if alt_day2_detour_1_tour and not alt_day2_detour_semifinal:                # если пропуск 1 тура и не пропуск полуфинала
        jump alt_day2_participate_fail_end_new                                  # переход на  поражение в 1 туре
    elif alt_day2_detour_semifinal:                                             # если пропуск полуфинала
        jump alt_day2_participate_win_end_new                                   # переход на победу в 1 туре

label alt_day2_tournament_start_new:                                            # начало 1 тура — сюда переходим при реванше
    call alt_day2_stipulation_new                                               # определяемся, кто первый ходит

#-------------------------------------------------------------------------------------------------
    # первоначальные "настройки" игроков — могут меняться по результатам игры
    # 'defense' — защита, 'gamble' — риск, 'succumb' — слив, 'foolplay' — рандом
    # вероятность ошибки: 1 = 80%, …, 4 = 20%, 5 — ошибок нет.

    if alt_my_rival_1_tour.take == 'un':                                                    # Лена
        if alt_day2_dv_ultim != 1:                                                              # если с Алисой не спорить
            $ alt_day2_gambler_behavior = 'gamble'                                              # Лена пытается рискнуть
            $ alt_day2_gambler_skill = 3                                                        # правда, ошибок многовато — 40%(3)
        else:
            $ alt_day2_gambler_behavior = 'succumb'                                             # Если поспорить — то также игра в поддавки
            $ alt_day2_gambler_skill = 4                                                        # может ошибиться  — 20%(4)
    elif alt_my_rival_1_tour.take == 'sl':                                                  # Славя будет защищаться, ошибок — 40%(3)
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 3
    elif alt_my_rival_1_tour.take == 'dv':                                                  # Алиса рискует, ошибок — 20%(4)
        $ alt_day2_gambler_behavior = 'gamble'
        $ alt_day2_gambler_skill = 4
    elif alt_my_rival_1_tour.take == 'mi':                                                  # Мику будет защищаться, ошибок — 40%(3)
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 3
    elif alt_my_rival_1_tour.take == 'us':                                                  # Ульяна будет защищаться
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 1                                                        # ошибок — 80%(1)
    elif alt_my_rival_1_tour.take == 'sh':                                                  # Шурик экспериментирует, так что может и рискнуть, и защищаться, и слить; ошибки 40%(3)
        $ alt_day2_gambler_behavior = renpy.random.choice(['defense', 'gamble'])            # у него своя кухня — набор из возможных вариантов
        $ alt_day2_gambler_skill = 3
    elif alt_my_rival_1_tour.take == 'mz':                                                  # Женя играет рандомно, как в классике, ошибки = 5
        $ alt_day2_gambler_behavior = 'foolplay'
        $ alt_day2_gambler_skill = 5
#-------------------------------------------------------------------------------------------------

label alt_day2_1_tour_re_game:                                                              # игра 1 тура — сюда возвращаемся на повторную игру
    $ alt_my_poker_hand = None
    $ alt_rival_poker_hand = None

    if alt_day2_walk == 1:
        $ VISIBLE = True
        $ INVISIBLE = True
    else:
        $ VISIBLE = True
        $ INVISIBLE = False

    python:
        dialogs = {
                        (0, 'win','jump'):'alt_day2_one_play_win_new',
                        (0, 'fail','jump'):'alt_day2_one_play_fail_new',
                        (0, 'draw','jump'):'alt_day2_one_play_draw_new'
                    }
        generate_cards_alt('bg hall', dialogs)

# ****************   НОВЫЕ  СОПЕРНИКИ   ******************************************
        if alt_my_rival_1_tour.take == 'un':
            rival = CardGameRivalWiseUsual(un_avatar_set, u"Лена", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_1_tour.take == 'sl':
            rival = CardGameRivalWiseUsual(sl_avatar_set, u"Славя", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_1_tour.take == 'dv':
            rival = CardGameRivalWiseUsual(dv_avatar_set, u"Алиса", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_1_tour.take == 'mi':
            rival = CardGameRivalWiseUsual(mi_avatar_set, u"Мику", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_1_tour.take == 'us':
            rival = CardGameRivalWiseLikeUS(us_avatar_set, u"Ульяна", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_1_tour.take == 'sh':
            rival = CardGameRivalWiseUsual(sh_avatar_set, u"Шурик", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_1_tour.take == 'mz':
            rival = CardGameRivalWiseUsual(mz_avatar_set, u"Женя", alt_day2_gambler_behavior, alt_day2_gambler_skill)
# ************************************************************************************

    $ alt_hint_poker = alt_hint_poker_contractual                                           # подсказки комбинаций — по просмотру правил
    jump cards_gameloop_wise_alt                                                            # переход карточный стол

#-------------------------------------------------------------------------------------------------
label alt_day2_participate_fail_end_new:
    $ alt_day2_result_tour = 1                                              # Семён проиграл в 1 туре

    $ persistent.altCardsFail_new = True

    $ alt_day2_gamblers_1_tour[places_my_table[1]].winner = True            # соперник выиграл
    $ alt_tournament_state = "1_round_end"                                  # устанавливаем конец 1-го раунда

    scene bg int_dining_hall_sunset with dissolve
    call alt_day2_summary_poker_round

# ---------------------------------------------------- ДИАЛОГИ
    if alt_my_rival_1_tour.take == 'un':
        $ lp_un = lp_un + 1
        stop music fadeout 2
        if alt_day2_dv_ultim == 1:
            show un angry2 pioneer at center with dissolve
            un "You gave in... You damned crook, you gave in..."
            play music music_list["you_lost_me"] fadein 2
            "What is she even talking about? Calling me a crook too."
            if alt_day2_walk == 1:
                th "She's not that far from the truth, though."
            me "Lena, I'm sorry, but..."
            un "Don't say anything. I know what you were arguing about with that redhead."
            un "And I know - what's at stake!"
            show un sad pioneer with dspr
            un "Don't you understand that no one wants such a victory? And you tomorrow... for the whole camp..."
            me "Do you really think I care? Let him say what he wants. I did what I thought was right."
        else:
            show un angry2 pioneer with dspr
            un "What have you done?"
            play music music_list["you_lost_me"] fadein 2
            "She lifted herself above the table and immediately fell back down."
            un "Why? Who needs such a victory..."
            me "Me?"
            th "She's so pretty when she's angry."
        show un angry2 pioneer with dspr
        "And Lena slammed her palm on the table, so that for a second everyone was silent and turned to her."
        un "Who needs that kind of victory?"
        "She repeated."
        me "That victory was for me."
        "In the silence of the grave, I said."
        show un serious pioneer with dspr
        me "Just to point out to someone that threats or blackmail don't solve everything."
        me "Enjoy your evening."
        stop music fadeout 3
        hide un with dissolve
        "I nodded and walked away from the table, leaving Lena silently gulping for air."
        play music music_list["my_daily_life"] fadein 5

    elif alt_my_rival_1_tour.take == 'sl':
        show sl smile pioneer with dissolve
        sl "Semyon, if you want to play again, I don't mind."
        "Funny girl, even willing to sacrifice her own victory."
        th "No, it's my turn to be noble today."
        "I leaned over the table and said."
        me "I wish you luck in the semifinals!"
        sl "But I just sat down to play for company!"
        sl "I don't like cards at all."
        me "What can you do. {w}If you signed up, play to the end."
        show sl sad pioneer with dspr
        me "Besides, I really want you to win today. Can you do it?"
        show sl normal pioneer with dspr
        "Slavya nodded uncertainly, and I stood up and gave her a thumbs-up."
        "A little self-confidence outside her usual habitat is what she needs."

    elif alt_my_rival_1_tour.take == 'dv':
        if alt_day2_dv_ultim == 1:
            show dv grin pioneer2 with dspr
            dv "So, are you prepared?"
            "She was reveling in the moment."
            if alt_day2_walk == 1:
                th "Yeah, and was it worth tagging cards if they didn't help me?"
            else:
                pass
            me "For what?"
            dv "For what? To a story about where you looked, what you touched."
            dv "It's going to be a very interesting story, I feel it!"
            show dv laugh pioneer2 with dspr
            dv "But okay."
            me "Yeah?"
            "I was a bit of a jerk on the spot."
            th "Did she really change her mind!"
            show dv smile pioneer2 with dissolve
            dv "I'll tell them all about it at the finals, when I'll be hailed as the winner!"
            "Yeah, I got my hopes up for nothing."
            "It's Dvachevskaya, after all!"
            th "You can't expect anything good from her."
        "I tried to save face."
        "Politely stood up, tilted my head, and said,"
        me "Congratulations on your victory."
        me "And good luck in the semifinals."
        "Turned around and walked away to the fans."
        th "Might be able to get lost in the crowd."

    elif alt_my_rival_1_tour.take == 'mi':
        show mi happy pioneer with dspr
        mi "Oh, what luck! I've never, ever been lucky at cards, so I thought it wasn't my thing, but then I was asked, and I said yes."
        mi "I didn't even think I could win! Senechka, you're not offended? Or do you want to replay, I do not feel sorry! No, really, really not offended?"
        show mi smile pioneer with dspr
        mi "I just don't want to feel good at the expense of others, it's bad, Pa always told me that you can't build happiness on other people's tears."
        me "It's okay. You're playing great, that's why you won."
        me "Good luck in the semifinals."
        hide mi with dissolve
        "I wished, and turned away, and departed."

    elif alt_my_rival_1_tour.take == 'us':
        show us laugh pioneer with dissolve
        us "Hee! Loser!"
        "Thanks, cap."
        me "Do you have to yell about it to the whole mess hall?"
        us "Of course we do!"
        show us grin pioneer with dspr
        us "Do you want to play some more? {w}Just for fun."
        us "While the others are slowing down, we'll have time for a game. Well?"
        me "What's the catch?"
        us "There's no catch."
        us "So, you want some?"
        me "Thanks, but no."
        show us dontlike pioneer with dissolve
        us "Nerd! {w}Don't you even want to get even?"
        us "Doesn't it hurt to lose to a girl?"
        me "I don't give a shit, really."
        th "Who thinks and decides what there is remains his domain."
        "Wise advice for all occasions: talk less."
        us "Nerd! {w}Nerd."
        "She shouted."
        show us dontlike pioneer at fright with move
        "And then she jumped up abruptly and went to the table set aside for the next game."
        us "You're just afraid of losing again! You weakling!"
        me "Yeah, take me at it again, baby."
        me "Enjoy your evening."
        stop music fadeout 3
        hide us with dissolve
        "I headed toward the crowd of spectators. It was my turn to change roles."
        play music music_list["my_daily_life"] fadein 3

    elif alt_my_rival_1_tour.take == 'sh':
        show sh normal pioneer with dissolve
        sh "It was a decent game. Thank you."
        if loki:
            me "Likewise."
        elif herc:
            "He held out his hand to me, which I shook with dignity."
        else:
            "We shook hands."
            "He's got a strong grip, though, for someone who can't lift anything heavier than a blowtorch."
        sh "And I went on to smash the enemy's lines."

    elif alt_my_rival_1_tour.take == 'mz':
        show mz normal glasses pioneer with dissolve
        "Zhenya shrugged her shoulders and got up from the table."
        mz "Looks like this is going to be even easier than I thought."
# ---------------------------------------------------- \\Диалоги

    scene bg int_dining_hall_sunset with dissolve
    "Meanwhile, the situation was as follows:"
    pause(.5)
    call alt_day2_1_tour_analizer                                                   # Вызов анализатора 1 раунда
    $ renpy.block_rollback()                                                          # блокируем роллбак
    stop music fadeout 3
    $ alt_drawing_of_detour()                                                       # вызываем рандомизатор пропуска полуфинала и финала
    $ renpy.fix_rollback()                                                          # фиксируем выбор — "откатом" поменять будет нельзя
    jump alt_day2_semifinal_new                                                     # переход в полуфинал ?

#------------------------------------------------------------------------------------------------
label alt_day2_participate_win_end_new:
    $ alt_day2_result_tour = 2                                              # Семён выиграл в 1 туре
    if not alt_day2_detour_semifinal:                                       # если не "выигрыш" в 1 туре скипом
        $ persistent.altCardsWonRivals_new[alt_spr_my_rival] = True         # Выиграли у этого соперника
    $ persistent.altCardsWon1_new = True
    $ alt_day2_gamblers_1_tour[places_my_table[0]].winner = True            # Семён выиграл
    $ alt_tournament_state = "1_round_end"                                  # устанавливаем конец 1-го раунда

# -------------------------------------------------------------------------
# ЕСЛИ Славя, Мику или Шурик и НЕ скип тура — итоги ДО диалогов
    if (alt_my_rival_1_tour.take in ['sl','mi','sh']) and not alt_day2_detour_semifinal:
        scene bg int_dining_hall_sunset with dissolve
        "The first round was over."
        "The situation, meanwhile, was as follows:"
        call alt_day2_1_tour_analizer                                                   # вызываем анализатор 1 тура
        $ renpy.block_rollback()                                                          # блокируем роллбак
# -------------------------------------------------------------------------
    pause(1)
    scene bg int_dining_hall_sunset with dissolve
    call alt_day2_summary_poker_round

# ---------------------------------------------------- ДИАЛОГИ
    if alt_my_rival_1_tour.take == 'un':
        if alt_day2_rival_win == 0:
            "She had nothing."
            "And with what she had, I'd be ashamed to open my cards."
        else:
            "Lena got a couple or two good cards for these games."
            "Unfortunately, it wasn't enough to win."
        "Poor girl."
        show un sad pioneer with dissolve
        "She sat there as if she herself could not believe what had just happened."
        if lp_un >= 6 and not alt_day2_detour_semifinal:
            menu:
                "Offer her a redo match":
                    $ karma += 5
                    $ lp_un += 1
                    me "Unlucky match."
                    un "Yes..."
                    me "How about one more?"
                    show un smile pioneer with dspr
                    "Lena smiled."
                    un "The offer is tempting, but I'll decline."
                    me "Why?"
                    show un shy pioneer with dspr
                    un "Well…"
                    pause(0.5)
                    if dr:
                        me "Okay, you don't have to tell me."
                        me "If you don't want to, that's your right."
                        me "I can't force you."
                        show un smile pioneer with dspr
                        "Lena smiled appreciatively."
                        un "Good luck. I'll be rooting for you."
                        me "Mm-hmm...{w} Thank you."
                    else:
                        me "Yes?..."
                        th "I'm sorry, Lena, but I'm going to do a little pincer work."
                        show un sad pioneer with dspr
                        un "I'm not too fond of such games, and I don't know how to play them at all."
                        un "That's why I'm not eager to win. Even before the start I decided for myself - whatever happens."
                        un "And a rematch... A rematch isn't it."
                        "And on her face you could clearly read - I don't want to lose anymore."
                        me "That's your right. I won't insist."
                        show un cry_smile pioneer with dspr
                        un "Thank you."
                        show un shy pioneer with dspr
                        un "I'll be rooting for you."
                    hide un with dissolve
                    "She got up from the table and disappeared behind the fans."
                    jump alt_day2_1_tour_end                                                 # В ПОЛУФИНАЛ
                "Do nothing":
                    pass
        $ lp_un -= 1
        $ lp_dv += 1
        "I smiled."
        me "Thanks for playing!"
        show un shy pioneer with dspr
        un "O-o-okay."
        hide un with dissolve
        "She got up from the table and disappeared behind the fans."

# ====================================================== Пропускаем часть диалога, если "выиграли" 1 тур скипом
        if not alt_day2_detour_semifinal:
            "And I couldn't help cheering."
            th "I wonneredededereded! I mean I won."
            dreamgirl "Yay! {w=.4}Against a girl. {w=.4}In a game that neither you nor she knows. {w}Great achievement."
            th "Shut up."
            th "I'll rejoice in winning the way I only rejoice when I roll up that redheaded sassy girl!"
            dreamgirl "No, you really are a hero. No doubt about it."
            dreamgirl "Maybe you should have let the girl win. She doesn't look the happiest as it is, and you knocked the rest of the ground out from under her."
            dreamgirl "And how did it feel? Was it worth it?"
            th "I said shut up."
            show blinking with dissolve
            if herc or loki:
                "My aim is not to encourage every sissy, but to rub the nose of one redheaded arrogant girl!"
                "Although, frankly, the temptation to lose just to see how she fulfills its threats is great enough. {w}No, seriously!"
                scene bg ext_square_sunset
                show prologue_dream
                with fade
                "Tomorrow we get up, we go to the lineup, and there she is already on the podium, between Olga Dmitrievna and Slavya."
                show dv grin pioneer2 behind prologue_dream with diam
                "So and so, she says in a nasty voice, a certain Semyon had not yet arrived at the camp, but he came to spy on me and even groped me a little."
                "That's the kind of publicity I should be paying for!"
                "It's like, 'Semen's coming! Girls are hiding!'"
                hide dv with dissolve
            else:
                "Even if the girls suddenly start making eyes at me, I'm not going to throw the game to any of them."
                "I imagine the red-headed bitch will carry out her threats."
                scene bg ext_square_sunset
                show prologue_dream
                with fade
                "For example, at the morning lineup."
                show dv grin pioneer behind prologue_dream with dissolve
                "She comes forward, smugly winks at me, and says at the top of her voice:"
                dv "{i}Olga Dmitrievna, may I report?{/i}"
                "And so on."
                "A collective trial, and with it, disgrace, is assured for me."
                dreamgirl "And here's the correct translation of your verbiage: I'm shaking for my skin."
                dreamgirl "To fear the wolves is not to walk in the woods, you know?"
                th "I'm just as fine in the city."
                th "Let the wolves go to the hunters."
        scene bg int_dining_hall_sunset with dissolve

    elif alt_my_rival_1_tour.take == 'sl':
        "Slavya jumped up abruptly and propped her fists on the table."
        show sl serious pioneer with dspr
        sl "And you're a serious adversary."
        "She frowned at me."
        show sl angry pioneer with dspr
        sl "Remind me never to underestimate you!"
        me "Many who underestimated Semyon bitterly regretted it!"
        "I played along."
        show sl smile2 pioneer with dspr
        "Then she couldn't stand it and smiled, spoiling the whole scene."
        sl "And the round was really interesting!"
        if lp_sl >= 6 and not alt_day2_detour_semifinal:
            menu:
                "Wanna go again?":
                    $ karma += 5
                    show sl smile pioneer with dspr
                    sl "Thanks"
                    $ lp_sl += 1
                    show sl laugh pioneer with dspr
                    extend ", but… No!"
                    sl "Let's see you show some class yourself!"
                    "The girl patted me on the shoulder and headed for the cheering camp."
                    hide sl with dissolve
                    jump alt_day2_semifinal_new
                "Do nothing":
                    pass
        else:
            pass
        "I smiled."
        me "Thanks for the game!"
        sl "Thank you!"
        hide sl with dissolve
        "Nodding to me, she got up and walked over to Olga Dmitrievna, and they had a lively conversation there."

# ====================================================== Пропускаем часть диалога, если "выиграли" 1 тур скипом
        if not alt_day2_detour_semifinal:
            "Well, it was a hard fight, but I won."
            th "The perfect confrontation, however, is a game in which you both understand nothing."
            dreamgirl "Well, yes, well, yes."
            "Mumbled the inner voice."
            dreamgirl "Your fit is mid, and you get zero bitches."
            th "Shut up. You don't understand anything."
            th "It's a matter of individual prestige. I'll move on to the finale."
            if alt_result_dv_1_tour == 4:                                                       # Дваче в другом полуфинале
                th "And I'll road roll the ginger boor up there!"
            elif alt_result_dv_1_tour == 3:                                                     # Дваче в 1/2 к Семёну
                th "And I'll roll anyone out of out there!"
            elif alt_result_dv_1_tour == 2:                                                     # Дваче слетела в 1 туре
                th "What can't be said for Alisa. So it's going to be an easy win."
            dreamgirl "Hopes... Dreams... Fantasies..."
            th "Are you doubting me?!"
            dreamgirl "No, no, no, no, what do you mean! {w}I believe in you! I know your potential."
            th "You see!"
            dreamgirl "You'll fall off halfway through."
            th "Come on!"
            if alt_result_dv_1_tour == 4:                                                                # Дваче в другом полуфинале
                "Maybe it's {i}her{/i} who's going to lose halfway through!"
                "She's going to lose."
                dreamgirl "Hopes... Dreams..."
                th "You're repeating yourself."
                dreamgirl "You're just being too high-minded. {w}And as the Great Ones say, a true master is without pride."
            elif alt_result_dv_1_tour == 3:                                                              # Дваче в 1/2 к Семёну
                th "By the way, we're about to have a chance to shackle Redhead in the semifinals."
                dreamgirl "Yeah, well, we're the lucky ones."
                dreamgirl "But you'd better get ready for a stern test - she's not just going to give you the win!"
            elif alt_result_dv_1_tour == 2:                                                              # Дваче слетела в 1 туре
                "I grinned."
                th "And even if I do."
                th "I'll draw your attention to the fact that while we were bickering, Dvachevskaya was out in the very first round."
                "I took off my imaginary hat and pressed it to my chest."
                me "Rest in piss!"
                show dv angry pioneer2 far at left with dissolve
                "Dvachevskaya grinned, but said nothing."

    elif alt_my_rival_1_tour.take == 'dv':
        show dv sad pioneer2 with dspr
        "Aliska screwed up."
        "Ha. Ha. Ha."
        "Her look is something no MasterCard and Visa can buy."
        "A truly priceless sight!"

# ====================================================== Пропускаем часть диалога, если "выиграли" 1 тур скипом
        if not alt_day2_detour_semifinal:
            if lp_dv >= 6:
                menu:
                    "So, how'd you like that, huh?":
                        $ karma += 5
                        if loki or herc:
                            $ lp_dv += 1
                            show dv rage pioneer2 with dspr
                            "Alice sulked, sulked..."
                            me "Dismembered like Allah screwed the turtle!"
                            "I wouldn't be surprised if she came up with something else nasty now, just to hurt me."
                            show dv angry pioneer2 with dspr
                            "But she surprised me."
                            show dv laugh pioneer2 with dspr
                            dv "You're pretty good! Good!"
                            "She laughed, poking me in the shoulder with her fist."
                            dv "I guess we'll consider our wager closed."
                            th "Phew."
                            "I suppressed the urge to wipe my forehead in relief."
                            show dv grin pioneer2 with dspr
                            dv "Or if you want, can we bet on something else?"
                            "I recoiled."
                            "But tried to answer solidly:"
                            me "No. {w}You've already put your naturelle on the line."
                            dreamgirl "Only maiden's honor next! {w}Will you say it out loud?"
                            "Yeah, right this fucking instant. My 'naturelle' came out in a shaky voice."
                            show dv laugh pioneer2 with dspr
                            "Alisa laughed again, seeing my reaction, and stood up."
                            show dv smile pioneer2 with dspr
                            dv "Good luck to you."
                        else:
                            "I began, and, feeling the fervor wane, I continued more calmly:"
                            me "I think I've won."
                            dv "Uh-huh."
                            me "And you are now..."
                            show dv sad pioneer2 with dspr
                            pause(.4)
                            show dv guilty pioneer2 with dissolve
                            dv "Yes..."
                            dv "I won't say anything to anyone. {w}You're the winner."
                            "Alisa looked depressed and kind of... Baffled, or something."
                            "It wasn't so much the loss that seemed to embarrass her, but my reaction to it."
                            dv "Okay, bye."
                        hide dv with dissolve
                        jump alt_day2_1_tour_end
                    "I guess that's it":
                        hide dv with dissolve
                        "Alisa nodded and silently got up from the table."
                        pass
            else:
                pass
        if alt_day2_dv_ultim == 1:
            "I think I just successfully solved my little betting problem."

    elif alt_my_rival_1_tour.take == 'mi':
        show mi surprise pioneer with dissolve
        mi "Ow!"
        "She put her hands to her mouth."
        mi "I what, I lost, didn't I? Because I never figured out what to do here, all I did was snatch cards from you and not give you mine."
        show mi upset pioneer with dspr
        "She shook her head."
        mi "Some incomprehensible game."
        show mi smile pioneer with dspr
        mi "But still, thanks for playing with me!"
        if lp_mi >= 6 and not alt_day2_detour_semifinal:
            menu:
                "Maybe you wanna go for another round?":
                    $ karma += 5
                    $ lp_mi += 1
                    "I enjoyed just sitting at the same table with her."
                    "Especially since no one was looking at us anyway."
                    "The attention of the audience was focused on the main actors of tonight - Alisa and Ulyana."
                    me "Shall we?"
                    show mi shy pioneer with dspr
                    mi "Is that allowed?"
                    me "No, but... Who cares?"
                    show el serious pioneer at left with dissolve
                    show mi surprise pioneer with dspr
                    el "I care!"
                    "Electronik, who appeared out of nowhere, replied."
                    el "You win, you're welcome at the semifinal table!"
                    hide el with dissolve
                    "Shit."
                    "My smile came out apologetic."
                    me "See you then."
                "I'd be right happy to":
                    "I smiled."
                    me "If you ever want to play again, come to me!"
            hide mi with dissolve
            "Miku nodded and got up from the table."
        else:
            "I smiled."
            me "You're welcome!"
            mi "I'll go, okay? I want to see you win! You're going to win, aren't you? I'll be really, really rooting for you!"
            "Unable to contain my smile, I nodded."
            me "Of course I will."
            mi "Then good luck next time!"
            hide mi with dissolve
            "She left."

# ====================================================== Пропускаем часть диалога, если "выиграли" 1 тур скипом
        if not alt_day2_detour_semifinal:
            "I can't say I had to work hard."
            "It sounded like pure luck to me."
            "Although, of course, my karma and luck are antonyms."
            "I'm the walking embodiment of Murphy's Law."
            dreamgirl "Yeah, well, yeah. {w}And the fact that you pulled a ticket not even for a million, but for a new life, we kind of don't take that into account, do we?"
            th "You mean getting into the camp?"
            th "I can't call it luck in the literal sense of the word."
            dreamgirl "What else would you call it?"
            th "Well... Just being in the wrong place at the wrong time."
            dreamgirl "And got a mouthful of youth, summer, and sexy pioneers."
            th "You know, I don't believe when a lot is good. {w}There's got to be a catch somewhere."
            dreamgirl "And what is it this time?"
            th "Well, for example, it could be that the transfer to the camp is a side effect of being hit by the cosmic energy beam."
            th "Or it could even be the secret service testing the teleporter prototype, and something went wrong in their settings."
            dreamgirl "I don't know what you're consuming, but sprinkle me some."
            if alt_day2_dv_ultim == 1:
                dreamgirl "Besides, you have an erotic bet here, remember?"
                if alt_result_dv_1_tour == 4:                                                                   # Дваче в другом полуфинале
                    th "I remember, I remember."
                    th "But this bet has every chance of resolving itself completely on its own."
                    dreamgirl "The hopes of the young men are nurtured..."
                    th "Aren't they science?"
                    dreamgirl "In your case it's actually hopes."
                    dreamgirl "Rest assured, she'll get to you and tear you to shreds and then carry out her threat."
                    th "Oh, thank you, you gloomy nerd."
                elif alt_result_dv_1_tour == 3:                                                                 # Дваче в 1/2 к Семёну
                    th "As if I'll be able to forget here."
                    "Judging by the schedule, my opponent in the semifinals is just Dvachevskaya."
                    dreamgirl "That's lucky!"
                    dreamgirl "Let's hurt her!"
                elif alt_result_dv_1_tour == 2:                                                                 # Дваче слетела в 1 туре
                    "That would even be ridiculous."
                    th "A bet? What bet?"
                    th "While we were judging our luck here, Aliska got kicked out on the first round."
                    "I took off my imaginary hat and pressed it to my chest."
                    me "Rest in piss!"
                    show dv angry pioneer2 far at left with dissolve
                    "Dvachevskaya grinned, but said nothing."

    elif alt_my_rival_1_tour.take == 'us':
        show us sad pioneer with dspr
        us "You can't do that, I just started playing around!"
        me "Me too. {w}You lost, I won. All's fair."
        play music music_7dl["genki"] fadein 3
        us "We'll replay it! Only you give in now, do you hear?"
        us "I have to win and take the grand prize!"
        show us angry pioneer with dspr
        us "You must lose! Must! Got it!"
        "A little more and I'll start laughing my head off, that's how funny it looked."

# ====================================================== Пропускаем часть диалога, если "выиграли" 1 тур скипом
        if not alt_day2_detour_semifinal:
            if alt_day2_us_escape:
                us "Oh is that so! Then I'll... I'll run away again tomorrow, got it!"
                us "And peel your own potatoes then! For the whole camp!"
                "Now that was a bigger threat, I didn't feel like being on canteen duty alone."
            else:
                us "Ah is that so! Then I'll tell everyone about you and Dvachevskaya!"
                if (alt_day2_dv_ultim == 1) and (loki or herc):
                    me "You little brat, don't you dare! It's our bet, you've only been breaking it up!"
                    show us grin pioneer with dspr
                    "Ulyana only smiled."
                else:
                    me "Are you going to tell everyone what she promised to tell? In case I lose?"
                    "She nodded."
            if herc or loki:
                me "Don't you want some hot chocolate?"
                show us surp1 pioneer with dspr
                us "What?"
                me "I say you can do as you want, but you lost."
                show us dontlike pioneer with dspr
                me "And card debt is sacred. That's it, get out of here, I'm going to win."
                "She pouted, but she did as I said."
                hide us
                with flash_red
                "True, in passing she stepped on my foot - let her."
                stop music fadeout 3
                "I was feeling generous and forgave her this little prank."
            if dr:
                me "Okay."
                "I sighed."
                me "Deal. I'll give you one more chance."
                show el serious pioneer at left with dissolve
                "Her screams caught Electronik's attention."
                el "No rematches!"
                el "One match, game to two wins, loser eliminated."
                "Ulyana threw an unmistakable look at Electronik, signifying trouble ahead for him."
                stop music fadeout 3
                "But at least she diverted her attention from me, and I breathed a sigh of relief."
        else:
            me "Do as you please, but you lost."
            me "And card debt is sacred. That's it, get out of here, I'm going to win."
            "She pouted, but she did as I said."
            hide us
            with flash_red
            "True, in passing she stepped on my foot - let her."
            stop music fadeout 3
            "I was feeling generous and forgave her this little prank."
        play music music_list["my_daily_life"] fadein 5

    elif alt_my_rival_1_tour.take == 'sh':
        "Shurik was out of luck."
        "But he seemed more interested in the process of testing new rules and algorithms than in winning."
        "A true fanatic of his cause."
        show sh normal pioneer with dissolve
        sh "You're very good at adapting to the new rules of the game."
        "He praised."
        hide sh with dissolve
        "And, shaking my hand, left."


# ====================================================== Пропускаем часть диалога, если "выиграли" 1 тур скипом
        if not alt_day2_detour_semifinal:
            "Probably off to invent another wild thing or to write an essay about it in the wall newspaper."
            "I was surprised to find Shurik and Slavya very much alike."
            "Both passionate about their work, both wildly responsible."
            "And both hardly ever rest."
            th "I probably should've gave in to him, idiot, I'll find a way to stretch my thighs anyway, and he looks like he's about to go back to sit in the club."
            "That way the summer will go by and he'll still be pale."
            dreamgirl "Hey!"
            th "What?"
            dreamgirl "What's that nasty stuff you've got there? {w}Conscience? {w}Throw it away immediately."
            dreamgirl "Always picking up crap from the floor."
            if alt_day2_dv_ultim == 1:
                th "What is it?"
                dreamgirl "A reminder that we don't just sit around here sitting around for nothing."
                dreamgirl "We have one goal! To show one redheaded terrorist what a word is worth!"
                if alt_result_dv_1_tour == 4:                                                           # Дваче в другом полуфинале
                    dreamgirl "And the special educational moment is that we'll wash her in the game by her own rules!"
                    th "If she loses at another table, we won't wash anyone."
                    dreamgirl "I have a suspicion that people like her don't give up so easily."
                    th "Well, if we meet in the finals, I'll beat her."
                    dreamgirl "You can't beat anyone with that attitude. {w}Come on!"
                elif alt_result_dv_1_tour == 3:                                                         # Дваче в 1/2 к Семёну
                    th "Yeah, we'll show her right now."
                    dreamgirl "Great! The reckoning was a lot closer than I thought it would be!"
                    if alt_day2_us_escape:
                        dreamgirl "She asked to resist her a bit, go on, fulfill her request."
                elif alt_result_dv_1_tour == 2:                                                         # Дваче слетела в 1 туре
                    "To be honest, it was a little late for grading words."
                    "I looked at the table of participants - Alisa was out after the first game."
                    th "Just {w=.3}your{w=.2} luck."
                    th "Rest in peace, dear bandit."
                    th "I will avenge you."
            else:
                th "What's wrong with that?"
                dreamgirl "That conscience breeds doubt, and doubt leads to defeat."
                th "I'm aware of that."
                th "But do I need to win?"
                dreamgirl "And next you'll start babbling nonsense about «it's all about participation»."
                "Snorted the inner voice."
                th "I'll say it's Allah's will."

    elif alt_my_rival_1_tour.take == 'mz':
        show mz normal glasses pioneer with dissolve
        "Beetle's reaction amused me."
        mz "Hallelujah!"
        show mz angry glasses pioneer far with dspr
        pause(0.5)
        hide mz with moveoutleft
        "With a slam on the table, she got up and disappeared."
        "She must have rushed off to her best friends, the books."
        "That's who doesn't need much to be happy."

# ---------------------------------------------------- \\ Диалоги


# -------------------------------------------------------------------------
label alt_day2_1_tour_end:
# ЕСЛИ НЕ Славя, Мику или Шурик ИЛИ при скипе — итоги после диалогов
    if (alt_my_rival_1_tour.take not in ['sl','mi','sh']) or alt_day2_detour_semifinal:
        scene bg int_dining_hall_sunset with dissolve
        "The first round was over."
        "The situation, meanwhile, was as follows:"
        call alt_day2_1_tour_analizer                                                     # вызываем анализатор 1 тура
        $ renpy.block_rollback()                                                          # блокируем роллбак
    scene bg int_dining_hall_sunset with dissolve
    stop music fadeout 3
# -------------------------------------------------------------------------

    "Anyway, that's all lyricism."
    jump alt_day2_semifinal_new                                             # переход в полуфинал

#-------------------------------------------------------------------------------------------------
label alt_day2_semifinal_new:
    stop music fadeout 1
    scene bg int_dining_hall_sunset with dissolve
    show el smile pioneer at left with dissolve
    play music music_list["get_to_know_me_better"] fadein 2
    el "So!"
    "Electronik, clearly proud of his role as master of ceremonies, spoke up."
    el "The first round is over, the winners meet in the second round!"

    $ alt_tournament_state = "semifinal_start"                                                      # устанавливаем начало полуфинала
#-------------------------------------------------------------------------------------------------
    if alt_day2_result_tour != 1:                                                                       # если не продули в 1 туре
        $ alt_day2_my_win = alt_day2_rival_win = alt_day2_game_played_out = 0                           # обнуляем результат игр
        $ alt_my_rival_semifinal = alt_get_me_rival(alt_day2_gamblers_semifinal)                        # узнаём своего соперника

        $ alt_name_my_rival_i = alt_my_rival_semifinal.name['i']                                        # узнаём ИМЯ своего соперника (в именительном падеже)
        $ alt_name_my_rival_r = alt_my_rival_semifinal.name['r']                                        # узнаём ИМЯ своего соперника (в родительном падеже)
        $ alt_name_my_rival_d = alt_my_rival_semifinal.name['d']                                        # узнаём ИМЯ своего соперника (в дательном падеже)
        $ alt_name_my_rival_v = alt_my_rival_semifinal.name['v']                                        # узнаём ИМЯ своего соперника (в винительном падеже)
        $ alt_name_my_rival_t = alt_my_rival_semifinal.name['t']                                        # узнаём ИМЯ своего соперника (в творительном падеже)

        $ alt_spr_my_rival = alt_my_rival_semifinal.take                                                # получаем спрайт соперника — заголовок
        $ alt_emo_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][0]                         # эмоция (строка)
        $ alt_acc_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][1]                         # аксессуар (строка)
        $ alt_clot_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][2]                        # одежда (строка)
        $ alt_pos_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][3]                         # положение

        $ alt_nick_my_rival = alt_my_rival_semifinal.nick                                               # получаем характер соперника (для диалога)

        if alt_my_rival_1_tour.take == 'un':
            hide el with dissolve
            "Lena stood modestly on the sidelines and watched the events of the tournament."
            show un smile2 pioneer far at right with dissolve
            "There was no anger or resentment or anything like that on her face."
            "On the contrary, she was genuinely supportive of me and the other guys."
            hide un with dissolve
            "Well, after making sure I didn't offend her, I relaxed a little."
    "Meanwhile, the names of the participants in the second round have already appeared in the table."
    call show_tournament_table                                                                      # "показали таблицу"
    $ alt_mstt = 0
    if alt_day2_result_tour != 1:                                                                       # если не продули в 1 туре
        $ places_my_table = alt_get_my_table(alt_day2_gamblers_semifinal)                               # Стол Семёна = [место Семёна, место соперника, № их стола]
    else:                                                                                               # продули в 1 туре
        $ alt_table_no = 5
    "And if this table is to be believed, four players meet in the semifinals."
    $ alt_random_box_1 = range(1,len(alt_table_affiliation)+1)                                      # черный ящик — список от 1 до длины представлений столов +1
    while alt_table_no <= 6:                                                                        # перебираем столы от 5 по 6
        $ sitting_at_table,gambler_upper,gambler_lower,must_taunt = alt_declare_tournament_tables(alt_table_no)  #расссадка, игроки, таунты — по номеру стола
        "%(sitting_at_table)s"
        call show_tournament_table
        extend " %(gambler_upper)s"                                                                 # выводим в окно имя верхнего игрока
        call show_tournament_table
        extend " and %(gambler_lower)s."                                                              # выводим в окно имя нижего игрока
        if must_taunt != None:                                                                      # если таунт есть
            "%(must_taunt)s"                                                                        # выводим его
        if alt_day2_result_tour != 1:                                                                       # если не продули в 1 туре
            if alt_table_no != places_my_table[2]:                                                          # если номер стола — НЕ свой
                $ alt_day2_gamblers_semifinal[2*(alt_table_no-4)-renpy.random.choice([1,2])].winner = True  # тогда один из игроков (рандомно) — победитель в этапе
                $ renpy.block_rollback()
        $ alt_table_no += 1
    if (alt_day2_detour_number != 0):                                                               # если выбрали конкретного соперника для финала
        $ alt_day2_gamblers_semifinal[2].winner = False                                             # его соперник в полуфинале проигрывает
        $ alt_day2_gamblers_semifinal[3].winner = True                                              # а он сам выигрывает в полуфинале

    if alt_day2_result_tour == 1:                                                               # если продули в 1 туре
        scene bg int_dining_hall_sunset with joff_r
        $ alt_tournament_state = "semifinal_end"                                                # устанавливаем конец полуфинала
        $ alt_drawing_of_detour_semifinal()
        $ renpy.fix_rollback()                                                                  # фиксируем выбор — "откатом" поменять будет нельзя
        jump alt_day2_semifinal_detour                                                          # и переходим в конец проигрыша в 1/2

    pause (0.3)
    scene bg int_dining_hall_sunset with dissolve


# ---------------------------------------------------- ДИАЛОГИ
    if alt_my_rival_semifinal.take == 'un':
        show un shy pioneer with dspr
        me "Good luck to both of us?"
        show un smile pioneer with dspr
        pause(.3)
        show un shy pioneer with dspr
        un "Y-yes..."
        "She tried to smile, but immediately mingled again and became silent."

    elif alt_my_rival_semifinal.take == 'sl':
        show sl smile pioneer with dspr
        sl "Ugh! I didn't think I'd get this far!"
        "Slavya smiled."
        me "That doesn't mean I'm going to give in to you now!"
        show sl laugh pioneer with dspr
        sl "And don't!"
        "The girl laughed."
        sl "May the best win!"

    elif alt_my_rival_semifinal.take == 'dv':
        "The sneer and mischief in Alisa's gaze did not bode well for me."
        show dv grin pioneer2 with dspr
        dv "I made up a new rule."
        "She whispered, leaning toward me."
        me "What other rule?"
        dv "If you beat me now, but lose in the finals, I'll still tell everyone."
        me "Hey, that's not fair!"
        show dv laugh pioneer2 with dspr
        dv "Though you won't win."
        "The girl laughed."
        dv "You're finished!"

    elif alt_my_rival_semifinal.take == 'mi':
        stop music fadeout 2
        show mi normal pioneer far with dissolve
        "RNGesus sent me Miku as an opponent."
        play music music_7dl["tellyourworld"] fadein 3
        show mi normal pioneer with dspr
        "The pioneer girl took a seat across the street and asked:"
        show mi upset pioneer with dspr
        mi "Say, Senechka, what size are you?"
        "I gasped for air."
        dreamgirl "Well, don't be so shy! The girl {b}wants{/b} to know!"
        th "These are not things that should be discussed in public."
        dreamgirl "Where else? A pioneer girl is lonely and wants warmth and affection."
        th "Do you think of anything else at all?"
        dreamgirl "I do, of course, but this is more interesting!"
        me "I don't..."
        show mi happy pioneer with dspr
        mi "You don't know? That's okay. I have everything I need at the club."
        mi "We'll take the measurements after the tournament. And when we're done, we can play guitars!"
        if not ('music' in list_joined_clubs_7dl):
            show mi smile pioneer with dspr
            mi "You know how to play, right?"
            show mi grin pioneer with dspr
            extend " If not, I'll teach you!"
        dreamgirl "You'll definitely like it, go for it!"
        dreamgirl "She'll gently take your fingerboard in one hand and the kapodaster in the other..."
        dreamgirl "And raise your voice to a higher pitch!"
        show mi shocked pioneer with dspr
        mi "Oh, Senechka, you're suddenly so red. Are you hot? Or is it bad? Shall I call nu…"
        show mi scared pioneer with dspr
        me "Don't!" with vpunch
        "Wonderful. Scared the girl and screeched like a rooster all over the canteen."
        dreamgirl "Being a living failure is your destiny."
        "After exhaling, I tried again, calmer now."
        show mi surprise pioneer with dspr
        me "I'm sorry I yelled. There's nothing wrong with me."
        show mi smile pioneer with dspr
        mi "It's okay, Senechka. I understand everything."
        "Do you really understand?"
        "I'm lucky Miku is so resilient."
        dreamgirl "Just to clarify - are you really going to trade in the young and soft for the gray and dull?"
        th "How do you think?"
        $renpy.notify('…degenerate, holy fucking shit!')
        dreamgirl "You really are a…" # дегенерат, пиздец просто!
        me "If you find me after the tournament, I'll go to the club with you."
        show mi grin pioneer with dspr
        mi "Great! You'll be the prettiest at the disco!"
        "Disco? What does disco have to do with it?"
        dreamgirl "They want to make a shirt that fits you, you dummy."
        th "Why didn't you tell me right away, Stirlitz?"
        dreamgirl "I was too far from failing."
        dreamgirl "Just don't screw it up yourself when you pose for the young maiden naked."
        show mi smile pioneer with dspr
        stop music fadeout 2
        me "Ahem... Let's start the game already."
        play music music_list["get_to_know_me_better"] fadein 3

    elif alt_my_rival_semifinal.take == 'us':
        stop music fadeout 2
        show us grin pioneer with dissolve
        us "Will you give in, will you?"
        play music music_list["i_want_to_play"] fadein 1
        "With a smile up to her ears she stared at me."
        us "I want to beat everyone!"
        if (alt_day2_dv_ultim == 1) and (loki or herc):
            me "I won't."
            "I shook my head in the negative."
            me "We've had a bet, remember?"
            if loki or herc:
                extend " You were the witness!"
            show us sad pioneer with dspr
            us "The bet, yes, but…"
            show us grin pioneer with dspr
        us "We'll play by my rules!"
        me "What rules?"
        us "Simple!"
        me "Ahhhh! Very informative."
        us "You bet!"
        show us laugh pioneer with dspr
        "After enjoying my sour face, Ulyana began to explain."
        show us smile pioneer with dspr
        us "It's simple: you give me the good cards, and I'll give you whatever cards I want."
        me "What's in it for me?"
        us "You help the kid win and you get..."
        show us normal pioneer with dspr
        "Ulyana thought about it."
        "There don't seem to be many things the little one is willing to part with."
        us "Candy. I'll give you candy. " #(хочется написать «дружбу» или «и дружбу», но в дальнейшем это никак не проявит себя. Досадно.)
        me "Equivalent exchange…"
        show us grin pioneer with dspr
        us "Well, I'm glad we reached can…"
        show us calml pioneer with dspr
        extend " cunse…"
        show us angry pioneer with dspr
        extend " kunsexxus…"
        if herc:
            us "What are you laughing at?!"
            me "You don't want to know."
            us "I want to know."
            us "Tell me, rookie!"
            show us smile pioneer with dspr
            us "Or you'll wake up in the morning with ants under your blanket!"
            th "Impressive threat."
            me "Okay, in your ear."
            show us grin pioneer close with dissolve
            us "That's better!"
            "Ulyanka leaned toward me."
            "And when only a few centimeters remained between us..."
            with hpunch
            show us surp2 pioneer with dspr
            us "Ow!"
            show us angry pioneer with dspr
            us "You!…"
            "The little one was not bad: she did not hesitate to smash my forehead with hers." with vpunch
            "Not hard. She wouldn't have it any other way."
            "We stared at each other for a few seconds."
            show us laugh pioneer with dspr
            "And then we both couldn't help but laugh."
            me "Come on, let's play already, the counselor is staring at us."
            us "Expect ants anyway."
            th "I hope she's kidding. Or she'll forget."
        else:
            me "Consensus."
            show us dontlike pioneer with dspr
            me "Don't use complicated words, it's too early for you."
            "And why do people think that using compound words makes them smarter in the eyes of others?"
            show us upset pioneer with dspr
            us "Boo-boo-boo. Naughty."
            me "Let's play already."

    elif alt_my_rival_semifinal.take == 'sh':
        show sh normal pioneer with dissolve
        sh "It'll be a decent fight."
        "He nodded."
        me "Don't think I'm going to give in to you."
        show sh smile pioneer with dspr
        sh "And don't you get your hopes up either!"
        me "Then to arms!"

    elif alt_my_rival_semifinal.take == 'mz':
        "Seriously, how did she manage to win, with that attitude to the game?"
        show mz normal glasses pioneer with dissolve
        mz "Listen. What was your name."
        "She began."
        me "Semyon."
        mz "Yeah, right. Semyon."
        mz "Semyon, do you want me to say you won and go?"
        me "Is that allowed?"
        mt "No, you can't! Play on!"
        "The squad leader shouted from the side of the fans."
        show mz angry glasses pioneer with dspr
        "Cursing, Zhenya abandoned her plans."
# ---------------------------------------------------- /ДИАЛОГИ

# ----------------------------------------------------------------------------------------------------
    if alt_day2_detour_semifinal:                                           # если пропуск полуфинала
        scene bg int_dining_hall_sunset with dissolve2
        pause(1.0)
        if not alt_day2_detour_final:                                       # Если НЕ пропуск финала
            jump alt_day2_semifinal_fail_end_new                            # на поражение в 1/2 финала
        elif alt_day2_detour_final:                                         # Если выбрано "проиграть в финале"
            jump alt_day2_semifinal_win_end_new                             # на победу в 1/2 финала

# ----------------------------------------------------------------------------------------------------
label alt_day2_semifinal_start_new:                                                     # начало полуфинала
    call alt_day2_stipulation_new                                                       # определяемся, кто первый ходит

    # первоначальные "настройки" игроков — могут меняться по результатам игры
    # 'defense' — защита, 'gamble' — риск, 'succumb' — слив, 'foolplay' — рандом
    # вероятность ошибки: 1 = 80%, …, 4 = 20%, 5 — ошибок нет.

    if alt_my_rival_semifinal.take == 'un':                                                    # Лена
        if alt_day2_dv_ultim != 1:                                                              # если с Алисой не спорить
            $ alt_day2_gambler_behavior = 'gamble'                                              # пытается рискнуть
            $ alt_day2_gambler_skill = 3                                                        # правда, ошибок многовато — 40%(3)
        else:
            $ alt_day2_gambler_behavior = 'succumb'                                             # Если поспорить — то также игра в поддавки
            $ alt_day2_gambler_skill = 4                                                        # может ошибиться  — 20%(4)
    elif alt_my_rival_semifinal.take == 'sl':                                                  # Славя будет защищаться, ошибок — 20%(4)
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 4
    elif alt_my_rival_semifinal.take == 'dv':                                                  # Алиса рискует, ошибок — 20%(4)
        $ alt_day2_gambler_behavior = 'gamble'
        $ alt_day2_gambler_skill = 4
    elif alt_my_rival_semifinal.take == 'mi':                                                  # Мику будет защищаться, ошибок — 20%(4)
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 4
    elif alt_my_rival_semifinal.take == 'us':                                                  # Ульяна будет защищаться по-своему
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 3                                                            # ошибок — 40%(3)
    elif alt_my_rival_semifinal.take == 'sh':                                                   # Шурик экспериментирует, так что может и рискнуть, и защищаться, и слить; ошибки 20%(4)
        $ alt_day2_gambler_behavior = renpy.random.choice(['defense', 'gamble'])                # у него своя кухня — набор из возможных вариантов
        $ alt_day2_gambler_skill = 4
    elif alt_my_rival_semifinal.take == 'mz':                                                  # Женя играет рандомно, как в классике, ошибки = 5
        $ alt_day2_gambler_behavior = 'foolplay'
        $ alt_day2_gambler_skill = 5

label alt_day2_semifinal_re_game:                                                           # игра в полуфинале — сюда возвращаемся на повторную игру
    $ alt_my_poker_hand = None
    $ alt_rival_poker_hand = None

    if alt_day2_walk == 1:
        $ VISIBLE = True
        $ INVISIBLE = True
    else:
        $ VISIBLE = True
        $ INVISIBLE = False

    python:
        dialogs = {
                        (0, 'win','jump'):'alt_day2_one_play_win_new',
                        (0, 'fail','jump'):'alt_day2_one_play_fail_new',
                        (0, 'draw','jump'):'alt_day2_one_play_draw_new'
                    }
        generate_cards_alt('bg hall', dialogs)


# ****************   НОВЫЕ  СОПЕРНИКИ   ******************************************

        if alt_my_rival_semifinal.take == 'un':
            rival = CardGameRivalWiseUsual(un_avatar_set, u"Лена", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_semifinal.take == 'sl':
            rival = CardGameRivalWiseUsual(sl_avatar_set, u"Славя", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_semifinal.take == 'dv':
            rival = CardGameRivalWiseUsual(dv_avatar_set, u"Алиса", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_semifinal.take == 'mi':
            rival = CardGameRivalWiseUsual(mi_avatar_set, u"Мику", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_semifinal.take == 'us':
            rival = CardGameRivalWiseLikeUS(us_avatar_set, u"Ульяна", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_semifinal.take == 'sh':
            rival = CardGameRivalWiseUsual(sh_avatar_set, u"Шурик", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_semifinal.take == 'mz':
            rival = CardGameRivalWiseUsual(mz_avatar_set, u"Женя", alt_day2_gambler_behavior, alt_day2_gambler_skill)

# ************************************************************************************

    $ alt_hint_poker = alt_hint_poker_contractual                                           # подсказки комбинаций — по просмору правил
    jump cards_gameloop_wise_alt                                                            # переход карточный стол

#-------------------------------------------------------------------------------------------------
label alt_day2_semifinal_fail_end_new:
    $ alt_day2_result_tour = 11                                                 # Семён проиграл в полуфинале
    $ persistent.altCardsWon1_new = True

    $ alt_day2_gamblers_semifinal[places_my_table[1]].winner = True            # соперник выиграл
    $ alt_rival_final = alt_day2_gamblers_semifinal[places_my_table[1]]         # и он выходит в финал
    $ alt_day2_gamblers_semifinal[places_my_table[0]].winner = False            # Семён проиграл
    $ alt_tournament_state = "semifinal_end"                                   # устанавливаем конец полуфинала
    scene bg int_dining_hall_sunset with dissolve
    call alt_day2_summary_poker_round

# ---------------------------------------------------- ДИАЛОГИ;
    if alt_my_rival_semifinal.take == 'un':
        $ lp_un += 1
        stop music fadeout 2
        if alt_day2_dv_ultim == 1:
            show un serious pioneer at center with dissolve
            un "And why did you do that?"
            play music music_7dl["areyouabully"] fadein 3
            "She asked, looking at me with obvious dislike."
            me "Excuse me?"
            un "You think I haven't heard about your little 'bet' with Alisa?"
            un "You should've won!"
            if alt_day2_walk == 1:
                th "Yeah, I was planning to. I even marked the cards. But..."
            th "It didn't work out."
            me "What can I say now? I lost, you won. Have a good evening."
            "Especially since we don't negotiate with terrorists."
        else:
            show un angry pioneer with dissolve
            un "You gave in, didn't you?"
            play music music_7dl["areyouabully"] fadein 3
            "Lena tilted her head sideways and glared at me with a distasteful look."
            un "Instead of playing normally, you were playing a giveaway."
            me "You imagined it."
            "I grinned."
        un "Please allow us to play again!"
        "In the ensuing silence, Lena asked."
        un "My opponent was giving in."
        show dv grin pioneer2 far at fleft with dissolve
        dv "If he gave in, he's the fool."
        "Alisa snorted."
        "Yeah, well, she knows what's at stake."
        show un angry2 pioneer with dspr
        un "And you should keep quiet! It's all because of you! Again!"
        stop music fadeout 3
        show un sad pioneer with dspr
        "She hid her face in her palms, and I rose from the table, feeling like a rocket stage that had launched another shuttle into orbit."
        hide dv
        hide un
        with dissolve
        pause(0.3)
        play music music_list["get_to_know_me_better"] fadein 1

    elif alt_my_rival_semifinal.take == 'sl':
        show sl normal pioneer with dissolve
        sl "Once again I'm being forced to do things I don't understand."
        me "Excuse me?"
        th "Is she rambling or something?"
        show sl serious pioneer with dspr
        "Slavya brushed it off."
        sl "Don't mind me, just thinking out loud."
        me "I see. Well, good luck in the finals, then!"
        sl "Right."
        show sl sad pioneer with dissolve
        sl "Why did I even agree to play?"
        me "You don't like cards?"
        sl "No. I like other games."
        "She wrinkled her nose like she'd eaten something sour."
        "And I went up - I had the excitement of rooting for the finalists waiting for me."

    elif alt_my_rival_semifinal.take == 'dv':
        if alt_day2_dv_ultim == 1:
            show dv grin pioneer2 with dspr
            dv "Do you think it would be better if I announced it myself from the podium?"
            "Alisa gloated like I was her blood enemy with the five knees tradition."
            dv "Or would it be better to get you to the podium with me?"
            if alt_day2_walk == 1:
                th "You better explain to me how the hell do you know {i}my{/i} markings."
            me "It won't work."
            show dv surprise pioneer2 with dspr
            dv "Why?"
            me "Because if you get me out on stage, no one would ever believe that I had the strength to handle you and - what were you saying?"
            show dv laugh pioneer2 with dspr
            dv "Yes. Well..."
            "The thought occurred to her."
            dv "I'll say you tied me up."
            me "With tights!"
        "Alisa laughed merrily, and I got up."
        "God, why are all bitches so redheaded?"
        "Do I really have 'mock here' written somewhere?"
        me "Go play. You've got the finals waiting for you."
        me "And if you lose, shame on you."
        "I turned around and left for the fans."

    elif alt_my_rival_semifinal.take == 'mi':
        show mi happy pioneer with dspr
        mi "Yay! I'm winning again!"
        mi "I'm, I'm... I'm super-Miku!"
        me "Oh my God, where did you dig up this miracle?"
        "I mumbled."
        show mi smile pioneer with dspr
        mi "I want to celebrate my victory with some very good thing or even a deed, but I can't think of anything, maybe you, Senechka, can give me some advice?"
        "Machine-gun girl."
        th "At times we inevitably had cards thrown on the line, but the suits were wrong..."
        th "Honey, honey, stop yapping, I didn't do anything wrong to you, why are you shooting me up here!"
        me "I don't know."
        "Sullenly I replied."
        "Defeat's got me a little rattled."
        show mi happy pioneer with dspr
        mi "Oh, I know, I think! Yes! I just had an idea! I'll..."
        show mi happy pioneer far with dissolve
        "She climbed up on the table."
        mi "I'll sing to you!"
        "She took a breath, and..."
        show dv angry pioneer2 at cleft with easeinleft
        show mt angry pioneer at cright with easeinright
        with vpunch
        "Unbeknownst to me, Olga and Alisa, roaring in unison, rushed to drag her to the floor."
        "With a grin, I got up from the table and walked away to the fans."

    elif alt_my_rival_semifinal.take == 'us':
        if (alt_day2_dv_ultim == 1) and (loki or herc):
            show us laugh pioneer with dissolve
            us "Hooray-hooray-hooray, it's a beautiful game! I'm handsome and smart and agile and strong!"
            "She shouted."
            me "Do a flip flop out of joy."
            th "Why does she like the fact that now I'm getting booed by the whole camp?"
            me "I didn't know your idol was Winnie the Pooh and his shouting."
            us "What about it!"
            if alt_day2_us_escape:
                us "I've got a bear, too!"
                "She showed her tongue."
                us "But not recognizing the best ghost in the world... shame on you!"
        hide us with dissolve
        "I grimaced and stood up."
        us "Hello to losers."
        "She shouted at my back."
        "And I didn't react. Got used to it."

    elif alt_my_rival_semifinal.take == 'sh':
        show sh normal pioneer with dissolve
        sh "It's a shame it ended so quickly."
        "With dignity Shurik nodded."
        sh "It would be idael, if we'd been given ten games with the same deck so we could figure out the logic."
        me "And sit here till morning?"
        me "I don't mind, but who's going to let us."
        "I nodded and got up from the table."

    elif alt_my_rival_semifinal.take == 'mz':
        show mz normal glasses pioneer with dissolve
        mz "Oops."
        "She muttered to herself."
        mz "I didn't open the cards on purpose. Is it even possible to lose here?"
        me "As you can see."
        "I said and got up from the table."
# ---------------------------------------------------- \\ Диалоги

label alt_day2_semifinal_detour:
    pause(.5)
    scene bg int_dining_hall_sunset with dissolve
    "In the semifinals it was like this:"
#-------------------------------------------------------------------------------------------------
    call alt_day2_semifinal_analizer                                                  # анализ полуфинала
    $ renpy.block_rollback()                                                          # блокируем роллбак
    jump alt_day2_final_new                                 # и смотрим финал

#-------------------------------------------------------------------------------------------------
label alt_day2_semifinal_win_end_new:
    $ alt_day2_result_tour = 12                                             # Семён выиграл в полуфинале
    if not alt_day2_detour_final:                                           # если не "выигрыш" в полуфинале скипом
        $ persistent.altCardsWonRivals_new[alt_spr_my_rival] = True         # Выиграли у этого соперника

    $ persistent.altCardsWon2_new = True
    $ alt_day2_gamblers_semifinal[places_my_table[0]].winner = True             # Семён выиграл
    $ alt_rival_final = alt_day2_gamblers_semifinal[places_my_table[0]]         # и он выходит в финал
    $ alt_day2_gamblers_semifinal[places_my_table[1]].winner = False            # Соперник проиграл
    $ alt_tournament_state = "semifinal_end"                                    # устанавливаем конец полуфинала
    scene bg int_dining_hall_sunset with dissolve
    call alt_day2_summary_poker_round

# ---------------------------------------------------- ДИАЛОГИ
    if alt_my_rival_semifinal.take == 'un':
        stop music fadeout 2
        "Lena tried her best."
        play music music_list["lets_be_friends"]
        "One could see that she liked the way she was taken seriously."
        "It's just a pity that sometimes even trying your best is decidedly not enough."
        show un sad pioneer with dissolve
        un "That's a shame. I almost made it."
        "Now they're angry, and they're screaming, and they're flicking their feet, and they don't know why the people around them are so funny."
        me "Do you want a rematch?"
        show un normal pioneer with dspr
        un "Nooo, rematch wouldn't be good."
        "She sighed."
        if alt_day2_walk == 1:
            th "That's nothing, if you only knew what I beat you with..."
        me "So it's okay?"
        "She nodded."
        "What else could she have done?"
        th "And she's a gambler."
        "I noted to myself."
        th "So, if anything, you can dare her?"
        "She reminded me of someone with her impulsiveness."
        "And when I realized who it was, I shook my head for a long time, driving away foolish thoughts."
        show un shy pioneer with dspr
        un "Why are you looking so strange?"
        th "No, it can't be."
        "It's just that I've been inhaling the smells from the canteen, and I'm hallucinating."
        show un shocked pioneer with dspr
        me "Dvachevskaya!"
        "Alisa looked at me - trying to say something like 'who's speaking my name in vain' - but didn't say anything."
        hide un with dissolve
        "And I, without explaining anything else, went to the table of the local celestials."
        stop music fadeout 2
        th "I'm in for the finale!"
        "The guys at the neighboring tables weren't wasting any time either."
        play music music_list["get_to_know_me_better"] fadein 2

    elif alt_my_rival_semifinal.take == 'sl':
        show sl smile2 pioneer with dspr
        "Slavya sighed softly and smiled."
        "I didn't really understand what caused her positive reaction, but I was glad that I hadn't offended the girl with my victory."
        show sl normal pioneer with dspr
        "She rose easily from her chair and nodded to me:"
        sl "You just got here, but already won first place."
        sl "That's how legends become legends!"
        me "I haven't won anything yet..."
        show sl laugh pioneer with dspr
        sl "Don't tell me you're not aiming to win!"
        hide sl with dissolve
        "She went back to the fans."
        "And I went to the table of finalists, assessing the situation in between."

    elif alt_my_rival_semifinal.take == 'dv':
        show dv surprise pioneer2 with dissolve
        $ lp_dv += 1
        if herc or loki:
            play music music_list["that_s_our_madhouse"] fadein 3
        else:
            play music music_list["glimmering_coals"] fadein 3
        th "So, Gagarin flew, Pushkin finished."
        th "Won!!!"
        show dv sad pioneer2 with dspr
        th "And the redhead screwed up."
        "I got up from the table and cast a dismissive glance at poor Alisa."
        "She seemed to feel completely out of place."
        "Now I'm on my way to the lofty heights, where the gods themselves will be my opponents!"
        th "Not any self-righteous creeps who think I can be intimidated or confused."
        if herc or loki:
            "I winked at Dvachevskaya."
            me "Congratulations!"
            dv "What?"
            me "Happy shameful defeat to you!"
            $ lp_dv += 1
            show dv rage pioneer2 with dspr
            "I think she did swear at me."
            "I can't tell - she got so twisted that I laughed."
            th "Okay, she's done for the day."
        else:
            "I stood up in silence and headed for the finalists' table."
            "I don't have time for kindergarten fiddling with losers."
        "I went to the finalists' table, assessing the current situation in between."

    elif alt_my_rival_semifinal.take == 'mi':
        show mi sad pioneer with dspr
        "Miku was definitely upset about losing."
        "Looks like she was just starting to get the hang of the rules, and there you go."
        "Humiliating Defeat."
        "Bumped into me."

        show mi serious pioneer with dspr
        mi "Next time the victory will be mine!"

        show mi serious pioneer far with dspr
        show mi serious pioneer far at left with move
        hide mi with moveoutleft

        "She turned her nose up at the ceiling and, rising, proudly withdrew, taking her place among the losers."

        show mi grin pioneer far at fleft with moveinleft
        "Although, she spoiled the picture a little by turning around and showing me her tongue."

        show mi smile pioneer far with dspr
        pause(0.3)
        hide mi with moveoutleft

        "A cultured man, a legacy of an era..."
        me "Thanks for the game!"
        "The guys at the neighboring tables didn't waste any time either."
        "The game turned out to be quite entertaining."

    elif alt_my_rival_semifinal.take == 'us':
        show us dontlike pioneer with dissolve
        "Winning against Ulyana was easier than..."
        "Than to live through the consequences of this victory..."
        play music music_list["awakening_power"] fadein 1
        show us angry pioneer with dspr
        pause(0.3)
        "Because she suddenly leaned over the table and started pounding me with her little fists."
        "And quite strongly!" with vpunch
        us "You promised to lose!" with hpunch
        "She was so offended, like I betrayed her!"
        us "You promised! I asked you!" with vpunch
        "I wonder if she realizes she just admitted to cheating?" with hpunch
        if alt_day2_walk == 1:
            th "However, I, myself, was cheating, but..."
        me "I didn't promise anything!"
        "With difficulty I managed to get a few words in between strikes..."
        "And the only thing that wasn't clear to me..."
        th "Why isn't anyone saving me?!!" with vpunch
        th "Where is Olga Dmitrievna when you need her?!" with hpunch
        "But everyone seemed to be having so much fun watching me get killed that no one thought to stop the fun..."
        stop music fadeout 6
        "Finally, after putting the hundredth bruise on my arms and head, Ulyana panted a little and stopped beating me." with vpunch
        show us dontlike pioneer with dspr
        "But she was still dissatisfied…"
        play music music_list["i_want_to_play"] fadein 2
        "And that's putting it mildly…"
        show us angry pioneer with dspr
        us "AUUUGH!"
        "She stomped her foot fiercely." with vpunch
        us "All right, all right!"
        us "I'll remember that!"
        hide us with moveoutleft
        "And with those words, she abruptly turned around and went into the hall."
        "I had a couple of minutes to clean myself up and clarify the playoff situation."

    elif alt_my_rival_semifinal.take == 'sh':
        show sh normal pioneer with dissolve
        "Shurik nodded at me and stood up."
        "I don't know if he was impressed with my skill at the game I was playing today for the first time in my life or not."
        "Anyway, he was indifferent enough to lose."
        if not ('cyber' in list_joined_clubs_7dl) and ('cyber' in list_voyage_7dl):
            show sh smile pioneer with dspr
            sh "About the cybernetics club, if anything..."
            "I nodded."
        hide sh with dissolve
        if not ('cyber' in list_joined_clubs_7dl) and ('cyber' in list_voyage_7dl):
            "But let's talk about cybernetics later, but in the meantime let's see what the other pioneers are up to."
        else:
            "In the meantime, I decided to see what the other pioneers were up to."

    elif alt_my_rival_semifinal.take == 'mz':
        show mz normal glasses pioneer with dissolve
        "Zhenya's reaction amused me."
        "First she threw the cards on the table and hid her face in her hands."
        "And then she threw her hands up in the air and barked:"
        show mz laugh glasses pioneer with dspr
        mz "Hallelujah!" with vpunch

        show mz normal glasses pioneer far with dissolve
        pause(0.25)
        show mz normal glasses pioneer far at fleft with move
        hide mz with moveoutleft

        "And then she teleported out of the canteen."
        "And I decided to see how the neighbors were doing."
# ---------------------------------------------------- \\ Диалоги

#-------------------------------------------------------------------------------------------------
    pause(.5)
    call alt_day2_semifinal_analizer                                    # анализ полуфинала
    $ renpy.block_rollback()                                                          # блокируем роллбак
#-------------------------------------------------------------------------------------------------
label alt_day2_final_new:
    $ alt_day2_my_win = alt_day2_rival_win = alt_day2_game_played_out = 0                       # обнуляем результат игр
    $ alt_tournament_state = "final_start"                                                      # устанавливаем начало финала
    if alt_day2_result_tour == 1:                                                               # Если продул в 1 туре
        $ alt_drawing_of_detour_final()                                                         # вызываем рандомизатор
        $ renpy.fix_rollback()                                                                  # фиксируем выбор — "откатом" поменять будет нельзя
# -----------------------------------------------------------------------
    $ alt_my_rival_final, alt_index_rival_final = alt_get_me_rival_final(alt_day2_gamblers_final,alt_rival_final)      # узнаём второго соперника в финале и его индекс  в рассадке

    $ alt_name_my_rival_i = alt_my_rival_final.name['i']                                   # узнаём ИМЯ второго финалиста (в именительном падеже)
    $ alt_name_my_rival_r = alt_my_rival_final.name['r']                                   # узнаём ИМЯ второго финалиста (в родительном падеже)
    $ alt_name_my_rival_d = alt_my_rival_final.name['d']                                   # узнаём ИМЯ второго финалиста (в дательном падеже)
    $ alt_name_my_rival_v = alt_my_rival_final.name['v']                                   # узнаём ИМЯ второго финалиста (в винительном падеже)
    $ alt_name_my_rival_t = alt_my_rival_final.name['t']                                   # узнаём ИМЯ второго финалиста (в творительном падеже)

    $ alt_spr_my_rival = alt_my_rival_final.take                                                # получаем спрайт соперника — заголовок
    $ alt_emo_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][0]                     # эмоция (строка)
    $ alt_acc_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][1]                     # аксессуар (строка)
    $ alt_clot_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][2]                    # одежда (строка)
    $ alt_pos_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][3]                     # положение

    $ alt_nick_my_rival = alt_my_rival_final.nick                                               # получаем характер соперника (для диалога)
# -----------------------------------------------------------------------

    # ================================================ пересаживаемся за финальный стол.
    show el smile pioneer at left with dissolve
    el "The semifinals are over, the winners meet in the finals!"
    hide el with dissolve
    $ alt_mstt = 2
    call show_tournament_table                                                                  # показать таблицу — итоги полуфинала
# ----------------------------------------------------------------------------------------------------
label alt_day2_final_choice_new:
    if alt_rival_final.take == 'me':                                                            # Семён прошел в финал
        "I'm moving steadily toward victory, my next victim is already in sight."

# ---------------------------------------------------- ДИАЛОГИ
        if alt_my_rival_final.take == 'un':
            "I'm sorry, Lena. It's nothing personal."
        elif alt_my_rival_final.take == 'sl':
            "Slavya. Well, she's playing soullessly anyway, so I'll only do her good."
        elif alt_my_rival_final.take == 'dv':
            "Alisa, aha."
            me "Alisa, hey, Alisa."
            dv "What?"
            me "You're finished."
            "She laughed."
        elif alt_my_rival_final.take == 'mi':
            "Miku."
            "As a gallant fellow, I'm inclined to give up this game to make a girl feel good."
            "But as a player I can smell victory, so no mercy!"
        elif alt_my_rival_final.take == 'us':
            "The kid? Man, somebody explain to me clearly: what the hell did that little misunderstanding forget in the finale?"
        elif alt_my_rival_final.take == 'sh':
            "Shurik? Hmm. It's going to be an interesting fight."
        elif alt_my_rival_final.take == 'mz':
            "Beetlewoman."
            "Might squeak about not wanting to play, but - geez, she's in the finals!"
            "It's going to take some work."
# ---------------------------------------------------- /ДИАЛОГИ

        if alt_day2_detour_final:                                                                  # если пропуск финала
            scene bg int_dining_hall_sunset with dissolve2
            pause(1.0)
            if not alt_day2_tournament_fast_win:                                                   # Если НЕ победа в финале
                $ alt_day2_result_tour = 21                                                         # Семён проиграл в финале
                "Looks like I didn't stand a chance."
                call alt_day2_summary_poker_round
                jump alt_day2_final_fail_end_new                                                    # на поражение в финале
            elif alt_day2_tournament_fast_win:                                                      # если победа в финале
                $ alt_day2_result_tour = 22                                                         # Семён выиграл в финале
                call alt_day2_summary_poker_round
                jump alt_day2_final_win_end_new                                                    # на победу в финале

        jump alt_day2_final_start_new                                                              # играем финал
# ----------------------------------------------------------------------------------------------------
    else:                                                                                      # Семён продул в 1/2
        $ alt_name_rival_final = alt_rival_final.name['i']                                     # Получаем имя финалиста — кому Семён проиграл
        if alt_day2_result_tour == 1:                                                           # Если продул в 1 туре
            if alt_rival_final.take == alt_my_rival_1_tour.take:                                # соперник в 1 туре и финале тот же
                "My rival from the first round reaches the finals — %(alt_name_rival_final)s{nw}"
            else:
                if alt_my_rival_1_tour.take == 'sh':
                    "Shurik, my lucky opponent, lost in the semifinals."
                else:
                    $ alt_name_rival_1_tour = alt_my_rival_1_tour.name['i']
                    "%(alt_name_rival_1_tour)s, who sent me to the company of fans, herself lost in the semifinals."
                "And to the finals comes %(alt_name_rival_final)s{nw}"
        else:
            "Since I was deflated and lost, the first finalist is %(alt_name_rival_final)s{nw}"
        extend ", where they will meet{nw}"
# ---------------------------------------------------
        if alt_my_rival_semifinal == None:                                                                        # Если каким-то образом второй финалист не назначен (может быть и такое)
            $ alt_my_rival_semifinal = alt_day2_gamblers_final[1-alt_day2_gamblers_final.index(alt_rival_final)]  # Это НЕ тот, кому Семён проиграл
# ---------------------------------------------------

# ---------------------------------------------------- ДИАЛОГИ
        if alt_my_rival_final.take == 'un':
            extend " Lena and will try to beat her."
        elif alt_my_rival_final.take == 'sl':
            extend " Slavya and will prove to everyone that blonde is a diagnosis."
        elif alt_my_rival_final.take == 'dv':
            if alt_rival_final.take == 'us':
                extend "… Alisa? Did they plan this from the start?!"
            else:
                extend " Alisa and try to survive this fight."
        elif alt_my_rival_final.take == 'mi':
            extend " Miku. {w}I don't think there will be many problems there. Although the Japanese girl did make it to the finals.."
        elif alt_my_rival_final.take == 'us':
            if alt_rival_final.take == 'dv':
                extend " Ulyana."
                "It's funny, but it looks like the redheads really did simply trash this tournament like they wanted to."
            else:
                extend " Ulyana and will try to survive after meeting her."
        elif alt_my_rival_final.take == 'sh':
            extend " Shurik and will try to prove that brains are completely unneeded in a card game."
        elif alt_my_rival_final.take == 'mz':
            extend " Zhenya."
            "What else can you say about her?"
            "Right. Beetlewoman."
# ---------------------------------------------------- /ДИАЛОГИ
        scene bg int_dining_hall_sunset with joff_r
        $ alt_day2_gamblers_final[renpy.random.choice([0,1])].winner = True                                    #  один из игроков (рандомно) — победитель в финале
        $ alt_tournament_state = "final_end"
        call alt_day2_final_analizer

        if (alt_day2_dv_ultim == 1):
            "Well, now we can sum it up."
            "The bet was a natural failure - it was foolish to hope with my luck. In hindsight, I should have known in advance what we were going to play."
            "It's not a game, it's just a coin flip! Randomly handed out cards, randomly choosing which one to take from your opponent."
            if (alt_day2_walk == 1) and (alt_my_rival_final.take != 'dv'):
                dreamgirl "You marked the cards, you idiot! How did you even manage to lose with that?!"
                th "It was a misinput."
            else:
                "Anyway, the defeat was not my fault. Here."
        $ renpy.block_rollback()                                                                                # блокируем роллбак
        stop music fadeout 2
        jump alt_day2_prepare_transition_to_supper
# ------------------------------------------------------------------------------------------------------------------------------

label alt_day2_final_start_new:
    call alt_day2_checking_scores
    call alt_day2_stipulation_new                                                       # определяемся, кто первый ходит
# ----------------------------------------------------------------------------
    # первоначальные "настройки" игроков — могут меняться по результатам игры
    # 'defense' — защита, 'gamble' — риск, 'succumb' — слив, 'foolplay' — рандом
    # вероятность ошибки: 1 = 80%, …, 4 = 20%, 5 — ошибок нет.
    if alt_my_rival_final.take == 'un':                                                    # Добрались сюда — так что нефиг, Лена защищается
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 4                                                       # ошибки, правда, есть — 20%(4)
    elif alt_my_rival_final.take == 'sl':                                                  # Славя будет защищаться, может ошибиться — 20%(4)
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 4
    elif alt_my_rival_final.take == 'dv':                                                  # Алиса рискует, вероятность ошибки 20%
        $ alt_day2_gambler_behavior = 'gamble'
        $ alt_day2_gambler_skill = 4
    elif alt_my_rival_final.take == 'mi':                                                  # Мику будет защищаться, может ошибиться — 20%(4)
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 4
    elif alt_my_rival_final.take == 'us':                                                  # Ульяна к финалу научилась играть и будет защищаться, но с ошибками 40% (3)
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 3                                                       # ошибок — 40%(3)
    elif alt_my_rival_final.take == 'sh':                                                  # Шурик экспериментирует по-прежнему, вероятность ошибки 20%
        $ alt_day2_gambler_behavior = renpy.random.choice(['defense', 'gamble'])           # у него своя кухня — набор из возможных вариантов
        $ alt_day2_gambler_skill = 4
    elif alt_my_rival_final.take == 'mz':                                                  # Женя играет рандомно, как в классике, вероятность ошибки 20%
        $ alt_day2_gambler_behavior = 'foolplay'
        $ alt_day2_gambler_skill = 4
# ----------------------------------------------------------------------------

    if alt_day2_walk == 1:
        $ VISIBLE = True
        $ INVISIBLE = True
    else:
        $ VISIBLE = True
        $ INVISIBLE = False

# ------------------------------------------------------------------------------------------------------------------------------
# Палим Семёна с крапом карт
    if alt_day2_walk == 1 and INVISIBLE:                                    # Если Сёма мухлевал И ЕГО ещё не поймали, его таки в финале МОГУТ спалить
        if alt_my_rival_final.take == 'dv':                               # палит Алиса
            "But before it started, Alisa looked suspiciously at the cards we were playing."
            th "No way..."
            "A chill ran down my spine..."
            "And she leaned slightly over the table and, smiling slyly, asked in a whisper - so that only I could hear her..."
            show dv smile pioneer2 with dissolve
            dv "So you've marked all the cards, have you?"
            dv "Prudent..."
            th "She knew I cheated!!!"
            "I blushed."
            th "If she gets up now and tells everybody..."
            th "That would be terrible!!!"
            th "Unbearable!!!"
            th "Horrible!!!"
            "But Alisa didn't seem to think of giving me away..."
            "She was smiling!"
            dv "Were you hoping to beat me like that, too?"
            "And I, cursing my honesty, also in a whisper, answered:"
            me "Yes..."
            "She snorted, however, without any anger."
            dv "Don't even dream..."
            "Unnoticed by the audience, she took a brand new deck of cards out of her pocket and swapped it with the one I had marked..."
            dv "We'll play with mine!"
            show dv laugh pioneer2 with dissolve
            "She smiled contentedly."
            dv "I'm prudent, too..."
            "Game on."
            $ INVISIBLE = False
# ------------------------------------------------------------------------------------------------------------------------------

label alt_day2_final_re_game:                                                           # игра в финале — сюда возвращаемся на повторную игру
    $ alt_my_poker_hand = None
    $ alt_rival_poker_hand = None

    python:
        dialogs = {
                        (0, 'win','jump'):'alt_day2_one_play_win_new',
                        (0, 'fail','jump'):'alt_day2_one_play_fail_new',
                        (0, 'draw','jump'):'alt_day2_one_play_draw_new'
                    }
        generate_cards_alt('bg hall', dialogs)

# ****************   НОВЫЕ  СОПЕРНИКИ   ******************************************
        if alt_my_rival_final.take == 'un':
            rival = CardGameRivalWiseUsual(un_avatar_set, u"Lena", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_final.take == 'sl':
            rival = CardGameRivalWiseUsual(sl_avatar_set, u"Slavya", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_final.take == 'dv':
            rival = CardGameRivalWiseUsual(dv_avatar_set, u"Alisa", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_final.take == 'mi':
            rival = CardGameRivalWiseUsual(mi_avatar_set, u"Miku", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_final.take == 'us':
            rival = CardGameRivalWiseUsual(us_avatar_set, u"Ulyana", alt_day2_gambler_behavior, alt_day2_gambler_skill) # К финалу Ульянка уже и играть научиться должна бы
        elif alt_my_rival_final.take == 'sh':
            rival = CardGameRivalWiseUsual(sh_avatar_set, u"Shurik", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_final.take == 'mz':
            rival = CardGameRivalWiseUsual(mz_avatar_set, alt_day2_gambler_behavior, alt_day2_gambler_skill)           # Женя играет рандомно, как в классике
# ************************************************************************************

    $ alt_hint_poker = alt_hint_poker_contractual                                           # подсказки комбинаций — по просмору правил
    jump cards_gameloop_wise_alt                                                            # переход карточный стол

#-------------------------------------------------------------------------------------------------
label alt_day2_final_fail_end_new:
    $ alt_day2_result_tour = 21                                             # Семён проиграл в финале
    scene bg int_dining_hall_sunset with dissolve
    $ persistent.altCardsWon2_new = True

    if alt_day2_gamblers_final[0].take != 'me':                             # если 1-й игрок — НЕ Семён
        $ alt_day2_gamblers_final[0].winner = True                          # он и выиграл
    else:                                                                   # если 2-й игрок — НЕ Семён
        $ alt_day2_gamblers_final[1].winner = True                          # он и выиграл
    $ alt_tournament_state = "final_end"                                    # устанавливаем конец финала

    if not alt_day2_detour_final:                                           # если НЕ пропуск финала
        "Seems like I didn't stand a chance."
        call alt_day2_summary_poker_round

    scene
    call alt_day2_final_analizer
    $ renpy.block_rollback()                                                          # блокируем роллбак
    scene bg int_dining_hall_sunset with dissolve

# ---------------------------------------------------- ДИАЛОГИ
    if alt_my_rival_final.take == 'un':
        $ lp_un += 1
        stop music fadeout 2
        show un surprise pioneer with dissolve
        "Lena doesn't seem to have fully understood exactly what just happened."
        play music music_7dl["take_my_hand"] fadein 3
        "And there was the birth of a legend, +50 to experience, a new level, and the unlocking of self-confidence!"
        show un cry_smile pioneer with dspr
        "Lena looked at me for a long, steady moment, and her hands were shaking."
        "I am silent, she is silent, and it is as if a kind of repulsive wall has grown around us, protecting us - but only as long as we are together."
        "It's as if two people, each incomplete when alone, are much stronger together than if you just put their characteristics together."
        "I can't tell now if I was giving in or playing hard to get, but just coming here was already a good idea, a hundredfold paid off by these moments."
        dreamgirl "Don't fall in love with her, chief, you've known her less than twenty-four hours."
        "I shrugged it off."
        th "So what?"
        "I mean, everyone sings about love at first sight, why shouldn't I fall victim to this magical phenomenon?"
        "All right, but can I just admit to myself that I like her?"
        "Just her face, her figure, and her demeanor."
        th "Maybe she's got pound roaches in there, and she only looks like a coy girl, eyes to the floor, eyelashes bang-bang-bang."
        th "But I don't know that, do I?"
        th "So I'll enjoy the ignorance."
        th "For that is true bliss."
        "Not knowing bad things about loved ones, not understanding the meaning of the lyrics of a beautiful song in Japanese, not thinking about fertilizer for strawberries and apple trees, not understanding that a beautiful coat means the death of an animal."
        "Here and now - for a small fraction of a second - just to fall in love, to fall prey to the situation, the mood and the atmosphere."
        with fade
        "And let go of the moment, because it's time to wake up and go to work."
        me "Congratulations on your victory."
        "I smiled."
        show un shy pioneer with dspr
        un "T-thanks…"
        "They've already put her name on the list of winners, and tomorrow they'll probably make her raise the flag as the most active participant."
        "After all, you can't get first place without actively participating."
        "Isn't that right?"
        "Oh, my condolences."
        if alt_day2_dv_ultim == 1:
            th "Although I'm probably the one who should be sympathetic?"
            dreamgirl "Are you talking about Dvachevskaya's insinuations? Don't drift, she's washed up before she even reached the finale, shame on her."
            "As if to confirm my words, Alisa, who had been watching us the whole game, seemingly forgetting to breathe, flinched and looked away."
            "Looks like she doesn't have the guts to bring her nastiness to its logical conclusion."
        stop music fadeout 3

    elif alt_my_rival_final.take == 'sl':
        $ lp_sl -= 1
        $ karma += 10
        stop music fadeout 3
        show sl sad pioneer with dspr
        "Slavya groaned and dropped her head on her folded arms."
        play music music_list["forest_maiden"] fadein 5
        sl "Have you guys even tried?"
        me "I - did my best!"
        sl "Semyon, please."
        show sl serious pioneer with dspr
        "She frowned."
        sl "There's no worse card player than me, and I took... Ah, why did I even agree to this!"
        me "But we were..."
        sl "Did you really not care so much that you were too lazy to even try a little?"
        show sl sad pioneer with dspr
        sl "I'm very, very disappointed."
        sl "If you're going to be as active at tomorrow's dance, I'll take the hint, and you can entertain yourselves for the rest of the shift."
        show mt laugh pioneer at left with dissolve
        mt "What have we got here, huh?"
        mt "Winner's demarche? Well, finally! {w}I was beginning to think you were a living Madame Tussauds exhibit." # "экспонент" — так задумано или меняем на "экспонат"? ## полагаю, трудно случайно вместо "экспонат" написать "экспонент" ### не пацаны, в английском оно так не работает
        show sl angry pioneer with dspr
        sl "Olga Dmitrievna, I'm serious, and you!"
        show mt normal pioneer with dspr
        mt "Slavya, just enjoy winning, okay? {w}I know your attitude toward card games, and if I had the chance to put someone else in your place, I would."
        hide mt with moveoutleft
        "Olga sighed sympathetically, winked at her, and disappeared into the kitchen."
        "Looks like the words about the prize had some justification!"

    elif alt_my_rival_final.take == 'dv':
        $ lp_dv = lp_dv/2
        stop music fadeout 2
        if loki or herc:
            "It was fun to lose."
            play music music_list["you_lost_me"]
            "On either side, no matter how you look at it, I've got the upper hand - if I win, I'll be able to shut Dvachevskaya up a bit."
            dreamgirl "Exactly until she's ripe for another prank."
            th "That's enough."
            "And if I lose, she'll give me a PR stunt in the spirit of «Syoma's coming, hide the women»."
            "So I wished my opponent good luck from the bottom of my heart."
            "And got ready for the show."
        else:
            th "I blew it."
            th "I screwed up."
            play music music_list["you_lost_me"]
            th "Like always…"
            if alt_day2_walk == 1:                                                 # была лишняя проверка
                th "Even after I marked the cards."
            "I got that nasty feeling that they were going to point and whisper at me - «Look, it's him! Yes, that's him! He screwed up.»"
            "I moved away from the table without raising my eyes to anyone."
            "Especially not at Alisa."
            "Her gaze literally burned my back."
        if alt_day2_dv_ultim == 1:                                                 # Спорил
            th "I lost the bet."
            if loki or herc:
                "Now we wait until tomorrow and enjoy the free advertising?"
            else:
                "Now I'm... {w} Screwed? Done for? Fucked?"
                th "Should I escape from the camp before it's too late?"
        else:                                                                       # НЕ спорил
            if alt_day2_dv_ultim == 2:                                              # Если лапал
                "And now if she tells everyone that I groped her, it'll be true, right?"
                "As my dad used to say in difficult situations - not oops, but yops."
            else:                                                                   # НЕ лапал
                "Although I didn't argue with Dvachevskaya, she may well now tell everyone what she made up on the porch."
                "And they'll believe her. As they usually believe any winner."

        "Alisa won, and everyone congratulated her."
        "Electronik waved his hands, signaling the end of the tournament, and added her name to the table."
        th "Alisa won..."
        if alt_day2_dv_ultim == 1:
            th "And I lost both the tournament and the bet..."
        else:
            th "And I lost... As always, though."
        th "What will happen?!"
        show dv normal pioneer2 at fleft with dissolve
        "I looked at Alisa. There didn't seem to be a trace of joy on her face..."
        if alt_day2_dv_ultim == 2:
            "Alisa got up from the table and, perceptibly forcing herself…"
            show mt normal pioneer at fright with dissolve
            "Headed for the counselor! Yes! The moment of truth!"
            show dv normal pioneer2 at fleft with moveinleft
            th "Will the girl have enough balls?"
            "Everything inside me trembled in anticipation."
            "I moved closer, trying to hear the details."
            "But she was whispering, and I could hear nothing..."
            show dv guilty pioneer2 at cright
            show mt normal pioneer at fright
            with dissolve
            "She blushed more and more, and I could literally read her lips."
            "…hands…"
            "…right on the chest…"
            "…and under the skirt…"
            me "Dvachevskaya, you have such a fervent imagination!"
            "I drew the line at their whispering."
            show dv sad pioneer2 at left
            show mt normal pioneer at right
            with dissolve
            me "Why don't you tell me aloud? I'd like to hear it too."
            stop music fadeout 3
            "And Olga Dmitrievna calmly looked at me and said:"
            mt "Alice says you're a hell of a player."
            show mt smile pioneer at right with dspr
            mt "I think that's about right."
            hide dv
            hide mt
            with dissolve
            "I laughed and cleared the table."
            "You bet I did. That's not the reaction Aliska was expecting from me, not at all."
        else:
            "With indifference, lazily casting a squinted glance at me, Alisa…"
            show mt normal pioneer at fright with dissolve
            "Went straight to Olga Dmitrievna, who was standing among the audience the whole time!"
            show dv normal pioneer2 at fleft with dspr:
                xalign 0.1
                linear 3.0 xalign 0.7
            if loki:
                th "Will she really say?"
            elif herc:
                th "So she decided to tell her story?"
            if dr:
                th "She's really going to tell?!"
            if not alt_day2_dv_ultim:
                if loki:
                    th "I didn't bet with her."
                elif herc:
                    th "How stubborn she is."
                    dreamgirl "Reminds you of anyone?"
            if dr:
                "It was as if everything in me was turned upside down."
                "I rushed after her..."
                "But it was too late..."
            elif herc:
                "I sat back comfortably and waited for the denouement."
                dreamgirl "Not afraid?"
                th "Not at all."
                th "If the counselor believes this nonsense, I'll be disappointed in her."
            show dv smile pioneer2 at cright
            show mt normal pioneer at fright
            with dissolve
            "Alisa stood next to Olga Dmitrievna and whispered something hotly in her ear, looking at me rather slyly."
            if dr:
                "I couldn't let that happen!"
                "With a loud scream..."
                me "It's not true!"
                me "Everything she says about me is NOT TRUE!"
                show dv smile pioneer2 at left
                show mt normal pioneer at right
                with dissolve
                "I ran up to them."
                stop music fadeout 3
                "And Olga Dmitrievna calmly looked at me and said:"
                mt "I think it's true."
                show mt smile pioneer at right with dspr
                mt "You don't know how to play cards at all."
                "This is the most embarrassing thing I've ever experienced."
            elif herc:
                "I grinned back at the redhead."
                me "Go ahead."
                show dv sad pioneer2 at cright with dspr
                pause(0.3)
                show dv normal pioneer2 at cright with dissolve
                "I don't think Dvachevskaya can read lips, but she realized how indifferent I was to her exertions."
                th "It's a little late for that."
                dreamgirl "Put some oil on the fire."
                th "In what way?"
                "I can think of at least five ways to make Dvachevsky blush."
                "And all five were indecent gestures."
                "I won't do it, but the thought of it amused me."
                th "Thank you."
                dreamgirl "At your service."
                "Olga looked at me and calmly said:"
                mt "Well yes, that's right, he can't play."
                mt "But he doesn't seem to care too much."
                stop music fadeout 3
                "I almost laughed."
                "She didn't have enough courage after all!"
            elif loki:
                show dv normal pioneer2 at cright with dissolve
                "I tried to keep my face and not lose my dignity, waiting for the denouement."
                "I don't believe a qualified educator like our counselor would believe this ridiculous nonsense."
                "Especially from the mouth of Dvachevskaya."
                "If she does, I'm a little disappointed in her."
                "And I'll remind Dvachevskaya of that."
                "Finally, Olga said quietly:"
                mt "Well, yes, that's right."
                mt "He doesn't know how to play cards at all."
                stop music fadeout 3
                "The redhead couldn't make it and went backwards."
                "I wasn't hiding a smile."

    elif alt_my_rival_final.take == 'mi':
        stop music fadeout 3
        show mi happy pioneer with dspr
        $ lp_mi += 1
        $ karma += 10
        mi "Yes! Yes! Do you understand that?! It's me again, and I'm back on the horse!"
        play music music_7dl["ourfirstmet"] fadein 3
        mi "I had no doubt in my mind that I would come and beat everyone!"
        mi "And I came and I won."
        mi "I'm, I'm... I'm super-Miku!"
        me "Charming monster."
        "I mumbled."
        show mi smile pioneer with dspr
        mi "I don't get out of the club that often, because everyone always has something to do, everyone is in a hurry and tells me «we'll talk later!»."
        mi "And I don't want later, I want now! And now, while I'm a winner, you all have to listen to me and not swear that I talk too much!"
        th "Deficiency of attention, affection, warmth and care... And I thought I was a hikikomori."
        me "What's with the yelling?"
        stop music fadeout 3
        "For me to be in the finals was already an achievement, so I wasn't too upset about losing."
        play music music_7dl["tender_song"] fadein 3
        "And Miku suddenly raised a finger to the sky."
        show mi happy pioneer with dspr
        mi "Oh, I know, I think! Yes! I just had an idea! I…"
        show mi happy pioneer far with dissolve
        "She climbed up on the table."
        mi "I'll sing to you!"
        "She took a breath, and..."
        show dv angry pioneer2 at cleft with easeinleft
        show mt angry pioneer at cright with easeinright
        with vpunch
        "Unbeknownst to me, Olga and Alisa, roaring in unison, rushed to drag her to the floor."
        "But how could they!"
        show mi laugh pioneer far at fleft with diam
        "The finalists' game table was big, not unlike the narrow one at which we qualified."
        "So the little, scrawny little Jap successfully jumped between raking hands and sang at the top of her developed lungs."
        "She sang about something of her own, in a lunar accent that even when I was drunk I found tongue-shattering, so I didn't try to comprehend."
        "It was much more interesting to listen to the voice."
        "And laughing at the clapping here and there in time with the singing."
        "More often from Alisa and Olga Dmitrievna who were trying to catch Miku, but there was a share of applause from the appreciative audience, too."
        mi "La-la, la-la-la-la, la-la-la, la-la-la-la!"
        "She howled, running around tables, chairs, and showing us not only her high level of card playing, but also her outstanding parkour training."
        "I'd bet on the Japanese girl and I wouldn't miss it."
        "That's her whole life."
        "Fidgety, running and jumping on stage, and performing not three minutes at a time, but full-blown concerts of several hours."
        hide mt
        hide dv
        with dissolve
        "So for another five minutes, both catchers plopped down next to the tables, and she kept singing on and on, making strange, shearling motions with her fingers in the air."
        "Somehow such movements, and even more so in the execution of the ultramarine manicure, made an unpleasantly cold tickle in my stomach."
        show mi normal pioneer far at center with easeinleft
        with fade
        "But it all comes to an end sometime."
        show mi smile pioneer with dissolve
        "The long-playing song of the Japanese starlet also ended, and she, coming up the table at my side, held out her hand to me."
        "And I, like a true gentleman, accepted it and helped the girl down."
        show mi happy pioneer close with dspr
        mi "Thank you! You're my hero!"
        show mt rage pioneer at fleft with dissolve
        mt "Well, Hatsune!"
        "Miku clung to me with her whole body for a moment, and then ran away from the screams of the furious squad leader."
        hide mi with flash

    elif alt_my_rival_final.take == 'us':
        $ lp_us += 1
        stop music fadeout 2
        "As you know, it's the beginners and the fools who get lucky at cards."
        play music music_7dl["genki"] fadein 3
        "Since we're all new here, we were on equal footing."
        "But someone got one more chance!"
        "And everyone knows who it is, and why he got more!"
        show us normal pioneer with dissolve
        "Those empty, glassy blue eyes look very strange framed by scarlet bangs."
        "A wheat-colored braid, like Slavya's, would suit this child much better."
        "Such an incomplete blonde."
        show us laugh pioneer with dspr
        us "Yay! I won!"
        "She jumped up on the chair!"
        us "I won! And now the super prize is mine! {w}Miiiiiiiiiiine!"
        me "Yours, yours. Just get off the chair or you'll fall over."
        "No way."
        "Ulyanka started bouncing on the dangerously squeaky chair and chanting:"
        us "Prize! Prize! Prize!"
        me "Calm down, will you?"
        show us grin pioneer with dspr
        us "You're just jealous that I'll have the prize and you won't!"
        "I have no idea what prize she's talking about."
        "Actually, I'd better go before something happens."
        hide us with dissolve
        scene
        call show_tournament_table
        "And in the very center of the table, in huge red letters, was the name."
        el "The winner is Ulyana!"
        "Everyone began to shout «congratulations, congratulations»!"
        scene bg int_dining_hall_sunset
        show us grin pioneer
        with dissolve
        "But Ulyana brushed it off. {w}She was interested in other things:"
        us "Where are the prizes?"

    elif alt_my_rival_final.take == 'sh':
        show sh normal pioneer with dissolve

        "Honoring Shurik looked awkward and strained."

        show sh serious pioneer far with dissolve
        pause(0.25)
        show sh serious pioneer far at fright with move
        hide sh with moveoutright

        "He stood up, bowed, and walked out of the canteen without even waiting for his name to be put on the leaderboard."

        show mi shocked pioneer far at center with dspr
        mi "Nightmarish man."
        "Noticed Miku."

        show mi upset pioneer far with dspr
        mi "Totally far from publicity."

        show un normal pioneer far at left with dspr
        show mi upset pioneer far at right with move
        un "He has other merits."

        show us smile pioneer far at fleft with moveinleft
        us "Yes? Please elaborate on the merits, because I didn't hear you."

        show mi surprise pioneer far at fright
        show un serious pioneer far at center
        with move
        un "All you want to hear about is lewdness."

        show sl serious pioneer far at cleft with dspr
        show un serious pioneer far at cright with move
        sl "Lena, and you yourself should think a little bit about what you say in the presence of the child."

        show un surprise pioneer far
        show us dontlike pioneer far
        show mi dontlike pioneer far
        with dspr
        us "Hey, I'm already fourteen!" #us "Эй, мне уже двадцать девять!"
        mi "Hey, I'm already sixteen!"

        un "Uh…"
        sl "Yes, yes, you were ranting about Shurik's merits."

        show dv surprise pioneer2 far at center with dspr
        dv "Girls, what are you discussing here, and without me?"

        show mi cry_smile pioneer far:
            xcenter 0.86
        show un grin pioneer far:
            xcenter 0.67
        show sl surprise pioneer far:
            xcenter 0.33
        show us surp1 pioneer far:
            xcenter 0.10
        with move
        un "Oh, Dvachevskaya, get lost! You forest nightmare, you thought of scaring the newcomer with your tits."
        me "Hey, I'm still here!"

        show mi rage pioneer far
        show un rage pioneer far
        show dv rage pioneer2 far
        show sl angry pioneer far
        show us angry pioneer far
        with dspr
        all "SHUT UP!" with vpunch

        show mi smile pioneer far
        show un shy pioneer far
        show dv grin pioneer2 far
        show sl shy pioneer far
        show us normal pioneer far
        with dspr
        "So I did."

        show mi laugh pioneer far
        show un laugh pioneer far
        show dv laugh pioneer2 far
        show sl laugh pioneer far
        show us laugh pioneer far
        with dspr
        $renpy.notify("Syoma, you're such a degenerate, it's fucked up!")
        "What else was there for me to do." #Сёма, какой же ты дегенерат, пиздец просто!

    elif alt_my_rival_final.take == 'mz':
        show mz normal glasses pioneer with dissolve
        "The Beetle stood up."
        "She gave everyone a wild look."
        mz "Is that it? No more victims?"
        play sound sfx_7dl["highfive"]
        pause(1)
        play sound sfx_7dl["highfive"]
        pause(1)
        "In complete silence she asked."
        play sound sfx_7dl["highfive"]
        pause(1)
        play sound sfx_7dl["highfive"]
        show el smile pioneer at left with dissolve
        "Only Electronik kept clapping."
        mz "All right. I'll go then."
        el "Hurrah for the winner!"

        show mz normal glasses pioneer far with dissolve
        pause(0.25)
        show mz normal glasses pioneer far at fleft with move
        hide mz with moveoutleft

        play sound sfx_7dl["highfive"]
        "Shouted Syroezhkin after her."
        "I think it's love after all."
        sh "El, that's it, she's gone. Calm down."
# ---------------------------------------------------- \\ Диалоги
    stop music fadeout 3
    jump alt_day2_prepare_transition_to_supper                        # пошли ужинать

#-------------------------------------------------------------------------------------------------
label alt_day2_final_win_end_new:
    $ alt_day2_result_tour = 22                                             # Семён выиграл в финале
    $ lp_dv += 1

    if not alt_day2_detour_final:                                          # если НЕ пропуск финала
        $ persistent.altCardsWonRivals_new[alt_spr_my_rival] = True        # Выиграли у этого соперника
    $ persistent.altCardsWon3_new = True

    if alt_day2_gamblers_final[0].take == 'me':                             # если 1-й игрок — Семён
        $ alt_day2_gamblers_final[0].winner = True                            # он и выиграл
    else:                                                                   # если 2-й игрок — Семён
        $ alt_day2_gamblers_final[1].winner = True                            # он и выиграл
    $ alt_tournament_state = "final_end"                                   # устанавливаем конец финала

    if not alt_day2_detour_final:                                                # если НЕ пропуск финала
        call alt_day2_summary_poker_round

    scene
    call alt_day2_final_analizer
    $ renpy.block_rollback()                                                          # блокируем роллбак
    stop music fadeout 3
    scene bg int_dining_hall_sunset with dissolve

# ---------------------------------------------------- ДИАЛОГИ
    if alt_my_rival_final.take == 'un':
        show un shy pioneer with dissolve
        un "W-well, I g-guess that's it."
        play music music_7dl["take_my_hand"] fadein 3
        me "What?"
        show un sad pioneer with dspr
        un "U-uh… You won. C-congratulations."
        "She mumbled."
        "You could hardly make her out over the noise of the crowd, and she just kept on and on..."
        "If it were up to me, I'd probably ask her to speak louder."
        th "But how could I."
        th "That means imminent convergence."
        scene bg int_dining_hall_sunset with dissolve
        "Not listening any more to what she was telling me, I got up."
        "And went to the blackboard, where Electronik had already written my name."
        scene
        call show_tournament_table
        "Mine!"
        if alt_day2_dv_ultim in (1, 2):
            th "And let the red-headed vulture try to yap something there."
        scene bg int_dining_hall_sunset with dissolve
        if alt_day2_dv_ultim == 2:
            show dv shy pioneer2 with dissolve
            "Catching my gaze, she blushed like a poppy."
            "And I, with my head bowed to the side, performed a pantomime called «pulling on a rubber glove»."
            show dv shocked pioneer2 with dspr
            "And wiggled my fingers eloquently."
            "Alisa felt sick to her stomach."
            th "Or maybe she thought I wasn't putting on a glove, but... Ew, she's so spoiled."
        else:
            "Lena was lost somewhere in the background, and I could feel someone's gaze unremittingly on my shoulder blades."
            show dv smile pioneer2 with dspr
            play sound sfx_punch_medium
            dv "Congratulations!" with vpunch
            "So I almost expected a clap between the shoulder blades."
            "Apparently, this is how Dvachevskaya greets everyone she's interested in."
        hide dv with dissolve

    elif alt_my_rival_final.take == 'sl':
        $ lp_sl += 1
        show sl smile pioneer with dspr
        "I won?"
        play music music_7dl["please_reprise"] fadein 3
        "Won?!"
        me "YES!"
        "Throwing the cards over my head, I barked:"
        me "I'm the winner!!!" with vpunch
        show sl smile2 pioneer with dspr
        "For some reason, here and now, I wanted to act the way I felt."
        "Not the way the rules demanded, and without being stopped by «what would people say»."
        "It's her influence. Her."
        "We've known each other less than 24 hours."
        "But already the sincerity of feelings is becoming one of the most important virtues."
        sl "Yes!"
        "She said with a ringing voice."
        "Her eyes shone."
        sl "You are the winner of the tournament."
        sl "You - are the winner."
        "Like in boxing, she's standing next to me."
        "Grabbing my wrist."
        "And pulls me to the sky with her hand up."
        show sl happy pioneer with dspr
        sl "Sem-{w=.3}yon! Sem-{w=.3}yon!"
        "She's chanting."
        "It's hard to fight the feeling of the surrealness of what's going on."
        "It's like I'm caught up in some space opera or some other pathological genre."
        th "But these people don't know how to shy away from honest words and honest feelings."
        "They scream along with it."
        "They look at me."
        "My fifteen minutes of fame."
        $renpy.notify('This is a pun on how Slavya/Glory are only different in 1 letter in Russian')
        dreamgirl "Fifteen minutes of Glory?"
        "And I laughed."
        th "Yes! Hell yes! That's right."
        "Olga Dmitrievna pushed her way over to us."
        show mt normal pioneer at left with dissolve
        mt "Don't go anywhere after dinner, there will be a prize giving."
        show sl normal pioneer with dspr
        dv "Congratulations!"
        "From behind me I heard a voice I really didn't want to hear."
        "Judging by Slavya's narrowed eyes, I wasn't the only one."
        "But I turned around."
        hide mt
        hide sl
        with dissolve
        show dv smile pioneer2 at cright with dissolve
        if alt_day2_dv_ultim == 1:
            dv "You won the bet and the tournament."
        else:
            dv "Good job!"
        hide dv with dissolve
        "She poked me in the shoulder with her fist and, turning around, disappeared into the crowd."

    elif alt_my_rival_final.take == 'dv':
        $ lp_dv += 1
        th "I won!"
        play music music_7dl["sheiscool"] fadein 3
        th "Won?"
        th "Won!!!"
        show dv normal pioneer2 with dspr
        "Just a few hours ago, I couldn't have imagined myself so happy!"
        "I looked at Alisa triumphantly, not yet believing my good fortune..."
        "And everyone around me was already congratulating me on my victory, and Electronik was writing my name on his chart!"
        scene
        call show_tournament_table
        th "My name!!!"
        th "I won the tournament!"
        scene bg int_dining_hall_sunset with dissolve
        "As if those hours of worry and tension had never happened..."
        "I was as light as a feather..."
        "It's like I've learned to fly!"
        if alt_day2_dv_ultim == 1:
            th "I won the bet!!!"
        if alt_day2_dv_ultim == 2:
            show dv shy pioneer2 with dissolve
            "Alisa was ready to fall apart on the spot - so red she was."
            "Catching her gaze, I winked, making the most preposterous face."
            show dv rage pioneer2 with dspr
            "She got all twisted up."
            "And I laughed."
            "Tonight is definitely my night!"
        else:
            show dv smile pioneer2 with dissolve
            "And Alisa finally got up from her seat and clapped me on the shoulder as she walked past me."
            dv "Congratulations!"
            "And those words made me so happy!"
            th "I beat Alisa!!!"
        hide dv with dissolve

    elif alt_my_rival_final.take == 'mi':
        $ lp_mi += 2
        $ alt_day2_mi_snap = True
        show mi smile pioneer with dspr
        mi "You really won! You did great!"
        play music music_7dl["tellyourworld"] fadein 3
        "She exclaimed."
        show mi normal pioneer with dspr
        mi "Just don't think it's going to help you!"
        "Sternly said the girl."
        mi "Next time I'll be sure to beat you!"
        "Sure. As much as you like. But - next time."
        "And now..."
        "The table showed my name in thick red marker."
        "Miku grabbed my arm and dragged me along."
        me "Hey!"
        mi "Hurry up!"
        "Not understanding anything, I hurried after her."
        me "And what?"
        "We stopped at the blackboard, and the girl waved to someone."
        mi "Uncle Borya-sensei! We're here!"
        if ('sport_area' in list_voyage_7dl):
            th "What could she possibly want from Sanich?"
            "With curiosity I thought."
        show ba normal uniform at cleft behind mi # Здесь не надо meet поставить? ## "знакомство" уже состоялось к этому моменту либо при посещении спортплощадки, либо по завершению обхода на экстраде заочно
        show mi smile pioneer at right
        with dissolve
        ba "Yeah, kid, what did you call for?"
        mi "Do you have any more shots?"
        show ba smile uniform with dspr
        ba "For you, kiddo, as many as you want."
        "Out of nowhere a hard brown camera case appeared in his hands, and from there..."
        "A good old «compact machine», a film one."
        "I almost said «rarity», but you could tell it was a working machine."
        ba "Only no flash today, so get someplace a little brighter."
        "Miku smiled and turned on the boiling activity, bracing everyone and rearranging."
        "As a result, the table cloth was removed and moved closer to the window, where Shurik and Electronik held it stretched."
        scene bg int_dining_hall_sunset with dissolve
        with dissolve
        scene
        call show_tournament_table
        "Miku stood up next to me."
        show mi normal pioneer at cleft with dissolve
        "A little closer."
        "Just a little bit more."
        show mi dontlike pioneer with dspr
        mi "Senya!"
        "Finally she couldn't stand it."
        mi "I'm taking a picture with you! Come on, give the girl a quick hug."
        me "But I..."
        "I sighed."
        th "I can't remember the last time I took a picture with someone like that."
        th "I don't know how to hug anybody for a picture..."
        show mi normal pioneer with dspr
        mi "Come on, be more courageous!"
        "She moved her shoulder impatiently."
        scene cg d2_mi_me_polaroid_7dl
        with dissolve
        "And I, with a sigh, put my hand on her shoulder."
        "Awkward - just as I felt - awkward."
        "Dangling hand, insensitive fingers."
        "Like taking a picture with a friend instead of a girl."
        "It came to me too late that a girl should be hugged by the waist, not like this."
        "But... too late!"
        play sound sfx_7dl["snap"]
        scene
        $ renpy.show("cg d2_mi_me_polaroid_7dl", what = Sepia("cg d2_mi_me_polaroid_7dl"))
        show PolaroidFrame_7dl
        with flash
        pause(3)
        me "Cheeeeese."
        "Belatedly I came to my senses."
        scene bg int_dining_hall_sunset
        show mi laugh pioneer at cleft
        with dissolve
        mi "Hee-hee-hee."
        mi "Senechka, you're a miracle."
        hide mi with moveoutleft
        "She giggled and ran away."

    elif alt_my_rival_final.take == 'us':
        $ lp_us -= 1
        th "I won!"
        th "Won?"
        th "Won!!!"
        play music music_7dl["genki"] fadein 3
        "Bang!" with vpunch
        with flash_red
        show us calml pioneer with dissolve
        us "And you didn't win anything!"
        "She looked up at me with a frown."
        us "You didn't play it right, we're replaying it!"
        me "What does that mean, «didn't play right»?"
        show us dontlike pioneer with dspr
        me "I won the tournament! {w}How can I play wrong?"
        us "Silently! You cheated!"
        "She stomped her foot."
        us "You played wrong and cheated!"
        if alt_day2_walk == 1:
            th "Did she find out about the marking? But how?"
            th "If she tells everyone about it now, I'll be lynched on the nearest aspen tree."
        us "You didn't give in to me very well."
        "Ah. Well, that made all the difference."
        hide us with dissolve
        "I laughed and walked away."
        show dv smile pioneer2 with dissolve
        "And Alisa finally got up from her seat and clapped me on the shoulder as she walked past me."
        dv "Congratulations!"
        "And those words made me so happy!"
        th "I won!!!"
        hide dv with dissolve

    elif alt_my_rival_final.take == 'sh':
        stop ambience
        show sh rage pioneer with dissolve
        sh "So, won?"
        play music music_7dl["dead_silence"] fadein 3
        "Slowly he said."
        "He was standing so strangely, there was no way I could make out his eyes because of the glare on his glasses."
        show sh serious pioneer with dspr
        "Yes, and his very pose..."
        "For some reason it reminded me of the character of Elijah Wood from «City of Sins»."
        "He didn't seem to do anything supernatural, but he made me anxious in the same way, just by appearing on the screen."
        "And Shurik made me anxious."
        sh "So you think you can just show up and win my tournament?"
        scene black
        show sh rage pioneer close
        with diam
        sh "Who are you, anyway?"
        sh "You act like you're not seventeen years old anymore."
        show sh rage pioneer close with dspr
        sh "Maybe, you are…"
        scene
        $ renpy.show("bg int_dining_hall_sunset", what = Noir("bg int_dining_hall_sunset"))
        show sh rage pioneer close with dspr:
            xalign .5 yalign .7 zoom 0.7
            ease 0.3 yalign .4 zoom 1.25
        "He took a sharp step in my direction and held out his hand."
        mt "Shurik!"
        stop music fadeout 3
        play ambience ambience_dining_hall_full fadein 5
        show blinking
        scene bg int_dining_hall_sunset with dissolve
        with diam
        show sh upset pioneer with dissolve
        "The obsession of the moment vanished, Shurik transformed from a sinister figure back into an ordinary, slightly distracted, guy."
        "The gray, crushing walls gave way to the reddish light of the rolling sunset."
        "And most importantly -"
        "After all, I'm a winner!"
        hide sh with dissolve
        scene
        call show_tournament_table
        "Electronik put my name on the list of winners."
        el "And after supper..."
        scene bg int_dining_hall_sunset with dissolve
        "Olga Dmitrievna gagged him with her hand."
        th "Right, let it be a surprise. And there's a separate cauldron in hell for those who spoil."

    elif alt_my_rival_final.take == 'mz':
        "Beetle's reaction was discouraging."
        "There wasn't any."
        "But it didn't embarrass me."
        "The important thing is that I won!"
        "Let the others think and do what they want."
        "Even Alisa."
        "No one will believe her now."
        "And that's probably what makes me happiest."
# ---------------------------------------------------- \\ Диалоги

    stop music fadeout 3
    jump alt_day2_prepare_transition_to_supper                                            # ушли ужинать

# ======================================================================================================================
#                                          ОБЩИЕ МЕТКИ ПО ОБРАБОТКЕ ТУРНИРА
# ======================================================================================================================

# ----------------------------------------------------------------------------------
# ОПРЕДЕЛЯЕМСЯ С ОЧЕРЁДНОСТЬЮ ПЕРВОГО ХОДА В КОНЕ
label alt_day2_stipulation_new:
    scene bg int_dining_hall_sunset with dissolve
    python:
        alt_spr_rival = [alt_spr_my_rival,alt_emo_my_rival,alt_acc_my_rival,alt_clot_my_rival]
        alt_spr_my_riv_1 = " ".join(alt_spr_rival)
        renpy.show(alt_spr_my_riv_1,[alt_pos_my_rival])
        renpy.transition(dspr)
    alt_nick_my_rival "Who goes first?"

    $ alt_whose_first_move = renpy.random.choice(['rival', 'player'])
    pause(1)
    if alt_tournament_state == "1_round_start":                             # если первый тур
        "I took a five-ruble coin out of my breast pocket - I really hope no one has any questions about the denomination - and tossed it in the air."
        "The dubious honor of making the first move fell to"
    elif alt_tournament_state == "semifinal_start":                         # если полуфинал
        "I flipped a coin in the air again."
        "No luck this time -"
    elif alt_tournament_state == "final_start":                             # если финал
        "For the third time he threw in the net... I mean, he flipped a coin."
        "Looks like the first move is"
    if alt_whose_first_move == 'rival':
        extend " %(alt_name_my_rival_d)s."
    elif alt_whose_first_move == 'player':
        extend " me."

    return

# ----------------------------------------------------------------------------------
# Победа Семёна в очередной игре тура
label alt_day2_one_play_win_new:
    window auto
    $ alt_day2_my_win += 1                                                  # +1 к победам Семёна
    $ alt_day2_game_played_out += 1                                         # +1 результативная игра
    $ alt_day2_result_current_game = 1                                      # победа Семёна
    jump alt_day2_checking_scores                                           # считаем очки

# ----------------------------------------------------------------------------------
# Поражение Семёна в очередной игре тура
label alt_day2_one_play_fail_new:
    window auto
    $ alt_day2_rival_win += 1                                               # +1 к победам соперника
    $ alt_day2_game_played_out += 1                                         # +1 результативная игра
    $ alt_day2_result_current_game = 2                                      # победа соперника
    jump alt_day2_checking_scores                                           # считаем очки

#-----------------------------------------------------------------------------------
# НИЧЬЯ в очередной игре тура
label alt_day2_one_play_draw_new:
    window auto
    $ show_cards_alt()
    $ renpy.transition(dissolve)
    el "Draw! Play again."
    if alt_tournament_state == "1_round_start":                             # если первый тур
        jump alt_day2_1_tour_re_game                                        # играем первый тур
    elif alt_tournament_state == "semifinal_start":                         # если полуфинал
        jump alt_day2_semifinal_re_game                                  # играем полуфинал
    elif alt_tournament_state == "final_start":                             # если финал
        jump alt_day2_final_re_game                                      # играем финал

#-----------------------------------------------------------------------------------
# Анилизируем счёт по играм в этапе
label alt_day2_checking_scores:
    scene bg int_dining_hall_sunset with dissolve
    if alt_day2_my_win == alt_day2_rival_win:                                                   # если счёт равный
        if alt_day2_game_played_out == 0:                                                       # ещё не играли (0:0)
            if alt_day2_gamblers_final[0].take == 'me':                                         # если 1-й игрок — Семён
                $ alt_day2_upper_gambler_name = "Semyon"
                $ alt_day2_bottom_gambler_name = alt_name_my_rival_t
            else:
                $ alt_day2_upper_gambler_name = alt_name_my_rival_t
                $ alt_day2_bottom_gambler_name = "Semyon"
            show el normal pioneer far at left with dissolve
            el "Less than a minute left until the final game between %(alt_day2_upper_gambler_name)s and %(alt_day2_bottom_gambler_name)s, the score is still 0-0."
            "Electronik commented on the game as best he could."
            hide el with dissolve
            return
        else:                                                                                   # если 1:1
            call alt_day2_current_game_end_compare_hands                                        # сравнение комбинаций по итогам игры
            show el serious pioneer far at left with dspr
            el "So, at the end of the two games we have a draw so far; the winner will be determined in the decisive game."
            el "And who will go first - now we'll play, and the portable random number generator will help us in this."
            "Electronik took a coin out of his pocket."
            el "Heads? Tails?"
            menu:
                "Heads":
                    $ alt_whose_first_move_choice = 1
                "Tails":
                    $ alt_whose_first_move_choice = 0
            $ alt_whose_first_move_random = renpy.random.choice([0, 1])
            if alt_whose_first_move_random == 0:
                "El flipped a coin, tails came out."
            else:
                "The tossed coin fell on heads."
            $ renpy.block_rollback()                                                                # блокируем роллбак
            if alt_whose_first_move_choice == alt_whose_first_move_random:
                if alt_name_my_rival_i == "Shurik":
                    el "Guessed right. Shurik will be the first one to go{nw}"
                else:
                    el "Guessed right. The first one to go will be %(alt_name_my_rival_i)s{nw}"
                if alt_whose_first_move == 'player':
                    extend ", like in the first round."
                else:
                    extend ", like in the second round."
                $ alt_whose_first_move = 'rival'
            else:
                el "Missed. So the first move is yours{nw}"
                if alt_whose_first_move == 'player':
                    extend ", like in the second round."
                else:
                    extend ", like in the first round."
                $ alt_whose_first_move = 'player'
            scene bg int_dining_hall_sunset with dissolve
            jump alt_day2_transition_to_game
    elif alt_day2_my_win > alt_day2_rival_win:                                                  # Семён ведёт в счёте
        call alt_day2_current_game_end_compare_hands                                            # сравнение комбинаций по итогам игры
        if alt_day2_game_played_out == 1:                                                       # по итогам первой игры
            show el normal pioneer far at left with dspr
            if alt_whose_first_move == 'rival':                                                 # если первым ходил соперник
                el "Semyon, you get the first move now."
                $ alt_whose_first_move = 'player'                                               # то первым ходит Семён
            else:                                                                               # если ходил Семён
                el "The right of the first move passes to %(alt_name_my_rival_d)s."
                $ alt_whose_first_move = 'rival'                                                # то первым ходит соперник
            scene bg int_dining_hall_sunset with dissolve
            jump alt_day2_transition_to_game                                                    # переход к игре
        else:                                                                                   # по итогам тура
            show el normal pioneer far at left with dspr
            el "Semyon wins against %(alt_name_my_rival_r)s with the score of %(alt_day2_my_win)d-%(alt_day2_rival_win)d."
            scene bg int_dining_hall_sunset with dissolve
            if alt_tournament_state == "final_start":                                           # если финал
                jump alt_day2_final_win_end_new                                                 # победа в финале
            elif alt_tournament_state == "semifinal_start":                                     # если полуфинал
                jump alt_day2_semifinal_win_end_new                                             # победа в полуфинале
            elif (alt_tournament_state == "1_round_start"):                                     # если первый тур
                jump alt_day2_participate_win_end_new                                           # победа в 1 туре
    else:                                                                                       # соперник выигрывает
        call alt_day2_current_game_end_compare_hands                                            # сравнение комбинаций по итогам игры
        if alt_day2_game_played_out == 1:                                                       # по итогам первой игры
            show el normal pioneer far at left with dspr
            if alt_whose_first_move == 'rival':                                                 # если первым ходил соперник
                el "In the next round, Semyon will be the first to go."
                $ alt_whose_first_move = 'player'                                               # то первым ходит Семён
            else:                                                                               # если ходил Семён
                el "%(alt_name_my_rival_i)s, you get the first move now."
                $ alt_whose_first_move = 'rival'                                                # то первым ходит соперник
            scene bg int_dining_hall_sunset with dissolve
            jump alt_day2_transition_to_game                                                    # переход к игре
        else:                                                                                   # по итогам тура
            show el normal pioneer far at left with dissolve
            el "%(alt_name_my_rival_i)s wins, the current score is %(alt_day2_rival_win)d-%(alt_day2_my_win)d."
            scene bg int_dining_hall_sunset with dissolve
            if alt_tournament_state == "final_start":                                           # если финал
                jump alt_day2_final_fail_end_new                                                # поражение в финале
            elif alt_tournament_state == "semifinal_start":                                     # если полуфинал
                jump alt_day2_semifinal_fail_end_new                                            # поражение в полуфинале
            elif (alt_tournament_state == "1_round_start"):                                     # если первый тур
                jump alt_day2_participate_fail_end_new                                          # поражение в 1 туре


#-----------------------------------------------------------------------------------
# Возвращаемся к обратно к игре на соответствующий этап
label alt_day2_transition_to_game:                                                    # переход к игре
    if alt_tournament_state == "final_start":                                         # если финал
        jump alt_day2_final_re_game                                                   # играем финал
    elif alt_tournament_state == "semifinal_start":                                   # если полуфинал
        jump alt_day2_semifinal_re_game                                               # играем полуфинал
    elif (alt_tournament_state == "1_round_start"):                                   # если первый тур
        jump alt_day2_1_tour_re_game                                                  # играем 1 тур

#-----------------------------------------------------------------------------------
# Результат ИГРЫ (сравниваем и оцениваем комбинации)
label alt_day2_current_game_end_compare_hands:                                      # Результат текущей игры
    $ alt_day2_current_rout_status = 0                                              # текущая игра закончена
    if alt_day2_result_current_game == 1:                                           # победа Семёна
        $ alt_day2_summary_poker_1, alt_day2_summary_poker_2 = alt_comparison_poker_hands(alt_my_poker_hand, alt_rival_poker_hand, 'me', alt_spr_my_rival)
        if alt_day2_game_played_out == 1:                                           # сыграли раз
            $ alt_day2_current_rout_status = 1                                      # Семён выиграл 1-ю игру
        elif alt_day2_game_played_out == 2:                                         # сыграли два раза
            if alt_day2_rival_win == 1:                                             # соперник выиграл один раз
                $ alt_day2_current_rout_status = 2                                  # Семён отыгрался

    elif alt_day2_result_current_game == 2:                                         # победа соперника
        $ alt_day2_summary_poker_1, alt_day2_summary_poker_2 = alt_comparison_poker_hands(alt_rival_poker_hand, alt_my_poker_hand, alt_spr_my_rival, 'me')
        if alt_day2_game_played_out == 1:                                           # сыграли раз
            $ alt_day2_current_rout_status = 3                                      # соперник выиграл 1-ю игру
        elif alt_day2_game_played_out == 2:                                         # сыграли два раза
            if alt_day2_my_win == 1:                                                # Семён выиграл один раз
                $ alt_day2_current_rout_status = 4                                  # соперник отыгрался

    $ alt_day2_result_current_game = 0                                              # результат текущей игры = 0 (ничья)
    "%(alt_day2_summary_poker_1)s"
    "%(alt_day2_summary_poker_2)s"

    if alt_day2_current_rout_status in [1,2,3,4]:                                   # если игра не закончена
        call alt_day2_current_game_ending_dialogs                                   # вызов диалога по текущей ситуации
    else:
        pass
    return

#-----------------------------------------------------------------------------------
# диалоги по итогам очередной игры (выиграл/проиграл-сравнял счёт)
# сортировка — сначала по персонажам, потом — по ситуациям (0-проверка, 1 — Семён выиграл 1-ю, 2 — Семен сравнял счёт, 3 — соперник выиграл 1-ю, 4 — соперник сравнял счёт)
# ---------------------------------------------------------
# тут же "накручиваем" скилл соперникам по итогам очередной игры

label alt_day2_current_game_ending_dialogs:
# Лена
    if alt_spr_my_rival == 'un':
        if alt_day2_current_rout_status == 1:                   # если Семён выиграл первый раз
            if alt_day2_gambler_behavior != 'succumb':          # если не "поддавки"
                $ alt_day2_gambler_skill += 1                     # увеличиваем навык

            "Apparently, Lena's luck skill is even lower than mine."
            show un smile pioneer at cright with dissolve
            "But she doesn't seem to be too upset about it."
            un "Good job."
            "Praised Lena."
            me "Thank you."
            show un shy pioneer at cright with dspr
            "And a second later she was blushing."


        elif alt_day2_current_rout_status == 2:                 # если Семён отыгрался
            if alt_day2_gambler_behavior != 'succumb':          # если не "поддавки"
                $ alt_day2_gambler_skill += 1                     # увеличиваем навык

            show un shy pioneer at cright with dissolve
            "Lena's gaze wandered from me to the cards on the table, and so on several times."
            "She obviously wanted to say something, but she couldn't get over her embarrassment."
            "I don't know what could have put this, a couple of minutes ago, serious, girl in a blush."
            dreamgirl "Idiot."
            "Subconscious muttered."
            "Anyway, I'm not going to force words out of Lena."


        elif alt_day2_current_rout_status == 3:                 # и она выиграла первый раз
            if alt_day2_gambler_behavior == 'succumb':          # если "поддавки"
                $ alt_day2_gambler_skill += 1                     # увеличиваем навык

            if alt_day2_gambler_behavior == 'succumb':
                "Yeah. I obviously didn't play my best. And Lena obviously noticed that."
                show un serious pioneer at cright with dissolve
                "Her judgmental gaze awakened in me a vague sense of guilt."
                "As if it were my fault for losing."
                dreamgirl "Yes, it was."
                dreamgirl "The girl gave in to you, but you screwed up anyway."
                th "Evidence?"
                dreamgirl "Right there on her face."
                "Unclearly answered the inner voice and fell silent."
            else:
                "Lena proved to be a serious adversary, hiding a couple of aces up her sleeve."
                show un shy pioneer at cright with dissolve
                "I didn't expect her to be so stubborn."
                "Apparently, she was surprised herself."


        elif alt_day2_current_rout_status == 4:                 # и она отыгралась
            if alt_day2_gambler_behavior == 'succumb':          # если "поддавки"
                $ alt_day2_gambler_skill += 1                     # увеличиваем навык

            if alt_day2_gambler_behavior == 'succumb':          # если "поддавки"
                show un sad pioneer at cright with dissolve
                "Lena herself wasn't too happy about the little victory - on the contrary, she looked at me as if she was guilty of something."
                dreamgirl "Don't be an oaf and cheer up."
                th "I know without you."
                me "Well done, Len. Well played."
                show un shy pioneer at cright with dspr
                un "T-thank you."
                "The girl's voice was agitated; she couldn't believe what had happened."
                "That's why she flinched when Electronik said her name loudly."
            else:
                "It looks like Lena has no intention of giving up."
                show un smile pioneer at cright with dissolve
                un "Don't expect an easy victory."
                "Just now she was sitting there embarrassed, and now she's cheering me on!"
                "That's what gambling does to people."
                show un shy pioneer at cright with dspr
                "The effect, however, was short-lived."

# Славя
    elif alt_spr_my_rival == 'sl':
        if alt_day2_current_rout_status == 1:                   # если Семён выиграл первый раз
            $ alt_day2_gambler_skill += 1                     # увеличиваем навык

            show sl smile pioneer at cright with dissolve
            "Slavya doesn't seem the least bit saddened by the defeat."
            sl "Cards aren't my thing after all."
            me "You're just unlucky, that's all."
            show sl laugh pioneer at cright with dspr
            sl "It's not about luck, I really don't know how!"
            show sl smile2 pioneer at cright with dspr
            sl "I've tried it many times, but it's no use."
            sl "I don't understand the point of this stupid game."
            me "So why do you play?"
            show sl smile pioneer at cright with dspr
            sl "Camp event, Semyon. Everyone is obligated to attend."






        elif alt_day2_current_rout_status == 2:                 # если Семён отыгрался
            $ alt_day2_gambler_skill += 1                     # увеличиваем навык

            show sl smile pioneer at cright with dissolve
            sl "See, you can do it when you want!"
            me "I just got lucky."
            show sl normal pioneer at cright with dspr
            "Slavya obviously wanted to hear more from me, but I didn't know what else to add here."
            sl "Now we'll see if it's luck or talent."
            th "The second, unequivocally."
            th "Talented loser."
            "It was as if Slavya had heard my thoughts and tried to cheer me up."
            show sl happy pioneer at cright with dspr
            sl "Cheer up!"



        elif alt_day2_current_rout_status == 3:                 # и она выиграла первый раз


            show sl surprise pioneer at cright with dissolve
            me "Is something wrong?"
            show sl normal pioneer at cright with dspr
            sl "No, it's just..."
            sl "I'm not very good at cards."
            me "How very is your 'not good'?"
            show sl sad pioneer at cright with dspr
            sl "I've tried it many times, but it's no use."
            sl "I don't understand the point of this stupid game."
            "I thought I was the worst player here."
            "The activist has succeeded in many things, except gambling."
            "But even she could beat me."

        elif alt_day2_current_rout_status == 4:                 # и она отыгралась

            show sl angry pioneer at cright with dissolve
            sl "You did it on purpose, didn't you?"
            "And I, trying to keep a nonchalant expression on my face, replied:"
            me "Not at all."
            sl "That's not true! You know that I..."
            pause(1)
            show sl normal pioneer at cright with dspr
            sl "Okay, never mind."

# Алиса
    elif alt_spr_my_rival == 'dv':
        if alt_day2_current_rout_status == 1:                   # если Семён выиграл первый раз
            $ alt_day2_gambler_skill += 1                     # увеличиваем навык

            show dv surprise pioneer2 at cright with dissolve
            "The redhead was in mild shock."
            "What can I say, I know how to surprise. Especially myself."
            me "Is Mademoiselle ready to fall to her knees and weep from defeat?"
            show dv smile pioneer2 at cright with dspr
            "My line brought Alisa out of her stupor and stirred her up."
            dv "No way!"
            show dv angry pioneer2 at cright with dspr
            dv "Mademoiselle is ready to punch a cavalier in the face."
            "I almost laughed."

        elif alt_day2_current_rout_status == 2:                 # если Семён отыгрался
            $ alt_day2_gambler_skill += 1                     # увеличиваем навык
            $ alt_day2_gambler_behavior = 'gamble'          # и начинает рисковать

            show dv guilty pioneer2 at cright with dissolve
            "It's nice to see the mask of arrogance falling from Dvachevskaya's face."
            "I didn't even say anything - I silently picked up that very mask and tried it on myself."
            show dv angry pioneer2 at cright with dspr
            "Alisa didn't like it, Alisa clenched her fists."
            if herc or loki:
                "I don't care."
                "Dvachevskaya's threats don't scare me."
                "I continued to stare at the redhead with defiance."
                pause(1)
                show dv guilty pioneer2 at cright with dspr
                "The winner of the staring contest was me."
                "Alisa unclenched her fists and looked away."
                if herc:
                    "I even felt a little embarrassed that I seemed to have offended the girl."
                    "But not enough to rush to apologize."
                    "Alisa has to figure out for herself what she did wrong."

                elif loki:
                    dreamgirl "There you go, you hurt the girl."
                    th "She deserved it."

            else:
                "I raised my hands in a conciliatory gesture."
                me "Hush, hush, I was just kidding."
                dv "Another one of those jokes..."
                me "Got it, not stupid."




        elif alt_day2_current_rout_status == 3:                 # и она выиграла первый раз
            $ alt_day2_gambler_behavior = 'defense'              # садится в оборону

            show dv grin pioneer2 at cright with dissolve
            "Alisa looked at me with a sneering grin."
            "I bet she's glad she got a confirmation of her words."
            "And it's infuriating."
            me "Aren't you celebrating your victory a little early, Dvachevskaya?"
            show dv laugh pioneer2 at cright with dspr
            dv "I don't think so."
            "I was about to spit venom at the redhead when I heard my inner voice retort."
            dreamgirl "You fool, she's provoking you on purpose, and you're falling for it!"
            dreamgirl "If you want to rub Dvachevskaya's nose in it, you need to stay calm."
            th "That makes sense."
            show dv normal pioneer2 at cright with dspr
            "Alisa gave a sort of disappointed sniffle - clearly she was expecting a different reaction."
            th "But no way."

        elif alt_day2_current_rout_status == 4:                 # и она отыгралась
            $ alt_day2_gambler_behavior = 'gamble'          # и начинает рисковать

            show dv laugh pioneer2 at cright with dissolve
            "DvaChe is pretty damn pleased with herself."
            me "Why are you grinning?"
            show dv grin pioneer2 at cright with dspr
            dv "Can't I?"
            dreamgirl "You can!"
            th "Whose side are you on anyway?"
            dreamgirl "My own."
            dreamgirl "And you, you fool, didn't realize the girl was flirting with you."
            th "Dvachevskaya? Flirting?"
            th "I'll never believe it. Wrong type."
            dreamgirl "Pfft... As if you know too much about them."
            "The inner voice snorted and went quiet."

# Мику
    elif alt_spr_my_rival == 'mi':

        if alt_day2_current_rout_status == 1:                   # если Семён выиграл первый раз
            $ alt_day2_gambler_skill += 1                     # увеличиваем навык

            stop music fadeout 2
            show mi smile pioneer at cright with dissolve
            mi "Well done, Senechka. You play well."
            play music music_7dl["what_am_i_doing_here"] fadein 1
            me "It's all luck."
            show mi shocked pioneer at cright with dspr
            mi "Really? And I thought you were an experienced player."
            "If that's Miku's tactic - to hit my self-esteem with every word - she's succeeded."
            dreamgirl "You'd think you had self-esteem."
            show mi sad pioneer at cright with dspr
            mi "I have no luck at all at cards."
            mi "I don't know how to play them! I don't understand!{w} Or I'm just stupid."
            mi "You're not stupid."
            "Though I don't know you well enough to say so."
            dreamgirl "So get to know her {i}closer{/i}."
            "It sent shivers down my spine."
            "The intonations that crept into the voice of the inner scrooge reminded me of our charming nurse."

            me "It's just that each person is better at something than the other."
            if loki:
                me "I know firsthand that learning to play even one instrument is not easy, but you are able to play several at once."
                me "It's not just talent, it's hard work."
                me "Stupid people can't do that."
                me "As a rule they..."
                "The words stick in my throat."
                mi "As a rule - they what?"
                me "Difficulties break them quickly."
                th "Sometimes even physically."
                me "They get stuck in one place and find a thousand excuses to whine about the unfulfilled instead of at least one reason to move forward to their dreams."
                dreamgirl "Just like...?"
                th "Just like me."
            elif herc:
                me "For example, I didn't do well with music."
                th "But I excelled in the use of knives and firearms."
                me "But you succeeded."
                me "Talent or persistence, it doesn't matter."
                me "Stupid people can't do that."
            elif dr:
                me "Gambling is not your thing. That's all."

            mi "You're probably right."
            show mi smile pioneer at cright with dspr
            mi "No, that's how it is!"
            show mi smile pioneer at cright with dspr
            mi "The one who really knows how to play cards is Alisa."
            "Dvachevskaya?"

            scene bg ext_dining_hall_near_day
            show dv smile pioneer2
            show prologue_dream
            with flash

            "I didn't doubt it at all."
            "A man with such a smug face wouldn't offer a wager if he wasn't sure of winning."
            if (alt_day2_dv_ultim != 1) and (alt_day2_walk == 1):
                dreamgirl "Why didn't you bet then, cheater?"

            scene bg int_dining_hall_sunset
            show mi shy pioneer at cright
            with flash

            show mi normal pioneer at cright with dspr
            mi "We played with her once, and I lost six times in a row!"

            menu:
                "Ask her about that incident":

                    $ lp_mi += 1

                    me "You, and cards? With Dvachevskaya?"
                    me "You're, what do you call it... a kamikaze?!"
                    show mi laugh pioneer at cright with dspr
                    mi "You say that too! It just came out on its own somehow!"
                    "Apparently it's the norm with women that 'it' always comes out on its own."
                    show mi normal pioneer at cright with dspr
                    mi "I was sitting in a club at the time, painting the notes of one of my songs for the piano."
                    mi "It was very beautiful. I think it was even better than the original. More melodic, more emotional!"
                    show mi smile pioneer at cright with dspr
                    mi "Well, I remember exactly that it was Wednesday!"
                    show mi surprise pioneer at cright with dspr
                    mi "Although, no, that day Ulyana..."
                    "I was beginning to regret my decision to keep the dialogue going into a monologue, when Miku herself returned to the subject."
                    show mi normal pioneer at cright with dspr
                    mi "Anyway, never mind!"

                    scene bg int_musclub_day
                    show prologue_dream
                    with flash

                    mi "I was almost done with the song..."
                    mi "...when suddenly a disheveled Alisa burst into the club!"

                    play sound sfx_open_door_strong
                    with vpunch
                    show dv scared pioneer2 far at center behind prologue_dream
                    with moveinright

                    dv "{i}If the Hat comes in, I'm not here!{/i}"

                    hide dv with moveoutleft
                    play sound sfx_close_door_clubs_nextroom
                    with vpunch

                    mi "And hid in the back room."

                    scene bg int_dining_hall_sunset
                    show mi shocked pioneer at cright
                    with fade

                    mi "At first I was frightened: what had Alisa done to be so frightened of the counselor?"
                    show mi happy pioneer at cright with dspr
                    mi "Olga Dmitrievna is not evil. She is strict, but kind."
                    "Miku is just as naive as she is."
                    dreamgirl "Will you take advantage?"
                    th "You're all giggles and laughs and all about one thing."
                    dreamgirl "All about the good, the eternal."
                    show mi dontlike pioneer at cright with dspr
                    mi "Anyway, Alisa scared me."
                    show mi upset pioneer at cright with dspr
                    mi "I froze and kept listening: what if someone is really coming?"
                    show mi normal pioneer at cright with dspr
                    mi "Sat like that for ten minutes until Alisa decided to come out of hiding."
                    show mi laugh pioneer at cright with dspr
                    mi "You should have seen her face!"
                    me "Yeah, I can imagine..."

                    scene bg int_musclub_day
                    show prologue_dream
                    with flash
                    show dv surprise pioneer2 at fleft behind prologue_dream with moveinleft
                    show dv surprise pioneer2 at fleft behind prologue_dream with dissolve
                    show dv normal pioneer2 at fleft behind prologue_dream with dspr

                    mi "When Alisochka was about to leave, I asked her:"
                    show dv normal pioneer2 at cright behind prologue_dream with move
                    mi "{i}Oh, Alisa, what have you done? Why would Olga-san be looking for you?{/i}"
                    show dv smile pioneer2 at cright behind prologue_dream with dspr
                    mi "She just waved it off, you know!"
                    mi "Said she was going to tell me sometime later, that she had some unfinished business."
                    "My money's on Dvachevskaya bluntly talking her way out of it."
                    "Miku's talkativeness puts people off."
                    mi "{i}What's the case? Urgent? May I…{/i}"
                    show dv laugh pioneer2 at cright behind prologue_dream with dspr
                    dv "{i}No. It's a secret!{/i}"
                    mi "{i}Come on, Alisa-a-a! I'm curious. Tell me about it!{/i}"
                    show dv grin pioneer2 at cright behind prologue_dream with dspr
                    dv "{i}Wanna bet?{/i}"
                    dv "{i}You win against me, and I'll tell you what that was.{/i}"
                    mi "And pulled out the cards."
                    mi "{i}Oh, I don't know how. I mean, I've never tried it, so…{/i}"
                    show dv smile pioneer2 at cright behind prologue_dream with dspr
                    dv "{i}That's okay!{/i}"
                    show dv laugh pioneer2 at cright behind prologue_dream with dspr
                    dv "{i}If you don't want to, we'll teach you. If you can't, we'll make you!{/i}"

                    scene bg int_dining_hall_sunset
                    show mi smile pioneer at cright
                    with flash2

                    mi "And that's the story."
                    show mi smile pioneer at cright with dspr
                    mi "Alisa tried to teach me during the game, but I never understood anything!"
                    me "I see."
                    $ lp_dv += 1
                    me "And Dvachevskaya is not as bad as she looks."
                    stop music fadeout 3
                    mi "Alisochka is very good. You just need to get to know her better."

                "Ignore her":

                    $ lp_mi -= 1
                    stop music fadeout 3
                    me "I see."
                    show mi sad pioneer at cright with dspr
                    pause(1)
                    hide mi with dissolve

                    #if not(final):
                    #    "Я отвернулся к другим столам, посмотреть, как играет кто-нибудь из моих потенциальных соперников."
                    #    "Мику по ряду причин в их число уже не входила." # это же промежуточные итоги, Мику вполне может ещё отыграться

            play music music_list["my_daily_life"] fadein 2

        elif alt_day2_current_rout_status == 2:                 # если Семён отыгрался
            $ alt_day2_gambler_skill += 1                     # увеличиваем навык

            show mi smile pioneer at cright with dissolve
            "Miku wasn't the least bit upset about losing."
            mi "Well done, Senechka, well fought back."
            show mi upset pioneer at cright with dspr
            mi "So, since you won, now the final round awaits us, right?"
            "Clarified Miku."
            show mi laugh pioneer at cright with dspr
            mi "We may be comrades, but I won't give in!"
            "The first time I heard it, I didn't think much of it and let it pass me by, but..." # Возможен исход, при котором здесь "Сенечка" упоминается впервые. Лучше убрать эту строку вообще. ## Нет, здесь Семён отыгрался, значит, первый раз должна была выиграть Мику (см. alt_day2_current_rout_status == 3). Там Сенечка упоминается 2 раза.
            me "Miku, why «Senechka»?"
            show mi shocked pioneer at cright with dspr
            mi "Huh?"
            show mi shy pioneer at cright with dspr
            "Face color change detected."
            "I didn't think a simple question could embarrass our Japanese girl."
            show mi happy pioneer at cright with dspr
            mi "Because Semyon is too rude and formal, and Senechka sounds nice."

        elif alt_day2_current_rout_status == 3:                 # и она выиграла первый раз
            show mi shy pioneer at cright with dissolve
            mi "Did I win?"
            me "Yes."
            show mi happy pioneer at cright with dspr
            mi "Yay!"
            show mi smile pioneer at cright with dspr
            mi "Senechka, don't worry - there's nothing wrong with losing."
            mi "I didn't understand how to play this game until the end, either. You could say I got lucky."
            me "Uh-huh."
            show mi sad pioneer at cright with dspr
            mi "You were upset after all. Don't worry, losing is also an experience."
            show mi smile pioneer at cright with dspr
            mi "But I understand you. I was upset too when I lost to Alisa at cards."
            th "Miku played cards with Alisa?"
            dreamgirl "And you thought the whole world revolved around you, and the campers were just waiting for His Majesty to show up on the horizon?"
            dreamgirl "Everyone has their own life, their own story, and it doesn't begin with your arrival, it doesn't end with your departure."
            dreamgirl "Whether you need it is an important question, but a separate one."
            show mi serious pioneer at cright with dspr
            th "Don't you think you're being too much of a smartass?"
            dreamgirl "Of the two of us, I'm the only one who uses the brain for its intended purpose."
            dreamgirl "And since I'm the crutch for the mentally handicapped in this duo, here's some more advice for you: stop talking to yourself and talk to a girl."
            show mi normal pioneer at cright with dspr
            mi "Senechka, are you okay? Your eye is twitching."
            me "I'm fine. Keep going."

        elif alt_day2_current_rout_status == 4:                 # и она отыгралась
            show mi surprise pioneer at cright with dissolve
            "Hafu stared at the cards for a long time and couldn't understand the obvious."
            "Even Electronik came up to us, nodding affirmatively at her."
            show mi normal pioneer at cright with dspr
            mi "Did I win?"
            me "Yes."
            show mi happy pioneer at cright with dspr
            mi "Yay!"

            if alt_result_dv_1_tour > 2 and alt_result_dv_semifinal > 2:
                show mi laugh pioneer at cright with dspr
                mi "Alisa! See, I know how to play! I was able to win back!"
                "The redhead at the next table blushed."
                "If I were Alisa, I wouldn't blush and instead would pretend I didn't know Miku."

            show mi grin pioneer at cright with dspr
            mi "Hold on, Senechka! I'm going to win you!" # "Выиграю тебя" — так задумано или меняем на "обыграю"? ## задумано
            show mi smile pioneer at cright with dspr
            me "Yeah, good luck."
            dreamgirl "Oh please, you'll need it yourself."
            th "You doubt my abilities?"
            dreamgirl "I do share a head with you, after all. So I don't doubt - I know."

# Ульяна
    elif alt_spr_my_rival == 'us':
        if alt_day2_current_rout_status == 1:                   # если Семён выиграл первый раз
            $ alt_day2_gambler_skill += 1                     # увеличиваем навык

            show us angry pioneer at cright with dissolve
            us "Why didn't you give in to me?!"
            me "Why should I?"
            us "Because I'm a kid and you're an adult! You have to give in!"
            me "Legally speaking, I'm still a child, too."
            dreamgirl "Almost turning 30 as a child."
            th "Shush!"
            "However, the redhead needs some kind of reassurance."
            "She's got a wreath on her forehead. Almost as if she's about to jump up on the table and start beating me."
            if herc:
                dreamgirl "And you 'oop!' - into the bear's grip - and throw her back!"
                th "I wasn't trained to beat up children!"
                th "A thumb grip will be more than enough..."
            me "Calm down, it's only the first round."
            me "You'll still have a chance to win it back, and with my luck the odds are pretty good."
            show us dontlike pioneer at cright with dspr
            us "Watch out, or else..."
            if herc or loki:
                me "Else what?"
                dreamgirl "A scolopendra in your pants, that's what."
                th "I'm so scared I'm shaking already."
            else:
                me "Else what?.."
                "I tried to add more confidence to my voice, but it was frankly weak."
                dreamgirl "Come on, are you really scared of a little girl?"
                Dreamgirl "So she shoves a scolopendra down your pants, so what? Deadly?"
                th "Always expect the worst so you can rejoice in the best."
            show us grin pioneer at cright with dspr
            if (counter_sl_7dl == 0) and dr:
                us "Or I'll douse you again!"
            else:
                us "You'll see!"
            us "If you don't give me all the best cards you have."
            me "Deal."
            dreamgirl "Really?"
            if loki:
                th "Perhaps."
            elif herc:
                th "That depends on her acting."
            else:
                th "Random is our judge."

        elif alt_day2_current_rout_status == 2:                 # если Семён отыгрался
            $ alt_day2_gambler_skill += 1                     # увеличиваем навык

            show us dontlike pioneer at cright with dissolve
            us "Not fair!"
            if loki:
                "The temptation to return the taunt was too great."
                me "Well, you said yourself that the game is simple and only a fool wouldn't understand it."
                show us angry pioneer at cright with dspr
                "Oh yes, the swollen vein on the redhead's forehead was a balm to my soul."
                "And once the little one has beaten me, probably with her feet, I'll need it for my body, too."
                "Luckily, I was saved by the timely voice of Electronik."
            elif herc:
                me "Not everything in the world is measured by honesty."
                us "{i}Not everything in the world is measured by honesty.{/i}"
                "Ulyana mockingly repeated."
                show us grin pioneer at cright with dspr
                us "Expect an honest cockroach under the pillow."
            elif dr:
                th "I won by the will of Random, and the concept of honesty does not apply to it."
                dreamgirl "Say that out loud, and you'll get a well-deserved kick in the knee or a cockroach in your soup."
                th "That's why I'd rather not say anything."
                "Ulyana threatened to put cockroaches under my pillow, or to snoop and douse me with a bucket of water."
                "I nodded silently, nodding occasionally."
                show us normal pioneer at cright with dspr
                "In the end, the redhead changed from anger to mercy."
                show us grin pioneer at cright with dspr
                "But if I somehow win in the final round as well, something…{w=0.5} wicked will be waiting for me."
                "That's the way it is."
            elif d3:
                me "А ты задонатила на победу?"
                us "Чего, это как?"
                me "Пожертвование, мелкая."
                us "Не буду я тебе до… да… жертвовать."
                us "Ты же не больной, руки-ноги целы."
                us "Пожертвования тебе не нужны."
                me "Зря. В моём…"
                "Я осёкся."
                "Чуть не сказал Ульяне «в моём времени»."
                "В её же времени о таком не слышали, но наверняка пресекалось бы и считалось тунеядством."
                "Никогда не понимал таких людей, что в этом такого?"
                "Очередной вид заработка же."
                "Не всем же стоять по восемь часов у станка, есть бойцы интеллектуального фронта."
                dreamgirl "Этого милого светлого мальчика зовут Семён."
                dreamgirl "Ему срочно нужна ваша помощь!"
                dreamgirl "Он страдает от тяжелого и неизлечимого заболевания."
                dreamgirl "Он — ох…"

        elif alt_day2_current_rout_status == 3:                 # и она выиграла первый раз

            show us surp1 pioneer at cright with dissolve
            us "Wow! I didn't know this could happen!"
            me "What is this?"
            us "How? How can you play so badly? It's a simple game!"
            show us laugh pioneer at cright with dspr
            us "Only a nerd like you wouldn't understand."
            th "You little bugger!"

            if (counter_sl_7dl >= 1) or dr:
                "And how I wanted to respond with something toxic, but it's silly to be offended by a child, isn't it?"
                dreamgirl "Appearances can be deceiving. Look at her and yourself and compare."
                dreamgirl "The age difference is insignificant."
                th "What are you implying?"
                "The inner voice answered with silence."

            else:

                if loki:
                    me "Maybe I should give you another splash of water. To calm your fervor?"
                    show us grin pioneer at cright with dspr
                    us "And you try to catch up!"
                    me "I won't take the speed, I'll take the cunning."
                    show us smile pioneer at cright with dspr
                    me "Once you're alone in the cabin, I'll sneak up behind you and…"

                elif herc:
                    me "Familiar with vitamin «Р»?"
                    show us smile pioneer at cright with dspr
                    us "No! What's that?"
                    me "Keep it up..."
                    "My hand rested on the belt buckle."
                    me "...and you'll find out."
                    show us grin pioneer at cright with dspr
                    us "Okay!"




        elif alt_day2_current_rout_status == 4:                 # и она отыгралась

            show us grin pioneer at cright with dissolve
            us "Well done, Syomka. You're on the road to correction!"
            "Praised Ulyanka."
            dreamgirl "You're a fool after all."
            th "Well, maybe it's for the best."
            dreamgirl "Just a reminder: the game isn't over yet."

# Шурик
    elif alt_spr_my_rival == 'sh':
        $ alt_day2_gambler_skill += 1                     # увеличиваем навык — Шурику без вариантов

# ============================================================= эксперименты Шурика
        if alt_day2_current_rout_status in [3,4]:                               # Если Шурик выиграл игру
            pass
        else:                                                                   # если Шурик проиграл игру
            if alt_day2_gambler_behavior == 'defense':                          # если Шурик защищался
                $ alt_day2_gambler_behavior = 'gamble'                          # смена стратегии
            elif alt_day2_gambler_behavior == 'gamble':                         # если Шурик рисковал
                $ alt_day2_gambler_behavior = 'defense'                         # смена стратегии
# =============================================================

        if alt_day2_current_rout_status == 1:                   # если Семён выиграл первый раз

            show sh surprise pioneer at cright with dissolve
            sh "I underestimated you."
            me "Well, thank you."
            show sh smile pioneer at cright with dspr
            sh "Even with my sufficiently high probability of winning, you were dealt cards that defeated me."
            "Was he trying to figure out what cards I had?"
            "Random doesn't spare those."
            show sh serious pioneer at cright with dspr
            "Shurik extended his hand to me as a sign of respect."
            if herc:
                "I answered."
                show sh upset pioneer at cright with dspr
                "When the pioneer grimaced a little, I knew I'd overdone it a little."
                "He'll think I'm trying to take him out of the game."
                dreamgirl "And you aren't?"
                th "What's the point of that? It's not like we're playing poker for money."
            elif loki:
                "I've always been squeamish about handshakes and didn't respond."
                show sh normal pioneer at cright with dspr
                "The cyberneticist just sniggered and shrugged his shoulders."
            else:
                "I tentatively took his hand and grimaced."
                show sh smile pioneer at cright with flash_red
                th "It's like being squeezed in a vise."
                th "He did it on purpose, no other way."
                dreamgirl "No, you're just a wimp."


        elif alt_day2_current_rout_status == 2:                 # если Семён отыгрался

            show sh serious pioneer at cright with dissolve
            sh "I underestimated you."
            th "You're not the only one."
            me "Well, thank you."
            sh "Even with my rather high probability of winning you got cards that defeated me."
            "Shurik extended his hand to me as a sign of respect."
            if herc:
                "I answered."
                show sh upset pioneer at cright with dspr
                "When the pioneer grimaced a little, I knew I'd overdone it a little."
                "He'll think I'm trying to take him out of the game."
                dreamgirl "And you're not?"
                th "And you keep your mouth shut at all, traitor! I didn't give you a word."
                dreamgirl "As if need your permission."
                dreamgirl "Well, let's see if it was luck or if you really know how to do something."
            elif loki:
                "I've always been squeamish about handshakes and didn't respond."
                show sh normal pioneer at cright with dspr
                "The cyberneticist just sniggered and shrugged his shoulders."
                dreamgirl "To victory over other people's heads?"
                th "I don't think so. He's more serious and has every chance of winning."
                dreamgirl "So you've given up."
                th "No. I just won't lose that way - let him scratch out a win for himself."
            else:
                "I tentatively took his hand and grimaced."
                show sh upset pioneer at cright with flash_red
                th "It's like being squeezed in a vise!"
                "That's something I know how to do, with a 99%% chance of drawing an unlucky ticket."
                "My torture in the tournament could have been over by now."






        elif alt_day2_current_rout_status == 3:                 # и он выиграл первый раз

            show sh normal pioneer at cright with dissolve
            sh "Hmm, it worked..."
            me "What?"
            show sh surprise pioneer at cright with dspr
            sh "Ah?"
            show sh normal pioneer at cright with dspr
            sh "Yes, I tried to apply the formulas for calculating the probability of a better poker hand to this game."
            sh "I had to make some adjustments, of course, but the result was enough to show that your cards weren't any better."
            "Did he just calculate it? Seeing no more than half?"
            dreamgirl "Be careful with him. He's not as simple as he seems."
            th "I've already noticed. You're very helpful."
            th "You'd better tell me how to play against one of those."
            dreamgirl "Are you going to win?"
            th "Any other options?"
            th "They won't let me get up from the table and just walk away. And giving in is stupid."
            dreamgirl "You haven't got a chance anyway."
            th "Random is my judge, not you."

        elif alt_day2_current_rout_status == 4:                 # и он отыгрался

            show sh smile pioneer at cright with dissolve
            sh "Hmm, it worked..."
            me "Why do you keep counting?"
            show sh upset pioneer at cright with dspr
            sh "Ah?"
            show sh normal pioneer at cright with dspr
            sh "Yes, I'm trying to apply the formulas for calculating the probability of a better poker hand to this game."
            sh "I have to correct some things, of course, but even under these conditions the result gives an idea of your cards."
            "Without even seeing half, he predicts the whole set?"
            "I don't believe it. It's kind of mystical."
            dreamgirl "Who's to say..."

# Женя
    elif alt_spr_my_rival == 'mz': # Ей скилл не повышается, потому что foolplay? ## Ну ды
        show mz normal glasses pioneer at cright with dissolve
        if alt_day2_current_rout_status == 1:                   # если Семён выиграл первый раз

            "Buzzer didn't even move an eyebrow."
            "Emotional doldrums. «Pokerface»."
            "It's a little disappointing. You could have at least made a semblance of disappointment."
            mz "What?"
            me "Zhenya, how did you get here in the first place?"
            me "You don't look very happy."
            show mz angry glasses pioneer with dspr
            mz "Here - where to? To the camp? To the library? Tournament? The world?"
            mz "Ask specific questions if you want a specific answer."
            "Hard man."
            if herc or loki:
                "And why do I meet so many of these people?"
                dreamgirl "Like attracts like?"
                me "If I have time, I'll come over for a cup of tea, and we can talk about anything."
                me "About the leaders of the proletariat, or going to Mars, or London's «Martin Eden»."
                show mz rage glasses pioneer with dspr
                me "Hell, you can show me your baby pictures of you in diapers."
                me "In the meantime, I'm interested in the third one."
                me "Do a mere mortal a favor and tell me your secret."
                "I expected all sorts of things from the Bug: that she'd jump up and punch me in the face, that she'd yell at the whole room."
                "Yes, even that she would complain to the squad leader and demand to be released to the infirmary because she was psychologically traumatized and now needs rest."
                show mz laugh glasses pioneer with dspr
                pause(.5)
                show mz normal glasses pioneer with dspr
                "And she smiled."
                "Only for a moment, but I could have sworn I saw it."
                dreamgirl "Miracles...! Oh, miracles!..."
                mz "The counselor."
                mz "Came and mouthed: squad event, all have to be present, no objections accepted."
                me "Oh, that Olga Len...{w=0.3} Dmitrievna."
            else:
                me "Never mind."
                "I mumbled."
                show mz normal glasses pioneer with dspr
                "What a mean person."
                "Zhenya has more trouble communicating than I do."
                dreamgirl "Try to get her to talk to you."
                dreamgirl "See if you can get to know her from a different angle."
                dreamgirl "And then she'll call you to tea at the library, and there, among the shelves, books will fall off the shelves to the sound of a loud moani..."
                th "No!" with vpunch
                show mz bukal glasses pioneer with dspr
                mz "Psycho."
                "Zhenya snorted."
                dreamgirl "If you think that a slap will get rid of me, you're very wrong."
                th "Blah, blah, blah! I can't hear you!"
                dreamgirl "Idiot..."

        elif alt_day2_current_rout_status == 2:                 # если Семён отыгрался

            show mz normal glasses pioneer with dissolve
            mz "Keep up the good work."
            "If it were up to me."
            me "No promises, but I'll try."
            mz "Uh-huh, you'll try."
            hide mz with dissolve

        elif alt_day2_current_rout_status == 3:                 # и она выиграла первый раз

            show mz bukal glasses pioneer at cright with dissolve
            "The winner of the first round herself sighed wearily."
            "If she's that uninterested, why did she even agree to it?"
            "Couldn't she have covered up her busyness in the library in front of the counselor?"
            mz "Is there something on my face?"
            "Languidly she asked."
            th "More like an absence."
            "Thought I, answering:"
            me "No, I was just thinking."
            show mz normal glasses pioneer at cright with dspr
            mz "I see."


        elif alt_day2_current_rout_status == 4:                 # и она отыгралась


            show mz bukal glasses pioneer at cright with dspr
            if herc or loki:
                "Zhenya sighed sadly."
            else:
                "Her face was as if it had absorbed all the torment of the world."

            mz "Do me a favor - don't screw up the next round."
            me "If it were up to me."
            mz "Who else could it depend on?"
            mz "Just don't say stupid things like «god»."
            "Disdain, almost with hatred in her voice."
            "A true communist!"
            th "Or is it something personal?"
            me "I wouldn't dream of it."
            th "Random isn't a god. He's higher than that."
            show mz angry glasses pioneer at cright with dspr
            mz "Great."

    show el normal pioneer far at left with dissolve
    if alt_day2_current_rout_status == 1:
        el "This game was won by Semyon, the score is 1-0 in his favor."
    elif alt_day2_current_rout_status == 3:
        if alt_spr_my_rival == 'sh':                            # Шурик
            el "In this game Shurik won, the score is 1-0 in his favor."
        else:
            el "In this game %(alt_name_my_rival_i)s won, leading the match with the score of 1-0."
    elif alt_day2_current_rout_status == 2:
        el "Semyon wins and evens the score in the match."
    elif alt_day2_current_rout_status == 4:
        if alt_spr_my_rival == 'sh':                            # Шурик
            el "Shurik wins and evens the score in the match."
        else:
            el "%(alt_name_my_rival_i)s wins and evens the score in the match."
    return

#-----------------------------------------------------------------------------------
# Результат КОНА
label alt_day2_summary_poker_round:
    if alt_day2_result_tour in [1,11,21]:                                                              # Если проигрыш в КОНЕ
        if alt_day2_detour_1_tour:                                                                     # если скипаем тур
            $ alt_day2_my_win = renpy.random.choice([1,0])                                             # рандомно выигрыш Семёна 0 или 1
    elif alt_day2_result_tour in [2,12,22]:                                                            # Если выигрыш в КОНЕ
        if alt_day2_detour_1_tour:                                                                     # если скипаем тур
            $ alt_day2_rival_win = renpy.random.choice([1,0])                                          # рандомно выигрыш соперника 0 или 1
    return

#-----------------------------------------------------------------------------------
# АНАЛИЗАТОР 1-го ТУРА
label alt_day2_1_tour_analizer:
    $ alt_table_no = 0                                                                  # № стола = 1 (начинаем с НУЛЯ в этом случае)
    $ alt_mstt = 0                                                                      # обнуляем глобальный счетчик таблицы
    call show_tournament_table                                                          #  показываем исходное положение ??? сортируем игроков ???
    $ alt_result_dv_1_tour = alt_get_result_dv(alt_day2_gamblers_1_tour, 8)             # а где там наша ДваЧе?
    pause(1)
    $ alt_random_box_1 = range(1,len(alt_table_winner)+1)                               # черный ящик 1 — список от 1 до длины победителей +1
    while alt_table_no <= 4:                                                            # перебираем столы от 1 до 4
    #результат, игроки, высказывания — по номеру стола
        $ renpy.block_rollback()                                                        # блокируем роллбак
        $ results_at_table,gambler_win,winner_remark,loser_remark = alt_declare_results_tables(alt_table_no, alt_day2_gamblers_1_tour)
        "%(results_at_table)s"                                                          # оглашаем результат за столом
        call show_tournament_table                                                      # переход по метке — вызов очередной фишки
        extend " %(gambler_win)s."                                                      # выводим в окно имя победителя
        $ a_c_i = 0                                                                     # счетчик фраз
        while a_c_i < len(winner_remark):                                               # пока счетчик фраз меньше их количества
            $ alt_gambler_saying = winner_remark[a_c_i][0]                              # кто говорит
            $ alt_gambler_remark = winner_remark[a_c_i][1]                              # фраза
            if alt_gambler_saying != None:                                              # если определено, от кого фраза
                alt_gambler_saying "%(alt_gambler_remark)s"                             # выводим её от лица говорящего
            else:                                                                       # если "от автора"
                "%(alt_gambler_remark)s"                                                # выводим фразу "от автора"
            $ a_c_i += 1                                                                # увеличиваем счетчик фраз
        call show_tournament_table                                                      # переход по метке — вызов очередной фишки
        $ a_c_i = 0                                                                     # счетчик фраз
        while a_c_i < len(loser_remark):                                                # пока счетчик фраз меньше их количества
            $ alt_gambler_saying = loser_remark[a_c_i][0]                               # кто говорит
            $ alt_gambler_remark = loser_remark[a_c_i][1]                               # фраза
            if alt_gambler_saying != None:                                              # если определено, от кого фраза
                alt_gambler_saying "%(alt_gambler_remark)s"                             # выводим её от лица говорящего
            else:                                                                       # если "от автора"
                "%(alt_gambler_remark)s"                                                # выводим фразу "от автора"
            $ a_c_i += 1                                                                # увеличиваем счетчик фраз
        $ alt_table_no += 1                                                             # следующий стол
    return

#-----------------------------------------------------------------------------------
# АНАЛИЗАТОР ПОЛУФИНАЛА
label alt_day2_semifinal_analizer:
    $ alt_table_no = 4                                                                  # № стола = 4 (начинаем с четвертого в этом случае)
    $ alt_mstt = 0                                                                      # обнуляем глобальный счетчик таблицы
    call show_tournament_table                                                          #  показываем исходное положение ??? сортируем игроков ???
    $ alt_result_dv_semifinal = alt_get_result_dv(alt_day2_gamblers_semifinal, 4)       # а где там наша ДваЧе?
    pause(1)
    $ alt_random_box_1 = range(1,len(alt_table_winner)+1)                               # черный ящик 1 — список от 1 до длины победителей +1
    while alt_table_no <= 6:                                                            # перебираем столы 5-6
    #результат, игроки, высказывания — по номеру стола
        $ renpy.block_rollback()                                                        # блокируем роллбак
        $ results_at_table,gambler_win,winner_remark,loser_remark = alt_declare_results_tables(alt_table_no, alt_day2_gamblers_semifinal)
        "%(results_at_table)s"                                                          # оглашаем результат за столом
        call show_tournament_table                                                      # переход по метке — вызов очередной фишки
        extend " %(gambler_win)s."                                                      # выводим в окно имя победителя
        $ a_c_i = 0                                                                     # счетчик фраз
        while a_c_i < len(winner_remark):                                               # пока счетчик фраз меньше их количества
            $ alt_gambler_saying = winner_remark[a_c_i][0]                              # кто говорит
            $ alt_gambler_remark = winner_remark[a_c_i][1]                              # фраза
            if alt_gambler_saying != None:                                              # если определено, от кого фраза
                alt_gambler_saying "%(alt_gambler_remark)s"                             # выводим её от лица говорящего
            else:                                                                       # если "от автора"
                "%(alt_gambler_remark)s"                                                # выводим фразу "от автора"
            $ a_c_i += 1                                                                # увеличиваем счетчик фраз
        call show_tournament_table                                                      # переход по метке — вызов очередной фишки
        $ a_c_i = 0                                                                     # счетчик фраз
        while a_c_i < len(loser_remark):                                                # пока счетчик фраз меньше их количества
            $ alt_gambler_saying = loser_remark[a_c_i][0]                               # кто говорит
            $ alt_gambler_remark = loser_remark[a_c_i][1]                               # фраза
            if alt_gambler_saying != None:                                              # если определено, от кого фраза
                alt_gambler_saying "%(alt_gambler_remark)s"                             # выводим её от лица говорящего
            else:                                                                       # если "от автора"
                "%(alt_gambler_remark)s"                                                # выводим фразу "от автора"
            $ a_c_i += 1                                                                # увеличиваем счетчик фраз
        $ alt_table_no += 1                                                             # следующий стол
    return

#-----------------------------------------------------------------------------------
# АНАЛИЗАТОР ФИНАЛА
label alt_day2_final_analizer:
    $ alt_mstt = 3
    call show_tournament_table                                                          # показываем исходное положение, сортируем игроков
    $ alt_take_tournament_winner = alt_day2_gamblers_final[0].take                      # Ник победителя
    if alt_take_tournament_winner == "me":
        $ alt_name_tournament_winner = "Semyon"
    else:
        $ alt_name_tournament_winner = alt_day2_gamblers_final[0].name['v']             #  Получаем имя победителя турнира

    $ alt_take_tournament_loser = alt_day2_gamblers_final[1].take                       # Ник проигравшего
    if alt_take_tournament_loser == "me":
        $ alt_name_tournament_loser = "Semyon"
    else:
        $ alt_name_tournament_loser = alt_day2_gamblers_final[1].name['d']              #  Получаем имя проигравшего в финале

    if alt_take_tournament_loser in ['me','sh']:
        $ alt_pronomen_final_loser = "he"
    else:
        $ alt_pronomen_final_loser = "she"

    $ winner_remark, loser_remark = alt_declare_results_final(alt_take_tournament_winner, alt_take_tournament_loser) # вызываем функцию на финал — фразы победителя, проигравшего — по их никам.

    show el normal pioneer at cleft with dissolve
    el "So, the tournament is over."
    "The organizer remembered his duties."
    $ alt_mstt = 0
    el "Congratulations to our winner — %(alt_name_tournament_winner)s!"
    play sound sfx_concert_applause
    call show_tournament_table                                                          # двигаем победителя
    pause(0.2)

    $ a_c_i = 0                                                                     # счетчик фраз
    while a_c_i < len(winner_remark):                                               # пока счетчик фраз меньше их количества
        $ alt_gambler_saying = winner_remark[a_c_i][0]                              # кто говорит
        $ alt_gambler_remark = winner_remark[a_c_i][1]                              # фраза
        if alt_gambler_saying != None:                                              # если определено, от кого фраза
            alt_gambler_saying "%(alt_gambler_remark)s"                             # выводим её от лица говорящего
        else:                                                                       # если "от автора"
            "%(alt_gambler_remark)s"                                                # выводим фразу "от автора"
        $ a_c_i += 1                                                                # увеличиваем счетчик фраз

    $ alt_mstt += 1
    el "And %(alt_name_tournament_loser)s wasn't as lucky today; nevertheless, %(alt_pronomen_final_loser)s takes honorable second place."
    call show_tournament_table                                                      # прячем проигравшего
    pause(0.2)

    $ a_c_i = 0                                                                     # счетчик фраз
    while a_c_i < len(loser_remark):                                                # пока счетчик фраз меньше их количества
        $ alt_gambler_saying = loser_remark[a_c_i][0]                               # кто говорит
        $ alt_gambler_remark = loser_remark[a_c_i][1]                               # фраза
        if alt_gambler_saying != None:                                              # если определено, от кого фраза
            alt_gambler_saying "%(alt_gambler_remark)s"                             # выводим её от лица говорящего
        else:                                                                       # если "от автора"
            "%(alt_gambler_remark)s"                                                # выводим фразу "от автора"
        $ a_c_i += 1                                                                # увеличиваем счетчик фраз
    hide el with dissolve
    return

# --------------------------------------------------------------------------
# Подготовка перехода на ужин: — очистка слоя, разблокировка роллбэка
label alt_day2_prepare_transition_to_supper:
    python:
        renpy.scene('underlay')
        renpy.with_statement(dissolve)
    $ alt_who_how_plays_poker()                                                     # посмотрели, кто и как сыграл
    if alt_day2_gamblers_result['me'] <= 11:
        $ alt_my_rival_final.take = None
        if alt_day2_gamblers_result['me'] == 1:
            $ alt_my_rival_semifinal.take = None
    $ d2_cardgame_block_rollback = False
    return
