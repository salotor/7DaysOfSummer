label alt_day4_dv_dj_start:
    call alt_day4_dv_dj_vars
    $ routetag = "dvdj"
    $ alt_pause(.1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Alisa. DJ. Morning")
    call alt_day4_dv_dj_morning
    $ alt_pause(1)
    $ alt_save_name(4, u"Alisa. DJ. Breakfast")
    call alt_day4_dv_dj_breakfast
    $ alt_pause(1)
    $ alt_chapter(4, u"Alisa. DJ. Freedom to readhead!")
    call alt_day4_dv_dj_alise_free
    $ alt_pause(1)
    $ alt_chapter(4, u"Alisa. DJ. Red hurricane")
    call alt_day4_dv_dj_radio_event
    $ alt_pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_save_name(4, u"Alisa. DJ. Dinner")
    call alt_day4_dv_dj_lunch
    $ alt_pause(1)
    $ alt_chapter(4, u"Alisa. DJ. Quiet hour")
    call alt_day4_dv_dj_silent_hour
    $ alt_pause(1)
    $ alt_save_name(4, u"Alisa. DJ. Lunch")
    call alt_day4_dv_dj_afternoon
    $ alt_pause(1)
    $ alt_save_name(4, u"Alisa. DJ. Concert")
    call alt_day4_dv_dj_concert
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_save_name(4, u"Alisa. DJ. Evening")
    call alt_day4_dv_dj_dinner
    $ alt_pause(1)
    $ alt_chapter(4, u"Alisa. DJ. Searching for Ulyana")
    call alt_day4_dv_dj_us_search
    $ alt_pause(1)
    $ persistent.sprite_time = 'night'
    $ night_time()
    $ alt_save_name(4, u"Alisa. DJ. Beach date")
    call alt_day4_dv_dj_date_on_the_beach
    $ alt_pause(1)
    $ alt_save_name(4, u"Alisa. DJ. Lights out")
    call alt_day4_dv_dj_sleeptime
    $ alt_pause(1)
    jump alt_day5_dv_dj_begin

label alt_day5_dv_dj_begin:
    call alt_day5_dv_dj_vars
    $ alt_pause(1)
    $ alt_chapter(5, u"Alisa. DJ. Morning")
    call alt_day5_dv_dj_morning
    $ alt_pause(1)
    $ alt_save_name(5, u"Alisa. DJ. Breakfast")
    $ day_time()
    call alt_day5_dv_dj_breakfast
    $ alt_pause(1)
    $ alt_chapter(5, u"Alisa. DJ. 2ch-FM")
    call alt_day5_dv_dj_dvachcast
    $ alt_pause(1)
    $ persistent.sprite_time = "day"
    $ alt_chapter(5, u"Alisa. DJ. Lunch")
    call alt_day5_dv_dj_lunch
    $ alt_pause(1)
    $ alt_save_name(5, u"Alisa. DJ. Quiet hour")
    call alt_day5_dv_dj_map_siesta
    $ alt_pause(1)
    $ alt_save_name(5, u"Alisa. DJ. Lunch")
    call alt_day5_dv_dj_afternoon
    $ alt_pause(1)
    $ alt_chapter(5, u"Alisa. DJ. Broadcast")
    call alt_day5_dv_dj_radio_broadcast
    $ alt_pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_save_name(5, u"Alisa. DJ. Evening")
    call alt_day5_dv_dj_dinner
    $ alt_pause(1)
    $ alt_chapter(5, u"Alisa. DJ. Fire")
    call alt_day5_dv_dj_campfire
    $ alt_pause(1)
    $ persistent.sprite_time = 'night'
    $ night_time()
    $ alt_save_name(5, u"Alisa. DJ. Lights out")
    call alt_day5_dv_dj_sleeptime
    $ alt_pause(1)
    jump alt_day6_dv_dj_begin

label alt_day6_dv_dj_begin:
    $ alt_chapter(6, u"Alisa. DJ. Morning")
    $ persistent.sprite_time = "day"
    $ sunset_time()
    call alt_day6_dv_dj_morning
    $ alt_pause(1)
    $ alt_save_name(6, u"Alisa. DJ. Breakfast")
    call alt_day6_dv_dj_breakfast
    $ alt_pause(1)
    $ alt_chapter(6, u"Alisa. DJ. Broadcast")
    $ day_time()
    call alt_day6_dv_dj_broadcast
    $ alt_pause(1)
    $ alt_save_name(6, u"Alisa. DJ. Dinner")
    call alt_day6_dv_dj_lunch
    $ alt_pause(1)
    $ alt_save_name(6, u"Alisa. DJ. Quiet hour")
    call alt_day6_dv_dj_siesta
    $ alt_pause(1)
    $ alt_chapter(6, u"Alisa. DJ. Concert")
    call alt_day6_dv_dj_concert
    $ alt_pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Alisa. DJ. Evening")
    call alt_day6_dv_dj_dinner
    $ alt_pause(1)

    if (alt_day6_dv_dj_secret):
        $ alt_dv_dj_ends = 'true'
    elif (lp_dv >= 20):
        $ alt_dv_dj_ends = 'good'
    elif (lp_dv >= 16 and karma >= 75):
        $ alt_dv_dj_ends = 'rej'
    elif (lp_dv >= 16 and karma < 75):
        $ alt_dv_dj_ends = 'neu'
    else:
        $ alt_dv_dj_ends = 'bad'
    $ alt_save_name(6, u"Alisa. DJ. Evening")
    call alt_day6_dv_dj_no_dance
    $ alt_pause(1)
    $ persistent.sprite_time = 'night'
    $ night_time()
    $ alt_save_name(6, u"Alisa. DJ. Heart to heart")
    call alt_day6_dv_dj_un_night
    if alt_dv_dj_ends == 'true' and lp_dv < 16:
        return
    $ alt_pause(1)
    $ alt_save_name(6, u"Alisa. DJ. Lights out")
    if alt_dv_dj_ends == 'true' or alt_dv_dj_ends == 'good':
        call alt_day6_dv_dj_sleeptime
    else:
        call alt_day6_dv_dj_sleeptime2
    $ alt_pause(1)
    jump alt_day7_dv_dj_begin

label alt_day7_dv_dj_begin:
    $ alt_save_name(7, u"Alisa. DJ. Dream")
    call alt_day7_dv_dj_dream
    $ alt_pause(1)
    $ alt_save_name(7, u"Alisa. DJ. Morning")
    $ persistent.sprite_time = "day"
    $ day_time()
    call alt_day7_dv_dj_morning
    $ alt_save_name(7, u"Alisa. DJ. Points over i")
    call alt_day7_dv_dj_points
    $ alt_pause(1)
    $ alt_save_name(7, u"Alisa. DJ. Departure")
    call alt_day7_dv_dj_departure
    $ alt_pause(1)
    $ persistent.sprite_time = "prolog"
    $ prolog_time()
    $ alt_save_name(7, u"Alisa. DJ. Epilogue")
    if alt_dv_dj_ends == 'bad':
        call alt_day7_dv_dj_bad
    elif alt_dv_dj_ends == 'neu':
        call alt_day7_dv_dj_neu
    elif alt_dv_dj_ends == 'rej':
        call alt_day7_dv_dj_rej
    elif alt_dv_dj_ends == 'good':
        call alt_day7_dv_dj_good
    elif alt_dv_dj_ends == 'exc' and herc:
        call alt_day7_dv_dj_herc_exc
    elif alt_dv_dj_ends == 'exc' and loki:
        call alt_day7_dv_dj_loki_exc
    elif alt_dv_dj_ends == 'exc' and dr:
        call alt_day7_dv_dj_dr_exc
    else:
        call alt_day7_dv_dj_true
    return
