import pathlib
import os
import EFile
from enum import *


def initialize_files():
    for i, e in enumerate(EFile.value):
        os.makedirs(e, exist_ok=True)
    
    #os.makedirs(File., exist_ok=True)
    curses=FileHelper.pat
    current_directory = os.path.join(os.getcwd(),'src/files')
    os.makedirs('src/files/projects',exist_ok=True)
    src_ok = False
    print("dupa: ",current_directory)
    dirs = [d for d in pathlib.Path(current_directory).iterdir() if d.is_file()]
#    dirs.
   # os.
    for i in dirs:
        print(i.name)
            #current_directory = os.path.join(current_directory, 'src')

class FileHelper:
    name = ''
    pat = os.path.join(os.getcwd(), 'src/files')

    def __init__(self, name, pat):
        self.name = name
        self.pat = pat
