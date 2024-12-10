# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 10:11:12 2023

@author: josho
"""

import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
#se definen e y pi para posibles calculos del numero de euler y pi
e=np.e
pi=np.pi
def derivada(funcion, x):
    #Definición de la derivada
    h=1e-5
    derivada=(funcion(x+h)-funcion(x))/h
    return derivada

def newton(funcion, x, paro):
    error_relativo=paro + 1
    xi=x
    iteraciones=0
    resultados=[]

    while abs(error_relativo)>paro:
        xf=xi-(funcion(xi)/derivada(funcion, xi))
        error_absoluto=abs(xf-xi)
        error_relativo=error_absoluto/abs(xf)
        xi=xf
        iteraciones+=1
        resultados.append([xi, error_relativo, error_absoluto, iteraciones])

    return resultados

#Solicitar la función al usuario
funcion_str=input("Ingresa la función (en términos de x): ")

#Convertir la cadena de texto en una función de Python con lambda
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
print("\nEn base a la gráfica mostrada... ")
#Punto en el que se calculará la raíz
x=float(input("Ingresa el valor del punto más próximo a la raíz de la función: "))


#Criterio de paro (solicitud)
paro=int(input("Ingrese la cantidad de decimales para el criterio de paro: "))
paro1=paro
paro=10**(-paro)

#Llamamos las funciones y resultados
resultados=newton(funcion, x, paro)

#Crear la tabla con encabezados
tabla=PrettyTable()
tabla.field_names=["Iteración", "Raíz", "Error Relativo", "Error Absoluto"]

#Llenar la tabla con resultados
for i, (raiz, error_rel, error_abs, iteraciones) in enumerate(resultados, start=1):
    tabla.add_row([i, raiz, error_rel, error_abs])

#Mostrar tabla con resultados
print(tabla)
print ("En la iteración", iteraciones,", el valor", f"{raiz:.{int(paro1)}f}", "es una buena aproximación a la raíz.")