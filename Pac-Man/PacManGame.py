#numero matricola 331968
from time import time
from PacMan import Actor, Arena, PacMan, Ghost, big_cookies, cookies, big_cookies
from pacman_biscotti import cookis, big_cookis


class PacManGame:
    def __init__(self):
        #inizializzazione nel costruttore i personaggi come istanza
        self._arena = Arena ((232, 280))
        self._Hero = PacMan(self._arena, (112, 88))
        cookies.make_cookis(self._arena)
        big_cookies.make_big_cookis(self._arena)
        
        G = Ghost(self._arena, (8, 8), 0)
        G1 = Ghost(self._arena, (8, 232), 1)
        G2 = Ghost(self._arena, (208, 8), 2)
        G3 = Ghost(self._arena, (208, 232), 3)
    

    def arena(self) -> Arena:
        return self._arena
    
    def PacMan(self) -> PacMan:
        return self._Hero

    def game_over(self) -> bool:
        return self._Hero.lives() 

    def game_won(self) -> bool:
        return self._Hero.eaten_cookies() - 244
    