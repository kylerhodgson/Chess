import unittest
from Models.GameModel.gamemodel import *


class GameModelTest(unittest.TestCase):
    def test_GameModelInit(self):
        game = GameModel()
        self.assertTrue(game.get_board() is not None)
        self.assertFalse(game.get_black_in_check())
        self.assertFalse(game.get_white_in_check())
