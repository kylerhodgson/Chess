import kivy
kivy.require('1.9.1')


from kivy.app import App
from kivy.uix.label import Label


class Chess(App):

    def build(self):
        return Label(text='We are going to be kings!')


if __name__ == '__main__':
    Chess().run()