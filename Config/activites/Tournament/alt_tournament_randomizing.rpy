init 10 python:
# -----------------------------------------------------------------------------------------------
# спрайты соперников
    alt_sprites_rival_recognition = {             # ['эмоция', 'аксессуар', 'одежда', положение]
        "un":   ['shy',    '',        'pioneer',  cright],
        "sl":   ['smile2', '',        'pioneer',  cright],
        "dv":   ['grin',   '',        'pioneer2', cright],
        "mi":   ['smile',  '',        'pioneer',  cright],
        "us":   ['laugh',  '',        'pioneer',  cright],
        "sh":   ['normal', '',        'pioneer',  cright],
        "mz":   ['normal', 'glasses', 'pioneer',  cright]
    }
# ------------------------------------------------
init python:
# ------------------------------------------------
    if persistent.altCardsWonRivals_new == None:             # Выигрывали ли когда-то у этого соперника
        persistent.altCardsWonRivals_new = {
            'un':   False,
            'sl':   False,
            'dv':   False,
            'mi':   False,
            'us':   False,
            'sh':   False,
            'mz':   False
        }
# ------------------------------------------------
    alt_day2_gamblers_summary = {                           # результат турнира — кто на каком этапе как сыграл.
        'me':   [0,0,0],                                    # в списке:  0 — 1 тур, 1 — полуфинал, 2 — финал
        'un':   [0,0,0],                                    # значение:  0 — результат не определен, 2 — победа, 1 — поражение
        'sl':   [0,0,0],                                    # в итоге: результат = 10 х индекс + значение
        'dv':   [0,0,0],                                    # 0 — не участвовал, 2/1 — победа/поражение в 1 коне; 12/11 — в 1/2; 22/21 — в финале
        'mi':   [0,0,0],
        'us':   [0,0,0],
        'sh':   [0,0,0],
        'mz':   [0,0,0]
        }

    alt_day2_gamblers_result = {
        'me':   0,
        'un':   0,
        'sl':   0,
        'dv':   0,
        'mi':   0,
        'us':   0,
        'sh':   0,
        'mz':   0
        }

# ------------------------------------------------
label alt_day2_cards_tournament_vars:
# Переменные турнира — тур до двух побед
    $ alt_day2_my_win = 0                                   # Количество побед Семёна в коне
    $ alt_day2_rival_win = 0                                # Количество побед соперника в коне
    $ alt_day2_game_played_out = 0                          # сколько раз сыграли в коне
    $ alt_day2_result_current_game = 0                      # результат текущей игры
    $ alt_hint_poker_contractual = False                    # Комбинации на руках не показываются при игре
    $ alt_day2_revanche = False                             # Реванша не было
    $ alt_day2_detour_number = 0                            # Выбор соперника для финала

# Переменные турнира — рассадка и прочее
    $ wipedown2 = CropMove(1.3, "wipedown")

    $ alt_day2_result_tour = 0                                                          # Итог тура (0-начало, 2/1 — победа/поражение в 1 коне; 12/11 — в 1/2; 22/21 — в финале )
    $ alt_day2_detour_1_tour = False                                                    # Пропуск 1 тура (если скип турнира)
    $ alt_day2_detour_semifinal = False                                                 # Пропуск 1/2  (если скип турнира)
    $ alt_day2_detour_final = False                                                     # Пропуск финала  (если скип турнира)
    $ alt_day2_tournament_fast_win = False                                              # Победа в финале (если скип турнира)
    $ alt_tournament_state = None                                                       # этап турнира
    $ alt_my_rival_semifinal = None                                                     # Неуловимый второй финалист
    $ alt_mstt = 0                                                                      # глобальный счетчик турнирной таблицы
    $ alt_day2_gamblers_begin = []                                                      # Пустой список игроков при рассадке
    $ alt_winners_1_tour = []                                                           # Пустой список победителей 1 тура
    $ alt_losers_1_tour = []                                                            # Пустой список проигравших в 1 туре
    $ alt_winners_semifinal = []                                                        # Пустой список победителей полуфинала
    $ alt_losers_semifinal = []                                                         # Пустой список проигравших в полуфинале

init:
# Новые persistent'ы турнира
    if persistent.altCardsDemo_new == None:
        $ persistent.altCardsDemo_new = False
    if persistent.altCardsFail_new == None:
        $ persistent.altCardsFail_new = False
    if persistent.altCardsWon1_new == None:
        $ persistent.altCardsWon1_new = False
    if persistent.altCardsWon2_new == None:
        $ persistent.altCardsWon2_new = False
    if persistent.altCardsWon3_new == None:
        $ persistent.altCardsWon3_new = False
    if persistent.altRulesRead_new == None:
        $ persistent.altRulesRead_new = False

# ------------------------------------------------
    # КАРТИНКИ МАСТЕЙ В ОПИСАНИЕ ПРАВИЛ ТУРНИРА
    image suit_2ch_S = im.Scale(get_image_7dl("gui/tournament/suit/suit_2ch.png"),21,28)
    image suit_2ch_L = im.Scale(get_image_7dl("gui/tournament/suit/suit_2ch.png"),26,35)
    image suit_ussr_S = im.Scale(get_image_7dl("gui/tournament/suit/suit_ussr.png"),21,28)
    image suit_ussr_L = im.Scale(get_image_7dl("gui/tournament/suit/suit_ussr.png"),26,35)
    image suit_utan_S = im.Scale(get_image_7dl("gui/tournament/suit/suit_utan.png"),21,28)
    image suit_utan_L = im.Scale(get_image_7dl("gui/tournament/suit/suit_utan.png"),26,35)
    image suit_uvao_S = im.Scale(get_image_7dl("gui/tournament/suit/suit_uvao.png"),21,28)
    image suit_uvao_L = im.Scale(get_image_7dl("gui/tournament/suit/suit_uvao.png"),26,35)

# ------------------------------------------------
    # ДОПОЛНИТЕЛЬНЫЕ АВАТАРКИ ПЕРСОНАЖЕЙ
init python:
    p = get_image_7dl("gui/avaset/sh/sh-")
    sh_avatar_set = {
                 'body':p+"body.png",
                 0     :p+"emo6.png",
            }

    p = get_image_7dl("gui/avaset/mi/mi-")
    mi_avatar_set = {
                 'body':p+"body.png",
                 0     :p+"emo5.png",
            }

    p = get_image_7dl("gui/avaset/mz/mz-")
    mz_avatar_set = {
                 'body':p+"body.png",
                 0     :p+"emo6.png",
            }

# ------------------------------------------------

init 2 python:
# ===============================================================================================
#                   СЛОВАРИ, ТАУНТЫ, ПРЕДСТВАЛЕНИЯ СТОЛОВ, ДИАЛОГИ И Т. П.
# -----------------------------------------------------------------------------------------------



# ===============================================================================================
# ОСОБЫЕ РАСКЛАДЫ — ПРЕДСТАВЛЕНИЕ СТОЛА ВМЕСТО СТАНДАРТНОГО, ПРИ ДАННОМ СОЧЕТАНИИ ИГРОКОВ
# -----------------------------------------------------------------------------------------------
# Ключ: me+sh (по алфафиту); Значения: суффикс представления, падеж стола, падежи игроков
    alt_table_special_name = {
        "me+sh":    ["men's company has formed:","t","i"],                                                 # Семён + Шурик, стол: ТП, игроки: ИП
        "dv+us":    ["got occupied by redheads:","i","i"],                                                            # Алиса + Ульяна, стол: ИП, игроки: ИП
        "dv+mi":    ["was taken by our musicians:","i","i"]                                                          # Алиса + Мику, стол: ИП, игроки: ИП

        }

# ===============================================================================================
# ВЗАИМНЫЕ ТАУНТЫ ИГРОКОВ — ПОКАЗЫВАЮТСЯ ВМЕСТО СТАНДАРТНЫХ (ПРИОРИТЕТ 1 — ВЫСШИЙ)
# отсортировано по возможным сочетаниям ников в алфавитном порядке
# -----------------------------------------------------------------------------------------------
    alt_table_mutual_taunt = {
        "dv+me":    "Dvachevskaya stared at me with a challenge, clearly alluding to the conversation on the porch.",
        "dv+mi":    "Miku eyed Alisa warily as she settled at the table, looking victorious.",
        "dv+mz":    "Alisa was trying to show off, but Zhenya, on the other hand, was completely calm.",
        "dv+sh":    "Alisa stared carnivorously at Shurik, but he didn't seem to pay any attention to her at all.",
        "dv+sl":    "The perfect solution. A person who wants to win at all costs against a person who doesn't need all this nonsense.",
        "dv+un":    "Alisa winked, and Lena, to my surprise, smiled weakly and said something to the redhead.",
        "dv+us":    "The two beasts clashed with each other, neither of them clearly intent on conceding!",
        "me+mi":    "Miku seemed to have no idea what the game was coming up, but she tried her best to enjoy herself.",
        "me+mz":    "The Buzzer sat there with a look of the greatest favor. Apparently, she really wants this to be over quickly.",
        "me+sh":    "Shurik adjusted his glasses on the bridge of his nose, folded his arms crosswise across his chest, and stared thoughtfully at the table top. He was in his own thoughts, that's for sure.",
        "me+sl":    "Slavya smiled warmly at me, apparently encouraging me, but all I could do was shrug my shoulders and smile crookedly.",    # Семён + Славя
        "me+un":    "Lena sat across from me, cringing and trying to look anywhere but at me, and certainly not in my eyes.",    # Семён + Лена
        "me+us":    "The little one, looking to see if anyone was watching, furtively showed me her tongue.",
        "mi+mz":    "Zhenya looked at her opponent, sighed sadly, and sat down opposite.",    # Мику + Женя
        "mi+sh":    "As soon as Shurik sat down at the table, Miku immediately shot him up with words. The cyberneticist nodded nonchalantly and answered something.",    # Мику + Шурик
        "mi+sl":    "Slavya took a seat across from Miku. The girls exchanged a few words and wished each other good luck.",    # Мику + Славя
        "mi+un":    "Miku was glad when Lena sat down across from her. Her feelings were reciprocated - the green-eyed girl smiled.",    # Мику + Лена
        "mi+us":    "The rocket girl, seeing that I was looking in their direction, showed me her tongue, and Miku waved.",    # Мику + Ульяна
        "mz+sh":    "Both looked at each other silently over their glasses, waiting for the game to begin.",    # Женя + Шурик
        "mz+sl":    "An interesting couple. Slavya, who doesn't need all this nonsense, versus Zhenya, who would prefer an activity more useful than playing cards.",    # Женя + Славя
        "mz+un":    "The person who is trying to avoid unnecessary attention has fallen out as an opponent of someone who doesn't care about you.",    # Женя + Лена
        "mz+us":    "Fortunately for Ulyana, you can't burn people with your eyes. She also wasn't happy that Random sent her the Buzzer as an opponent.",    # Женя + Ульяна
        "sh+sl":    "Slavya smiled at Shurik in a friendly way, to which he responded with a nod.",    # Шурик + Славя
        "sh+un":    "Shurik took a seat across from Lena and asked the pioneer girl something. Something about «posters for the stand».",    # Шурик + Лена
        "sh+us":    "Ulyanka immediately whispered something in Shurik's ear, and I heard something like «will sign up for club».", # Шурик + Ульяна
        "sl+un":    "Although Slavya cheered Lena up, it's unlikely she'll make it to the finals with that attitude.",    # Славя + Лена
        "sl+us":    "Ulyanka sat down on the chair opposite Slavya and showed her her tongue. Slavya, looking to see if anyone was watching, furtively showed her tongue in response, which surprised me.",    # Славя + Ульяна
        "un+us":    "Lena shuddered when the little girl jumped up to her, and then blushed after Ulyanka whispered something in her ear. The redheaded bandit laughed all over the canteen, but after a remark from Electronik, she still sat down at the table.", # Лена + Ульяна
        }

# -----------------------------------------------------------------------------------------------
# ТАУНТЫ ДЛЯ ИГРОКОВ В ПАРЕ С СЕМЁНОМ — (ПРИОРИТЕТ 2)
# отсортировано по условному номеру игрока
# Количество фраз для каждого соперника может быть ЛЮБЫМ (не обязательно одинаковым), выбор рандомный
# -----------------------------------------------------------------------------------------------
    alt_table_taunt_with_me = {
        "un":   [           # Лена
                    "Lena was sitting across from me.",
                    "On the opposite side of the table, Lena smiled at me timidly."
                ],
        "sl":   [           # Славя
                    "Across from me sat Slavya."
                ],
        "dv":   [           # Алиса
                    "Alisa, smiling, sat across from me.",
                    "On the opposite side, Redhead grinned sneeringly."
                ],
        "mi":   [           # Мику
                    "The Japanese girl smiled radiantly at me on the other side of the table.",
                    "On the opposite side of the table was the anime girl.",
                    "Miku sat comfortably across from me."
                ],
        "us":   [           # Ульяна
                    "Ulyanka was making faces at me from across the table.",
                    "The little one was fidgeting on the opposite chair."
                ],
        "sh":   [           # Шурик (для пробы оставим пустым)
                    None
                ],
        "mz":   [           # Женя (картинки без очков)
                    "On the opposite side of the table, an unsociable librarian glared at me."
                ]
        }

# ===============================================================================================
# ТАУНТЫ ДЛЯ ИГРОКОВ, ЕСЛИ СИДЯТ ДРУГ С ДРУГОМ = ПО ВТОРОМУ ИГРОКУ В ПАРЕ — (ПРИОРИТЕТ 3)
# отсортировано по условному номеру игрока
# Количество фраз для каждого соперника может быть ЛЮБЫМ (не обязательно одинаковым), выбор рандомный
# ПЛОХИЕ НОВОСТИ — внутритекстовые теги работать не будут.
# -----------------------------------------------------------------------------------------------
    alt_table_taunt_gamblers = {
        "un":   [           # Лена
                    "Lena intercepted my gaze and turned all red.",
                    "Lena pretended not to notice me looking at her.",
                    "I'm surprised that Lena agreed to participate in a public event."
                ],
        "sl":   [           # Славя
                    "Slavya sensed that I was looking at her and smiled.",
                    "Slavya nodded encouragingly at me.",
                    "It was strange to see the «proper» girl with cards in her teeth."
                ],
        "dv":   [           # Алиса
                    "Dvachevskaya laughed when she saw me pretending not to look at her.",
                    "I hope Alisa gets knocked off in this round!",
                    "Well, Dvachevskaya won't lose that easily."
                ],
        "mi":   [           # Мику
                    "The Japanese girl looked amused - she pretended to know why she was here.",
                    "You don't have to worry about the Japanese girl - she didn't seem to care about cards at all.",
                    "The Japanese girl was obviously agitated about something. And it wasn't the cards at all."
                ],
        "us":   [           # Ульяна
                    "Kid showed me her tongue and turned away.",
                    "Kid was busy intimidating her opponent.",
                    "Kid was smiling and shaking her head, preparing for a decisive victory!"
                ],
        "sh":   [           # Шурик
                    "He winked at me and gave me a thumbs-up.",
                    "With his eyes closed, the cybernetic was calculating something in his mind. The odds of winning?",
                    "The guy really didn't seem to have heard of such a game - he looked confused."
                ],
        "mz":   [           # Женя
                    "Zhenya, as usual, ignored me.",
                    "You could see that Zhenya would be glad to drop everything and go to the library.",
                    "It's obviously Zhenya who looks alien here."
                ]
        }

# ===============================================================================================
#  Для каждой пары "победитель/проигравший" приоритет 1
#  отсортировано по сочетаниям ников в алфавитном порядке (победитель > проигравший)
#           МОЖНО добавить варианты — с дальнейшим рандомным выбором
#
#    Сначала идут фразы победителя
#    разделитель блоков "*"
#    ниже — фразы проигравшего
#    если сочетание "xx>yy" не найдено — обработчик эту таблицу пропустит
#    если не найден разделитель "*" или их найдено больше одного — обработчик пропустит таблицу
#    одной из частей, либо обеих частей может не быть (т.е. "*" стоит вначале или конце списка)
#    если  в одной из частей нет строк, или первая строка блока [None, None] или [None, " "] или [] —
#    обрабочик пропустит этот блок — т. е. будет считать его пустым
#
#   структура: [кто говорит (или None  — если "от автора"), что говорит]
#   если несколько строк — и выводиться будет в несколько строк
#
#
#   ПЛОХИЕ НОВОСТИ — внутритекстовые теги (например, {w}) работать не будут.
# -----------------------------------------------------------------------------------------------
    alt_table_mutual_gamblers_win_los = {
# ------------------------------------------- Алиса
        "dv>me":    [       # Алиса > Семён
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "dv>mi":    [       # Алиса > Мику
                        [None, "Dvachevskaya jumped up from the table and hooted:"],
                        [dv, "Ole, ole, ole! Alisa, let's go!"],
                        [None, "She rejoiced at her victory as if she had won at least a car."],
                        "*",
                        [mi, "It's okay, Alisochka. I'll remember everything..."],
                        [None, "Miku turned her nose up and stepped back to the audience."]
                    ],
        "dv>mz":    [       # Алиса > Женя
                        [None, "Despite the landslide victory, she didn't look happy for some reason."],
                        [dv, "That's it, huh?"],
                        [None, "Confused, she asked Zhenya."],
                        "*",
                        [mz, "Hallelujah, I'm finally free."],
                        [None, "Zhenya squeaked and cleared out of the canteen."]
                    ],
        "dv>sh":    [       # Алиса > Шурик
                        [None, "When she won, she acted strangely."],
                        [None, "She stood up from the table, put her twisted palms to her eyes in a goggle gesture, and shook her elbows."],
                        [dv, "Glasses are out! Adieu."],
                        "*",
                        [sh, "Why did I even come…"],
                        [None, "Shurik shrugged his shoulders indifferently and got up from the table."]
                    ],
        "dv>sl":    [       # Алиса > Славя
                        [None, "Losing, Slavya smiled and nodded to her."],
                        [sl, "That's it? Can I go now?"],
                        [None, "Alisa nodded; she was only interested in winning.."],
                        "*",
                        [dv, "And you're all right, upstart, you can play."],
                        [sl, "Oh, please."],
                    ],
        "dv>un":    [       # Алиса > Лена
                        [None, "She looked condescendingly at Lena."],
                        [dv, "As if anyone doubted that it would be otherwise!"],
                        [None, "Rolling over, she flicked her opponent on the forehead."],
                        "*",
                        [un, "I didn't really feel like it."],
                        [None, "Lena pretended not to care about the results of the match."]
                    ],
        "dv>us":    [       # Алиса > Ульяна
                        [None, "Defeating her friend, the redhead arrogantly turned up her nose:"],
                        [dv, "You are too young, Padawan, try next year."],
                        "*",
                        [us, "Look at this old hag."],
                        [None, "Ulyanka was hurt by the defeat, and she made no secret of it."]
                    ],
# ------------------------------------------- Семён
        "me>dv":    [       # Семён > Алиса
                        [None, "Until the end, Dvachevskaya did not see me as a serious opponent, and this played against her."],
                        "*",
                        [None, "Defeating the red-headed pest made me excited."]
                    ],
        "me>mi":    [       # Семён > Мику
                        [None, "I couldn't take defeating hafu as my own personal accomplishment, though. She just didn't fully understand the rules."],
                        "*",
                        [None, "I think if Miku had had a chance to win back, I would have been facing defeat."]

                    ],
        "me>mz":    [       # Семён > Женя
                        [None, "A simple task when your opponent is interested in a quick defeat."],
                        "*",
                        [None, "From the corner of my eye, I noticed the sad sigh of Electronik."],
                        [None, "Worried for Buzzer? Or «because» of her?"]
                    ],
        "me>sh":    [       # Семён > Шурик

                        [None, "Shurik turned out to be a worthy opponent."],
                        "*",
                        [None, "It took a lot of effort to defeat him."],



                    ],
        "me>sl":    [       # Семён > Славя
                        [None, "It's too early to relax. The main difficulties are yet to come."],
                        "*",
                        [None, "It's not hard to win when your opponent is the living embodiment of the phrase «the main thing is not to win, the main thing is to participate»."],


                    ],
        "me>un":    [       # Семён > Лена
                        [None, "I hope Lena won't be too disappointed."],
                        "*",
                        [None, "This is just a game, right?"]

                    ],
        "me>us":    [       # Семён > Ульяна

                        [None, "It seems that the bird of fortune is firmly settled on my shoulder today, and Ulyanka has met the bird «Oblomingo»."],
                        "*",
                        [th, "So, should we expect another «cutlet Ulyana-style»?"],
                        [dreamgirl, "The girl is inventive, she will think up a more terrible revenge."],
                        [dreamgirl, "Or she'll give up on the fool and forgive."],
                        [dreamgirl, "As the card goes."],
                        [th, "Puns, huh."]

                    ],
# ------------------------------------------- Мику
        "mi>dv":    [       # Мику > Алиса
                        [None, " "],
                        "*",
                        [None, " "]

                    ],
        "mi>me":    [       # Мику > Семён
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "mi>mz":    [       # Мику > Женя
                        [mi, " "],
                        "*",
                        [None, " "]
                    ],
        "mi>sh":    [       # Мику > Шурик
                        [mi, " "],
                        "*",
                        [None, " "]
                    ],
        "mi>sl":    [       # Мику > Славя
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "mi>un":    [       # Мику > Лена
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "mi>us":    [       # Мику > Ульяна
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
# ------------------------------------------- Женя
        "mz>dv":    [       # Женя > Алиса
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "mz>me":    [       # Женя > Семён
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "mz>mi":    [       # Женя > Мику
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "mz>sh":    [       # Женя > Шурик
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "mz>sl":    [       # Женя > Славя
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "mz>un":    [       # Женя > Лена
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "mz>us":    [       # Женя > Ульяна
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
# ------------------------------------------- Шурик
        "sh>dv":    [       # Шурик > Алиса
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "sh>me":    [       # Шурик > Семён
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "sh>mi":    [       # Шурик > Мику
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "sh>mz":    [       # Шурик > Женя
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "sh>sl":    [       # Шурик > Славя
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "sh>un":    [       # Шурик > Лена
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "sh>us":    [       # Шурик > Ульяна
                        [None, "Shurik condescendingly looked at Ulyana, as if saying, 'Know our people'."],
                        [sh, "Thank you for playing."],
                        [None, "He thanked politely."],
                        "*",
                        [us, "Boo-boo-boo, pest, didn't let the kid win!"],
                        [None, "Ulyana puffed up and turned away."]
                    ],
# ------------------------------------------- Славя
        "sl>dv":    [       # Славя > Алиса
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "sl>me":    [       # Славя > Семён
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "sl>mi":    [       # Славя > Мику
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "sl>mz":    [       # Славя > Женя
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "sl>sh":    [       # Славя > Шурик
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "sl>un":    [       # Славя > Лена
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "sl>us":    [       # Славя > Ульяна
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
# ------------------------------------------- Лена
        "un>dv":    [       # Лена > Алиса
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "un>me":    [       # Лена > Семён
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "un>mi":    [       # Лена > Мику
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "un>mz":    [       # Лена > Женя
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "un>sh":    [       # Лена > Шурик
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "un>sl":    [       # Лена > Славя
                        [sl, "Good luck."],
                        "*",
                        [un, "T-thanks."],
                        [None, "At a loss, Lena replied."]
                    ],
        "un>us":    [       # Лена > Ульяна
                        [None, "She herself, apparently, has not yet fully believed that she has won."],
                        [un, "I what, I…"],
                        "*",
                        [us, "Aaaaah, Lenka the penny sausage, the noxious sausage!"],
                        [None, "Ulyana wanted to add something else, but the rushing squad leader pulled her aside."]
                    ],
# ------------------------------------------- Ульяна
        "us>dv":    [       # Ульяна > Алиса
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "us>me":    [       # Ульяна > Семён
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "us>mi":    [       # Ульяна > Мику
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "us>mz":    [       # Ульяна > Женя
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "us>sh":    [       # Ульяна > Шурик
                        [None, "Having won, Ulyana behaved predictably."],
                        [us, "And so it will be with everyone!"],
                        "*",
                        [sh, "Thank you too."],
                        [None, "After getting up, Shurik stepped aside."]
                    ],
        "us>sl":    [       # Ульяна > Славя
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "us>un":    [       # Ульяна > Лена
                        [None, " "],
                        "*",
                        [None, " "]
                    ]
        }

# ===============================================================================================
# ДЛЯ ИГРОКОВ — ПОБЕДИТЕЛЕЙ 1 тура
# отсортировано по условному номеру игрока
#      МОЖНО добавить варианты — с дальнейшим рандомным выбором
# структура: [кто говорит (или None  — если "от автора"), что говорит]
# если несколько строк — и выводиться будет в несколько строк
# ПЛОХИЕ НОВОСТИ — внутритекстовые теги работать не будут.
# -----------------------------------------------------------------------------------------------
    alt_table_gamblers_winner_1_tour = {
       "me":   [           # Сёма
                    [None, "I'm on my way to victory."]
                ],
        "un":   [           # Лена
                    [None, "She had to work hard, but she won."]
                ],
        "sl":   [           # Славя
                    [None, "The activist did not seem to understand what happened, but obediently moved to the table of semifinalists."]
                ],
        "dv":   [           # Алиса
                    [None, "She rolled her opponent by a landslide - she seemed to enjoy the game."]
                ],
        "mi":   [           # Мику
                    [None, "Yeah, I guess a talented person is talented at everything."]
                ],
        "us":   [           # Ульяна
                    [None, "The kid didn't bother with something as silly as the rules of the game."],
                    [None, "Instead, she played by her own."]
                ],
        "sh":   [           # Шурик
                    [None, "Honestly, I'm not surprised. He had every chance."]
                ],
        "mz":   [           # Женя
                    [None, "She grimaced in displeasure - she seemed to realize that winning also meant continuing to participate in this stupid game."]
                ]
    }

# ===============================================================================================
# ДЛЯ ИГРОКОВ — ПОБЕДИТЕЛЕЙ ПОЛУФИНАЛА
# отсортировано по условному номеру игрока
#      МОЖНО добавить варианты — с дальнейшим рандомным выбором
# структура: [кто говорит (или None  — если "от автора"), что говорит]
# если несколько строк — и выводиться будет в несколько строк
# ПЛОХИЕ НОВОСТИ — внутритекстовые теги работать не будут.
# -----------------------------------------------------------------------------------------------
    alt_table_gamblers_winner_semifinal = {
        "me":   [           # Сёма
                    [None, "I'm going to the finals."]
                ],
        "un":   [           # Лена
                    [None, "For the second game in a row, she's sitting there looking lost, but she's getting stronger and stronger combinations. Isn't the dealer playing along with her?"]
                ],
        "sl":   [           # Славя
                    [None, "The girl grumbled and shrugged, not really wanting to continue the game. She seemed to have decided to join in just out of a sense of camaraderie."]
                ],
        "dv":   [           # Алиса
                    [None, "The redhead was bulldozing along, not lingering on any of her opponents - her goal was the finale, and nothing else!"]
                ],
        "mi":   [           # Мику
                    [None, "She rejoiced at every good card like a little child."]
                ],
        "us":   [           # Ульяна
                    [None, "The little one is on a roll today."],
                    [None, "The second game in a row without knowing the rules is almost like driving a car without hands."]
                ],
        "sh":   [           # Шурик
                    [None, "His equanimity would have been the envy of Buddha himself. Perhaps that was his secret?"]
                ],
        "mz":   [           # Женя
                    [None, "I was frankly amused by the fact that she wanted to play the least."],
                    [None, "But she got this far."]
                ]
    }

# ===============================================================================================
# ДЛЯ ИГРОКОВ — ПОБЕДИТЕЛЕЙ ФИНАЛА
# отсортировано по условному номеру игрока
#      МОЖНО добавить варианты — с дальнейшим рандомным выбором
#  (заготовка словаря, фразы можно дописать по аналогии с 1 туром и 1\2)
# структура: [кто говорит (или None  — если "от автора"), что говорит]
# если несколько строк — и выводиться будет в несколько строк
# Если [None, None] или [None, " "] — обработчик не выведет ничего
# ПЛОХИЕ НОВОСТИ — внутритекстовые теги работать не будут.
# -----------------------------------------------------------------------------------------------
    alt_table_gamblers_winner_final = {
        "me":   [           # Сёма
                    [None, "I didn't think that with my luck I would make it at least to the semifinals."],
                    [None, "So, do not expect from me beautiful speeches and gratitude to the losers, I am not mentally prepared for this."]
                ],
        "un":   [           # Лена
                    [None, "Lena, who was in mild shock, flinched in surprise when she heard her name."]
                ],
        "sl":   [           # Славя
                    [None, "Slavya was very embarrassed to be the center of attention and applause."]
                ],
        "dv":   [           # Алиса
                    [None, "The redhead towered over the others, climbing into a chair and throwing her arms up in the air."],
                    [th, "Ave me, yeah?"]
                ],
        "mi":   [           # Мику
                    [None, "Miku bowed to the audience and thanked them for their support."]
                ],
        "us":   [           # Ульяна
                    [None, "Ulyana looked like someone who never doubted for a second that she would win."]
                ],
        "sh":   [           # Шурик
                    [None, "Shurik put on a look of equanimity worthy of our bronze figure."]
                ],
        "mz":   [           # Женя
                    [None, "The buzzer grimaced as the auditorium exploded with applause and cheers in her honor."]
                ]
    }

# ===============================================================================================
# ДЛЯ ИГРОКОВ — ПРОИГРАВШИХ в 1 туре
# отсортировано по условному номеру игрока
#             МОЖНО добавить варианты — с дальнейшим рандомным выбором
# структура: [кто говорит (или None  — если "от автора"), что говорит]
# если несколько строк — и выводиться будет в несколько строк
# ПЛОХИЕ НОВОСТИ — внутритекстовые теги работать не будут.
# -----------------------------------------------------------------------------------------------
    alt_table_gamblers_loser_1_tour = {
        "me":   [           # Сёма
                    [None, "I stay in the first round."],
                    [None, "I'll be a fan; what else can I do?"]
                ],
        "un":   [           # Лена
                    [None, "Lena quietly got up and joined the fans. She looked upset."]
                ],
        "sl":   [           # Славя
                    [None, "Slavya shrugged, stood up, and, after passing the counselor and saying something to her, took her place among the fans."]
                ],
        "dv":   [           # Алиса
                    [None, "To see Dvachevskaya's face in defeat is priceless!"],
                    [None, "I laughed, covering with my hand, but she seemed to hear me - she burned me with her gaze."]
                ],
        "mi":   [           # Мику
                    [None, "Miku got up, waved to everyone, and went up to the fans."],
                    [None, "She was very happy about something."]
                ],
        "us":   [           # Ульяна
                    [None, "Ulyana sulked, shouted something and tried to stamp her feet, but Olga Dmitrievna quickly calmed her down."],
                    [None, "The little one tried to wander away from the canteen, but a shout from the squad leader forced her to change her course to the cheerleading seats."]
                ],
        "sh":   [           # Шурик
                    [None, "Shurik reacted the way I expected - he adjusted his glasses, flicked his bangs back from his forehead, and stood up."],
                    [None, "He tilted his head briefly and took his place in the crowd."]
                ],
        "mz":   [           # Женя
                    [None, "With a look of great relief, Zhenya threw the cards on the table, stood up and headed outside."]
                ]
    }

# ===============================================================================================
# ДЛЯ ИГРОКОВ — ПРОИГРАВШИХ в ПОЛУФИНАЛЕ
# отсортировано по условному номеру игрока
#             МОЖНО добавить варианты — с дальнейшим рандомным выбором
# структура: [кто говорит (или None  — если "от автора"), что говорит]
# если несколько строк — и выводиться будет в несколько строк
# ПЛОХИЕ НОВОСТИ — внутритекстовые теги работать не будут.
# -----------------------------------------------------------------------------------------------
    alt_table_gamblers_loser_semifinal = {
        "me":   [           # Сёма
                    [None, "And I blew it. What else can I say?"]
                ],
        "un":   [           # Лена
                    [None, "Lena quietly rose and joined the fans."]
                ],
        "sl":   [           # Славя
                    [None, "Slavya smiled wistfully and pushed the cards away with great relief."],
                    [sl, "That's it, I'm done for the year to come."],
                    [None, "She got up and went to Olga Dmitrievna, who was waiting for her."]
                ],
        "dv":   [           # Алиса
                    [None, "For a long time Alisa did not want to believe that she had lost."],
                    [None, "She even tried to get the judge to order a rematch, to no avail."],
                    [None, "Dvachevskaya stood up from the table, chanting unprintable."]
                ],
        "mi":   [           # Мику
                    [None, "Miku looked at her cards again, apparently trying to remember them better."],
                    [None, "Or maybe she never learned the rules of the game."],
                    [None, "I wouldn't be surprised."]
                ],
        "us":   [           # Ульяна
                    [us, "Hey, you all played it wrong! You're all crooks, crooks!"],
                    [None, "Shouted Ulyanka, fighting back."],
                    [None, "It took ten minutes to calm her down a little and bring her to her senses."],
                    [None, "In the end, the little one stomped her foot and ran out of the canteen."]
                ],
        "sh":   [           # Шурик
                    [None, "Shurik nodded and got up from the table."],
                    [None, "He seems to have trouble showing emotion."]
                ],
        "mz":   [           # Женя
                    [None, "It's been a long time since I've seen anyone so excited about defeat."],
                    [None, "Zhenya smiled, sighed, and squared her shoulders."],
                    [mz, "Finally!"],
                    [None, "She barked and walked out of the canteen."]
                ]
    }

# ===============================================================================================
# ДЛЯ ИГРОКОВ — ПРОИГРАВШИХ в ФИНАЛЕ
# отсортировано по условному номеру игрока
#             МОЖНО добавить варианты — с дальнейшим рандомным выбором
#  (заготовка словаря, фразы можно дописать по аналогии с 1 туром и 1\2)
# структура: [кто говорит (или None  — если "от автора"), что говорит]
# если несколько строк — и выводиться будет в несколько строк
# ПЛОХИЕ НОВОСТИ — внутритекстовые теги работать не будут.
# -----------------------------------------------------------------------------------------------
    alt_table_gamblers_loser_final = {
        "me":   [           # Сёма
                    [None, "It's not for nothing that they say third place is better than second place."],
                    [None, "After all, third place is still a prize, but second place could have been first, and that's more hurtful."]
                ],
        "un":   [           # Лена
                    [None, "Lena quietly stepped aside, leaving the winner to bask in the glory."]
                ],
        "sl":   [           # Славя
                    [None, "The activist had even more fans than the winner. Most of them were kids from the younger squads."]
                ],
        "dv":   [           # Алиса
                    [None, "Alice tsked unhappily, but that was all."]
                ],
        "mi":   [           # Мику
                    [None, "Lena approached Miku, wanting to console her, but she smiled as if nothing had happened, saying that everything was fine, that she wasn't worried at all, and…"],
                    [None, "Brrr!"],
                    [th, "I'm babbling just like Miku."]

                ],
        "us":   [           # Ульяна
                    [None, "Ulyana strongly disagreed and demanded a rematch from Electronik."],
                    [None, "And she was so active that the squad leader had to be involved to subdue her."]

                ],
        "sh":   [           # Шурик
                    [None, "Shurik took the defeat calmly, as an unfortunate but insignificant circumstance."]
                ],
        "mz":   [           # Женя
                    [None, "The librarian looked like a person whose suffering was finally over."],
                    [mz, "Can I go now?"],
                    [mt, "No."]
                ]
    }

# ===============================================================================================
# словарь склонений номеров столов, стола № 0 — нет, тут склоняем "стол"
# верхний полуфинал = 5, нижний полуфинал = 6, финал = 7
# ПОКА ВЫЗЫВАЮТСЯ НЕ ВСЕ — ЭТО ЦИФРЫ
    alt_table_name_cases = {                                                                                    # словарь склонений столов
        "i": ["table","First","Second","Third","Last","First semifinal","Second semifinal","final"],                     # именительный падеж
        "r": ["table","First","Second","Third","Last","First semifinal","Second semifinal","final"],               # родительный падеж
        "d": ["table","First","Second","Third","Last","First semifinal","Second semifinal","final"],               # дательный падеж
        "t": ["table","On the first","On the second","On the third","On the last","On first semifinal","On second semifinal","final"],      # творительный падеж (винительного не надо)
        "p": ["table","First","Second","Third","Last","First semifinal","Second semifinal","final"]                    # предложный падеж
    }

# ===============================================================================================
# словарь суффиксов принадлежности столов
# ДОЛЖНО БЫТЬ НЕ МЕНЕЕ 4-х значений (максимум 4 стола в проходе, вызванный вариант далее не вызывается)
    alt_table_affiliation = {
        1:  ["taken by","i","i"],                 # если "заняли" = стол: именительный падеж, игроки: именительный падеж
        2:  ["belonged to","i","d"],            # если "принадлежал" = стол: именительный падеж, игроки: дательный падеж
        3:  ["settled","t","i"],          # если "расположились" = стол: творительный падеж, игроки: именительный падеж
        4:  ["meet","t","i"],            # если "встречаются" = стол: творительный падеж, игроки: именительный падеж
        5:  ["firmly occupied by","i","i"]     # если "оккупировали" = стол: именительный падеж, игроки: именительный падеж
    }

# ===============================================================================================
# словарь суффиксов принадлежности столов — победители
# ДОЛЖНО БЫТЬ НЕ МЕНЕЕ 4-х значений (максимум 4 стола в проходе, вызванный вариант далее не вызывается)
    alt_table_winner = {
        1:  [" victory went to","t","d"],                                        # если "победа ушла" = стол: творительный падеж, игроки: дательный падеж
        2:  [" brought good luck to","i","d"],                                       # если "принёс удачу" = стол: именительный падеж, игроки: дательный падеж
        3:  [", everything seemed to be in favor of","t","d"],                         # если "всё подыгрывало" = стол: творительный падеж, игроки: дательный падеж
        4:  [" luck was definitely smiling today for","t","d"]      # если "удача..улыбалась" = стол: творительный падеж, игроки: дательный падеж
    }

# ==============================================================================
#                               ФУНКЦИИ РАССАДКИ
#
# ==============================================================================

init 3 python:
# ----------------------------------------------------------------------------------------
# называем турнирный стол (по его номеру)
    def alt_declare_tournament_tables(table_no):
        global alt_day2_gamblers_1_tour
        global alt_day2_gamblers_semifinal
        global alt_tournament_state
        global alt_table_special_name
        global alt_table_mutual_taunt
        global alt_table_taunt_with_me
        global alt_table_taunt_gamblers
        global alt_table_name_cases
        global alt_table_affiliation
        global alt_random_box_1
        gamblers_tmp = alt_day2_gamblers_1_tour[0:8]                        # копируем список картежников 1 тура (с 0 по 8), рассаженных по столам, упражняемся с копией
        if alt_tournament_state == "1_round_start":                         # если начало 1 тура
            pass
        elif alt_tournament_state == "semifinal_start":                     # если начало полуфинала
            gamblers_tmp.extend(alt_day2_gamblers_semifinal)                # добавляем в конец список картежников полуфинала
        nicks = [gamblers_tmp[2*table_no-2].take, gamblers_tmp[2*table_no-1].take]              # получаем список ников
        nicks.sort()                                                                            # сортируем его по алфавиту
        combine_nicks = "+".join(nicks)                                                         # .. и комбинируем через +
        if combine_nicks in alt_table_special_name:                                                 # если для комбинации игроков предусмотрено специальное представление стола
            table_name = alt_table_name_cases[alt_table_special_name[combine_nicks][1]][table_no]       # склоняем номер стола
            table_title = alt_table_name_cases[alt_table_special_name[combine_nicks][1]][0]             # склоняем слово "стол"
            table_suffix = alt_table_special_name[combine_nicks][0]                                 # склоняем принадлежность стола
            gamblers_case = alt_table_special_name[combine_nicks][2]                                # получаем падеж для игроков
        else:                                                                                   # специального представления стола не предусмотрено
            tab_var = renpy.random.choice(alt_random_box_1)                                 # выбираем из количества оставшихся вариантов
            alt_random_box_1.remove(tab_var)                                                    # из списка вариантов удаляем использованный вариант
            table_name = alt_table_name_cases[alt_table_affiliation[tab_var][1]][table_no]              # склоняем номер стола
            table_title = alt_table_name_cases[alt_table_affiliation[tab_var][1]][0]                    # склоняем слово "стол"
            table_suffix =  alt_table_affiliation[tab_var][0]                                       # склоняем принадлежность стола
            gamblers_case = alt_table_affiliation[tab_var][2]                                       # получаем падеж для игроков
        table = " ".join([table_name,table_title,table_suffix])                  #собираем представление стола в массив .. и комбинируем через " "
        gambler_upper = gamblers_tmp[2*table_no-2].name[gamblers_case]              # получаем имя верхнего игрока в нужном падеже
        gambler_lover = gamblers_tmp[2*table_no-1].name[gamblers_case]              # получаем имя нижнего игрока в нужном падеже
        if combine_nicks in alt_table_mutual_taunt and alt_table_mutual_taunt[combine_nicks] != " ":    # если определен парный таунт
            taunt = alt_table_mutual_taunt[combine_nicks]                                               # … его и покажем
        elif gamblers_tmp[2*table_no-2].take == 'me':                                       # если в паре первый игрок — Сёмен
            # показываем таунт второго игрока с Семеном (рандом 1/длина списка)
            taunt = alt_table_taunt_with_me[gamblers_tmp[2*table_no-1].take][renpy.random.randint(0,len(alt_table_taunt_with_me[gamblers_tmp[2*table_no-1].take])-1)]
        elif gamblers_tmp[2*table_no-1].take == 'me':                                       # если в паре второй игрок — Сёмен
            # показываем таунт первого игрока (рандом 1/длина списка)
            taunt = alt_table_taunt_with_me[gamblers_tmp[2*table_no-2].take][renpy.random.randint(0,len(alt_table_taunt_with_me[gamblers_tmp[2*table_no-2].take])-1)]
        else:                                                                                           # если нет особых условий
            # таунт второго игрока в списке (рандом 1/длина списка)
            taunt = alt_table_taunt_gamblers[gamblers_tmp[2*table_no-1].take][renpy.random.randint(0,len(alt_table_taunt_gamblers[gamblers_tmp[2*table_no-1].take])-1)]
        return table, gambler_upper, gambler_lover, taunt

# ----------------------------------------------------------------------------------------
# Проверяем, есть ли что в общем словаре
    def alt_whats_in_mutual_table_win_los(winner_take, loser_take):
        global alt_table_mutual_gamblers_win_los
        winner_sentence = loser_sentence = None                                 # считаем, для победителя и проигравшего совместных фраз нет
        combine_nicks = ">".join([winner_take, loser_take])                     # комбинируем ники через ">"
        if combine_nicks in alt_table_mutual_gamblers_win_los:                  # если есть такая комбинация  в словаре
            united_sentence = alt_table_mutual_gamblers_win_los[combine_nicks]  # загружаем список фраз по ключу
            if united_sentence.count("*") == 1:                                 # если найден только один разделитель "*"
                delimiter = united_sentence.index("*")                          # получаем позицию разделителя списка
                if delimiter != 0:                                              # если позиция разделителя не в начале списка
                    if len(united_sentence[0]) != 0:                            # если первая фраза не пустая
                        if united_sentence[0][1] not in [None, " "]:            # если собственно фраза не пустая
                            winner_sentence = united_sentence[0:delimiter]      # получаем список фраз победителя
                if delimiter !=  united_sentence[-1]:                           # если позиция разделителя не в конце списка
                    if len(united_sentence[delimiter+1]) != 0:                  # если первая фраза после разделителя не пустая
                        if united_sentence[delimiter+1][1] not in [None, " "]:  # если собственно фраза не пустая
                            loser_sentence = united_sentence[delimiter+1:len(united_sentence)]      # получаем список фраз проигравшего
        return winner_sentence, loser_sentence

# ----------------------------------------------------------------------------------------
# подводим итоги стола (по его номеру, список игроков)
    def alt_declare_results_tables(table_no, gamblers):
        global alt_table_name_cases
        global alt_table_gamblers_winner_1_tour
        global alt_table_gamblers_loser_1_tour
        global alt_table_gamblers_winner_semifinal
        global alt_table_gamblers_loser_semifinal
        global alt_table_winner
        global alt_random_box_1
        tab_var = renpy.random.choice(alt_random_box_1)                                     # выбираем из количества оставшихся вариантов
        alt_random_box_1.remove(tab_var)                                                    # из списка вариантов удаляем использованный вариант
        table_name = alt_table_name_cases[alt_table_winner[tab_var][1]][table_no]                     # склоняем номер стола
        table_title = alt_table_name_cases[alt_table_winner[tab_var][1]][0]                    # склоняем слово "стол"
        table_suffix =  alt_table_winner[tab_var][0]                                       # склоняем принадлежность стола
        winner_case = alt_table_winner[tab_var][2]                                       # получаем падеж для победителя
        table = " ".join([table_name,table_title])                                       # собираем представление стола в массив .. и комбинируем через " "
        table = table + table_suffix
        if table_no <= 4:                                                       # если № стола 1..4
            m = table_no                                                        # указатель — по номеру стола
        else:
            m = table_no - 4                                                    # указатель = номер стола — 4
        gambler_winner = gamblers[2*m-2].name[winner_case]                      # получаем имя победителя в нужном падеже
        winner_take = gamblers[2*m-2].take                                      # получаем ник победителя
        loser_take = gamblers[2*m-1].take                                       # получаем ник проигравшего
        winner_sentence, loser_sentence = alt_whats_in_mutual_table_win_los(winner_take, loser_take) # проверяем. есть ли что в общем словаре, если есть — вытаскиваем фразы оттуда
        if winner_sentence != None:                                             # если разыскали что-то в общем словаре для победителя
            winner_remark = winner_sentence[:]                                  # фразы победителей берём из общего словаря
        else:
            if table_no <= 4:                                                   # если № стола 1..4
                w = alt_table_gamblers_winner_1_tour                            # фразы победителей — по словарю 1 тура
            else:
                w = alt_table_gamblers_winner_semifinal                         # фразы победителей — по словарю полуфинала
            j = len(w[winner_take])                                             # получаем количество фраз
            winner_remark = []                                                  # ремарка победителя
            for i in range (0,j):                                               # читаем строки из словаря победителей
                winner_remark.append(w[winner_take][i])                         # добавляем в список очередную фразу
        if loser_sentence != None:                                              # если в совместном блоке для проигравшего что-то есть
            loser_remark = loser_sentence[:]                                    # фразы проигравших берём из общего словаря
        else:
            if table_no <= 4:                                                   # если № стола 1..4
                l = alt_table_gamblers_loser_1_tour                             # фразы проигравших — по словарю 1 тура
            else:                                                               # если № стола 5 и выше
                l = alt_table_gamblers_loser_semifinal                          # фразы проигравших — по словарю полуфинала
            j = len(l[loser_take])                                              # получаем количество фраз
            loser_remark = []                                                   # ремарка проигравшего
            for i in range (0,j):                                               # читаем строки из словаря проигравших
                loser_remark.append(l[loser_take][i])                           # добавляем в список очередную фразу
        return table, gambler_winner, winner_remark, loser_remark

# ----------------------------------------------------------------------------------------
# подводим итоги финала (победитель, проигравший)
    def alt_declare_results_final(winner_take, loser_take):
        global alt_table_gamblers_winner_final
        global alt_table_gamblers_loser_final
        winner_sentence, loser_sentence = alt_whats_in_mutual_table_win_los(winner_take, loser_take) # проверяем. есть ли что в общем словаре, если есть — вытаскиваем фразы оттуда
        if winner_sentence != None:                                             # если разыскали что-то в общем словаре для победителя
            winner_remark = winner_sentence[:]                                  # фразы победителей берём из общего словаря
        else:
            w = alt_table_gamblers_winner_final                             # фразы победителей — по словарю финала
            j = len(w[winner_take])                                                 # получаем количество фраз
            winner_remark = []                                                      # ремарка победителя
            for i in range (0,j):                                                   # читаем строки из словаря победителей
                winner_remark.append(w[winner_take][i])                             # добавляем в список очередную фразу
        if loser_sentence != None:                                             # если разыскали что-то в общем словаре для проигравшего
            loser_remark = loser_sentence[:]                                   # фразы победителей берём из общего словаря
        else:
            l = alt_table_gamblers_loser_final                              # фразы проигравших — по словарю финала
            j = len(l[loser_take])
            loser_remark = []
            for i in range (0,j):
                loser_remark.append(l[loser_take][i])
        return winner_remark, loser_remark

# ----------------------------------------------------------------------------------------
# тащим картинку картёжника
    def alt_get_img_playon(gamblers):
        prefix  = default_7dl_path+"Pics/gui/tournament/"
        suffix = "_playon.png"
        return prefix+gamblers+suffix

# ----------------------------------------------------------------------------------------
# создаём игроков
    def alt_set_gamblers():
        gamblers = []                                       # Картежники: (ники) 0:Семён, 1:Лена, 2:Славя, 3:Алиса, 4:Мику, 5:Ульянка, 6:Шурик, 7:Женя
        nick_of_gamblers = [me,un,sl,dv,mi,us,sh,mz]                                                            # ХАРАКТЕРЫ
        take_of_gamblers = ['me','un','sl','dv','mi','us','sh','mz']                                            # ники (текст)
    # Склоняем картежников (имена):
        #name_me = [u'я',u'меня',u'мне',u'меня',u'мной',u'мне']                                                  # имена Семёна (именительный..предложный)
        name_me = [u'yours truly','yours truly','yours truly','yours truly','yours truly','yours truly']
        name_un = [u'Lena',u'Lena',u'Lena',u'Lena',u'Lena',u'Lena']                                            # имена Лены (именительный..предложный)
        name_sl = [u'Slavya',u'Slavya',u'Slavya',u'Slavya',u'Slavya',u'Slavya']                                      # имена Слави (именительный..предложный)
        name_dv = [u'Alisa',u'Alisa',u'Alisa',u'Alisa',u'Alisa',u'Alisa']                                      # имена Алисы (именительный..предложный)
        name_mi = [u'Miku']*6                                                                                   # имена Мику (именительный..предложный) = одинаковые, но пусть так
        name_us = [u'Ulyana',u'Ulyana',u'Ulyana',u'Ulyana',u'Ulyana',u'Ulyana']                          # имена Ульяны (именительный..предложный)
        name_sh = [u'Shurik',u'Shurik',u'Shurik',u'Shurik',u'Shurik',u'Shurik']                                 # имена Шурика (именительный..предложный)
        name_mz = [u'Zhenya',u'Zhenya',u'Zhenya',u'Zhenya',u'Zhenya',u'Zhenya']                                            # имена Жени (именительный..предложный)
        name_of_gamblers = [name_me,name_un,name_sl,name_dv,name_mi,name_us,name_sh,name_mz]                    # список списков имен картежников
        cases = ['i','r','d','v','t','p']                                              # Список используемых падежей
    # Создаем картежников
        for i in range (0,8):                                                           # для 8 картежников (номер элемента списка = номер картежника)
            gambler = []                                                                # очередной картежник
            gambler.nick = nick_of_gamblers[i]                                          # ник картежника (ХАРАКТЕР)
            gambler.take = take_of_gamblers[i]                                          # ник картежника (текст)
            gambler.name = {}                                                           # имя картёжника (словарь падежей) — пустой
            for j in range (0,6):                                                       # перебираем падежи
                gambler.name[cases[j]] = name_of_gamblers[i][j]                         # имя картежника = словарь "падеж":"имя в падеже"
            gambler.face = alt_get_img_playon(gambler.take)                             # иконка игрока в турнире, путь к файлу
            gambler.image = gambler.take+"_playon"                                      # иконка игрока в турнире, псевдоним
            gambler.place = None                                                        # № места игрока
            gambler.place_xy = None                                                     # координаты места игрока [x,y]
            gambler.table = None                                                        # № стола игрока
            gambler.winner = False                                                      # Игрок победил
            gamblers.append(gambler)                                                    # добавляем очередного картёжника в список
        return gamblers                                                                 # функция возвращает список картежников

# ----------------------------------------------------------------------------------------
# округляем пару чисел мест — для № стола
    def alt_round_up(x):
        y = int(round((x+1.5)/2))                                                       # 1,5 добавляем из-за особенностей округления питона
        return y

# ----------------------------------------------------------------------------------------
# рассаживаем  картёжников по столам (начальный расклад) — ВЫЗЫВАЕТСЯ ОДИН РАЗ
    def alt_gamblers_shuffler():
        global alt_winners_1_tour
        global alt_losers_1_tour
        places_1_round = range(8)                                                       # список мест в 1 раунде — для рандома
    # первоначальная рассадка (снизу вверх) 0-3 слева, 4-7 справа
        x_gamblers_1_round = [459,1315]                                                 # координаты x начальных мест рассадки (слева, справа)
        y_gamblers_1_round = [157,312,620,775]                                          # координаты y начальных мест рассадки (сверху вниз)
        places_gamblers_1_round = []                                                    # места первоначальной рассадки
    # полуфинал места 8-9-10-11
        x_gamblers_semifinal = [648,1135]                                               # координаты x полуфинала (слева, справа)
        y_gamblers_semifinal = [235,698]                                                # координаты y полуфинала (сверху вниз)
        places_gamblers_semifinal = []                                                  # места полуфинала (0-3), добавляем 8
    # финал места 12-13
        places_gamblers_final = [[888,358],[888,573]]*2                                 # места финала, 1-3 стол — верхнее, 2-4 стол — нижнее
        for i in range (0,2):                                                           # запускаем цикл в цикле по x, y
            for j in range (0,4):
                places_gamblers_1_round.append([x_gamblers_1_round[i],y_gamblers_1_round[j]]) # очередному месту присваиваем координаты
        for i in range (0,2):                                                           # запускаем цикл в цикле по x, y
            for j in range (0,2):
                places_gamblers_semifinal.append([x_gamblers_semifinal[i],y_gamblers_semifinal[j]]) # очередному месту присваиваем координаты
        gamblers = alt_set_gamblers()                                                   # формируем список игроков (ссылка)
        if (alt_day2_detour_number != 0):                                               # если выбрали конкретного соперника для финала
            for k in (0, alt_day2_detour_number):                                       # сначала рассаживаем Семёна и соперника для финала
                if k == 0:
                    place = 0                                                           # Семёна - за первый стол
                elif k == alt_day2_detour_number:
                    place = 7                                                           # соперника для финала - за четвёртый стол
                gamblers[k].place = place                                                   # Даём игроку место
                gamblers[k].place_xy = places_gamblers_1_round[place]                       # Даём игроку координаты места
                gamblers[k].table = alt_round_up(place)                                     # № стола = округлвверх (№ места)
                gamblers[k].place_sm_xy = places_gamblers_semifinal[gamblers[k].table-1]    # Даём игроку координаты места в полуфинале
                gamblers[k].place_f_xy = places_gamblers_final[gamblers[k].table-1]         # Даём игроку координаты места в финале
                gamblers[k].place_w_xy = [1049,458]                                         # координаты победителя турнира 1051.460
                gamblers[k].winner = False                                                  # сбрасываем флаг победителя
                places_1_round.remove(place)                                                # из списка мест удаляем присвоенное место
        k = 0                                                                           # Счетчик циклов рандома
        while k < 8:                                                                    # Пока счетчик < 8 (места с 0 по 7)
            if (k in (0, alt_day2_detour_number)) and (alt_day2_detour_number != 0):    # если игроку уже присвоено место (Семён или соперник для финала)
                k += 1                                                                  # переходим к следующему
            else:                                                                       # обычная рандомная рассадка
                place = renpy.random.choice(places_1_round)                                 # Место = случайное из списка оставшихся мест
                gamblers[k].place = place                                                   # Даём игроку место
                gamblers[k].place_xy = places_gamblers_1_round[place]                       # Даём игроку координаты места
                gamblers[k].table = alt_round_up(place)                                     # № стола = округлвверх (№ места)
                gamblers[k].place_sm_xy = places_gamblers_semifinal[gamblers[k].table-1]    # Даём игроку координаты места в полуфинале
                gamblers[k].place_f_xy = places_gamblers_final[gamblers[k].table-1]         # Даём игроку координаты места в финале
                gamblers[k].place_w_xy = [1049,458]                                         # координаты победителя турнира 1051.460
                gamblers[k].winner = False                                                  # сбрасываем флаг победителя
                places_1_round.remove(place)                                                # из списка мест удаляем присвоенное место
                k += 1                                                                      # увеличиваем счетчик на 1
        alt_winners_1_tour = []                                                             # Победители  1 тура — очищаем
        alt_losers_1_tour = []                                                              # Проигравшие в 1 туре — очищаем
        return gamblers                                                                     # функция возвращает список картежников, "рассаженных" по столам

# ----------------------------------------------------------------------------------------
# узнаём своего соперника
    def alt_get_me_rival(gamblers):
        gamblers_tmp = gamblers[:]                                                      # копируем сет игроков, упражняемся с ним, не трогаем основной
        for i in range (0,len(gamblers_tmp)):                                           # перебираем игроков
            if gamblers_tmp[i].take == 'me':                                            # если очередной игрок — Семён
                table = gamblers_tmp[i].table                                           # узнаём номер своего стола
                del gamblers_tmp[i]                                                     # удаляем себя из списка
                break                                                                   # на этом цикл заканчиваем
        for i in range (0,len(gamblers_tmp)):                                           # перебираем оставшихся
            if gamblers_tmp[i].table == table:                                          # если № стола очередного игрока совпадает с моим
                rival = gamblers_tmp[i]                                                 # он и есть мой соперник
                break                                                                   # на этом цикл заканчиваем
        return rival                                                                    # функция возвращает моего соперника

# ----------------------------------------------------------------------------------------
# узнаём второго соперника в финале
    def alt_get_me_rival_final(gamblers,gambler):
        gamblers_tmp = gamblers[:]                                                      # копируем сет игроков, упражняемся с ним, не трогаем основной
        for i in range (0,len(gamblers_tmp)):                                           # перебираем игроков
            if gamblers_tmp[i].take != gambler.take:                                    # если очередной игрок не Семён или его победитель в 1/2
                rival = gamblers_tmp[i]                                                 # он и есть второй соперник
                index = i                                                               # .. и индекс соперника в списке
        return rival, index                                                             # функция возвращает второго соперника

# ----------------------------------------------------------------------------------------
# Получаем номер места игрока для сортировки
    def alt_sort_gamblers_by_place(x):
        return x.place

# ----------------------------------------------------------------------------------------
# Упорядочиваем игроков по номерам мест
    def alt_gamblers_arrange(gamblers):
        gamblers_tmp = gamblers[:]                                                      # копируем сет игроков, упражняемся с ним, не трогаем основной
        gamblers_tmp.sort(cmp,alt_sort_gamblers_by_place)                               # сортируем список по номеру мест (от 0 до 7)
        return gamblers_tmp

# ----------------------------------------------------------------------------------------
# Узнаём своё место
    def alt_get_my_table(gamblers):
        for i in range(1,9):                                                            # перебираем столы — все (1-4 начало, 5-6 полуфинал)
            if gamblers[2*i-2].take == 'me':                                            # если в паре первый игрок — Сёмен
                table = gamblers[2*i-2].table                                           # номер стола
                places = [2*i-2, 2*i-1, table]                                          # места Семёна и соперника, № стола
                break                                                                   # на этом цикл заканчиваем
            elif gamblers[2*i-1].take == 'me':                                          # если в паре второй игрок — Сёмен
                table = gamblers[2*i-1].table                                           # номер стола
                places = [2*i-1, 2*i-2, table]                                          # места Семёна и соперника, № стола
                break                                                                   # на этом цикл заканчиваем
        return places

# ----------------------------------------------------------------------------------------
# Где там Алиса?
    def alt_get_result_dv(gamblers, count):
        me_table = dv_table_los = dv_table_win = 0                                      # столы = 0
        result = 0                                                                      # результат = 0 (мы продули ДваЧе)
        for i in range(0, count):                                                       # переберем игроков
            if gamblers[i].take == "me":                                                # если очередной игрок — Семён
                if gamblers[i].winner == False:                                         # и он — проигравший
                    break                                                               # на том анализ заканчиваем
                else:                                                                   # а вот если выиграл
                    me_table = gamblers[i].table                                        # получаем стол Семёна
                    continue                                                            # следующий игрок
            elif gamblers[i].take == "dv":                                              # если очередной игрок — Алиса
                if gamblers[i].winner == False:                                         # и она — проиграла
                    dv_table_los = gamblers[i].table                                    # получаем стол Алисы — проигравшей
                    continue                                                            # следующий игрок
                else:                                                                   # Если Алиса победила
                    dv_table_win = gamblers[i].table                                    # получаем стол Алисы — победившей
        else:                                                                           # если Семён не проиграл
            if me_table == dv_table_los:                                                # и номера столов Семёна и Алисы-проигравшей совпали
                result = 1                                                              # Дваче продула именно Семёну
            elif me_table != dv_table_los and dv_table_los != 0:                        # Если номера столов Семёна и Алисы-проигравшей НЕ совпали, и стол Алисы не 0
                result = 2                                                              # Дваче продула, но не Семёну
            if dv_table_win != 0:                                                       # Дваче кого-то таки нагнула
                if me_table == dv_table_win:                                            # Если номера столов одинаковые
                    result = 3                                                          # Сёма и Алиса встретятся за одним столом
                else:
                    result = 4                                                          # Сёма и Алиса будут за разными столами
        return result

# ----------------------------------------------------------------------------------------
# Показываем турнирную таблицу перед первым раундом (игроки)
    def alt_show_tournament_table_1_round(gamblers):
        global alt_mstt
        background = 'bg int_dining_hall_sunset'
        table = 'alt_tournament_bg'
        if alt_mstt == 9:
            renpy.scene('underlay')
            renpy.scene('master')
            renpy.show(background,layer='underlay')                                 # показываем подоснову
            renpy.show(table,layer='underlay')                                      #показываем турнирную таблицу
            renpy.with_statement(dissolve)
            return
        elif alt_mstt < 9:
            j = alt_mstt                                                            # локальный счетчик — по глобальному
            ui.layer('underlay')
            while j < 8:                                                            # пока счетчик меньше 8
                for i in range(0,j+1):                                              # пока счетчик изображений в диапазоне 0 — очередной игрок
                    ui.image(gamblers[i].face,xpos=gamblers[i].place_xy[0],ypos=gamblers[i].place_xy[1])    # показываем очередную картинку (от 1 до всех)
                    renpy.transition(diam,layer='underlay')
                j += 1                                                               # увеличиваем счётчик
                ui.close()                                                          # закрываем слой
                alt_mstt = j                                                        # глобальный счетчик — по локальному
                if alt_mstt >= 8:                                                   # если счетчик добрался до 8 (показали всех)
                    alt_mstt = 0                                                    # обнуляем счетчик
                return                                                              # возвращаемся

# ----------------------------------------------------------------------------------------
# показываем турнирную таблицу после 1 раунда и перед полуфиналом (игроки)
    def alt_show_tournament_table_semifinal(gamblers,gamblers_2 = None):
        global alt_mstt
        global alt_table_no
        global alt_winners_1_tour
        global alt_losers_1_tour
        global alt_day2_gamblers_semifinal
        background = 'bg int_dining_hall_sunset'
        table = 'alt_tournament_bg'
        if (alt_table_no == 0) or ((alt_table_no == 5) and (alt_mstt == 8)):
            renpy.scene('underlay')
            renpy.scene('master')
            renpy.show(background,layer='underlay')                                 # показываем подоснову
            ui.layer('underlay')                                                    # выводим монохромные картинки 1 тура
            ui.image(ImageReference(table))                                         # показываем турнирную таблицу
            for i in range(0,8):
                gray = im.MatrixColor(gamblers[i].face, im.matrix.brightness(-0.1)*im.matrix.saturation(0.05))
                alpha = im.Alpha(gray, 0.7)
                ui.imagebutton(gray, gray, clicked=None, xpos=gamblers[i].place_xy[0], ypos=gamblers[i].place_xy[1])
            if (alt_table_no == 5) and (alt_mstt == 8):
                for j in range(0,4):
                    color =  im.MatrixColor(gamblers_2[j].face,im.matrix.brightness(-0.1)*im.matrix.saturation(0.9))
                    ui.imagebutton(color, color, clicked=None, xpos=gamblers_2[j].place_sm_xy[0], ypos=gamblers_2[j].place_sm_xy[1])
                    alt_day2_gamblers_semifinal[j].winner = False
            ui.close()                                                              # закрываем слой
            if alt_table_no == 0:
                alt_winners_1_tour = []                                         # очищаем победителей 1 тура
                alt_losers_1_tour =[]                                           # очищаем проигравших 1 тура
                for i in range(0,8):
                    renpy.show(gamblers[i].image, at_list=[Transform(xpos=gamblers[i].place_xy[0],ypos=gamblers[i].place_xy[1],xanchor=0,yanchor=0)], layer='underlay')
                    if gamblers[i].winner == True:
                        alt_winners_1_tour.append(gamblers[i])
                    else:
                        alt_losers_1_tour.append(gamblers[i])
                for j in range(0,4):
                    gamblers[2*j:2*j+1] = [alt_winners_1_tour[j],alt_losers_1_tour[j]]
                alt_day2_gamblers_semifinal = alt_winners_1_tour[:]                     # полуфиналисты — копия победителей 1 тура
                temp = alt_day2_gamblers_semifinal.pop(2)                               # меняем местами 1 и 2 элементы
                alt_day2_gamblers_semifinal.insert(1,temp)                              #
                for k in range(0,4):                                                    # перебираем игроков
                    alt_day2_gamblers_semifinal[k].place = k+8                          # присваиваем новое место (с 8-го)
                    alt_day2_gamblers_semifinal[k].table = alt_round_up(k+8)            # присваиваем новый номер стола (5, 6)
                    alt_table_no = 1
            renpy.with_statement(dissolve)
            return
        elif alt_table_no < 5:
            j = alt_mstt                                                # локальный счетчик — по глобальному
            while j < 8:                                                # пока счетчик меньше 8
                if gamblers[j].winner == True:
                    x1 = gamblers[j].place_xy[0]
                    y1 = gamblers[j].place_xy[1]
                    x2 = gamblers[j].place_sm_xy[0]
                    y2 = gamblers[j].place_sm_xy[1]
                    renpy.hide(gamblers[j].image, layer='underlay')
                    renpy.show(gamblers[j].image, at_list=[Move((x1,y1), (x2,y2), 1.5)], layer='underlay')
                else:
                    renpy.transition(wipedown2, layer='underlay')
                    renpy.hide(gamblers[j].image, layer='underlay')
                j += 1                                                   # увеличиваем счётчик
                alt_mstt = j
                return
        elif (alt_table_no >= 5) and (alt_mstt < 5):
            j = alt_mstt                                                # локальный счетчик — по глобальному
            while j < 4:                                                # пока счетчик меньше 4
                renpy.show(gamblers_2[j].image, at_list=[Transform(xpos=gamblers_2[j].place_sm_xy[0],ypos=gamblers_2[j].place_sm_xy[1],xanchor=0,yanchor=0)], layer='underlay')
                renpy.transition(diam, layer='underlay')
                j += 1                                                   # увеличиваем счётчик
                alt_mstt = j
                return

# ----------------------------------------------------------------------------------------
# показываем турнирную таблицу после полуфинала (игроки)
    def alt_show_tournament_table_final(gamblers,gamblers_2 = None):
        global alt_mstt
        global alt_table_no
        global alt_day2_gamblers_1_tour
        global alt_winners_semifinal
        global alt_losers_semifinal
        global alt_day2_gamblers_final
        background = 'bg int_dining_hall_sunset'
        table = 'alt_tournament_bg'
        if alt_table_no == 4:
            gamblers_0 = alt_day2_gamblers_1_tour[:]
            renpy.scene('underlay')
            renpy.scene('master')
            renpy.show(background,layer='underlay')                                 # показываем подоснову
            ui.layer('underlay')                                                    # выводим монохромные картинки 1 тура
            ui.image(ImageReference(table))                                         # показываем турнирную таблицу
            for i in range(0,8):                                                    # вывели первый тур
                gray = im.MatrixColor(gamblers_0[i].face, im.matrix.brightness(-0.1)*im.matrix.saturation(0.05))
                ui.imagebutton(gray, gray, clicked=None, xpos=gamblers_0[i].place_xy[0], ypos=gamblers_0[i].place_xy[1])
            for j in range(0,4):
                gray = im.MatrixColor(gamblers[j].face, im.matrix.brightness(-0.1)*im.matrix.saturation(0.05))
                ui.imagebutton(gray, gray, clicked=None, xpos=gamblers[j].place_sm_xy[0], ypos=gamblers[j].place_sm_xy[1])
            ui.close()
            alt_winners_semifinal = []
            alt_losers_semifinal =[]
            for k in range(0,4):
                renpy.show(gamblers[k].image, at_list=[Transform(xpos=gamblers[k].place_sm_xy[0],ypos=gamblers[k].place_sm_xy[1],xanchor=0,yanchor=0)], layer='underlay')
                if gamblers[k].winner == True:
                    alt_winners_semifinal.append(gamblers[k])
                else:
                    alt_losers_semifinal.append(gamblers[k])
            for f in range(0,2):
                gamblers[2*f:2*f+1] = [alt_winners_semifinal[f],alt_losers_semifinal[f]]
            alt_day2_gamblers_final = alt_winners_semifinal[:]
            alt_table_no = 5
            renpy.with_statement(dissolve)
            return
        elif alt_table_no > 4:
            j = alt_mstt                                                # локальный счетчик — по глобальному
            while j < 4:                                                # пока счетчик меньше 4
                if gamblers[j].winner == True:
                    x1 = gamblers[j].place_sm_xy[0]
                    y1 = gamblers[j].place_sm_xy[1]
                    x2 = gamblers[j].place_f_xy[0]
                    y2 = gamblers[j].place_f_xy[1]
                    renpy.hide(gamblers[j].image, layer='underlay')
                    renpy.show(gamblers[j].image, at_list=[Move((x1,y1), (x2,y2), 1.5)], layer='underlay')
                else:
                    renpy.transition(wipedown2, layer='underlay')
                    renpy.hide(gamblers[j].image, layer='underlay')
                j += 1                                                   # увеличиваем счётчик
                alt_mstt = j
                return

# ----------------------------------------------------------------------------------------
# Показываем турнирную таблицу — победа в финале (игроки)
    def alt_show_tournament_table_win(gamblers_1,gamblers_2,gamblers_3):
        global alt_mstt
        global alt_tournament_state
        background = 'bg int_dining_hall_sunset'
        table = 'alt_tournament_bg'
        if alt_mstt == 2 and alt_tournament_state == "final_start":
            for m in range(0,2):
                gamblers_3[m].winner = False
        if alt_mstt == 2 or (alt_mstt == 3 and alt_tournament_state == "final_end"):
            renpy.scene('underlay')
            renpy.scene('master')
            renpy.show(background,layer='underlay')
            ui.layer('underlay')
            ui.image(ImageReference(table))
            for i in range(0,8):                                                                                            # вывели первый тур
                gray = im.MatrixColor(gamblers_1[i].face, im.matrix.brightness(-0.1)*im.matrix.saturation(0.05))
                ui.imagebutton(gray, gray, clicked=None, xpos=gamblers_1[i].place_xy[0], ypos=gamblers_1[i].place_xy[1])
            for j in range(0,4):                                                                                            # вывели полуфинал
                gray = im.MatrixColor(gamblers_2[j].face, im.matrix.brightness(-0.1)*im.matrix.saturation(0.05))
                ui.imagebutton(gray, gray, clicked=None, xpos=gamblers_2[j].place_sm_xy[0], ypos=gamblers_2[j].place_sm_xy[1])
            for k in range(0,2):                                                                                            # вывели финал
                gray = im.MatrixColor(gamblers_3[k].face, im.matrix.brightness(-0.1)*im.matrix.saturation(0.05))
                ui.imagebutton(gray, gray, clicked=None, xpos=gamblers_3[k].place_f_xy[0], ypos=gamblers_3[k].place_f_xy[1])
            renpy.with_statement(dissolve)
            ui.close()
            for m in range(0,2):
                renpy.show(gamblers_3[m].image, at_list=[Transform(xpos=gamblers_3[m].place_f_xy[0],ypos=gamblers_3[m].place_f_xy[1],xanchor=0,yanchor=0)], layer='underlay')
            if alt_mstt == 2:
                return
        if alt_mstt == 3:
            if gamblers_3[0].winner == False:
                temp = gamblers_3.pop(1)
                gamblers_3.insert(0,temp)
            return
        if alt_mstt < 2:
            j = alt_mstt
            if gamblers_3[j].winner == True:
                x1 = gamblers_3[j].place_f_xy[0]
                y1 = gamblers_3[j].place_f_xy[1]
                x2 = gamblers_3[j].place_w_xy[0]
                y2 = gamblers_3[j].place_w_xy[1]
                renpy.hide(gamblers_3[j].image, layer='underlay')
                renpy.show(gamblers_3[j].image, at_list=[Move((x1,y1), (x2,y2), 1.3)], layer='underlay')
            else:
                renpy.transition(wipedown2, layer='underlay')
                renpy.hide(gamblers_3[j].image, layer='underlay')
            renpy.with_statement(dissolve)
            return

# ----------------------------------------------------------------------------------------
# Рандомизатор пропуска игры (поражение в 1 туре)
    def alt_drawing_of_detour():
        global alt_day2_gamblers_1_tour
        global alt_day2_gamblers_semifinal
        global alt_day2_my_seat
        winners_1 = []
        alt_day2_my_seat = None
        alt_day2_gamblers_semifinal = []                        # очищаем полуфиналистов
        for i in range(0,8):                                    # сортируем игроков 1 тура
            if alt_day2_gamblers_1_tour[i].winner == True:
                winners_1.append(alt_day2_gamblers_1_tour[i])
            if alt_day2_gamblers_1_tour[i].take == 'me':        # смотрим, где там наш Сёма сидел
                alt_day2_my_seat = i
            alt_day2_gamblers_1_tour[i].winner = False          # сбрасываем всем флаги побед
        alt_day2_gamblers_semifinal = winners_1[:]              # копируем победителей в полуфинальный список
        temp = alt_day2_gamblers_semifinal.pop(2)               # меняем местами 2 и 3 полуфиналиста
        alt_day2_gamblers_semifinal.insert(1,temp)
        return

# ----------------------------------------------------------------------------------------
# Рандомизатор пропуска игры (поражение в 1 туре — идём через полуфинал)
    def alt_drawing_of_detour_semifinal():
        global alt_day2_gamblers_semifinal
        for j in [0,2]:                                         # сортируем игроков 1 тура
            alt_day2_gamblers_semifinal[j+renpy.random.choice([0,1])].winner = True        # два рандомных победителя (между 0 и 1, 2 и 3)
        return

# ----------------------------------------------------------------------------------------
# Рандомизатор пропуска игры (поражение в 1 туре — идём через финал)
    def alt_drawing_of_detour_final():
        global alt_day2_my_seat
        global alt_day2_gamblers_final
        global alt_rival_final
        if alt_day2_my_seat in [0,1,4,5]:                                  # если Сэмэн сидел сверху
            alt_rival_final = alt_day2_gamblers_final[0]        # то его "победитель" — первый финалист
        elif alt_day2_my_seat in [2,3,6,7]:                                # если Сэмэн сидел снизу
            alt_rival_final = alt_day2_gamblers_final[1]        # то его "победитель" — второй финалист
        return

# ----------------------------------------------------------------------------------------
# Сопоставление покерных комбинаций на руках у соперников
    def alt_comparison_poker_hands(winner_hand, loser_hand, winner, loser):
        name_of_combo = {                                           # склонения комбинаций по падежам
            0:  {                                                   # Старшая карта
                    'i':    ["high", "high", "high cards"],
                    'r':    ["high", "high", "high cards"],
                    'd':    ["high", "high", "high cards"],
                    'v':    ["high", "high", "high cards"],
                    't':    ["high", "high", "high cards"],
                    'p':    ["high", "high", "high cards"],
                    'num':  0,                                      # число карты — единственное
                    'case': None,                                   # падеж — транзит на карту
                    'cas0': 'i',                                    # падеж для 0 — именительный
                    'pr':   None,                                   # приставки нет
                    'me':   None                                    # Сёмино местоимение — транзит на карту
                    },
            1:  {                                                   # Пара
                    'i':    ["pair", "", "pairs"],
                    'r':    ["pair", "", "pairs"],
                    'd':    ["pair" "", "pairs"],
                    'v':    ["pair", "", "pairs"],
                    't':    ["pair", "", "pairs"],
                    'p':    ["pair" "", "pairs"],
                    'num':  1,                                      # число карты — множественное
                    'case': 'r',                                    # падеж — родительный (пара двоек)
                    'cas0': 'r',                                    # падеж для 0 — родительный (из троек)
                    'pr':   "из ",                                  # приставка для 0
                    'me':   1                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            2:  {                                                   # Две пары (добавить куда-то "и")
                    'i':    ["two pairs", "", "two pairs"],
                    'r':    ["two pairs", "", "two pairs"],
                    'd':    ["two pairs" "", "two pairs"],
                    'v':    ["two pairs", "", "two pairs"],
                    't':    ["two pairs", "", "two pairs"],
                    'p':    ["two pairs" "", "two pairs"],
                    'num':  1,                                      # число карты — множественное
                    'case': 'r',                                     # падеж — родительный (пара троек и двоек)
                    'cas0': 'r',                                    # падеж для 0 — родительный (из дам и шестёрок)
                    'pr':   "из ",                                  # приставка для 0
                    'me':   2                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            3:  {                                                   # Тройка
                    'i':    ["three of a kind", "", "three of a kind"],
                    'r':    ["three of a kind" "", "three of a kind"],
                    'd':    ["three of a kind" "", "three of a kind"],
                    'v':    ["three of a kind" "", "three of a kind"],
                    't':    ["three of a kind" "", "three of a kind"],
                    'p':    ["three of a kind" "", "three of a kind"],
                    'num':  1,                                      # число карты — множественное
                    'case': 'r',                                     # падеж — родительный (тройка дам)
                    'cas0': 'r',                                    # падеж для 0 — родительный (из девяток)
                    'pr':   "from ",                                  # приставка для 0
                    'me':   1                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            4:  {                                                   # Стрит
                    'i':    ["straight from", "", "straights"],
                    'r':    ["straight from", "", "straights"],
                    'd':    ["straight from", "", "straights"],
                    'v':    ["straight from", "", "straights"],
                    't':    ["straight from", "", "straights"],
                    'p':    ["straight from", "", "straights"],
                    'num':  0,                                      # число карты — единственное
                    'case': 'r',                                     # падеж — родительный (стрит от короля, стрит от семёрки)
                    'cas0': 'r',                                    # падеж для 0 — родительный (от семёрки)
                    'pr':   "from ",                                  # приставка для 0
                    'me':   0                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            5:  {                                                   # Флеш ("от" добавить в мастях)
                    'i':    ["flush", "", "flushes"],
                    'r':    ["flush", "", "flushes"],
                    'd':    ["flush", "", "flushes"],
                    'v':    ["flush", "", "flushes"],
                    't':    ["flush", "", "flushes"],
                    'p':    ["flush", "", "flushes"],
                    'num':  0,                                      # число карты — единственное
                    'case': 'r',                                     # падеж — родительный (флеш (хх) от короля, флеш (хх) от семёрки)
                    'cas0': 'r',                                    # падеж для 0 — родительный (от дамы)
                    'pr':   "from ",                                  # приставка для 0
                    'me':   0                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            6:  {                                                   # Фулл-хаус (добавить "из", "и")
                    'i':    ["full-house of three", "", "full-houses"],
                    'r':    ["full-house of three", "", "full-houses"],
                    'd':    ["full-house of three", "", "full-houses"],
                    'v':    ["full-house of three", "", "full-houses"],
                    't':    ["full-house of three", "", "full-houses"],
                    'p':    ["full-house of three", "", "full-houses"],
                    'num':  1,                                      # число карты — множественное
                    'case': 'r',                                     # падеж — родительный (фулл-хаус из тройки королей и двойки шестёрок)
                    'cas0': 'r',                                    # падеж для 0 — родительный (из вальтов и пятёрок)
                    'pr':   "from ",                                  # приставка для 0
                    'me':   0                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            7:  {                                                   # Покер
                    'i':    ["quad of", "", "quads"],
                    'r':    ["quad of", "", "quads"],
                    'd':    ["quad of", "", "quads"],
                    'v':    ["quad of", "", "quads"],
                    't':    ["quad of", "", "quads"],
                    'p':    ["quad of", "", "quads"],
                    'num':  1,                                      # число карты — множественное
                    'case': 'r',                                     # падеж — родительный (покер из десяток)
                    'cas0': 'r',                                    # падеж для 0 — родительный (из тузов)
                    'pr':   "of ",                                  # приставка для 0
                    'me':   0                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            8:  {                                                   # Стрит-флеш ("от" перенести в масти)
                    'i':    ["straight flush", "", "straight flushes"],
                    'r':    ["straight flush", "", "straight flushes"],
                    'd':    ["straight flush", "", "straight flushes"],
                    'v':    ["straight flush", "", "straight flushes"],
                    't':    ["straight flush", "", "straight flushes"],
                    'p':    ["straight flush", "", "straight flushes"],
                    'num':  0,                                      # число карты — единственное
                    'case': 'r',                                     # падеж — родительный (стрит-флеш (хх) от короля, стрит-флеш (хх) от семёрки)
                    'cas0': 'r',                                    # падеж для 0 — родительный (от дамы)
                    'pr':   "from ",                                  # приставка для 0
                    'me':   0                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            9:  {                                                   # Роял-флеш ("от" НЕ надо, от туза он); и не сравниваем по одинаковым комбинациям, ибо ничья
                    'i':    ["flush royale"],
                    'r':    ["flush royale"],
                    'd':    ["flush royale"],
                    'v':    ["flush royale"],
                    't':    ["flush royale"],
                    'p':    ["flush royale"],
                    'num':  False,                                      # число карты — НЕТ (про туза не говорим)
                    'case': False,                                       # падежа тоже нет
                    'me':   0                                       # Сёмино местоимение — [мой, моя, мои]
                    }
            }
        value_name = {                                             # склонения значений карт по падежам и количеству
            1:  {                                                  # вот тут туза на всякий случай впишем
                    'i':    ["ace", "aces"],
                    'r':    ["ace", "aces"],
                    'd':    ["ace", "aces"],
                    'v':    ["ace", "aces"],
                    't':    ["ace", "aces"],
                    'p':    ["ace", "aces"],
                    'me':   0                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            2:  {                                                  #
                    'i':    ["deuce", "deuces"],
                    'r':    ["deuce", "deuces"],
                    'd':    ["deuce", "deuces"],
                    'v':    ["deuce", "deuces"],
                    't':    ["deuce", "deuces"],
                    'p':    ["deuce", "deuces"],
                    'me':   1                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            3:  {                                                  #
                    'i':    ["three", "threes"],
                    'r':    ["three", "threes"],
                    'd':    ["three", "threes"],
                    'v':    ["three", "threes"],
                    't':    ["three", "threes"],
                    'p':    ["three", "threes"],
                    'me':   1                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            4:  {                                                  #
                    'i':    ["four", "fours"],
                    'r':    ["four", "fours"],
                    'd':    ["four", "fours"],
                    'v':    ["four", "fours"],
                    't':    ["four", "fours"],
                    'p':    ["four", "fours"],
                    'me':   1                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            5:  {                                                  #
                    'i':    ["five", "fives"],
                    'r':    ["five", "fives"],
                    'd':    ["five", "fives"],
                    'v':    ["five", "fives"],
                    't':    ["five", "fives"],
                    'p':    ["five", "fives"],
                    'me':   1                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            6:  {                                                  #
                    'i':    ["six", "sixes"],
                    'r':    ["six", "sixes"],
                    'd':    ["six", "sixes"],
                    'v':    ["six", "sixes"],
                    't':    ["six", "sixes"],
                    'p':    ["six", "sixes"],
                    'me':   1                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            7:  {                                                  #
                    'i':    ["seven", "sevens"],
                    'r':    ["seven", "sevens"],
                    'd':    ["seven", "sevens"],
                    'v':    ["seven", "sevens"],
                    't':    ["seven", "sevens"],
                    'p':    ["seven", "sevens"],
                    'me':   1                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            8:  {                                                  #
                    'i':    ["eight", "eights"],
                    'r':    ["eight", "eights"],
                    'd':    ["eight", "eights"],
                    'v':    ["eight", "eights"],
                    't':    ["eight", "eights"],
                    'p':    ["eight", "eights"],
                    'me':   1                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            9:  {                                                  #
                    'i':    ["nine", "nines"],
                    'r':    ["nine", "nines"],
                    'd':    ["nine", "nines"],
                    'v':    ["nine", "nines"],
                    't':    ["nine", "nines"],
                    'p':    ["nine", "nines"],
                    'me':   1                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            10: {                                                  #
                    'i':    ["ten", "tens"],
                    'r':    ["ten", "tens"],
                    'd':    ["ten", "tens"],
                    'v':    ["ten", "tens"],
                    't':    ["ten", "tens"],
                    'p':    ["ten", "tens"],
                    'me':   1                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            11: {                                                  # Валет
                    'i':    ["jack", "jacks"],
                    'r':    ["jack", "jacks"],
                    'd':    ["jack", "jacks"],
                    'v':    ["jack", "jacks"],
                    't':    ["jack", "jacks"],
                    'p':    ["jack", "jacks"],
                    'me':   0                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            12: {                                                  # Дама
                    'i':    ["queen", "queens"],
                    'r':    ["queen", "queens"],
                    'd':    ["queen", "queens"],
                    'v':    ["queen", "queens"],
                    't':    ["queen", "queens"],
                    'p':    ["queen", "queens"],
                    'me':   1                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            13: {                                                  # Король
                    'i':    ["king", "kings"],
                    'r':    ["king", "kings"],
                    'd':    ["king", "kings"],
                    'v':    ["king", "kings"],
                    't':    ["king", "kings"],
                    'p':    ["king", "kings"],
                    'me':   0                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            14: {                                                  # Туз
                    'i':    ["ace", "aces"],
                    'r':    ["ace", "aces"],
                    'd':    ["ace", "aces"],
                    'v':    ["ace", "aces"],
                    't':    ["ace", "aces"],
                    'p':    ["ace", "aces"],
                    'me':   0                                       # Сёмино местоимение — [мой, моя, мои]
                    }
            }
        name_of_suit = ["Дваче","СССР","Унылок","ЮВАО"]     # масти
        combo_difference = {                                                            # разница комбинаций
            0:  {                                                                       # комбинации одинаковы
                    'm':     "almost managed to get a draw.",                          # тут первая фраза ПРОИГРАВШЕГО м
                    'f':     "almost managed to draw the game.",                       # тут первая фраза ПРОИГРАВШЕГО ж
                    'p2':    ["Although we both had our hands full of","but","and"],      # 1,3,6 части фразы
                    'cc':    "i",                                                       # падеж комбинации
                    'nc':    2                                                          # индекс в списке комбинаций
                    },
            1:  {                                                                       # разница 1..3
                    'm':     "won by a small margin.",                          # первая фраза ПОБЕДИТЕЛЯ м
                    'f':     "won by a small margin.",                         # первая фраза ПОБЕДИТЕЛЯ ж
                    'p2':    ["After all","compared to","is just a bit, but still weaker."], # 1,4,7 части фразы
                    'ccL':   "i",                                                       # падеж первой комбинации
                    'ccw':   "d"                                                        # падеж второй комбинации
                    },
            2:  {                                                                       # разница 4..6
                    'm':     "won with a significant advantage.",                  # первая фраза ПОБЕДИТЕЛЯ м
                    'f':     "won with a significant advantage.",                 # первая фраза ПОБЕДИТЕЛЯ ж
                    'p2':    ["With cards like","against","should've forfeited right there."], # 1,4,7 части фразы
                    'ccL':   "i",                                                       # падеж первой комбинации
                    'ccw':   "r"                                                        # падеж второй комбинации
                    },
            3:  {                                                                       # разница 7..9
                    'm':     "won with a smashing score, you could say 'dry'.",    # первая фраза ПОБЕДИТЕЛЯ м
                    'f':     "won with a smashing score, you could say 'dry'.",   # первая фраза ПОБЕДИТЕЛЯ ж
                    'p2':    ["Whatever you say, but","compared to","— is less than nothing."], # 1,4,7 части фразы
                    'ccL':   "i",                                                       # падеж первой комбинации
                    'ccw':   "t"                                                        # падеж второй комбинации
                    }
            }
        rivals = {                                                                  # сопернички
            'me':   ["I","I",[["my","my","my"],["my","my","my"],["my","my","my"],["my","my","my"]],"","my","my"],
            'un':   ["Lena","Lena","her","her","Lena's","her"],
            'sl':   ["Slavya","Slavya","her","her","Slavya's","her"],
            'dv':   ["Alisa","Alisa","her","her","Alisa's","her"],
            'mi':   ["Miku","Miku","her","her","Miku's","her"],
            'us':   ["Ulyana","Ulyana","her","her","Ulyanka's","her"],
            'sh':   ["Shurik","Shurik","his","his","Shurik's","his"],
            'mz':   ["Zhenya","Zhenya","her","her","Zhenya's","her"]
            }
        residual = winner_hand[0]-loser_hand[0]
        if residual == 0:
            d_combo = 0
        elif residual in [1,2]:
            d_combo = 1
        elif residual in [3,4,5]:
            d_combo = 2
        else:
            d_combo = 3
        if winner in ['me','sh']:                               # Если Семён или Шурик
            g_w = 'm'
        else:
            g_w = 'f'
        if loser in ['me','sh']:                               # Если Семён или Шурик
            g_L = 'm'
        else:
            g_L = 'f'
        if d_combo == 0:                                               # Комбинации одинаковые
            pref_1 = rivals[loser][0]
            suff_1 = combo_difference[d_combo][g_L]
        else:
            pref_1 = rivals[winner][1]
            suff_1 = combo_difference[d_combo][g_w]
        phrase_1 = " ".join([pref_1,suff_1])
        if d_combo != 0:
            if loser == 'me':                                       # проблемы только с Сёмой, с остальными проще
                m_S = name_of_combo[loser_hand[0]]['me']            # местоимение Семёна(цифра) — лезем в комбинации
                if m_S == None:                                     # если в комбинациях его не нашли
                    m_S = value_name[loser_hand[1]]['me']           # смотрим в очках карт
                phr_2_2 =  rivals[loser][2][0][m_S]                 # первое местоимение
            else:                                                   # не Семён
                phr_2_2 = rivals[loser][2]                          # местоимение одно, выбирать не нужно
            if winner == 'me':                                       # проблемы только с Сёмой, с остальными проще
                m_S = name_of_combo[winner_hand[0]]['me']            # местоимение Семёна(цифра) — лезем в комбинации
                if m_S == None:                                      # если в комбинациях его не нашли
                    m_S = value_name[winner_hand[1]]['me']           # смотрим в очках карт
                phr_2_5 =  rivals[winner][2][d_combo][m_S]           # второе местоимение
            else:
                phr_2_5 = rivals[winner][3]                          # местоимение одно, выбирать не нужно
            c_c_L = combo_difference[d_combo]['ccL']                  # падеж первой комбинации  — лузера
            c_c_w = combo_difference[d_combo]['ccw']                  # падеж второй комбинации — победителя
            c_k_L = name_of_combo[loser_hand[0]]['case']            # падеж карт комбинации лузера
            c_k_w = name_of_combo[winner_hand[0]]['case']           # падеж карт комбинации победителя
            k_k_L = name_of_combo[loser_hand[0]]['num']             # число карт комбинации лузера (0 = ед. 1 = мн.)
            k_k_w = name_of_combo[winner_hand[0]]['num']            # число карт комбинации победителя (0 = ед. 1 = мн.)
            if c_k_L == None:
                c_k_L = c_c_L
            if c_k_w == None:
                c_k_w = c_c_w
            if loser_hand[0] == 0 and loser_hand[1] not in [1,11,13,14]: # если старшая карта и НЕ туз, король, валет
                k_L = 1
            else:
                k_L = 0
            if winner_hand[0] == 0 and winner_hand[1] not in [1,11,13,14]: # если старшая карта и НЕ туз, король, валет
                k_w = 1
            else:
                k_w = 0
            if loser_hand[2] == None:                               # если масти нет
                combo_L_s = None
            else:                                                   # масть есть
                combo_L_s = name_of_suit[loser_hand[2]] + " от"        # рояла не будет по определению — читаем масть и добавляем "от"
            if winner_hand[2] == None:                              # если масти нет
                combo_w_s = None
            else:                                                   # масть есть
                if winner_hand[0] == 9:                             # если роял
                    combo_w_s = name_of_suit[winner_hand[2]]           # читаем масть
                else:
                    combo_w_s = name_of_suit[winner_hand[2]] + " от"   # читаем масть и добавляем "от"
            combo_L_c = name_of_combo[loser_hand[0]][c_c_L][k_L]
            combo_w_c = name_of_combo[winner_hand[0]][c_c_w][k_w]
            combo_L_k = value_name[loser_hand[1]][c_k_L][k_k_L]
            if winner_hand[0] != 9:                                     # Если не королевский
                combo_w_k = value_name[winner_hand[1]][c_k_w][k_k_w]
            if loser_hand[0] in [2,6]:                                                # если две пары или фулл-хаус
                combo_L_k_2 = value_name[loser_hand[3]][c_k_L][k_k_L]
            else:
                combo_L_k_2 = None
            if winner_hand[0] in [2,6]:                                                # если две пары или фулл-хаус
                combo_w_k_2 = value_name[winner_hand[3]][c_k_w][k_k_w]
            else:
                combo_w_k_2 = None
            if loser_hand[0] in [5,8]:                                          # если флеши (королевской у лезера не будет всяко)
                phr_2_3 = " ".join([combo_L_c, combo_L_s, combo_L_k])
            elif loser_hand[0] == 6:                                               # если фул-хаус
                phr_2_3 = " ".join([combo_L_c, combo_L_k, "и двух", combo_L_k_2])
            elif loser_hand[0] == 2:                                               # если две пары
                phr_2_3 = " ".join([combo_L_c, combo_L_k, "и", combo_L_k_2])
            else:
                phr_2_3 = " ".join([combo_L_c, combo_L_k])
            if winner_hand[0] == 9:                                                 # на королевском — только масти без карт
                phr_2_6 = " ".join([combo_w_c, combo_w_s])
            elif winner_hand[0] in [5,8]:                                           # если флеши
                phr_2_6 = " ".join([combo_w_c, combo_w_s, combo_w_k])
            elif winner_hand[0] == 6:                                               # если фул-хаус
                phr_2_6 = " ".join([combo_w_c, combo_w_k, "и двух", combo_w_k_2])
            elif winner_hand[0] == 2:                                               # если две пары
                phr_2_6 = " ".join([combo_w_c, combo_w_k, "и", combo_w_k_2])
            else:
                phr_2_6 = " ".join([combo_w_c, combo_w_k])
            phr_2_3 += ","
            if d_combo != 3:
                phr_2_6 += ","
            phr_2_1 = combo_difference[d_combo]['p2'][0]
            phr_2_4 = combo_difference[d_combo]['p2'][1]
            phr_2_7 = combo_difference[d_combo]['p2'][2]
            phrase_2 = " ".join([phr_2_1,phr_2_2,phr_2_3,phr_2_4,phr_2_5,phr_2_6,phr_2_7])
        else:
            phr_2_4 = rivals[winner][4] + " -"                             # Для победителя — либо имя (не Семён), либо местоимение
            phr_2_7 = rivals[loser][5] + " -"                              # Для проигравшего (7 часть) только местоимения
            c_c_0 = combo_difference[d_combo]['cc']                  # падеж комбинации
            c_n_0 = combo_difference[d_combo]['nc']                  # ссылка в список
            phr_2_2 = name_of_combo[loser_hand[0]][c_c_0][c_n_0] + ","
            c_k_w = name_of_combo[winner_hand[0]]['cas0']                   # падеж карты победителя для 0
            c_k_L = name_of_combo[loser_hand[0]]['cas0']                    # падеж карты лузера для 0
            n_k_w = name_of_combo[winner_hand[0]]['num']                    # число карты победителя для 0
            n_k_L = name_of_combo[loser_hand[0]]['num']                     # число карты лузера для 0
            p_k_w = name_of_combo[winner_hand[0]]['pr']                     # приставка карты победителя для 0
            p_k_L = name_of_combo[loser_hand[0]]['pr']                      # приставка карты лузера для 0
            if p_k_w != None:                                               # если приставка есть
                card_w = p_k_w + value_name[winner_hand[1]][c_k_w][n_k_w]   # с приставкой
            else:
                card_w = value_name[winner_hand[1]][c_k_w][n_k_w]           # без приставки (старшая карта)
            if p_k_L != None:                                               # если приставка есть
                card_L = p_k_L + value_name[loser_hand[1]][c_k_L][n_k_L]    # с приставкой
            else:
                card_L = value_name[loser_hand[1]][c_k_L][n_k_L]            # без приставки (старшая карта)
            if winner_hand[0] in [2,6]:                                     # если две пары или фулл-хаус
                phr_2_5 = card_w + " и " + value_name[winner_hand[3]][c_k_w][n_k_w]
            else:
                phr_2_5 = card_w
            if loser_hand[0] in [2,6]:                                     # если две пары или фулл-хаус
                phr_2_8 = card_L + " и " + value_name[loser_hand[3]][c_k_L][n_k_L]
            else:
                phr_2_8 = card_L
            phr_2_5 += ","                                                   #карта победителя
            phr_2_8 += "."                                                   #карта проигравшего
            phr_2_1 = combo_difference[d_combo]['p2'][0]
            phr_2_3 = combo_difference[d_combo]['p2'][1]
            phr_2_6 = combo_difference[d_combo]['p2'][2]
            phrase_2 = " ".join([phr_2_1,phr_2_2,phr_2_3,phr_2_4,phr_2_5,phr_2_6,phr_2_7,phr_2_8])
        return phrase_1, phrase_2

# ----------------------------------------------------------------------------------------
# как кто играет в карты — считаем и запоминаем.
    def alt_who_how_plays_poker():
        global alt_day2_gamblers_summary
        global alt_day2_gamblers_result
        global alt_losers_1_tour
        global alt_winners_1_tour
        global alt_losers_semifinal
        global alt_winners_semifinal
        global alt_day2_gamblers_final
        for k in alt_day2_gamblers_summary.keys():
            alt_day2_gamblers_result[k] = 0
            for m in range(0,3):
                alt_day2_gamblers_summary[k][m] = 0
        for i in range(0,4):
            alt_day2_gamblers_summary[alt_losers_1_tour[i].take][0] = 1
            alt_day2_gamblers_summary[alt_winners_1_tour[i].take][0] = 2
        for j in range(0,2):
            alt_day2_gamblers_summary[alt_losers_semifinal[j].take][1] = 1
            alt_day2_gamblers_summary[alt_winners_semifinal[j].take][1] = 2
            alt_day2_gamblers_summary[alt_day2_gamblers_final[j].take][2] = 2-j
        for x in alt_day2_gamblers_summary.keys():
            for y in range(0,3):
                if alt_day2_gamblers_summary[x][y] == 0:        # не участвовали — пропускаем
                    continue
                elif alt_day2_gamblers_summary[x][y] == 1:      # проиграли — считаем и пропускаем
                    alt_day2_gamblers_result[x] = 10*y+1
                    continue
                elif alt_day2_gamblers_summary[x][y] == 2:      # выиграли — считаем
                    alt_day2_gamblers_result[x] = 10*y+2
        return





# =====================================================================================================================================================
#                                                        ПОКАЗЫВАЕМ ТУРНИРНУЮ ТАБЛИЦУ
# =====================================================================================================================================================
label show_tournament_table:                                                                                        # сюда ныряем из турнира
    if alt_tournament_state == "1_round_start":                                                                     # если начало 1-го раунда
        $ alt_show_tournament_table_1_round(alt_day2_gamblers_1_tour)                                               # вызываем турнирную таблицу — там показывается очередная фишка
    elif alt_tournament_state == "1_round_end":
        $ alt_show_tournament_table_semifinal(alt_day2_gamblers_1_tour)
    elif alt_tournament_state == "semifinal_start":
        $ alt_show_tournament_table_semifinal(alt_day2_gamblers_1_tour,alt_day2_gamblers_semifinal)
    elif alt_tournament_state == "semifinal_end":
        $ alt_show_tournament_table_final(alt_day2_gamblers_semifinal)
    elif alt_tournament_state in ["final_start","final_end"]:
        $ alt_show_tournament_table_win(alt_day2_gamblers_1_tour, alt_day2_gamblers_semifinal,alt_day2_gamblers_final)
    return
