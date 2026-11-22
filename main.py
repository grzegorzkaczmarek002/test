# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
from contextlib import nullcontext


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def kasyno(wiek):
    if wiek >= 18:
        print ("Możesz wejść do kasyna")
    else:
        print ("Nie możesz wejść do kasna")

    for i in range (3):
        print (i)

    licznik = 0
    while licznik < 3:
        licznik += 1
def pole_kola(r):
    r = 5
    pole = math.pi * r ** 2
    print(f"Pole koła wynosi: {pole:.2f}")

def dodaj (a,b):
    wynik = a + b
    print(f"Wynik wynosi: {wynik}")
def kalkulator (a,b,operacja):
    if operacja == "dodawanie":
        wynik = a + b
    elif operacja == "odejmowanie":
        wynik = a - b
    elif operacja == "mnożenie":
        wynik = a * b
    elif operacja == "dzielenie":
        wynik = a / b
    elif operacja == "potęgowanie":
        wynik = a ** b
    elif operacja == "pierwiastkowanie":
        wynik = a ** (1/b)
    else:
        print ("Niepoprawna operacja")
        return 0
    print(f"Wynik wynosi: {wynik}")
def temperatura (celsjusz):
    fahrenheit = (celsjusz * 9/5) + 32
    print (f"{celsjusz}°C = {fahrenheit}°F")
def pole_kwadratu(a):
    pole = a ** 2
    print(f"Pole kwadratu wynosi: {pole}")
def zakup (produkt, cena, ilosc):
    koszt = cena * ilosc
    print (f"Produkt: {produkt} kosztuje: {koszt:.2f}")
class Samochod:
    def __init__(self,marka,model):
        self.marka = marka
        self.model = model
        self.przebieg = 0

    def jedz (self,kilometry):
        self.przebieg += kilometry
class Student:
    def __init__(self,imie, nazwisko, oceny):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny = oceny.copy()

    def srednia_ocen (self):
        if len(self.oceny) == 0:
            return "NONE"
        srednia = 0
        liczba_ocen = len(self.oceny)
        for ocena in self.oceny:
            srednia += ocena
        srednia = srednia / liczba_ocen
        return srednia



if __name__ == '__main__':
    print_hi('PyCharm')
    pole_kola(5)
    kasyno(20)
    dodaj(10,20)
    kalkulator(5,2,"pierwiastkowanie")
    temperatura(100)
    pole_kwadratu(4)
    zakup ("Chleb", 3.5, 3)
    owoce = ["jabłko", "banan", "gruszka"]
    owoce.append ("gruszka")
    owoce.insert(1, "pomarańcza")
    owoce.remove("banan")
    owoce.pop()
    print(f"{owoce}")
    lista1 = ["mail","raport", "telefon"]
    lista1.remove("mail")
    lista1.insert(0, "pilne")
    print (f"{lista1}")
    lista2 = [12,8,15]
    lista2.append(10)
    lista2.remove(min(lista2))
    lista2.sort(reverse=True)
    print(f"{lista2}")
    student = {"imie": "Jan", "oceny" : [4,5,3]}
    print(student["imie"])
    print(student.get("telefon","brak"))
    student ["wiek"] = 20
    x,y = (52.23,21.01)
    a = {1,2,3,4}
    b = {3,4,5,6}
    print(a & b)
    print (a - b)
    zbiory1 = {"rower", "kino"}
    zbiory2 = {"kino", "bieganie"}
    print(zbiory1 & zbiory2)
    print(zbiory1 - zbiory2)
    pies = {r"""
     / \__
    (    @\___
     /         O
    /   (_____/
    /_____/   U
    """}

    kot = {r"""
     /\_/\
    ( o.o )
     > ^ <
    """}

    przepiorka = {r"""
           __
      ____ (o)>
     /       /
    /_______/
       /  /
    """}
    zwierzeta = ["kot", "pies", "kot","przepiorka"]
    zbiory = {"kot": kot, "pies": pies, "przepiorka" : przepiorka}

    symbole = set()
    for zwierze in zwierzeta:
        symbole.update(zbiory[zwierze])

    for symbol in sorted(symbole):
        print(symbol)

    print("Liczba różnych symboli:", len(symbole))

    student = Student("Jan", "Kowalski", [4, 5, 3])
    srednia_ocen = student.srednia_ocen()
    print(f"{srednia_ocen}")