# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 17:20:27 2022

@author: jarus
"""

for i in range(0,101):
    if  (i % 3==0 and i % 5==0):
        print("FizzBuzz")
    elif (i % 3==0):
        print("Fizz")
    elif (i % 5==0):
        print("Buzz")
    else:
        print(i)

lista = [1,-4,8,15,40,85,120]
najmniejsza=None
najwieksza=None
for i in lista:
    if najmniejsza==None or najmniejsza>i:
        najmniejsza=i
    if najwieksza==None or najwieksza<i:
        najwieksza=i
    print("Najamniejsza liczba to :",najmniejsza)
    print("Najwieksza liczba to :",najwieksza)

zdanie="Ala ma kota"
