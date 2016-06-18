from Models.Pieces.teamcolor import TeamColor
from Models.Pieces.piecetype import PieceType
from Models.board import Board


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


class Pawn(ChessPiece):

    def __init__(self, team_color, position):
        self._pieceType = PieceType.pawn
        if team_color != TeamColor.black | team_color != TeamColor.white:
            """Need to somehow say that the value is invalid"""
        self._team = team_color
        self._position = position

    """Calculates moves that this piece can do based on current position and team"""
    def moves(self, board):
        possible_moves = []
        x = self._position[0]
        y = self._position[1]
        if self._team == TeamColor.white:
            if y == 1 & board.get_piece_at_index(x, y + 1) is None:
                possible_moves.append((x, y + 1))
                if board.get_piece_at_index(x, y + 2) is None:
                    possible_moves.append((x, y + 2))
            elif board.get_piece_at_index(x, y + 1) is None:
                possible_moves.append((x, y + 1))
            """will this call a null reference exception? if there is no piece at that spot in the board?"""
            if board.get_piece_at_index(x + 1, y + 1).team == TeamColor.black:
                possible_moves.append((x + 1, y + 1))
            if board.get_piece_at_index(x - 1, y + 1).team == TeamColor.black:
                possible_moves.append((x - 1, y + 1))
        elif self._team == TeamColor.black:
            if y == 6 & board.get_piece_at_index(x, y - 1) is None:
                possible_moves.append((x, y - 1))
                if board.get_piece_at_index(x, y - 2) is None:
                    possible_moves.append((x, y))
            elif board.get_piece_at_index(x, y - 1) is None:
                possible_moves.append((x, y - 1))
            if board.get_piece_at_index(x + 1, y - 1).team == TeamColor.white:
                possible_moves.append((x + 1, y - 1))
            if board.get_piece_at_index(x - 1, y - 1).team == TeamColor.white:
                possible_moves.append((x - 1, y - 1))
        return possible_moves


class Bishop(ChessPiece):

    def __init__(self, team_color, position):
        self._pieceType = PieceType.bishop
        self._team = team_color
        self._position = position

    """Calculates moves that this piece can do based on current position and team"""
    def moves(self, board):
        possible_moves = [self.moves_helper1(1, board),
                          self.moves_helper2(1, board),
                          self.moves_helper3(1, board),
                          self.moves_helper4(1, board)]
        return possible_moves

    """Do I need to be 'None' checking in these functions?"""
    def moves_helper1(self, num, board):
        possible_moves = []
        x = self._position[0] + num
        y = self._position[1] + num
        if x > 7 | y > 7 | (board.get_piece_at_index(x, y) != None & board.get_piece_at_index(x, y).get_team() == self.get_team()):
            return possible_moves
        elif board.get_piece_at_index(x, y) != None & board.get_piece_at_index(x, y).get_team() != self.get_team():
            return possible_moves.append((x, y))
        possible_moves.append(self.moves_helper1(num + 1, board))
        possible_moves.append((x, y))
        return possible_moves

    def moves_helper2(self, num, board):
        possible_moves = []
        x = self._position[0] + num
        y = self._position[1] - num
        if x > 7 | y < 0 | (board.get_piece_at_index(x, y) != None & board.get_piece_at_index(x, y).get_team() == self.get_team()):
            return possible_moves
        elif board.get_piece_at_index(x, y) != None & board.piece_at_index(x, y).get_team() != self.get_team():
            possible_moves.append((x, y))
            return possible_moves
        possible_moves.append(self.moves_helper2(num + 1, board))
        possible_moves.append((x, y))
        return possible_moves

    def moves_helper3(self, num, board):
        possible_moves = []
        x = self._position[0] - num
        y = self._position[1] + num
        if x < 0 | y > 7 | (board.get_piece_at_index(x, y) != None & board.get_piece_at_index(x, y).get_team() == self.get_team()):
            return possible_moves
        elif board.get_piece_at_index(x, y) != None & board.get_piece_at_index(x, y).get_team() != self.get_team():
            return possible_moves.append((x, y))
        possible_moves.append(self.moves_helper3(num + 1, board))
        possible_moves.append((x, y))
        return possible_moves

    def moves_helper4(self, num, board):
        possible_moves = []
        x = self._position[0] - num
        y = self._position[1] - num
        if x < 0 | y < 0 | (board.get_piece_at_index(x, y) != None & board.get_piece_at_index(x, y).get_team() == self.get_team()):
            return possible_moves
        elif board.get_piece_at_index(x, y) != None & board.get_piece_at_index(x, y).get_team() != self.get_team():
            return possible_moves.append((x, y))
        possible_moves.append(self.moves_helper4(num + 1, board))
        possible_moves.append((x, y))
        return possible_moves
