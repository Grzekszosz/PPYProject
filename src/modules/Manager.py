import datetime
import readchar
from modules.Ludzie import Ludzie

from PPYProject.utils.pullContent import *
from PPYProject.src.modules.Log import *
from PPYProject.src.modules.Pracownik import *
class Manager(Ludzie):
    projectList = []
    taskList = []
    def __init__(self,id,imie,nazwisko,stanowisko):
        super().__init__(id,imie,nazwisko,stanowisko)

    @staticmethod
    def addMenago():
        from utils.pullContent import lastPepoleId
        lastId=lastPepoleId()
        lastId=int(lastId)+1
        manager= Manager(lastId,input("Podaj imie: "),input("Podaj nazwisko: "),"Project manager")
        manager.setLogin()
        manager.setPassword()
        manager.writeMe()

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
                case '1':#Listuje przypisane zadania
                    cls()
                    for i in self.taskList:
                        i.toString()
                    pass
                case '2':#Listuje przypisane projekty
                    cls()
                    for i in self.projectList:
                        print(i.toString())
                    pass
                case '3':#Modyfikuje przypisanym zadaniem
                    cls()
                    print_manage_task()
                    choseTask=readchar.readchar()
                    match choseTask:
                        case '0':
                            pass
                        case '1': #Dodaje zadanie
                            cls()
                            self.taskList.append(Task.addTask(self))
                            self.suck_Mine()
                        case '2':#Na podstawie wybranego zadania..
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
                                            changeTask.manageTask() #.. Zarządza zadaniem
                                            changeTask.writeMe()
                                            self.suck_Mine()
                                    goodChar = False
                                if char=='0':
                                    break
                                else:
                                    cls()
                case '4':#Zarządzanie projektem
                    file=FileHelper(EFile.PROJECTS.name,EFile.PROJECTS.value)
                    ProjList=pull(file)
                    goodChar = True
                    cls()
                    printManagmentProjects()
                    switch = readchar.readchar()
                    match switch:
                        case '0':
                            pass
                        case '1':#Listuje przypisane projekty
                            for project in ProjList:
                                project.toString()
                        case '2':#Dodaje nowy projekt
                            project=Project.addProject()
                            project.writeMe()
                            self.suck_Mine()
                            goodChar = False
                        case '3':#Na podstawie wybranego projektu..
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
                                            project.manageProject()#..Zarządza projektem
                                            project.writeMe()
                                            self.suck_Mine()
                                        goodChar = False
                                if char=='0':
                                    break
                                else:
                                    cls()

                case '5':#Zarządznie pracownikami
                    cls()
                    while True:
                        print_manage_worker()
                        char =readchar.readchar()
                        match char:
                            case '0':
                                cls()
                                break
                            case '1':#Listuj pracownika
                                print("Dupa")
                                cls()
                                printUsers(getUsers())
                                continue
                            case '2':#Dodaje pracownika
                                while True:
                                    cls()
                                    worker_or_menago()
                                    chose = readchar.readchar()
                                    if chose == '1':
                                        Pracownik.addWorker()
                                    elif chose == '2':
                                        Manager.addMenago()
                                    elif chose == '0':
                                        cls()
                                        break
                            case '3':#Zarządza pracownikiem
                                while True:
                                    cls()
                                    print_modify_worker()
                                    chose=readchar.readchar()
                                    match chose:
                                        case '0':
                                            cls()
                                            break
                                        case '1':#Zmiana loginu
                                            user=getUser()
                                            user.setLogin()
                                            user.overWriteMe()
                                            break
                                        case '2':#Zmiana hasla
                                            user = getUser()
                                            user.setPassword()
                                            user.overWriteMe()
                                            break
                                        case '3':#Zmiana nazwiska
                                            user = getUser()
                                            user.setSurname()
                                            user.overWriteMe()
                                            break
                                pass
                            case _:
                                cls()
                case _:
                    cls()
        cls()
