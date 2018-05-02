from math import sqrt
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
def pgcd(a,b):
    print(a)
    print(b)
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
                return False
            else :
                n += 1
        return True

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

def openPopup():
    content = Button(text='Ok', size=(50,50))
    popup = Popup(title='Valeurs incorrectes !', content=content,
              auto_dismiss=False, size_hint=(None, None), size=(200, 100))
    content.bind(on_press=popup.dismiss)

    popup.open()


def closePopup():
    popup.dismiss()
