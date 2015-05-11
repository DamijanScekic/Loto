__author__ = 'Windows'

from random import randint

print ("Dobrodosli v Igri loto")
odgovor = int(raw_input("Koliko stevil zelis vplacati? "))

def zrebanje(x):
    seznam = []
    for stevilo in range (0,x):
        stevilo = randint (0,99)
        seznam.append(stevilo)
    print("Izzrebana stevila so: ")
    print(seznam)
    print("Zelimo vam veliko srece pri zrebanju. ")
zrebanje(odgovor)

