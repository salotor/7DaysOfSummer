init 9999 python:
    # Список всех фонов. Сначала идёт основное изображение. Далее по порядку (опционально): оригинальный ли это фон (True/False), доп. варианты фона (в квадратных скобках).
    sdl_gall_bgs_list = [
        sdl_gall_bg("bus_stop", False, ["ext_bus_stop_summer_7dl"]),
        sdl_gall_bg("ext_adductius_7dl", True),
        sdl_gall_bg("ext_admins_day_7dl", True, ["ext_admins_night_7dl", "ext_admins_rain_7dl"]),
        sdl_gall_bg("ext_aidpost_day", False, ["ext_aidpost_night", "ext_aidpost_rain_7dl", "ext_aidpost_sunset_7dl", "ext_aidpost_night_light_7dl"]),
        sdl_gall_bg("ext_alley_7dl", False),
        sdl_gall_bg("ext_backdoor_day_7dl", True, ["ext_backdoor_night_7dl", "ext_backdoor_sunset_7dl"]),
        sdl_gall_bg("ext_backroad_day_7dl", True, ["ext_backroad_sunset_7dl"]),
        sdl_gall_bg("ext_backstage_alt_day_7dl", False, ["ext_backstage_alt_night_7dl"]),
        sdl_gall_bg("ext_bathhouse_day_7dl", False, ["ext_bathhouse_night"]),
        sdl_gall_bg("ext_beach2_day_7dl", False),
        sdl_gall_bg("ext_beach_day", False, ["ext_beach_night", "ext_beach_sunset"]),
        sdl_gall_bg("ext_boathouse_alt2_day_7dl", False),
        sdl_gall_bg("ext_boathouse_alt_day_7dl", True, ["ext_boathouse_alt_night_7dl"]),
        sdl_gall_bg("ext_boathouse_day", False, ["ext_boathouse_night", "ext_boathouse_rain_7dl", "ext_boathouse_sunset_7dl"]),
        sdl_gall_bg("ext_bus", False, ["ext_no_bus", "ext_no_bus_night", "ext_no_bus_sunset"]),
        sdl_gall_bg("ext_bus2_7dl", False),
        sdl_gall_bg("ext_bush_sunset_7dl", True),
        sdl_gall_bg("ext_busstop_dust_7dl", True, ["ext_busstop_sun_7dl"]),
        sdl_gall_bg("ext_camp_entrance_day", False, ["ext_camp_entrance_night", "ext_camp_entrance_sunset_7dl", "ext_entrance_night_clear_7dl", "ext_entrance_night_clear_closed_7dl", "ext_entrance_winter_7dl", "ext_entrance_fantasm_winter_7dl"]),
        sdl_gall_bg("ext_childhouse_day_7dl", True, ["ext_childhouse_winter_7dl"]),
        sdl_gall_bg("ext_city_night2_7dl", True),
        sdl_gall_bg("ext_city_night_7dl", True),
        sdl_gall_bg("ext_clubs_day", False, ["ext_clubs_night", "ext_clubs_rain_7dl", "ext_clubs_sunset_7dl"]),
        sdl_gall_bg("ext_coulisses_7dl", False),
        sdl_gall_bg("ext_countryside_day_7dl", True),
        sdl_gall_bg("ext_dining_hall_away_day", False, ["ext_dining_hall_away_night", "ext_dining_hall_away_rain_7dl", "ext_dining_hall_away_sunset"]),
        sdl_gall_bg("ext_dining_hall_backroad_day_7dl", False, ["ext_dining_hall_backroad_night_7dl"]),
        sdl_gall_bg("ext_dining_hall_near_day", False, ["ext_dining_hall_near_night", "ext_dining_hall_near_rain_7dl", "ext_dining_hall_near_sunset"]),
        sdl_gall_bg("ext_dv_hideout_day_7dl", False),
        sdl_gall_bg("ext_earth_7dl", False),
        sdl_gall_bg("ext_emptiness_7dl", False),
        sdl_gall_bg("ext_gostinka_day_7dl", True, ["ext_gostinka_night_7dl"]),
        sdl_gall_bg("ext_hospital2_away_day_7dl", True, ["ext_hospital2_away_night_7dl"]),
        sdl_gall_bg("ext_house_of_dv_day", False, ["ext_house_of_dv_night"]),
        sdl_gall_bg("ext_house_of_el_day_7dl", False, ["ext_house_of_el_night_7dl"]),
        sdl_gall_bg("ext_house_of_mt_day", False, ["ext_house_of_mt_night", "ext_house_of_mt_night_without_light", "ext_house_of_mt_rain_7dl", "ext_house_of_mt_sunset"]),
        sdl_gall_bg("ext_house_of_sl_day", False, ["ext_house_of_sl_night_7dl"]),
        sdl_gall_bg("ext_house_of_un_day", False, ["ext_house_of_un_day_with_un_7dl", "ext_house_of_un_night_7dl", "ext_house_of_un_rain_7dl"]),
        sdl_gall_bg("ext_houses_day", False, ["ext_houses_night_7dl", "ext_houses_rainy_day_7dl", "ext_houses_snowy_day_7dl", "ext_houses_sunset"]),
        sdl_gall_bg("ext_island_day", False, ["ext_island_night"]),
        sdl_gall_bg("ext_japan_graveyard_rain_7dl", True),
        sdl_gall_bg("ext_khruschevka_day_7dl", True, ["ext_khruschevka_night_7dl", "ext_khruschevka_rain_7dl", "ext_khruschevka_sunset_7dl", "ext_khruschevka_winter_7dl"]),
        sdl_gall_bg("ext_lake_day_7dl", True, ["ext_lake_night_7dl", "ext_lake_night_px_7dl", "ext_lake_sunset_7dl"]),
        sdl_gall_bg("ext_library_day", False, ["ext_library_night", "ext_library_sunset_7dl"]),
        sdl_gall_bg("ext_lost_city_7dl", False),
        sdl_gall_bg("ext_musclub_day", False, ["ext_musclub_night_7dl", "ext_musclub_rain_7dl", "ext_musclub_snowy_day_7dl"]),
        sdl_gall_bg("ext_musclub_verandah_day_7dl", False),
        sdl_gall_bg("ext_mv2_7dl", True),
        sdl_gall_bg("ext_night_sky_7dl", False),
        sdl_gall_bg("ext_old_building_day_7dl", False, ["ext_old_building_day_rainy_7dl", "ext_old_building_night", "ext_old_building_night_moonlight"]),
        sdl_gall_bg("ext_old_road_7dl", False),
        sdl_gall_bg("ext_path2_day", False, ["ext_path2_night", "ext_path2_rain_7dl"]),
        sdl_gall_bg("ext_path_day", False, ["ext_path_night", "ext_path_rain_7dl", "ext_path_sunset"]),
        sdl_gall_bg("ext_playground_day", False, ["ext_playground_night", "ext_playground_sunset_7dl"]),
        sdl_gall_bg("ext_polyana_day", False, ["ext_polyana_night", "ext_polyana_sunset"]),
        sdl_gall_bg("ext_railbridge_sunset_7dl", True),
        sdl_gall_bg("ext_road2_night_7dl", False),
        sdl_gall_bg("ext_road_day", False, ["ext_road_night2", "ext_road_sunset_7dl", "ext_road_winter_7dl"]),
        sdl_gall_bg("ext_road_night", False),
        sdl_gall_bg("ext_roof_city_night_7dl", False),
        sdl_gall_bg("ext_sandpit_day_7dl", True, ["ext_sandpit_night_7dl"]),
        sdl_gall_bg("ext_seashore_7dl", False),
        sdl_gall_bg("ext_shower_day_7dl", True, ["ext_shower_night_7dl"]),
        sdl_gall_bg("ext_sky2_7dl", False),
        sdl_gall_bg("ext_sky_7dl", False),
        sdl_gall_bg("ext_smolensky_graveyard_day_7dl", True, ["ext_smolensky_graveyard_winter_7dl", "ext_smolensky_graveyard_winter_day_7dl"]),
        sdl_gall_bg("ext_square2_day_7dl", True),
        sdl_gall_bg("ext_square_day", False, ["ext_square_day_party_7dl", "ext_square_night", "ext_square_night_party", "ext_square_night_party2", "ext_square_rain_day_7dl", "ext_square_sunset", "ext_square_sunset3_7dl"]),
        sdl_gall_bg("ext_stage_big_day_7dl", False, ["ext_stage_big_clear_day_7dl", "ext_stage_big_night", "ext_stage_big_sunset_7dl"]),
        sdl_gall_bg("ext_stage_normal_day", False, ["ext_stage_normal_clear_7dl", "ext_stage_normal_night"]),
        sdl_gall_bg("ext_stairs_day_7dl", False, ["ext_stairs_night_7dl", "ext_stairs_sunset_7dl"]),
        sdl_gall_bg("ext_stand3_7dl", False),
        sdl_gall_bg("ext_street_night_7dl", False),
        sdl_gall_bg("ext_suare_winter_7dl", False),
        sdl_gall_bg("ext_tennis_court_7dl", True),
        sdl_gall_bg("ext_townscape_ph2_day_7dl", True),
        sdl_gall_bg("ext_townscape_ph_day_7dl", True),
        sdl_gall_bg("ext_tree_house_7dl", True, ["ext_tree_house_sunset_7dl"]),
        sdl_gall_bg("ext_tribune_day_7dl", False),
        sdl_gall_bg("ext_un_hideout_day_7dl", True, ["ext_un_hideout_night_7dl"]),
        sdl_gall_bg("ext_underwater_7dl", False),
        sdl_gall_bg("ext_us_lake_7dl", False),
        sdl_gall_bg("ext_valun_day_7dl", True),
        sdl_gall_bg("ext_volley_court_7dl", True),
        sdl_gall_bg("ext_warehouse2_day_7dl", True),
        sdl_gall_bg("ext_warehouse_day_7dl", False, ["ext_warehouse_blurry_7dl", "ext_warehouse_night_7dl", "ext_warehouse_rain_day_7dl", "ext_warehouse_sunset_7dl"]),
        sdl_gall_bg("ext_washstand2_day", False),
        sdl_gall_bg("ext_washstand_day", False, ["ext_washstand_night_7dl", "ext_washstand_rain_7dl"]),
        sdl_gall_bg("ext_winter_night_7dl", True, ["ext_winter_night_rotate_7dl"]),
        sdl_gall_bg("ext_winterpark_7dl", True),

        sdl_gall_bg("int_access2_day_7dl", True),
        sdl_gall_bg("int_access_day_7dl", False),
        sdl_gall_bg("int_admin_boxes_day_7dl", False),
        sdl_gall_bg("int_admins_7dl", True),
        sdl_gall_bg("int_aidpost_day", False, ["int_aidpost_day_apple", "int_aidpost_night", "int_aidpost_no_light_night_7dl", "int_aidpost_sunset_7dl"]),
        sdl_gall_bg("int_attic2_day_7dl", False, ["int_attic2_night_7dl"]),
        sdl_gall_bg("int_attic_7dl", False),
        sdl_gall_bg("int_bar_7dl", False),
        sdl_gall_bg("int_bus", False, ["int_bus_black", "int_bus_night", "int_bus_people_day", "int_bus_people_night", "int_bus_warp_7dl"]),
        sdl_gall_bg("int_bus_flood_7dl", True),
        sdl_gall_bg("int_caffee_day_7dl", False),
        sdl_gall_bg("int_catacomb_door_fullbright_7dl", False),
        sdl_gall_bg("int_catacombs_entrance", False),
        sdl_gall_bg("int_catacombs_hole", False),
        sdl_gall_bg("int_catacombs_living", False),
        sdl_gall_bg("int_chief_office_day_7dl", True, ["int_chief_office_rain_7dl"]),
        sdl_gall_bg("int_childhouse_corridor_7dl", True, ["int_hospital_corridor_7dl"]),
        sdl_gall_bg("int_childhouse_room_day_7dl", True, ["int_childhouse_room_night_7dl"]),
        sdl_gall_bg("int_church_7dl", False),
        sdl_gall_bg("int_clubs_dj_7dl", True, ["int_clubs_dj_nolight_7dl"]),
        sdl_gall_bg("int_clubs_male2_night", False, ["int_clubs_male2_night_nolight", "int_warehouse2_day_7dl"]),
        sdl_gall_bg("int_clubs_male_day", False, ["int_clubs_male_night_7dl", "int_clubs_male_night_candle_7dl", "int_clubs_male_rain_7dl", "int_clubs_male_rain_clean_table_7dl", "int_clubs_male_sunset"]),
        sdl_gall_bg("int_coaching_room_7dl", False),
        sdl_gall_bg("int_concert_room_7dl", False),
        sdl_gall_bg("int_coupe_day_7dl", True, ["int_coupe_night_7dl"]),
        sdl_gall_bg("int_dining_hall_day", False, ["int_dining_hall_night", "int_dining_hall_people_day", "int_dining_hall_people_rain_7dl", "int_dining_hall_people_sunset_7dl", "int_dining_hall_people_sunset_pp_7dl", "int_dining_hall_rain_7dl", "int_dining_hall_sunset"]),
        sdl_gall_bg("int_dv_radioroom_day_7dl", False, ["int_dv_radioroom_night_7dl"]),
        sdl_gall_bg("int_dv_room_7dl", False, ["int_dv_room_night_7dl"]),
        sdl_gall_bg("int_editorial_day_7dl", True),
        sdl_gall_bg("int_excalator2_7dl", True),
        sdl_gall_bg("int_excalator_7dl", True),
        sdl_gall_bg("int_extra_house_day_7dl", False, ["int_extra_house_night_7dl", "int_extra_house_nolight_7dl", "int_extra_house_rain_7dl", "int_extra_house_sunset_7dl"]),
        sdl_gall_bg("int_future_airliner_7dl", False),
        sdl_gall_bg("int_future_office_7dl", False),
        sdl_gall_bg("int_home_lift_7dl", True, ["int_future_lift_7dl"]),
        sdl_gall_bg("int_hospital_hall_day_7dl", True),
        sdl_gall_bg("int_house_of_dv_day", False, ["int_house_of_dv_night", "int_house_of_dv_night_no_light_7dl"]),
        sdl_gall_bg("int_house_of_el_day_7dl", False, ["int_house_of_el_sunset_7dl"]),
        sdl_gall_bg("int_house_of_mt_day", False, ["int_house_of_mt_backpack_day", "int_house_of_mt_backpack_sunset", "int_house_of_mt_night", "int_house_of_mt_night2", "int_house_of_mt_noitem_day_7dl", "int_house_of_mt_noitem_night", "int_house_of_mt_sunset"]),
        sdl_gall_bg("int_house_of_sl_day", False),
        sdl_gall_bg("int_house_of_un_day", False, ["int_house_of_un_night"]),
        sdl_gall_bg("int_kitchen_7dl", False),
        sdl_gall_bg("int_liaz", False, ["int_liaz_city_7dl"]),
        sdl_gall_bg("int_library_day", False, ["int_library_night", "int_library_night2", "int_library_rain_7dl"]),
        sdl_gall_bg("int_looney_bin_7dl", False),
        sdl_gall_bg("int_looney_bin_nightmare_7dl", False),
        sdl_gall_bg("int_metrostation_7dl", False),
        sdl_gall_bg("int_mine", False, ["int_mine_water_7dl"]),
        sdl_gall_bg("int_mine_coalface", False),
        sdl_gall_bg("int_mine_crossroad", False),
        sdl_gall_bg("int_mine_door", False),
        sdl_gall_bg("int_mine_exit_day_7dl", False, ["int_mine_exit_night_light"]),
        sdl_gall_bg("int_mine_halt", False),
        sdl_gall_bg("int_mine_halt_left_7dl", False),
        sdl_gall_bg("int_mine_heart_7dl", False),
        sdl_gall_bg("int_mine_room", False),
        sdl_gall_bg("int_mine_room2_7dl", False),
        sdl_gall_bg("int_mt_sam_room_7dl", True),
        sdl_gall_bg("int_mt_sam_room_away_7dl", True),
        sdl_gall_bg("int_mt_sam_room_close_7dl", True),
        sdl_gall_bg("int_musclub_day", False, ["int_musclub_night_nolight_7dl", "int_musclub_rain_7dl", "int_musclub_sunset_7dl"]),
        sdl_gall_bg("int_old_building_cab_day_7dl", False, ["int_old_building_cab_night_7dl"]),
        sdl_gall_bg("int_old_building_day_7dl", False, ["int_old_building_night"]),
        sdl_gall_bg("int_opened_door_7dl", False),
        sdl_gall_bg("int_potato_storage_7dl", True),
        sdl_gall_bg("int_refinery_day_7dl", True, ["int_refinery_night_7dl"]),
        sdl_gall_bg("int_school_corridor_7dl", False),
        sdl_gall_bg("int_semen_bath_7dl", False),
        sdl_gall_bg("int_semen_kitchen_7dl", False),
        sdl_gall_bg("int_semen_room_7dl", False),
        sdl_gall_bg("int_semen_room_alt_7dl", False),
        sdl_gall_bg("int_sporthall_day_7dl", True, ["int_sporthall_night_7dl"]),
        sdl_gall_bg("int_staircase_7dl", True),
        sdl_gall_bg("int_store_7dl", True),
        sdl_gall_bg("int_toilet_night_7dl", True),
        sdl_gall_bg("int_train_7dl", True),
        sdl_gall_bg("int_tree_house_7dl", True, ["int_tree_house_sunset_7dl"]),
        sdl_gall_bg("int_un_exhibition_7dl", False),
        sdl_gall_bg("int_un_stud_7dl", False),
        sdl_gall_bg("int_us_frontdoor_7dl", False),
        sdl_gall_bg("int_us_kitchen_7dl", False),
        sdl_gall_bg("int_us_livingroom_7dl", False),
        sdl_gall_bg("int_wagon_day_7dl", True, ["int_wagon_sunset_7dl"]),
        sdl_gall_bg("int_ward2_sunset_7dl", False),
        sdl_gall_bg("int_ward_day_7dl", False, ["int_ward_sunset_7dl"]),
        sdl_gall_bg("int_wardrobe2_7dl", True, ["int_wardrobe2_mirror_7dl"]),
        sdl_gall_bg("int_wardrobe_7dl", True, ["int_wardrobe_mirror_7dl"]),
        sdl_gall_bg("int_warehouse3_day_7dl", True, ["int_warehouse3_night_7dl"]),
        sdl_gall_bg("int_warehouse_day_7dl", True),
        sdl_gall_bg("intro_xx", False, ["int_intro_liaz_7dl"]),
        sdl_gall_bg("semen_room", False, ["int_semen_room_clean_7dl", "int_semen_room_half_clean_7dl", "int_semen_room2_7dl"]),
        sdl_gall_bg("semen_room_window", False, ["int_semen_room_window_day_7dl"])
        ]

    # Список всех артов. Сначала идёт основное изображение. Далее по порядку (опционально): список персонажей на арте (в квадратных скобках), оригинальный ли это арт (True/False), показан ли на арте 18+ cumтент (True/False), вертикальный ли арт (соотношение сторон в виде числа/False), доп. варианты арта (в квадратных скобках).
    sdl_gall_arts_list = [
        sdl_gall_art("d0_me_loki_park_7dl", ["me"], True, False, False),
        sdl_gall_art("d1_me_end_of_day_7dl", ["me"], False, False, False),
        sdl_gall_art("d1_food_normal", [""], False, False, False, ["d1_food_skolop"]),
        sdl_gall_art("d1_grasshopper", ["us","un"], False, False, False),
        sdl_gall_art("d1_me_mirror_casual2_7dl", ["me"], False, False, False, ["d3_me_mirror_bordo_7dl", "d3_me_mirror_pioneer_7dl", "d7_me_mirror_casual_7dl"]),
        sdl_gall_art("d1_mi_bus_7dl", ["mi"], True, False, False, ["d1_mi_bus2_7dl", "d1_mi_bus3_7dl"]),
        sdl_gall_art("d1_mi_dv_bus_7dl", ["mi","dv"], True, False, False, ["d1_mi_dv_bus2_7dl"]),
        sdl_gall_art("d1_sl_dinner", ["sl","me"], False, False, False, ["d1_sl_dinner_day_7dl", "d1_sl_dinner_pi_7dl", "d1_sl_dinner_0", "d1_sl_dinner_0_day_7dl", "d1_sl_dinner_0_pi_7dl"]),
        sdl_gall_art("d1_un_book_7dl", ["un"], True, False, False, ["d1_un_book0_7dl"]),
        sdl_gall_art("d1_uv_2", ["uv"], False, False, False),
        sdl_gall_art("d2_2ch_beach", ["dv"], False, False, 0.56),
        sdl_gall_art("d2_dv_boat_day_7dl", ["dv","me"], False, False, False),
        sdl_gall_art("d2_us_boat_day_7dl", ["us","me"], False, False, False),
        sdl_gall_art("d5_me_boat_night_7dl", ["me"], False, False, False),
        sdl_gall_art("d5_un_boat_night_7dl", ["un","me"], False, False, False),
        sdl_gall_art("d6_mi_boat_day_7dl", ["mi","me"], False, False, False),
        sdl_gall_art("d4_lineup_with_mi_7dl", ["mt","dv","mz","sl","el"], False, False, False, ["d2_lineup", "d4_lineup_no_un_7dl", "d4_lineup_no_un_us_7dl"]),
        sdl_gall_art("d2_mi_polaroid_7dl", ["mi","me"], True, False, False),
        sdl_gall_art("d2_micu_lib", ["mz"], False, False, False),
        sdl_gall_art("d2_miku_piano", ["mi"], False, True, False, ["d2_miku_piano2"]),
        sdl_gall_art("d2_mt_resort_7dl", ["mt","me"], True, False, False),
        sdl_gall_art("d2_mt_undressed", ["mt"], False, True, False, ["d2_mt_undressed_2"]),
        sdl_gall_art("d2_slavya_forest", ["sl"], False, True, False),
        sdl_gall_art("d2_sovenok", ["un","me"], False, False, False, ["d2_un_owlet_pioneer_7dl"]),
        sdl_gall_art("d2_un_kissing_7dl", ["un","me"], True, False, False),
        sdl_gall_art("d2_un_knees_7dl", ["un","me"], True, False, False),
        sdl_gall_art("d2_us_soccer_sunset_7dl", ["us"], False, True, False),
        sdl_gall_art("d2_us_trainhop_7dl", ["us"], True, False, False),
        sdl_gall_art("d2_water_dan", ["dv","me"], False, False, False, ["d2_water_dan_night_7dl"]),
        sdl_gall_art("d3_disco", ["el","us","mt","sl","sh"], False, False, False, ["d3_disco_no_un_7dl"]),
        sdl_gall_art("d7_dv_alice_dj_7dl", ["dv"], True, False, False, ["d3_dv_alice_dj80_7dl"]),
        sdl_gall_art("d3_dv_guitar", ["dv"], False, True, False),
        sdl_gall_art("d3_dv_kiss_7dl", ["dv","me"], True, False, False),
        sdl_gall_art("d3_dv_scene_1", ["dv","me"], False, False, False, ["d3_dv_scene_2"]),
        sdl_gall_art("d3_me_fag_room_7dl", ["me"], False, False, False),
        sdl_gall_art("d3_mi_dance_7dl", ["mi","me"], True, False, False, ["d3_mi_dance_bordo_7dl"]),
        sdl_gall_art("d3_mt_dance_7dl", ["mt","me"], False, False, False),
        sdl_gall_art("d3_potato_1_7dl", ["us","me"], False, False, False, ["d3_potato_2_7dl"]),
        sdl_gall_art("d3_sl_bath_unplaited_7dl", ["sl"], False, True, False),
        sdl_gall_art("d3_sl_dance", ["sl","me"], False, False, False, ["d3_sl_dance_bordo_7dl", "d6_sl_dance_pioneer_7dl"]),
        sdl_gall_art("d6_dv_dance_pioneer_7dl", ["dv","me"], False, False, False, ["d6_dv_dance_bordo_7dl"]),
        sdl_gall_art("d3_un_dance", ["un","me"], False, False, False, ["d3_un_dance_bordo_7dl", "d6_un_dance_pioneer_7dl"]),
        sdl_gall_art("d3_un_dance2_7dl", ["un","me"], True, False, False),
        sdl_gall_art("d6_ka_dance_7dl", ["ka","me"], False, False, False),
        sdl_gall_art("d3_sl_evening", ["sl","me"], False, False, False),
        sdl_gall_art("d3_un_forest", ["un","me"], False, False, False),
        sdl_gall_art("d3_us_library_3", ["us","me"], False, False, False, ["d3_us_library_4", "d4_us_morning"]),
        sdl_gall_art("d3_ussr_catched", ["us"], False, False, False),
        sdl_gall_art("d4_sl_un_catac_7dl", ["sl","un"], False, False, False, ["d4_catac", "d4_sl_catac_7dl"]),
        sdl_gall_art("d4_cs_car_day_cs_7dl", ["cs","ba"], True, False, False, ["d4_cs_car_open_7dl", "d4_cs_car_dark_7dl", "d4_cs_car_day_ba_gl_7dl", "d4_cs_car_day_cs_coat_7dl", "d4_cs_car_night_cs_7dl"]),
        sdl_gall_art("d4_dv_falls_7dl", ["dv","me"], False, False, False),
        sdl_gall_art("d4_un_falls_7dl", ["un","me"], False, False, False),
        sdl_gall_art("d6_mi_dv_concert_7dl", ["mi","dv"], True, False, False, ["d4_dv_concert_7dl"]),
        sdl_gall_art("d4_dv_mt", ["dv","mt","me"], False, False, False),
        sdl_gall_art("d4_el_wash", ["el"], False, False, False),
        sdl_gall_art("d7_dv", ["dv","me"], False, False, False),
        sdl_gall_art("d4_un_camping_7dl", ["un","me"], False, False, False),
        sdl_gall_art("d4_un_reject_7dl", ["un"], False, False, False, ["d5_un_pixies_7dl"]),
        sdl_gall_art("d4_hatch_night_7dl", [""], True, False, False, ["d4_hatch_night_open_7dl"]),
        sdl_gall_art("d4_mi_moon_dancing_7dl", ["mi"], False, False, False),
        sdl_gall_art("d4_mi_falls_7dl", ["mi","me"], True, False, False, ["d4_mi_falls2_7dl"]),
        sdl_gall_art("d4_mi_guitar", ["mi"], False, False, False, ["d4_mi_guitar_club_7dl", "d4_mi_guitar_moon_7dl"]),
        sdl_gall_art("d4_mi_hedgehod_night_7dl", ["mi","me"], True, False, False, ["d4_mi_hedgehod_day_7dl"]),
        sdl_gall_art("d4_kandji_7dl", [""], True, False, False),
        sdl_gall_art("d4_mi_sup_7dl", ["mi"], False, False, False),
        sdl_gall_art("d4_sh_met_7dl", ["sh","me"], False, False, False),
        sdl_gall_art("d4_sl_lookup_7dl", ["sl"], True, False, False),
        sdl_gall_art("d4_sl_lookup2_7dl", ["sl"], True, False, False),
        sdl_gall_art("d4_mt_board_7dl", ["mt"], True, False, False, ["d4_mt_board_7dl mt_normal", "d4_mt_board_7dl mt_normal2", "d4_mt_board_7dl mt_dontlike", "d4_mt_board_7dl mt_grin", "d4_mt_board_7dl mt_laugh", "d4_mt_board_7dl mt_smile", "d4_mt_board_7dl mt_smile2", "d4_mt_board_7dl mt_smile3"]),
        sdl_gall_art("d4_us_stardust_7dl", ["us"], True, False, False),
        sdl_gall_art("d4_volley_rage_7dl", ["un","ba","mt"], False, False, False),
        sdl_gall_art("d5_cake", ["dv","us","mt","un","me"], False, False, False),
        sdl_gall_art("d5_cs", ["cs"], False, True, False),
        sdl_gall_art("d5_dv_argue", ["dv","me"], False, False, False),
        sdl_gall_art("d5_dv_arm_7dl", ["dv","me"], True, False, False, ["d5_dv_arm_jojo_7dl"]),
        sdl_gall_art("d5_dream_7dl", [""], False, False, False),
        sdl_gall_art("d5_dv_island", ["dv","me"], False, False, False),
        sdl_gall_art("d5_dv_sleep_7dl", ["dv"], True, False, False, ["d5_dv_sleep2_7dl"]),
        sdl_gall_art("d5_dv_sleep_together_7dl", ["dv","me"], True, False, False, ["d5_dv_sleep_together2_7dl", "d5_dv_sleep_together3_7dl"]),
        sdl_gall_art("d5_alisa_7dl", [""], False, False, False),
        sdl_gall_art("d5_mi_conv_7dl", ["mi","me"], False, False, False),
        sdl_gall_art("d5_mt_redress_7dl", ["mt"], False, True, False),
        sdl_gall_art("d5_rainy_idle_7dl", [""], False, False, False),
        sdl_gall_art("d5_sh_us", ["sh","us"], False, False, False),
        sdl_gall_art("d5_sl_bed_7dl", ["sl"], False, False, False),
        sdl_gall_art("d5_un_bed_7dl", ["un"], False, False, False),
        sdl_gall_art("d7_mt_bed_7dl", ["mt"], False, False, False),
        sdl_gall_art("d5_sl_bench_day_7dl", ["sl","me"], True, False, False, ["d5_sl_bench_neutral_7dl", "d5_sl_bench_night_7dl"]),
        sdl_gall_art("d5_sl_hugs_7dl", ["sl","me"], True, False, False),
        sdl_gall_art("d5_sl_kissing_7dl", ["sl","me"], False, False, False),
        sdl_gall_art("d5_sl_moon_7dl", ["sl"], False, True, False),
        sdl_gall_art("d5_sl_piano_1_7dl", ["sl"], True, False, False, ["d5_sl_piano_2_7dl", "d5_sl_piano_3_7dl", "d5_sl_piano_4_7dl", "d5_sl_piano_5_7dl"]),
        sdl_gall_art("d5_snark_7dl", [""], True, False, False),
        sdl_gall_art("d5_square_sl_lead_7dl", ["sh","dv","us","un","mz","me","mt","sl"], True, False, False, ["d5_square_me_lead_7dl", "d5_square_us_lead_7dl"]),
        sdl_gall_art("d5_sl_swimming_7dl", ["sl"], False, True, False),
        sdl_gall_art("d5_un_carrier_7dl", ["un"], True, False, False),
        sdl_gall_art("d5_un_film_7dl", ["un","me"], False, False, False),
        sdl_gall_art("d5_us_old_photo_7dl", ["us"], False, False, False),
        sdl_gall_art("d5_thousand_twinkles_7dl", [""], True, False, False),
        sdl_gall_art("d5_twinkle_1_7dl", [""], True, False, False, ["d5_twinkle_2_7dl", "d5_twinkle_3_7dl", "d5_twinkle_4_7dl", "d5_twinkle_5_7dl", "d5_twinkle_6_7dl"]),
        sdl_gall_art("d5_un_island", ["un","me"], False, False, False, ["d5_un_island_dress_7dl"]),
        sdl_gall_art("d5_un_sleep", ["un","me"], False, False, False),
        sdl_gall_art("d5_us_ghost", ["us","me"], False, False, False),
        sdl_gall_art("d5_us_kiss_dress_7dl", ["us","me"], False, False, False),
        sdl_gall_art("d5_us_rendezvous_7dl", ["us","me"], True, False, False),
        sdl_gall_art("d5_us_sneakpeak_7dl", ["us"], True, False, False),
        sdl_gall_art("d5_us_sneakpeak2_7dl", ["me","us"], True, False, False, ["d5_us_sneakpeak2_2_7dl", "d5_us_sneakpeak2_3 _7dl", "d5_us_sneakpeak2_4_7dl"]),
        sdl_gall_art("d5_me_snch_run_7dl", ["me","ba"], True, False, False, ["d5_me_snch_run2_7dl", "d6_me_run_7dl", "d6_me_run2_7dl"]),
        sdl_gall_art("d6_disco2_7dl", ["un","us","dv","sl","mt"], False, False, False),
        sdl_gall_art("d6_dv_hentai_7dl", ["dv","me"], True, True, False),
        sdl_gall_art("d6_dv_hentai2_7dl", ["dv","me"], True, True, False),
        sdl_gall_art("d6_mi_farewell_7dl", ["mi"], False, False, False, ["d6_mi_cya_7dl"]),
        sdl_gall_art("d6_mi_departure_7dl", ["mi"], True, False, False),
        sdl_gall_art("d6_mi_hugs_7dl", ["mi","me"], True, False, False),
        sdl_gall_art("d6_mi_leaving_7dl", ["mi"], False, False, False),
        sdl_gall_art("d6_mi_morning_7dl", ["mi"], False, True, False),
        sdl_gall_art("d6_mi_salute_7dl", ["mi","me"], True, False, False, ["d6_mi_salute2_7dl"]),
        sdl_gall_art("d6_mi_swimming_7dl", ["mi"], False, True, False),
        sdl_gall_art("d6_mi_grass_7dl", ["mi","me"], False, False, 1.3),
        sdl_gall_art("d6_mt_salute_7dl", ["mt","me"], True, False, False),
        sdl_gall_art("d6_sl_clean_7dl", ["sl"], True, False, False, ["d6_sl_clean_dress_7dl", "d6_sl_clean_dress2_7dl"]),
        sdl_gall_art("d6_sl_dinner_7dl", ["dv","mi","sl","me","us","el"], True, False, False, ["d6_mi_dinner_7dl"]),
        sdl_gall_art("d6_sl_hentai_2", ["sl"], False, True, False),
        sdl_gall_art("d6_puppy_7dl", [""], True, False, False),
        sdl_gall_art("d6_sl_swim", ["sl"], False, True, False),
        sdl_gall_art("d6_sl_zettai_7dl", ["sl"], True, False, 1.3),
        sdl_gall_art("d6_un_evening_0_7dl", ["un"], False, False, False, ["d6_un_evening_0_1_7dl", "d6_un_evening_0_2_7dl", "d6_un_evening_2", "d6_un_evening_3_7dl"]),
        sdl_gall_art("d6_faceless_hands_7dl", [""], True, False, False, ["d6_faceless_hands2_7dl"]),
        sdl_gall_art("d6_un_death_7dl", ["un"], True, True, False),
        sdl_gall_art("d6_un_violence_7dl", ["un"], True, False, False, ["d6_un_violence2_7dl"]),
        sdl_gall_art("d6_us_dance_7dl", ["us","me"], True, False, False),
        sdl_gall_art("d6_us_ghost_7dl", ["us","me"], True, False, False, ["d6_us_ghost_hole_7dl", "d6_us_photo_7dl", "d6_us_photo_torn_7dl"]),
        sdl_gall_art("d6_us_kiss_7dl", ["us","me"], True, False, False),
        sdl_gall_art("d6_us_kiss2_7dl", ["us","dn"], True, False, False),
        sdl_gall_art("d6_me_cyberfish_7dl", ["me","sh","el"], True, False, False, ["d6_me_cyberfish_7dl el_cf_surp semen_cf_normal sh_cf_bore", "d6_me_cyberfish2_7dl el_cf_surp2 semen_cf_surp sh_cf_surp", "d6_me_cyberfish_7dl el_cf_happy semen_cf_surp sh_cf_smile", "d6_me_cyberfish_7dl el_cf_sad semen_cf_normal sh_cf_poker", "d6_me_cyberfish_7dl el_cf_sorrow semen_cf_normal sh_cf_poker", "d6_me_cyberfish_7dl el_cf_smile semen_cf_normal sh_cf_poker", "d6_me_cyberfish_7dl el_cf_smile2 semen_cf_normal sh_cf_smile", "d6_me_cyberfish_7dl el_cf_normal semen_cf_normal sh_cf_poker", "d6_me_cyberfish_7dl el_cf_surp3 semen_cf_normal sh_cf_surp", "d6_me_cyberfish_7dl el_cf_smile3 semen_cf_normal sh_cf_bore"]),
        sdl_gall_art("d6_am_aquasemen_7dl", ["am"], True, False, False),
        sdl_gall_art("d7_bus_night_7dl", [""], False, False, False),
        sdl_gall_art("d7_dv_addic_7dl", ["dv","me"], False, False, False),
        sdl_gall_art("d7_dv_child_7dl", ["dv","me"], True, False, False),
        sdl_gall_art("d7_dv_come_with_me_1_7dl", ["dv"], True, False, False, ["d7_dv_come_with_me_2_7dl"]),
        sdl_gall_art("d7_dv_epilogue_kiss_7dl", ["dv","me"], False, False, False),
        sdl_gall_art("d7_dv_epilogue_bus_7dl", ["dv","me"], True, False, False, ["d7_dv_epilogue_bus2_7dl"]),
        sdl_gall_art("d7_me_epilogue_bus_7dl", ["me"], True, False, False),
        sdl_gall_art("d7_mi_epilogue_bus_7dl", ["mi","me"], True, False, False, ["d7_mi_epilogue_bus2_7dl"]),
        sdl_gall_art("d7_mt_epilogue_bus_7dl", ["mt","me"], True, False, False, ["d7_mt_epilogue_bus2_7dl", "d7_mt_epilogue_bus3_7dl"]),
        sdl_gall_art("d7_sl_epilogue_bus_7dl", ["sl","me"], True, False, False, ["d7_sl_epilogue_bus2_7dl"]),
        sdl_gall_art("d7_un_epilogue_bus_7dl", ["un","me"], True, False, False, ["d7_un_epilogue_bus2_7dl"]),
        sdl_gall_art("d7_us_epilogue_bus_7dl", ["us","me"], True, False, False, ["d7_us_epilogue_bus2_7dl", "d7_us_epilogue_bus3_7dl"]),
        sdl_gall_art("d7_dv_hugs_7dl", ["dv","me"], True, False, False, ["d7_dv_hugs2_7dl", "d7_dv_hugs3_7dl", "d7_dv_hugs4_7dl"]),
        sdl_gall_art("d7_dv_loki_exc_7dl", ["dv"], False, False, False),
        sdl_gall_art("d7_dv_looney_7dl", ["dv","me"], True, False, False),
        sdl_gall_art("d7_dv_noir_7dl", ["dv"], False, False, False),
        sdl_gall_art("d7_dv_rf_reject_7dl", ["dv"], True, False, 0.7),
        sdl_gall_art("d7_dv_stars_7dl", ["dv"], False, False, False),
        sdl_gall_art("d7_me_frozen_7dl", ["me"], True, False, False),
        sdl_gall_art("d7_pioneers_leaving", ["sl","mt","sh","dv","us","me","un","el"], False, False, False, ["d7_leaving_no_sh_7dl", "d7_leaving_no_sl_7dl", "d7_leaving_no_sl_me_7dl"]),
        sdl_gall_art("d7_me_looney_7dl", ["me"], False, False, False),
        sdl_gall_art("d7_mi_club27_7dl", ["mi"], True, False, False),
        sdl_gall_art("d7_mi_concert2_7dl", ["mi"], False, False, False, ["d7_mi_concert_7dl"]),
        sdl_gall_art("d7_mi_epilogue_7dl", ["mi"], False, False, False, ["d7_mi_epilogue0_7dl"]),
        sdl_gall_art("d7_mi_farewell_7dl", ["mi"], False, False, False),
        sdl_gall_art("d7_mi_ghost_7dl", ["mi"], True, False, 0.71),
        sdl_gall_art("d7_mi_hugs_7dl", ["mi"], True, False, 0.56),
        sdl_gall_art("d7_mi_stroll_7dl", ["mi","me"], False, False, False),
        sdl_gall_art("d7_mi_letter_7dl", ["mi"], False, False, False, ["d7_mi_letter_rain_7dl", "d7_mi_letter_rain_tears_7dl"]),
        sdl_gall_art("d7_mi_lost_7dl", ["mi"], True, False, False, ["d7_mi_lost2_7dl"]),
        sdl_gall_art("d7_mi_meeting_7dl", ["mi"], False, False, False),
        sdl_gall_art("d7_mi_ramen_7dl", ["mi","me"], True, False, False),
        sdl_gall_art("d7_mi_reenter_7dl", ["mi","me"], True, False, False),
        sdl_gall_art("d7_mi_sparkle_7dl", ["mi","me"], True, False, False, ["d7_mi_sparkle_smile_7dl"]),
        sdl_gall_art("d7_mi_sunk_7dl", ["mi"], True, False, False),
        sdl_gall_art("d7_mt_epilogue_miracle_7dl", ["mt"], True, False, False),
        sdl_gall_art("d7_me_arseny_7dl", ["me"], True, False, False, ["d7_me_semen_7dl"]),
        sdl_gall_art("d7_mt_old_7dl", ["mt","me"], True, False, False, ["d7_mt_old2_7dl", "d7_mt_old3_7dl"]),
        sdl_gall_art("d7_sl_hug_7dl", ["sl","me"], True, False, False, ["d7_sl_hug2_7dl"]),
        sdl_gall_art("d7_un_cry_7dl", ["un"], True, False, False, ["d7_un_cry2_7dl"]),
        sdl_gall_art("d7_un_epilogue_7dl", ["un"], False, False, False),
        sdl_gall_art("d7_epilogue_fall_7dl", [""], False, False, False),
        sdl_gall_art("d7_un_epilogue_bad_7dl", ["un"], False, False, False),
        sdl_gall_art("d7_me_cosmonaut_7dl", ["me"], True, False, False),
        sdl_gall_art("d7_fire_7dl", [""], True, False, False),
        sdl_gall_art("d7_un_firebridge_7dl", ["un"], True, False, False, ["d7_un_firebridge2_7dl", "d7_un_firebridge3_7dl"]),
        sdl_gall_art("d7_un_fireyes_7dl", ["un"], True, False, False),
        sdl_gall_art("d7_un_epilogue_rf_7dl", ["un"], False, False, False),
        sdl_gall_art("d7_un_reanimation_7dl", ["un"], True, False, False),
        sdl_gall_art("d7_un_suicide", ["un"], False, False, 1.3),
        sdl_gall_art("d7_un_take_my_hand_7dl", ["un","me"], True, False, False),
        sdl_gall_art("d7_us_bedroom_7dl", ["us","dn"], True, False, False, ["d7_us_bedroom2_7dl", "d7_us_bedroom3_7dl", "d7_us_bedroom4_7dl"]),
        sdl_gall_art("d7_us_pixie_7dl", ["us"], True, False, False),
        sdl_gall_art("epilogue_un_bad", ["me"], False, False, False, ["d7_me_tai_tai_7dl"]),
        sdl_gall_art("epilogue_dv_2", [""], False, False, False),
        sdl_gall_art("epilogue_mi_1", ["mi","me"], False, False, False),
        sdl_gall_art("epilogue_mi_9", ["mi","me"], False, False, False),
        sdl_gall_art("epilogue_sl", ["sl"], False, False, False, ["epilogue_sl_2"])
        ]

    sdl_gall_girls_list = {'mi':[], 'dv':[], 'sl':[], 'un':[], 'mt':[], 'us':[]}
    sdl_gall_girls_list_orig = {'mi':[], 'dv':[], 'sl':[], 'un':[], 'mt':[], 'us':[]}
    for girl in sdl_gall_girls_list:
        for img in sdl_gall_arts_list:
            if girl in img.get_girls():
                sdl_gall_girls_list[girl].append(img)
                if img.get_orig():
                    sdl_gall_girls_list_orig[girl].append(img)

    sdl_gall_arts_list_orig = []
    for img in sdl_gall_arts_list:
        if img.get_orig():
            sdl_gall_arts_list_orig.append(img)

    sdl_gall_bgs_list_orig = []
    for img in sdl_gall_bgs_list:
        if img.get_orig():
            sdl_gall_bgs_list_orig.append(img)

init python:
    class sdl_gall_bg:
        def __init__(self, img, orig=False, add_img=[], vert=False, type="bg "):
            self.img = img
            self.orig = orig
            self.add_img = add_img
            self.vert = vert
            self.type = type

        def get_img(self):
            return self.img

        def get_orig(self):
            return self.orig

        def get_add_img(self):
            return self.add_img

        def get_vert(self):
            return self.vert

        def get_type(self):
            return self.type

    class sdl_gall_art:
        def __init__(self, img, girls=[], orig=False, hent=False, vert=False, add_img=[], type="cg "):
            self.img = img
            self.girls = girls
            self.orig = orig
            self.hent = hent
            self.vert = vert
            self.add_img = add_img
            self.type = type

        def get_img(self):
            return self.img

        def get_girls(self):
            return self.girls

        def get_orig(self):
            return self.orig

        def get_hent(self):
            return self.hent

        def get_vert(self):
            return self.vert

        def get_add_img(self):
            return self.add_img

        def get_type(self):
            return self.type

    def sdl_gal_check_seen(img):
        if renpy.seen_image(img.get_type()+img.get_img()):
            return True
        for i in img.get_add_img():
            if renpy.seen_image(img.get_type()+i):
                return True

    def sdl_gal_set_list():
        global sdl_gall_curr_list
        if sdl_gall_mode == "bgs":
            if sdl_gall_orig:
                sdl_gall_curr_list = sdl_gall_bgs_list_orig
            else:
                sdl_gall_curr_list = sdl_gall_bgs_list
        elif sdl_gall_mode == "arts":
            if sdl_gall_orig:
                sdl_gall_curr_list = sdl_gall_arts_list_orig
            else:
                sdl_gall_curr_list = sdl_gall_arts_list
        elif sdl_gall_mode in sdl_gall_girls_list:
            if sdl_gall_orig:
                sdl_gall_curr_list = sdl_gall_girls_list_orig[sdl_gall_mode]
            else:
                sdl_gall_curr_list = sdl_gall_girls_list[sdl_gall_mode]

    def sdl_gall_progress_calc():
        global sdl_gall_progress
        seen_count = 0.0
        img_count = 0.0
        for img in sdl_gall_bgs_list:
            if sdl_gal_check_seen(img):
                seen_count += 1
            img_count += 1
        for img in sdl_gall_arts_list:
            if sdl_gal_check_seen(img):
                seen_count += 1
            img_count += 1
        ratio = seen_count / img_count * 100
        sdl_gall_progress = round(ratio, 1)

init 1:
    image bg gallery_7dl = get_image_7dl("gui/gallery/gallery_bg.png")
    $ locked_img_7dl = ["gallery_stub_1.png", "gallery_stub_2.png", "gallery_stub_3.png"]

    $ sdl_gall_mode = ""
    $ sdl_gall_page = 1

    $ style.sdl_page_text = Style(style.default)
    $ style.sdl_page_text.font  = get_image_7dl("fonts/a_AvanteLtNr.ttf")
    $ style.sdl_page_text.color = "#ffffff"
    $ style.sdl_page_text.size = 60

    $ sdl_gall_sshow = False
    $ sdl_gall_orig = False
    $ sdl_gall_curr_list = []

screen sdl_gall_main:
    add get_image_7dl("gui/gallery/gallery_bg.png")

    if not sdl_gall_mode == "bgs":
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_bgs_%s.png") xalign 0.31 yalign 0.029
            action [SetVariable("sdl_gall_mode", "bgs"), SetVariable("sdl_gall_page", 1), Function(sdl_gal_set_list), Show("sdl_gall_photos", transition=Dissolve(0.2)), Show("sdl_gall_bw", transition=Dissolve(0.2)), Show("sdl_gall_fw", transition=Dissolve(0.2)), Show("sdl_gall_sshow", transition=Dissolve(0.2))]
    else:
        add get_image_7dl("gui/gallery/gallery_navig_bgs_hover.png") xalign 0.31 yalign 0.029
    if not sdl_gall_mode == "arts":
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_arts_%s.png") xalign 0.733 yalign 0.032
            action [SetVariable("sdl_gall_mode", "arts"), SetVariable("sdl_gall_page", 1), Function(sdl_gal_set_list), Show("sdl_gall_photos", transition=Dissolve(0.2)), Show("sdl_gall_bw", transition=Dissolve(0.2)), Show("sdl_gall_fw", transition=Dissolve(0.2)), Show("sdl_gall_sshow", transition=Dissolve(0.2))]
    else:
        add get_image_7dl("gui/gallery/gallery_navig_arts_hover.png") xalign 0.733 yalign 0.032
    if sdl_gall_mode not in ("bgs", "filter"):
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_filter_%s.png") xcenter 0.917 ycenter 0.148
            action [Hide("sdl_gall_sshow", transition=Dissolve(0.2)), Hide("sdl_gall_bw", transition=Dissolve(0.2)), Hide("sdl_gall_fw", transition=Dissolve(0.2)), SetVariable("sdl_gall_mode", "filter"), SetVariable("sdl_gall_page", 1), Show("sdl_gall_filter", transition=Dissolve(0.2))]
    if sdl_gall_mode == "filter":
        timer 0.01 action [Show("sdl_gall_filter", transition=Dissolve(0.2)), Show("sdl_gall_exit", transition=Dissolve(0.2))]
    else:
        timer 0.01 action [Function(sdl_gal_set_list), Show("sdl_gall_photos", transition=Dissolve(0.2)), Show("sdl_gall_bw", transition=Dissolve(0.2)), Show("sdl_gall_fw", transition=Dissolve(0.2)), Show("sdl_gall_sshow", transition=Dissolve(0.2)), Show("sdl_gall_exit", transition=Dissolve(0.2))]
        if not sdl_gall_orig:
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_orig_unch_%s.png") xcenter 0.08 ycenter 0.148
                action [SetVariable("sdl_gall_orig", True), SetVariable("sdl_gall_page", 1), Hide("sdl_gall_photos", transition=Dissolve(0.2)), Function(sdl_gal_set_list), Show("sdl_gall_photos", transition=Dissolve(0.2))]
        else:
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_orig_ch_%s.png") xcenter 0.08 ycenter 0.148
                action [SetVariable("sdl_gall_orig", False), SetVariable("sdl_gall_page", 1), Hide("sdl_gall_photos", transition=Dissolve(0.2)), Function(sdl_gal_set_list), Show("sdl_gall_photos", transition=Dissolve(0.2))]
        text "ОРИГИНАЛЬНЫЕ\nАРТЫ":
            text_align 0.5
            xcenter 0.08
            ycenter 0.23
            color "#fff"
            font get_image_7dl("fonts/a_AvanteLtNr.ttf")
            size 45

    # Панелька плеера
    if sdl_mus_engine.is_active:
        use music_panel_7dl(default_music=music_7dl["more_than_alive"])

screen sdl_gall_exit:
    if sdl_gall_sshow:
        imagebutton:
            if persistent.stream_mode:
                auto get_image_7dl("gui/gallery/gallery_navig_exit_a_%s.png") xalign 0.029 yalign 0.971
            else:
                auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xalign 0.029 yalign 0.971
            action [Hide("sdl_gall_exit", transition=Dissolve(0.2)), SetVariable("sdl_gall_sshow", False), Jump("sdl_gall_continue")]
    elif sdl_gall_mode == "filter":
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xalign 0.029 yalign 0.971
            action [Hide("sdl_gall_filter", transition=Dissolve(0.2)), Hide("sdl_gall_exit", transition=Dissolve(0.2)), SetVariable("sdl_gall_mode", ""), SetVariable("sdl_gall_page", 1), Jump("main_menu_7dl")]
    else:
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xalign 0.029 yalign 0.971
            action [Hide("sdl_gall_photos", transition=Dissolve(0.2)), Hide("sdl_gall_bw", transition=Dissolve(0.2)), Hide("sdl_gall_fw", transition=Dissolve(0.2)), Hide("sdl_gall_sshow", transition=Dissolve(0.2)), Hide("sdl_gall_exit", transition=Dissolve(0.2)), SetVariable("sdl_gall_mode", ""), SetVariable("sdl_gall_page", 1), Jump("main_menu_7dl")]

screen sdl_gall_bw:
    if sdl_gall_page > 1:
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_backward_%s.png") xalign 0.045 yalign 0.5
            action [SetVariable("sdl_gall_page", sdl_gall_page-1), Hide("sdl_gall_photos", transition=Dissolve(0.2)), Function(sdl_gal_set_list), Show("sdl_gall_photos", transition=Dissolve(0.2))]

screen sdl_gall_fw:
    if sdl_gall_page < ((len(sdl_gall_curr_list) - 1) // 6 + 1):
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_forward_%s.png") xalign 0.957 yalign 0.5
            action [SetVariable("sdl_gall_page", sdl_gall_page+1), Hide("sdl_gall_photos", transition=Dissolve(0.2)), Function(sdl_gal_set_list), Show("sdl_gall_photos", transition=Dissolve(0.2))]

screen sdl_gall_filter:
    tag menu
    $ sdl_gall_filter_imgs = {"mi": ["Мику", "d6_mi_hugs_7dl"], "dv": ["Алиса", "d7_dv_hugs_7dl"], "sl": ["Славя", "d7_sl_hug_7dl"], "un": ["Лена", "d3_un_dance2_7dl"], "mt": ["Ольга", "d2_mt_resort_7dl"], "us": ["Ульяна", "d6_us_dance_7dl"]}
    $ sdl_gall_img_count = 0
    for char in sdl_gall_filter_imgs:
        imagebutton:
            idle get_image_7dl("gui/gallery/arts/"+sdl_gall_filter_imgs[char][1]+"_idle.png") xalign (0.2 + 0.3 * (sdl_gall_img_count % 3)) yalign (0.15 if sdl_gall_img_count < 3 else 0.93)
            action [Hide("sdl_gall_filter", transition=Dissolve(0.2)), Hide("sdl_gall_bw", transition=Dissolve(0.2)), Hide("sdl_gall_fw", transition=Dissolve(0.2)), SetVariable("sdl_gall_mode", char), SetVariable("sdl_gall_page", 1), Function(sdl_gal_set_list), Show("sdl_gall_photos", transition=Dissolve(0.2)), Show("sdl_gall_bw", transition=Dissolve(0.2)), Show("sdl_gall_fw", transition=Dissolve(0.2))]
        text sdl_gall_filter_imgs[char][0]:
            text_align 0.5
            xcenter (0.26 + 0.24 * (sdl_gall_img_count % 3))
            ycenter (0.45 if sdl_gall_img_count < 3 else 0.91)
            style "replays_textbutton"
            color "#2f059a"
        $ sdl_gall_img_count += 1

screen sdl_gall_sshow:
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_navig_slide_show_%s.png") xcenter 1761 ycenter 280
        action [Hide("sdl_gall_photos", transition=Dissolve(0.2)), Hide("sdl_gall_bw", transition=Dissolve(0.2)), Hide("sdl_gall_fw", transition=Dissolve(0.2)), Hide("sdl_gall_sshow", transition=Dissolve(0.2)), Jump("sdl_gall_sshow_imgs")]

screen sdl_gall_photos:
    tag menu
    text "ОТКРЫТО\nАРТОВ: [sdl_gall_progress]%":
        text_align 0.5
        xcenter 0.08
        ycenter 0.63
        color "#fff"
        font get_image_7dl("fonts/a_AvanteLtNr.ttf")
        size 45
    $ sdl_gall_img_count = 0
    if sdl_gall_mode == "bgs":
        textbutton str(sdl_gall_page)+" / "+str(((len(sdl_gall_curr_list) - 1) // 6 + 1)):
            text_style "sdl_page_text"
            style "sdl_page_text"
            xalign 0.95
            yalign 0.95
        for img in sdl_gall_curr_list[sdl_gall_page*6-6:sdl_gall_page*6]:
            if sdl_gal_check_seen(img):
                imagebutton:
                    auto get_image_7dl("gui/gallery/bgs/"+img.get_img()+"_%s.png") xalign (0.2 + 0.3 * (sdl_gall_img_count % 3)) yalign (0.15 if sdl_gall_img_count < 3 else 0.93)
                    action [Hide("sdl_gall_photos", transition=Dissolve(0.2)), Hide("sdl_gall_bw", transition=Dissolve(0.2)), Hide("sdl_gall_fw", transition=Dissolve(0.2)), Hide("sdl_gall_sshow", transition=Dissolve(0.2)), Hide("sdl_gall_exit", transition=Dissolve(0.2)), Call("sdl_gall_show_imgs", img)]
            else:
                add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign (0.2 + 0.3 * (sdl_gall_img_count % 3)) yalign (0.15 if sdl_gall_img_count < 3 else 0.93)
            $ sdl_gall_img_count += 1
    elif (sdl_gall_mode == "arts") or (sdl_gall_mode in sdl_gall_girls_list):
        textbutton str(sdl_gall_page)+" / "+str(((len(sdl_gall_curr_list) - 1) // 6 + 1)):
            text_style "sdl_page_text"
            style "sdl_page_text"
            xalign 0.95
            yalign 0.95
        for img in sdl_gall_curr_list[sdl_gall_page*6-6:sdl_gall_page*6]:
            if sdl_gal_check_seen(img) and (persistent.hentai_graphics_7dl or (not img.get_hent())):
                imagebutton:
                    auto get_image_7dl("gui/gallery/arts/"+img.get_img()+"_%s.png") xalign (0.2 + 0.3 * (sdl_gall_img_count % 3)) yalign (0.15 if sdl_gall_img_count < 3 else 0.93)
                    action [Hide("sdl_gall_photos", transition=Dissolve(0.2)), Hide("sdl_gall_bw", transition=Dissolve(0.2)), Hide("sdl_gall_fw", transition=Dissolve(0.2)), Hide("sdl_gall_sshow", transition=Dissolve(0.2)), Hide("sdl_gall_exit", transition=Dissolve(0.2)), Call("sdl_gall_show_imgs", img)]
            else:
                add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign (0.2 + 0.3 * (sdl_gall_img_count % 3)) yalign (0.15 if sdl_gall_img_count < 3 else 0.93)
            $ sdl_gall_img_count += 1

label sdl_gall_start:
    $ make_names_known_7dl()
    $ sdl_gall_progress_calc()
    if not sdl_mus_engine.is_active:
        play music music_7dl["more_than_alive"] fadein 3
    scene bg gallery_7dl with fade
    $ sdl_gall_mode = "arts"
    $ renpy.block_rollback()
    call screen sdl_gall_main

label sdl_gall_continue:
    scene bg gallery_7dl with dissolve
    $ renpy.block_rollback()
    call screen sdl_gall_main

label sdl_gall_show_imgs(img):
    python:
        if renpy.seen_image(img.get_type()+img.get_img()):
            renpy.scene()
            if img.get_vert():
                sdl_gall_vert_ratio = img.get_vert()
                renpy.show(img.get_type()+img.get_img(), at_list=[bottotop])
            else:
                renpy.show(img.get_type()+img.get_img(), at_list=[normal_gallery])
            renpy.with_statement(fade)
            renpy.pause()
        if img.get_add_img():
            for i in img.get_add_img():
                if renpy.seen_image(img.get_type()+i):
                    renpy.scene()
                    if img.get_vert():
                        sdl_gall_vert_ratio = img.get_vert()
                        renpy.show(img.get_type()+i, at_list=[bottotop])
                    else:
                        renpy.show(img.get_type()+i, at_list=[normal_gallery])
                    renpy.with_statement(fade)
                    renpy.pause()
        renpy.show("bg black")
    jump sdl_gall_continue

label sdl_gall_sshow_imgs:
    $ sdl_gall_sshow = True
    python:
        if sdl_gall_mode == "arts" or (sdl_gall_mode in sdl_gall_girls_list):
            for img in sdl_gall_curr_list:
                if (renpy.seen_image(img.get_type()+img.get_img())) and (persistent.hentai_graphics_7dl or (not img.get_hent())):
                    renpy.scene()
                    if img.get_vert():
                        sdl_gall_vert_ratio = img.get_vert()
                        renpy.show(img.get_type()+img.get_img(), at_list=[bottotop])
                        renpy.with_statement(fade)
                        renpy.pause(round(6.72/sdl_gall_vert_ratio, 1))
                    else:
                        renpy.show(img.get_type()+img.get_img(), at_list=[normal_gallery])
                        renpy.with_statement(fade)
                        if persistent.stream_mode:
                            renpy.pause(15)
                        else:
                            renpy.pause(4)
        elif sdl_gall_mode == "bgs":
            for img in sdl_gall_curr_list:
                if renpy.seen_image(img.get_type()+img.get_img()):
                    renpy.scene()
                    renpy.show(img.get_type()+img.get_img(), at_list=[normal_gallery])
                    renpy.with_statement(fade)
                    if persistent.stream_mode:
                        renpy.pause(15)
                    else:
                        renpy.pause(4)
    if persistent.stream_mode:
        jump sdl_gall_sshow_imgs
    else:
        hide screen sdl_gall_exit
        $ sdl_gall_sshow = False
        jump sdl_gall_continue
