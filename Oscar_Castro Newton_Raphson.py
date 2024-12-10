"""
Nombre: Newton Raphson
Fecha Inicio: 21/09/2021
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

"""
import matplotlib.pyplot as plt
import sympy as sy
import numpy as np
import math as m

def F(ecuacion,x):
     return eval(ecuacion)

def trunc(cf,num):
     n = str(num)

     if num < 0 and num - int(num) == 0:
          num = str(n[:cf+1])
     elif num < 0 and num - int(num) != 0:
          num = str(n[:cf+2])
     elif num - int(num) != 0:
          num = str(n[:cf+1])
     elif num - int(num) == 0:
          num = str(n[:cf])
          
     return float(num)

def recta(ecuacion,a):
     y = ecuacion.subs(x,a)
     der = ecuacion.diff(x)
     
     m = der.subs(x,a)
     b  = (-1*m*a)+y
     if b > 0:
          m = str(m)
          b = str(b)
          funr = m+"*x+"+b
     elif b < 0:
          m = str(m)
          b = str(b)
          funr = m+"*x"+b
     elif b == 0:
          m = str(m)
          b = str(b)
          funr = m+"*x"
          
     return sy.parse_expr(funr)

print("""
                                        NEWTON RAPHSON
      INSTRUCCIONES:
      Este programa calcula la raíz de un polinomio usando el método de Newton Raphson.
      Para calcular la raíz debes colocar un punto que sea muy cercano a la raíz, este
      punto no debe estar muy lejos de la raíz, ya que puede que no converga por esta
      razón.

      ECUACION: Para colocar la ecuación f(x) solo se puede usar de variable la letra " x ",
                para colocar un exponente debes colocar un (**) y para una multiplicación debes
                colocar (*).
                Ejemplo:
                
                ╠═══  x**3-2*x**2-1  ═══╣
                
                Tiene una raiz cerca de ╠═ x = 1 ═╣ """)

x = sy.symbols("x")

e = np.e

p = "si"
while p == "s" or p == "S" or p == "si" or p == "SI" or p == "Si" or p == "sI":
     
     i = "no"
     while i == "n" or i == "N" or i == "no" or i == "NO" or i == "No" or i == "nO":
          try:
               ecuacion = sy.parse_expr(input("\n\t Digite su ecuacion f(x):"))
               ecuacion.subs(x,1)
               i = "si"
          except:
               print("\n\t┌──────────────────────────────────────────┐")
               print("  \t│  Error:  Colocaste mal la ecuacion f(x)  │")
               print("  \t└──────────────────────────────────────────┘")
               i = str(input("\t Deseas salir [si/no]"))
          
     c = np.linspace(-100,100,10001)
     
     d = []
     g = []
     for i in c:
          e = ecuacion.subs(x,i)
          d.append(e)
          g.append(0)
          
     inter = "si"
     while inter == "s" or inter == "S" or inter == "si" or inter == "SI" or inter == "Si" or inter == "sI":
          
          a = float(input("\n\t Coloca un punto:"))
          
          ec = list(str(ecuacion))
          
          for j in range(len(ec)):
               if ec[j] == "x" and ec[j+1] == "*":
                    h = []
                    i = 0
                    v = recta(ecuacion,a)  
                    for i in c:
                         u = v.subs(x,i)
                         h.append(u)
                    z = 1
                    break
               elif ec[j] == "x" and ec[j+1] != "*":
                    z = 0
                    break
          
          plt.style.use("dark_background") 
          fig, ax = plt.subplots()
          ax.grid()
          ax.set_title("Newton Raphson")
          ax.plot(c,g,color="red")
          ax.plot(g,c,color="red")
          ax.plot(c,d,color="blue")#,label=f"$f(x) = {ecuacion}$")
          if z == 1:
               ax.plot(c,h,color="orange",label=f"$r(x) = {v}$")
               ax.plot(a,v.subs(x,a),marker ="o",color="white")
          ax.plot(a,0,marker ="o",color="white")
          if a >= 0:
               ax.set_xlim((-1*a)-5,a+5)
          elif a < 0:
               ax.set_xlim((a-5,(-1*a)+5))
          ax.set_ylim(-10,10)
          ax.legend()
          plt.show()
          
          inter = str(input("- Observa la gráfica - ¿Deseas cambiar el punto? [si/no] »» "))
     
     cf = int(input("\n\t Cifras significativas:"))
     tol = 10**(-1*(cf))
     
     plt.style.use("dark_background") 
     fig, ax = plt.subplots()
     ax.grid()
     ax.set_title("Newton Raphson")
     ax.plot(c,g,color="red")
     ax.plot(g,c,color="red")
     ax.plot(c,d,color="blue",label=f"$f(x) = {ecuacion}$")
     if a >= 0:
          ax.set_xlim((-1*a)-5,a+5)
     elif a < 0:
          ax.set_xlim((a-5,(-1*a)+5))
     ax.set_ylim(-10,10)
     ax.legend()
     print("\n")
     
     i = 0
     l = 0
     r = 0
     e1 = 0
     s = 0
     while i <= 1000:
          
          if i == 0:
               print("{:^86}".format("╔════════════════════════════════════════════════════════════════════════════════════╗"))
               print("{:^1}{:^84}{:^1}".format("║",f"{ecuacion}","║"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("╠","═══════════","╦","════════════════════════","╦","═══════════════","╦","═══════════════","╦","═══════════════","╣"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("║","Iteracion","║","Raiz","║","F(x)","║","Error abs","║","Error rel","║"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("╠","═══════════","╬","════════════════════════","╬","═══════════════","╬","═══════════════","╬","═══════════════","╣"))

          der = ecuacion.diff(x)
          fder = der.subs(x,a)
          fa = ecuacion.subs(x,a)
          if fder == 0 and round(fa,cf) != 0:
               print("{:^1}{:^13}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("╚","═════════════","╩","════════════════════════","╩","═══════════════","╩","═══════════════","╩","═══════════════","╝"))
               print("\n\t┌───────────────────────────────────────────────────────────────┐")
               print("  \t│  Error: Se encontró con un máximo o un mínimo de la función,  │")
               print("  \t│         coloca un punto aún mas cerca de la raíz.             │")
               print("  \t│         AYUDATE DE LA GRAFICA                                 │")
               print("  \t└───────────────────────────────────────────────────────────────┘")
               ax.set_ylim(-10,10)
               ax.plot(a,recta(ecuacion,a),marker ="o",color="white")
               plt.show()
               l = 1
               break
          
          cr = round(r,cf)
          
          if fder != 0:
               r = a - (fa/fder)
          
          erabs = 0
          errel = 0
          if i >= 1 and r == 0:
               erabs = abs(e1-r)
               errel = abs(e1-r)/abs(tol)
          elif i >= 1 and r != 0:
               erabs = abs(e1-r)
               errel = abs(e1-r)/abs(r)
          
               
          if i >= 0:
               e1 = abs(r)
          
          if i >= 1:
               if round(errel,cf) <= tol:
                    s = 1
                    break
               elif round(erabs,cf) <= tol:
                    s = 2
                    break
               elif cr == round(r,cf):
                    break
               
          i += 1
          
          if i <= 100:
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("║",i,"║",str(r),"║",trunc(10,round(abs(float(fa)),10)),"║",trunc(10,round(float(erabs),10)),"║",trunc(10,round(float(errel),10)),"║"))
          elif i == 101:
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("╠","═══════════","╬","════════════════════════","╬","═══════════════","╬","═══════════════","╬","═══════════════","╣"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("║",":  :  :","║",":  :  :    :  :  :","║",":   :   :","║",":   :   :","║",":   :   :","║"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("╠","═══════════","╬","════════════════════════","╬","═══════════════","╬","═══════════════","╬","═══════════════","╣"))
          elif i == 1000:
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("║",i,"║",str(r),"║",trunc(10,round(abs(float(fa)),10)),"║",trunc(10,round(float(erabs),10)),"║",trunc(10,round(float(errel),10)),"║"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("╚","═══════════","╩","════════════════════════","╩","═══════════════","╩","═══════════════","╩","═══════════════","╝"))
               print("   ┌────────────────────────────────────────────────────────────────────────────────┐")
               print("   │  Error: Llego al número máximo de iteraciones (1000), no se encontro la raíz.  │")
               print("   │                                                                                │")
               print("   │      Caso 1: El punto esta muy lejos de la raiz, coloca un punto más cerca de  │")
               print("   │              la raíz.                                                          │")
               print("   │              AYUDATE DE LA GRAFICA                                             │")
               print("   │                                                                                │")
               print("   │      Caso 2: No tiene raíces reales.                                           │")
               print("   └────────────────────────────────────────────────────────────────────────────────┘")
               l = 1
               plt.show()
               break
          
          if round(fa,cf) == 0:
               break
          
          a = r
                    
     if l == 0:
          print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("╠","═══════════","╩","════════════════════════","╩","═══════════════","╩","═══════════════","╩","═══════════════","╣"))
          print("{:^1}{:^32}{:^32}{:^20}{:^1}".format("║","Raiz aproximada ≈",trunc(cf,round(r,cf))," ","║"))
          print("{:^86}".format("╚════════════════════════════════════════════════════════════════════════════════════╝"))
          if s == 1:
               print("{:^85}".format("╔════════════════════════════════════════════════════════════════════════════════════╗"))
               print("{:^1}{:^84}{:^1}".format("║","Paro por error relativo","║"))
               print("{:^85}".format("╚════════════════════════════════════════════════════════════════════════════════════╝"))
          elif s == 1:
               print("{:^85}".format("╔════════════════════════════════════════════════════════════════════════════════════╗"))
               print("{:^1}{:^84}{:^1}".format("║","Paro por error absoluto","║"))
               print("{:^85}".format("╚════════════════════════════════════════════════════════════════════════════════════╝"))
          if r >= 0:
               ax.set_xlim(round(float(-1*r),cf)-1,round(float(r),cf)+1)
          elif r < 0:
               ax.set_xlim(round(float(r),cf)-1,round(float(-1*r),cf)+1)
          ax.set_ylim(-10,10)
          ax.plot(round(r,cf),0,marker ="o",color="white")
          plt.show()
     p = str(input("\n\t¿Deseas buscar la raiz de otro polinomio? [si/no] »» "))