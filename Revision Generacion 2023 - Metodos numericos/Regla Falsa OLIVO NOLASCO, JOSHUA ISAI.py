# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 10:11:45 2023

@author: josho
"""

from math import cos, sin

#Creacion de un menu para la seleccion de la funcion a utilizar
print("Menú de opciones.")
print("1. Cos(x)")
print("2. Sin(x)")
print("3. Función polinómica")
menu=int(input("Seleccione una opción: "))
orden=[]
while menu<0 and menu>4:
    menu=int(input("Seleccione correctamente una opción: "))
    
    
def f(x):
    return eval(ecuacion);

def regla_falsa(a,b,tol):
    m1=a
    c=b
    k=0
    if (f(a)*f(b)>0):
        print("La función no tiene raices reales")
        return 0

    while (abs(m1 - c) > tol):
        m1=c
        c=b - ((f(b)*(b - a)) / (f(b) - f(a)))
        error=(abs(b - a)) / 2
        orden.append((c, (a, b), error))
        if (f(a)*f(c)<0):
            b=c
        if (f(c)*f(b)<0):
            a=c
        k+=1

    print("Nueva Aproximación:           | (a, b):             | Error Absoluto:         | Error Relativo:         ")
    for iteracion in orden:
        #trabajo de los errores abs y relativo
        valor_verdadero=iteracion[0]  
        valor_aproximado=c
        error_absoluto=abs(valor_verdadero - valor_aproximado)
        error_relativo=error_absoluto/abs(valor_verdadero)
        
        print(iteracion[0], " | [", iteracion[1][0], ",", iteracion[1][1], "] | ", error_absoluto, " | ", error_relativo)
    
    print("En x", k, " =", f"{c:.{int(paro)}f}", " es una buena aproximación.")
    
    
    
#Ingreso de los intervalos
a=float(input("Ingrese el valor minimo del intervalo de la función: "))
b=float(input("Ingrese el valor máximo del intervalo de la función: "))
#Solicitud de la condicion de paro
paro=float(input("Ingrese el numero de decimales a aproximar: 10**-"))
#Condicionales segun la opcion seleccionada
if menu==1:
    argumento=input("Ingrese el argumento: cos(")
    ecuacion=cos(argumento)
    regla_falsa(a, b, 10**(-paro))

if menu==2:
    argumento=input("Ingrese el argumento: sin(")
    ecuacion=sin(argumento)
    regla_falsa(a, b, 10**(-paro))
    
if menu==3:
    ecuacion=input("Ingrese la función polinómica a evaluar: ")
    regla_falsa(a, b, 10**(-paro))