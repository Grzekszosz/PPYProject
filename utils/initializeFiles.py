from src.modules.EFile import *
from utils.printScripts import *
from src.modules.FileHelper import FileHelper

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
