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


class BoardBox(Rectangle):
    pass


class BoardWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(BoardWidget, self).__init__(**kwargs)
        pieces = []
        with self.canvas:
            size = 70
            for i in range(8):
                for j in range(8):
                    Color(1, 0, 0, 1) if (i+j)%2 == 0 else Color(0,0,1,1)  #  colors range from 0-1 instead of 0-255
                    Rectangle(pos=(j * size, abs(i-7) * size), size=(size,size))
                    s = Scatter(do_rotation=False, do_scale=False)
                    s.set_center_x(j * size + size/2)
                    s.set_center_y((abs(i-7))*size + size/2)
                    s.auto_bring_to_front = True
                    im = Image(source='Images/pawn.png')
                    s.add_widget(im)
                    s.id = "Pawn" + str(j) + str(abs(i-7))
                    s.size = (size/2, size/2)
                    self.add_widget(s)
                    pieces += [s]


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
