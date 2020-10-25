import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):
    
    def setUp(self):
        self.game = BowlingGame.BowlingGame()
    
    def testCreateGame(self):
        game = BowlingGame.BowlingGame()
        
    def testGutterGale(self):
        for i in range(20):
            self.game.roll(0)
        assert self.game.score() == 0
    def testAllOnes(self):
        for i in range(20):
            self.game.roll(1)
        assert self.game.score() == 20
        