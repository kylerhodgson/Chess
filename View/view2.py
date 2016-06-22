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


class BoardBox(Rectangle):
    pass


class BoardWidget(GridLayout):
    def __init__(self, **kwargs):
        super(BoardWidget, self).__init__(**kwargs)
        self.cols = 8
        self.rows = 8
        self.build()
        with self.canvas.before:
            Color(1, 0, 1, 1)  # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=self.size, pos=self.pos)

    def build(self):
        for i in range(8):
            for j in range(8):
                s = Scatter(do_rotation=False, do_scale=False)
                s.auto_bring_to_front = True
                s.set_center_x(j * self.col_default_width)
                im = Image(source='Images/pawn.png')
                s.add_widget(im)
                self.add_widget(s)
                im.reload()


class Chess2(App):

    def build(self):
        b = BoardWidget()
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
        box = BoxLayout()
        box.add_widget(b)
        return box

if __name__ == '__main__':
    Chess2().run()