from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color
from kivy.graphics.vertex_instructions import Rectangle
from View.gamepiece import Piece


class BoardWidget(FloatLayout):
    piece_map = dict()
    _container = None

    def __init__(self, container, **kwargs):
        super(BoardWidget, self).__init__(**kwargs)
        self._container = container
        with self.canvas.before:
            Color(0, 0, 0, 1)
            self.rectangle = Rectangle(pos=(0, 0), size=self.size)
            length = self.get_length()
            self.draw_board(length)
        self.place_pieces(length)

    def on_size(self, *args):
        self.rectangle.size = self.size
        self.canvas.clear()
        self.clear_widgets()
        length = self.get_length()
        with self.canvas.before:
            self.draw_board(length)
        self.place_pieces(length)

    def draw_board(self, length):
        Color(0, 0, 0, 1)
        Rectangle(pos=(0, 0), size=self.size)
        for i in range(8):
            for j in range(8):
                Color(.95, .95, .95, .9) if (i + j) % 2 == 0 else Color(.3, .3, .3, .9)
                Rectangle(pos=(j * length / 8, abs(i - 7) * length / 8),
                          size=(length / 8, length / 8))

    def place_pieces(self, length):
        for piece in self.piece_map.values():
            if piece is not None:
                piece.resize(length)
                self.add_widget(piece)

    def set_piece(self, piece):
        if piece is None:
            return
        length = self.get_length()
        p = Piece(container=self._container, length=length, piece=piece, do_rotation=False, do_scale=False)
        self.piece_map[piece.__hash__()] = p

    def get_length(self):
        return self.rectangle.size[0] if self.rectangle.size[0] < self.rectangle.size[1] else self.rectangle.size[1]

    def get_piece(self, piece):
        return self.piece_map[piece.__hash__()]

    def delete_piece(self, piece):
        self.remove_widget(self.piece_map[piece.__hash__()])
        self.piece_map[piece.__hash__()] = None

    def delete_all_pieces(self):
        for piece in self.piece_map.values():
            if piece is not None:
                self.remove_widget(piece)
        self.piece_map.clear()

    def highlight_position(self, position):
        """TODO: Highlight a position for when a king is in check"""
        return True