### TODO wciagam wszystkie pliki z folderu
### TODO tworze na tej podstawie odpowienia liste obiektow
### TODO i ja zwracam
from PPYProject.src.modules.EFile import *
from PPYProject.src.modules.FileHelper import *

def pull(file):
    print(file.name,file.pat)
    lists=file.listFolder()
    if file.name==EFile.PROJECTS.name:
        print("dupa2")
        for list in lists:
            print("dupa3")
            proj=FileHelper(list,EFile.PROJECTS.value/list)
            projList=proj.read_lines()
            print(projList)