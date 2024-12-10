"""
Nombre: Horner
Fecha Inicio: 07/10/2021
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

"""
import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
from sympy.polys.polytools import Poly

def F(ecuacion,x):
     return eval(str(ecuacion))

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

def ExpMayor(ecuacion):
     ecuacion = list(ecuacion)
     
     ecuacion.append("^") 
     
     grados = []
     i = 0
     while i <= len(ecuacion): 
          
          ecuacion.append("^")
          
          if ecuacion[i] == "^":
               break
          
          if i == 0 and ecuacion[i] != "x":
               j = ecuacion[i]
               k = 0
               while j != 1:
                    if j == str(k):
                         grados.append(0.0)
                         j = 1                  
                    elif (j == "+" or j == "-") and ecuacion[i+1] == str(k):
                         grados.append(0.0)
                         j = 1
                    elif (j == "+" or j == "-") and ecuacion[i+1] == "x":
                         j = 1  
                    else:
                         k += 1 
                    
          elif ecuacion[i] == "x" and ecuacion[i+1] == "*":
               j = i
               k = i + 3
               ecu1 = ""
               while j == i:
                    if ecuacion[k] == "+" or ecuacion[k] == "-":
                         j = i+2
                    elif ecuacion[k] != "-" and ecuacion[k] != "+" and ecuacion[k] != "x" and ecuacion[k] != "*" and ecuacion[k] != "^":
                         ecu1 += ecuacion[k]
                         k += 1
                         j = i
                    elif ecuacion[k] == "0":
                         ecu1 += ecuacion[k]
                         k += 1
                         j = i
                    else:
                         j = i+2
                    
               if ecu1 != "":
                    grados.append(float(ecu1))
                    i += 3
                    
          elif ecuacion[i] == "x" and ecuacion[i+1] != "*":
               grados.append(float(1))
               i += 1
                    
          elif ecuacion[i] != "-" and ecuacion[i] != "+" and ecuacion[i] != "*" and ecuacion[i] != "^":
               j = ecuacion[i]
               k = 0
               while j != 1 and k <= len(ecuacion):
                    if j == str(k) and ecuacion[i-1] != "-" and ecuacion[i-1] != "+" and ecuacion[i-1] != "*" and ecuacion[i-1] != "^":
                         j = 1
                    elif j == str(k) and ecuacion[i+1] != "*":
                         grados.append(0.0)
                         j = 1
                    elif (j == "+" or j == "-") and ecuacion[i+1] == str(k):
                         grados.append(0.0)
                         j = 1
                    elif ecuacion[i+1] == "-" or ecuacion[i+1] == "+" or ecuacion[i+1] == "x":
                         j = 1
                    else:
                         k += 1 
                    
          i += 1
          
     #Ordenamiento Decresiente
     for i in range(1,len(grados)):
          for j in range(len(grados)-i):
               if(grados[j] < grados[j+1]):
                    aux = grados[j]
                    grados[j] = grados[j+1]
                    grados[j+1] = aux
                         
     return grados

print("""
                                        HORNER
      INSTRUCCIONES:
      Este programa calcula la raíz de un polinomio usando el método de Horner.
      Para calcular la raíz debes colocar un punto cercano a la raíz, este punto 
      no debe estar en un maximo o un minimo de la funcion, ya que puede que no 
      el metodo se detiene cuando ocurre esto razón. Este método se basa en la 
      división sintética.

      ECUACION: Para colocar la ecuación f(x) solo se puede usar de variable la letra " x ",
                para colocar un exponente debes colocar un (**) y para una multiplicación debes
                colocar (*).
                Ejemplo:
                
                ╠═══  x**3-2*x**2-1  ═══╣
                
                Tiene una raiz cerca de ╠═ x = 1 ═╣ """)

x = sy.symbols("x")

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
          
     ecuP = Poly(ecuacion,x)

     cof = ecuP.coeffs()

     gr = int(ecuP.degree())

     listgr = ExpMayor(ecuacion)

     for i in range(len(cof)):
          cof[i] = float(cof[i])

     exp = [0.0]*(gr+1)

     for i in range(len(exp)+1):
          for j in range(len(listgr)):
               if gr-i == listgr[j]:
                    exp[i] = cof[j]
                    break
     
     c = np.linspace(-100,100,1001)

     d = []
     g = []
     for i in c:
          e = F(ecuacion,i)
          d.append(e)
          g.append(0)
     
     inter = "si"
     while inter == "s" or inter == "S" or inter == "si" or inter == "SI" or inter == "Si" or inter == "sI":
          
          a = float(input("\n\t Coloca un punto:"))
          
          plt.style.use("dark_background") 
          fig, ax = plt.subplots()
          ax.grid()
          ax.set_title("Horner")
          ax.plot(c,g,color="red")
          ax.plot(g,c,color="red")
          ax.plot(c,d,color="blue",label=f"$f(x) = {ecuacion}$")
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
     ax.set_title("Horner")
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
     
     j = 0
     l = 0
     r = 0
     e1 = 0
     s = 0
     while j <= 1000:
          
          if j == 0 and l == 0:
               print("{:^86}".format("╔════════════════════════════════════════════════════════════════════════════════════╗"))
               print("{:^1}{:^84}{:^1}".format("║",f"{ecuacion}","║"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("╠","═══════════","╦","════════════════════════","╦","═══════════════","╦","═══════════════","╦","═══════════════","╣"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("║","Iteracion","║","Raiz","║","F(x)","║","Error abs","║","Error rel","║"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("╠","═══════════","╬","════════════════════════","╬","═══════════════","╬","═══════════════","╬","═══════════════","╣"))
          
          qin = [exp[0]]
          p = 0
          for i in range(1,len(exp)):
               if i == 1:
                    pin = exp[i]+(exp[i-1]*a)
               else:
                    pin = exp[i]+(pin*a)
          
               qin.append(pin)
          
          p = qin[gr]

          qx = [exp[0]]
          q = 0
          for i in range(1,len(qin)-1):
               if i == 1:
                    pin = qin[i]+(qin[i-1]*a)
               else:
                    pin = qin[i]+(pin*a)
          
               qx.append(pin)

          q = qx[gr-1]

          if q != 0:
               r = a - (p/q)
          elif q == 0 and p != 0:
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("╚","═══════════","╩","════════════════════════","╩","═══════════════","╩","═══════════════","╩","═══════════════","╝"))
               print("\n\t┌───────────────────────────────────────────────────────────────┐")
               print("  \t│  Error: Se encontró con un máximo o un mínimo de la función,  │")
               print("  \t│         coloca un punto diferente.                            │")
               print("  \t│         AYUDATE DE LA GRAFICA                                 │")
               print("  \t└───────────────────────────────────────────────────────────────┘")
               ax.plot(c,d,color="blue",label=f"$f(x) = {ecuacion}$")
               ax.plot(a,0,marker ="o",color="white")
               ax.plot(a,F(ecuacion,a),marker ="o",color="white")
               if a >= 0:
                    ax.set_xlim((-1*a)-5,a+5)
               elif a < 0:
                    ax.set_xlim((a-5,(-1*a)+5))
               plt.show()
               l = 1
               break
          elif p == 0 and q == 0:
               r = a
               fr = F(ecuacion,r)
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("║",j+1,"║",str(r),"║",trunc(10,round(abs(float(fr)),10)),"║",0,"║",0,"║"))
               break
          
          fr = F(ecuacion,r)
          
          erabs = 0
          errel = 0
          if j >= 1 and r == 0:
               erabs = abs(e1-r)
               errel = abs(e1-r)/abs(tol)
          elif j >= 1 and r != 0:
               erabs = abs(e1-r)
               errel = abs(e1-r)/abs(r)
          
          if j >= 0:
               e1 = abs(r)
          
          if j >= 1:
               if round(errel,cf) <= tol:
                    s = 1
                    break
               elif round(erabs,cf) <= tol:
                    s = 2
                    break
          
          j += 1
          
          if j <= 100:
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("║",j,"║",str(r),"║",trunc(10,round(abs(float(fr)),10)),"║",trunc(10,round(float(erabs),10)),"║",trunc(10,round(float(errel),10)),"║"))
          elif j == 101:
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("╠","═══════════","╬","════════════════════════","╬","═══════════════","╬","═══════════════","╬","═══════════════","╣"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("║",":  :  :","║",":  :  :    :  :  :","║",":   :   :","║",":   :   :","║",":   :   :","║"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("╠","═══════════","╬","════════════════════════","╬","═══════════════","╬","═══════════════","╬","═══════════════","╣"))
               l = 2
          elif j == 1000:
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("║",j,"║",str(r),"║",trunc(10,round(abs(float(fr)),10)),"║",trunc(10,round(float(erabs),10)),"║",trunc(10,round(float(errel),10)),"║"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("╚","═══════════","╩","════════════════════════","╩","═══════════════","╩","═══════════════","╩","═══════════════","╝"))
               print("   ┌────────────────────────────────────────────────────────────────────────────────┐")
               print("   │  Error: Llego al número máximo de iteraciones (1000), no se encontro la raíz.  │")
               print("   │                                                                                │")
               print("   │      Caso: No tiene raíces reales.                                             │")
               print("   └────────────────────────────────────────────────────────────────────────────────┘")
               l = 1
               ax.set_xlim(round(r,cf)-1,round(r,cf)+1)
               ax.set_ylim(-10,10)
               ax.plot(round(r,cf),0,marker ="o",color="white")
               plt.show()
               break
          
          if round(fr,cf) == 0:
               s = 3
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
          elif s == 2:
               print("{:^85}".format("╔════════════════════════════════════════════════════════════════════════════════════╗"))
               print("{:^1}{:^84}{:^1}".format("║","Paro por error absoluto","║"))
               print("{:^85}".format("╚════════════════════════════════════════════════════════════════════════════════════╝"))
          ax.set_xlim(round(r,cf)-1,round(r,cf)+1)
          ax.set_ylim(-10,10)
          ax.plot(round(r,cf),0,marker ="o",color="white")
          plt.show()
     
     elif l == 2:
          print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("║",j,"║",str(r),"║",trunc(10,round(abs(float(fr)),10)),"║",trunc(10,round(float(erabs),10)),"║",trunc(10,round(float(errel),10)),"║"))
          print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("╠","═══════════","╩","════════════════════════","╩","═══════════════","╩","═══════════════","╩","═══════════════","╣"))
          print("{:^1}{:^32}{:^32}{:^20}{:^1}".format("║","Raiz aproximada ≈",trunc(cf,round(r,cf))," ","║"))
          print("{:^86}".format("╚════════════════════════════════════════════════════════════════════════════════════╝"))
          if s == 1:
               print("{:^85}".format("╔════════════════════════════════════════════════════════════════════════════════════╗"))
               print("{:^1}{:^84}{:^1}".format("║","Paro por error relativo","║"))
               print("{:^85}".format("╚════════════════════════════════════════════════════════════════════════════════════╝"))
          elif s == 2:
               print("{:^85}".format("╔════════════════════════════════════════════════════════════════════════════════════╗"))
               print("{:^1}{:^84}{:^1}".format("║","Paro por error absoluto","║"))
               print("{:^85}".format("╚════════════════════════════════════════════════════════════════════════════════════╝"))
          ax.set_xlim(round(r,cf)-1,round(r,cf)+1)
          ax.set_ylim(-10,10)
          ax.plot(round(r,cf),0,marker ="o",color="white")
          plt.show()
          
     p = str(input("\n\t¿Deseas buscar la raiz de otro polinomio? [si/no] »» "))