import os
from PPYProject.src.modules.EFile import *

#KLasa pomocnicza do obsługi plików
class FileHelper:
    name = ''
    pat = ''

    def __init__(self, name, pat):
        self.name = name
        self.pat = pat

    def __del__(self):
        pass
    #Zapisuje do pliku, można wskazać z jakim parametrem
    def write_to_file(self, content, parameter='a'):
        with open(self.pat, parameter) as file:
            file.writelines(content)

    #Zwraca zawartość całego pliku w strinu
    def read_file_all(self):
        with open(self.pat, 'r') as file:
            return file.read()

    #Zwraca zawartość pliku w liniach
    def read_lines(self):
        ret = []
        with open(self.pat, 'r') as file:
            lines = file.readlines()
            for line in lines:
                ret.append(line.strip())
        return ret

    #Zwraca zawartosć folderu w liniach
    def listFolder(self):
        ret = os.listdir(self.pat)
        return ret

    #W zależności od podanego sufixa sprawdza czy user o danym ID istnieje w pliku
    def find(self,Id,sufix=None):
        lines=self.read_lines()
        if self.name==EFile.USERS.name:
            for line in lines:
                content=line.split(';')
                if sufix =='Project Manager':
                    if content[0].__contains__(Id) and content[3]==sufix :
                        return True
                else:
                    if content[0].__contains__(Id):
                        return True
        if str(self.pat).startswith(str(EFile.PROJECTS.value)):
            tasks=lines[5].split(',')
            if tasks.__contains__(Id):
                return True
        return False
    #Zwraca ostatnie ID Taska lub Logu
    def lastId(self):
        max = 0
        if self.name==EFile.TASKS.name or self.name == EFile.LOGS.name:
            listTasks=self.listFolder()
            for i in listTasks:
                id=i.removesuffix('.txt')
                if int(max)<int(id):
                    max=id
        return max
