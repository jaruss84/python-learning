# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

x="Hello World"
print(x)
napis="witaj na ZIiP"
calkowita=20
rzeczywista=10.0
type(napis)
type(calkowita)
type(rzeczywista)
print("Nasze zmienne to napis: {}, rzeczywista: {}, calkowita: {}".format(napis, rzeczywista, calkowita))
lista=[1,2,"dupa",3,3==3,5,6<10]
print(lista)

lista= []\
    
napis="Ala ma kota, a kot ma Alę"
kot=(napis[14:18])
print(kot)

lista=[1,2,3,"czapka"]
print(lista)

imie="Jarek"
wiek=37
if imie=="Jarek" and wiek==37:
        print("Nazywam sie Jarek i mam 37lat")
if imie=="Jarek" or imie=="Stefan":
    print("nazywam sie Jarek lub nie wiem")


CzyJestSobota=True
CzyJestWieczor=True
CzyJestCieplo=True

if CzyJestSobota==True and CzyJestWieczor==True and CzyJestCieplo==True:
    print("Idziemy na miasto")
    
Warunek1=True
Warunek2=False


if Warunek1 and Warunek2:
    print("Oba warunki sa spelnione")
elif Warunek1 or Warunek2:
    print("jeden z warunkow jest spelniony")
else:
    print("jeden z warunkow nie jest spelniony")
    
    
owoce=["jabko", "pomarancza", "kokos"]
if "pomarancza" in owoce:
    print("jest pomarancza!")
else:
    print("niestety nie ma pomaranczy ")


owoce=["jabko", "pomarancza","kokos", "gruszka", "truskawka" ]
x=owoce[-1]
print(x)

y=owoce[1:3]
print(y)

z=owoce[::-1]
print(z)


zbior1= set(["pomarancza", "arbuz", "banan"])
zbior2= set(["truskawka","arbuz","banan"])

zbior3= zbior1.intersection(zbior2)
print(zbior3)

zbior4= zbior1.union(zbior2)
print(zbior4)

rng = range(10)
print(rng)


rng = range(5,20)
print(rng[0])
print(rng[1])   
print(rng[2])
print(rng[3])
print(rng[4])
print(rng[5])


for i in range(5,21):
    print(i)
name = input("Jak masz na imie?")
print("czesc{}.".format(name))


for i in range(0,3):
    name=input("Jak masz na imie?")
    print("Czesc{}".format(name))

for i in range(1,10):
    print(i)


for t in range(1,100):
    if t % 7==0:
        print("Podzielna przez7!")





lata = int(input())
oprocentowanie = float(input())
kapital = int(input())

for i in range(lata+1):
    kapital = kapital + kapital * oprocentowanie
    print(kapital)


for x in range(1,100):
    if x % 7 == 0:
        print("{}-Podzielna przez 7!".format(x))
    else:
        print(x)


Lista= ['pomarancza', 'arbuz', 'banan']
i=1
for x in Lista:
    print("{} - {}".format(i,x))
    i=i+1  



Lista= ['pomarancza', 'arbuz', 'banan']

for i,x in enumerate(Lista):
    print("{} - {}".format(i+1,x))
    
    
for a,x in enumerate(range(100,200)):
     if  x % 7==0:
         print("{} {} - Podzielna przez 7!".format(a,x))


else:
    print("{} {}".format(a,x))
    
    
    
a=7
while a>4:
    a = int(input("Podaj liczbe wieksza od 4:"))
    print("Podano liczbe: {}".format(a))
    print("Twoja liczba nie byla wieksza od 4")


i=0
while i < 100:
    print(i)
    i=i+1

i=100
while i>0:
    print(i)
    i=i-1
    
i=0
x=0
while i<10:
    i=i+1
    x=x+i
    print(x)

import random
rand = random.randint(1,30)
pick=0
while pick !=rand:
    pick=int(input("Podaj liczbe między 1-30"))
    if pick>rand:
        print('Żle!!! Twoj pick jest za duzy')
    elif pick<rand:
        print("Żle!! Twoj pick jest za maly")
    print("-"*30)
print("Wygrany numer to",rand,"Dobra robota")



import random
rand = random.randint(1,30)
i=0
while i!=rand:
    i=int(input("Podaj liczbe calkowita"))
if i>rand:
    print("Liczba niepoprawna. Liczba za duza")
elif i<rand:
    print("Liczba nieporawna. Liczba za mala")
    print("Zgadles",rand,"Dobra robota")




import random
rand = random.randint(1,30)
i=1
while i!=rand:
    i=int(input("Podaj liczbe:"))
    if i > rand:
        print("Podana liczba jest za duza")
    if i < rand:
        print("Podana liczba jest za mala")
        print("Brawo")



Lista = ["A","B","C","D","E","F"]
i=1
for x in Lista:
    print("{} {}".format(x,i))
    i=i+1

with open("C:/Users/jarus/OneDrive/Pulpit/pliki/plik.txt", 'w') as plik:
    plik.write('Hello')
    plik.close()
    
    
with open("C:/Users/jarus/OneDrive/Pulpit/pliki/plik.txt", 'r') as plik:
    print(plik.read())
    plik.close()
    
    
for i in range(10):
    with open("C:/Users/jarus/OneDrive/Pulpit/pliki/plik {}.txt".format(i)) as plik:
        plik.write('Numer: {}'.format(i))
        plik.close()



for i in range(1,100):
    with open(r'C:\Users\jarus\OneDrive\Dokumenty\moje pliki\plik,txt', 'w') as plik:
    



import random
for i in range(100):
    rand = random.randint(1, 100)
with open(r'C:\Users\jarus\OneDrive\Dokumenty\moje pliki\plik.txt'.format(i), 'w') as plik:
        plik.write(str(rand))
        plik.close()



Lista = ['Element 1', 'Element 2', 'Element 3']
with open(r'C:\Users\jarus\OneDrive\Dokumenty\moje pliki\plik.txt','w') as plik:
        plik.writelines(Lista)
        plik.close()

Lista = ['Element 1', 'Element 2', 'Element 3']
with open(r'C:\Users\jarus\OneDrive\Dokumenty\moje pliki\plik.txt', 'w') as plik:
    for i in Lista:
        plik.write('{}'.format(i))
    plik.close()



import os

print(os.getcwd())


os.chdir(r'C:\Users\jarus\OneDrive\Dokumenty\moje pliki')
    print(os.listdir(os.getcwd()))




import os
lista = os.listdir('C:/Windows')
with open(r'C:\Users\jarus\OneDrive\Dokumenty\moje pliki\plik.txt', 'w') as plik:
    for i in lista:
        plik.write('{}\n'.format(i))
    plik.close()

wynik = 0
i = 0
while i < 3:
    x = int(input("Podaj parzystą, dodatnią liczbę:"))
    if (x > 0 and x % 2 == 0):
        wynik += x
    else:
        print("Miała być liczba dodatnia parzysta, zapytam się o liczbę ponownie")
        continue
    print("Aktualny wynik dodawania to:", wynik)
    i += 1

    
    





szukanaLiczba = 100
zgadywanaLiczba = 0

while zgadywanaLiczba != szukanaLiczba:
    zgadywanaLiczba = int(input("Liczba której szukasz to:"))
    if (zgadywanaLiczba < szukanaLiczba):
        print("za mala")
    elif (zgadywanaLiczba > szukanaLiczba):
        print("za duza")
    else:
        print("Brawo")



lista = [1,56,"Stefan",84,120]
lista2 = ["Krzysiek","Arek","Stefan","Franek"]
for i in lista:



definicje={}    
while(True):
    print("1: Stworz definicje")
    print("2: Znajdz definicje")
    print("3: Usun definicje")
    print("4: Zakoncz")
    wybor=input("Co chcesz zrobic?")
    if (wybor=="1"):
        klucz=input("Podaj slowo do zdefiniowania:")
        definicja=input("Podaj definicje:")
        definicje[klucz]=definicja
        print("Definicja dodana pomylnie")
    elif (wybor=="2"):
        klucz=input("Podaj definicje:")
        if klucz in definicje:
            print(definicje[klucz])
        else:
            print("Nie znaleziono definicji",klucz)
    elif (wybor=="3"):
        klucz=input("Podaj definicje:")
        if klucz in definicje:
            del definicje[klucz]
            print("Usunieto definicje o nazwie :",klucz)
        else:
            print("Nie znaleziono definicji o nazwie:",klucz)
    elif (wybor=="4"):
        print("Konczymy prace")
        break
    else:
        print("Podales cos z poza zakresu")
        
        
        
 names={"Arkadisz","Bartosz","beata","Cezary","Krzysztof","Zenon"}       
        
        
names={name.capitalize()
       for name in names
       if name.startswith("B")
       del name in names}
print(names)   

for i in range(2,471):
    if (i % 7== 0) and (i % 5 !=0):
        print("Liczba",i,"jest podzielna przez 7 ale nie jest podzielna prze 5")
        
numbers=[
    number
    for number in range(2,471)
    if (number%7==0) 
    if (number%5!=0)
    ]
print(numbers)


def wiadomosc_powitalna(imie):
    print("Czesc",imie,"witam Cie w moim programie")
imiona=["Stefan","Ania","Franek"]
for imie in imiona:
    wiadomosc_powitalna(imie)



def pole_prostokata(a,b):
    print(a*b)
pole_prostokata(8, 9)

import math

print("Witam Cię w programie obliczającym pola figur!!!")

def pole_kwadratu(a):
    return a * a

def pole_prostokata(a, b):
    return a * b

def pole_kola(r):
    return math.pi * r ** 2

def pole_trojkata(a, h):
    return 0.5 * a * h

def pole_trapezu(a, b, h):
    return (a + b) / 2 * h

while(True):
    
    print("1- Jesli chcesz obliczyć pole kwadratu")
    print("2- Jesli chcesz obliczyć pole prostokata")
    print("3- Jesli chcesz obliczyć pole koła")
    print("4- Jesli chcesz obliczyć pole trójkąta")
    print("5- Jesli chcesz obliczyć pole trapezu")
    print("6- Jesli chcesz zakończyć program")
    print("\n")
    wybor= int(input("Wybierz jakie pole obliczamy: "))
    if wybor==1:
        a=int(input("Podaj długosć boku: "))
        print("Pole powierzchni kwadratu o boku: ",a, "wynosi: ",pole_kwadratu(a))
    elif wybor==2:
        a=int(input("Podaj długosc pierwszego boku: "))
        b=int(input("Podaj długosc drugiegi boku: "))
        print("Pole powierzchni prostokąta o bokach: ",a,"i",b,"wynosi",pole_prostokata(a, b))
    elif wybor==3:
        r=int(input("Podaj długosć promienia: "))
        print("Pole powierzchni koła o promieniu: ",r,"wynosi: ",pole_kola(r))
    elif wybor==4:
        a=int(input("Podaj długosć podstawy trójkąta: "))
        h=int(input("Podaj wysokosć trójkąta: "))
        print("Pole trójkąta o długoci podstawy: ",a,"i wysokoci: ",h,"wynosi: ",pole_trojkata(a, h))
    elif wybor==5:
        a=int(input("Podaj długosć górnej podstawy trapezu: "))
        b=int(input("Podaj długosć dolnej podstawy trapezu: "))
        h=int(input("Podaj wysokosć trapezu: "))
        print("Pole powierzni trapezu o podstawach: ",a,"i",b,"i wysokosci",h,"wynosi: ",pole_trapezu(a, b, h))
    elif wybor==6:
        print("Kończymy. Pa Pa :)")
        break
    else:
        print("Błedny wybór!!. Wybierz jeszcze raz proszę")
        
    
user_number=int(input("Wpisz liczbę do której mam sumować: "))
num_gen= (number 
for number in range(user_number+1))
print(sum(num_gen))


import time    
def sumuj_do(liczba):
     return sum(liczba for liczba in range(1,liczba+1))



def time_prformance(func,arg,how_many_times=1):
     for i in range(1,how_many_times):
         start=time.perf_counter()
         func(arg)
         end=time.perf_counter()
         return end-start 
print(time_prformance(sumuj_do,4000,8))
    
import time

def funktion_performance(func,*arg,how_many_times=1):
    sum=0
    
    for i in range(0,how_many_times):
        start=time.perf_counter()
        func(*arg)
        end=time.perf_counter()
        sum=sum+(end-start)
        return sum
setContainer= {i for i in range(1000)}
listContainer=[i for i in range(1000)]
def szukamy_liczby(liczba,container):
    liczba=int(input("Podaj liczbę: "))
    if liczba in setContainer:
        return True
    else:
        return False
print(funktion_performance(szukamy_liczby,450,setContainer,how_many_times=300))   
print(funktion_performance(szukamy_liczby,450,listContainer,how_many_times=300))    
  
    
import math
def count(*args):
    sum=0
    liczby=[*args]
    for arg in liczby:
        sum=sum+arg
    print("Suma wszystkich liczb",liczby,"Wynosi:")   
    return sum
print(count(2,8,75,258))

import math
def count(ile):
    suma=0
    lista=[]
    for i in range(0,ile):
        lista.append(x)
        x=int(input()
        suma+=x
    print(lista)
    return suma
print(count(5))
        
def zbieranie_liczb (ile):
    lista = []
    print ("Podaj",ile,"liczb całkowitych: ")
    for i in range (0,ile):
        a = int(input())
        lista.append(a)
    print("Podane liczby to: ", lista)
    return lista
    
def sumowanie (func, ile):
    lista2 = func(ile)
    sum = 0
    for i in lista2:
        sum = sum + i
    print ("Suma tych liczb wynosi: ")
    return sum
 
print (sumowanie(zbieranie_liczb, 5))

    
 
def podaj_liczby(n):
    lista = []
    suma = 0
 
    for i in range(0, n):
        x = int(input("Wstaw liczby: "))
        lista.append(x)
        suma += x
 
    print(lista)
    return suma
 
print(podaj_liczby(5))      
  
import math    
def liczyc(*args):
     sum=0
     liczby=[*args]
     for i in liczby:
         sum=sum+1
         print("Suma wszystkich liczb",liczby,"wynosi: ")
         return sum
print(liczyc(5,5,6,5,2,5))
    
import random
cardList = ["9", "9", "9", "9",
"10", "10", "10", "10",
"Jack", "Jack", "Jack", "Jack",
"Queen", "Queen", "Queen", "Queen",
"King", "King", "King", "King",
"Ace", "Ace", "Ace", "Ace",
"Joker", "Joker"]
random.shuffle(cardList)  
listaGracza1=[]
listaGracza2=[]
def losowanieKart(iloscKart,dlaKogo):
    for i in range(0,iloscKart):
        karta=cardList.pop()
        dlaKogo.append(karta)
        
losowanieKart(5, listaGracza1) 
losowanieKart(5, listaGracza2)   
print(listaGracza1)  
print(listaGracza2)    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
    
    
    
    
    
    
























        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        









    
