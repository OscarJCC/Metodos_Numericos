"""
Nombre: Secante
Fecha Inicio: 14/10/2021
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

def fin():
     print("""
           ╔═══════════╗  ╔═══════════╗  ╔════════╗       ╔════╗
           ║           ║  ║           ║  ║        ╚╗      ║    ║
           ║     ╔═════╝  ╚══╗     ╔══╝  ║     ╔╗  ╚╗     ║    ║
           ║     ║           ║     ║     ║     ║╚╗  ╚╗    ║    ║
           ║     ╚══╗        ║     ║     ║     ║ ╚╗  ╚╗   ║    ║
           ║        ║        ║     ║     ║     ║  ╚╗  ╚╗  ║    ║
           ║     ╔══╝        ║     ║     ║     ║   ╚╗  ╚╗ ║    ║
           ║     ║           ║     ║     ║     ║    ╚╗  ╚╗║    ║
           ║     ║        ╔══╝     ╚══╗  ║     ║     ╚╗  ╚╝    ║
           ║     ║        ║           ║  ║     ║      ╚╗       ║
           ╚═════╝        ╚═══════════╝  ╚═════╝       ╚═══════╝
           """)

print("""
                                        SECANTE
      INSTRUCCIONES:
      Este programa calcula la raíz de un polinomio usando el método de la Secante.
      Para calcular la raíz debes colocar un intervalo [a,b] que sea muy cercano a la raíz.
      Debes cuidar que al evaluar en la función en f(a) sea diferente a f(b), ya que si esto 
      se cumple la secante nunca cruzara el eje x y no se podrá realizar el método. 
      Tambien debes cuidar que el intervalo no este muy lejos de la raíz, ya que puede 
      que no converga por esta razón.

      ECUACION: Para colocar la ecuación f(x) solo se puede usar de variable la letra " x ",
                para colocar un exponente debes colocar un (**) y para una multiplicación debes
                colocar (*).
                Ejemplo:
                
                ╠═══  x**3-2*x**2-1  ═══╣
                
                Tiene una raiz entre ╠═ x = 1 ═╣ y ╠═ x = 3 ═╣ """)

p = "si"
while p == "s" or p == "S" or p == "si" or p == "SI" or p == "Si" or p == "sI":
     
     i = "si"
     while i == "s" or i == "S" or i == "si" or i == "SI" or i == "Si" or i == "sI" and i != "n" and i != "N" and i != "no" and i != "NO" and i != "No" and i != "nO":
          try:
               ecuacion = str(input("\n\t Digite su ecuacion f(x):"))
               F(ecuacion,1)
               i = "no"
          except:
               print("\n\t┌───────────────────────────────────────────┐")
               print("  \t│  Error:  Colocaste mal la ecuación f(x),  │")
               print("  \t│          sigue las instrucciones.         │")
               print("  \t│                                           │")
               print("  \t│          Colocaste una función que no es  │")
               print("  \t│          un polinomio.                    │")
               print("  \t└───────────────────────────────────────────┘")
               i = str(input("\n\t¿Deseas continuar? [si/no] »» "))
               if i == "n" or i == "N" or i == "no" or i == "NO" or i == "No" or i == "nO":
                    fin()
                    exit(1)
               
     c = np.linspace(-100,100,1001)
     d = []
     g = []
     for i in c:
          try:
               e = F(ecuacion,i)
          except:
               fin()
               exit(1)
          d.append(e)
          g.append(0)
     
     inter = "si"
     while inter == "s" or inter == "S" or inter == "si" or inter == "SI" or inter == "Si" or inter == "sI":
          
          i = "si"
          while i == "s" or i == "S" or i == "si" or i == "SI" or i == "Si" or i == "sI" and i != "n" and i != "N" and i != "no" and i != "NO" and i != "No" and i != "nO":
               try:
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
                         i = "no"    
               except:
                    print("\n\t┌─────────────────────────────────────────────────────────┐")
                    print("  \t│  Error:  Colocaste alguna letra o símbolo en alguno de  │")
                    print("  \t│          los límite, debes darles un valor numérico.    │")
                    print("  \t└─────────────────────────────────────────────────────────┘")
                    i = str(input("\n\t¿Deseas continuar? [si/no] »» "))
                    if i == "n" or i == "N" or i == "no" or i == "NO" or i == "No" or i == "nO":
                         fin()
                         exit(1)
          
          h = []
          try:
               v = recta(ecuacion,a,b)
          except:
               fin()
               exit(1)
          for i in c:
               u = F(v,i)
               h.append(u)
          plt.style.use("dark_background") 
          fig, ax = plt.subplots()
          ax.grid()
          ax.set_title("Secante")
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
          print("\n")
          inter = str(input("- Observa la gráfica - ¿Deseas cambiar el intervalo? [si/no] »» "))
     
     i = "si"
     while i == "s" or i == "S" or i == "si" or i == "SI" or i == "Si" or i == "sI" and i != "n" and i != "N" and i != "no" and i != "NO" and i != "No" and i != "nO":
          try:
               cf = int(input("\n\t Cifras significativas:"))
               i = "no" 
          except:
               print("\n\t┌─────────────────────────────────────────────────────┐")
               print("  \t│  Error:  Colocaste alguna letra o símbolo para las  │")
               print("  \t│          cifras significativa, debes darles un      │")
               print("  \t│          valor numérico.                            │")
               print("  \t└─────────────────────────────────────────────────────┘")
               i = str(input("\n\t¿Deseas continuar? [si/no] »» "))
               if i == "n" or i == "N" or i == "no" or i == "NO" or i == "No" or i == "nO":
                    fin()
                    exit(1)
     try:
          tol = 10**(-1*(cf))
     except:
          fin()
          exit(1)
          
     plt.style.use("dark_background") 
     fig, ax = plt.subplots()
     ax.grid()
     ax.set_title("Secante")
     ax.plot(c,g,color="red")
     ax.plot(g,c,color="red")
     ax.plot(c,d,color="blue",label=f"$f(x) = {ecuacion}$")
     ax.set_xlim(a,b)
     ax.set_ylim(-10,10)
     ax.legend()
     
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

          fa = F(ecuacion,a)
          fb = F(ecuacion,b)
          
          if fb == fa and round(fa,cf) != 0:
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("╚","═══════════","╩","════════════════════════","╩","═══════════════","╩","═══════════════","╩","═══════════════","╝"))
               print("\n\t┌────────────────────────────────────────────────────────────────┐")
               print("  \t│  Error:                                                        │")
               print("  \t│     Caso 1: Al evaluar la funcion en el intervalo f(a) = f(b)  │")
               print("  \t│             por lo que la recta secante nunca cruza por el     │")
               print("  \t│             eje x, coloca otro intervalo diferente.            │")
               print("  \t│             AYUDATE DE LA GRAFICA                              │")
               print("  \t│                                                                │")
               print("  \t│      Caso 2: La secante no pudo coincidir con la raíz, coloca  │")
               print("  \t│              otro intervalo diferente.                         │")
               print("  \t│              AYUDATE DE LA GRAFICA                             │")
               print("  \t└────────────────────────────────────────────────────────────────┘")
               ax.plot(c,h,color="orange",label=f"$r(x) = {v}$")
               ax.plot(c,d,color="blue",label=f"$f(x) = {ecuacion}$")
               ax.plot(a,0,marker ="o",color="white")
               ax.plot(b,0,marker ="o",color="white")
               ax.plot(a,F(ecuacion,a),marker ="o",color="white")
               ax.plot(b,F(ecuacion,b),marker ="o",color="white")
               ax.set_xlim(a-.5,b+.5)
               plt.show()
               l = 1
               break
          
          if fb != fa:
               r = a - ((fa*(b-a))/(fb-fa))
          
          fr = F(ecuacion,r)
          
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
               
          i += 1
          
          if i <= 100:
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("║",i,"║",str(r),"║",trunc(10,round(abs(float(fa)),10)),"║",trunc(10,round(float(erabs),10)),"║",trunc(10,round(float(errel),10)),"║"))
          elif i == 101:
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("╠","═══════════","╬","════════════════════════","╬","═══════════════","╬","═══════════════","╬","═══════════════","╣"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("║",":  :  :","║",":  :  :    :  :  :","║",":   :   :","║",":   :   :","║",":   :   :","║"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("╠","═══════════","╬","════════════════════════","╬","═══════════════","╬","═══════════════","╬","═══════════════","╣"))
          elif i == 200:
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("║",i,"║",str(r),"║",trunc(10,round(abs(float(fa)),10)),"║",trunc(10,round(float(erabs),10)),"║",trunc(10,round(float(errel),10)),"║"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("╚","═══════════","╩","════════════════════════","╩","═══════════════","╩","═══════════════","╩","═══════════════","╝"))
               print("   ┌────────────────────────────────────────────────────────────────────────────────┐")
               print("   │  Error: Llego al número máximo de iteraciones (200), no se encontro la raíz.   │")
               print("   │                                                                                │")
               print("   │      Caso 1: El intervalo esta muy lejos de la raiz, coloca un intervalo más   │")
               print("   │              cercano.                                                          │")
               print("   │              AYUDATE DE LA GRAFICA                                             │")
               print("   │                                                                                │")
               print("   │      Caso 2: La secante no pudo coincidir con la raiz, coloca otro intervalo   │")
               print("   │              diferente.                                                        │")
               print("   │              AYUDATE DE LA GRAFICA                                             │")
               print("   │                                                                                │")
               print("   │      Caso 3: No tiene raíces reales.                                           │")
               print("   └────────────────────────────────────────────────────────────────────────────────┘")
               l = 1
               ax.set_xlim(round(r,cf)-1,round(r,cf)+1)
               ax.set_ylim(-10,10)
               ax.plot(round(r,cf),0,marker ="o",color="white")
               plt.show()
               break
          
          if round(fr,cf) == 0:
               break
          
          if fa < 0 and fb < 0:
               if fa < fb:
                    a = r
               elif fb < fa:
                    b = r
          elif fa > 0 and fb > 0:
               if fa < fb:
                    b = r
               elif fb < fa:
                    a = r
          elif fa < 0 and fb > 0:
               a = r
          elif fa > 0 and fb < 0:
               b = r

                    
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
               
          ax.set_xlim(round(r,cf)-1,round(r,cf)+1)
          ax.set_ylim(-10,10)
          ax.plot(round(r,cf),0,marker ="o",color="white")
          plt.show()
          
     p = str(input("\n\t¿Deseas buscar la raiz de otro polinomio? [si/no] »» "))
     
fin()