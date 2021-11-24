#numero matricola 331968
from time import time
from PacMan import Actor, Arena, PacMan, Ghost, big_cookies, cookies, big_cookies
from pacman_biscotti import cookis, big_cookis

#game nella modalita hard(genera  doppio dei fantasmi in classic game)
class PacManGame_Hard:
    def __init__(self):
        #inizializzazione nel costruttore i personaggi come istanza
        self._arena_hard = Arena ((232, 280))
        self._Hero_hard = PacMan(self._arena_hard, (112, 88))
        cookies.make_cookis(self._arena_hard)
        big_cookies.make_big_cookis(self._arena_hard)
        
        
        Ghost(self._arena_hard, (208, 232), 0)
        Ghost(self._arena_hard, (8, 8), 0)
        Ghost(self._arena_hard, (208, 232), 0)
        Ghost(self._arena_hard, (8, 8), 0)
        Ghost(self._arena_hard, (208, 232), 0)
        Ghost(self._arena_hard, (8, 8), 0)
        Ghost(self._arena_hard, (208, 232), 0)
        Ghost(self._arena_hard, (8, 8), 0)
    
    
        
        
    def arena(self) -> Arena:
        return self._arena_hard
    
    def PacMan(self) -> PacMan:
        return self._Hero_hard

    def game_over(self) -> bool:
        return self._Hero_hard.lives() 

    def game_won(self) -> bool:
        return self._Hero_hard.eaten_cookies() - 244