label alt_day4_un_fz_start_new:
    call alt_day4_un_fz_vars
    $ alt_save_name(4, u"Лена. ФЗ. Cон")
    $ persistent.sprite_time = "night"
    $ night_time()
    if alt_day3_un_fz_walk:
        call alt_day4_un_fz_dream_un
    elif alt_day3_un_fz_stories:
        call alt_day4_un_fz_dream_road
    $ alt_chapter(4, u"Лена. ФЗ. Утро")
    $ alt_pause(.1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    call alt_day4_un_fz_morning
    $ alt_pause(1)
    $ alt_save_name(4, u"Лена. ФЗ. Медпункт")
    call alt_day4_un_fz_aidpost
    $ alt_pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    if alt_day4_un_fz_morning_event == 'un':
        $ alt_save_name(4, u"Лена. ФЗ. Стенгазета")
        call alt_day4_un_fz_un_nwsppr
    elif alt_day4_un_fz_morning_event == 'mt':
        $ alt_save_name(4, u"Лена. ФЗ. Помощник вожатой")
        call alt_day4_un_fz_mt_help
    elif alt_day4_un_fz_morning_event == 'dv':
        $ alt_save_name(4, u"Лена. ФЗ. Побег с Алисой")
        call alt_day4_un_fz_dv_escape
        if (counter_un_fz_dv_fake_date != 2):
            $ alt_pause(1)
            $ alt_save_name(4, u"Лена. ФЗ. Заблудший.")
            call alt_day4_un_fz_old_road
    $ alt_pause(1)
    $ alt_chapter(4, u"Лена. ФЗ. Обед")
    if alt_day4_un_fz_morning_event == 'un':
        call alt_day4_un_fz_lunch_nwsppr
    elif alt_day4_un_fz_morning_event == 'mt':
        call alt_day4_un_fz_lunch_boat
    else:
        call alt_day4_un_fz_lunch_forest
    $ alt_pause(1)
    $ alt_save_name(4, u"Лена. ФЗ. Тихий час")
    call alt_day4_un_fz_siesta
    $ alt_pause(1)
    $ alt_save_name(4, u"Лена. ФЗ. Полдник")
    call alt_day4_un_fz_afternoon
    $ alt_pause(1)
    $ alt_save_name(4, u"Лена. ФЗ. Песчаная коса")
    call alt_day4_un_fz_un_date
    $ alt_pause(1)
    $ alt_chapter(4, u"Лена. ФЗ. Ужин")
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    call alt_day4_un_fz_dinner
    $ alt_pause(1)
    if alt_day4_un_fz_us_run:
        call alt_day4_un_fz_run
    else:
        call alt_day4_un_fz_debriefing
    $ alt_pause(1)
    $ alt_chapter(4, u"Лена. ФЗ. Вечерние события")
    call alt_day4_un_fz_evening
    $ alt_pause(1)
    if (counter_un_fz_mt_transit == 3):
        call alt_day4_un_fz_mt_house
        call alt_day4_me_neu_mt_diary_vol1
        $ alt_pause(1)
        $ routetag = "neu"
        jump alt_day5_me_neu_start
    else:
        call alt_day4_un_fz_portwine
        $ alt_pause(1)
        $ persistent.sprite_time = "night"
        $ night_time()
        $ alt_save_name(4, u"Лена. ФЗ. «Чаепитие»")
        call alt_day4_un_fz_tea_party
        $ alt_pause(1)
        call alt_day4_un_fz_afterparty
        $ alt_pause(1)
        $ alt_save_name(4, u"Лена. ФЗ. Отбой")
        call alt_day4_un_fz_sleeptime
        $ alt_pause(1)
        jump alt_day5_un_fz_begin
    return

label alt_day5_un_fz_begin:
    call alt_day5_un_fz_vars
    $ alt_pause(2)
    call alt_day5_un_fz_dream
    $ alt_pause(3)
    $ alt_chapter(5, u"Лена. ФЗ. Утро")
    call alt_day5_un_fz_morning
    $ alt_pause(1)
    $ alt_save_name(5, u"Лена. ФЗ. Завтрак")
    call alt_day5_un_fz_breakfast
    $ alt_pause(1)
    $ alt_save_name(5, u"Лена. ФЗ. Свечка")
    call alt_day5_un_fz_cndl
    $ alt_pause(1)
    if (counter_un_fz_dv_fake_date == 3):
        call alt_day5_un_fz_dream2_dv
    else:
        if alt_day4_un_fz_un_evening == 'sleep':
            call alt_day5_un_fz_dream2_un
        else:
            call alt_day5_un_fz_dream2_road
    $ alt_pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(5, u"Лена. ФЗ. Обед")
    call alt_day5_un_fz_lunch
    $ alt_pause(1)
    $ alt_save_name(5, u"Лена. ФЗ. Золушка")
    call alt_day5_un_fz_beach_work
    $ alt_pause(1)
    $ alt_save_name(5, u"Лена. ФЗ. Полдник")
    call alt_day5_un_fz_afternoon
    $ alt_pause(1)
    if alt_day5_un_fz_old_camp:
        $ alt_save_name(5, u"Лена. ФЗ. Старый лагерь")
        call alt_day5_un_fz_old_camp
    else:
        $ alt_save_name(5, u"Лена. ФЗ. Костровая поляна")
        call alt_day5_un_fz_bonfire_glade
    $ alt_pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Лена. ФЗ. Ужин")
    call alt_day5_un_fz_dinner
    $ alt_pause(1)
    call alt_day5_un_fz_mission
    $ alt_pause(1)
    $ alt_save_name(5, u"Лена. ФЗ. Костёр")
    call alt_day5_un_fz_evening
    $ alt_pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    call alt_day5_un_fz_campfire
    $ alt_pause(1)
    $ alt_save_name(5, u"Лена. ФЗ. Поиски")
    call alt_day5_un_fz_search
    $ alt_pause(1)
    if (counter_un_fz_old_road >= 7):
        call alt_day5_un_fz_rr
        $ alt_pause(1)
        $ alt_save_name(5, u"Лена. ФЗ. Отбой")
        call alt_day5_un_fz_rr_sleeptime
        jump alt_day6_un_fz_rr_begin
    else:
        call alt_day5_un_fz_fzr
        $ alt_pause(1)
        $ alt_save_name(5, u"Лена. ФЗ. Отбой")
        call alt_day5_un_fz_fzr_sleeptime
        jump alt_day6_un_fz_begin
    $ alt_pause(1)
    return

label alt_day6_un_fz_begin:
    call alt_day6_un_fz_vars
    $ alt_pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Лена. ФЗ. Пробуждение")
    call alt_day6_un_fz_morning
    $ alt_pause(1)
    $ alt_save_name(6, u"Лена. ФЗ. Линейка")
    call alt_day6_un_fz_lineup
    $ alt_pause(1)
    $ alt_chapter(6, u"Лена. ФЗ. Завтрак")
    call alt_day6_un_fz_breakfast
    $ alt_pause(1)
    call alt_day6_un_fz_map_morning
    $ alt_pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(6, u"Лена. ФЗ. Обед")
    call alt_day6_un_fz_lunch
    $ alt_pause(1)
    $ alt_save_name(6, u"Лена. ФЗ. Помощь Славе")
    call alt_day6_un_fz_sl_help
    $ alt_pause(1)
    $ alt_save_name(6, u"Лена. ФЗ. Полдник")
    call alt_day6_un_fz_afternoon
    $ alt_pause(1)
    $ alt_save_name(6, u"Лена. ФЗ. Концерт")
    call alt_day6_un_fz_concert
    $ alt_pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Лена. ФЗ. Ужин")
    if counter_un_fz_dv_fake_date == 3:
        call alt_day6_un_fz_dv_dinner
        $ alt_pause(1)
        $ persistent.sprite_time = "night"
        $ night_time()
        $ alt_chapter(6, u"Лена. ФЗ. Вечер с Алисой.")
        call alt_day6_un_fz_dv_date
        $ alt_pause(1)
        $ alt_chapter(6, u"Лена. ФЗ. Поиски Лены.")
        call alt_day6_un_fz_dv_un_search
        $ alt_pause(1)
        $ alt_chapter(6, u"Лена. ФЗ. Кошмар наяву.")
        call alt_day6_un_fz_dv_un_night
        $ alt_pause(2)
    elif counter_un_fz_un_route >= 7:
        call alt_day6_un_fz_good_dinner
        $ alt_pause(1)
        $ alt_chapter(6, u"Лена. ФЗ. Точки над «Ё».")
        call alt_day6_un_fz_good_un_evening
        $ alt_pause(1)
        $ persistent.sprite_time = "night"
        $ night_time()
        $ alt_chapter(6, u"Лена. ФЗ. Танцы.")
        if (alt_un_fz_ends == "n_end"):
            call alt_day6_un_fz_dance1
            $ alt_chapter(6, u"Лена. ФЗ. Отбой.")
            call alt_day6_un_fz_sleeptime1
        else:
            call alt_day6_un_fz_dance2
            $ alt_pause(2)
            $ alt_chapter(6, u"Лена. ФЗ. Прогулка.")
            call alt_day6_un_fz_night_walk
            $ alt_pause(1)
            $ alt_chapter(6, u"Лена. ФЗ. Отбой.")
            call alt_day6_un_fz_sleeptime2
    else:
        call alt_day6_un_fz_bad_neu_dinner
        $ alt_pause(1)
        $ persistent.sprite_time = "night"
        $ night_time()
        $ alt_save_name(6, u"Лена. ФЗ. На поиски.")
        call alt_day6_un_fz_un_search
        $ alt_pause(1)
        $ alt_save_name(6, u"Лена. ФЗ. Отбой.")
        if alt_un_fz_ends == "n_end":
            call alt_day6_un_fz_neu_sleeptime
        elif  alt_un_fz_ends == "b_end":
            call alt_day6_un_fz_neu_bad_sleeptime
            $ alt_pause(1)
            $ alt_save_name(6, u"Лена. ФЗ. На границе чистилища.")
            call alt_day6_un_fz_night_in_hell
    jump alt_day7_un_fz_begin
    return

label alt_day6_un_fz_rr_begin:
    if alt_day5_un_fz_old_camp:
        if (counter_un_fz_dream_road == 3):
            pass
        else:
            $ routetag = "un7dlbad"
    else:
        $ routetag = "un7dlgood"
    $ alt_pause(2)
    $ alt_chapter(6, u"Лена. ФЗ. Утро")
    call alt_day6_un_fz_rr_dream
    $ alt_pause(2)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    call alt_day6_un_fz_rr_morning
    $ alt_pause(1)
    call alt_day6_un_fz_rr_lineup
    $ alt_pause(1)
    $ alt_save_name(6, u"Лена. ФЗ. Завтрак")
    call alt_day6_un_fz_rr_breakfast
    $ alt_pause(1)
    $ alt_save_name(6, u"Лена. ФЗ. На поиски")
    call alt_day6_un_fz_rr_search
    if alt_day5_un_fz_old_camp:
        call alt_day6_un_fz_rr_search2
    else:
        call alt_day6_un_fz_rr_search3
    $ alt_pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(6, u"Лена. ФЗ. Обед")
    call alt_day6_un_fz_rr_lunch
    $ alt_pause(1)
    $ alt_save_name(6, u"Лена. ФЗ. Спасение Гвардии")
    call alt_day6_un_fz_rr_guard_resque
    $ alt_pause(1)
    $ alt_save_name(6, u"Лена. ФЗ. Старая Дорога")
    call alt_day6_un_fz_rr_old_road
    $ alt_pause(1)
    $ alt_chapter(6, u"Лена. ФЗ. Иной мир")
    call alt_day6_un_fz_rr_another_world
    $ alt_pause(1)
    if alt_day5_un_fz_old_camp:
        if (counter_un_fz_dream_road == 3):
            call alt_day6_un_fz_rr_farewell
            $ alt_pause(1)
            call alt_day6_un_fz_rr_true
        else:
            call alt_day6_un_fz_rr_farewell
            $ alt_pause(1)
            call alt_day6_un_fz_rr_bad
    else:
        call alt_day6_un_fz_rr_good
    return

label alt_day7_un_fz_begin:
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_pause(1)
    if (alt_un_fz_ends == "b_end") or (counter_un_fz_dv_fake_date == 3):
        $ routetag = "un7dlbad"
        $ alt_chapter(7, u"Лена. ФЗ. Ад.")
        call alt_day7_un_fz_bad_morning
        $ alt_pause(1)
        $ alt_save_name(7, u"Лена. ФЗ. Ад. В поисках Ольги.")
        call  alt_day7_un_fz_bad_mt_search
        $ alt_pause(1)
        $ alt_chapter(7, u"Лена. ФЗ. Ад. Отбытие.")
        call alt_day7_un_fz_bad_departure
        $ alt_pause(2)
        $ alt_save_name(7, u"Лена. ФЗ. В бездну.")
        call alt_day7_un_fz_bad_end
        $ alt_pause(1)
        if (counter_un_fz_dv_fake_date == 3):
            $ alt_save_name(7, u"Лена. ФЗ. Навстречу неизвестному.")
            $ persistent.sprite_time = "night"
            call alt_day7_un_fz_bad_end_postscriptum
    elif alt_un_fz_ends == "g_end":
        $ routetag = "un7dlgood"
        $ alt_chapter(7, u"Лена. ФЗ. Утро.")
        call alt_day7_un_fz_good_morning
        $ alt_pause(1.5)
        $ alt_save_name(7, u"Лена. ФЗ. Завтрак.")
        call alt_day7_un_fz_good_breakfast
        $ alt_pause(1)
        $ alt_save_name(7, u"Лена. ФЗ. Прощание.")
        call alt_day7_un_fz_good_farewell
        $ alt_pause(1.5)
        $ alt_chapter(7, u"Лена. ФЗ. Отбытие.")
        call alt_day7_un_fz_good_departure
        $ alt_pause(1)
        $ alt_save_name(7, u"Лена. ФЗ. Пока я буду нужен.")
        call alt_day7_un_fz_good_end
    else:
        $ alt_chapter(7, u"Лена. ФЗ. Утро.")
        call alt_day7_un_fz_neu_morning
        $ alt_pause(1.5)
        $ alt_save_name(7, u"Лена. ФЗ. Завтрак.")
        call alt_day7_un_fz_neu_breakfast
        $ alt_pause(1)
        $ alt_save_name(7, u"Лена. ФЗ. Прощание с лагерем.")
        call alt_day7_un_fz_neu_camp_farewell
        $ alt_pause(1)
        $ alt_chapter(7, u"Лена. ФЗ. Отбытие.")
        call alt_day7_un_fz_neu_departure
        $ alt_pause(2.5)
        $ prolog_time()
        if ((counter_un_fz_old_road >= 5) and (alt_un_fz_ends == "n_end")):
            $ alt_save_name(7, u"Лена. ФЗ. Ад в моей голове.")
            call alt_day7_un_fz_rj_end
        elif (alt_un_fz_ends == "n_end"):
            $ alt_save_name(7, u"Лена. ФЗ. День сурка.")
            call alt_day7_un_fz_neu_end
    return