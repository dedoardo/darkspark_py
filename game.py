import pygame
import ship
import user_interface as u_interface
import camera
import game_interface
import time as pytime
import enemy
import collision
import menu
import pickle
import load
import copy

# this simple function restarts the game by
# creating new class istances
def game_restart():
    player_ship_class.restart()
    computer_ships_class.restart()

pygame.init()

# screen init
screen = pygame.display.set_mode((1366,768),0,32)
clock = pygame.time.Clock()


# background img
background_img = pygame.image.load('images/wide_bg2.jpg').convert()
fight_zone = pygame.Surface((background_img.get_width(),
                             background_img.get_height()))

# the screen is split into user interface and the actual ship zone
main_window = pygame.Surface((1370,518))
user_interface = pygame.Surface((1370,250))

# some constants and variables we need
MAX_FPS = 120
off_x = 0
off_y = 0
movement_direction = 0
rotation_direction = 0
steering_direction = 0
fire_time = 0
start_time = pytime.time()
begin = pytime.time()
now = 0
t_1 = 0
comp_fire_time = 0
shield_regeneration_time = 0
# this variable will keep track of the game state
game_state = "main_menu"

# class initialization
player_ship_class = ship.Player_Ship()
computer_ships_class = enemy.Enemy_Ships(player_ship_class)
user_interface_class = u_interface.Interface(1366,768,player_ship_class,
                                             computer_ships_class)
minimap_class = game_interface.Minimap(player_ship_class,
                                       background_img,
                                       computer_ships_class)
collision_class = collision.Collision_Detection(player_ship_class,
                                                computer_ships_class)
main_menu = menu.Main_Menu(computer_ships_class,player_ship_class)
highscores = load.Highscores()
game_saves = load.Load_Game()

while True :

    # INCREASING DIFFICULTY by 0.1 each 30 seconds
    now = pytime.time() - begin
    if now >= 15 :
        computer_ships_class.difficulty += 0.1
        begin = pytime.time()
    # CHECKING THE GAME STATE
    if game_state == "new_game":
        game_state = "game"
        game_restart()
    if game_state == "main_menu" :
        game_state = main_menu.blit_main_menu(screen,game_state)
        continue
    if game_state == "highscores":
        game_state = highscores.blit_highscores(screen,game_state)
        continue
    if game_state == "game_over":
        overall_time = pytime.time() - start_time
        game_state = main_menu.blit_game_over(screen,game_state,overall_time)
        game_restart()
        continue
    if game_state == "pause":
        game_state = main_menu.pause_menu(screen,game_state)
    if game_state == "save_game":
        game_state = game_saves.save_game(player_ship_class,
                                            computer_ships_class,game_state)
        continue
    if game_state == "load_game":
        game_state,computer_ships_class,player_ship_class = game_saves.load_game(
                                player_ship_class,
                                computer_ships_class,
                                game_state)
        continue
    if player_ship_class.is_dead() == True:
        print "DEAD"
        game_state = "game_over"
        continue
    

    # --------------TIME VARIABLES-------
    bullet_time = clock.tick(200)
    fire_time += clock.tick(200)
    time = clock.tick(200)
    comp_fire_time += clock.tick(200)
    shield_regeneration_time += clock.tick(200)
    # ---------------END TIME VARIABLES---------
    # --------------SCREEN BLITTING--------------
    # The screen blits the main_window and the user_interface than
    # that blit their own stuff
    screen.fill((0,0,0))
    
    screen.blit(main_window,(0,0))
    screen.blit(user_interface,(0,518))

    # updating the user interface i'm using the screen because it's easier
    user_interface_class.update(screen)

    # now the main_window blits the background and all his stuffs
    # calculating the offset
    off_x,off_y = camera.calculate_offset(player_ship_class.x,
                                          player_ship_class.y,
                                          off_x,off_y)
    main_window.blit(fight_zone,(off_x,off_y))
    fight_zone.blit(background_img,(0,0))
    player_ship_class.update_position(fight_zone,movement_direction,
                                      rotation_direction,
                                      steering_direction,time)
    player_ship_class.blit_bullet(fight_zone,bullet_time)
    minimap_class.update_minimap(main_window)
    player_ship_class.regenerate_shield(shield_regeneration_time,
                                        time)
    
    
    # --------------COMPUTER TIME--------------
    computer_ships_class.pop_ship()
    computer_ships_class.blit_ships(fight_zone,time)
    comp_fire_time = computer_ships_class.fire(comp_fire_time)
    computer_ships_class.blit_bullet(fight_zone,time)
    # ---------------END COMPUTER TIME----------
    shield_regeneration_time = collision_class.check_all_collisions(shield_regeneration_time)
    

    # ---------------END SCREEN BLITTING --------

    # --------------EVENT HANDLING --------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                player_ship_class.shield_active = not player_ship_class.shield_active
            if event.key == pygame.K_ESCAPE :
                game_state = "pause"
                continue
            if event.key == pygame.K_p:
                game_state = "save_game"
                continue
    movement_direction = 0
    rotation_direction = 0
    steering_direction = 0
    # ----------GETTING KEY EVENTS------------
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_a]:
        rotation_direction = +1
    elif pressed_keys[pygame.K_d]:
        rotation_direction = -1
    if pressed_keys[pygame.K_s]:
        movement_direction = -1
    elif pressed_keys[pygame.K_w]:
        movement_direction = +1
    if pressed_keys[pygame.K_e]:
        steering_direction = +1
    elif pressed_keys[pygame.K_q]:
        steering_direction = -1
    if pressed_keys[pygame.K_SPACE]:
        fire_time = player_ship_class.fire(fire_time)
    if pressed_keys[pygame.K_1]:
        player_ship_class.active_weapon = 1
    elif pressed_keys[pygame.K_2]:
        player_ship_class.active_weapon = 2
    elif pressed_keys[pygame.K_3]:
        player_ship_class.active_weapon = 3
    elif pressed_keys[pygame.K_4]:
        player_ship_class.active_weapon = 4
    elif pressed_keys[pygame.K_5]:
        player_ship_class.active_weapon = 5

    # ---------- END GETTING KEY EVENTS------------

    #--------------END EVENT HANDLING------------


    pygame.display.update()
