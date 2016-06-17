#  The chess board that will be used in this project
# The board is 0 based in the lower left hand corner
# The White team should start at the bottom, the black at the top
from Models.Pieces.chesspiece import ChessPiece


class Board:

    """Standard initializer. Makes a normal size board"""
    def __init__(self):
        self._xRange = 8
        self._yRange = 8
        self._board = []
        self.setboard()

    """Another initializer: can make a bigger board"""
    def __init__(self, x_value, y_value):
        self._xRange = x_value
        self._yRange = y_value
        self._board = []
        self.setboard()

    """Creates the board with the specified size"""
    def set_board(self):
        self._board = [[None for x in range(self._xRange)] for y in range(self._yRange)]

    """Returns the board"""
    def board(self):
        return self._board

    """Returns the piece at the specified index."""
    def get_piece_at_index(self, x, y):
        if self.is_inside_board((x, y)):
            return self._board[x][y]
        return None

    def get_piece_at_index(self, position):
        if self.is_inside_board(position):
            return self.piece_at_index(position[0], position[1])

    def set_piece_at_index(self, position, piece):
        self._board[position[0]][position[1]] = piece

    def is_inside_board(self, position):
        return position[0] >= 0 & position[0] < self._xRange & position[1] >= 0 & position[1] < self._yRange

