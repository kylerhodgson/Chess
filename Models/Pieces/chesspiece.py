class ChessPiece:

    """Todo: check inputs piece_type and team_color to make sure that they have correct values"""
    def __init__(self, piece_type, team_color, x_value, y_value):
        self._pieceType = piece_type
        self._team = team_color
        self._position = (x_value, y_value)

    def get_type(self):
        return self._pieceType

    def get_team(self):
        return self._team

    def set_team(self, team):
        self._team = team

    def get_position(self):
        return self._position

    def set_position(self, x, y):
        self._position = (x, y)
