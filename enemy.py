# THIS IS THE CLASS THAT REPRESENT THE ENEMY SHIPS
import pygame
import random
import math

class Enemy_Ships:
    def __init__(self,player_ship_class):
        # ---- THIS PART OF CODE SUCKS BECAUSE I'M TRYING TO GET MORE IMAGES
        # AND MAKE DICTIONARIES AS I DID FOR THE SHIP CLASS
        self.player_ship_class = player_ship_class
        # bullets
        self.bullet_img = pygame.transform.scale(pygame.image.load('images/comp_weapon_0.png').convert_alpha(),
                                                   (32,32))

        # some constants and variable
        self.SHIP_SPEED = 500
        self.FIRE_TIME = 300
        self.BULLET_SPEED = 2000

        # rotating this image
        alien_ship_0 = pygame.image.load('images/computer_ship_0.png').convert()
        computer_ship_0 = pygame.transform.rotate(alien_ship_0, -90)
        computer_ship_0.set_colorkey((255,255,255))

        self.computer_ship_images = {
            1 : computer_ship_0}


        self.bullets = []
        self.destroyed_ships = 0
        self.difficulty = 1.
        self.active_ship_side = [[],[],[],[]]


        #-----------------------------------------------------------

    def restart(self):
        self.bullets = []
        self.destroyed_ships = 0
        self.difficulty = 1.
        self.active_ship_side = [[],[],[],[]]


        
    def get_heading(self,b_x,b_y):
        # let's have some fun with trig
        d_x = self.player_ship_class.x
        d_y = self.player_ship_class.y

        # getting magnitude and then heading
        m_x = b_x - d_x
        m_y = b_y - d_y
        m = math.sqrt(m_x ** 2 + m_y **2)
        h_x = m_x / m
        h_y = m_y / m
        return h_x,h_y




    def pop_ship(self):
        # Ships are popped randomly in the map
        # two ships per side
        for i in range (0,4):
            if len(self.active_ship_side[i]) >= 2:
                break
            else :
                # i pop the ship in different position based on the side
                # 0 left , 1 top, 2 right, 3 bottom side
                if i == 0 :
                    r_x = random.randrange(0, 300)
                    r_y = random.randrange(0,1600)
                elif i == 1:
                    r_x = random.randrange(0,2560)
                    r_y = random.randrange(0,300)
                elif i == 2 :
                    r_x = random.randrange(2560-300,2560)
                    r_y = random.randrange(0,1600)
                else :
                    r_x = random.randrange(0,2560)
                    r_y = random.randrange(1600-300,1600)

            self.active_ship_side[i].insert(0,[r_x,r_y,0,0,0,100])


    def blit_ships(self,fight_zone,time):
        collided = []
        for i in range(0,4):
            for ship in self.active_ship_side[i]:
                if ship[0] < 0 or ship[1] < 0 or ship[0] > 2560 or ship[1] > 1600:
                    self.active_ship_side[i].remove(ship)
                    continue
                old_x = ship[0]
                old_y = ship[1]
                h_x,h_y = self.get_heading(ship[0],ship[1])
                ship[2] = -h_x
                ship[3] = -h_y
                # getting rotation with atan2
                rotation = math.degrees(math.atan2(h_y,-h_x))
                ship[4] = rotation
                ship[0] += (self.SHIP_SPEED * (time / 1000.)* self.difficulty) * (-h_x) 
                ship[1] += (self.SHIP_SPEED * (time / 1000.)* self.difficulty) * (-h_y)
                rotated_ship = pygame.transform.rotate(self.computer_ship_images[1],
                                                       rotation)
                distance = self.get_distance(ship[0],ship[1])
                ship_rect = rotated_ship.get_rect()
                ship_rect.topleft = (ship[0],ship[1])
                # -------- CHECKING FOR COLLISION WITH OTHER SHIPS------
                for i in range (0,4):
                    for c_ship in self.active_ship_side[i]:
                        if ship == c_ship :
                            continue
                        rotated_c_ship = pygame.transform.rotate(self.computer_ship_images[1],
                                                                 c_ship[4])
                        c_ship_rect = rotated_c_ship.get_rect()
                        c_ship_rect.topleft = (c_ship[0],c_ship[1])
                        collide = ship_rect.colliderect(c_ship_rect)
                        if collide == True :
                            c_distance = self.get_distance(c_ship[0],c_ship[1])
                            if c_distance < distance :
                                ship[0] = old_x
                                ship[1] = old_y
                fight_zone.blit(rotated_ship,(ship[0],ship[1]))
                #------------ END CHECKING -----------------

    # ------ HERE WE GOT BULLET FUNCTIONS ------
    def fire(self,fire_time):
        if fire_time > self.FIRE_TIME :
            fire_time = 0
            for i in range(0,4):
                for ship in self.active_ship_side[i]:
                    self.bullets.insert(0,[ship[0],ship[1],ship[2],ship[3]])

        return fire_time

    def blit_bullet(self,fight_zone,time):
        b_distance = self.BULLET_SPEED * (time / 1000.)
        for bullet in self.bullets :
            if bullet[0] < 0 or bullet[1] < 0 or bullet[0] > 2560 or bullet[1] > 1600:
                self.bullets.remove(bullet)
            bullet[0] += bullet[2] * b_distance
            bullet[1] += bullet[3] * b_distance
            fight_zone.blit(self.bullet_img,(bullet[0],bullet[1]))


    def get_distance(self,b_x,b_y):
        d_x = self.player_ship_class.x
        d_y = self.player_ship_class.y
        m_x = b_x - d_x
        m_y = b_y - d_y
        m = math.sqrt(m_x ** 2 + m_y ** 2)
        return m







