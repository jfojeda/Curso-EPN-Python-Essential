# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 18:57:46 2023

@author: jfoje
"""
lista=[]
archivo=open("devices.txt")
for elemento in archivo:
    elemento=elemento.strip()
    lista.append(elemento)
    print (elemento)
    
archivo.close()

