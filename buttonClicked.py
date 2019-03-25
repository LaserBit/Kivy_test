# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty


class TextWidget(Widget):
    text = StringProperty()    # プロパティの追加

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = ''

    def clicked(self):  # ボタンをクリック時
        if self.text == '':
            self.text = 'Hello World'
        else:
            self.text = ''


class buttonClickedAPP(App):
    def __init__(self, **kwargs):
        super(buttonClickedAPP, self).__init__(**kwargs)
        self.title = 'TESTING'  # ウィンドウの名前を変更

    def build(self):
        return TextWidget()


if __name__ == '__main__':
    buttonClickedAPP().run()
