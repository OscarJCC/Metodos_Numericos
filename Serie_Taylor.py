"""
Nombre: Convertido de sistema Decimal a Binorio
Fecha Inicio: 05/09/2021
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

∑_(n = 0)^(inf) (f^n(a)/n!)(x-a)^n

f(a) + (f´(a)/1!)(x - a) + (f´´(a)/2!)(x - a)^2 + (f´´´(a)/3!)(x - a)^3 + ··· + (f^n(a)/n!)(x - a)^n

"""


import sympy as sy
import numpy as np
import matplotlib.pyplot as plt


x = sy.symbols("x")

inter = int(input("Numero de interaciones:"))
a = float(input("Numero en el que se quiere generar la funcion:"))
f = sy.cos(x)
print(type(f))
print("Funcion = ", f)

n = 1
suma = f.subs(x,a)
y = []
while n <= inter:
     der = sy.diff(f,x)
     b = der.subs(x,a)
     y.append(b)
     print("Derivada",n,"=",b)
     f = der
     suma += (b/sy.factorial(n))*(x-a)**n
     if f == 0:
          break
     else:
          n += 1
print(y)
print(suma)
print(suma.subs(x,0.001))

c = np.linspace(-20,20,1001)
d = np.array([])
for i in c:
     e = suma.subs(x,i)
     d = np.append(d,e)
g = np.cos(c)
fig, ax = plt.subplots()
ax.grid()
ax.set_title("Funciones de taylor")
ax.plot(c,g,color="red",label=r"$\cos(x)$")
ax.plot(c,d,color="blue",label=r"$\cos(x)$")
ax.set_xlabel("Eje x")
ax.set_ylabel("Eje y")
ax.set_xlim(-15,15)
ax.set_ylim(-2,2)
ax.legend()
plt.show()