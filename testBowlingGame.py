import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):
    def testCreateGame(self):
        game = BowlingGame.BowlingGame()
        
    def testGutterGale(self):
        game = BowlingGame.BowlingGame()
        for i in range(20):
            game.roll(0)
        assert game.score() == 0