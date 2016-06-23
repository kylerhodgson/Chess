import unittest
from Models.GameModel.Pieces.chesspiece import *
from Models.GameModel.board import *


class PawnPieceTest(unittest.TestCase):

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
        board = Board()
        pawn = Pawn(TeamColor.white, (0, 1))
        board.set_piece_at_index(pawn.get_position(), pawn)
        moves = pawn.get_moves(board)
        self.assertListEqual([(0, 2), (0, 3)], moves)
        self.assertEqual(len(moves), 2)

    def test_PawnInitialMoveWhite(self):
        board = Board()
        pawn = Pawn(TeamColor.white, (0, 2))
        board.set_piece_at_index(pawn.get_position(), pawn)
        moves = pawn.get_moves(board)
        self.assertListEqual([(0, 3)], moves)

    def test_PawnInitialMoveBlack(self):
        board = Board()
        pawn = Pawn(TeamColor.black, (6, 6))
        board.set_piece_at_index(pawn.get_position(), pawn)
        moves = pawn.get_moves(board)
        self.assertListEqual([(6, 5), (6, 4)], moves)


class BishopPieceTests(unittest.TestCase):
    def test_BishopInitialize(self):
        bishop = Bishop(TeamColor.black, (5, 5))
        self.assertEqual(bishop.get_team(), TeamColor.black)
        self.assertEqual(bishop.get_position(), (5, 5))
        self.assertEqual(bishop.get_type(), PieceType.bishop)

    def test_BishopMove(self):
        bishop = Bishop(TeamColor.black, (5, 5))
        board = Board()
        board.set_piece_at_index(bishop.get_position(), bishop)
        moves = bishop.get_moves(board)
        self.assertListEqual(
            [(4, 4), (3, 3), (2, 2), (1, 1), (0, 0), (6, 4), (7, 3), (4, 6), (3, 7), (6, 6), (7, 7)], moves)

    def test_BishopMove2(self):
        bishop = Bishop(TeamColor.black, (5, 5))
        bishop2 = Bishop(TeamColor.white, (2, 2))
        bishop3 = Bishop(TeamColor.black, (4, 6))
        board = Board()
        board.set_piece_at_index(bishop.get_position(), bishop)
        board.set_piece_at_index(bishop2.get_position(), bishop2)
        board.set_piece_at_index(bishop3.get_position(), bishop3)
        moves = bishop.get_moves(board)
        self.assertListEqual(
            [(4, 4), (3, 3), (2, 2), (6, 4), (7, 3), (6, 6), (7, 7)], moves)

    def test_BishopMove3(self):
        bishop = Bishop(TeamColor.black, (1, 3))
        bishop2 = Bishop(TeamColor.black, (2, 2))
        bishop3 = Bishop(TeamColor.black, (3, 1))
        pawn = Pawn(TeamColor.black, (3, 3))
        pawn2 = Pawn(TeamColor.black, (1, 1))
        board = Board()
        board.set_piece_at_index(bishop.get_position(), bishop)
        board.set_piece_at_index(bishop2.get_position(), bishop2)
        board.set_piece_at_index(bishop3.get_position(), bishop3)
        board.set_piece_at_index(pawn.get_position(), pawn)
        board.set_piece_at_index(pawn2.get_position(), pawn2)
        moves = bishop2.get_moves(board)
        self.assertListEqual([], moves)
        self.assertEqual(len(bishop3.get_moves(board)), 6)
        self.assertEqual(len(pawn.get_moves(board)), 1)
        self.assertEqual(len(bishop.get_moves(board)), 6)
