# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 18:52:53 2023

@author: jfoje
"""

def division(b , a):
        d=float(int(b)/int(a))
        print('el resultado es: ',d)


x=int(input('ingrese el primer valor  '))
y=int(input('ingrese el segundo valor '))
division(y,x)


def multiply (z,c):
    print(int(z)*int(c))
    return float(z*c)

resultado=multiply(x,y)


#lista

def lista1(lista):
    for item in lista:
        print('Hola',item )
        print('\n')
        print(type(lista))

lista1(['Jean'])

#tupla

def lista1(*lista):
    for item in lista:
        print('Hola',item )
        print('\n')
        print(type(lista))
lista1(['Jean'])