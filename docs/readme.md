# Stipant

## System zarządzania projektami

### Opis:

#### System do zarządzania projektami, zadaniami, pracownikami
System pozwala na przegląd projektów, dodanie nowego, zmiana parametrów projektu, zmiane właściciela projektu, przypisanie/odpisanie osób z projektów, podgląd przypisanych zadań do projektu
Dodawanie zadań wraz z właścicielem i podpiąć zadanie do projektu, modyfikacja statusu oraz priorytetu zadania. Dopisywanie logów do zadania, przeglądanie logów
Dodawanie użytkowników, zmiane ich loginu, hasła, nazwiska

### Wymagania:
Statusy, Priorytety
1. Logowanie do systemu

#### Poniższe punktu działają w wersji próbnej systemu, obsługuje tylko typ pracownika 'Project Manager'
2. Wylistowanie przypisanych do zalogowanego zadań
3. Wylistowanie przypisanych do zalogowanego projektow
4. Modyfikuje wybrane przypisane zadanie
   1. Dodaje nowe zadanie
      1. Z nazwą, opisem, datą rozpoczęcia, datą zakończenia, statusem, priorytetem, z przypisanym właścicielem
         1. Status ->(Otwarte, W toku, Zamknięte, Blokada)
         2. Priorytet ->(Bardzo niski, Niski, Normalny, Wysoki, Bardzo wysoki)
   2. Dodaje Loga do zadania
      1. Log ma swój opis, spędzony czas, podpięte zadanie, oraz informacje o właścicielu Loga
   3. Listuje logi wybranego zadania
   4. Zmienia status, priorytet zadania
   5. Zmienia właściciela zadania
5. Zarządzanie projektem
   1. Listuje przypisane projekty
   2. Pozwala dodać nowy projekt 
      1. Z podaną nazwą, opisem, datą startu, datą zakończenia, przypisaną osobą odpowiedzialną (Musi to być Project Manager)
   3. Modyfikować przypisany, wybrany projekt 
      1. Zmiana właściciela projektu 
      2. Podanie nowych dat rozpoczęcia, zakończenia projektu
      3. Dopisanie pracownika do projektu
      4. Usunięcie pracownika z projektu
      5. Wylistowanie zadań podpiętych do projektu
      6. Wylistowanie pracowników podpiętych do projektu
6. Zarządza pracownikami
   1. Listuje wszystkich pracowników
   2. Dodaje pracownika
   3. Zarządza wybranym pracownikiem
      1. Zmiana loginu
      2. Zmiana hasła
      3. Zmiana nazwiska
7. System korzysta z plików txt które służą jako 'baza' systemu. Wszelkie zmiany są wprowadzane do plików, tak by przy ponownym uruchomieniu mogły się zaczytać
8. System uniemożliwia podania błędnych wartości w różnych menu programu
9. Wszelkie elementy projektowe(projekty, zadania, logi, użytkownicy) mają swoje unikalne ID

## Jak korzystać z systemu
Zalecane jest uruchomienie projektu za pomocą ide Pycharm

W różnych miejscach systemu, program prosi nas o wybranie odpowiedniej opcji poprzez wskazanie jej numeru. Wpisując numer i potwierdzając enter

[x] ~ opcja x | <- gdzie x to numer opcji x

[x] ⚡~ opcja x | <-  '⚡' informuje o tym, że w tym menu nie trzeba potwierdzać enterem wybranej opcji. 
Opcja wybierze się zaraz po kliknięciu odpowiedniego numeru

Wpierw trzeba się zalogować (Dane logowania można podejrzeć w folderze /files/login.txt) Podając login i hasło

Po zalogowaniu jesteśmy przenoszeni do głównego menu Menagera w którym wyświetlaja się opcje co możemy zrobić(patrz wymagania) System przenosi nas wtedy dalej do kolejnych menu w których jesteśmy proszeni o wybór opcji lub wpisanie pewnych wartości.
W zależności od wybranej opcji czasem trzeba wpisać wartośc lub wybrać z listy element podając jego [id]. Podawane dane przez użytkownika nie są walidowane w żaden sposób
### Wymagania systemowe Systemu Stipant
Zalecane jest uruchomienie projektu w środowisku Pycharm 
#### Konfiguracja projektu w Pycharm
Python 3.11
- script: wskazuje na plik main.py w projekcie
- working directory: wskazuje na folder 'src' projektu
- enviorment variables: wskazuje PYTHONUNBUFFERED=1;PYTHONPATH=C:\Users\\...\PPy\PPYProject\src
- Opcje dodatkowe
  - 'Open run/debug tool window when started'
  - 'Add content roots to PYTHONPATH'
  - 'Add source roots to PYTHONPATH'
  - 'Emulate terminal in output console'



Wykonał: Grzegorz Orłowski s26489
## Licencja

[MIT](https://choosealicense.com/licenses/mit/)

