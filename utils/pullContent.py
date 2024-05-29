### TODO wciagam wszystkie pliki z folderu
### TODO tworze na tej podstawie odpowienia liste obiektow
### TODO i ja zwracam
import os

from PPYProject.src.modules.EFile import *
from PPYProject.src.modules.FileHelper import *
from PPYProject.src.modules.Project import *
#TODO to można by było zrobić bardziej dynamic
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