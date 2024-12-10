# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 10:21:26 2023

@author: josho
"""

import numpy as np
import numpy.linalg as la

print("Ejemplo: /Users/josho/OneDrive/Escritorio/tabla.txt")
archivo=input("En base al ejemplo anterior, ingrese el directorio del archivo a analizar: ")

#Leer el archivo y extraer los datos numéricos
x_datos=[]
y_datos=[]

with open(archivo, 'r') as file:
    next(file)  #Salta la primera línea si contiene encabezados
    for linea in file:
        x, y=map(float, linea.strip().split(','))
        x_datos.append(x)
        y_datos.append(y)

#Grado del polinomio
grado=2

#Construir la matriz (utilizando algebra lineal)
A=np.vander(x_datos, N=grado + 1, increasing=True)

#Resolver el sistema de ecuaciones usando Gauss-Jordan de Numpy
A_transpuesta=np.transpose(A)
A_transpuesta_A=np.dot(A_transpuesta, A)
A_transpuesta_y=np.dot(A_transpuesta, y_datos)

#Resolución del sistema
coeficientes=la.solve(A_transpuesta_A, A_transpuesta_y)

#Crear la función polinómica a utilizar
def polinomio_interpolante(x, coeficientes):
    resultado=0
    for i, coef in enumerate(coeficientes):
        resultado+=coef*(x ** i)
    return resultado

#Valor a calcular
x_interpolar=float(input("Ingrese el valor a calcular: "))

#Calcular el valor interpolado
y_interpolar = polinomio_interpolante(x_interpolar, coeficientes)

#Impresión de resultados
print(f"Para el valor interpolado de {x_interpolar}, el resultado es {y_interpolar}")
