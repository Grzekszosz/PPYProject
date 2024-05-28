import readchar

from modules.Ludzie import Ludzie
from PPYProject.utils.printScripts import *

class Manager(Ludzie):
    projectList=[]

    def __init__(self):
        pass ###TODO suck mine powinien opdpalac sie w konstruktorze

    def suck_Mine(self):
        ###TODO
        ###TODO dostaje liste obiektow projetkow
        ### swoje, wkładam do projectList
        pass
    def get_in(self):

        while True:
            print(manager_menu)
            chose = readchar.readchar()
            print(f"{chose}")
            match chose:
                case '0':
                    break
                case '1':
                    #Wyświetl zadania(w Jag.statusu, priorytetu, terminów, ludzi)
             #       idLoged = auth.login()
             #       if idLoged != -1:
             #           loged = auth.make(idLoged)
             #           welcome(loged)
                    pass
                case '2':
                    #Wyświetl projekty()
                    break
                case '3':

                    break
                case '4':
                    break
                case '5':
                    break
                case _:
                    cls()
           # try:
            #    if loged is None:
            #        cls()
            #        print("Nie poprawne kredki")
            #        continue
            #except NameError:
            #    print(print("Nie poprawne kredki"))
    def manageWorkers(self):
        print("Manaze Workers")
## TODO- Zarządzanie pracownikiem(dodaj, usuń, modyfikuj, przypiszDoZadania)
## TODO- Zarządzanie projektem(dodaj, usuń, modyfikuj, przypisz / utworzZadania)
## TODO- Zarządzanie zadaniem(dodaj, usuń, modyfikuj, przypisz / utworzZadania)
## TODO- Wyświetl projekty(wg.statusu, priorytetu, terminów)
## TODO- Wyświetl zadania(wg.statusu, priorytetu, terminów, ludzi)