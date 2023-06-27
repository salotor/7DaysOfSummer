label alt_day1_start:
    call alt_day1_vars
    $ routetag = "common"
    pause(1)
    call alt_day1_begin
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(1, u"Awakening")
    call alt_day1_bus_start
    pause(1)
    $ alt_chapter(1, u"First meeting")
    call alt_day1_firts_met
    pause(1)
    $ alt_chapter(1, u"Arrival")
    call alt_day1_arrival
    if (counter_sl_7dl != 1):
        if herc or loki:
            call alt_day1_chase1
            $ alt_chapter(1, u"Warehouse")
            call alt_day1_warehouse
            pause(1)
    $ alt_chapter(1, u"Squad leader")
    call alt_day1_mod_tan
    pause(1)
    $ alt_chapter(1, u"Electronik")
    call alt_day1_elektron
    pause(1)
    $ alt_chapter(1, u"Excursion")
    call alt_day1_meeting
    pause(1)
    call alt_day1_soccer_d1
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(1, u"Supper")
    call alt_day1_supper
    pause(1)
    if (counter_sl_7dl == 2):
        $ alt_chapter(1, u"Excursion. Evening")
        call alt_day1_meeting2
    else:
        $ alt_chapter(1, u"Chase")
        call alt_day1_chase
        pause(1)
        if alt_day1_us_shotted:
            call alt_day1_headshot
        else:
            call alt_day1_nocatch
        pause(1)
        $ persistent.sprite_time = "night"
        $ night_time()
        $ alt_chapter(1, u"Saviour")
        call alt_day1_slavya_saviour
        pause(1)
    $ alt_chapter(1, u"Evening")
    call alt_day1_lena
    pause(1)
    call alt_day1_sleep
    pause(1)
    jump alt_day2_start
