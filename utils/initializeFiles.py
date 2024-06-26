import os

from PPYProject.src.modules.EFile import *
from PPYProject.src.modules.FileHelper import FileHelper
from PPYProject.utils.printScripts import *
#Paczka inicjalizująca podstawowe pliki do pracy systemu
#Mapuje funkcje
map_content = {
    EFile.LOGIN.name: login_content(),
    EFile.USERS.name: users_content()
}

#Inicjalizuje pliki
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
