import pickle
import pygame
import copy
import random

class Highscores:
    def __init__(self):
        self.highscores_filename = 'highscore.txt'
        self.MAX_WIDTH = 1370
        self.MAX_HEIGHT = 768
        self.highscores_bg = pygame.image.load('images/highscores_bg.jpg').convert()
        self.highscore_font = pygame.font.Font('fonts/ethnocentric.ttf',35)
        self.highscores = dict()
        
    @staticmethod 
    def load_highscore(highscore,name):
        FileObj = open('highscore.txt','rb')
        olddic = pickle.load(FileObj)
        olddic[highscore] = name
        FileObj.close()
        FileObj = open('highscore.txt','wb')
        pickle.dump(olddic,FileObj)
        FileObj.close()

    def get_highscores(self):
        try :
            FileObj = open(self.highscores_filename,'rb')
            self.highscores = pickle.load(FileObj)
        except EOFError :
            pass
    def sort_highscore(self):
        l = []
        for i in self.highscores:
            l.append(i)
        l.sort()
        newdict = dict()
        for i in l :
            newdict[i] = self.highscores[i]

        return newdict
            
    def blit_highscores(self,screen,game_state):
        name_list = []
        score_list = []
        self.get_highscores()
        self.highscores = self.sort_highscore()
        name = "POINT     "
        name_text = self.highscore_font.render(name,True,(255,255,255))
        point = "NAME"
        point_text = self.highscore_font.render(point,True,(255,255,255))
        # I'm preparing the text just one time to avoid useless memory usage
        for n in self.highscores :
            name_list.insert(0,n)
            score_list.insert(0,self.highscores[n])

            
    
        while True:
            e = pygame.event.wait()
            if e.type == pygame.QUIT :
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE :
                    game_state = "main_menu"
                    break
        
            
            screen.fill((0,0,0))
            screen.blit(self.highscores_bg,(0,0))
            screen.blit(name_text,(self.MAX_WIDTH / 2 - name_text.get_width() ,
                                   150))
            screen.blit(point_text,(self.MAX_WIDTH / 2 + point_text.get_width(),
                                    150))
            # blitting results
            # only the first ten, but the others will be kept in memory
            # who knows .... :P
            r = 0
            while r < 10:
                r += 1
                i = 0
                for n in name_list :
                    i += 1
                    n_text = self.highscore_font.render(str(n),True,(0,255,0))
                    screen.blit(n_text,(self.MAX_WIDTH / 2 - name_text.get_width(),
                                        150 + n_text.get_height() * i))

                i = 0
                for s in score_list :
                    i += 1
                    s_text = self.highscore_font.render(str(s),True,(0,0,255))
                    screen.blit(s_text,(self.MAX_WIDTH / 2 + point_text.get_width(),
                                        150 + s_text.get_height() * i))

            pygame.display.update()
        
        return game_state
        
        
class Load_Game:
    def __init__(self):
        self.saves_filename = 'saves.txt'

    def save_game(self,player_ship_class,computer_ships_class,game_state):
        p_c = [player_ship_class.x,
                              player_ship_class.y,
                              player_ship_class.armor,
                              player_ship_class.shield_hp,
                              player_ship_class.weapon_ammo]
        c_c = [computer_ships_class.active_ship_side,
                                computer_ships_class.bullets,
                                computer_ships_class.difficulty,
                                computer_ships_class.destroyed_ships]
        # saving all the needed things into one dictionary
        # that will be dumped later
        save_dict = {
            "player_class" : p_c,
            "computer_class" : c_c
                                    
        }
        # creating a random name for the file 
        #str(str(random.randint(0,100000)) + ".txt")
        try :
            fobj = open(self.saves_filename,'wb')
            pickle.dump(save_dict,fobj)
            fobj.close()
        except EOFError:
            print "EOFError Popped , remove try, except to see message"
        game_state = "main_menu"
        return game_state
    def load_game(self,player_ship_class,computer_ships_class,game_state):
        # i'm still gonna create it as empty to avoid more errors
        saves = dict()
        # opening the file in binary mode and saving the dict
        try :
            fobj = open(self.saves_filename,'rb')
            saves = pickle.load(fobj)
        except EOFError:
            print "EOFError Popped, remove try,except to see message"
        # loading all the datas into the active classes
        player_ship_class.x = saves["player_class"][0]
        player_ship_class.y = saves["player_class"][1]
        player_ship_class.armor = saves["player_class"][2]
        player_ship_class.shield_hp = saves["player_class"][3]
        player_ship_class.weapon_ammo = saves["player_class"][4]
        # loading enemies
        computer_ships_class.active_ship_side = saves["computer_class"][0]
        computer_ships_class.bullets = saves["computer_class"][1]
        computer_ships_class.difficulty = saves["computer_class"][2]
        computer_ships_class.destroyed_ships = saves["computer_class"][3]

        # changing game state 
        game_state = "game"
        return game_state,computer_ships_class,player_ship_class

