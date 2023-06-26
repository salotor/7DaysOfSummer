init 999:

    # neko
    image sl neko veryfar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_neko.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_neko.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_neko.png")) )

    image dv neko veryfar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/dv/dv_neko.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/dv/dv_neko.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/dv/dv_neko.png")) )

    image un neko veryfar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/un/un_neko.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/un/un_neko.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/un/un_neko.png")) )

    image mi neko veryfar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/mi/mi_neko.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/mi/mi_neko.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/mi/mi_neko.png")) )

    # sl
    image sl pioneer normal veryfar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_1_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_1_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_1_normal.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_1_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_1_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_1_normal.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_1_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_1_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_1_normal.png")) )

    image sl pioneer serious veryfar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_1_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_1_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_1_serious.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_1_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_1_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_1_serious.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_1_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_1_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_1_serious.png")) )

    image sl pioneer scared veryfar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_4_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_4_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_4_scared.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_4_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_4_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_4_scared.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_4_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_4_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_4_scared.png")) )

    image sl pioneer surprise veryfar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_3_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_3_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_3_surprise.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_3_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_3_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_3_surprise.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_3_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_3_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sl/sl_3_surprise.png")) )

    # un
    image un pioneer normal veryfar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/un/un_1_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_1_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_1_normal.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/un/un_1_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_1_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_1_normal.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/un/un_1_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_1_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_1_normal.png")) )

    image un pioneer scared veryfar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/un/un_2_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_2_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_2_scared.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/un/un_2_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_2_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_2_scared.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/un/un_2_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_2_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_2_scared.png")) )

    image un pioneer shocked veryfar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/un/un_2_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_2_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_2_shocked.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/un/un_2_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_2_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_2_shocked.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/un/un_2_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_2_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_2_shocked.png")) )

    image un pioneer serious veryfar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/un/un_3_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_3_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_3_serious.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/un/un_3_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_3_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_3_serious.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/un/un_3_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_3_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_3_serious.png")) )

    image un pioneer evilsmile veryfar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/un/un_1_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_1_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_1_evil_smile.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/un/un_1_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_1_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_1_evil_smile.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/un/un_1_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_1_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_1_evil_smile.png")) )

    image un pioneer shy veryfar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/un/un_1_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_1_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_1_shy.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/un/un_1_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_1_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_1_shy.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/un/un_1_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_1_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_1_shy.png")) )

    image un pioneer surprise veryfar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/un/un_2_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_2_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_2_surprise.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/un/un_2_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_2_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_2_surprise.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/un/un_2_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_2_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/un/un_2_surprise.png")) )

    # el
    image el pioneer slap = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), get_image_uvao_7dl("sprites/normal/el/el_2_body.png"),(0,0), get_image_uvao_7dl("sprites/normal/el/el_2_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/normal/el/el_slap.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), get_image_uvao_7dl("sprites/normal/el/el_2_body.png"),(0,0), get_image_uvao_7dl("sprites/normal/el/el_2_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/normal/el/el_slap.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), get_image_uvao_7dl("sprites/normal/el/el_2_body.png"),(0,0), get_image_uvao_7dl("sprites/normal/el/el_2_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/normal/el/el_slap.png")) )

    image el pioneer normal veryfar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/el/el_1_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/el/el_1_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/el/el_1_normal.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/el/el_1_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/el/el_1_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/el/el_1_normal.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/el/el_1_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/el/el_1_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/el/el_1_normal.png")) )

    image el pioneer scared veryfar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/el/el_2_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/el/el_2_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/el/el_2_scared.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/el/el_2_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/el/el_2_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/el/el_2_scared.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/el/el_2_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/el/el_2_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/el/el_2_scared.png")) )

    image el pioneer sad veryfar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/el/el_2_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/el/el_2_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/el/el_2_sad.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/el/el_2_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/el/el_2_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/el/el_2_sad.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/el/el_2_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/el/el_2_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/el/el_2_sad.png")) )

    image el pioneer surprise veryfar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/el/el_2_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/el/el_2_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/el/el_2_surprise.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/el/el_2_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/el/el_2_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/el/el_2_surprise.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/el/el_2_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/el/el_2_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/el/el_2_surprise.png")) )

    # sh
    image sh pioneer rage veryfar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/sh/sh_2_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sh/sh_2_rage.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/sh/sh_2_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sh/sh_2_rage.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/sh/sh_2_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sh/sh_2_rage.png")) )

    image sh pioneer scared veryfar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/sh/sh_1_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sh/sh_1_scared.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/sh/sh_1_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sh/sh_1_scared.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/sh/sh_1_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/sh/sh_1_scared.png")) )

    image sh angry bar close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), get_image_uvao_7dl("sprites/close/sh/sh_angry_bar.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), get_image_uvao_7dl("sprites/close/sh/sh_angry_bar.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), get_image_uvao_7dl("sprites/close/sh/sh_angry_bar.png")) )

    image sh angry bar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), get_image_uvao_7dl("sprites/normal/sh/sh_angry_bar.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), get_image_uvao_7dl("sprites/normal/sh/sh_angry_bar.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), get_image_uvao_7dl("sprites/normal/sh/sh_angry_bar.png")) )

    image sh angry bar far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), get_image_uvao_7dl("sprites/far/sh/sh_angry_bar.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), get_image_uvao_7dl("sprites/far/sh/sh_angry_bar.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), get_image_uvao_7dl("sprites/far/sh/sh_angry_bar.png")) )

    image sh angry bar veryfar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/sh/sh_angry_bar.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/sh/sh_angry_bar.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/sh/sh_angry_bar.png")) )

    image sh angry bar3 = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), get_image_uvao_7dl("sprites/normal/sh/sh_angry_bar3.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), get_image_uvao_7dl("sprites/normal/sh/sh_angry_bar3.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), get_image_uvao_7dl("sprites/normal/sh/sh_angry_bar3.png")) )

    image sh angry bar3 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), get_image_uvao_7dl("sprites/far/sh/sh_angry_bar3.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), get_image_uvao_7dl("sprites/far/sh/sh_angry_bar3.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), get_image_uvao_7dl("sprites/far/sh/sh_angry_bar3.png")) )

    image sh angry bar3 veryfar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/sh/sh_angry_bar3.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/sh/sh_angry_bar3.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/sh/sh_angry_bar3.png")) )

    image sh angry bar2 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), get_image_uvao_7dl("sprites/close/sh/sh_angry_bar2.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), get_image_uvao_7dl("sprites/close/sh/sh_angry_bar2.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), get_image_uvao_7dl("sprites/close/sh/sh_angry_bar2.png")) )

    image sh mad bar2 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), get_image_uvao_7dl("sprites/close/sh/sh_angry_bar2.png"), (0,0), get_image_uvao_7dl("sprites/close/sh/sh_mad_smile.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), get_image_uvao_7dl("sprites/close/sh/sh_angry_bar2.png"), (0,0), get_image_uvao_7dl("sprites/close/sh/sh_mad_smile.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), get_image_uvao_7dl("sprites/close/sh/sh_angry_bar2.png"), (0,0), get_image_uvao_7dl("sprites/close/sh/sh_mad_smile.png")) )

    # mt
    image mt pioneer angry veryfar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_2_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_2_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_2_angry.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_2_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_2_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_2_angry.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_2_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_2_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_2_angry.png")) )

    image mt pioneer normal veryfar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_1_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_1_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_1_normal.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_1_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_1_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_1_normal.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_1_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_1_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_1_normal.png")) )

    image mt pioneer scared3 veryfar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_3_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_3_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_3_scared3.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_3_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_3_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_3_scared3.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_3_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_3_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_3_scared3.png")) )

    image mt pioneer surprise veryfar = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_1_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_1_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_1_surprise.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_1_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_1_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_1_surprise.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((500,1080), (0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_1_body.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_1_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/veryfar/mt/mt_1_surprise.png")) )

    image mt scared3 panama pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), get_image_uvao_7dl("sprites/normal/mt/mt_3_body.png"),(0,0), get_image_uvao_7dl("sprites/normal/mt/mt_3_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/normal/mt/mt_3_scared3.png"),(0,0), get_image_uvao_7dl("sprites/normal/mt/mt_3_panama.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), get_image_uvao_7dl("sprites/normal/mt/mt_3_body.png"),(0,0), get_image_uvao_7dl("sprites/normal/mt/mt_3_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/normal/mt/mt_3_scared3.png"),(0,0), get_image_uvao_7dl("sprites/normal/mt/mt_3_panama.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), get_image_uvao_7dl("sprites/normal/mt/mt_3_body.png"),(0,0), get_image_uvao_7dl("sprites/normal/mt/mt_3_pioneer.png"),(0,0), get_image_uvao_7dl("sprites/normal/mt/mt_3_scared3.png"),(0,0), get_image_uvao_7dl("sprites/normal/mt/mt_3_panama.png")) )

    # cs
    image cs normal2 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), get_image_uvao_7dl("sprites/close/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/close/cs/cs_1_normal.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), get_image_uvao_7dl("sprites/close/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/close/cs/cs_1_normal.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), get_image_uvao_7dl("sprites/close/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/close/cs/cs_1_normal.png")) )

    image cs normal2 = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), get_image_uvao_7dl("sprites/normal/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/normal/cs/cs_1_normal.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), get_image_uvao_7dl("sprites/normal/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/normal/cs/cs_1_normal.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), get_image_uvao_7dl("sprites/normal/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/normal/cs/cs_1_normal.png")) )

    image cs normal2 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), get_image_uvao_7dl("sprites/far/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/far/cs/cs_1_normal.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), get_image_uvao_7dl("sprites/far/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/far/cs/cs_1_normal.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), get_image_uvao_7dl("sprites/far/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/far/cs/cs_1_normal.png")) )

    image cs smile2 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), get_image_uvao_7dl("sprites/close/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/close/cs/cs_1_smile.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), get_image_uvao_7dl("sprites/close/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/close/cs/cs_1_smile.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), get_image_uvao_7dl("sprites/close/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/close/cs/cs_1_smile.png")) )

    image cs smile2 = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), get_image_uvao_7dl("sprites/normal/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/normal/cs/cs_1_smile.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), get_image_uvao_7dl("sprites/normal/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/normal/cs/cs_1_smile.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), get_image_uvao_7dl("sprites/normal/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/normal/cs/cs_1_smile.png")) )

    image cs smile2 far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), get_image_uvao_7dl("sprites/far/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/far/cs/cs_1_smile.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), get_image_uvao_7dl("sprites/far/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/far/cs/cs_1_smile.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), get_image_uvao_7dl("sprites/far/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/far/cs/cs_1_smile.png")) )

    image cs badgirl2 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), get_image_uvao_7dl("sprites/close/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/close/cs/cs_2_badgirl.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), get_image_uvao_7dl("sprites/close/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/close/cs/cs_2_badgirl.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), get_image_uvao_7dl("sprites/close/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/close/cs/cs_2_badgirl.png")) )

    image cs badgirl2 = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), get_image_uvao_7dl("sprites/normal/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/normal/cs/cs_2_badgirl.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), get_image_uvao_7dl("sprites/normal/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/normal/cs/cs_2_badgirl.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), get_image_uvao_7dl("sprites/normal/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/normal/cs/cs_2_badgirl.png")) )

    image cs shy2 close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), get_image_uvao_7dl("sprites/close/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/close/cs/cs_1_shy.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), get_image_uvao_7dl("sprites/close/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/close/cs/cs_1_shy.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), get_image_uvao_7dl("sprites/close/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/close/cs/cs_1_shy.png")) )

    image cs badgirl2 glasses = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), get_image_uvao_7dl("sprites/normal/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/normal/cs/cs_2_badgirl.png"), (0,0), get_image_uvao_7dl("sprites/normal/cs/cs_1_glasses.png")), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), get_image_uvao_7dl("sprites/normal/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/normal/cs/cs_2_badgirl.png"), (0,0), get_image_uvao_7dl("sprites/normal/cs/cs_1_glasses.png")), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), get_image_uvao_7dl("sprites/normal/cs/cs_2_body.png"), (0,0), get_image_uvao_7dl("sprites/normal/cs/cs_2_badgirl.png"), (0,0), get_image_uvao_7dl("sprites/normal/cs/cs_1_glasses.png")) )
