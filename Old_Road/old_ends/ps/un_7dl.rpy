label alt_day7_un_7dl_good_rf_ps_old:
    $ prolog_time()
    play music music_7dl["sh_ai_rejuv"] fadein 3
    scene
    $ renpy.show("bg ext_city_night_7dl", what = Noir("bg ext_city_night_7dl", brightness = 0.1, tint_r = 0.2, tint_g = 0.9, tint_b = 0.7, saturation = 0.7))
    with joff_l
    "Существует множество разных кризисов — веры, творчества, возраста."
    "Мой кризис в том, что книги врут. {w}Соплежуи с умными мордами врут!"
    "Какого дьявола?!"
    "Они сказали, что надо просто сделать всё возможное, приложить усилия — и мечта будет достижима!!!"
    "Не было таких усилий, какие я бы не прикладывал!"
    scene
    $ renpy.show("bg ext_city_night_7dl", what = Noir("bg ext_city_night_7dl", brightness = 0.2, tint_r = 0.3, tint_g = 0.8, tint_b = 0.7, saturation = 0.6))
    with blind_l
    "В «комодо» восемь вкладок, которые я обновляю, не чувствуя интереса к их содержимому."
    "Я живу по инерции."
    "Я почти слышу, как лопается сердце перед фактом того, сколько мне ещё осталось."
    "Слишком много. {w}Подавляюще много — годы и годы."
    scene
    $ renpy.show("bg int_home_lift_7dl", what = Noir("bg int_home_lift_7dl", brightness = 0.1, tint_r = 0.2, tint_g = 0.9, tint_b = 0.7, saturation = 0.7))
    with diam
    "Читатель, тебе весело или грустно? {w}Ты влюблён или равнодушен?"
    "Ты вообще {i}хоть что-нибудь{/i} чувствуешь?"
    "Я — нет."
    "Если встать на стул, то можно снять люстру, которую повесили туда ещё старые владельцы квартиры."
    "Там крюк, рассчитанный на сто килограмм веса."
    "Однажды я проверю его на прочность."
    scene
    $ renpy.show("bg semen_room_window", what = Noir("bg semen_room_window", brightness = 0.2, tint_r = 0.2, tint_g = 1.0, tint_b = 1.0, saturation = 0.7))
    with dissolve
    "Когда перестанет пробирать музыка."
    "И отсверки фар выхватят из темноты силуэт моего безжизненного одиночества."
    "Когда больные глаза перестанут ловить фокус."
    with flash
    "Когда перестанет спасать даже моё самое последнее средство."
    scene
    $ renpy.show("bg int_sam_house_clean_7dl", what = Noir("bg int_sam_house_clean_7dl", brightness = 0.2, tint_r = 0.2, tint_g = 1.0, tint_b = 1.0, saturation = 0.7))
    with dissolve
    "Я пришёл в себя, сидя на продавленном кресле напротив монитора."
    "Жутко болела голова, запрокинутая последние несколько часов, затекла шея."
    "Очень хотелось пить, но сил подняться не было."
    "На полу рядом с креслом валялся грязный жгут с сигаретными пропалинами по краю."
    "Привычно болело место укола."
    with blind_l
    "И в жгучей белизне таяло прощальное:"
    scene cg d7_un_epilogue_bad2_7dl
    show prologue_dream
    with dissolve2
    stop music fadeout 10
    show alt_letter "Спасибо…" at truecenter with zoomin
    pause(8)
    jump alt_stories_start