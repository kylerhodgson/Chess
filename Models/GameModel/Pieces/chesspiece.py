from Models.GameModel.Pieces.teamcolor import TeamColor
from Models.GameModel.Pieces.piecetype import PieceType


class ChessPiece:

    def __init__(self, piece_type, team_color, x_value, y_value):
        self._pieceType = piece_type
        self._team = team_color
        self._position = (x_value, y_value)
        self._id = None

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

    def get_id(self):
        return self._id


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
        x_plus = x + 1
        x_minus = x - 1
        y = self._position[1]
        y_plus = y + 1
        y_minus = y - 1
        if self._team == TeamColor.white:
            if y == 1 and board.get_piece_at_index((x, y + 1)) is None:
                possible_moves.append((x, y + 1))
                if board.get_piece_at_index((x, y + 2)) is None:
                    possible_moves.append((x, y + 2))
            elif y_plus < 8 and board.get_piece_at_index((x, y + 1)) is None:
                possible_moves.append((x, y + 1))
            if x_plus < 8 and y_plus < 8 and board.get_piece_at_index((x + 1, y + 1)) is not None \
                    and board.get_piece_at_index((x + 1, y + 1)).get_team() == TeamColor.black:
                possible_moves.append((x + 1, y + 1))
            if x_minus >= 0 and y_plus < 8 and board.get_piece_at_index((x - 1, y + 1)) is not None \
                    and board.get_piece_at_index((x - 1, y + 1)).get_team() == TeamColor.black:
                possible_moves.append((x - 1, y + 1))
        elif self._team == TeamColor.black:
            if y == 6 and board.get_piece_at_index((x, y - 1)) is None:
                possible_moves.append((x, y - 1))
                if board.get_piece_at_index((x, y - 2)) is None:
                    possible_moves.append((x, y - 2))
            elif y_minus >= 0 and board.get_piece_at_index((x, y - 1)) is None:
                possible_moves.append((x, y - 1))
            if x_plus < 8 and y_minus >= 0 and board.get_piece_at_index((x + 1, y - 1)) is not None \
                    and board.get_piece_at_index((x + 1, y - 1)).get_team() == TeamColor.white:
                possible_moves.append((x + 1, y - 1))
            if x_minus >= 0 and y_minus >= 0 and board.get_piece_at_index((x - 1, y - 1)) is not None \
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
                if board.get_piece_at_index((xr, yu)).get_team() != self.get_team():
                    possible_moves += [(xr, yu)]
            else:
                possible_moves += [(xr, yu)]
                possible_moves += self.moves_helper(num + 1, board, 0, 0, 0, 1)
        return possible_moves


class Rook(ChessPiece):
    def __init__(self, team_color, position):
        self._pieceType = PieceType.rook
        self._team = team_color
        self._position = position

    def get_moves(self, board):
        possible_moves = self.moves_helper(1, board, 1, 1, 1, 1)
        return possible_moves

    def moves_helper(self, num, board, up, down, left, right):
        possible_moves = []
        x = self._position[0]
        y = self._position[1]
        y_up = self._position[1] + num
        y_down = self._position[1] - num
        x_right = self._position[0] + num
        x_left = self._position[0] - num
        if up and y_up < 8:
            piece = board.get_piece_at_index((x, y_up))
            if piece is not None and piece.get_team() != self.get_team():
                possible_moves += [(x, y_up)]
            elif piece is None:
                possible_moves += [(x, y_up)]
                possible_moves += self.moves_helper(num+1, board, 1, 0, 0, 0)
        if down and y_down >= 0:
            piece = board.get_piece_at_index((x, y_down))
            if piece is not None and piece.get_team() != self.get_team():
                possible_moves += [(x, y_down)]
            elif piece is None:
                possible_moves += [(x, y_down)]
                possible_moves += self.moves_helper(num + 1, board, 0, 1, 0, 0)
        if left and x_left >= 0:
            piece = board.get_piece_at_index((x_left, y))
            if piece is not None and piece.get_team() != self.get_team():
                possible_moves += [(x_left, y)]
            elif piece is None:
                possible_moves += [(x_left, y)]
                possible_moves += self.moves_helper(num + 1, board, 0, 0, 1, 0)
        if right and x_right < 8:
            piece = board.get_piece_at_index((x_right, y))
            if piece is not None and piece.get_team() != self.get_team():
                possible_moves += [(x_right, y)]
            elif piece is None:
                possible_moves += [(x_right, y)]
                possible_moves += self.moves_helper(num + 1, board, 0, 0, 0, 1)
        return possible_moves


class Queen(ChessPiece):
    def __init__(self, team_color, position):
        self._pieceType = PieceType.queen
        self._team = team_color
        self._position = position

    def get_moves(self, board):
        possible_moves = self.moves_helper_straight(1, board, 1, 1, 1, 1)
        possible_moves += self.moves_helper_diagonal(1, board, 1, 1, 1, 1)
        return possible_moves

    def moves_helper_straight(self, num, board, up, down, left, right):
        possible_moves = []
        x = self._position[0]
        y = self._position[1]
        y_up = self._position[1] + num
        y_down = self._position[1] - num
        x_right = self._position[0] + num
        x_left = self._position[0] - num
        if up and y_up < 8:
            piece = board.get_piece_at_index((x, y_up))
            if piece is not None and piece.get_team() != self.get_team():
                possible_moves += [(x, y_up)]
            elif piece is None:
                possible_moves += [(x, y_up)]
                possible_moves += self.moves_helper_straight(num + 1, board, 1, 0, 0, 0)
        if down and y_down >= 0:
            piece = board.get_piece_at_index((x, y_down))
            if piece is not None and piece.get_team() != self.get_team():
                possible_moves += [(x, y_down)]
            elif piece is None:
                possible_moves += [(x, y_down)]
                possible_moves += self.moves_helper_straight(num + 1, board, 0, 1, 0, 0)
        if left and x_left >= 0:
            piece = board.get_piece_at_index((x_left, y))
            if piece is not None and piece.get_team() != self.get_team():
                possible_moves += [(x_left, y)]
            elif piece is None:
                possible_moves += [(x_left, y)]
                possible_moves += self.moves_helper_straight(num + 1, board, 0, 0, 1, 0)
        if right and x_right < 8:
            piece = board.get_piece_at_index((x_right, y))
            if piece is not None and piece.get_team() != self.get_team():
                possible_moves += [(x_right, y)]
            elif piece is None:
                possible_moves += [(x_right, y)]
                possible_moves += self.moves_helper_straight(num + 1, board, 0, 0, 0, 1)
        return possible_moves

    def moves_helper_diagonal(self, num, board, bl, br, ul, ur):
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
                possible_moves += self.moves_helper_diagonal(num+1, board, 1, 0, 0, 0)
        if br and xr < 8 and yb >= 0:
            if board.get_piece_at_index((xr, yb)) is not None:
                if board.get_piece_at_index((xr, yb)).get_team() != self.get_team():
                    possible_moves.append((xr, yb))
            else:
                possible_moves += [(xr, yb)]
                possible_moves += self.moves_helper_diagonal(num+1, board, 0, 1, 0, 0)
        if ul and xl >= 0 and yu < 8:
            if board.get_piece_at_index((xl, yu)) is not None:
                if board.get_piece_at_index((xl, yu)).get_team() != self.get_team():
                    possible_moves += [(xl, yu)]
            else:
                possible_moves += [(xl, yu)]
                possible_moves += (self.moves_helper_diagonal(num + 1, board, 0, 0, 1, 0))
        if ur and xr < 8 and yu < 8:
            if board.get_piece_at_index((xr, yu)) is not None:
                if board.get_piece_at_index((xr, yu)).get_team() != self.get_team():
                    possible_moves += [(xr, yu)]
            else:
                possible_moves += [(xr, yu)]
                possible_moves += self.moves_helper_diagonal(num + 1, board, 0, 0, 0, 1)
        return possible_moves


class King(ChessPiece):
    def __init__(self, team_color, position):
        self._pieceType = PieceType.king
        self._team = team_color
        self._position = position

    def get_moves(self, board):
        possible_moves = []
        x = self._position[0]
        y = self._position[1]
        y_plus = y + 1 < 8
        y_minus = y - 1 >= 0
        x_plus = x + 1 < 8
        x_minus = x - 1 >= 0
        if x_plus:
            piece = board.get_piece_at_index((x + 1, y))
            if piece is None or piece.get_team() != self.get_team():
                possible_moves += [(x + 1, y)]
            if y_plus:
                piece = board.get_piece_at_index((x + 1, y + 1))
                if piece is None or piece.get_team() != self.get_team():
                    possible_moves += [(x + 1, y + 1)]
            if y_minus:
                piece = board.get_piece_at_index((x + 1, y - 1))
                if piece is None or piece.get_team() != self.get_team():
                    possible_moves += [(x + 1, y - 1)]
        if x_minus:
            piece = board.get_piece_at_index((x - 1, y))
            if piece is None or piece.get_team() != self.get_team():
                possible_moves += [(x - 1, y)]
            if y_plus:
                piece = board.get_piece_at_index((x - 1, y + 1))
                if piece is None or piece.get_team() != self.get_team():
                    possible_moves += [(x - 1, y + 1)]
            if y_minus:
                piece = board.get_piece_at_index((x - 1, y - 1))
                if piece is None or piece.get_team() != self.get_team():
                    possible_moves += [(x - 1, y - 1)]
        if y_minus:
            piece = board.get_piece_at_index((x, y - 1))
            if piece is None or piece.get_team() != self.get_team():
                possible_moves += [(x, y - 1)]
        if y_plus:
            piece = board.get_piece_at_index((x, y + 1))
            if piece is None or piece.get_team() != self.get_team():
                possible_moves += [(x, y + 1)]
        return possible_moves


class Knight(ChessPiece):
    def __init__(self, team_color, position):
        self._pieceType = PieceType.knight
        self._team = team_color
        self._position = position

    def get_moves(self, board):
        possible_moves = []
        x = self._position[0]
        y = self._position[1]
        x_2 = x + 2 < 8
        x_1 = x + 1 < 8
        x_m2 = x - 2 >= 0
        x_m1 = x - 1 >= 0
        y_2 = y + 2 < 8
        y_1 = y + 1 < 8
        y_m2 = y - 2 >= 0
        y_m1 = y - 1 >= 0
        if x_2:
            if y_1:
                piece = board.get_piece_at_index((x + 2, y + 1))
                if piece is None or piece.get_team() != self.get_team():
                    possible_moves += [(x + 2, y + 1)]
            if y_m1:
                piece = board.get_piece_at_index((x + 2, y - 1))
                if piece is None or piece.get_team() != self.get_team():
                    possible_moves += [(x + 2, y - 1)]
        if x_m2:
            if y_1:
                piece = board.get_piece_at_index((x - 2, y + 1))
                if piece is None or piece.get_team() != self.get_team():
                    possible_moves += [(x - 2, y + 1)]
            if y_m1:
                piece = board.get_piece_at_index((x - 2, y - 1))
                if piece is None or piece.get_team() != self.get_team():
                    possible_moves += [(x - 2, y - 1)]
        if y_2:
            if x_1:
                piece = board.get_piece_at_index((x + 1, y + 2))
                if piece is None or piece.get_team() != self.get_team():
                    possible_moves += [(x + 1, y + 2)]
            if x_m1:
                piece = board.get_piece_at_index((x - 1, y + 2))
                if piece is None or piece.get_team() != self.get_team():
                    possible_moves += [(x - 1, y + 2)]
        if y_m2:
            if x_1:
                piece = board.get_piece_at_index((x + 1, y - 2))
                if piece is None or piece.get_team() != self.get_team():
                    possible_moves += [(x + 1, y - 2)]
            if x_m1:
                piece = board.get_piece_at_index((x - 1, y - 2))
                if piece is None or piece.get_team() != self.get_team():
                    possible_moves += [(x - 1, y - 2)]
        return possible_moves
