# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 23:49:12 2023

@author: josho
"""

import matplotlib.pyplot as plt
import numpy as np
import re

print("Ejemplo: /Users/josho/OneDrive/Escritorio/tabla.txt")
archivo=input("En base al ejemplo anterior, ingrese el directorio del archivo a analizar: ")

x_datos=[]
y_datos=[]
xy_datos=[]
x2_datos=[]
matriz=[]
with open(archivo, 'r') as file:
    for linea in file:
        print(linea)
    estilo=int(input("\nEl archivo es vertical u horizontal?     1 = Vertical.   0 = Horizontal\n"))
    encabezadosup=int(input("\nTiene encabezado superior unicamente de letras?   1 = Si.  0 = No.\n"))
    
    file.seek(0)
    #Leemos los datos si tienen encabezados o no
    xsum=0
    ysum=0
    xysum=0
    x2sum=0
    if (estilo == 1) and (encabezadosup == 1):
        next(file)  
        for linea in file:
            x, y=map(float, linea.strip().split(','))
            xy=x*y
            x2=x*x
            x2sum+=x2
            xysum+=xy
            xsum+=x
            ysum+=y
            x2_datos.append(x2)
            x_datos.append(x)
            y_datos.append(y)
            n=len(x_datos)
            xy_datos.append(xy)
    if (estilo == 1) and (encabezadosup == 0): 
        for linea in file:
            x, y=map(float, linea.strip().split(','))
            xy=x*y
            xysum+=xy
            xsum+=x
            ysum+=y
            x_datos.append(x)
            n=len(x_datos)
            y_datos.append(y)
            xy_datos.append(xy)
    
    #Si el archivo es horizontal
    if estilo == 0:
        if encabezadosup==1:
            next(file)
        for linea in file:
            vectores=[float(p) for p in re.findall(r"-?\d+\.?\d*", linea)]
            matriz.append(vectores)
        for i in matriz[0]:
            xsum+=i
            x2=i*i
            x2_datos.append(x2)
            x2sum+=x2
        for i in matriz[1]:
            ysum+=i
        xysum=sum(matriz[0][i]*matriz[1][i] for i in range(len(matriz[0])))
        n=len(vectores)
        print("Matriz de los valores: \n", matriz)
        x_datos=matriz[0]
        y_datos=matriz[1]
    
    l=(xsum*ysum)/n
    k=(xsum**2)/n
    m=(xysum-l)/(x2sum-k)
    b=(ysum/n)-(m*xsum/n)

    
print("\nA continuación se dará a conocer la gráfica de la recta correspondiente a los datos leídos mediante el método de mínimos cuadrados.")
x=np.array(x_datos)
y_pred = m * x + b

# Graficar los puntos originales
plt.scatter(x_datos, y_datos, label='Datos originales')
# Graficar la recta 
plt.plot(x, y_pred, color='red', label='Recta de ajuste')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Recta de ajuste por mínimos cuadrados')
plt.legend()
plt.grid(True)
plt.show()
    
file.close()