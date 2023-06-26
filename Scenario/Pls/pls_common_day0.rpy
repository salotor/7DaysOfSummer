label alt_day0_prologue:
    $ renpy.pause(2)
    $ prolog_time()
    scene black
    play music music_list["drown"] fadein 3
    $ plthr = u"Выбор"
    $ alt_chapter0()
    with fade
    show spill_red with dspr
    $ renpy.pause(2)
    show spill_gray with dspr
    $ renpy.pause(2)
    if persistent.mi_7dl_good_human or persistent.mi_7dl_good_star:
        show acm_m
    if persistent.dv_7dl_good_ussr:
        show acm_a
    if persistent.sl_7dl_loki_good or persistent.sl_7dl_herc_good or persistent.sl_7dl_dr_good:
        show acm_s
    if persistent.un_7dl_good_ussr:
        show acm_l
    if persistent.mt_7dl_good:
        show acm_o
    if persistent.us_7dl_good:
        show acm_u
    with dissolve2
    $ renpy.pause(3)
    scene black with fade2
    show alt_credits "Я с трудом вспоминаю, \n с чего всё началось…" with dissolve2:
        pos (200,540)
    with dissolve2
    $ renpy.block_rollback()
    call screen alt_day0_charsel

label alt_day0_approve_herc:
    play sound sfx_7dl["mpbt"] fadein 0
    scene intro_herc with dissolve
    $ renpy.pause(1)
    jump alt_day0_role_h

label alt_day0_approve_loki:
    play sound sfx_punch_medium
    scene intro_loki with dissolve
    $ renpy.pause(1)
    jump alt_day0_role_l

label alt_day0_approve_dr:
    play sound sfx_wind_gust
    scene intro_dr with dissolve
    $ renpy.pause(1)
    jump alt_day0_role_d

label alt_day0_role_h:
    $ herc = True
    $ plthr = u"Герк"
    $ alt_chapter0()
    play sound sfx_7dl["role_herc"]
    $ renpy.pause(4)
    with fade2
    $ routetag = "prologue"
    scene black with fade
    show alt_credits "ПРЕДУПРЕЖДЕНИЕ\nВсе совпадения персонажей и характеров\nс реально существующими людьми\nсчитать злой волей автора" with dissolve2:
        pos (200,540)
    $ renpy.pause(4)
    $ prolog_time()
    call alt_day0_start_h
    jump alt_day0_start

label alt_day0_role_l:
    $ loki = True
    $ plthr = u"Локи"
    $ alt_chapter0()
    play sound sfx_7dl["role_loki"]
    $ renpy.pause(4)
    with dissolve2
    $ routetag = "prologue"
    scene black with fade
    show alt_credits "ПРЕДУПРЕЖДЕНИЕ\nВсе совпадения персонажей и характеров\nс реально существующими людьми\nсчитать злой волей автора" with dissolve2:
        pos (200,540)
    $ renpy.pause(4)
    $ prolog_time()
    call alt_day0_start_l
    jump alt_day0_start

label alt_day0_role_d:
    $ dr = True
    $ plthr = u"Дрищ"
    $ alt_chapter0()
    play sound sfx_7dl["role_drisch"]
    $ renpy.pause(4)
    with fade2
    $ routetag = "prologue"
    scene black with fade
    show alt_credits "ПРЕДУПРЕЖДЕНИЕ\nВсе совпадения персонажей и характеров\nс реально существующими людьми\nсчитать злой волей автора" with dissolve2:
        pos (200,540)
    $ renpy.pause(4)
    $ prolog_time()
    call alt_day0_start_d
    jump alt_day0_start

label alt_day0_start:
    if alt_day_catapult:
        return
    $ renpy.pause(1)
    play music "<to 66.9>" + music_7dl["intro"] fadein 5
    scene black
    $ renpy.pause(3)
    scene op_back
    with dissolve2
    $ renpy.pause(2)
    show op_mi
    with dissolve2
    $ renpy.pause(2)
    show op_dv zorder 2
    with dissolve2
    $ renpy.pause(2)
    show sl_bus
    with dissolve2
    $ renpy.pause(2)
    show op_un
    with dissolve2
    $ renpy.pause(2)
    show mt_bus
    with dissolve2
    $ renpy.pause(2)
    show op_us
    show uv_bus zorder 1
    with dissolve2
    $ renpy.pause(2)
    show logo_day:
        pos (400,150)
    with dissolve2
    show logo_7dl with zoomin:
        pos (1200,350)
    with vpunch
    $ renpy.pause(2)
    scene black
    with dissolve2
    stop music fadeout 5
    $ renpy.pause(5)
    $ renpy.pause(1)
    jump alt_day1_start