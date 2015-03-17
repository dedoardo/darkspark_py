import pygame
import math
import random
pygame.init()
# This is the class for the lower interface the biggest one
class Interface:
    def __init__(self,MAX_WIDTH,MAX_HEIGHT,ship_class,computer_ships_class):
        self.ship_class = ship_class
        self.computer_ships_class = computer_ships_class
        self.MAX_WIDTH = MAX_WIDTH
        self.MAX_HEIGHT = MAX_HEIGHT
        self.interface_bg = pygame.image.load('images/interface_bg.png')

        # lifebar variables
        self.LIFEBAR_MAX_WIDTH = 400
        self.LIFEBAR_MAX_HEIGHT = 45
        self.LIFEBAR_COLOR = (0,255,0)

        # shield variables
        self.SHIELDBAR_MAX_WIDTH = 410
        self.SHIELDBAR_MAX_HEIGHT = 45
        self.SHIELDBAR_COLOR = (0,0,255)

        self.font = pygame.font.Font("fonts/ethnocentric.ttf",32)
        self.weapon_font = pygame.font.Font("fonts/Starcraft.ttf",12)
        self.stat_font = pygame.font.Font("fonts/Robotica.ttf",25)


        

    def update(self,screen):
        screen.blit(self.interface_bg,(0,(self.MAX_HEIGHT - self.interface_bg.get_height())))
        self.update_lifebar(screen)
        self.update_shieldbar(screen)
        self.update_weapon(screen)
        self.update_game_stats(screen)

    def update_lifebar(self,screen):
        actual_life = self.ship_class.armor
        n_pixel = self.LIFEBAR_MAX_WIDTH - (actual_life / 2.5)
        lifebar_rect = pygame.Rect(0,
                                   self.MAX_HEIGHT - 150,
                                   self.LIFEBAR_MAX_WIDTH - n_pixel,
                                  self.LIFEBAR_MAX_HEIGHT)
        pygame.draw.rect(screen,self.LIFEBAR_COLOR,lifebar_rect)
        t = "ARMOR HP : %r " % int(actual_life)
        text = self.font.render(t,True,(255,255,255))
        screen.blit(text,(self.LIFEBAR_MAX_WIDTH / 2 - (text.get_width() / 2),
                          self.MAX_HEIGHT - 150 
                          ))
        
        
        
    
    def update_shieldbar(self,screen):
        actual_shield = self.ship_class.shield_hp
        if actual_shield >= self.ship_class.max_shield_hp :
            actual_shield = self.ship_class.max_shield_hp
        n_pixel = 410 - (math.ceil(actual_shield / 2))
        shieldbar_rect = pygame.Rect(0,
                                     self.MAX_HEIGHT - 80,
                                     self.SHIELDBAR_MAX_WIDTH - n_pixel,
                                     self.SHIELDBAR_MAX_HEIGHT)
        pygame.draw.rect(screen,self.SHIELDBAR_COLOR,shieldbar_rect)
        shield_perc = (actual_shield* 100) / self.ship_class.max_shield_hp
        t = "SHIELD HP : %r " %int(((actual_shield * 100) / self.ship_class.max_shield_hp))
        text = self.font.render(t,True,(255,255,255))
        screen.blit(text,(self.SHIELDBAR_MAX_WIDTH / 2 - (text.get_width() / 2),
                          self.MAX_HEIGHT - 75))

    def update_weapon(self,screen):
        for i in range (1,6):
            # blitting weapon number
            t = str(i)
            text = self.weapon_font.render(t,True,(255,255,255))
            screen.blit(text,(400 + (75 * i),self.MAX_HEIGHT - 150))
            # blitting weapon image
            screen.blit(self.ship_class.weapon_images[i],
                        (400 + (75 * i) - self.ship_class.weapon_images[i].get_width() / 2,
                         self.MAX_HEIGHT - 120))
            # blitting weapon ammo
            a_t = str(self.ship_class.weapon_ammo[i])
            a_text = self.weapon_font.render(a_t,True,(255,255,255))
            screen.blit(a_text,(400 + (75 *i) - a_text.get_width() / 2,
                                self.MAX_HEIGHT - 90))

            # blitting weapon power
            p_text = self.weapon_font.render("Power :",True,(255,255,255))
            screen.blit(p_text,(400 + (75 * i) - p_text.get_width() / 2,
                                                        self.MAX_HEIGHT - 60))

            wp_t = str(self.ship_class.weapon_power[i])
            wp_text = self.weapon_font.render(wp_t,True,(255,255,255))
            screen.blit(wp_text,(400 +(75 * i) - wp_text.get_width() / 2,
                                 self.MAX_HEIGHT - 30))

    def update_game_stats(self,screen):
        # blitting the game stats
        p_t = "POINTS : %r" % self.computer_ships_class.destroyed_ships
        d_t = "DIFFICULTY : %r " % self.computer_ships_class.difficulty
        #  p_text = self.fon
        p_text = self.stat_font.render(p_t,True,(255,255,255))
        d_text = self.stat_font.render(d_t,True,(255,255,255))
        screen.blit(p_text,(self.MAX_WIDTH - 500,self.MAX_HEIGHT - 120))
        screen.blit(d_text,(self.MAX_WIDTH - 500,self.MAX_HEIGHT - 90))


