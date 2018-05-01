from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
import utils

from os import listdir
kv_path = './kv/'
for kv in listdir(kv_path):
    Builder.load_file(kv_path+kv)

class PgcdButton(Button):
    pass

class PgcmButton(Button):
    pass

class PremierButton(Button):
    pass

class FacteurButton(Button):
    pass
class LeaveButton(Button):
    pass


class Container(GridLayout):
    display = ObjectProperty()

    def pgcd(self):
        #recuperer A et B
        self.display.text = str(utils.pgcd(10,20))
    def pgcm(self):
        self.display.text = "pgcm"
    def premier(self):
        self.display.text = "premier"
    def facteurs(self):
        self.display.text = "facteurs"
    def leave(self):
        exit()

class MainApp(App):

    def build(self):
        self.title = 'Awesome app!!!'
        return Container()


if __name__ == "__main__":
    app = MainApp()
    app.run()

