init python:
    alt_day3_dj = False
    alt_day3_date = False
    alt_day4_un_fz_companion = False

    sdl_var_b_old_dv_cl_dj = sdl_Bool('alt_day3_dj', "Алиса стала диджеем")
    sdl_var_b_old_dv_cl_date = sdl_Bool('alt_day3_date', "Свидание с Алисой в 3 дне")
    sdl_var_b_old_dv_cl_fz = sdl_Bool('alt_day4_un_fz_companion', "Ходили с Алисой в СЛ")

label alt_day4_dv_cl_start:
    $ sdl_local_vars = [sdl_var_b_old_dv_cl_dj, sdl_var_b_old_dv_cl_date, sdl_var_b_old_dv_cl_fz]
    call screen sdl_replay_vars(sdl_local_vars)
    $ alt_vars_screen(sdl_local_vars)

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
    if not persistent.pivo_default_7dl:
        jump alt_stories_start
    else:
        return