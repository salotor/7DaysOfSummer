label alt_day4_me_no_vars:
    $ alt_no_un = 0
    $ alt_no_ammo = 0
    $ alt_no_weapon = 0
    $ alt_no_clue = 0
    return

label alt_day4_no_start:
    call alt_day4_me_no_vars
    $ noir_interface_on()
    $ noir_interface = True
    $ routetag = "Noir"
    $ plthr = "Нуар"
    $ alt_chapter(4, u"Долгий вечер")

    call alt_day4_no_begin
    pause(1)
    call alt_day4_no_trip
    pause(1)
    call alt_day4_no_passion
    pause(1)
    call alt_day4_no_corpse
    pause(1)
    call alt_day4_no_witch
    pause(1)
    call alt_day4_no_expo2
    pause(1)
    call alt_day4_no_rendezvous
    pause(1)
    call alt_day4_no_cop
    pause(1)

    $ noir_interface_off()
    $ noir_interface = False
    if not persistent.pivo_default_7dl:
        jump alt_stories_start
    else:
        return