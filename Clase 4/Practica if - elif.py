# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 18:33:16 2023

@author: jfoje
"""

Cal_p='A1'
print('Calificaciones: A1 - B1 - C1 - D - E')
Cal_a=input('ingrese Calificación del Cliente ' )

if Cal_p==Cal_a:
    print('nivel de riesgo bajo')
else:
    if Cal_a==str('B1'):
        print('nivel de riesgo deficiente')
    else:
        if Cal_a==str('C1'):
            print('nivel de riesgo potencial')
        else:
            if Cal_a==str('D'):
                print('nivel de riesgo dudoso recaudo')
            else:
                if Cal_a==str('E'):
                    print('nivel de riesgo perdida')
                else:
                    print('Valor ingresado es erroneo')

# elif
print('Segmentos: CO - IN')
Segmento=input('ingrese Calificación del Cliente ' )
Mora=int(input('ingrese días retraso '))

if Segmento==str('CO') and Mora>30:
    print('Vencido')
elif Segmento==str('CO') and Mora<=30 and Mora>0:
    print('En Mora')
elif Segmento==str('IN') and Mora>60:
    print('Vencido')
elif Segmento==str('IN') and Mora<=60 and Mora>0:
    print('En Mora')

else:
    print('error')