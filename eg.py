import kivy
from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='This is the first kivy app')

TestApp().run()