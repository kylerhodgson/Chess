from Models.GameModel.Pieces.teamcolor import TeamColor
from Models.GameModel.Pieces.piecetype import PieceType


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

    def set_position(self, pos):
        self._position = pos


class Pawn(ChessPiece):

    def __init__(self, team_color, position):
        self._pieceType = PieceType.pawn
        if team_color != TeamColor.black | team_color != TeamColor.white:
            """Need to somehow say that the value is invalid"""
        self._team = team_color
        self._position = position

    """Calculates moves that this piece can do based on current position and team"""
    def get_moves(self, board):
        possible_moves = []
        x = self._position[0]
        y = self._position[1]
        if self._team == TeamColor.white:
            if y == 1 and board.get_piece_at_index((x, y + 1)) is None:
                possible_moves.append((x, y + 1))
                if board.get_piece_at_index((x, y + 2)) is None:
                    possible_moves.append((x, y + 2))
            elif board.get_piece_at_index((x, y + 1)) is None:
                possible_moves.append((x, y + 1))
            """will this call a null reference exception? if there is no piece at that spot in the board?"""
            if board.get_piece_at_index((x + 1, y + 1)) is not None \
                    and board.get_piece_at_index((x + 1, y + 1)).get_team() == TeamColor.black:
                possible_moves.append((x + 1, y + 1))
            if board.get_piece_at_index((x - 1, y + 1)) is not None \
                    and board.get_piece_at_index((x - 1, y + 1)).get_team() == TeamColor.black:
                possible_moves.append((x - 1, y + 1))
        elif self._team == TeamColor.black:
            if y == 6 and board.get_piece_at_index((x, y - 1)) is None:
                possible_moves.append((x, y - 1))
                if board.get_piece_at_index((x, y - 2)) is None:
                    possible_moves.append((x, y - 2))
            elif board.get_piece_at_index((x, y - 1)) is None:
                possible_moves.append((x, y - 1))
            if board.get_piece_at_index((x + 1, y - 1)) is not None \
                    and board.get_piece_at_index((x + 1, y - 1)).get_team() == TeamColor.white:
                possible_moves.append((x + 1, y - 1))
            if board.get_piece_at_index((x - 1, y - 1)) is not None \
                    and board.get_piece_at_index((x - 1, y - 1)).get_team() == TeamColor.white:
                possible_moves.append((x - 1, y - 1))
        return possible_moves


class Bishop(ChessPiece):

    def __init__(self, team_color, position):
        self._pieceType = PieceType.bishop
        self._team = team_color
        self._position = position

    """Calculates moves that this piece can do based on current position and team"""
    def get_moves(self, board):
        possible_moves = self.moves_helper(1, board, 1, 1, 1, 1)
        return possible_moves

    def moves_helper(self, num, board, bl, br, ul, ur):
        possible_moves = []
        xl = self._position[0] - num
        xr = self._position[0] + num
        yb = self._position[1] - num
        yu = self._position[1] + num
        if bl and xl >= 0 and yb >= 0:
            if board.get_piece_at_index((xl, yb)) is not None:
                if board.get_piece_at_index((xl, yb)).get_team() != self.get_team():
                    possible_moves += [(xl, yb)]
            else:
                possible_moves += [(xl, yb)]
                possible_moves += self.moves_helper(num+1, board, 1, 0, 0, 0)
        if br and xr < 8 and yb >= 0:
            if board.get_piece_at_index((xr, yb)) is not None:
                if board.get_piece_at_index((xr, yb)).get_team() != self.get_team():
                    possible_moves.append((xr, yb))
            else:
                possible_moves += [(xr, yb)]
                possible_moves += self.moves_helper(num+1, board, 0, 1, 0, 0)
        if ul and xl >= 0 and yu < 8:
            if board.get_piece_at_index((xl, yu)) is not None:
                if board.get_piece_at_index((xl, yu)).get_team() != self.get_team():
                    possible_moves += [(xl, yu)]
            else:
                possible_moves += [(xl, yu)]
                possible_moves += (self.moves_helper(num + 1, board, 0, 0, 1, 0))
        if ur and xr < 8 and yu < 8:
            if board.get_piece_at_index((xr, yu)) is not None:
                if board.get_piece_at_index((xl, yb)).get_team() != self.get_team():
                    possible_moves += [(xr, yu)]
            else:
                possible_moves += [(xr, yu)]
                possible_moves += self.moves_helper(num + 1, board, 0, 0, 0, 1)
        return possible_moves



