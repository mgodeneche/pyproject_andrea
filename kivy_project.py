# coding: utf-8
import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import ObjectProperty
Builder.load_file('./kv/buttons.kv')

class pgcdButton(Button):
    pass

class pgcmButton(Button):
    pass

class premierButton(Button):
    pass

class facteurButton(Button):
    pass

class leaveButton(Button):
    pass

class menuScreen(GridLayout):
    display = ObjectProperty()

    def pgcd(self):
        #recuperer A et B
        self.display.text = MyApp.pgcd(a,b)
    
     


class MyApp(App):

    def build(self):
        self.title ="Application Python - Andrea Cicirello"
        return menuScreen()

    def afficherMenu():
        print ("MENU :")
        print (" 1 - Calculer le PGCD de deux nombres")
        print (" 2 - Calculer le PPCM de deux nombres")
        print (" 3 - Déterminer si un nombre est premier")
        print (" 4 - Donner la décomposition en facteur premier d'un nombre")
        print (" q - Quitter")
        return input("\nVotre choix :")

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
                    result = result + '.' + str(n)
                a = a / n
            else :
                n = n + 1
        if premier :
            return str(anciena)
        else :
            return result
    def traiterReponse(choix) :
        if (choix == 'q' or choix =='Q'):
            print("Exit")
            
	elif(choix==1):
            print("\nSaisissez 2 entiers ")
	    entier1 = input()
	    entier2 = input()
	    pgcdResult = pgcd(entier1, entier2)
	    print ("le pgcd de "+str(entier1)+" et "+str(entier2)+" est : "+str(pgcdResult))
	    # choix 2 : ppcm
        elif (choix == 2) :
            print ("\nSaisissez 2 entiers ")
            entier1 = input()
            entier2 = input()
            print ("le ppcm de "+str(entier1)+" et "+str(entier2)+" est "+str(ppcm(entier1, entier2)))
        elif (choix == 3) :
            entier = input("Saisissez un entier ")
            if premier(entier) :
                print (str(entier)+" est premier")
            else :
                print (str(entier)+" n'est pas premier")
        elif (choix == 4) :
             entier = input("Saisissez un entier ")
             print ("La décomposition de "+str(entier)+" en premiers est "+str(pdecomp(entier)))
    
if __name__ == '__main__':
    MyApp().run()
