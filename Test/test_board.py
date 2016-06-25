import unittest

from Models.GameModel.board import *
from Models.GameModel.Pieces.chesspiece import *


class GameBoardTest(unittest.TestCase):
    def test_BoardSetup(self):
        board = Board()
        self.assertTrue(board.is_inside_board((2, 2)))
        self.assertTrue(board.is_inside_board((0, 0)))
        self.assertTrue(board.is_inside_board((7, 7)))
        self.assertTrue(board.is_inside_board((7, 0)))
        self.assertTrue(board.is_inside_board((0, 7)))
        self.assertFalse(board.is_inside_board((10, 2)))
        self.assertFalse(board.is_inside_board((8, 8)))

    def test_BoardSetAndGetPieces(self):
        board = Board()
        pawn = Pawn(TeamColor.white, (6, 3))
        board.set_piece_at_index(pawn.get_position(), pawn)
        self.assertEqual(pawn, board.get_piece_at_index(pawn.get_position()))