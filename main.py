# -*- coding: utf8 -*-
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
class Popup(Popup):
   
    def dismiss():
        popup.dismiss()
class Container(GridLayout):
    display = ObjectProperty()
    aValue = ObjectProperty()
    global a 
    global b
    a = 0
    b = 0
    def pgcd(self):
        if(utils.inputValidator(a) and  utils.inputValidator(b)):
            self.display.text = str(utils.pgcd(a,b))
    def ppcm(self):
        if(utils.inputValidator(a) and  utils.inputValidator(b)):
           self.display.text = str(utils.ppcm(a,b))
    def premier(self):
        if(utils.inputValidator(a)):
           self.display.text = str(utils.premier(a))
    def facteurs(self):
        if(utils.inputValidator(a)):
            self.display.text = str(utils.pdecomp(a))
    def leave(self):
        exit()
    def updateA(container,textValue):
        global a
        if(utils.inputValidator(textValue.text)):
            a = int(textValue.text)
    def updateB(container,textValue):
        global b
        if(utils.inputValidator(textValue.text)):
            b = int(textValue.text)
     
        
        
class MainApp(App):

    def build(self):
        self.title = 'Application Python - Maxence Godeneche & Andrea Cicirello'
        return Container()


if __name__ == "__main__":
    app = MainApp()
    app.run()

