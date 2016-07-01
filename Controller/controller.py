from Models.GameModel.gamemodel import *
from View.view import Chess


class GameController:
    _game_model = None
    _game_view = None

    def __init__(self):
        self._game_model = GameModel(self)
        self._game_view = Chess()
        self._game_view.set_container(self)
        self._game_view.build()
        for l in self._game_model.get_board().get_board():
            for piece in l:
                self._game_view.get_board().set_piece(piece)
        self._game_view.run()

    def check_move(self, origin, destination):
        a = self._game_model.move(origin, destination)
        if a == MoveOptions.in_check:
            # do something
            return False
        elif a == MoveOptions.invalid_destination:
            # do something
            return False
        elif a == MoveOptions.moved:
            self.set_turn()
            return True
        return False

    def remove_piece(self, piece):
        self._game_view.remove_piece(piece)

    def restart(self):
        """Method for the view to call when it wants to restart"""
        self._game_model.restart()
        self._game_view.get_board().delete_all_pieces()
        self.add_all_pieces()
        self._game_view.get_board().place_pieces(self._game_view.get_board().get_length())
        self.set_turn()
        return True

    def add_all_pieces(self):
        for l in self._game_model.get_board().get_board():
            for piece in l:
                self._game_view.get_board().set_piece(piece)

    def checkmate(self, winning_team):
        """Method for the model to call when checkmate happens"""
        self._game_view.display_checkmate(winning_team)

    def stalemate(self):
        """Method for the model to call when a stalemate happens"""
        self._game_view.display_stalemate()

    def in_check(self, position):
        """Method for model to call when a player is in check"""
        self._game_view.get_board().highlight_position(position)
        return True

    def undo(self):
        if self._game_model.undo() is True:
            self._game_view.get_board().delete_all_pieces()
            self.add_all_pieces()
            self._game_view.get_board().place_pieces(self._game_view.get_board().get_length())
            self.set_turn()
            return True
        return False

    def redo(self):
        if self._game_model.redo() is True:
            self._game_view.get_board().delete_all_pieces()
            self.add_all_pieces()
            self._game_view.get_board().place_pieces(self._game_view.get_board().get_length())
            self.set_turn()
            return True
        return False

    def set_turn(self):
        self._game_view.set_turn(self._game_model._turn)
