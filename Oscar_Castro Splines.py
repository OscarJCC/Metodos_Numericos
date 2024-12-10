"""
Nombre: Splines cubicos
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

print("""
                                             Splines cúbicos
      INSTRUCCIONES:
      Este programa usa el método de Splines cúbicos para hacer el ajuste a una cierta cantidad “n” de 
      puntos dados, con “n-1” ecuaciones de tercer grado que se crean de punto en punto.
      
      El programa te pedirá los valoras en x y después los valores en y te indicara donde colocarlos.""")

p = "si"
while p == "s" or p == "S" or p == "si" or p == "SI" or p == "Si" or p == "sI":

     li = "si"
     while li == "s" or li == "S" or li == "si" or li == "SI" or li == "Si" or li == "sI":
          
          n = int(input("\n\t¿Cuál el número de puntos que colocaras? : "))
          
          print("\n\tColoca los valores en [x]:")
          print("\n\t\t╠═ x ═╣\n")

          x = []
          for i in range(n):
               l = float(input(f"\t\tx{i} = "))
               x.append(l)

          print("\n\tColoca los valores en [y]:")
          print("\n\t\t╠═ y ═╣\n")

          y = []
          for i in range(n):
               l = float(input(f"\t\ty{i} = "))
               y.append(l)

          print("{:^61}".format("\n╔═══════════════════════════════════════════════════════════╗"))
          print("{:^1}{:^59}{:^1}".format("║","Lista de datos","║"))
          print("{:^1}{:^11}{:^1}{:^23}{:^1}{:^23}{:^1}".format("╠","═══════════","╦","═══════════════════════","╦","═══════════════════════","╣"))
          print("{:^1}{:^11}{:^1}{:^23}{:^1}{:^23}{:^1}".format("║"," ","║","x","║","y","║"))
          print("{:^1}{:^11}{:^1}{:^23}{:^1}{:^23}{:^1}".format("╠","═══════════","╬","═══════════════════════","╬","═══════════════════════","╣"))
          for i in range(n):
               print("{:^1}{:^11}{:^1}{:^23}{:^1}{:^23}{:^1}".format("║",i,"║",x[i],"║",y[i],"║"))
          print("{:^1}{:^11}{:^}{:^23}{:^1}{:^23}{:^1}".format("╚","═══════════","╩","═══════════════════════","╩","═══════════════════════","╝"))

          li = str(input("\n- Observa la tabla - ¿Deseas cambiar los puntos? [si/no] »» "))
     
     d = ((n-1)*4)
     
     # Creacion de la matriz
     m = 0
     ma = []
     mat = []
     a = 0
     k = 2
     z = 3
     s = 0
     e = 0
     for i in range(d):
          for j in range(d):
               if i < d/2:
                    if i < 2 and z-j >= 0:
                         a = i
                         m = (x[a])**(z-j)
                    elif i >= k-2 and i < k and j >= s and z-j >= 0 and a < n:
                         a = i-e
                         m = (x[a])**(z-j)
                    else:
                         m = 0
               elif i >= d/2 and i < (d-n):
                    if j >= s and j < z and j != z:
                         if j == s:
                              m = ((3*((x[a])**(2)))*e)
                         elif j == s+1:
                              m = ((2*(x[a]))*e)
                         elif j == s+2:
                              m = ((1)*e)
                         else:
                              m = 0
                    elif j == z:
                         m = 0
                         z += 4
                         e = -1
                         s = k*2
                    else:
                         m = 0
               elif i >= d-n and i < d-2:
                    if j >= s and j < z-1 and j != z:
                         if j == s:
                              m = ((6*(x[a]))*e)
                         elif j == s+1:
                              m = ((2)*e)
                         else:
                              m = 0
                    elif j == z:
                         m = 0
                         z += 4
                         e = -1
                         s = k*2
                    else:
                         m = 0
               elif i >= d-2:
                    if i == d-2 and j <= 1:
                         if j == 0:
                              m = (6*(x[0]))
                         else:
                              m = 2
                    elif i == d-1 and j >= d-2:
                         if j == d-2:
                              m = 6*(x[n-1])
                         else:
                              m = 2
                    else:
                         m = 0
               ma.append(m)
          mat.append(ma)
          ma = []
          if i == k-1 and i < (d/2)-1:
               s = k*2
               k += 2
               z += 4
               e += 1
          elif i == (d/2)-1 or i == (d-n)-1:
               a = 1
               k = 2
               z = 3
               s = 0
               e = 1
          elif i > (d/2)-1 and i < (d-n):
               a += 1
               k += 2
               z = 3+s
               e = 1
          elif i > (d-n)-1 and i < (d-2):
               a += 1
               k += 2
               z = 3+s
               e = 1
     
     ms = []
     b = []
     a = 0
     e = 1
     for i in range(d):
          if i == 0:
               b = y[i]
          elif i >= 0 and i <= d/2-1:
               a = i-e
               b = y[a]
               e += 1           
          elif i == d/2-1:
               b = y[i]
          else:
               b = 0
          ms.append(b)
          e = a
     
     #Solucion del sistema
     B = np.array(ms)
     
     A = np.array(mat)
     
     #print(mat)
     
     Ainv = np.linalg.inv(A)
     
     sol = np.dot(Ainv,B)
     
     sol = list(sol)
     
     #Imprecion de ecuaciones     
     ec = ""
     a = 0
     print("{:^141}".format("\n╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗"))
     print("{:^1}{:5}{:4}{:105}{:^25}{:^1}".format("║"," "," ","Ecuaciones","Rango","║"))
     for i in range(n-1):
          o = 3
          for j in range(a,len(sol)):
               if j < (a + len(sol)/(n-1))-1:
                    if o == 3 or o == 2:
                         if sol[j] < 0:
                              ec += f"- {abs(sol[j])} x^{o} "
                         else:
                              ec += f"+ {sol[j]} x^{o} "
                         o = o-1
                    else:
                         if sol[j] < 0:
                              ec += f"- {abs(sol[j])} x "
                         else:
                              ec += f"+ {sol[j]} x "
               elif j == (a + len(sol)/(n-1))-1:
                    if sol[j] < 0:
                         ec += f"- {abs(sol[j])}"
                    else:
                         ec += f"+ {sol[j]}"
                         
                    if i == n-2:
                         print("{:^1}{:5}{:4}{:105}{:^25}{:^1}".format("║",i+1,") ≫ ",f"   {ec}",f"{x[i]} ≤ x ≤ {x[i+1]}","║"))
                    else:
                         print("{:^1}{:5}{:4}{:105}{:^25}{:^1}".format("║",i+1,") ≫ ",f"   {ec}",f"{x[i]} ≤ x < {x[i+1]}","║"))
                    ec = ""
                    a = j+1
                    break
     print("{:^141}".format("╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝"))
     
     # Grafica
     G = str(input("\n\t¿Deseas graficar los datos? [si/no] »» "))
     if G == "s" or G == "S" or G == "si" or G == "SI" or G == "Si" or G == "sI":
          k = np.linspace(-1000,1000,100001)
          g = [0]*100001

          plt.style.use("dark_background") 
          fig, ax = plt.subplots()
          
          ax.set_title("Splines cubico")
          ax.plot(k,g,color="red")
          ax.plot(g,k,color="red")
          ax.scatter(x,y,marker ="o",color="white")
          ec = ""
          a = 0
          r = []
          for i in range(n-1):
               o = 3
               for j in range(a,len(sol)):
                    if j < (a + len(sol)/(n-1))-1:
                         if o == 3 or o == 2:
                              if sol[j] < 0:
                                   ec += f"- {abs(sol[j])}*x**{o} "
                              else:
                                   ec += f"+ {sol[j]}*x**{o} "
                              o = o-1
                         else:
                              if sol[j] < 0:
                                   ec += f"- {abs(sol[j])}*x "
                              else:
                                   ec += f"+ {sol[j]}*x "
                    elif j == (a + len(sol)/(n-1))-1:
                         if sol[j] < 0:
                              ec += f"- {abs(sol[j])}"
                         else:
                              ec += f"+ {sol[j]}"

                         l = np.linspace(x[i],x[i+1],100001)

                         h = []
                         for k in l:
                              u = F(ec,k)
                              h.append(u)

                         ax.plot(l,h,color="blue")

                         ec = ""
                         a = j+1
                         break

          limx = OrCre(x)
          limy = OrCre(y)
          if limx[0] > 100 or limx[n-1] > 100:
               ax.set_xlim(limx[0]-10,limx[n-1]+10)
          else:
               ax.set_xlim(limx[0]-1,limx[n-1]+1)
          if limy[0] > 100 or limy[n-1] > 100:
               ax.set_ylim(limy[0]-10,limy[n-1]+10)
          else:
               ax.set_ylim(limy[0]-1,limy[n-1]+1)
          plt.show()
     
     #Evacluacion en ecuaciones
     E = str(input("\n\t¿Deseas evaluar en un punto? [si/no] »» "))
     while E == "s" or E == "S" or E == "si" or E == "SI" or E == "Si" or E == "sI":
          q = 0
          while q == 0:
               xe = float(input("\n\t\tx = "))
               if xe >= x[0] and xe < x[n-1]:
                    q = 1
               else:
                    print("\n\t┌────────────────────────────────────────────────────┐")
                    print("  \t│  Error: 'x' esta fuera del rango de puntos dados.  │")
                    print("  \t└────────────────────────────────────────────────────┘")
                    q = 0
          print("\n\t\tEl valor en el punto x es: ")
          ec = ""
          a = 0
          for i in range(n-1):
               o = 3
               for j in range(a,len(sol)):
                    if j < (a + len(sol)/(n-1))-1:
                         if o == 3 or o == 2:
                              if sol[j] < 0:
                                   ec += f"- {abs(sol[j])}*x**{o} "
                              else:
                                   ec += f"+ {sol[j]}*x**{o} "
                              o = o-1
                         else:
                              if sol[j] < 0:
                                   ec += f"- {abs(sol[j])}*x "
                              else:
                                   ec += f"+ {sol[j]}*x "
                    elif j == (a + len(sol)/(n-1))-1:
                         if sol[j] < 0:
                              ec += f"- {abs(sol[j])}"
                         else:
                              ec += f"+ {sol[j]}"

                         if xe >= x[i] and xe < x[i+1]:
                              if i == n-2:
                                   print(f"\t\t{F(ec,xe)}   ≫   esta en {x[i]} ≤ x ≤ {x[i+1]}")
                              else:
                                   print(f"\t\t{F(ec,xe)}   ≫   esta en {x[i]} ≤ x < {x[i+1]}")    
                         ec = ""
                         a = j+1
                         break
          
          E = str(input("\n\t¿Deseas evaluar en otro punto ? [si/no] »» "))

     p = str(input("\n\t¿Deseas buscar las funcion de ajuste de otros datos? [si/no] »» "))