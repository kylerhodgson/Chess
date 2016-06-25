# Game Model Class
from Models.GameModel.Resources.linkedlist import *
from Models.GameModel.moveoptions import MoveOptions
from Models.GameModel.Pieces.chesspiece import *
from Models.GameModel.board import *


class GameModel:

    def __init__(self, container):
        self._gameBoard = Board()
        self.initialize_game()
        self._white_king_in_check = False
        self._black_king_in_check = False
        self._black_king_position = (0, 0)
        self._white_king_position = (0, 0)
        self._turn = TeamColor.white
        self._move_history = LinkedList()
        self._container = container

    def move(self, origin, destination):
        old_piece1 = self._gameBoard.get_piece_at_index(origin)
        old_piece2 = self._gameBoard.get_piece_at_index(destination)
        old_turn = self._turn
        new_turn = TeamColor.white if self._turn == TeamColor.black else TeamColor.black
        piece = self._gameBoard.get_piece_at_index(origin)
        if piece is None or piece.get_team() != self._turn:
            return
        piece2 = self._gameBoard.get_piece_at_index(destination)
        _moves = piece.get_moves(self._gameBoard)
        if destination not in _moves:
            return MoveOptions.invalid_destination
        else:
            piece.set_position(destination)
            self._gameBoard.set_piece_at_index(origin, None)
            self._gameBoard.set_piece_at_index(destination, piece)
            """If in check, needs to check to see if move gets it out of check
            If not in check, needs to check to see if move gets player into check"""
            if self.check_for_check():
                piece.set_position(origin)
                self._gameBoard.set_piece_at_index(origin, piece)
                self._gameBoard.set_piece_at_index(destination, piece2)
                return MoveOptions.in_check
            """If move is different than what is next in the history, then delete the future moves in the history"""
            new_piece1 = self._gameBoard.get_piece_at_index(origin)
            new_piece2 = self._gameBoard.get_piece_at_index(destination)
            self._move_history.add_next(LinkedListNode(None, None, MoveData(old_piece1, old_piece2, new_piece1, new_piece2, old_turn, new_turn)))
            self._turn = TeamColor.white if self._turn == TeamColor.black else TeamColor.black
            if old_piece2 is not None:
                self._container.remove_piece(old_piece2)
            return MoveOptions.moved

    def check_for_check(self):
        if self._turn == TeamColor.white:
            if self._white_king_position in self.get_all_black_moves():
                return True
        elif self._black_king_position in self.get_all_white_moves():
            return True
        return False

    def initialize_game(self):
        """TODO: Finish this"""
        # set pawns
        for i in range(8):
            white_pawn = Pawn(TeamColor.white, (i, 1))
            self._gameBoard.set_piece_at_index((i, 1), white_pawn)
            black_pawn = Pawn(TeamColor.black, (i, 6))
            self._gameBoard.set_piece_at_index((i, 6), black_pawn)
        # set the rest of the pieces

    def get_all_black_moves(self):
        moves = []
        for x in range(8):
            for y in range(8):
                piece = self._gameBoard.get_piece_at_index((x, y))
                if piece is not None and piece.get_team() == TeamColor.black:
                    moves += piece.get_moves(self._gameBoard)
                """Do I need to reset the position here or somewhere else?"""
                if piece is not None and piece.get_team() == TeamColor.white & piece.get_type() == PieceType.king:
                    self._white_king_position = piece.get_position()
        return moves

    def get_all_white_moves(self):
        """TODO: Implement this"""
        moves = []
        return moves

    def undo(self):
        if self._move_history.move_previous():
            piece1 = self._move_history.get_data().get_old_piece1()
            piece2 = self._move_history.get_data().get_old_piece2()
            self._gameBoard.set_piece_at_index(piece1.get_position(), piece1)
            self._gameBoard.set_piece_at_index(piece2.get_position(), piece2)
            self._turn = self._move_history.get_data().get_old_turn()
            return True
        return False

    def redo(self):
        if self._move_history.move_next():
            piece1 = self._move_history.get_data().get_new_piece1()
            piece2 = self._move_history.get_data().get_new_piece2()
            self._gameBoard.set_piece_at_index(piece1.get_position(), piece1)
            self._gameBoard.set_piece_at_index(piece2.get_position(), piece2)
            self._turn = self._move_history.get_data().get_new_turn()
            return True
        return False

    def get_board(self):
        return self._gameBoard

    def get_white_in_check(self):
        return self._white_king_in_check

    def get_black_in_check(self):
        return self._black_king_in_check
