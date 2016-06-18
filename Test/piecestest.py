import unittest
from Models.Pieces.chesspiece import *
from Models.Pieces.teamcolor import *
from Models.Pieces.piecetype import *


class PiecesTest(unittest.TestCase):

    def test_PawnInitialize(self):
        pawn = Pawn(TeamColor.white, (0, 5))
        self.assertEqual(pawn.get_team(), TeamColor.white)
        self.assertEqual(pawn.get_position(), (0, 5))
        self.assertEqual(pawn.get_type(), PieceType.pawn)

    def test_PawnSetPosition(self):
        pawn = Pawn(TeamColor.white, (4, 3))
        pawn.set_position((4, 4))
        self.assertEqual(pawn.get_position(), (4, 4))

    def test_PawnSetTeam(self):
        pawn = Pawn(TeamColor.black, (6, 6))
        pawn.set_team(TeamColor.white)
        self.assertEqual(pawn.get_team(), TeamColor.white)
        pawn.set_team(TeamColor.black)
        self.assertEqual(pawn.get_team(), TeamColor.black)

    def test_PawnInitialMoveWhite(self):
        board = Board(8, 8)
        pawn = Pawn(TeamColor.white, (0, 1))
        board.set_piece_at_index(pawn.get_position(), pawn)
        moves = pawn.get_moves(board)
        self.assertListEqual([(0, 2), (0, 3)], moves)
        self.assertEqual(len(moves), 2)

    def test_PawnInitialMoveWhite(self):
        board = Board(8, 8)
        pawn = Pawn(TeamColor.white, (0, 2))
        board.set_piece_at_index(pawn.get_position(), pawn)
        moves = pawn.get_moves(board)
        self.assertListEqual([(0, 3)], moves)

    def test_PawnInitialMoveBlack(self):
        board = Board(8, 8)
        pawn = Pawn(TeamColor.black, (6, 6))
        board.set_piece_at_index(pawn.get_position(), pawn)
        moves = pawn.get_moves(board)
        self.assertListEqual([(6, 5), (6, 4)], moves)


