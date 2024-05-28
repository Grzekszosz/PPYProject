### TODO wciagam wszystkie pliki z folderu
### TODO tworze na tej podstawie odpowienia liste obiektow
### TODO i ja zwracam
from PPYProject.src.modules.EFile import *
from PPYProject.src.modules.FileHelper import *
from PPYProject.src.modules.Project import *
#TODO to można by było zrobić bardziej dynamic
def pull(file):
    print(file.name,file.pat)
    lists=file.listFolder()
    ret=[]
    print(lists)
    if file.name==EFile.PROJECTS.name:
        for list in lists:
            file=FileHelper(list,EFile.PROJECTS.value/list)
            projList=file.read_lines()
            file.name=str(file.name).removesuffix('.txt')
            project=Project(file.name,projList[0],projList[1],projList[2],projList[3])
            project.initializeMaster(projList[6])
            project.initializeWorkers(projList[4])
            project.initializeTasks(projList[5])

            #print("PULL",project.description)
            ret.append(project)
    return ret
