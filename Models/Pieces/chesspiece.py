class ChessPiece:

    """Todo: check inputs piece_type and team_color to make sure that they have correct values"""
    def __init__(self, piece_type, team_color, x_value, y_value):
        self._pieceType = piece_type
        self._team = team_color
        self._position = (x_value, y_value)

    def type(self):
        return self._pieceType

    def team(self):
        return self._team

    def position(self):
        return self._position
