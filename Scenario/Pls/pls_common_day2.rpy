label alt_day2_start:
    call alt_day2_vars
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    $ alt_chapter(2, u"Morning")
    call alt_day2_begin
    pause(1)
    $ alt_chapter(2, u"Lineup")
    call alt_day2_lineup
    pause(1)
    $ alt_chapter(2, u"Breakfast")
    call alt_day2_bf
    pause(1)
    if alt_day1_un == 4:
        call alt_day2_un_guide
    elif counter_sl_7dl == 3:
        call alt_day2_sl_guide
    else:
        call alt_day2_convoy
    pause(1)
    call alt_day2_map_prepare
    pause(1)
    call alt_day2_event_estrade
    pause(1)
    call alt_day2_dubstep
    pause(1)
    if alt_day2_minijack:
        call alt_day2_dubstep2
    else:
        call alt_day2_phone
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    call alt_day2_dinner
    pause(1)
    if alt_day2_us_escape:
        $ alt_chapter(2, u"The Grand Escape")
        call alt_day2_grand_escape
    else:
        $ alt_chapter(2, u"Day")
        call alt_day2_siesta
    pause(1)
    $ alt_chapter(2, u"Tournament")
    call alt_day2_tournament
    pause(1)
    if alt_day2_walk == 2:
        call alt_day2_walk_sl
    else:
        call alt_day2_walk_alone
    pause(1)
    $ alt_chapter(2, u"Ultimatum")
    call alt_day2_ultim
    pause(1)
    call alt_day2_cards_tournament_vars
    $ alt_chapter(2, u"Tournament")
    call alt_day2_cards_tournament
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(2, u"Supper")
    call alt_day2_supper
    pause(1)
    if alt_day2_us_cake == 1:
        call alt_day2_slot_us_try
        pause(1)
    if alt_day2_us_cake == 2:
        call alt_day2_slot_us
    else:
        call alt_day2_sup2
        pause(1)
        if alt_day2_sl_chased:
            call alt_day2_slot_sl
        elif alt_day2_dv_chased:
            call alt_day2_eventEv_beach1
            pause(1)
            if (lp_dv > 3) and (alt_day2_dv_ultim == 1):
                pass
            else:
                call alt_day2_mapEv_prepare
        else:
            call alt_day2_mapEv_prepare
    pause(1)
    $ night_time()
    $ persistent.sprite_time = "night"
    call alt_day2_dream
    pause(1)
    jump alt_day3_start
