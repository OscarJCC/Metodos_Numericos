# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 10:27:25 2023

@author: josho
"""

from math import cos, pi, sin

#Creacion de un menu para la seleccion de la funcion a utilizarP
print("Menú de opciones.")
print("1. Cos(x)")
print("2. Sin(x)")
print("3. Función polinómica")
menu=int(input("Seleccione una opción: "))

while menu<0 and menu>4:
    menu=int(input("Seleccione correctamente una opción: "))
    
    
def f(x):
    return eval(ecuacion);

def biseccion(a,b,tol):
    m1=a
    m=b
    k=0
    print("Punto medio:  |  (a, b):       |    Error:")
    if (f(a)*f(b)>0):
        print("La funcion no cambia de signo")
    
    while (abs(m1-m)>tol):
        m1=m
        m=a+((b-a)/2)
        error=(abs(b-a))/2
        print(m," | [",a,",",b,"] | ", error)
        if (f(a)*f(m)<0):
            b=m
        if (f(m)*f(b)<0):
            a=m
        k=k+1
        
    print("En x",k,"=",m," es una buena aproximación.")
    
    
#Ingreso de los intervalos
a=float(input("Ingrese el valor minimo del intervalo de la función: "))
b=float(input("Ingrese el valor máximo del intervalo de la función: "))
#Solicitud de la condicion de paro
paro=float(input("Ingrese el numero de decimales a aproximar: 10**-"))
#Condicionales segun la opcion seleccionada
if menu==1:
    argumento=input("Ingrese el argumento: cos(")
    ecuacion=cos(argumento)
    biseccion(a, b, 10**(-paro))

if menu==2:
    argumento=input("Ingrese el argumento: cos(")
    ecuacion=sin(argumento)
    biseccion(a, b, 10**(-paro))
    
if menu==3:
    ecuacion=input("Ingrese la función polinómica a evaluar: ")
    biseccion(a, b, 10**(-paro))
