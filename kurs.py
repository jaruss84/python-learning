# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 13:01:13 2021

@author: jarus
"""

values=[]

for i in range(1,10):
    if i % 2 == 0:
        values.append(i)
    print(values)
    
    
    for i in range(0,100):
     if i%7==0:
        /=7:
    print(i)

def podwoj(x):
    return x*2
print(podwoj(6))

my_List=[6,99,54,23,54,79]
my_List_filtered=list(filter(lambda x: x%2==0, my_List))
print(my_List_filtered)


import random
x=0
while x<100:
    x=x+1
    print(random.uniform(0, 100))
import random    
def will_weapon_hit(weaponChanceToHitPercentage):
    isHitChance = random.uniform(0,100)
    if (isHitChance<weaponChanceToHitPercentage):
        return "Hit"
    else:
        return "not Hit"
x=0
listHit=[]
while x<100:
    x=x+1
    print(listHit.append(will_weapon_hit(50)))
from collections import Counter
dicionaryHit = Counter(listHit)


zdanie=["I","","L","o","v","e","","P","y","t","h","o","n"]
for x,k in enumerate(zdanie[::-1]):
    print(x+1,k)
    

zdanie=["I","","L","o","v","e","","P","y","t","h","o","n"]
for x,k in enumerate(zdanie):
    print(x+1,k,zdanie[-x-1])
import random    
skarb_ze_skrzynek=["zielona","pomaranczowa","purpurowa","legendarna"]
from collections import Counter
print(Counter(random.choices(skarb_ze_skrzynek,[80,15,4,1],k=100)))    


import random    
def choose_random_numbers(losowa,wszystkie_losowe):
    print(random.sample(range(wszystkie_losowe+1), losowa))
choose_random_numbers(6, 49)

import random
 
cardList = ["9", "9", "9", "9",
"10", "10", "10", "10",
"Jack", "Jack", "Jack", "Jack",
"Queen", "Queen", "Queen", "Queen",
"King", "King", "King", "King",
"Ace", "Ace", "Ace", "Ace",
"Joker", "Joker"]
 
 
random.shuffle(cardList)
 
listaKartGracza1 = []
listaKartGracza2 = []
 
def losowanieKart(iloscKart, dlaKogo):
    for i in range(0, iloscKart):
        karta = cardList.pop()
        dlaKogo.append(karta)
 
losowanieKart(5, listaKartGracza1)
losowanieKart(5, listaKartGracza2)
 
print(listaKartGracza1)
print(listaKartGracza2)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

