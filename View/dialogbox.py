from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class PopupWindow(Popup):
    _button1 = None
    _button2 = None
    _title = None
    _dialog = None
    _content = None

    def __init__(self):
        super(PopupWindow, self).__init__()
        self._title = Label()
        self.title = "Game Over"
        self._title.font_size = 40
        self._button1 = Button()
        self._button2 = Button()
        self._dialog = Label()
        self._dialog.font_size = 20
        self._content = BoxLayout()
        self._content.orientation = 'vertical'
        self._content.add_widget(self._title)
        self._content.add_widget(self._dialog)
        self._content.add_widget(self._button1)
        self._content.add_widget(self._button2)
        self.content = self._content

    def set_title(self, text):
        self._title.text = text

    def set_message(self, text):
        self._dialog.text = text

    def set_button1_text(self, text):
        self._button1.text = text

    def set_button1_callback(self, callback):
        self._button1.bind(on_press=callback)
        self._button1.bind(on_touch_up=self.dismiss)

    def set_button2_text(self, text):
        self._button2.text = text

    def set_button2_callback(self, callback):
        self._button2.bind(on_press=callback)
        self._button2.bind(on_touch_up=self.dismiss)

    def open(self, *largs):
        super(PopupWindow, self).open(*largs)
