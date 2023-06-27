label alt_1974_start:
    scene black with fade3
    "КЖППДПП"
    pause(1)
    if not persistent.pivo_default_7dl:
        jump alt_stories_start
    else:
        return
