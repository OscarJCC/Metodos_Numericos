"""
Nombre: Minimos Cuadrados
Fecha Inicio:
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

"""

import numpy as np
import matplotlib.pyplot as plt

def F(ecuacion,x):
     return eval(str(ecuacion))

def OrCre(lista):
     for i in range(1,len(lista)):
          for j in range(len(lista)-i):
               if(lista[j] > lista[j+1]):
                    aux = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = aux
     return lista

def recta(m,b):
     if b > 0:
          m = str(m)
          b = str(b)
          funr = m+"*x + "+b
     elif b < 0:
          m = str(m)
          b = str(abs(b))
          funr = m+"*x - "+b
     elif b == 0:
          m = str(m)
          b = str(b)
          funr = m+"*x"
     
     return funr

print("""
                                        MINIMOS CUADRADOS
      INSTRUCCIONES:
      Este programa usa el metodo de minimos cuadrados para encontrar la recta que se ajusta a un
      conjunto de datos.
      
      El programa te pedirá los valoras en x y después los valores en y te indicara donde colocarlos.""")

p = "si"
while p == "s" or p == "S" or p == "si" or p == "SI" or p == "Si" or p == "sI":

     li = "si"
     while li == "s" or li == "S" or li == "si" or li == "SI" or li == "Si" or li == "sI":
          
          d = int(input("\n\t¿Cuál el número de puntos que colocaras? : "))
          
          print("\n\tColoca los valores en [x]:")
          print("\n\t\t╠═ x ═╣\n")

          x = []
          for i in range(d):
               l = float(input(f"\t\tx{i+1} = "))
               x.append(l)

          print("\n\tColoca los valores en [y]:")
          print("\n\t\t╠═ y ═╣\n")

          y = []
          for i in range(d):
               l = float(input(f"\t\ty{i+1} = "))
               y.append(l)

          print("{:^49}".format("\n╔═══════════════════════════════════════════════╗"))
          print("{:^1}{:^47}{:^1}".format("║","Lista de datos","║"))
          print("{:^1}{:^23}{:^1}{:^23}{:^1}".format("╠","═══════════════════════","╦","═══════════════════════","╣"))
          print("{:^1}{:^23}{:^1}{:^23}{:^1}".format("║","x","║","y","║"))
          print("{:^1}{:^23}{:^1}{:^23}{:^1}".format("╠","═══════════════════════","╬","═══════════════════════","╣"))
          for i in range(d):
               print("{:^1}{:^23}{:^1}{:^23}{:^1}".format("║",x[i],"║",y[i],"║"))
          print("{:^1}{:^23}{:^1}{:^23}{:^1}".format("╚","═══════════════════════","╩","═══════════════════════","╝"))

          li = str(input("\n- Observa la tabla - ¿Deseas cambiar los puntos? [si/no] »» "))
          
     xy = []     
     for i in range(d):
          xy.append(x[i]*y[i])
     
     x2 = []
     for i in range(d):
          x2.append((x[i])**2)
     
     sumax = 0
     for i in x:
          sumax += i
     
     sumay = 0
     for i in y:
          sumay += i
          
     sumaxy = 0
     for i in xy:
          sumaxy += i
          
     sumax2 = 0
     for i in x2:
          sumax2 += i
     
     m = ((d*(sumaxy))-(sumax*sumay))/((d*(sumax2))-((sumax)**2))
                                       
     b = ((sumax2*sumay)-(sumaxy*sumax))/((d*(sumax2))-((sumax)**2))
     
     ecu = recta(m,b)
     
     print("{:^49}".format("\n╔═══════════════════════════════════════════════╗"))
     print("{:^1}{:^47}{:^1}".format("║","Recta de ajuste","║"))
     print("{:^1}{:^47}{:^1}".format("║",ecu,"║"))
     print("{:^49}".format("╚═══════════════════════════════════════════════╝"))

     
     G = str(input("\n\t¿Deseas que se graficar los datos? [si/no] »» "))
     if G == "s" or G == "S" or G == "si" or G == "SI" or G == "Si" or G == "sI":
          k = np.linspace(-1000,1000,100001)
          g = [0]*100001

          h = []
          for i in k:
               u = F(ecu,i)
               h.append(u)

          plt.style.use("dark_background") 
          fig, ax = plt.subplots()
          #ax.grid()
          ax.set_title("Minimos Cuadrados")
          ax.plot(k,g,color="red")
          ax.plot(g,k,color="red")
          ax.scatter(x,y,marker ="o",color="white")
          ax.plot(k,h,color="blue")
          limx = OrCre(x)
          limy = OrCre(y)
          if limx[0] > 100 or limx[d-1] > 100:
               ax.set_xlim(limx[0]-10,limx[d-1]+10)
          else:
               ax.set_xlim(limx[0]-1,limx[d-1]+1)
          if limy[0] > 100 or limy[d-1] > 100:
               ax.set_ylim(limy[0]-10,limy[d-1]+10)
          else:
               ax.set_ylim(limy[0]-1,limy[d-1]+1)
          plt.show()
     
     p = str(input("\n\t¿Deseas buscar la recta de ajuste de otros datos? [si/no] »» "))
     