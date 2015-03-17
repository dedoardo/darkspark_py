# This file contains every interface that we can find in the fight_zon
# lifebars, minimaps, score, shields etc..
import pygame

class Minimap :
    def __init__(self,player_ship_class,background_img,computer_ships_class):
        self.player_ship_class = player_ship_class
        self.computer_ships_class = computer_ships_class

        # some constants
        self.MAX_HEIGHT = background_img.get_height() / 10
        self.MAX_WIDTH = background_img.get_width() / 10
        self.POS_X = 0
        self.POS_Y = 0
        self.RED = (255,0,0)
        self.BLUE = (0,0,255)
        self.GREEN = (0,255,0)
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)



    def update_minimap(self,fight_zone):
        # --------DRAWING THE MINIMAP---------
        minimap_rect = pygame.Rect(self.POS_X,self.POS_Y,
                                   self.MAX_WIDTH,self.MAX_HEIGHT)
        pygame.draw.rect(fight_zone,self.BLACK,minimap_rect)
        # -------DRAWING THE SHIP------------
        ship_rect = pygame.Rect(self.player_ship_class.x / 10,
                                self.player_ship_class.y / 10,
                                4,4)
        pygame.draw.rect(fight_zone,self.GREEN,ship_rect)
        #---------DRAWING THE BULLETS----------
        for i in range (1,6):
            for bullet in self.player_ship_class.bullets[i]:
                bullet_rect = pygame.Rect(bullet[0] / 10,
                                          bullet[1] / 10,
                                          2,2)
                pygame.draw.rect(fight_zone,self.BLUE,bullet_rect)

        #---------DRAWING THE ENEMY SHIP----------
        for i in range (0,4):
            for ship in self.computer_ships_class.active_ship_side[i]:
                comp_rect = pygame.Rect(ship[0] / 10 ,ship[1] / 10,3,3)
                pygame.draw.rect(fight_zone,self.RED,comp_rect)

        #--------DRAWING THE ENEMY BULLETS----------
        for bullet in self.computer_ships_class.bullets:
            b_rect = pygame.Rect(bullet[0] / 10 ,bullet[1] / 10,2,2)
            pygame.draw.rect(fight_zone,self.WHITE,b_rect)
            
                
        
