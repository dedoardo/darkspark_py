import pygame
import math

# THIS IS THE CLASS THAT CHECKS ALL THE COLLISION
# THERE IS A MAIN FUNCTION THAT CLASS ALL SUBFUNCTIONS
# THAT CKECKS WHETHER A COLLISION WITH A DETERMINATE OBJECT
# HAPPENS OR NOT . IT USES PYGAME.RECT COLLISIONDETECTION
# BECAUSE IS QUITE GOOD AND BETTER THAN ANYTHING I'M ACTUALLY ABLE
# TO CREATE. HAVE FUN :P

class Collision_Detection:
    def __init__(self,player_ship_class,computer_ships_class):
        self.player_ship_class = player_ship_class
        self.computer_ships_class = computer_ships_class



    def check_all_collisions(self,shield_time):
        # checking for enemy bullet to player ship collision
        p_ship_rect = self.player_ship_class.last_ship_img.get_rect()
        p_ship_rect.x = self.player_ship_class.x
        p_ship_rect.y = self.player_ship_class.y
        for e_bullet in self.computer_ships_class.bullets:
            bullet_rect = self.computer_ships_class.bullet_img.get_rect()
            bullet_rect.x = e_bullet[0]
            bullet_rect.y = e_bullet[1]
            if bullet_rect.colliderect(p_ship_rect) == True:
            # i use this variable to make sure that the player
            # ship shield will not regenerate i'm gonna return it at the end of the script
                shield_time = 0
                self.computer_ships_class.bullets.remove(e_bullet)
                # calculating the life or the shield the player will lose :
                if self.player_ship_class.shield_active :
                    self.player_ship_class.shield_hp -= 50 * self.computer_ships_class.difficulty
                    if self.player_ship_class.shield_hp <= 0 :
                        self.player_ship_class.armor += self.player_ship_class.shield_hp
                        self.player_ship_class.shield_hp = 0
                else :
                    self.player_ship_class.armor -= 45 * self.computer_ships_class.difficulty

        # checking for player bullet to enemy ship collision
        for i in range (1,6):
            for p_bullet in self.player_ship_class.bullets[i]:
                p_bullet_rect = self.player_ship_class.weapon_images[i].get_rect()
                p_bullet_rect.x = p_bullet[0]
                p_bullet_rect.y = p_bullet[1]
                for s in range (0,4):
                    for e_ship in self.computer_ships_class.active_ship_side[s]:
                        e_ship_rect = self.computer_ships_class.computer_ship_images[1].get_rect()
                        e_ship_rect.x = e_ship[0]
                        e_ship_rect.y = e_ship[1]
                        if p_bullet_rect.colliderect(e_ship_rect):
                            e_ship[5] -= self.player_ship_class.weapon_power[i]
                            if e_ship[5] <= 0 :
                                self.computer_ships_class.destroyed_ships += 1
                                self.computer_ships_class.active_ship_side[s].remove(e_ship)

        # checking for ship to ship collision
        for i in range (0,4):
            for e_ship in self.computer_ships_class.active_ship_side[i]:
                e_ship_rect = self.computer_ships_class.computer_ship_images[1].get_rect()
                e_ship_rect.x = e_ship[0]
                e_ship_rect.y = e_ship[1]
                if p_ship_rect.colliderect(e_ship_rect):
                    shield_time = 0
                    self.computer_ships_class.active_ship_side[i].remove(e_ship)
                    if self.player_ship_class.shield_active :
                        self.player_ship_class.shield_hp -= 80 * self.computer_ships_class.difficulty
                        if self.player_ship_class.shield_hp <= 0:
                            self.player_ship_class.armor += self.player_ship_class.shield_hp
                            self.player_ship_class.shield_hp = 0
                    else :
                        self.player_ship_class.armor -= 80 * self.computer_ships_class.difficulty
                        


        return shield_time
                        
        





