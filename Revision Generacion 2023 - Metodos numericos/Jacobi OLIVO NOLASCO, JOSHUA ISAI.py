# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 10:10:48 2023

@author: josho
"""

import re
import numpy as np
#import matplotlib.pyplot as plt
#from prettytable import PrettyTable
vectores=[]
A=[]
b=[]
x=[]
resultados=[]

print("\nEste programa funciona únicamente con matrices cuadradas.")
A1=[[1,2,3],
   [4,5,6],
   [7,8,9]]
B1=[[1], [2], [3]]
print("Ejemplo de Matriz: ")
for renglon in A1:
    print(renglon) 
print("\nEjemplo de vector solución del sistema: ")
for renglon in B1:
    print(renglon)

print("Siguiendo el primer ejemplo, la dimensión de los vectores es 3.")
dimA=int(input("Ingrese la dimensión de los vectores: "))
print("\nIngrese los valores de la matriz por renglón: ")
for i in range(dimA):
    renglones=input("")
    vectores=[float(p) for p in re.findall(r"-?\d+\.?\d*", renglones)]
    A.append(vectores)

print("\nIngrese los valores del vector solución que corresponden a la matriz ingresada: ")
for i in range(dimA):
    vn=float(input(""))
    b.append(vn)

o=int(input("Desea ingresar una estimación inicial para iniciar con el método de Jacobi? Si: 1.    No: 0.    \n"))
if o==1:
    print("Ingrese el vector: ")
    for i in range(dimA):
        a=float(input(""))
        x.append(a)
else: 
    for i in range(dimA):
        a=1.0
        x.append(a)
print("\nMatriz ingresada: ")
for renglon in A:
    print(renglon) 
print("\nVector ingresado: ")
for renglon in b:
    print("[", renglon, "]") 
    
print("\n Estimación iniciai: ")
for renglon in x:
    print("[", renglon, "]")


    
tolerancia=int(input("A cuántos decimales desea que finalice el método? Ejemplo: 4.    "))
tolerancia_1=10**(-tolerancia)
L = np.tril(A, k=-1)
U = np.triu(A, k=1)
D=np.diag(np.diag(A))

dinv=np.linalg.inv(D)
C=np.dot(dinv, b)
R= (L + U)*-1
T = np.dot(dinv, R)

valpropios=np.linalg.eigvals(T)
radioT=np.max(np.abs(valpropios))

print("\nMatriz T, siendo ésta D^(-1)*(L*U) :")
for renglon in T:
    print(renglon)
print("\nRadio espectral de T (Criterio de convergencia): ", radioT)
if radioT>1:
    print("Una de las condiciones de criterio de convergencia, es que el radio espectral de la matriz T sea menor a 1, para obtener una mayor confirmación de convergencia.")
    print("Posiblemente el método no convergerá. Analice los resultados siguientes. \n")
norma_residuo=tolerancia
k=0
while norma_residuo > tolerancia_1: 
    W=np.dot(T, x)
    x0=x
    x=W + C
    norma_residuo=np.linalg.norm(x - x0)
    k+=1
    resultados.append([x, norma_residuo, k])


print(f"En la iteración {k}, se obtuvo el vector resultante: ", x, "y se obtuvo una norma de :", norma_residuo)