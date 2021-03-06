# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty
from kivy.clock import Clock
from kivy.core.text import LabelBase, DEFAULT_FONT


class TextWidget(Widget):
    text = StringProperty()    # プロパティの追加
    time = NumericProperty()

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = ""
        self.time = 0
        self.event = Clock.schedule_interval(self.update_time, 1.0)
        pass

    def update_time(self, *args):
        self.time += 1

    def clicked(self):  # ボタンをクリック時
        if self.time == 10:
            self.event.cancel()
            self.text = "おめでとう!!"
        else:
            self.text = "ブブー(笑)"
            self.time = 0


class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = 'TESTING'  # ウィンドウの名前を変更

    def build(self):
        return TextWidget()


if __name__ == '__main__':
    LabelBase.register(DEFAULT_FONT, "ipaexg.ttf")
    TestApp().run()
