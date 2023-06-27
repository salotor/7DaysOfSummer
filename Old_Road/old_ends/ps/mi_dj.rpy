label alt_day7_mi_dj_good_rf_ps_old:
    play music music_7dl["unfinished_life"] fadein 3
    scene
    $ renpy.show("bg int_semen_room_clean_7dl", what = Noir("bg int_semen_room_clean_7dl", brightness = 0.1, tint_r = 0.2, tint_g = 0.9, tint_b = 0.7, saturation = 0.7))
    with touch
    "Так всё оно и будет однажды."
    "Я верю в это."
    "До такой степени верю, что вижу сны, подробные, цветные и с объёмным звуком."
    "Те самые, после которых долго-долго ноет что-то в душе."
    "А я не люблю боль. {w}Никто не любит."
    scene
    $ renpy.show("bg semen_room_window", what = Noir("bg semen_room_window", brightness = 0.1, tint_r = 0.2, tint_g = 0.9, tint_b = 0.7, saturation = 0.7))
    with diam
    "Лучше я закрою глаза ещё раз и детально восстановлю в памяти мою сладкую грёзу."
    "Ту самую, в которой мне звонят на телефон, а потом и в дверь."
    "Дверной глазок явит мне лестничную площадку, но если смотреть чуть ниже…"
    "Там можно будет разглядеть её."
    "Полтора метра жизнерадостности, счастья и шикарных волос, в которые так здорово зарываться носом."
    "Я обновил страничку с гастрольным графиком Хацунэ Мику — в этом году её зазвали в Лос-Анджелес и Париж. {w}Может, в следующем году и к нам заглянет?"
    "Больше чем уверен: на её концерте будет аншлаг."
    "А потом, после концерта, одна очень красивая девочка вытащит из кармана старый, истрёпанный листок, на котором синим химическим карандашом написан адрес."
    "Подзовёт кэб, один из которых всегда есть около Ледового Дворца, покажет бумажку и прикажет трогаться."
    scene
    $ renpy.show("bg int_staircase_7dl", what = Noir("bg int_staircase_7dl", brightness = 0.2, tint_r = 0.2, tint_g = 1.0, tint_b = 1.0, saturation = 0.7))
    show prologue_dream
    with dissolve
    if herc:
        "Улыбнётся консьержке: «К Сычёву, седьмой этаж»."
    else:
        "Консьержке: «Здравствуйте, я к Персунову»."
    "И минутой позже выйдет на моей лестничной площадке."
    "Моя дверь — первая слева от лифта."
    "Она уточнит ещё раз номер квартиры, найдёт звонок и…"
    "После пяти лет ожидания, год-два уже совсем не имеют значения…"
    scene
    $ renpy.show("bg int_staircase_7dl", what = Noir("bg int_staircase_7dl", brightness = 0.1, tint_r = 0.2, tint_g = 0.9, tint_b = 0.7, saturation = 0.7))
    show mi sad voca
    show prologue_dream
    with dissolve
    stop music fadeout 3
    "И однажды…"
    scene black
    with joff_l
    pause(3)
    if not persistent.pivo_default_7dl:
        jump alt_stories_start
    else:
        return