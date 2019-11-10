from kivy.app               import App
from kivy.uix.boxlayout     import BoxLayout
from kivy.uix.image         import Image
from kivy.lang              import Builder
from kivy.graphics          import Rectangle
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget        import Widget
from kivy.uix.scrollview    import ScrollView
from kivy.uix.popup         import Popup
from kivy.factory           import Factory
from kivy.uix.floatlayout   import FloatLayout
from kivymd.theming         import ThemeManager
from kivy.properties        import ObjectProperty


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return ' {}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return'{} {}'.format(self.first, self.last)
    
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
class WindowManager(ScreenManager):
    pass

class LoginScreen(Screen):
    pass

class Nav(Screen):
    username = ObjectProperty(None)
    def createbtn(self):
        print(self.username.text)

class GoodTrainerApp(App):
    theme_cls = ThemeManager()
    theme_cls.accent_palette = 'Blue'
    theme_cls.primery_palette = 'Green'
    theme_cls.theme_style = 'Light'

    username = ObjectProperty(None)
    def createbtn(self):
        username = self.username.text
        print(username)
    def build(self):
        return WindowManager()
    
        



if __name__ == "__main__": 
    GoodTrainerApp().run()


        