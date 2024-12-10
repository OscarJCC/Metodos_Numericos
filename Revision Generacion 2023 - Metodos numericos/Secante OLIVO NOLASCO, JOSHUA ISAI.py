# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:12:49 2023

@author: josho
"""

import numpy as np
from math import *
import matplotlib.pyplot as plt
from prettytable import PrettyTable
#se definen euler y pi para posibles calculos del numero de euler y pi
e=np.e
pi=np.pi

def f(x):
    return eval(funcion_str)

def secante(funcion, x0, x1, paro):
    error_relativo=paro + 1
    iteraciones=0
    resultados=[]
    while abs(error_relativo)>paro:
        x2=x0 - f(x0)*(x1-x0)/(f(x1)-f(x0))
        error_absoluto=abs(x2-x0)
        error_relativo=error_absoluto/abs(x2)
        x0=x2
        iteraciones+=1
        resultados.append([x0, error_relativo, error_absoluto, iteraciones])
        if iteraciones>1000:
            break
    return resultados
#Ingreso de la función
funcion_str=input("Ingresa la función (en términos de x): ")

#Convertir la cadena de texto en una función  
try:
    funcion=lambda x: eval(funcion_str)
except:
    print("La función ingresada no es válida.")
    exit(1)

#Crear un rango de valores de x
x_values=np.linspace(-10, 10, 400)
y_values=[funcion(x) for x in x_values]

#Graficar la función
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='Función')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfica de la Función')
plt.grid(True)
plt.legend()

#Mostrar la gráfica
plt.show()
print("\nLa siguiente gráfica representa la función ingresada... ")
#Punto en el que se calculará la raíz
x0=float(input("Ingrese el valor mínimo del intérvalo: "))
x1=float(input("Ingrese el valor máximo del intérvalo: "))

#determinar la existencia de raíz en los intérvalos
if (f(x0) * f(x1))>0:
    print("\nError en la continuación del programa, puede deberse a:")
    print("\n 1) En los valores ingresados [",x0,",",x1,"] no existen raíces reales en la función:",funcion_str,". Debido al Teorema de Bolzano y la determinación de raíces en intérvalos [a,b], debido a una divergencia.")
    print("\n 2) Es posible la existencia de 2 o más raíces en la función.")
    print("\n 3) El intérvalo ingresado contiene un máximo o un mínimo de la función.")
    print("Iniciar nuevamente el programa e ingrese un intervalo más próximo a la raíz deseada para una aproximación más precisa.")
    exit
        
#determinar si los valores son raíces de la función
while f(x0)==0:
    print("\nEl valor inicial [",x0,"] es una raíz de la función:",funcion_str)
    x0=float(input("Ingrese otro valor mínimo del intérvalo: "))
while f(x1)==0:
    print("\nEl valor final [",x1,"] es una raíz de la función:",funcion_str)
    x1=float(input("Ingrese otro valor máximo del intérvalo: "))
#condicional para evitar indeterminaciones
if f(x0) == f(x1):
    print("\nPor favor, ingrese un nuevo intérvalo de valores; debido a un error de indeterminación de la fórmula del método.")
    x0=float(input("Ingrese el valor mínimo del intérvalo: "))
    x1=float(input("Ingrese el valor máximo del intérvalo: "))
#Criterio de paro (solicitud)
paro=int(input("Ingrese la cantidad de decimales para el criterio de paro: "))
paro1=paro
paro=10**(-paro)

#Llamamos las funciones y resultados
resultados=secante(funcion, x0, x1, paro)

#Crear la tabla con encabezados
tabla=PrettyTable()
tabla.field_names=["Iteración", "Raíz", "Error Relativo", "Error Absoluto"]

#Llenar la tabla con resultados
for i, (raiz, error_rel, error_abs, iteraciones) in enumerate(resultados, start=1):
    tabla.add_row([i, raiz, error_rel, error_abs])
    
#Mostrar tabla con resultados
print(tabla)
print ("En la iteración", iteraciones,", el valor", f"{raiz:.{int(paro1)}f}", "es una buena aproximación a la raíz.")