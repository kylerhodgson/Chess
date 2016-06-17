from .chesspiece import ChessPiece


class Bishop(ChessPiece):

    def __init__(self, team_color, position):
        self._pieceType = "bishop"
        self._team = team_color
        self._position = position

    """Calculates moves that this piece can do based on current position and team"""
    def moves(self):
        possible_moves = self.moves_helper(1)
        """In the future, we will need to check if there are obstructions to these possible moves"""
        return possible_moves

    def moves_helper(self, num):
        possible_moves = []
        x_low = self._position[0] - num
        x_high = self._position[0] + num
        y_low = self._position[1] - num
        y_high = self._position[1] + num
        if x_low < 0 & x_high > 7 & y_low < 0 & y_high > 7:
            return possible_moves
        if x_low > 0 & y_low > 0:
            possible_moves.append((x_low, y_low))
        if x_low > 0 & y_high < 8:
            possible_moves.append((x_low, y_high))
        if x_high < 8 & y_low > 0:
            possible_moves.append((x_high, y_low))
        if x_high < 8 & y_high < 8:
            possible_moves.append((x_high, y_high))
        possible_moves.append(self.moves_helper(num + 1))
        return possible_moves
