"""
Nombre: Interpolacion simple
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
                                   Interpolacion simple
      INSTRUCCIONES:
      Este programa usa el método de interpolación simple para hacer un ajuste exacto con una función 
      polinomial que pase por una cierta cantidad de puntos dados.
      Las condiciones que deben de tener estos puntos, es que no se repita mucho los valor en las 
      variable, por ejemplo, no puede haber muchas "x = 2" o "x = 1" y de igual manera con la "y",
      si ocurre esto puede que este método no pueda ajustar una función a estos puntos.
      
      El programa te pedirá los valoras en x y después los valores en y te indicara donde colocarlos.""")

p = "si"
while p == "s" or p == "S" or p == "si" or p == "SI" or p == "Si" or p == "sI":

     li = "si"
     while li == "s" or li == "S" or li == "si" or li == "SI" or li == "Si" or li == "sI":
          
          d = int(input("\n\t¿Cuál el número de puntos que colocaras? : "))
          
          print("\n\tColoca los valores en [x]:")
          print("\n\t\t╠═ x ═╣\n")

          listax = []
          for i in range(d):
               l = float(input(f"\t\tx{i} = "))
               listax.append(l)

          print("\n\tColoca los valores en [y]:")
          print("\n\t\t╠═ y ═╣\n")

          listay = []
          for i in range(d):
               l = float(input(f"\t\ty{i} = "))
               listay.append(l)

          print("{:^61}".format("\n╔═══════════════════════════════════════════════════════════╗"))
          print("{:^1}{:^59}{:^1}".format("║","Lista de datos","║"))
          print("{:^1}{:^11}{:^1}{:^23}{:^1}{:^23}{:^1}".format("╠","═══════════","╦","═══════════════════════","╦","═══════════════════════","╣"))
          print("{:^1}{:^11}{:^1}{:^23}{:^1}{:^23}{:^1}".format("║"," ","║","x","║","y","║"))
          print("{:^1}{:^11}{:^1}{:^23}{:^1}{:^23}{:^1}".format("╠","═══════════","╬","═══════════════════════","╬","═══════════════════════","╣"))
          for i in range(d):
               print("{:^1}{:^11}{:^1}{:^23}{:^1}{:^23}{:^1}".format("║",i,"║",listax[i],"║",listay[i],"║"))
          print("{:^1}{:^11}{:^}{:^23}{:^1}{:^23}{:^1}".format("╚","═══════════","╩","═══════════════════════","╩","═══════════════════════","╝"))

          li = str(input("\n- Observa la tabla - ¿Deseas cambiar los puntos? [si/no] »» "))
     
     ma = []
     mat = []
     for i in range(d):
          for j in range(d+1):
               if j == d:
                    m = listay[i]
               else:
                    m = listax[i]**j
               ma.append(m)
          mat.append(ma)
          ma = []     
     
     
     #Gauss Jordan
     v = 0
     u = 0
     s = 0
     c = d
     f = d+1
     while u < c and v < f-1:
          
          l = mat[v][u]
          if l == 0 and mat[v][u+1] != 0 and u != f-1 and u != f-2:
               u += 1
               l = mat[v][u]
               s = 1
               for j in range(v,f):
                    mat[v][j] =  mat[v][j]/l
          elif l == 0:
               break
          elif l != 0 and l != 1:
               for j in range(v,f):
                    mat[v][j] =  mat[v][j]/l
     
          if c == 2:
               u = 0
          elif u == 1:
               u += 1
          elif u != 1:
               u = 0
          while u < c:
               if u == 1:
                    u += 1
                    for i in range(u,c):
                         l = mat[u][v]
                         for j in range(v,f):
                              mat[i][j] = mat[i][j] + (-1*l)*mat[v][j]
                         u += 1
                         
               elif u != 1 and s != 1:
                    u = 0
                    for i in range(u,c):
                         if u != v:
                              l = mat[u][v]
                              for j in range(v,f):
                                   mat[i][j] = mat[i][j] + (-1*l)*mat[v][j]
                         u += 1
               
               elif s == 1 and u != 1:
                    u = 0
                    v += 1
                    for i in range(u,c):
                         if u != v-1:
                              l = mat[u][v]
                              for j in range(v,f):
                                   mat[i][j] = mat[i][j] + (-1*l)*mat[v-1][j]
                         u += 1
     
          v += 1
          u = v
     
     cof = []
     for i in range(f-1):
          cof.append(mat[d-i-1][f-1])
    
    #Formacion de ecuacion
     ecu = ""
     for i in range(d):
          if cof[i] == 0:
               ec = ""
          elif i == d-1:               
               if cof[i] < 0:
                    ec = f"{abs(cof[i])}"
               else:
                    ec = f"{cof[i]}"
          elif d-i-1 == 1 and i == d-2:
               if cof[i+1] < 0:
                    if cof[i] < 0:
                         ec = f"{abs(cof[i])}*x - "
                    else:
                         ec = f"{cof[i]}*x - "
               else:
                    if cof[i] < 0:
                         ec = f"{abs(cof[i])}*x + "
                    else:
                         ec = f"{cof[i]}*x + "
          elif i == 0 and i != d-2:
               if cof[i+1] < 0:
                    if cof[i] < 0:
                         ec = f"-{abs(cof[i])}*x**{d-i-1} - "
                    else:
                         ec = f"{cof[i]}*x**{d-i-1} - "
               else:
                    if cof[i] < 0:
                         ec = f"-{abs(cof[i])}*x**{d-i-1} + "
                    else:          
                         ec = f"{cof[i]}*x**{d-i-1} + "
          else:
               if cof[i+1] < 0:
                    if cof[i] < 0:
                         ec = f"{abs(cof[i])}*x**{d-i-1} - "
                    else:
                         ec = f"{cof[i]}*x**{d-i-1} - "
               else:
               
                    if cof[i] < 0:
                         ec = f"{abs(cof[i])}*x**{d-i-1} + "
                    else:
                         ec = f"{cof[i]}*x**{d-i-1} + "
          ecu += ec
     
     printecu = ""
     for i in range(d):
          if cof[i] == 0:
               pec = ""
          elif i == d-1:
               if cof[i] < 0:
                    pec = f"{abs(cof[i])}"
               else:
                    pec = f"{cof[i]}"
          elif d-i-1 == 1 and i == d-2:
               if cof[i+1] < 0:
                    if cof[i] < 0:
                         pec = f"{abs(cof[i])} x - "
                    else:
                         pec = f"{cof[i]} x - "
               else:
                    if cof[i] < 0:
                         pec = f"{abs(cof[i])} x + "
                    else:
                         pec = f"{cof[i]} x + "
          elif i == 0 and i != d-2:
               if cof[i+1] < 0:
                    if cof[i] < 0:
                         pec = f"-{abs(cof[i])} x^{d-i-1} - "
                    else:
                         pec = f"{cof[i]} x^{d-i-1} - "
               else:
                    if cof[i] < 0:
                         pec = f"-{abs(cof[i])} x^{d-i-1} + "
                    else:
                         pec = f"{cof[i]} x^{d-i-1} + "
          else:
               if cof[i+1] < 0:
                    if cof[i] < 0:
                         pec = f"{abs(cof[i])} x^{d-i-1} - "
                    else:
                         pec = f"{cof[i]} x^{d-i-1} - "
               else:
                    if cof[i] < 0:
                         pec = f"{abs(cof[i])} x^{d-i-1} + "
                    else:
                         pec = f"{cof[i]} x^{d-i-1} + "
          printecu += pec
     
     print("\n\tLa funcion que se ajusta a los datos es:")
     print(printecu)

     #Grafica
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
          ax.set_title("Interpolación simple")
          ax.plot(k,g,color="red")
          ax.plot(g,k,color="red")
          ax.scatter(listax,listay,marker ="o",color="white")
          ax.plot(k,h,color="blue")
          limx = OrCre(listax)
          limy = OrCre(listay)
          if limx[0] > 100 or limx[d-1] > 100:
               ax.set_xlim(limx[0]-10,limx[d-1]+10)
          else:
               ax.set_xlim(limx[0]-1,limx[d-1]+1)
          if limy[0] > 100 or limy[d-1] > 100:
               ax.set_ylim(limy[0]-10,limy[d-1]+10)
          else:
               ax.set_ylim(limy[0]-1,limy[d-1]+1)
          plt.show()
     
     #Evaluacion en la funcion
     E = str(input("\n\t¿Deseas evaluar la función en un punto? [si/no] »» "))
     while E == "s" or E == "S" or E == "si" or E == "SI" or E == "Si" or E == "sI":
          
          x = float(input("\n\t\tx = "))
          
          print("\n\t\tEl valor en el punto x es: ")
          print(f"\t\t{F(ecu,x)}")
          
          E = str(input("\n\t¿Deseas evaluar en otro punto ? [si/no] »» "))
     
     p = str(input("\n\t¿Deseas buscar la funcion de ajuste de otros datos? [si/no] »» "))