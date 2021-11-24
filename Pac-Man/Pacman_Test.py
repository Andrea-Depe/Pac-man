#numero matricola 331968
import unittest
from time import time
from PacMan import Actor, Arena, PacMan, Ghost, big_cookies, cookies, big_cookies
from pacman_biscotti import cookis, big_cookis

class CornerTest(unittest.TestCase):
#test per verificare quando pac-man e nel angolo
    def test_corner_pacman(self):
        a = Arena((232, 280))
        p = PacMan(a, (8,8))
        p.move()
        self.assertTrue(p.position() == (8, 8))

    def test_corner_ghost(self):
        a = Arena((232, 280))
        G = Ghost(a, (8,8), 0)
        G._dx, G._dy = -2, 0 
        G.move()
        self.assertTrue(G.position() == (8, 10))

class PacMan_Collision_Test(unittest.TestCase):
# test collisione pacman con il fantasma 
    def test_pacman_collide_ghost(self):
        a = Arena((232, 280))
        p = PacMan(a, (8,8))
        G = Ghost(a, (8,8), 0)
        p.collide(G)
        self.assertTrue(p.collide(G) == a.remove(p))

#tetst collisione pacman in modalita power up con un fantasma
    def test_suepr_pacman_collide_ghost(self):
        a = Arena((232, 280))
        p = PacMan(a, (8,8))
        p._pacman_powerup = True
        G = Ghost(a, (8,8), 0)
        p.collide(G)
        self.assertTrue(p.collide(G) == a.remove(p))

#tetst per decrementare la vita di pacman 
    def test_pacman_collide_life(self):
        a = Arena((232, 280))
        p = PacMan(a, (8, 8))
        g = Ghost(a, (8, 8), 0)
        p._pacman_powerup = False
        p.collide(g)
        p.collide(g) 
        self.assertTrue(p.lives() == 2)

#tetst per verificare lo spown
    def test_pacman_collide_position(self):
        a = Arena((232, 280))
        p = PacMan(a, (8, 8))
        G = Ghost(a, (8,8), 0)
        p._pacman_powerup = False
        p.collide(G)

        self.assertTrue(p.position() == (112, 88))


if __name__ == '__main__':
    unittest.main()
  