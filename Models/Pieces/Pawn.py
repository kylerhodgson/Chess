from .chesspiece import ChessPiece

class Pawn(ChessPiece):

    def __init__(self, team_color, position):
        self._pieceType = "pawn"
        self._team = team_color
        self._position = position

    def moves(self):
        _moves = []
        return _moves

    