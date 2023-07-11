# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 18:15:09 2023

@author: jfoje
"""
# ejercicio clase
contar=int(input('ingrese valor a contar'))
contador=0

while contador<=contar:
    print(contador)
    contador+=1


# ejercicio bucle cont
contar1=int(input('ingrese valor a contar '))
contador1=0

while True:
    print(contador1)
    contador1+=1
    if contador1>contar1:
        break
    
 # practica 1  
while True:
    x=input('ingrese el numero a contar ')
    if x=='q' or x=='quit':
        print('Proceso Finalizado')
        break
    else:
        x=int(x)
        y=1 
        while True:
            print(y)
            y=y+1
            if y>x:
                 break
            