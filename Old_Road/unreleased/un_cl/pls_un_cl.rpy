label alt_day3_un_cl_vars:
    $ alt_day3_un_cl_portrait = False
    $ alt_day3_un_cl_kiss = False
    $ alt_day3_un_cl_question = False
    return

label alt_day3_un_cl_start:

    $ lp_un = 10
    $ counter_un_cl = 1
    $ routetag = "un"
    $ dr = True









    call alt_day3_un_cl_vars
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
    $ alt_chapter(4, u"Лена. КЛ. ???")
    call alt_day4_un_cl_dream
    pause(4)
    jump alt_stories_start
