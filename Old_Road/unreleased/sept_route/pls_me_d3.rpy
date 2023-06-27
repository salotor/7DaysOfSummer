init python:
    alt_me_neu_true = False

    sdl_var_b_old_me_d3_true = sdl_Bool('alt_me_neu_true', "Прошёл старого сыча на тру")

label alt_day1_me_d3_vars:
    $ alt_day2_us_candy = 0
    $ alt_d3_bad_0 = False
    $ alt_day1_me_d3_chase = False
    $ alt_day1_me_d3_robbery = False
    $ alt_day1_me_d3_dv_feed = False
    $ alt_day1_me_d3_sl_conv = False
    $ alt_day1_me_d3_sl_met = False
    $ alt_day1_me_d3_us_robbed = False
    return

label alt_day1_me_d3_start:
    $ sdl_local_vars = [sdl_var_b_old_me_d3_true]
    call screen sdl_replay_vars(sdl_local_vars)
    $ alt_vars_screen(sdl_local_vars)

    call alt_day1_me_d3_vars
    $ alt_d3_bad_0 = True
    $ reput = 100
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(1, u"ОТКАТ")
    call alt_day1_me_d3_M
    pause(1)
    call alt_day1_me_d3_A
    pause(1)
    call alt_day1_me_d3_S
    pause(1)
    call alt_day1_me_d3_L
    pause(1)
    call alt_day1_me_d3_O
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    call alt_day1_me_d3_supper
    pause(1)
    call alt_day1_me_d3_U
    if not alt_day1_me_d3_us_robbed:
        call alt_day1_me_d3_U_reject
        pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    call alt_day1_me_d3_ev_A_S
    pause(1)
    call alt_day1_me_d3_ev_mt
    pause(1)
    jump alt_day2_me_d3_start

label alt_day2_me_d3_start:
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(2, u"ОТКАТ")
    pause(1)
    call alt_day2_me_d3_pre
    scene black
    with fade
    pause(1)
    if not persistent.pivo_default_7dl:
        jump alt_stories_start
    else:
        return