# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:12:04 2023

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

def cuadratica(a, b, c):
    d1=b+(b**2 -4*a*c)**(1/2)
    d2=b-(b**2 -4*a*c)**(1/2)
    if abs(d1)>abs(d2):
        res=d1
    else:
        res=d2
    return res
    
def muller(funcion, x0, x1, x2, paro):
    error_relativo=paro + 1
    iteraciones=0
    resultados=[]
    while abs(error_relativo)>paro: 
        e_0=f(x0) - f(x2)
        e_1=f(x1) - f(x2)
        h_1=x1-x2
        h_2=x0-x2
        w=(h_1*(h_2)**2) - (h_2*(h_1)**2)
        a=((e_0*h_1)-(e_1*h_2))/w
        b=((e_1*(h_2)**2) - (e_0*(h_1)**2))/w
        c=f(x2)
        res=cuadratica(a, b, c)
        x3=x2 - ((2*c)/res)
        error_absoluto=abs(x3-x2)
        error_relativo=error_absoluto/abs(x3)
        x2=x3
        iteraciones+=1
        resultados.append([x3, error_relativo, error_absoluto, iteraciones])
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
x0=float(input("Ingrese el primer punto a evaluar: "))
x1=float(input("Ingrese el segundo punto a evaluar: "))
x2=float(input("Ingrese el tercer punto a evaluar: "))
print("\n")
#determinar la existencia de raíz en los puntos
comprobacion=0
if f(x0)==0:
    comprobacion=1
    print(f"El valor [{x0}] pertenece como raíz de la función {funcion_str}.")
if f(x1)==0:
    comprobacion+=1
    print(f"El valor [{x1}] pertenece como raíz de la función {funcion_str}.")
if f(x2)==0:
    comprobacion+=1
    print(f"El valor [{x2}] pertenece como raíz de la función {funcion_str}.")
#if comprobacion==0:
    #print(f"Se encontró {comprobacion} raíces cercanos a los puntos {x0}, {x1}, {x2}. Por favor, ejecute nuevamente el programa y elija nuevos puntos.")
if comprobacion>=2:
    print(f"Se dará a finalizar el programa, el método ha encontrado {comprobacion} raíces de la función ingresada.")
    exit(0)
    
#Criterio de paro (solicitud)
paro=int(input("Ingrese la cantidad de decimales para el criterio de paro: "))
paro1=paro
paro=10**(-paro)

#Llamamos las funciones y resultados
resultados=muller(funcion, x0, x1, x2, paro)

#Crear la tabla con encabezados
tabla=PrettyTable()
tabla.field_names=["Iteración", "Raíz", "Error Relativo", "Error Absoluto"]

#Llenar la tabla con resultados
for i, (raiz, error_rel, error_abs, iteraciones) in enumerate(resultados, start=1):
    tabla.add_row([i, raiz, error_rel, error_abs])
    
#Mostrar tabla con resultados
print(tabla)
print ("En la iteración", iteraciones,", el valor", f"{raiz:.{int(paro1)}f}", "es una buena aproximación a la raíz.")