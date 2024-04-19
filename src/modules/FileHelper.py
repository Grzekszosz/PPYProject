from .EFile import *
from utils.printScripts import *


# wynieść do innego pliku do utils

map_content = {
    EFile.USERS.name: login_content()
}


def initialize_files():
    for i in EFile:
        if i.value.name.rfind('.txt').__eq__(-1):
            os.makedirs(i.value, exist_ok=True)
        else:
            try:
                open(i.value, 'x')
                complete = FileHelper(i.name, i.value)
                complete.write_to_file(map_content.get(i.name))
                del complete
            except FileExistsError:
                pass


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
