label alt_day4_dv_cl_start:

    $ alt_day3_dj = 'dv'
    $ alt_day3_date = 'dv'
    $ alt_day4_un_fz_companion = 'dv'

    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Алиска. Утро")
    call alt_day4_dv_begin
    pause(1)
    jump alt_day5_dv_cl_start

label alt_day5_dv_cl_start:
 
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Алиска. Утро")
    call alt_day5_dv_begin
    pause(1)
    jump alt_stories_start