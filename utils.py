# -*- coding: utf8 -*-
from math import sqrt
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
def pgcd(a,b):
    while a%b!=0:
        a,b = b,a%b
    return b

def ppcm(a,b):
        return (a*b)/pgcd(a,b)

def premier(a):
        result = True
        n = 2
        top = sqrt(a)
        while (n <= top) :
            if a % n== 0 :
                return "Non"
            else :
                n += 1
        return "Oui"

def pdecomp(a):
        result = ''
        n = 2
        anciena = a
        premier = True
        while (n <= a) :
            if (a % n == 0) :
                premier = False
                if result == '' :
                    result = str(n)
                else :
                    result = result + ' x ' + str(n)
                a = a / n
            else :
                n = n + 1
        if premier :
            return str(anciena)
        else :
            return result

def openPopup(PopupText):
    if isinstance(App.get_running_app().root_window.children[0], Popup):
        pass
    else:
        content = Button(text='Ok', size=(50,50))
        popup = Popup(title=PopupText, content=content,
                  auto_dismiss=True, size_hint=(None, None), size=(200, 100))
        content.bind(on_press=popup.dismiss)
        popup.dismiss()
        popup.open()


def closePopup():
    popup.dismiss()

def inputValidator(x):
    return(nonEmptyValidation(x) and intValueValidation(x) and nonZeroValidation(x))

def nonEmptyValidation(x):
    try:
        x
    except NameError:
       openPopup('Valeurs non renseignées !')
    else:
       return True

def intValueValidation(x):
    try:
        x = int(x)
    except ValueError:
        openPopup('Renseignez un entier')
    else:
        return True
def nonZeroValidation(x):
    if(x==0):
        openPopup('Valeur incorrecte : 0')
    else:
        return True
