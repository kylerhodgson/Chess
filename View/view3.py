import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle
from kivy.uix.button import Button
from math import *
from kivy.graphics import *
from kivy.graphics import Color
from kivy.graphics.vertex_instructions import Rectangle


class BoardBox(Rectangle):
    pass


class BoardWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(BoardWidget, self).__init__(**kwargs)
        with self.canvas.before:
            Color(0, 0, 0, 1)
            self.rectangle = Rectangle(pos=(0, 0), size=self.size)
            length = self.get_length()
            self.draw_board(length)
        self.place_pieces(length)

    def on_size(self, *args):
        self.rectangle.size = self.size
        self.clear_widgets()
        self.canvas.clear()
        length = self.get_length()
        with self.canvas.before:
            self.draw_board(length)
        self.place_pieces(length)

    def draw_board(self, length):
        Color(0, 0, 0, 1)
        Rectangle(pos=(0, 0), size=self.size)
        for i in range(8):
            for j in range(8):
                Color(1, 0, 0, 1) if (i + j) % 2 == 0 else Color(0, 0, 1, 1) # colors range from 0-1 instead of 0-255
                Rectangle(pos=(j * length / 8, abs(i - 7) * length / 8),
                          size=(length / 8, length / 8))

    def place_pieces(self, length):
        for i in range(8):
            for j in range(8):
                s = Scatter(do_rotation=False, do_scale=False)
                s.size_hint = None, None
                s.size = length/8, length/8
                s.center = (j * length/8 + length / 16, (abs(i - 7)) * length/8 + length / 16)
                s.auto_bring_to_front = True
                im = Image(source='Images/pawn.png')
                im.size_hint = None, None
                im.size = length / 8, length / 8
                im.center = im.size[0]/2, im.size[1]/2
                s.add_widget(im)
                s.id = "Pawn" + str(j) + str(abs(i - 7))
                self.add_widget(s)

    def get_length(self):
        return self.rectangle.size[0] if self.rectangle.size[0] < self.rectangle.size[1] else self.rectangle.size[1]


class Chess3(App):

    def build(self):
        box = BoardWidget()
        """t = TextInput(font_size=150,
                      size_hint_y=None,
                      height=200,
                      text='default')

        f = FloatLayout()
        s = Scatter()
        l = Label(text='default',
                  font_size=150)

        t.bind(text=l.setter('text'))

        f.add_widget(s)
        s.add_widget(l)

        b.add_widget(t)
        b.add_widget(f)"""
        return box

if __name__ == '__main__':
    Chess3().run()
