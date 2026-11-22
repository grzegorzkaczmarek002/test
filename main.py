# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

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
if __name__ == '__main__':
    print_hi('PyCharm')
    pole_kola(5)
    kasyno(20)
    dodaj(10,20)
    kalkulator(5,2,"pierwiastkowanie")
    temperatura(100)
    pole_kwadratu(4)
    zakup ("Chleb", 3.5, 3)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
