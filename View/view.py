from kivy.app import App
from View.gameboard import BoardWidget


class Chess(App):
    _board = None
    _container = None

    def set_container(self, container):
        self._container = container

    def build(self):
        self._board = BoardWidget(self._container)
        return self._board

    def get_board(self):
        return self._board

    def remove_piece(self, piece):
        self._board.delete_piece(piece)
