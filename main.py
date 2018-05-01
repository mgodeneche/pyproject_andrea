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

class AnswerWidget(BoxLayout):
    def __init__(self,**kwargs):
        super(AnswerWidget,self).__init__(**kwargs)

        self.orientation = "vertical"

        self.name_input = TextInput(text='AAAAA')

        self.add_widget(self.name_input)

        self.save_button = Button(text="Valider")
        self.save_button.bind(on_press=self.save)

        self.save_popup = SaveDialog(self) # initiation of the popup, and self gets passed

        self.add_widget(self.save_button)


    def save(self,*args):
        self.save_popup.open()
        
class SaveDialog(Popup):

    def __init__(self,my_widget,**kwargs):  # my_widget is now the object where popup was called from.
        super(SaveDialog,self).__init__(**kwargs)

        self.my_widget = my_widget

        self.content = BoxLayout(orientation="horizontal")

        self.save_button = Button(text='Save')
        self.save_button.bind(on_press=self.save)

        self.cancel_button = Button(text='Cancel')
        self.cancel_button.bind(on_press=self.cancel)

        self.content.add_widget(self.save_button)
        self.content.add_widget(self.cancel_button)

    def save(self,*args):
        print "save %s" % self.AnswerWidget.name_input.text # and you can access all of its attributes
        #do some save stuff
        self.dismiss()

    def cancel(self,*args):
        print "cancel"
        self.dismiss()


class Container(GridLayout):
    display = ObjectProperty()
    global a
    a = 20
    global b
    b = 20
    def pgcd(self):
        return AnswerWidget()
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

