label alt_day4_sl_cl_start:
    if (counter_sl_cl == 7) and (lp_sl >= 13):
        call alt_day4_sl_cl_vars
        call alt_day4_un_fz_vars
        call alt_day4_me_neu_vars
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(4, u"Slavya. Morning.")
        call alt_day4_sl_cl_begin
        pause(1)
    call alt_day4_sl_cl_shurik
    pause(1)
    if alt_day4_sl_cl_tut_iz:
        call alt_day4_sl_cl_laundry
        pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Slavya. Evening.")
    call alt_day4_sl_cl_supper
    pause(1)
    call alt_day4_sl_cl_party_up
    pause(1)
    $ alt_chapter(4, u"Slavya. Searches.")
    call alt_day4_sl_cl_lf_coop
    pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    call alt_day4_sl_cl_old_camp
    pause(1)
    if alt_day4_sl_cl_lf_solo == 2:
        call alt_day4_sl_wh_night
    else:
        call alt_day4_sl_cl_old_camp2
    pause(1)
    call alt_day4_sl_cl_cs_night
    pause(1)
    jump alt_day5_sl_cl_start

label alt_day5_sl_cl_start:
    pause(1)
    call alt_day5_sl_cl_vars
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Slavya. Morning.")
    call alt_day5_sl_cl_begin
    pause(1)
    call alt_day5_sl_cl_chief
    pause(1)
    if alt_day_catapult:
        return
    call alt_day5_sl_cl_mt
    pause(1)
    call alt_day5_sl_cl_breakfast
    pause(1)
    call alt_day5_sl_cl_ba_quest
    pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    call alt_day5_sl_cl_catacombs
    pause(1)
    call alt_day5_sl_cl_fog
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    call alt_day5_sl_cl_return
    pause(1)
    $ alt_chapter(5, u"Slavya. Day.")
    call alt_day5_sl_cl_dinner
    pause(1)
    call alt_day5_sl_cl_campfire_prepare
    pause(1)
    call alt_day5_sl_cl_bathing
    pause(1)
    $ alt_chapter(5, u"Slavya. Evening.")
    call alt_day5_sl_cl_supper
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Slavya. Bonfire.")
    call alt_day5_sl_cl_campfire
    pause(1)
    call alt_day5_sl_cl_dn_aid
    pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    call alt_day5_sl_cl_cs_reward
    pause(1)
    $ alt_chapter(5, u"Slavya. Night.")
    call alt_day5_sl_cl_night
    pause(1)
    call alt_day5_sl_cl_sleeptime
    pause(1)
    jump alt_day6_sl_cl_start

label alt_day6_sl_cl_start:
    pause(1)
    call alt_day6_sl_cl_vars
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Slavya. Morning.")
    if alt_day5_sl_cl_hentai_done:
        call alt_day6_sl_cl_begin_good
    elif alt_day4_sl_cl_tut_iz:
        call alt_day6_sl_cl_begin_techno
    else:
        call alt_day6_sl_cl_begin_cave
    pause(1)
    call alt_day6_sl_cl_sh_problems
    pause(1)
    call alt_day6_sl_cl_breakfast
    pause(1)
    call alt_day6_sl_cl_ba_quest
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    call alt_day6_sl_cl_ba_kgb
    pause(1)
    $ alt_chapter(6, u"Slavya. Day.")
    call alt_day6_sl_cl_dinner
    pause(1)
    call alt_day6_sl_cl_amp_list
    pause(1)
    call alt_day6_sl_cl_amp_club
    pause(1)
    if alt_day6_sl_cl_shirt or (alt_sp < 4):
        call alt_day6_sl_cl_ambulance
        pause(1)
        call alt_day6_sl_cl_concert
        pause(1)
        call alt_day6_sl_cl_algorithm
        pause(1)
        $ persistent.sprite_time = "night"
        $ night_time()
        call alt_day6_sl_cl_sh_story
        pause(1)
        $ alt_chapter(6, u"Slavya. Alone again.")
        call alt_day6_sl_cl_sh_tug
        pause(1)
    else:
        call alt_day6_sl_cl_kgb
        pause(1)
        call alt_day6_sl_cl_pirate
        pause(1)
        if alt_day_catapult:
            call alt_day6_sl_cl_loki_exc
            pause(1)
            return
        elif (alt_day6_sl_cl_int == 1) and (alt_sp >= 6) and (persistent.sl_cl_good_rf or persistent.sl_cl_good_rf2 or persistent.sl_cl_good_ussr):
            call alt_day6_sl_cl_ba_help
            pause(1)
            $ persistent.sprite_time = "prolog"
            $ prolog_time()
            call alt_day6_sl_cl_home
            pause(1)
            call alt_day6_sl_cl_intellectual
            pause(1)
            if alt_day6_sl_cl_int == 2:
                $ routetag = "sltrue"
                $ alt_chapter(7, u"Slavya. Phantasm")
                call alt_day7_sl_cl_fear
                pause(1)
                $ persistent.sprite_time = "day"
                $ day_time()
                call alt_day7_sl_cl_1996
                pause(1)
                if alt_day6_sl_cl_int == 3:
                    $ persistent.sprite_time = "night"
                    $ night_time()
                    $ alt_chapter(7, u"Slavya. Choice.")
                    call alt_day7_sl_cl_loop
                    pause(1)
                    $ persistent.sprite_time = "day"
                    $ day_time()
                    call alt_day7_sl_cl_porridge
                    pause(1)
                    $ persistent.sprite_time = "night"
                    $ night_time()
                    if alt_day6_sl_cl_int == 5:
                        call alt_day7_sl_cl_int_rej
                    elif alt_day6_sl_cl_int == 4:
                        call alt_day7_sl_cl_int_true
                    else:
                        call alt_day7_sl_cl_int_good
                    pause(1)
                else:
                    call alt_day7_sl_cl_int_bad
                    pause(1)
            else:
                call alt_day7_sl_cl_int_bad
                pause(1)
            return
        else:
            call alt_day6_sl_cl_regular_arc
            pause(1)
            $ alt_chapter(6, u"Slavya. Concert.")
            call alt_day6_sl_cl_hala
            pause(1)
            $ persistent.sprite_time = "sunset"
            $ sunset_time()
            call alt_day6_sl_cl_sonic
            pause(1)
            call alt_day6_sl_cl_supper
            pause(1)
            $ alt_chapter(6, u"Slavya. Disco")
            call alt_day6_sl_cl_dance
            pause(1)
            call alt_day6_sl_cl_dancing
            pause(1)
            $ persistent.sprite_time = "night"
            $ night_time()
            $ alt_chapter(6, u"Slavya. Night.")
            call alt_day6_sl_cl_debarkader
            pause(1)
    jump alt_day7_sl_cl_start

label alt_day7_sl_cl_start:
    pause(1)
    call alt_day7_sl_cl_vars
    pause(1)
    if alt_day4_sl_cl_tut_iz:
        $ persistent.sprite_time = "prolog"
        $ prolog_time()
        call alt_day7_sl_cl_techno
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    if alt_day6_sl_cl_arc == 'sh':
        $ routetag = "sl"
        $ alt_chapter(7, u"Slavya. Isolation room.")
        call alt_day7_sl_cl_begin_sh
        $ alt_chapter(7, u"Slavya. Morning.")
    else:
        $ routetag = "slbad"
        $ alt_chapter(7, u"Slavya. Morning.")
        call alt_day7_sl_cl_begin_pi
    pause(1)
    call alt_day7_sl_cl_incident
    pause(1)
    call alt_day7_sl_cl_breakfast
    pause(1)
    call alt_day7_sl_cl_bl_tt_map
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    call alt_day7_sl_cl_photo
    pause(1)
    call alt_day7_sl_cl_dinner
    pause(1)
    if alt_day6_sl_cl_good == 1:
        call alt_day7_sl_cl_departure_a2th
        pause(1)
    elif alt_day6_sl_cl_good == 0:
        call alt_day7_sl_cl_departure_lone
        pause(1)
    $ alt_chapter(7, u"Slavya. Epilogue.")
    $ persistent.sprite_time = "prolog"
    $ prolog_time()
    if (lp_sl >= 18) or (alt_sp >= 6):
        if alt_day6_sl_cl_good == 1:
            if lp_sl >= 18:
                call alt_day7_sl_cl_good_ussr
            elif alt_sp >= 6:
                call alt_day7_sl_cl_good_rf
            pause(1)
            if alt_day6_sl_cl_arc == 'sh':
                $ persistent.sprite_time = "prolog"
                $ prolog_time()
                call alt_day7_sl_cl_ps
        elif alt_day6_sl_cl_good == 3:
            call alt_day7_sl_cl_bad
        else:
            if (alt_day6_sl_cl_arc == 'sh') and (lp_sl > 20):
                if alt_day6_sl_cl_good == 2:
                    call alt_day7_sl_cl_good_rf
                else:
                    call alt_day7_sl_cl_good_rf2
            else:
                if alt_sp >= 6:
                    call alt_day7_sl_cl_rej
                elif lp_sl >= 18:
                    call alt_day7_sl_cl_rej_rf
        pause(1)
    else:
        call alt_day7_sl_cl_bad
        pause(1)
        if alt_day6_sl_cl_arc == 'sh':
            $ persistent.sprite_time = "prolog"
            $ prolog_time()
            call alt_day7_sl_cl_ps
            pause(1)
    return
