import os
###TODO skrypty dla projektow, logow, zadan,
###TODO teksty zagniezdzajace menu dla pracownika i menagera

def cls():
    os.system("cls")


def menu_login():
    print("\t\t\t\t\t***Stipant***\n"
          "Wybierz opcje:\n"
          "\t[1] ~Zaloguj\n"
          "\t[0] ~Wyjdź\n")


def login_content():
    return (
        "1;Gorlowski;1234\n",
        "2;Nowak;1243\n",
        "3;Kowalski;4321\n"
    )


def users_content():
    return (
        "1;Orłowski;Grzegorz;Project.py Manager\n",
        "2;Nowak;Daniel;Dev\n",
        "3;Kowalski;Jan;Dev\n"
    )


def welcome(lud):
    cls()
    if lud.stanowisko == 'Project Manager':
        print("\t\t\tWitamy Pana {} {} MENADŻERA\n".format(lud.imie, lud.nazwisko))
    else:
        print("\t\t\tDzień dobry {} {} {}  \n".format(lud.imie, lud.nazwisko, lud.stanowisko))


def manager_menu():
    print(
        "[1] ~Wyświetl zadania(w Jag.statusu, priorytetu, terminów, ludzi)\n",
        "[2] ~Wyświetl projekty\n",
        "[3] ~Zarządzanie zadaniem(dodaj, usuń, modyfikuj, przypisz / utworzZadania)\n",
        "[4] ~Zarządzanie projektem(dodaj, usuń, modyfikuj, przypisz / utworzZadania)\n",
        "[5] ~Zarządzanie pracownikiem(dodaj, usuń, modyfikuj, przypiszDoZadania)\n",
        "[0] ~Wyloguj"
    )



def worker_menu():
    print(
        "\n[1] ~Wyświetl zadania(wg. statusu, priorytetu, terminów, ludzi - przypisane do mnie)\n",
        "[2] ~Zarządzanie zadaniem(modyfikuj *(status, logi_pracy)* )\n",
        "[3] ~Wyświetl projekty(przypisane do pracownika)\n",
        "[0] ~Wyloguj\n"
    )
def print_manage_task():
    print(
        "\n[1] ~Dodaj zadanie\n"+
        "[2] ~Modyfikuj swoje zadanie \n"+
        "[0] ~Wyjdz\n"
    )
def print_modify_task():
    print("\n[1] ~Dodaj log\n"
          "[2] ~Wylistuj logi\n"
          "[3] ~Zmien status / priorytet\n"
          "[4] ~Zmien wlasciciela\n"
          "[0] ~Anuluj")