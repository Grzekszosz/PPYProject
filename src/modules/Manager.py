import readchar

from modules.Ludzie import Ludzie
from PPYProject.utils.printScripts import *
from PPYProject.utils.pullContent import *
from PPYProject.src.modules.FileHelper import *
from PPYProject.src.modules.EFile import *
class Manager(Ludzie):
    projectList=[]
    taskList=[]
    def __init__(self,id,imie,nazwisko,stanowisko):
        super().__init__(id,imie,nazwisko,stanowisko)

    def suck_Mine(self):
        file=FileHelper(EFile.PROJECTS.name,EFile.PROJECTS.value)
        projList=pull(file)
        for proj in projList:
            if proj.master.id==self.id:
                self.projectList.append(proj)
        file=FileHelper(EFile.TASKS.name,EFile.TASKS.value)
        tasksList=pull(file)
        for tasks in tasksList:
            if tasks.owner.id==self.id:
                self.taskList.append(tasks)


    def get_in(self):
        self.suck_Mine()
        while True:
            manager_menu()
            chose = readchar.readchar()
            match chose:
                case '0':
                    break
                case '1':
#TODO "[1] ~Wyświetl zadania(w Jag.statusu, priorytetu, terminów, ludzi)\n",
                    cls()
                    for i in self.taskList:
                        i.toString()
                    pass
                case '2':
                    cls()
                    for i in self.projectList:
                        print(i.toString())
                    pass
                case '3':
                    cls()
                    manage_task()
                    choseTask=readchar.readchar()
                    match choseTask:
                        case '0':
                            break
                        case '1':
                            lastTaskId=0
                            print(FileHelper.lastId(EFile.TASKS.name,EFile.TASKS.value))

                           # task = Task(lastTaskId,input("Podaj nazwe zadania: "),input("Podaj opis zadania: "),input("Podaj date rozpoczęcia: "),input("Podaj date zakończenia: "),'','')

                           # self.taskList.append(task)
                            break
                        case '2':
                            #Modyfikacja zadania
                            break
#TODO [3] ~Zarządzanie zadaniem(dodaj, usuń, modyfikuj, przypisz / utworzZadania)
                    break
                case '4':
#TODO [4] ~Zarządzanie projektem(dodaj, usuń, modyfikuj, przypisz / utworzZadania)\n",
                    break
                case '5':
#TODO [5] ~Zarządzanie pracownikiem(dodaj, usuń, modyfikuj, przypiszDoZadania)\n",
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