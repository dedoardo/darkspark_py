import pygame
import math

# this is the class that represent the player ship
class Player_Ship:
    def __init__(self):
        # player ship that never changes
        self.ship_img = pygame.image.load('images/player_ship_0.png').convert()
        self.last_ship_img = self.ship_img
        # pygame variables
        self.fire_time = 0
    
        # ship variables ( speed etc...)
        self.armor = 1000
        self.speed = 1500
        self.rotation = 0
        self.rotation_speed = 720
        # this is the variable that represent the
        # ship position in the fight_zone
        # 100,100 are the standard values ( initial position)
        self.x = 650
        self.y = 250
        self.h_x = 0
        self.h_y = 0
        
        
        

        # shield variables
        self.shield_active = False
        self.shield_regeneration = 800
        self.shield_regeneration_speed = 1
        self.shield_hp = 150
        self.max_shield_hp = 800

        # weapon variables
        self.active_weapon = 3
        self.bullets = [[],[],[],[],[],[]]
        self.weapon_power = {
            1 : 100,
            2 : 80,
            3 : 120,
            4 : 50,
            5 : 250}
        self.weapon_ammo = {
            1 : 500,
            2 : 500,
            3 : 250,
            4 : 200,
            5 : 380}
        self.weapon_time = {
            1 : 50,
            2 : 60,
            3 : 40,
            4 : 75,
            5 : 25}
        self.weapon_images = {
            1 : pygame.image.load('images/weapon_1.png').convert_alpha(),
            2 : pygame.image.load('images/weapon_2.png').convert_alpha(),
            3 : pygame.image.load('images/weapon_3.png').convert_alpha(),
            4 : pygame.image.load('images/weapon_4.png').convert_alpha(),
            5 : pygame.image.load('images/weapon_5.png').convert_alpha()}
        self.weapon_speed = {
            1 : 800,
            2 : 1000,
            3 : 1200,
            4 : 900,
            5 : 1300}

        self.shield_images = {
            1 : pygame.image.load('images/shield_0.png').convert_alpha(),
            2 : pygame.image.load('images/shield_1.png').convert_alpha(),
            3 : pygame.image.load('images/shield_2.png').convert_alpha(),
            4 : pygame.image.load('images/shield_3.png').convert_alpha()}

    def restart(self):
        self.x = 650
        self.y = 250
        self.h_x = 0
        self.h_y = 0
        self.armor = 1000
        self.shield_hp = 150
        self.shield_active = False
        self.fire_time = 0
        

    def update_position(self,fight_zone,movement_direction,
                        rotation_direction,
                        steering_direction,time):
    
        temp_angle = 0


        # ---------- SHIP ROTATION ------------------
        # this rotation is taken from pygame.org website
        orig_rect = self.ship_img.get_rect()
        self.rotation += rotation_direction * self.rotation_speed * (time/1000.)
        rotated_ship = pygame.transform.rotate(self.ship_img,self.rotation)
        rotated_rect = orig_rect.copy()
        rotated_rect.center = rotated_ship.get_rect().center
        try :
            rotated_ship = rotated_ship.subsurface(rotated_rect).copy()
        except ValueError:
            pass
        #-----------END SHIP ROTATION-------------
        #-----------SHIP STEERING -------------

        #----------END SHIP STEERING-----------
        # THIS PART WILL BE FIXED LATER BECAUS IS NOT SO EASY AS I THOUGHT
        
##
##        temp_angle = self.rotation + ( 90 * steering_direction)
##        t_x = math.cos(math.radians(temp_angle))
##        t_y = math.sin(math.radians(temp_angle))
##        s_distance = (time/1000.) * self.speed * math.fabs(steering_direction)
##        self.x += t_x * s_distance
##        self.y += t_y * s_distance
##        print temp_angle
##        
##    
        #-----------ROTATING AND BLITTING SHIELD---------------
        # this part is kinda hard-coded, i'll try to fix this later
        if self.shield_active and self.shield_hp > 0:
            if self.shield_hp > 600 :
                orig_shield = self.shield_images[1].get_rect()
                rotated_shield = pygame.transform.rotate(self.shield_images[1],
                                                          self.rotation)
                rotated_shield_rect = rotated_shield.get_rect()
                rotated_shield_rect.center = orig_shield.center
                try :
                    rotated_shield = rotated_shield.subsurface(rotated_shield_rect).copy()
                except ValueError:
                    pass
            elif self.shield_hp > 450 :
                orig_shield = self.shield_images[2].get_rect()
                rotated_shield = pygame.transform.rotate(self.shield_images[2],
                                                          self.rotation)
                rotated_shield_rect = rotated_shield.get_rect()
                rotated_shield_rect.center = orig_shield.center
                try :
                    rotated_shield = rotated_shield.subsurface(rotated_shield_rect).copy()
                except ValueError:
                    pass
            elif self.shield_hp > 200 :
                orig_shield = self.shield_images[3].get_rect()
                rotated_shield = pygame.transform.rotate(self.shield_images[3],
                                                          self.rotation)
                rotated_shield_rect = rotated_shield.get_rect()
                rotated_shield_rect.center = orig_shield.center
                try :
                    rotated_shield = rotated_shield.subsurface(rotated_shield_rect).copy()
                except ValueError:
                    pass
            else:
                orig_shield = self.shield_images[4].get_rect()
                rotated_shield = pygame.transform.rotate(self.shield_images[4],
                                                          self.rotation)
                rotated_shield_rect = rotated_shield.get_rect()
                rotated_shield_rect.center = orig_shield.center
                try :
                    rotated_shield = rotated_shield.subsurface(rotated_shield_rect).copy()
                except ValueError:
                    pass
            fight_zone.blit(rotated_shield,(self.x - (self.ship_img.get_width() / 2),
                                            self.y - (self.ship_img.get_height() / 2)))
                                                     
        
        #-----------END ROTATING AND BLITTING SHIELD-----------

        #-----------SHIP MOVEMENT----------------

        distance = self.speed * (time/1000.) * movement_direction
        self.h_x = math.cos(self.rotation * math.pi / 180.)
        self.h_y = math.sin(self.rotation * math.pi / 180.)
        self.x += self.h_x * distance
        self.y -= self.h_y * distance
        if self.x < 0:
            self.x = 0
        elif self.x > 2560 :
            self.x = 2560
        if self.y < 0 :
            self.y = 0
        elif self.y > 1600:
            self.y = 1600
        

        #-----------END SHIP MOVEMENT

        #---------BLITTING EVERYTHIN--------------
        self.last_ship_img = rotated_ship.copy()
        fight_zone.blit(rotated_ship,(self.x,self.y))

        #-----------END BLITTING------------------
        
        
            

    def fire(self,fire_time):
        if fire_time >= self.weapon_time[self.active_weapon]:
            fire_time = 0
            self.bullets[self.active_weapon].insert(0,[self.x,self.y,self.h_x,self.h_y])
            self.weapon_ammo[self.active_weapon] -= 1
        return fire_time


    def blit_bullet(self,fight_zone,time):

        for i in range(1,6):
            for bullet in self.bullets[i]:
                if bullet[0] > 2560 or bullet[1] > 1600 or bullet[0] < 0 or bullet[1] < 0:
                    self.bullets[i].remove(bullet)
                else :
                    distance = self.weapon_speed[i] * (time / 1000.)
                    bullet[0] += distance * bullet[2]
                    bullet[1] -= distance * bullet[3]
                    fight_zone.blit(self.weapon_images[i],(bullet[0],bullet[1]))        
        
        
    def regenerate_shield(self,shield_time,time):
        if self.shield_hp < self.max_shield_hp :
            if shield_time >= self.shield_regeneration :
                r = shield_time - self.shield_regeneration
                if r > 100 :
                    shield_time = self.shield_regeneration
                    self.shield_hp += self.shield_regeneration_speed * time
        # i'm using another if cos compiler gives me indentation error!
        else :
            shield_time = 0
        return shield_time
    def is_dead(self):
        if self.armor <= 0 :
            return True
