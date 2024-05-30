import datetime
import readchar

from PPYProject.utils.pullContent import *

from PPYProject.src.modules.Priority import *
from PPYProject.src.modules.Log import *
from PPYProject.src.modules.Pracownik import *
class Manager(Ludzie):
    projectList = []
    taskList = []
    def __init__(self,id,imie,nazwisko,stanowisko):
        super().__init__(id,imie,nazwisko,stanowisko)

    def suck_Mine(self):
        self.projectList.clear()
        self.taskList.clear()
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
                    print_manage_task()
                    choseTask=readchar.readchar()
                    match choseTask:
                        case '0':
                            pass
                        case '1':
                            cls()
                            self.taskList.append(Task.addTask(self))
                            self.suck_Mine()
                        case '2':
                            cls()
                            char=''
                            goodChar = True
                            listId = []
                            changeTask=None
                            while goodChar:
                                for i in self.taskList:
                                    print("Wybierz zadanie ~id: \n"
                                       '[',i.id,'] | ',i.name,' | ',i.description,' | ',i.pirority,' | '
                                      ,i.status,' | ',i.owner.imie,' ',i.owner.nazwisko,' | ',i.project.name,'\n')
                                    listId.append(i.id)
                                print("[0] Anluj")
                                char=input()
                                if listId.__contains__(char):
                                    for taskE in self.taskList:
                                        if taskE.id == char:
                                            changeTask = taskE
                                            changeTask.manageTask()
                                            changeTask.writeMe()
                                            self.suck_Mine()
                                    goodChar = False
                                if char=='0':
                                    break
                                else:
                                    cls()

# [3] ~Zarządzanie zadaniem(dodaj, usuń, modyfikuj, przypisz / utworzZadania)

                case '4':
# [4] ~Zarządzanie projektem(dodaj,  modyfikuj, przypisz )\n",
                    file=FileHelper(EFile.PROJECTS.name,EFile.PROJECTS.value)
                    ProjList=pull(file)
                    goodChar = True
                    cls()
                    printManagmentProjects()
                    switch = readchar.readchar()
                    match switch:
                        case '0':
                            pass
                        case '1':
                            for project in ProjList:
                                project.toString()
                        case '2':
                            project=Project.addProject()
                            project.writeMe()
                            self.suck_Mine()
                            goodChar = False
                        case '3':
                            listId=[]
                            listId.clear()
                            goodChar = True
                            while goodChar:
                                for project in ProjList:
                                    project.toString()
                                    listId.append(str(project.id))
                                char=input("[0] ⚡~Anuluj\nWybierz projekt ~id: \n")
                                if listId.__contains__(char):
                                    for project in ProjList:
                                        if str(project.id)==char:
                                            project.manageProject()
                                            project.writeMe()
                                            self.suck_Mine()
                                        goodChar = False
                                if char=='0':
                                    break
                                else:
                                    cls()

                case '5':
                    while True:
                        char =readchar.readchar()
                        match char:
                            case '0':
                                break
                            case '1':#dodaj pracownika
                                while True:
                                    worker_or_menago()
                                    chose=readchar.readchar()
                                    if chose=='1':
                                        Pracownik.addWorker()
                                    elif chose=='2':
                                        pass
                                    elif chose=='0':
                                        break
                            case '2':
                                pass
                                #Usun pracownika
                            case '3':
                                pass
                                #zarzadzaj pracownikiem
                            case _:
                                cls()


#TODO [5] ~Zarządzanie pracownikiem(dodaj, usuń)\n",
                    break
                case _:
                    cls()
