#  The chess board that will be used in this project
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
        self._board = [[ChessPiece(None, None) for x in range(self._xRange)] for y in range(self._yRange)]

    """Returns the board"""
    def board(self):
        return self._board

    """Returns the piece at the specified index."""
    def piece_at_index(self, x, y):
        if x > 0 & x < self._xRange & y > 0 & y < self._yRange:
            return self._board[x][y]
        return None

