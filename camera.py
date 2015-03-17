import pygame

def calculate_offset(ship_x,ship_y,old_off_x,old_off_y):

    if ship_x > 650 and ship_y > 250 and ship_x < 2560 - (1360 - 650) and ship_y < 1600 - ( 518 - 250) :
        off_x = -(ship_x - 650)
        off_y = -(ship_y - 250)
    # the following two statements could be concetenated,but in this way it's
    # easier to understand
    #--------------CHECKING CORNERS AND SIDES------------
    # checking corners first
    # left top corner
    if ship_x <= 650 and ship_y <= 250:
        off_x = 0
        off_y = 0
    # right top corner
    elif ship_x >= 2560- ( 1370 - 650) and ship_y <= 250 :
        off_x = old_off_x
        off_y = old_off_y
    # bottom right corner
    elif ship_x >= 2560 - (1370 - 650) and ship_y >= 1600 - ( 518 - 250):
        off_x = old_off_x
        off_y = old_off_y
    # bottom left corner
    elif ship_x <= 650 and ship_y >= 1600 - ( 518 - 250):
        off_x = 0
        off_y = old_off_y
    # left side 
    elif ship_x <= 650 :
        off_x = 0
        off_y = -(ship_y - 250)
    # top side
    elif ship_y <= 250 :
        off_x = -(ship_x - 650)
        off_y = 0
    # right side
    elif ship_x >= 2560 - ( 1370 - 650):
        off_x = old_off_x
        off_y = -(ship_y - 250)
    elif ship_y >= 1600 - ( 518 - 250):
        off_x = -(ship_x - 650)
        off_y = old_off_y

    #--------------END CHECKING CORNERS AND SIDES----------

    return off_x,off_y
