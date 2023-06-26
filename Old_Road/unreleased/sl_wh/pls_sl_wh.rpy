label alt_day4_sl_wh_start:
    $ persistent.sprite_time = "night"
    $ night_time()
    call alt_day4_sl_wh_begin
    pause(1)
    jump alt_day5_sl_wh_start

label alt_day5_sl_wh_start:

    $ alt_day4_sl_cl_tut_iz = True

    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Ведьма. Утро.")
    call alt_day5_sl_wh_begin
    with fade
    jump alt_stories_start