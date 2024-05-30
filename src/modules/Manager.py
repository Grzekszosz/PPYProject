import datetime
import readchar
from PPYProject.utils.printScripts import *
from PPYProject.utils.pullContent import *
from PPYProject.src.modules.FileHelper import *
from PPYProject.src.modules.EFile import *
from PPYProject.src.modules.Status import *
from PPYProject.src.modules.Priority import *
from PPYProject.src.modules.Log import *
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
                            goodChar = True
                            fileId=FileHelper(EFile.TASKS.name,EFile.TASKS.value)
                            task = Task(int(fileId.lastId())+1,
                                        input("Podaj nazwe zadania: "),input("Podaj opis zadania: "),
                                        input("Podaj date rozpoczęcia: "),input("Podaj date zakończenia: "),
                                        '','')
                            Status.print_all_values()
                            choseStatus = readchar.readchar()
                            #TODO naprawić wciąganie danych by wybrana wartość była wszędzie
                            match choseStatus:
                                case '0':
                                    pass
                                case '1':
                                    task.status=Status.OPEN.value
                                case '2':
                                    task.status=Status.INPROGRES.value
                                case '3':
                                    task.status=Status.CLOSED.value
                                case '4':
                                    task.status=Status.BLOCKED.value
                                case _:
                                    pass
                            Priority.print_all_values()
                            chosePriority=readchar.readchar()
                            match chosePriority:
                                case '0':
                                    pass
                                case '1':
                                    task.pirority=Priority.VERYLOW.value
                                case '2':
                                    task.pirority=Priority.LOW.value
                                case '3':
                                    task.pirority=Priority.NORMAL.value
                                case '4':
                                    task.pirority=Priority.HIGH.value
                                case '5':
                                    task.pirority=Priority.VERYHIGH.value
                                case _:
                                    pass
                            users = getUsers()
                            while goodChar:
                                print("Wybierz osobę którą chcesz przypisać: ")
                                for user in users:
                                    print('[' + user.id + '] ' + user.imie + ' ' + user.nazwisko)
                                choseUser = input()
                                for user in users:
                                    if user.id==choseUser:
                                        task.owner=user
                                        goodChar=False
                                    else:
                                        cls()

                            goodChar=True
                            projects = pull(FileHelper(EFile.PROJECTS.name, EFile.PROJECTS.value))
                            while goodChar:
                                print("\nWybierz projekt który chcesz przypisać: \n")
                                for project in projects:
                                    print("[" + project.id + "] " + project.name + " " + project.description)
                                choseProject=input()
                                for project in projects:
                                    if project.id == choseProject:
                                        task.project=project
                                        goodChar=False
                                    else:
                                        cls()
                            goodChar=True
                            print("\n Dodano zadanie [{}] {} dla {} {} w projekcie {} {}:"
                                  .format(task.id,task.name,task.owner.imie, task.owner.nazwisko, task.project.name, task.project.description))
                            fileName=str(task.id)+".txt"
                            open(EFile.TASKS.value/fileName,'x')
                            file=FileHelper(fileName,EFile.TASKS.value/fileName)
                            file.write_to_file(task.getTask(),'a')
                            self.suck_Mine()
                        case '2':
                            cls()
                            char=''
                            goodChar = True
                            listId = []
                            changeTask=None
                            while goodChar:
                                for i in self.taskList:
                                    print("Wybierz zadanie:\n"
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
                                    goodChar = False

                                if char=='0':
                                    break
                                else:
                                    cls()










#TODO [3] ~Zarządzanie zadaniem(dodaj, usuń, modyfikuj, przypisz / utworzZadania)

                case '4':
#TODO [4] ~Zarządzanie projektem(dodaj, usuń, modyfikuj, przypisz / utworzZadania)\n",
                    break
                case '5':
#TODO [5] ~Zarządzanie pracownikiem(dodaj, usuń)\n",
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