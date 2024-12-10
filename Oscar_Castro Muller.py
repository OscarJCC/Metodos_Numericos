"""
Nombre: muller
Fecha Inicio: 07/10/2021
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

"""
import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.scimath import sqrt

def F(ecuacion,x):
     return eval(str(ecuacion))

def cuamuller(ecuacion,x0,x1,x2,tol):
     fx0 = F(ecuacion,x0)
     fx1 = F(ecuacion,x1)
     fx2 = F(ecuacion,x2)

     q0 = fx0 - fx2
     q1 = fx1 - fx2

     h0 = x1 - x2
     h1 = x0 - x2

     w = (h0*(h1**2))-((h0**2)*h1)
     
     if w == 0:
          w = tol
          
     a = ((q0*h0)-(q1*h1))/(w)
     b = ((q1*(h1**2))-(h0**2)*q0)/(w)
     c = fx2
     
     if b < 0 and c < 0:
          ecuaexp2 = str(a)+"*x**2"+str(b)+"*x"+str(c)
     elif b > 0 and c > 0:
          ecuaexp2 = str(a)+"*x**2+"+str(b)+"*x+"+str(c)
     elif b < 0 and c > 0:
          ecuaexp2 = str(a)+"*x**2"+str(b)+"*x+"+str(c)
     elif b > 0 and c < 0:
          ecuaexp2 = str(a)+"*x**2+"+str(b)+"*x"+str(c)
          
     return(ecuaexp2)

def trunc(cf,num):
     n = str(num)

     if type(num) == complex or type(num) == np.complex128:
          rnum = round(float(num.real),cf)
          rnumi = round(float(num.imag),cf)
          rni = str(rnum)
          ri = str(rnumi)
                    
          if rnum < 0 and rnum - int(rnum) == 0:
               rnum = float(str(rni[:cf+1]))
          elif rnum < 0 and rnum - int(rnum) != 0:
               rnum = float(str(rni[:cf+2]))
          elif rnum - int(rnum) != 0:
               rnum = float(str(rni[:cf+1]))
          elif rnum - int(rnum) == 0:
               rnum = float(str(rni[:cf]))
          
          if rnumi < 0 and rnumi - int(rnumi) == 0:
               rnumi = float(str(ri[:cf+1]))
          elif rnumi < 0 and rnumi - int(rnumi) != 0:
               rnumi = float(str(ri[:cf+2]))
          elif rnumi - int(rnumi) != 0:
               rnumi = float(str(ri[:cf+1]))
          elif rnumi - int(rnumi) == 0:
               rnumi = float(str(ri[:cf]))
          
          num = rnum + (rnumi)*1j
          
     elif num < 0 and num - int(num) == 0:
          num = float(str(n[:cf+1]))
     elif num < 0 and num - int(num) != 0:
          num = float(str(n[:cf+2]))
     elif num - int(num) != 0:
          num = float(str(n[:cf+1]))
     elif num - int(num) == 0:
          num = float(str(n[:cf]))
          
     return num

print("""
                                        MULLER
      INSTRUCCIONES:
      Este programa calcula la raíz de un polinomio usando el método de Muller.
      Para calcular la raíz debes colocar 3 puntos de los que se obtiene una 
      ecuación cuadrática, de esta ecuación sacamos sus raíces y las usamos para 
      aproximarnos a las raíces del polinomio, Con este método también podemos 
      obtienen las raíces imaginarias del polinomio.s
      
      ECUACION: Para colocar la ecuación f(x) solo se puede usar de variable la letra " x ",
                para colocar un exponente debes colocar un (**) y para una multiplicación debes
                colocar (*).
                Ejemplo:
                
                ╠═══  x**3-2*x**2-1  ═══╣
                
                ╠═ x = -1 ═╣ ╠═ x = 0 ═╣ ╠═ x = 1 ═╣ """)

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
     
     k = np.linspace(-100,100,1001)

     d = []
     g = []
     for i in k:
          e = F(ecuacion,i)
          d.append(e)
          g.append(0)
     
     inter = "si"
     while inter == "s" or inter == "S" or inter == "si" or inter == "SI" or inter == "Si" or inter == "sI":
          i = 0
          while i == 0:
               x0 = float(input("\n\t Coloca un punto (x0):"))
               x1 = float(input("  \t Coloca un punto (x1):"))
               x2 = float(input("  \t Coloca un punto (x2):"))

               if x0 == x1 or x1 == x2 or x0 == x2:
                    print("\n\t┌─────────────────────────────────────────────────────────────────────┐")
                    print("  \t│  Error: Dos de los puntos son iguales, deben ser todos diferentes.  │")
                    print("  \t└─────────────────────────────────────────────────────────────────────┘")
               else:
                    i = 1

          lpunts = [x0,x1,x2]
          for i in range(1,len(lpunts)):
               for j in range(len(lpunts)-i):
                    if(lpunts[j] < lpunts[j+1]):
                         aux = lpunts[j]
                         lpunts[j] = lpunts[j+1]
                         lpunts[j+1] = aux
                         
          fx0 = F(ecuacion,x0)
          fx1 = F(ecuacion,x1)
          fx2 = F(ecuacion,x2)
          
          cf = int(input("\n\t Cifras significativas:"))
          tol = 10**(-1*(cf))
          
          #h = []
          #v = cuamuller(ecuacion,x0,x1,x2,tol)
          #for i in k:
          #     u = F(v,i)
          #     h.append(u)
               
          plt.style.use("dark_background") 
          fig, ax = plt.subplots()
          ax.grid()
          ax.set_title("Muller")
          ax.plot(k,g,color="red")
          ax.plot(g,k,color="red")
          #ax.plot(k,h,color="orange",label=f"$r(x) = {v}$")
          ax.plot(k,d,color="blue",label=f"$f(x) = {ecuacion}$")
          ax.plot(x0,0,marker ="o",color="white")
          ax.plot(x1,0,marker ="o",color="white")
          ax.plot(x2,0,marker ="o",color="white")
          ax.plot(x0,fx0,marker ="o",color="white")
          ax.plot(x1,fx1,marker ="o",color="white")
          ax.plot(x2,fx2,marker ="o",color="white")
          ax.set_xlim(lpunts[2]-1,lpunts[0]+1)
          ax.set_ylim(-10,10)
          ax.legend()
          plt.show()
          
          inter = str(input("- Observa la gráfica - ¿Deseas cambiar los puntos? [si/no] »» "))
     
     plt.style.use("dark_background") 
     fig, ax = plt.subplots()
     ax.grid()
     ax.set_title("Muller")
     ax.plot(k,g,color="red")
     ax.plot(g,k,color="red")
     ax.plot(k,d,color="blue",label=f"$f(x) = {ecuacion}$")
     ax.set_xlim(lpunts[2]-1,lpunts[0]+1)
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
               print("{:^98}".format("╔════════════════════════════════════════════════════════════════════════════════════════════════╗"))
               print("{:^1}{:^96}{:^1}".format("║",f"{ecuacion}","║"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^19}{:^1}{:^19}{:^1}{:^19}{:^1}".format("╠","═══════════","╦","════════════════════════","╦","═══════════════════","╦","═══════════════════","╦","═══════════════════","╣"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^19}{:^1}{:^19}{:^1}{:^19}{:^1}".format("║","Iteracion","║","Raiz","║","F(x)","║","Error abs","║","Error rel","║"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^19}{:^1}{:^19}{:^1}{:^19}{:^1}".format("╠","═══════════","╬","════════════════════════","╬","═══════════════════","╬","═══════════════════","╬","═══════════════════","╣"))
          
          fx0 = F(ecuacion,x0)
          fx1 = F(ecuacion,x1)
          fx2 = F(ecuacion,x2)

          q0 = fx0 - fx2
          q1 = fx1 - fx2

          h0 = x1 - x2
          h1 = x0 - x2

          w = (h0*(h1**2))-((h0**2)*h1)
          
          if w == 0:
               w = tol
               
          a = ((q0*h0)-(q1*h1))/(w)
          b = ((q1*(h1**2))-(h0**2)*q0)/(w)
          c = fx2
          
          if (b-sqrt((b**2)-4*a*c)) == 0 or (b+sqrt((b**2)-4*a*c)) == 0 :
               r1 = (x2) - (2*c)/tol
               r2 = (x2) - (2*c)/tol
          else:
               r1 = (x2) - (2*c)/(b+sqrt((b**2)-4*a*c))
               r2 = (x2) - (2*c)/(b-sqrt((b**2)-4*a*c))
          
          x0 = x1
          x1 = x2

          fr1 = F(ecuacion,r1)
          fr2 = F(ecuacion,r2)
     
          if type(r1) == np.complex128 or type(r2) == np.complex128:          
               if abs(fr1) <= abs(fr2):
                    x2 = r1
               else:
                    x2 = r2
          else:
               if abs(fr1) <= abs(fr2):
                    x2 = r1
               elif abs(fr2) < abs(fr1):
                    x2 = r2
          
          erabs = 0
          errel = 0
          if type(x2) == np.complex128:
               if j >= 1 and x2 == 0:
                    erabs = e1-x2
                    errel = e1-x2/tol
               elif j >= 1 and x2 != 0:
                    erabs = e1-x2
                    errel = e1-x2/x2
          else:
               if j >= 1 and x2 == 0:
                    erabs = abs(e1-x2)
                    errel = abs(e1-x2)/abs(tol)
               elif j >= 1 and x2 != 0:
                    erabs = abs(e1-x2)
                    errel = abs(e1-x2)/abs(x2)
          
          if type(x2) == np.complex128:
               if j >= 0:
                    e1 = x2
          else:
               if j >= 0:
                    e1 = abs(x2)
          
          if type(x2) == np.complex128:
               if j >= 1:
                    if abs(errel) == tol:
                         s = 1
                         break
                    elif abs(erabs) == tol:
                         s = 2
                         break
          else:
               if j >= 1:
                    if round(errel,cf) <= tol:
                         s = 1
                         break
                    elif round(erabs,cf) <= tol:
                         s = 2
                         break
          
          if type(fx2) == np.complex128:
               if trunc(cf,fx2) == 0:
                    break
               elif fx0 == 0:
                    break
               elif fx1 == 0:
                    break
               elif fx2 == 0:
                    break
          elif round(fx2,cf) == 0:
               break
          
          j += 1
          
          if j <= 100:
               if type(x2) != np.complex128:
                    print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^19}{:^1}{:^19}{:^1}{:^19}{:^1}".format("║",j,"║",str(x2),"║",trunc(10,round(abs(float(fx2)),10)),"║",trunc(10,round(float(erabs),10)),"║",trunc(10,round(float(errel),10)),"║"))
               elif type(x2) == np.complex128:
                    print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^19}{:^1}{:^19}{:^1}{:^19}{:^1}".format("║",j,"║",trunc(7,x2),"║",trunc(5,fx2),"║",trunc(5,erabs),"║",trunc(5,errel),"║"))
          elif j == 101:
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^19}{:^1}{:^19}{:^1}{:^19}{:^1}".format("╠","═══════════","╬","════════════════════════","╬","═══════════════════","╬","═══════════════════","╬","═══════════════════","╣"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^19}{:^1}{:^19}{:^1}{:^19}{:^1}".format("║",":  :  :","║",":  :  :    :  :  :","║",":   :   :","║",":   :   :","║",":   :   :","║"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^19}{:^1}{:^19}{:^1}{:^19}{:^1}".format("╠","═══════════","╬","════════════════════════","╬","═══════════════════","╬","═══════════════════","╬","═══════════════════","╣"))
               l = 2
          elif j == 1000:
               if type(x2) != np.complex128:
                    print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^19}{:^1}{:^19}{:^1}{:^19}{:^1}".format("║",j,"║",str(x2),"║",trunc(10,round(abs(float(fx2)),10)),"║",trunc(10,round(float(erabs),10)),"║",trunc(10,round(float(errel),10)),"║"))
               elif type(x2) == np.complex128:
                    print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^19}{:^1}{:^19}{:^1}{:^19}{:^1}".format("║",j,"║",trunc(7,x2),"║",trunc(5,fx2),"║",trunc(5,erabs),"║",trunc(5,errel),"║"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^19}{:^1}{:^19}{:^1}{:^19}{:^1}".format("╚","═══════════","╩","════════════════════════","╩","═══════════════════","╩","═══════════════════","╩","═══════════════════","╝"))
               print("   ┌────────────────────────────────────────────────────────────────────────────────┐")
               print("   │  Error: Llego al número máximo de iteraciones (1000), no se encontro la raíz.  │")
               print("   └────────────────────────────────────────────────────────────────────────────────┘")
               l = 1
               
               if type(x2) == np.complex128:
                    ax.set_xlim(round(x2.real,cf)-1,round(x2.real,cf)+1)
                    ax.set_ylim(-10,10)
                    ax.plot(round(x2.real,cf),round(x2.imag,cf),marker ="o",color="white")
                    plt.show()
               else:
                    ax.set_xlim(round(x2,cf)-1,round(x2,cf)+1)
                    ax.set_ylim(-10,10)
                    ax.plot(round(x2,cf),0,marker ="o",color="white")
                    plt.show()
               break
          
          a = r
            
     if l == 0:
          print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^19}{:^1}{:^19}{:^1}{:^19}{:^1}".format("╠","═══════════","╩","════════════════════════","╩","═══════════════════","╩","═══════════════════","╩","═══════════════════","╣"))
          if type(x2) != np.complex128:
               print("{:^1}{:^32}{:^32}{:^32}{:^1}".format("║","Raiz aproximada ≈",trunc(cf,round(x2,cf))," ","║"))
          elif type(x2) == np.complex128:
               print("{:^1}{:^32}{:^32}{:^32}{:^1}".format("║","Raiz aproximada ≈",trunc(cf,x2)," ","║"))
          print("{:^97}".format("╚════════════════════════════════════════════════════════════════════════════════════════════════╝"))
          if s == 1:
               print("{:^97}".format("╔════════════════════════════════════════════════════════════════════════════════════════════════╗"))
               print("{:^1}{:^96}{:^1}".format("║","Paro por error relativo","║"))
               print("{:^97}".format("╚════════════════════════════════════════════════════════════════════════════════════════════════╝"))
          elif s == 2:
               print("{:^97}".format("╔════════════════════════════════════════════════════════════════════════════════════════════════╗"))
               print("{:^1}{:^96}{:^1}".format("║","Paro por error absoluto","║"))
               print("{:^97}".format("╚════════════════════════════════════════════════════════════════════════════════════════════════╝"))
          if type(x2) == np.complex128:
               ax.set_xlim(round(x2.real,cf)-1,round(x2.real,cf)+1)
               ax.set_ylim(-10,10)
               ax.plot(round(x2.real,cf),round(x2.imag,cf),marker ="o",color="white")
               plt.show()
          else:
               ax.set_xlim(round(x2,cf)-1,round(x2,cf)+1)
               ax.set_ylim(-10,10)
               ax.plot(round(x2,cf),0,marker ="o",color="white")
               plt.show()
     
     elif l == 2:
          if type(x2) != np.complex128:
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^19}{:^1}{:^19}{:^1}{:^19}{:^1}".format("║",j,"║",str(x2),"║",trunc(10,round(abs(float(fx2)),10)),"║",trunc(10,round(float(erabs),10)),"║",trunc(10,round(float(errel),10)),"║"))
          elif type(x2) == np.complex128:
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^19}{:^1}{:^19}{:^1}{:^19}{:^1}".format("║",j,"║",trunc(7,x2),"║",trunc(5,fx2),"║",trunc(5,erabs),"║",trunc(5,errel),"║"))
          print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^19}{:^1}{:^19}{:^1}{:^19}{:^1}".format("╠","═══════════","╩","════════════════════════","╩","═══════════════════","╩","═══════════════════","╩","═══════════════════","╣"))
          if type(x2) != np.complex128:
               print("{:^1}{:^32}{:^32}{:^32}{:^1}".format("║","Raiz aproximada ≈",trunc(cf,round(x2,cf))," ","║"))
          elif type(x2) != np.complex128:
               print("{:^1}{:^32}{:^32}{:^32}{:^1}".format("║","Raiz aproximada ≈",trunc(cf,x2)," ","║"))
          print("{:^97}".format("╚════════════════════════════════════════════════════════════════════════════════════════════════╝"))
          if s == 1:
               print("{:^97}".format("╔════════════════════════════════════════════════════════════════════════════════════════════════╗"))
               print("{:^1}{:^96}{:^1}".format("║","Paro por error relativo","║"))
               print("{:^97}".format("╚════════════════════════════════════════════════════════════════════════════════════════════════╝"))
          elif s == 2:
               print("{:^97}".format("╔════════════════════════════════════════════════════════════════════════════════════════════════╗"))
               print("{:^1}{:^96}{:^1}".format("║","Paro por error absoluto","║"))
               print("{:^97}".format("╚════════════════════════════════════════════════════════════════════════════════════════════════╝"))
          if type(x2) == np.complex128:
               ax.set_xlim(round(x2.real,cf)-1,round(x2.real,cf)+1)
               ax.set_ylim(-10,10)
               ax.plot(round(x2.real,cf),round(x2.imag,cf),marker ="o",color="white")
               plt.show()
          else:
               ax.set_xlim(round(x2,cf)-1,round(x2,cf)+1)
               ax.set_ylim(-10,10)
               ax.plot(round(x2,cf),0,marker ="o",color="white")
               plt.show()
          
     p = str(input("\n\t¿Deseas buscar la raiz de otro polinomio? [si/no] »» "))