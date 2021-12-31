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

from databaseStuff          import addToDataBase
from databaseStuff          import lookForUser

class UserData:

    def __init__(self, first, last, email, password):
        self.first = first
        self.last = last
        self.email = email
        self.password = password

    # @property
    # def email(self):
    #     return ' {}.{}@email.com'.format(self.first, self.last)

    # @property
    # def fullname(self):
    #     return'{} {}'.format(self.first, self.last)
    
    # def __repr__(self):
    #     return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
class WindowManager(ScreenManager):
    pass

class LoginScreen(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    def checkCred(self):
        a = self.username.text
        b = self.password.text
        val = lookForUser(a,b)

class Admin(Screen):
    pass

class Nav(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    lastName = ObjectProperty(None)
    firstName = ObjectProperty(None)
    def createbtn(self): 
        a = self.firstName.text
        b = self.lastName.text
        c = self.username.text
        d = self.password.text
        newuse = UserData(a,b,c,d)
        addToDataBase(newuse)
        print("in nav")

class GoodTrainerApp(App):
    theme_cls = ThemeManager()
    theme_cls.accent_palette = 'Blue'
    theme_cls.primery_palette = 'Green'
    theme_cls.theme_style = 'Light'   
    def build(self):
        return WindowManager()

if __name__ == "__main__": 
    GoodTrainerApp().run()


        
