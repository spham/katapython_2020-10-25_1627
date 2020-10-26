import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):
    
    def setUp(self):
        self.game = BowlingGame.BowlingGame()
    def testCreateGame(self):
        self.game = BowlingGame.BowlingGame()
        
    def testGutterGale(self):
        self.rollMany(0,20)
        assert self.game.score() == 0
    def testAllOnes(self):
        self.rollMany(1,20)
        assert self.game.score() == 20
        
    def rollMany(self, pins, rolls):
        for i in range(rolls):
            self.game.roll(pins)
    def testOneSpare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0,17)
        assert self.game.score() == 16
