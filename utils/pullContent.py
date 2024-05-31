### TODO wciagam wszystkie pliki z folderu
### TODO tworze na tej podstawie odpowienia liste obiektow
### TODO i ja zwracam
import os

from PPYProject.src.modules.Pracownik import *
from PPYProject.src.modules.EFile import *
from PPYProject.src.modules.FileHelper import *
from PPYProject.src.modules.Project import *
from modules.Manager import Manager
from utils import printScripts
#Paczka metod do wciągania danych z plików
#Zwraca liste instancji Projektow/Taskow
def pull(file):
    lists=file.listFolder()
    ret=[]
    if file.name==EFile.PROJECTS.name:
        for list in lists:
            file=FileHelper(list,EFile.PROJECTS.value/list)
            projList=file.read_lines()
            file.name=str(file.name).removesuffix('.txt')
            project=Project(file.name,projList[0],projList[1],projList[2],projList[3])
            project.initializeMaster(projList[6])
            project.initializeWorkers(projList[4])
            project.initializeTasks(projList[5])
            ret.append(project)
    if file.name==EFile.TASKS.name:
        for list in lists:
            taskFile=FileHelper(list,EFile.TASKS.value/list)
            taskLines=taskFile.read_lines()
            taskFile.name=str(taskFile.name).removesuffix('.txt')
            task=Task(taskFile.name,taskLines[0],taskLines[2],taskLines[7],taskLines[8],taskLines[3],taskLines[4])
            task.initializeLogs(taskLines[6])
            task.initializeOwner(taskLines[5])
            task.initalizeProj(taskLines[1])
            ret.append(task)
    return ret

#Zwraca projekt o podanym ID
def getProject(id):
    projList=os.listdir(EFile.PROJECTS.value)
    for proj in projList:
        file=FileHelper(proj.removesuffix('.txt'),EFile.PROJECTS.value/proj)
        listFile=file.read_lines()
        if listFile[0]==id:
            project = Project(file.name, listFile[0], listFile[1], listFile[2], listFile[3])
            project.initializeMaster(listFile[6])
            project.initializeWorkers(listFile[4])
            project.initializeTasks(listFile[5])
            return project
    return None
#Zwraca liste userow
def getUsers():
    ret=[]
    file=FileHelper(EFile.USERS.name,EFile.USERS.value)
    list = file.read_lines()
    for user in list:
        if user=='':
            continue
        content=user.split(';')
        if content[3] == 'Project Manager':
            ret.append(Manager(content[0],content[1],content[2],content[3]))
        else:
            ret.append(Pracownik(content[0],content[1],content[2],content[3]))
    return ret


#Drukuje na podstawie podanej listy userow informacje o userach
def printUsers(users):
    for user in users:
        print('[' + user.id + '] ' + user.imie + ' ' + user.nazwisko+' '+user.stanowisko)

#Zwraca wybraną osobę
def getUser():
    users=getUsers()
    goodChar = True
    while goodChar:
        printUsers(users)
        choseUser=input("Wybierz osobę: ")
        for user in users:
            if user.id == choseUser:
                return user
        printScripts.cls()


#Drukuje przekazaną liste projektów
def printProjects(projects):
    for project in projects:
        print("[" + project.id + "] " + project.name + " " + project.description)


#Zwraca stringa zawierajacego ID logow w podanym tasku
def logsIds(task):
    logId=''
    file=FileHelper(EFile.LOGS.name,EFile.LOGS.value)
    logsList=file.listFolder()
    for log in logsList:
        logFile=FileHelper(log,EFile.LOGS.value/log)
        contentLog=logFile.read_lines()
        if contentLog[0]==str(task.id):
            logId=logId+log.removesuffix('.txt')+','
        logId.rstrip(',')
    return logId


#Pozwala wybrac ktory projekt chcemyu przypisac do podanego taska
def getProjectS(task):
    goodChar=True
    projects = pull(FileHelper(EFile.PROJECTS.name, EFile.PROJECTS.value))
    Rproject=None
    while goodChar:
        print("\nWybierz projekt który chcesz przypisać: \n")
        printProjects(projects)
        choseProject = input()
        for project in projects:
            if project.id == choseProject:
                Rproject = project
                goodChar = False
        printScripts.cls()

    Rproject.tasks.append(task)
    Rproject.writeMe()
    return Rproject

#Zwraca najwyzsze obecnie ID projektu w systemie
def lastProjectId():
    file=FileHelper(EFile.PROJECTS.name,EFile.PROJECTS.value)
    listProject=file.listFolder()
    max=0
    for project in listProject:
        projectFile=FileHelper(project,EFile.PROJECTS.value/project)
        content=projectFile.read_lines()
        if int(max)<int(content[0]):
            max=content[0]
    return max
#Zwraca najwyższe obecnie ID usera w systemie
def lastPepoleId():
    max=0
    users=getUsers()
    for user in users:
        if int(max)<int(user.id):
            max=user.id
    return max
