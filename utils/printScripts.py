import os


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def menu_login():
    print("\t\t\t\t\t***Stipant***\n"
          "Wybierz opcje:\n"
          "\t[1] ~Zaloguj\n"
          "\t[0] ~Wyjdź\n")
