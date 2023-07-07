# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 19:38:02 2023

@author: jfoje
"""

texto=[input('ingrese un texto ')]

letra=input('ingrese las letras')  
for i in texto:

    x=str.count(i,letra)
    print(x )
    
R=[]
S=[]
AP=[]
FW=[]
lista=["R1","R2","R3",
       "S1","S2","S3",
       "AP1","FW1"]


for elemento in lista:
    if "R" in elemento:
        R.append(elemento)
    elif "S" in elemento:
        S.append(elemento)
    elif "AP" in elemento:
        AP.append(elemento)
    elif "FW" in elemento:
        FW.append(elemento)

print("Router",R, 
      "Switch",S, 
      "Objetos",AP,FW)