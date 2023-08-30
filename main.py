

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image


class LoginPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background = Image(source='login.jpeg', allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        self.register_input = TextInput(hint_text='Register Number')
        self.roll_input = TextInput(hint_text='Roll Number')
        self.signin_button = Button(text='Sign In', background_color='blue', bold=True)
        self.signin_button.bind(on_press=self.sign_in)
        self.roll_input.pos_hint = {"center_x": .5, "center_y": .5}
        self.register_input.size_hint = (0.6, 0.15)
        self.roll_input.size_hint = (0.6, 0.15)
        self.register_input.pos_hint = {"center_x": .5, "center_y": .5}
        self.signin_button.size_hint = (0.6, 0.15)
        self.signin_button.pos_hint = {"center_x": .5, "center_y": .5}
        self.empty_space = Label(size_hint_y=None, height=10)
        layout = BoxLayout(orientation='vertical', spacing=10)
        layout.add_widget(self.background)
        layout.add_widget(self.register_input)
        layout.add_widget(self.roll_input)
        layout.add_widget(self.signin_button)
        layout.add_widget(self.empty_space)
        self.add_widget(layout)

    def sign_in(self, instance):
        register_number = self.register_input.text
        roll_number = self.roll_input.text
        if register_number and roll_number:
            sm.current = 'main'


class MainPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = GridLayout(cols=2)
        self.categories = Button(text='Categories', bold=True)
        self.profile = Button(text='Profile', bold=True)
        self.notes = Button(text='Notes', bold=True)
        self.exit = Button(text='Exit', bold=True)
        self.exit.bind(on_release=self.quit)
        self.categories.bind(on_press=self.show_question)
        layout.add_widget(self.categories)
        layout.add_widget(self.profile)
        layout.add_widget(self.notes)
        layout.add_widget(self.exit)
        self.add_widget(layout)

    def quit(self, instance):
        # Go back to the login page
        sm.current = 'login'

    def show_question(self,insatnce):
        sm.current ='questions'


class QuestionsPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        for i in range(1, 11):
            button = Button(text=f'Test {i}')
            layout.add_widget(button)

        self.exit = Button(text='Exit', bold=True)
        self.exit.bind(on_release=self.quit)

        layout.add_widget(self.exit)
        self.add_widget(layout)




    def quit(self, instance):
        # Go back to the login page
        sm.current = 'main'


sm = ScreenManager()
sm.add_widget(LoginPage(name='login'))
sm.add_widget(MainPage(name='main'))
sm.add_widget(QuestionsPage(name='questions'))


class PECApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    PECApp().run()