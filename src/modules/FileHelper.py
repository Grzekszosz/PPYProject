import os
from PPYProject.src.modules.EFile import *

class FileHelper:
    name = ''
    pat = ''

    def __init__(self, name, pat):
        self.name = name
        self.pat = pat

    def __del__(self):
        pass

    def write_to_file(self, content):
        with open(self.pat, 'a') as file:
            file.writelines(content)

    def read_file_all(self):
        with open(self.pat, 'r') as file:
            return file.read()

    def read_lines(self):
        ret = []
        with open(self.pat, 'r') as file:
            lines = file.readlines()
            for line in lines:
                ret.append(line.strip())
        return ret

    def listFolder(self):
        ret = os.listdir(self.pat)
        return ret

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
        if self.name==EFile.TASKS.name:
            pass
        return False

