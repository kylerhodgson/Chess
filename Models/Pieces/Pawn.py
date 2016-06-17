from .chesspiece import ChessPiece


class Pawn(ChessPiece):

    def __init__(self, team_color, position):
        self._pieceType = "pawn"
        self._team = team_color
        self._position = position

    """Calculates moves that this piece can do based on current position and team"""
    def moves(self):
        possible_moves = []
        if self._team == "white":
            if self._position[1] == 1:
                possible_moves.append((self._position[0], 2))
                possible_moves.append((self._position[0], 3))
            else:
                possible_moves.append((self._position[0], self._position[1] + 1))
        elif self._team == "black":
            if self._position[1] == 6:
                possible_moves.append((self._position[0], 5))
                possible_moves.append((self._position[0], 4))
            else:
                possible_moves.append((self._position[0], self._position[1] - 1))
        return possible_moves

