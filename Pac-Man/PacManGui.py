#numero matricola 331968 Andrea De Pellegrin
from PacMan import cookies
import g2d
from PacManGame import PacManGame
from PacMan_Hard import PacManGame_Hard

class PacManGui:
    def __init__(self):
        self._game = PacManGame()
        self._game_hard = PacManGame_Hard()
        self._key = False
        self._game_mode = 'unselect'
        self._game_menu = False #variabile per il menu 
        self._win = False
        self._over = False
        g2d.init_canvas(self._game.arena().size())
        g2d.main_loop(self.tick)
        
  
    def home_screen(self) -> bool:
        #creazione della schermata di home 
        home_str = "press x to play"
        info= "press esc to close the game"
        info2 = "press m to return to menu"
        g2d.set_color((0, 0, 0))
        g2d.fill_rect((0, 0), (232, 280))

        g2d.set_color((255, 255, 0))
        g2d.draw_text(home_str,  (58, 170), 25)
        g2d.draw_text(info,  (5, 200), 25)
        g2d.draw_text(info2,  (10, 230), 25)
        g2d.draw_image('home.png', (40, 50) )

        if(g2d.key_pressed("x")): 
           self._key = True
           g2d.play_audio("Music/game_start.wav")

    def game_mood(self):
        #scelta della modalita di gioco
        g2d.draw_image('game-mode.png', (0,0) )

        if(g2d.key_pressed("1")): 
           self._game_mode = 'classic'
           self._game_menu = True

        elif(g2d.key_pressed("2")):
            self._game_mode = 'hard'
            self._game_menu = True

        else:
            self._game_mode = 'unselect'

    
    def tick(self):
        #tasti di navigazione 
        if g2d.key_pressed("Escape"):
                    g2d.close_canvas()

        if g2d.key_pressed("m"):
            self._game_mode = 'unselect'
            self._game_menu = False
            

        if not (self._key):
            self.home_screen()

        if(self._key):
            if not(self._game_menu):
                self.game_mood()

            if self._game_mode == 'classic':

                self._game.PacMan().control(g2d.current_keys())
                arena = self._game.arena() 
                arena.move_all(cookies) # Game logic

                g2d.clear_canvas()
                g2d.set_color((0, 0, 0))
                g2d.fill_rect((0, 240), (232, 40))
                g2d.draw_image("pac-man-bg.png", (0, 0))

                self._game.PacMan().symbol_life()
                self._game.PacMan().seconds_powerup()
                

                for a in arena.actors():
                    if a.symbol() != None:
                        g2d.draw_image_clip("pac-man.png", a.symbol(), a.size(), a.position())
                    else:
                        g2d.draw_image_clip("pac-man.png", self._game.PacMan().symbol(), self._game.PacMan().size(), self._game.PacMan().position())
                eaten_cookies = self._game.PacMan().eaten_cookies()
                points = eaten_cookies * 3
                points_txt = "points: " + str(points) 
                g2d.set_color((255, 255, 0))
                g2d.draw_text(points_txt + " ", (0, 260), 20)
                g2d.draw_text("Lives: ", (90, 260), 20)

                self._game.PacMan().control(g2d.current_keys())
                
                if not (self._game.game_over()) and not(self._win):
                        self._over = True
                        g2d.draw_image("game-over.png", (0, 0))  

                elif not(self._game.game_won()) and not(self._over):
                    self._win = True
                    g2d.draw_image("you-won.png", (0, 0))
                  

###################  MODALITA HARD ################
            elif self._game_mode == 'hard':
                
                self._game_hard.PacMan().control(g2d.current_keys())
                arena = self._game_hard.arena() 
                arena.move_all(cookies) # Game logic

                g2d.clear_canvas()
                g2d.set_color((0, 0, 0))
                g2d.fill_rect((0, 240), (232, 40))
                g2d.draw_image("pac-man-bg.png", (0, 0))

                self._game_hard.PacMan().symbol_life()
                self._game_hard.PacMan().seconds_powerup()
                

                for a in arena.actors():
                    if a.symbol() != None:
                        g2d.draw_image_clip("pac-man.png", a.symbol(), a.size(), a.position())
                    else:
                        g2d.draw_image_clip("pac-man.png", self._game_hard.PacMan().symbol(), self._game_hard.PacMan().size(), self._game_hard.PacMan().position())
                #calcolo del punteggio        
                eaten_cookies = self._game_hard.PacMan().eaten_cookies()
                points = eaten_cookies * 3
                points_txt = "points: " + str(points) 
                g2d.set_color((255, 255, 0))
                g2d.draw_text(points_txt + " ", (0, 260), 20)
                g2d.draw_text("Lives: ", (90, 260), 20)

                self._game_hard.PacMan().control(g2d.current_keys())
    
                if not (self._game_hard.game_over()):
                        g2d.draw_image("game-over.png", (0, 0))
                   

                elif not(self._game_hard.game_won()):
                    g2d.draw_image("you-won.png", (0, 0))
           
def main():
    gui = PacManGui()

main()
