"""
Nombre: Regla_falsa
Fecha Inicio: 13/09/2021
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

"""
import matplotlib.pyplot as plt
import numpy as np

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

def recta(ecux,a,b):
     ecuya = F(ecux,a)
     ecuyb = F(ecux,b)
     
     m = ((ecuyb)-(ecuya))/((b)-(a))
     b  = (-1*m*a)+ecuya
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
     
     return funr

print("""
                                        REGLA FALSA
      INSTRUCCIONES:
      Este programa calcula la raíz de un polinomio usando el método de Regla falsa.
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
               a = float(input("\n\t Límite inferior (a):"))
     
               b = float(input("\t Límite superior (b):"))

               if a > b:
                    print("\n\t┌─────────────────────────────────────────────────────┐")
                    print("  \t│  Error:  Límite inferior es mayor que el superior.  │")
                    print("  \t└─────────────────────────────────────────────────────┘")
               elif a == b:
                    print("\n\t┌───────────────────────────────────────────────────┐")
                    print("  \t│  Error:  Límite inferior y superior son iguales.  │")
                    print("  \t└───────────────────────────────────────────────────┘")
               else:
                    i = 1
          
          h = []
          v = recta(ecuacion,a,b)
          for i in c:
               u = F(v,i)
               h.append(u)
          
          plt.style.use("dark_background") 
          fig, ax = plt.subplots()
          ax.grid()
          ax.set_title("Regla falsa")
          ax.plot(c,g,color="red")
          ax.plot(g,c,color="red")
          ax.plot(c,h,color="orange",label=f"$r(x) = {v}$")
          ax.plot(c,d,color="blue",label=f"$f(x) = {ecuacion}$")
          ax.plot(a,0,marker ="o",color="white")
          ax.plot(b,0,marker ="o",color="white")
          ax.plot(a,F(ecuacion,a),marker ="o",color="white")
          ax.plot(b,F(ecuacion,b),marker ="o",color="white")
          ax.set_xlim(a-.5,b+.5)
          ax.set_ylim(-10,10)
          ax.legend()
          plt.show()
          
          inter = str(input("- Observa la gráfica - ¿Deseas cambiar el intervalo? [si/no] »» "))
     
     cf = int(input("\n\t Cifras significativas:"))
     tol = 10**(-1*(cf))
     
     plt.style.use("dark_background") 
     fig, ax = plt.subplots()
     ax.grid()
     ax.set_title("Regla falsa")
     ax.plot(c,g,color="red")
     ax.plot(g,c,color="red")
     ax.plot(c,d,color="blue",label=f"$f(x) = {ecuacion}$")
     ax.set_xlim(a,b)
     ax.set_ylim(-10,10)
     ax.legend()
     
     i = 0
     l = 0
     c = 0
     e1 = 0
     s = 0
     while i <= 1000:
          
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
               print("  \t│              este método de Regla falsa.                                │")
               print("  \t│              OBSERVA LA GRÁFICA                                         │")
               print("  \t└─────────────────────────────────────────────────────────────────────────┘")
               l = 1
               plt.show()
               break
          
          if i == 0 and l == 0:
               print("{:^86}".format("╔════════════════════════════════════════════════════════════════════════════════════╗"))
               print("{:^1}{:^84}{:^1}".format("║",ecuacion,"║"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("╠","═══════════","╦","════════════════════════","╦","═══════════════","╦","═══════════════","╦","═══════════════","╣"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("║","Iteracion","║","Raiz","║","F(x)","║","Error abs","║","Error rel","║"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("╠","═══════════","╬","════════════════════════","╬","═══════════════","╬","═══════════════","╬","═══════════════","╣"))
          
          kc = round(c,cf)
          
          c = b-((fb)*(b-a))/((fb-fa))
          
          fc = (F(ecuacion,c))
          
          erabs = 0
          errel = 0
          if i >= 1 and c == 0:
               erabs = abs(e1-c)
               errel = abs(e1-c)/abs(tol)
          elif i >= 1 and c != 0:
               erabs = abs(e1-c)
               errel = abs(e1-c)/abs(c)
     
          if i >= 0:
               e1 = abs(c)

          if fc*fa > 0:
               a = c
          elif fc*fb > 0:
               b = c

          if i >= 1:
               if round(errel,cf) <= tol:
                    s = 1
                    break
               elif round(erabs,cf) <= tol:
                    s = 2
                    break
               elif kc == round(c,cf):
                break
          
          print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("║",i+1,"║",c,"║",trunc(10,round(abs(float(fc)),10)),"║",trunc(10,round(float(erabs),10)),"║",trunc(10,round(float(errel),10)),"║"))
          
          if round(fc,cf) == 0:
               break
          
          i += 1
     
     if l == 0:
          print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("╠","═══════════","╩","════════════════════════","╩","═══════════════","╩","═══════════════","╩","═══════════════","╣"))
          print("{:^1}{:^32}{:^32}{:^20}{:^1}".format("║","Raiz aproximada ≈",trunc(cf,round(c,cf))," ","║"))
          print("{:^86}".format("╚════════════════════════════════════════════════════════════════════════════════════╝"))
          if s == 1:
               print("{:^86}".format("╔════════════════════════════════════════════════════════════════════════════════════╗"))
               print("{:^1}{:^84}{:^1}".format("║","Paro por error relativo","║"))
               print("{:^86}".format("╚════════════════════════════════════════════════════════════════════════════════════╝"))
          elif s == 1:
               print("{:^86}".format("╔════════════════════════════════════════════════════════════════════════════════════╗"))
               print("{:^1}{:^84}{:^1}".format("║","Paro por error absoluto","║"))
               print("{:^86}".format("╚════════════════════════════════════════════════════════════════════════════════════╝"))          
          ax.set_xlim(round(c,cf)-1,round(c,cf)+1)
          ax.set_ylim(-10,10)
          ax.plot(round(c,cf),0,marker ="o",color="white")
          plt.show()
     p = str(input("\n\t¿Deseas buscar la raiz de otro polinomio? [si/no] »» "))