# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 10:28:16 2023

@author: josho
"""

from prettytable import PrettyTable
iteraciones=[]
def horner(coef_1, x0):
    n=len(coef_1)
        #Condicionales
    if n<2:
        print("Error: El grado del polinomio debe ser al menos cuadrático.")
        return 0
        
    p=coef_1[0]
    q=p
    coef_2=[]
    coef_2.append(q)
    l=0
    error_rel=paro + 1
    for i in range(1, n):
        p=p*x0 + coef_1[i]
        coef_2.append(p)
    coef_2=coef_2[:n-1]
    #ciclo para aproximar a la raíz
    while error_rel>paro:
        p=coef_1[0]
        for i in range(1, len(coef_1)):
            p=p*x0 + coef_1[i]
        q=coef_1[0]
        for j in range(1, len(coef_2)):
            q=q*x0 + coef_2[j]
        if p==0:
            print(f"\nEl valor inicial {x0}, es la raíz de los coeficientes de la función.")
            return p, q, None, None, None, None
            break
        x1=(x0-(p/q))
        error_abs=abs(x1-x0)
        error_rel=(error_abs/abs(x1))
        x0=x1
        l+=1
        iteraciones.append([x1, error_abs, error_rel, l])
        if l>1000:
            break
    return p, q, x1, error_rel, error_abs, l
#Ingreso de la función
grado=int(input("Ingrese el grado de la función polinómica: "))
coef_1=[]
x0=float(input("Ingrese el valor inicial 'x0' para realizar la función polinomial: "))

for i in range(grado):
    coeficiente=float(input(f"Ingrese el coeficiente para x^{grado - i}: "))
    coef_1.append(coeficiente)

#Ingreso de la constante de la función
coeficiente=float(input("Ingrese el coeficiente para Constante C: "))
const=coeficiente
#Valor de la constante en una variable numérica independiente al array
coef_1.append(coeficiente)
#solicitud criterio de paro
paro=int(input("Ingrese la cantidad de decimales para el criterio de paro: "))
paro_1=paro
paro=10**(-paro)
#Llamado de la función
error_rel=paro+1
p, q, x1, error_rel, error_abs, l=horner(coef_1, x0)
#Crear la tabla con encabezados
tabla=PrettyTable()
tabla.field_names=["Iteración", "Raíz", "Error Absoluto", "Error Relativo"]
#Llenar la tabla
for i, (raiz, error_rel, error_abs, iteraciones) in enumerate(iteraciones, start=1):
    tabla.add_row([i, raiz, error_rel, error_abs])
if x1 and error_rel and error_abs and l is None:
    print(f"\nEl valor inicial [{x0}], es una raíz de los coeficientes de la función.")
if p and q and x1 is not None:
    #Mostrar tabla
    print (tabla)
    
    print ("En la iteración", l,", el valor", f"{x1:.{int(paro_1)}f}", "es una buena aproximación a la raíz.")
    
