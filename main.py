from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import utils

from os import listdir
kv_path = './kv/'
for kv in listdir(kv_path):
    Builder.load_file(kv_path+kv)

class PgcdButton(Button):
    pass

class PpcmButton(Button):
    pass

class PremierButton(Button):
    pass

class FacteurButton(Button):
    pass
class LeaveButton(Button):
    pass
class SaveButton(Button):
    pass
class TextInputA(TextInput):
    pass
class TextInputB(TextInput):
    pass
class AnswerWidget(BoxLayout):  
    def on_enter(instance, value):
        print('User pressed enter in', instance)
class Header(GridLayout):
   def validate(self):
       self.a.text = "A"

class Container(GridLayout):
    display = ObjectProperty()
    global a
    a = 20
    global b
    b = 20
    def pgcd(self):
        self.display.text = str(utils.pgcd(a,b))
    def ppcm(self):
        self.display.text = str(utils.ppcm(a,b))
    def premier(self):
        self.display.text = str(utils.premier(a))
    def facteurs(self):
        self.display.text = str(utils.pdecomp(a))
    def leave(self):
        exit()

class MainApp(App):

    def build(self):
        self.title = 'Application Python - Maxence Godeneche & Andrea Cicirello'
        return Container()


if __name__ == "__main__":
    app = MainApp()
    app.run()

