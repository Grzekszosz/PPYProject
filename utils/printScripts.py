import os
#Paczka metod, drukujących, zwracających zawartości na wydruki do konsoli lub do pliku
#Zrobione z myślą, by nie zaśmiecać kodu długimi printami/returnami

def cls():
    os.system("cls")


def menu_login():
    print("\t\t\t\t\t***Stipant***\n"
          "Wybierz opcje:\n"
          "\t[1] ⚡~Zaloguj\n"
          "\t[0] ⚡~Wyjdź\n")


def login_content():
    return (
        "1;Gorlowski;1234\n",
        "2;Dudus;1243\n",
        "3;Nowakowski;SilneHaslo\n"
    )


def users_content():
    return (
        "1;Grzegorz;Orlowski;Project Manager\n",
        "2;Daniel;Dudkowski;Dev\n",
        "3;Jan;Nowak;Analityk\n"
    )


def welcome(lud):
    cls()
    if lud.stanowisko == 'Project Manager':
        print("\t\t\tWitamy Pana {} {} MENADŻERA\n".format(lud.imie, lud.nazwisko))
    else:
        print("\t\t\tDzień dobry {} {} {}  \n".format(lud.imie, lud.nazwisko, lud.stanowisko))


def manager_menu():
    print(
        "[1] ⚡~Wyświetl swoje zadania\n",
        "[2] ⚡~Wyświetl swoje projekty\n",
        "[3] ⚡~Zarządzanie zadaniem(dodaj, modyfikuj, utworzZadania)\n",
        "[4] ⚡~Zarządzanie projektem(dodaj, modyfikuj, przypisz)\n",
        "[5] ⚡~Zarządzanie pracownikiem(dodaj, modyfikuj)\n",
        "[0] ⚡~Wyloguj"
    )
def printManagmentProjects():
    print(
        "\n[1] ⚡~Listuj wszystkie projekty\n"
        "[2] ⚡~Dodaj projekt\n"
        "[3] ⚡~Zarządzaj projektem\n"
        "[0] ⚡~Anuluj\n"
    )
def printManagmentProject():
    print(
        "\n[1] ⚡~Zmien odpowiedzialnego\n"
        "[2] ⚡~Zmien daty\n"
        "[3] ⚡~Dopisz pracownika\n"
        "[4] ⚡~Usun pracownika\n"
        "[5] ⚡~Pokaz zadania\n"
        "[6] ⚡~Pokaz pracownikow projektu\n"
    )

def worker_menu():
    print(
        "\n[1] ⚡~Wyświetl zadania(Przypisane do mnie)\n",
        "[2] ⚡~Zarządzanie zadaniem(modyfikuj *(status, logi_pracy)* )\n",
        "[3] ⚡~Wyświetl projekty(przypisane do mnie)\n",
        "[0] ⚡~Wyloguj\n"
    )
def print_manage_task():
    print(
        "\n[1] ⚡~Dodaj zadanie\n"+
        "[2] ⚡~Modyfikuj swoje zadanie \n"+
        "[0] ⚡~Wyjdz\n"
    )
def print_modify_task():
    print("\n[1] ⚡~Dodaj log\n"
          "[2] ⚡~Wylistuj logi\n"
          "[3] ⚡~Zmien status / priorytet\n"
          "[4] ⚡~Zmien wlasciciela\n"
          "[0] ⚡~Anuluj")
def print_manage_worker():
    print("\n[1] ⚡~Listuj pracownikow\n"
          "[2] ⚡~Dodaj pracownika\n"
          "[3] ⚡~Zarzadzaj pracownikiem\n"
          "[0] ⚡~Anuluj")
def print_modify_worker():
    print("\n[1] ⚡~Zmien login\n"
          "[2] ⚡~Zmien hasło\n"
          "[3] ⚡~Zmien nazwisko\n"
          "[0] ⚡~Anuluj")
def worker_or_menago():
    print("\n[1] ⚡~Dodaj Pracownik\n"
          "[2] ⚡~Dodaj Manager\n"
          "[0] ⚡~Anuluj")