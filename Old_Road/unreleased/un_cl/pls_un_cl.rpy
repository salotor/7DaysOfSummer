label alt_day3_un_cl_vars:
    $ alt_day3_un_cl_portrait = False
    $ alt_day3_un_cl_kiss = False
    $ alt_day3_un_cl_question = False
    return

label alt_day4_un_cl_vars:
    $ alt_day4_un_cl_punishment = False
    $ alt_day4_un_cl_alien_body = False
    $ alt_day4_un_cl_psr = False
    $ alt_day4_un_cl_london_hentai = False
    return

label alt_day3_un_cl_start:

    $ lp_un = 10
    $ counter_un_cl = 1
    $ routetag = "un"
    $ dr = True

    jump alt_un_cl_selector_caller

label alt_day3_un_cl_start_day:
    $ renpy.block_rollback()
    $ sdl_local_vars = [sdl_var_b_d3_me_duty]
    call screen sdl_replay_vars(sdl_local_vars)
    $ alt_vars_screen(sdl_local_vars)
    $ alt_char_set(plthr)
    call alt_day3_un_cl_vars
    stop music fadeout 2
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(3, u"Завтрак")
    call alt_day3_un_cl_begin
    pause(1)
    $ alt_chapter(3, u"Лена. КЛ. Карьер")
    call alt_day3_un_cl_event_sandpit
    pause(1)
    call alt_day3_un_cl_after_sandpit
    pause (1)
    $ alt_chapter(3, u"Лена. КЛ. Обед")
    call alt_day3_un_cl_lunch
    pause(1)
    $ alt_chapter(3, u"Лена. КЛ. Тихий час")
    call alt_day3_un_cl_quiet_hour
    pause(1)
    $ alt_chapter(3, u"Лена. КЛ. Полдник")
    call alt_day3_un_cl_afternoon
    pause(1)
    $ alt_chapter(3, u"Лена. КЛ. Медпункт")
    call alt_day3_un_cl_aidpost_help
    pause(1)
    $ alt_chapter(3, u"Лена. КЛ. Ужин")
    call alt_day3_un_cl_dinner
    pause(1)
    $ persistent.sprite_time = 'sunset'
    $ sunset_time()
    $ alt_chapter(3, u"Лена. КЛ. Вечер")
    call alt_day3_un_cl_evening
    pause(1)
    call alt_day3_un_cl_sleeptime
    pause(1)
    jump alt_day4_un_cl_start

label alt_day4_un_cl_start:
    $ renpy.block_rollback()
    stop music fadeout 2
    pause(1)
    call alt_day4_un_cl_vars
    $ persistent.sprite_time = 'night'
    $ night_time()
    $ alt_chapter(4, u"Лена. КЛ. ???")
    call alt_day4_un_cl_dream
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(4, u"Лена. КЛ. Утро")
    call alt_day4_un_cl_morning
    pause(1)
    call alt_day4_un_cl_exercise
    pause(1)
    $ alt_chapter(4, u"Лена. КЛ. Завтрак")
    call alt_day4_un_cl_breakfast
    pause(1)
    if alt_day4_un_cl_punishment == True:
        $ alt_chapter(4, u"Лена. КЛ. Под арестом")
        call alt_day4_un_cl_arrest
    else:
        $ alt_chapter(4, u"Лена. КЛ. Потерянная голова")
        call alt_day4_un_cl_clubs
        call alt_day4_un_cl_search
    pause(1)
    $ alt_chapter(4, u"Лена. КЛ. Обед")
    call alt_day4_un_cl_dinner
    pause(1)
    $ alt_chapter(4, u"Лена. КЛ. Тихий час")
    call alt_day4_un_cl_quiet_hour
    pause(1)
    $ persistent.sprite_time = 'sunset'
    $ sunset_time()
    $ alt_chapter(4, u"Лена. КЛ. Полдник")
    call alt_day4_un_cl_afternoon
    pause(1)
    $ alt_chapter(4, u"Лена. КЛ. Встреча с Леной")
    if alt_day4_un_cl_alien_body == True:
        call alt_day4_un_cl_evening_alien
    elif alt_day4_un_cl_psr == True:
        call alt_day4_un_cl_evening_psr
    else:
        call alt_day4_un_cl_evening_null
    pause(1)
    call alt_day4_un_cl_london
    if not persistent.pivo_default_7dl:
        jump alt_stories_start
    else:
        return
