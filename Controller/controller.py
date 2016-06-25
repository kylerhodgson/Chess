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
        for list in self._game_model.get_board().get_board():
            for piece in list:
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
            # do something
            return True
        return False

    def remove_piece(self, piece):
        self._game_view.remove_piece(piece)
