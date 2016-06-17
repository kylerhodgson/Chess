# Game Model Class
from Models.moveoptions import MoveOptions
from Models.Pieces.chesspiece import *
from Models.Resources.linkedlist import LinkedList


class GameModel:

    def __init__(self):
        self._gameBoard = Board()
        self.initialize_game()
        self._white_king_trouble = False
        self._black_king_trouble = False
        self._black_king_position = (0,0)
        self._white_king_position = (0,0)
        self._turn = TeamColor.white
        self._moveHistory = LinkedList()

    def move(self, origin, destination):
        piece = self._gameBoard.get_piece_at_index(origin)
        if piece is None | piece.get_team() != self._turn:
            return
        piece2 = self._gameBoard.get_piece_at_index(destination)
        _moves = piece.moves()
        if not _moves.contains(destination):
            return MoveOptions.invalid_destination
        else:
            piece.set_position(destination)
            self._gameBoard.set_piece_at_index(origin, None)
            self._gameBoard.set_piece_at_index(destination, piece)
            """If in check, needs to check to see if move gets it out of check"""
            """If not in check, needs to check to see if move gets player into check"""
            if self.check_for_check():
                piece.set_position(origin)
                self._gameBoard.set_piece_at_index(origin, piece)
                self._gameBoard.set_piece_at_index(destination, piece2)
                return MoveOptions.in_check
            """If move is different than what is next in the history, then delete the future moves in the history"""
            return MoveOptions.moved

    def check_for_check(self):
        if self._turn == TeamColor.white:
            return self.get_all_black_moves().contains(self._white_king_position)
        return self.get_all_white_moves().contains(self._black_king_position)

    def initialize_game(self):
        """TODO: Finish this"""
        """set pawns"""
        for i in range(8):
            white_pawn = Pawn(TeamColor.white, (i, 1))
            self._gameBoard.set_piece_at_index((i, 1), white_pawn)
            black_pawn = Pawn(TeamColor.black, (i, 6))
            self._gameBoard.set_piece_at_index((i, 6), black_pawn)
        """set the rest of the pieces"""

    def get_all_black_moves(self):
        moves = []
        for x in range(8):
            for y in range(8):
                piece = self._gameBoard.get_piece_at_index(x, y)
                if piece is not None & piece.get_team() == TeamColor.black:
                    moves.append(piece.moves())
                """Do I need to reset the position here or somewhere else?"""
                if piece is not None & piece.get_team() == TeamColor.white & piece.get_type() == PieceType.king:
                    self._white_king_position = piece.get_position()

    def get_all_white_moves(self):
        """TODO: Implement this"""

    def undo(self):
        """TODO: reset the pointer in the linked list to one node before the current one
            and reset the game board"""
        return False

    def redo(self):
        """If there is a move that can be redone, redo it.
            Did we even want a redo function?"""
        return False

    def create_move_node(self):
        """Linked list node for tracking history for undo/redo"""
        return False