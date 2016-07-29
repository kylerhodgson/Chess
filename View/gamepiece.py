from Models.GameModel.Pieces.chesspiece import *
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter


class Piece(Scatter):
    _length = None
    _origin = None
    _im = None
    _container = None

    def __init__(self, container, piece, length, **kwargs):
        self._origin = piece.get_position()
        self._length = length
        self._container = container
        super(Piece, self).__init__(**kwargs)
        self.resize(length)
        self.set_position(self._origin, length)
        self.auto_bring_to_front = True
        self._im = self.get_image(piece)
        if self._im is not None:
            self._im.size_hint = None, None
            self._im.size = length / 8, length / 8
            self._im.center = self._im.size[0] / 2, self._im.size[1] / 2
            self.add_widget(self._im)
        self.id = str(self._origin)

    def resize(self, length):
        self.size_hint = None, None
        self._length = length
        self.size = length / 8, length / 8
        self.set_position(self._origin, length)
        self.resize_im()

    def resize_im(self):
        if self._im is not None:
            self._im.size_hint = None, None
            self._im.size = self._length / 8, self._length / 8
            self._im.center = self._im.size[0] / 2, self._im.size[1] / 2

    @staticmethod
    def get_image(piece):
        if piece is None:
            return None
        im = None
        if piece.get_type() == PieceType.pawn:
            im = Image(source='View/Images/pawn.png')
        elif piece.get_type() == PieceType.bishop:
            im = Image(source='View/Images/bishop.png')
        elif piece.get_type() == PieceType.rook:
            im = Image(source='View/Images/rook.png')
        elif piece.get_type() == PieceType.knight:
            im = Image(source='View/Images/knight.png')
        elif piece.get_type() == PieceType.queen:
            im = Image(source='View/Images/queen.png')
        elif piece.get_type() == PieceType.king:
            im = Image(source='View/Images/king.png')
        if im is not None:
            im.color = (1, .6, .6, 1) if piece.get_team() == TeamColor.black else (.7, .7, 1, .9)
        return im

    def set_position(self, position, length):
        self.center = (position[0] * length / 8 + length / 16, position[1] * length / 8 + length / 16)

    def get_position(self):
        return self.pos

    def adjust_position(self):
        center = self.center
        x = int(center[0] / (self._length/8))
        y = int(center[1] / (self._length/8))
        if not self._container.check_move(self._origin, (x, y)):
            self.set_position(self._origin, self._length)
            return
        self.set_position((x, y), self._length)
        self._origin = (x, y)

    def on_touch_up(self, touch):
        self.adjust_position()
        return super(Piece, self).on_touch_up(touch)
