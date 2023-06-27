label alt_day4_un_fz_start_new:
    call alt_day4_un_fz_vars
    $ alt_save_name(4, u"Lena. FZ. Dream")
    $ persistent.sprite_time = "night"
    $ night_time()
    if alt_day3_un_fz_walk:
        call alt_day4_un_fz_dream_un
    elif alt_day3_un_fz_stories:
        call alt_day4_un_fz_dream_road
    $ alt_chapter(4, u"Lena. FZ. Morning")
    $ alt_pause(.1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    call alt_day4_un_fz_morning
    $ alt_pause(1)
    $ alt_save_name(4, u"Lena. FZ. Infirmary")
    call alt_day4_un_fz_aidpost
    $ alt_pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    if alt_day4_un_fz_morning_event == 'un':
        $ alt_save_name(4, u"Lena. FZ. Newspaper")
        call alt_day4_un_fz_un_nwsppr
    elif alt_day4_un_fz_morning_event == 'mt':
        $ alt_save_name(4, u"Lena. FZ. Helping squad leader")
        call alt_day4_un_fz_mt_help
    elif alt_day4_un_fz_morning_event == 'dv':
        $ alt_save_name(4, u"Lena. FZ. Escape with Alisa")
        call alt_day4_un_fz_dv_escape
        if (counter_un_fz_dv_fake_date != 2):
            $ alt_pause(1)
            $ alt_save_name(4, u"Lena. FZ. Lost.")
            call alt_day4_un_fz_old_road
    $ alt_pause(1)
    $ alt_chapter(4, u"Lena. FZ. Dinner")
    if alt_day4_un_fz_morning_event == 'un':
        call alt_day4_un_fz_lunch_nwsppr
    elif alt_day4_un_fz_morning_event == 'mt':
        call alt_day4_un_fz_lunch_boat
    else:
        call alt_day4_un_fz_lunch_forest
    $ alt_pause(1)
    $ alt_save_name(4, u"Lena. FZ. Quiet hour")
    call alt_day4_un_fz_siesta
    $ alt_pause(1)
    $ alt_save_name(4, u"Lena. FZ. Afternoon")
    call alt_day4_un_fz_afternoon
    $ alt_pause(1)
    $ alt_save_name(4, u"Lena. FZ. Beach")
    call alt_day4_un_fz_un_date
    $ alt_pause(1)
    $ alt_chapter(4, u"Lena. FZ. Supper")
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    call alt_day4_un_fz_dinner
    $ alt_pause(1)
    if alt_day4_un_fz_us_run:
        call alt_day4_un_fz_run
    else:
        call alt_day4_un_fz_debriefing
    $ alt_pause(1)
    $ alt_chapter(4, u"Lena. FZ. Evening events")
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
        $ alt_save_name(4, u"Lena. FZ. «Tea party»")
        call alt_day4_un_fz_tea_party
        $ alt_pause(1)
        call alt_day4_un_fz_afterparty
        $ alt_pause(1)
        $ alt_save_name(4, u"Lena. FZ. Lights out")
        call alt_day4_un_fz_sleeptime
        $ alt_pause(1)
        jump alt_day5_un_fz_begin
    return

label alt_day5_un_fz_begin:
    call alt_day5_un_fz_vars
    $ alt_pause(2)
    call alt_day5_un_fz_dream
    $ alt_pause(3)
    $ alt_chapter(5, u"Lena. FZ. Morning")
    call alt_day5_un_fz_morning
    $ alt_pause(1)
    $ alt_save_name(5, u"Lena. FZ. Breakfast")
    call alt_day5_un_fz_breakfast
    $ alt_pause(1)
    $ alt_save_name(5, u"Lena. FZ. Candle")
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
    $ alt_chapter(5, u"Lena. FZ. Dinner")
    call alt_day5_un_fz_lunch
    $ alt_pause(1)
    $ alt_save_name(5, u"Lena. FZ. Cinderella")
    call alt_day5_un_fz_beach_work
    $ alt_pause(1)
    $ alt_save_name(5, u"Lena. FZ. Lunch")
    call alt_day5_un_fz_afternoon
    $ alt_pause(1)
    if alt_day5_un_fz_old_camp:
        $ alt_save_name(5, u"Lena. FZ. Old camp")
        call alt_day5_un_fz_old_camp
    else:
        $ alt_save_name(5, u"Lena. FZ. Campfire glade")
        call alt_day5_un_fz_bonfire_glade
    $ alt_pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Lena. FZ. Supper")
    call alt_day5_un_fz_dinner
    $ alt_pause(1)
    call alt_day5_un_fz_mission
    $ alt_pause(1)
    $ alt_save_name(5, u"Lena. FZ. Campfire")
    call alt_day5_un_fz_evening
    $ alt_pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    call alt_day5_un_fz_campfire
    $ alt_pause(1)
    $ alt_save_name(5, u"Lena. FZ. Search")
    call alt_day5_un_fz_search
    $ alt_pause(1)
    if (counter_un_fz_old_road >= 7):
        call alt_day5_un_fz_rr
        $ alt_pause(1)
        $ alt_save_name(5, u"Lena. FZ. Lights out")
        call alt_day5_un_fz_rr_sleeptime
        jump alt_day6_un_fz_rr_begin
    else:
        call alt_day5_un_fz_fzr
        $ alt_pause(1)
        $ alt_save_name(5, u"Lena. FZ. Lights out")
        call alt_day5_un_fz_fzr_sleeptime
        jump alt_day6_un_fz_begin
    $ alt_pause(1)
    return

label alt_day6_un_fz_begin:
    call alt_day6_un_fz_vars
    $ alt_pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Lena. FZ. Awakening")
    call alt_day6_un_fz_morning
    $ alt_pause(1)
    $ alt_save_name(6, u"Lena. FZ. Lineup")
    call alt_day6_un_fz_lineup
    $ alt_pause(1)
    $ alt_chapter(6, u"Lena. FZ. Breakfast")
    call alt_day6_un_fz_breakfast
    $ alt_pause(1)
    call alt_day6_un_fz_map_morning
    $ alt_pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(6, u"Lena. FZ. Dinner")
    call alt_day6_un_fz_lunch
    $ alt_pause(1)
    $ alt_save_name(6, u"Lena. FZ. Helping Slavya")
    call alt_day6_un_fz_sl_help
    $ alt_pause(1)
    $ alt_save_name(6, u"Lena. FZ. Afternoon")
    call alt_day6_un_fz_afternoon
    $ alt_pause(1)
    $ alt_save_name(6, u"Lena. FZ. Concert")
    call alt_day6_un_fz_concert
    $ alt_pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Lena. FZ. Supper")
    if counter_un_fz_dv_fake_date == 3:
        call alt_day6_un_fz_dv_dinner
        $ alt_pause(1)
        $ persistent.sprite_time = "night"
        $ night_time()
        $ alt_chapter(6, u"Lena. FZ. Evening with Alisa.")
        call alt_day6_un_fz_dv_date
        $ alt_pause(1)
        $ alt_chapter(6, u"Lena. FZ. Searching for Lena.")
        call alt_day6_un_fz_dv_un_search
        $ alt_pause(1)
        $ alt_chapter(6, u"Lena. FZ. Nightmare unfolding.")
        call alt_day6_un_fz_dv_un_night
        $ alt_pause(2)
    elif counter_un_fz_un_route >= 7:
        call alt_day6_un_fz_good_dinner
        $ alt_pause(1)
        $ alt_chapter(6, u"Lena. FZ. Dots over «i».")
        call alt_day6_un_fz_good_un_evening
        $ alt_pause(1)
        $ persistent.sprite_time = "night"
        $ night_time()
        $ alt_chapter(6, u"Lena. FZ. Disco.")
        if (alt_un_fz_ends == "n_end"):
            call alt_day6_un_fz_dance1
            $ alt_chapter(6, u"Lena. FZ. Lights out.")
            call alt_day6_un_fz_sleeptime1
        else:
            call alt_day6_un_fz_dance2
            $ alt_pause(2)
            $ alt_chapter(6, u"Lena. FZ. Walk.")
            call alt_day6_un_fz_night_walk
            $ alt_pause(1)
            $ alt_chapter(6, u"Lena. FZ. Lights out.")
            call alt_day6_un_fz_sleeptime2
    else:
        call alt_day6_un_fz_bad_neu_dinner
        $ alt_pause(1)
        $ persistent.sprite_time = "night"
        $ night_time()
        $ alt_save_name(6, u"Lena. FZ. Search.")
        call alt_day6_un_fz_un_search
        $ alt_pause(1)
        $ alt_save_name(6, u"Lena. FZ. Lights out.")
        if alt_un_fz_ends == "n_end":
            call alt_day6_un_fz_neu_sleeptime
        elif  alt_un_fz_ends == "b_end":
            call alt_day6_un_fz_neu_bad_sleeptime
            $ alt_pause(1)
            $ alt_save_name(6, u"Lena. FZ. At the Hell's Gate.")
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
    $ alt_chapter(6, u"Lena. FZ. Morning")
    call alt_day6_un_fz_rr_dream
    $ alt_pause(2)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    call alt_day6_un_fz_rr_morning
    $ alt_pause(1)
    call alt_day6_un_fz_rr_lineup
    $ alt_pause(1)
    $ alt_save_name(6, u"Lena. FZ. Breakfast")
    call alt_day6_un_fz_rr_breakfast
    $ alt_pause(1)
    $ alt_save_name(6, u"Lena. FZ. Search")
    call alt_day6_un_fz_rr_search
    if alt_day5_un_fz_old_camp:
        call alt_day6_un_fz_rr_search2
    else:
        call alt_day6_un_fz_rr_search3
    $ alt_pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(6, u"Lena. FZ. Dinner")
    call alt_day6_un_fz_rr_lunch
    $ alt_pause(1)
    $ alt_save_name(6, u"Lena. FZ. Saving Guardsmen")
    call alt_day6_un_fz_rr_guard_resque
    $ alt_pause(1)
    $ alt_save_name(6, u"Lena. FZ. The Old Road")
    call alt_day6_un_fz_rr_old_road
    $ alt_pause(1)
    $ alt_chapter(6, u"Lena. FZ. Another world")
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
        $ alt_chapter(7, u"Lena. FZ. Hell.")
        call alt_day7_un_fz_bad_morning
        $ alt_pause(1)
        $ alt_save_name(7, u"Lena. FZ. Hell. Searching for Olga.")
        call  alt_day7_un_fz_bad_mt_search
        $ alt_pause(1)
        $ alt_chapter(7, u"Lena. FZ. Hell. Departure.")
        call alt_day7_un_fz_bad_departure
        $ alt_pause(2)
        $ alt_save_name(7, u"Lena. FZ. Into the void.")
        call alt_day7_un_fz_bad_end
        $ alt_pause(1)
        if (counter_un_fz_dv_fake_date == 3):
            $ alt_save_name(7, u"Lena. FZ. Into the unknown.")
            $ persistent.sprite_time = "night"
            call alt_day7_un_fz_bad_end_postscriptum
    elif alt_un_fz_ends == "g_end":
        $ routetag = "un7dlgood"
        $ alt_chapter(7, u"Lena. FZ. Morning.")
        call alt_day7_un_fz_good_morning
        $ alt_pause(1.5)
        $ alt_save_name(7, u"Lena. FZ. Breakfast.")
        call alt_day7_un_fz_good_breakfast
        $ alt_pause(1)
        $ alt_save_name(7, u"Lena. FZ. Farewells.")
        call alt_day7_un_fz_good_farewell
        $ alt_pause(1.5)
        $ alt_chapter(7, u"Lena. FZ. Departure.")
        call alt_day7_un_fz_good_departure
        $ alt_pause(1)
        $ alt_save_name(7, u"Lena. FZ. As Long as I am Needed.")
        call alt_day7_un_fz_good_end
    else:
        $ alt_chapter(7, u"Lena. FZ. Morning.")
        call alt_day7_un_fz_neu_morning
        $ alt_pause(1.5)
        $ alt_save_name(7, u"Lena. FZ. Breakfast.")
        call alt_day7_un_fz_neu_breakfast
        $ alt_pause(1)
        $ alt_save_name(7, u"Lena. FZ. Farewells.")
        call alt_day7_un_fz_neu_camp_farewell
        $ alt_pause(1)
        $ alt_chapter(7, u"Lena. FZ. Departure.")
        call alt_day7_un_fz_neu_departure
        $ alt_pause(2.5)
        $ prolog_time()
        if ((counter_un_fz_old_road >= 5) and (alt_un_fz_ends == "n_end")):
            $ alt_save_name(7, u"Lena. FZ. ...")
            call alt_day7_un_fz_rj_end
        elif (alt_un_fz_ends == "n_end"):
            $ alt_save_name(7, u"Lena. FZ. Groundhog Day.")
            call alt_day7_un_fz_neu_end
    return