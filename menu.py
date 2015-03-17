import pygame
import load

class Main_Menu():
    def __init__(self,computer_ships_class,player_ship_class):
        self.computer_ships_class = computer_ships_class
        self.player_ship_class = player_ship_class
        self.MAX_HEIGHT = 768
        self.MAX_WIDTH = 1370

        self.new_game_button = pygame.image.load('images/new_game_button.png').convert_alpha()
        self.load_game_button = pygame.image.load('images/load_game_button.png').convert_alpha()
        self.highscores_button = pygame.image.load('images/highscores_button.png').convert_alpha()
        self.exit_button = pygame.image.load('images/exit_button.png').convert_alpha()
        self.menu_bg = pygame.image.load('images/menu_bg.jpg').convert()

        self.game_over_bg = pygame.image.load('images/game_over.png').convert_alpha()
        
        self.game_over_font = pygame.font.Font('fonts/radiostars.ttf',30)
        self.main_font = pygame.font.Font('fonts/Robotica.ttf',30)
    def blit_main_menu(self,screen,game_state):
        while True :
            screen.fill((0,0,0))

                    
                    
            screen.blit(self.menu_bg,(0,0))
            screen.blit(self.new_game_button,(self.MAX_WIDTH / 2 - self.new_game_button.get_width() / 2,
                                              self.MAX_HEIGHT / 2 - self.new_game_button.get_height() * 2))
                        
            screen.blit(self.load_game_button,(self.MAX_WIDTH / 2 - self.load_game_button.get_width() / 2,
                                               self.MAX_HEIGHT / 2 - self.new_game_button.get_height()))

            screen.blit(self.highscores_button,(self.MAX_WIDTH / 2 - self.highscores_button.get_width() / 2,
                                                self.MAX_HEIGHT / 2 ))

            screen.blit(self.exit_button,(self.MAX_WIDTH / 2 - self.exit_button.get_width() / 2,
                                          self.MAX_HEIGHT / 2 + self.exit_button.get_height()))

            new_game_rect = self.new_game_button.get_rect()
            new_game_rect.x = self.MAX_WIDTH / 2 - self.new_game_button.get_width() / 2
            new_game_rect.y = self.MAX_HEIGHT / 2 - self.new_game_button.get_height() * 2

            load_game_rect = self.load_game_button.get_rect()
            load_game_rect.x = self.MAX_WIDTH / 2 - self.load_game_button.get_width() / 2
            load_game_rect.y = self.MAX_HEIGHT / 2 - self.load_game_button.get_height() 

            highscores_rect = self.highscores_button.get_rect()
            highscores_rect.x = self.MAX_WIDTH / 2 - self.highscores_button.get_width() / 2
            highscores_rect.y = self.MAX_HEIGHT / 2

            exit_rect = self.exit_button.get_rect()
            exit_rect.x = self.MAX_WIDTH / 2 - self.exit_button.get_width() / 2
            exit_rect.y = self.MAX_HEIGHT / 2 + self.exit_button.get_height() 

            # BLOCKING ALL EVENTS
            m_x,m_y = pygame.mouse.get_pos()
            e = pygame.event.wait()
            if e.type == pygame.QUIT :
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                # checking all collisione
                if new_game_rect.collidepoint(m_x,m_y):
                    game_state = "new_game"
                    break
                if exit_rect.collidepoint(m_x,m_y):
                    exit()
                if highscores_rect.collidepoint(m_x,m_y):
                    game_state = "highscores"
                    break
                if load_game_rect.collidepoint(m_x,m_y):
                    game_state = "load_game"
                    print "load game"
                    break

            pygame.display.update()
        return game_state
    
    def blit_game_over(self,screen,game_state,time):
        score_t = "SCORE  : %r" % (self.computer_ships_class.destroyed_ships * 50)
        time_t = "TIME ELAPSED : %r" % int(time)
        score_text = self.game_over_font.render(score_t,True,(0,255,0))
        time_text = self.game_over_font.render(time_t,True,(0,255,0))
        highscore = self.computer_ships_class.destroyed_ships * 50
        name = "player"
        while game_state == "game_over" :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN :
                        load.Highscores.load_highscore(highscore,name)
                        game_state = "main_menu"
                    elif event.key == pygame.K_BACKSPACE :
                        name = name[0:-1]
                    elif event.key <= 127:
                        if len(name) <= 15 :
                            name += chr(event.key)
                    

            
            name_text = self.main_font.render(name,True,(255,255,255))
        
                    
            screen.blit(self.game_over_bg,(self.MAX_WIDTH / 2 - self.game_over_bg.get_width() / 2,
                                       self.MAX_HEIGHT / 2  -self.game_over_bg.get_height() / 2))
            screen.blit(score_text,(self.MAX_WIDTH / 2 - score_text.get_width() / 2,
                                    self.MAX_HEIGHT / 2 - score_text.get_height() * 2))
            screen.blit(time_text,(self.MAX_WIDTH / 2 - time_text.get_width() / 2,
                                   self.MAX_HEIGHT / 2))
            screen.blit(name_text,(self.MAX_WIDTH / 2 - name_text.get_width() / 2,
                                   self.MAX_HEIGHT / 2 + name_text.get_height() * 2 ))
            
            pygame.display.update()
        return game_state

    def pause_menu(self,screen,game_state):
        while game_state == "pause" :
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                game_state = "game"

            
        return game_state
