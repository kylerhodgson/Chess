from kivy.app import App
from View.gameboard import BoardWidget
from View.dialogbox import PopupWindow
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from Models.GameModel.Pieces.teamcolor import TeamColor


class Chess(App):
    _board = None
    _view = None
    _container = None
    _resources = None
    _my_bool = False
    _turn_display = None

    def set_container(self, container):
        self._container = container

    def build(self):
        self._view = BoxLayout()
        self._board = BoardWidget(self._container)
        self._view.add_widget(self._board)
        self._resources = BoxLayout(orientation='vertical')
        self._resources.size_hint_x = .3
        if self._my_bool is True:
            self._turn_display = Label()
            self._turn_display.text = "White's turn"
            self._turn_display.size_hint_y = .1
            self._resources.add_widget(self._turn_display)
            restart = Button()
            restart.text = "Restart"
            restart.bind(on_press=self.restart)
            restart.size_hint_y = .25
            self._resources.add_widget(restart)
            self._view.add_widget(self._resources, 0)
            label = Label()
            label.text = "Move history here"
            self._resources.add_widget(label)
            undo = Button()
            undo.text = "Undo"
            undo.bind(on_press=self.undo)
            undo.size_hint_y = .25
            self._resources.add_widget(undo)
            redo = Button()
            redo.text = "Redo"
            redo.bind(on_press=self.redo)
            redo.size_hint_y = .25
            self._resources.add_widget(redo)
        self._my_bool = True
        return self._view

    def get_board(self):
        return self._board

    def remove_piece(self, piece):
        self._board.delete_piece(piece)

    def display_stalemate(self):
        popup = PopupWindow()
        popup.set_button1_text("Yes")
        popup.set_button1_callback(self.restart)
        popup.set_button2_text("No")
        popup.set_button2_callback(popup.dismiss)
        popup.set_title("Stalemate!")
        popup.set_message("Would you like to play again?")
        popup.open()

    def display_checkmate(self, winning_team):
        popup = PopupWindow()
        popup.set_button1_text("Yes")
        popup.set_button1_callback(self.restart)
        popup.set_button2_text("No")
        popup.set_button2_callback(popup.dismiss)
        popup.set_title("Checkmate!")
        team = "White" if winning_team == TeamColor.White else "Black"
        popup.set_message(team + " wins! Would you like to play again?")
        popup.open()
        return True

    def restart(self, args):
        self._container.restart()

    def undo(self, args):
        a = self._container.undo()
        # do something with a

    def redo(self, args):
        a = self._container.redo()
        # do something with a

    def set_turn(self, turn):
        self._turn_display.text = "White's turn" if turn == TeamColor.white else "Black's turn"
