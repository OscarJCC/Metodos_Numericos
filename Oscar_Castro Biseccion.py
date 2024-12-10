"""
Nombre: Biseccion
Fecha Inicio: 06/09/2021
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

"""
import matplotlib.pyplot as plt
import numpy as np
import math

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

print("""
                                        BISECCIÓN
      INSTRUCCIONES:
      Este programa calcula la raíz de un polinomio usando el método de Bisección.
      Para calcular la raíz debes colocar un intervalo [a,b] en el que se encuentra la raíz,
      al evaluar el polinomio en los intervalos f(a) debe ser con signo opuesto a f(b) o f(b)
      debe ser con signo opuesto a f(a), si esto no ocurre este método no te servirá.
      Recuerda colocar el intervalo lo más cerca posible a la raíz que deseas calcular.

      ECUACIÓN: Para colocar la ecuación f(x) solo se puede usar de variable la letra " x ",
                para colocar un exponente debes colocar un (**) y para una multiplicación debes
                colocar (*).
                Ejemplo:      ╠═══  x**3-2*x**2-1  ═══╣
                Tiene una raiz entre ╠═ x = 1 ═╣ y ╠═ x = 3 ═╣ """)
p = "si"
while p == "s" or p == "S" or p == "si" or p == "SI" or p == "Si" or p == "sI":
     
     i = "no"
     while i == "n" or i == "N" or i == "no" or i == "NO" or i == "No" or i == "nO":
          ecuacion = str(input("\n\t Digite su ecuacion f(x):"))
          try:
               F(ecuacion,1)
               i = "si"
          except:
               print("\n\t┌──────────────────────────────────────────┐")
               print("  \t│  Error:  Colocaste mal la ecuación f(x)  │")
               print("  \t└──────────────────────────────────────────┘")
               i = str(input("\t Deseas salir [si/no]"))
          
     c = np.linspace(-100,100,1001)
    
     d = []
     g = []
     for i in c:
          e = F(ecuacion,i)
          d.append(e)
          g.append(0)
     
     inter = "si"
     while inter == "s" or inter == "S" or inter == "si" or inter == "SI" or inter == "Si" or inter == "sI":
          i = 0
          while i == 0:
               a = float(input("\n\t Limite inferior (a):"))
     
               b = float(input("\t Limite superior (b):"))

               if a > b:
                    print("\n\t┌─────────────────────────────────────────────────────┐")
                    print("  \t│  Error:  Limite inferior es mayor que el superior.  │")
                    print("  \t└─────────────────────────────────────────────────────┘")
               elif a == b:
                    print("\n\t┌───────────────────────────────────────────────────┐")
                    print("  \t│  Error:  Limite inferior y superior son iguales.  │")
                    print("  \t└───────────────────────────────────────────────────┘")
               else:
                    i = 1
          
          plt.style.use("dark_background") 
          fig, ax = plt.subplots()
          ax.grid()
          ax.set_title("Bisección")
          ax.plot(c,g,color="red")
          ax.plot(g,c,color="red")
          ax.plot(c,d,color="blue",label=f"$f(x) = {ecuacion}$")
          ax.plot(a,0,marker ="o",color="white")
          ax.plot(b,0,marker ="o",color="white")
          ax.set_xlim(a-.5,b+.5)
          ax.set_ylim(-10,10)
          ax.legend()
          plt.show()
          
          inter = str(input("- Observa la grafica - ¿Deseas cambiar el intervalo? [si/no] »» "))
     
     cf = int(input("\n\t Cifras significativas:"))
     tol = 10**(-1*(cf))
     n = int((math.log(b-a)-math.log(tol))/math.log(2))
     
     plt.style.use("dark_background") 
     fig, ax = plt.subplots()
     ax.grid()
     ax.set_title("Bisección")
     ax.plot(c,g,color="red")
     ax.plot(g,c,color="red")
     ax.plot(c,d,color="blue",label=f"$f(x) = {ecuacion}$")
     ax.set_xlim(a-.5,b+.5)
     ax.set_ylim(-10,10)
     ax.legend()
     
     i = 0
     l = 0
     xm = 0
     e1 = 0
     s = 0
     while i <= n:
          
          fa = F(ecuacion,a)
          fb = F(ecuacion,b)

          if fa*fb > 0:
               print("\n\t┌─────────────────────────────────────────────────────────────────────────┐")
               print("  \t│  Error:                                                                 │")
               print("  \t│      Caso 1: No tiene raíces reales o no hay raíces en este intervalo.  │")
               print("  \t│                                                                         │")
               print("  \t│      Caso 2: Hay más de 2 raíces en el intervalo. Coloca un intervalo   │")
               print("  \t│              más próximo a la raíz que quieres calcular.                │")
               print("  \t│              AYUDATE DE LA GRÁFICA                                      │")
               print("  \t│                                                                         │")
               print("  \t│      Caso 3: Si observas la gráfica al evaluar la ecuación en los       │")
               print("  \t│              limites [a,b] tenemos que f(a) es del mismo signo que      │")
               print("  \t│              f(b), por lo que para esta ecuación f(x) no funciona       │")
               print("  \t│              este metodo de Bisección.                                  │")
               print("  \t│              OBSERVA LA GRAFICA                                         │")
               print("  \t└─────────────────────────────────────────────────────────────────────────┘")
               l = 1
               ax.plot(a,0,marker ="o",color="white")
               ax.plot(b,0,marker ="o",color="white")
               plt.show()
               break
          
          if i == 0 and l == 0:
               print("{:^86}".format("╔════════════════════════════════════════════════════════════════════════════════════╗"))
               print("{:^1}{:^84}{:^1}".format("║",ecuacion,"║"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("╠","═══════════","╦","════════════════════════","╦","═══════════════","╦","═══════════════","╦","═══════════════","╣"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("║","Iteración","║","Raiz","║","F(x)","║","Error abs","║","Error rel","║"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("╠","═══════════","╬","════════════════════════","╬","═══════════════","╬","═══════════════","╬","═══════════════","╣"))
          
          kxm = round(xm,cf)
          
          if a == -1*b or b == -1*a:
               xm = round((tol)/2,cf-1)
          else:
               xm = b+((a-b)/2)
          
          fxm = F(ecuacion,xm)

          erabs = 0
          errel = 0
          if i >= 1:
               erabs = abs(e1-xm)
               errel = abs(e1-xm)/abs(xm)
          
          erabs = 0
          errel = 0
          if i >= 1 and xm == 0:
               erabs = abs(e1-xm)
               errel = abs(e1-xm)/abs(tol)
          elif i >= 1 and xm != 0:
               erabs = abs(e1-xm)
               errel = abs(e1-xm)/abs(xm)
     
          if i >= 0:
               e1 = abs(xm)

          if fxm*fa > 0:
               a = xm
          elif fxm*fb > 0:
               b = xm

          if i >= 1:
               if round(errel,cf) <= tol:
                    s = 1
                    break
               elif round(erabs,cf) <= tol:
                    s = 2
                    break
               elif kxm == round(xm,cf):
                    break
          
          print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("║",i+1,"║",xm,"║",trunc(10,round(abs(float(fxm)),10)),"║",trunc(10,round(float(erabs),10)),"║",trunc(10,round(float(errel),10)),"║"))
          
          if round(fxm,cf) == 0:
               s = 3
               break
               
          i += 1
     
     if l == 0:
          print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("╠","═══════════","╩","════════════════════════","╩","═══════════════","╩","═══════════════","╩","═══════════════","╣"))
          print("{:^1}{:^32}{:^32}{:^20}{:^1}".format("║","Raiz aproximada ≈",trunc(cf,round(xm,cf))," ","║"))
          print("{:^86}".format("╚════════════════════════════════════════════════════════════════════════════════════╝"))
          if s == 0:
               print("{:^85}".format("╔════════════════════════════════════════════════════════════════════════════════════╗"))
               print("{:^1}{:^84}{:^1}".format("║",f"Paro por formula a {n} iteraciones","║"))
               print("{:^85}".format("╚════════════════════════════════════════════════════════════════════════════════════╝"))
          elif s == 1:
               print("{:^85}".format("╔════════════════════════════════════════════════════════════════════════════════════╗"))
               print("{:^1}{:^84}{:^1}".format("║","Paro por error relativo","║"))
               print("{:^85}".format("╚════════════════════════════════════════════════════════════════════════════════════╝"))
          elif s == 1:
               print("{:^85}".format("╔════════════════════════════════════════════════════════════════════════════════════╗"))
               print("{:^1}{:^84}{:^1}".format("║","Paro por error absoluto","║"))
               print("{:^85}".format("╚════════════════════════════════════════════════════════════════════════════════════╝"))
          ax.set_xlim(round(xm,cf)-1,round(xm,cf)+1)
          ax.set_ylim(-10,10)
          ax.plot(round(xm,cf),0,marker ="o",color="white")
          plt.show()
     p = str(input("\n\t¿Deseas buscar la raiz de otro polinomio? [si/no] »» "))