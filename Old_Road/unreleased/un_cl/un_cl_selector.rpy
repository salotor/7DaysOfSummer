init:
    $ path_un_cl = default_7dl_path + "Old_Road/unreleased/un_cl/"

    image ba mil = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), path_un_cl + 'Images/ba_mil.png', (0, 0), path_un_cl + 'Images/ba_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), path_un_cl + 'Images/ba_mil.png', (0, 0), path_un_cl + 'Images/ba_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), path_un_cl + 'Images/ba_mil.png', (0, 0), path_un_cl + 'Images/ba_normal.png'))

label alt_un_cl_selector_caller:
    $ renpy.block_rollback()
    play music music_7dl["exodus"] fadein 3
    scene cg d3_me_fag_room_7dl with dissolve
    call screen alt_un_cl_selector

screen alt_un_cl_selector:
    tag menu
    modal False
    imagebutton:
        auto path_un_cl + "Images/day3_un_cl_%s.png" xpos 0 ypos 0
        hovered [ShowTransient("matrix", transition=Dissolve(0.5)), Function(renpy.show, "zzz", what = "bg ext_sandpit_day_7dl"), Function(renpy.show, "sss", what = "un "+" "+renpy.random.choice(['angry','evil_smile','normal','normal2','shy','silent_angry','smile','smile2','snide_smile','sorrow','shy_smile','close_eyes_cry','cry','cry_smile','sad','scared','shocked','surprise','angry2','close_eye','grin','happy','laugh','rage','serious','smile3'])+" "+renpy.random.choice(['pioneer','dress','sport']), at_list = [left])]
        unhovered [Hide("matrix", transition=Dissolve(1.0)), Function(renpy.hide, "zzz"), Function(renpy.hide, "sss")]
        action [Hide("alt_un_cl_selector", transition=Dissolve(0.5)), Jump("alt_day3_un_cl_start_day")]
    imagebutton:
        auto path_un_cl + "Images/day4_un_cl_%s.png" xpos 960 ypos 0
        hovered [ShowTransient("matrix", transition=Dissolve(0.5)), Function(renpy.show, "zzz", what = "cg d7_me_jeep_7dl"), Function(renpy.show, "sss", what = "un2 "+" "+renpy.random.choice(['angry','evil_smile','normal','normal2','shy','silent_angry','smile','smile2','snide_smile','sorrow','shy_smile','close_eyes_cry','cry','cry_smile','sad','scared','shocked','surprise','angry2','close_eye','grin','happy','laugh','rage','serious','smile3'])+" "+renpy.random.choice(['casual','winter']), at_list = [right])]
        unhovered [Hide("matrix", transition=Dissolve(1.0)), Function(renpy.hide, "zzz"), Function(renpy.hide, "sss")]
        action [Hide("alt_un_cl_selector", transition=Dissolve(0.5)), Jump("alt_day4_un_cl_start")]
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xcenter 131 ycenter 994
        hovered [NullAction()]
        unhovered [NullAction()]
        action [Jump("alt_stories_start")]


screen matrix:
    add path_un_cl + "Images/matrix.png" xpos 0 ypos 0