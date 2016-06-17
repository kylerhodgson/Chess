class ChessPiece:

    """Todo: check inputs piece_type and team_color to make sure that they have correct values"""
    def __init__(self, piece_type, team_color):
        self._pieceType = piece_type
        self._team = team_color

    def type(self):
        return self._pieceType

    def team(self):
        return self._team
