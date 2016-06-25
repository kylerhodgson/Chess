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


class BoardBox(Rectangle):
    pass


class BoardWidget(GridLayout):
    def build(self):
        self.cols = 8
        self.rows = 8
        self.padding = 15
        for i in range(8):
            for j in range(8):
                button = Button(text="("+str(j)+","+str(abs(i-7))+")")
                self.add_widget(button)


class ChessBoard(App):

    def build(self):
        b = BoardWidget()
        b.build()
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
        return b

