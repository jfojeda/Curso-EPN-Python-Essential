# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 19:31:48 2023

@author: jfoje
"""
#ejemplo clase arbol
class arbol:
    def __init__(self,Especie,Altura,Edad,Grosor,Tipo ):
        self.Especie=Especie
        self.Altura=Altura
        self.Edad=Edad
        self.Grosor=Grosor
        self.Tipo=Tipo
        
    def Florecer(self):
        print("Árbol floreciendo")
    def Crecer(self):
        print(self.especie,"Se registra nueva altura")
    def Oxigeno(self):
        print("Se registra tn de oxigeno")
    def info(self):
        print("Especie: ",self.Especie , "Tipo: ",self.Tipo)

a1=arbol("pino", 15, 5, 3.5, "Madera")
a2=arbol("mango", 12, 12, 2, "Frutal")
a3=arbol("podocarpus", 25, 70, 5, "Madera")

a1.info()
a2.Crecer()
a3.info()

print("\n"*2)

#ejemplo clase coche
class auto:
    def __init__(self,Marca,Anio,Cilindraje,Traccion,Capacidad ):
        self.Marca=Marca
        self.Anio=Anio
        self.Cilindraje=Cilindraje
        self.Traccion=Traccion
        self.Capacidad=Capacidad
        
    def Acelerar(self):
        print(self.Marca,self.Anio,"Acelerando al máximo permitido")
    def Frenar(self):
        print(self.Marca,self.Anio,"Tiempo de frenado eficiente")
    def Carga(self):
        print(self.Marca,self.Anio,"Carga hasta la indicada por el fabricante")
    def infoauto(self):
        print("Marca: ",self.Marca , "Año: ",self.Anio,"Tranccion: ",self.Traccion)

c1=auto("Kia", 2014, 2.0, "4x2", "5P")
c2=auto("Chevrolet",2019,3.4,"4x4","2P")
c3=auto("Nissan", 2023, 1.5, "4x2", "5P")

c1.Acelerar()
c2.Carga()
c3.infoauto()