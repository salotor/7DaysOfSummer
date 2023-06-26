init:
    image anim_noir: # белый шум с заставкой
        get_image_7dl("bg/ext_noir1_7dl.png")
        pause 0.14
        get_image_7dl("bg/ext_noir2_7dl.png")
        pause 0.14
        get_image_7dl("bg/ext_noir3_7dl.png")
        pause 0.14
        repeat

# Нуар
    image noir_bus_7dl = im.Grayscale("images/misc/op/back.jpg")
    image noir_cs_cg_7dl = im.Grayscale(get_image_7dl("cg/d4_cs_car_day_cs_coat_7dl.jpg"))
    image noir_khruschevka_day_7dl = im.Grayscale(get_image_7dl("bg/ext_khruschevka_day_7dl.jpg"))
    image noir_mt_sam_room_close_7dl = im.Grayscale(get_image_7dl("bg/int_mt_sam_room_close_7dl.jpg"))
    image noir_townscape_ph_day_7dl = im.Grayscale(get_image_7dl("bg/ext_townscape_ph_day_7dl.jpg"))
