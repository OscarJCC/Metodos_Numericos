"""
Nombre: Gauss Seidel
Fecha Inicio: 21/10/2021
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

"""
import math
def trunc(cf,num):

     if type(num) == float or type(num) == int:
          n = str(round(float(num),cf))
          l = 0
          nu =""
          for j in n:
               if j == "e":
                    nu += j
                    l = 1   
               elif l == 1:
                    nu += j
                    
          if (len(n)-len(nu)) <= cf:
               num = float(str(n[:len(n)-len(nu)]))
          elif num < 0 and num - int(num) == 0:
               num = float(str(n[:cf+1]))
          elif num < 0 and num - int(num) != 0:
               num = float(str(n[:cf+2]))
          elif num - int(num) != 0:
               num = float(str(n[:cf+1]))
          elif num - int(num) == 0:
               num = float(str(n[:cf]))

          for j in str(num):
               if j == "e":
                    l = 0
                    break
                    
          if l == 1: 
               num = str(num)
               num += nu
               num = float(num)
               l = 0
          
     elif type(num) == complex:
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
     
     elif type(num) == list:
          nume = []
          for i in range(len(num)):
               n = str(round(float(num[i]),cf))
               
               l = 0
               nu =""
               for j in n:
                    if j == "e":
                         nu += j
                         l = 1   
                    elif l == 1:
                         nu += j
               
               if num[i] < 0 and num[i] - int(num[i]) == 0:
                    nume.append(float(str(n[:cf+1])))
               elif num[i] < 0 and num[i] - int(num[i]) != 0:
                    nume.append(float(str(n[:cf+2])))
               elif num[i] - int(num[i]) != 0:
                    nume.append(float(str(n[:cf+1])))
               elif num[i] - int(num[i]) == 0:
                    nume.append(float(str(n[:cf])))
                    
               for j in str(nume[i]):
                    if j == "e":
                         l = 0
                    
               if l == 1: 
                    nume[i] = str(nume[i])
                    nume[i] += nu
                    nume[i] = float(nume[i])
                    l = 0
          
     if type(num) == list:
          return nume   
     else:       
          return num

def PrintMat(name,matriz,c,f,cf):
     if cf > 10:
          print(f"\n{name}:\n")
          for i in range(c):
               for j in range(f):
                    if j == f-1:
                         print("{:^3}{:^14}".format(" ¦ ",trunc(cf,matriz[i][j])),end=" ")
                    else:
                         print("{:^14}".format(trunc(cf,matriz[i][j])),end=" ")
               print("\n")
     elif cf > 10:
          print(f"\n{name}:\n")
          for i in range(c):
               for j in range(f):
                    if j == f-1:
                         print("{:^3}{:^24}".format(" ¦ ",trunc(cf,matriz[i][j])),end=" ")
                    else:
                         print("{:^24}".format(trunc(cf,matriz[i][j])),end=" ")
               print("\n")
     else:
          print(f"\n{name}:\n")
          for i in range(c):
               for j in range(f):
                    if j == f-1:
                         print("{:^3}{:^9}".format(" ¦ ",trunc(cf,matriz[i][j])),end=" ")
                    else:
                         print("{:^9}".format(trunc(cf,matriz[i][j])),end=" ")
               print("\n")
               
def NorVec(lista):
     j = 0
     for i in lista:
          j += math.pow(i,2)

     nv = math.sqrt(j)
     
     return nv
               
print("""
                                        Gauss Seidel
      INSTRUCCIONES:
      Este programa usa el método de Gauss Seidel para encontrar la solución a sistemas de 
      ecuaciones con las condicion iniciales:
          ■    Al formar la matriz con los coeficientes la diagonal debe ser estrictamente 
               domínate, para que la diagonal de la matriz se estrictamente domínate:
            
               |C00| > |C01| + |C02| + ⋯  + |C0n|
               |C11| > |C10| + |C12| + ⋯  + |C1n|
                 ⋮       ⋮       ⋮     ⋱       ⋮
               |Cnn| > |Cn1| + |Cn2| + ⋯  + |Cnn-1|  
            
               Si esta condición no se cumple el programa no converge, por lo que no 
               encuantra la solución del sistema.
            
          ■    La ecuación debe tener las mismas variables que ecuación, la matriz de 
               coeficientes debe ser cuadrada, esta debe tener un determinante ≠ 0 y
               no puede tener ceros en su diagonal.
            """)

p = "si"
while p == "s" or p == "S" or p == "si" or p == "SI" or p == "Si" or p == "sI":
     d = int(input("\n\tColoca la dimensión de la matriz que se formara : "))
     f = d+1
     c = d

     x = []
     for i in range(f-1):
          if i == 0:
               x.append(float(input(f"\n\tValor x{i+1} = ")))
          else:
               x.append(float(input(f"\tValor x{i+1} = ")))

     cf = int(input("\n\tCifras significativas:"))
     tol = 10**(-1*(cf))
     
     m = "si"
     while m == "s" or m == "S" or m == "si" or m == "SI" or m == "Si" or m == "sI":
          ecu= ""
          for i in range(c):
               for j in range(f):
                    if j >= f-1:
                         ec = f"= (S{i+1})"
                    elif j == f-2:
                         ec = f"(C{i}{j}) x{j+1} "
                    else:
                         ec = f"(C{i}{j}) x{j+1} + "
                    ecu += ec
               if i == 0:
                    print(f"\n{ecu}")
               else:
                    print(ecu)
               ecu = ""

          ma = []
          mat = []
          for i in range(c):
               for j in range(f):
                    if j == 0:
                         m = float(input(f"\nC{i}{j} = "))
                    elif j >= f-1:
                              m = float(input(f"S{i+1}  = "))
                    else:
                         m = float(input(f"C{i}{j} = "))
                    ma.append(m)
               mat.append(ma)
               ma = []


          ecu= ""
          for i in range(c):
               for j in range(f):
                    if j >= f-1:
                         ec = f"= {mat[i][j]}"
                    elif j == f-2:
                         if mat[i][j] < 0:
                              ec = f"- {abs(mat[i][j])} x{j+1} "
                         else:
                              ec = f"{mat[i][j]} x{j+1} "
                    else:
                         if mat[i][j] < 0:
                              if mat[i][j+1] < 0:
                                   ec = f"- {abs(mat[i][j])} x{j+1} "
                              else:
                                   ec = f"- {abs(mat[i][j])} x{j+1} + "
                         else:
                              if mat[i][j+1] < 0:
                                   ec = f"{mat[i][j]} x{j+1} "
                              else:
                                   ec = f"{mat[i][j]} x{j+1} + "
                    ecu += ec
               if i == 0:
                    print(f"\n{ecu}")
               else:
                    print(ecu)
               ecu = ""
     
     #mat = [[3,-.1,-.2,7.85],[.1,7,-.3,-19.3],[.3,-.2,10,71.4]]
          name = "Matriz"
          PrintMat(name,mat,c,f,cf)

          for i in range(d):
               g = 0
               for j in range(d):
                    if i != j:
                         g += abs(mat[i][j])
               h = mat[i][i]
               if h == 0:
                    print("\n\t┌──────────────────────────────────────────────────────────────────────────────┐")
                    print("  \t│  Error:  Hay un cero en la diagonal coloca las ecuaciones en otra posición.  │")
                    print("  \t└──────────────────────────────────────────────────────────────────────────────┘")
                    m = str(input("\n\t¿Deseas cambiar de posicion las ecuaciones? [si/no] »» "))
                    k = 2
                    break
               elif h < g:
                    print("\n\t┌────────────────────────────────────────────────────┐")
                    print("  \t│  Error:  La matriz no es diagonalmente dominante.  │")
                    print("  \t└────────────────────────────────────────────────────┘")
                    m = str(input("\n\t¿Deseas cambiar de posicion las ecuaciones? [si/no] »» "))
                    k = 3
                    break
               elif i == j:
                    m = str(input("- Observa la matriz - ¿Deseas cambiar los coeficientes? [si/no] »» "))
                    k = 0
                    break
               
     it = 0
     error = 0
     en = 0
     xr1 = []
     xr2 = []
     s = 0
     inter = 150
     while it <= inter and k != 2:
          if it == 0:
               print("{:^102}".format("╔════════════════════════════════════════════════════════════════════════════════════════════════════╗"))
               print("{:^1}{:^100}{:^1}".format("║","Metodo de Gauss Seidel","║"))
               print("{:^1}{:^11}{:^1}{:^72}{:^1}{:^15}{:^1}".format("╠","═══════════","╦","════════════════════════════════════════════════════════════════════════","╦","═══════════════","╣"))
               print("{:^1}{:^11}{:^1}{:^72}{:^1}{:^15}{:^1}".format("║","Iteracion","║","Solucion","║","Error","║"))
               print("{:^1}{:^11}{:^1}{:^72}{:^1}{:^15}{:^1}".format("╠","═══════════","╬","════════════════════════════════════════════════════════════════════════","╬","═══════════════","╣"))
               print("{:^1}{:^11}{:^1}{:^72}{:^1}{:^15}{:^1}".format("║",it,"║",f"{x}","║",trunc(10,error),"║"))
               it += 1
          
          xr1 = []
          for i in range(d):
               xr1.append(x[i])
          
          sol = 0
          a = 0
          for i in range(c):
               for j in range(f):
                    if i == j:
                         a = mat[i][j]
                    elif j == f-1:
                         b = mat[i][j]
                    else:
                         sol += (-1*mat[i][j])*x[j]
               if b != 0:
                    x[i] = (b+sol)/a
               else:
                    x[i] = sol/a
               sol = 0      
          
          xr2 = []
          for i in range(d):
               xr2.append(x[i])
          
          try:
               if it > 0:
                    xr = []
                    for i in range(d):
                         xr.append(xr2[i]-xr1[i])
                    error = NorVec(xr)/NorVec(xr2)
          except:
               k = 1
               break
          
          print("{:^1}{:^11}{:^1}{:^72}{:^1}{:^15}{:^1}".format("║",it,"║",f"{trunc(72//(d+5),x)}","║",trunc(10,error),"║"))

          it += 1
          
          if k == 0:
               l = 0
               for i in range(c):
                    for j in range(f-1):
                         sol += mat[i][j]*trunc(cf,x[j])
                    if trunc(cf,sol) == mat[i][f-1]:
                         l += 1
                    else:
                         l = 0
                    sol = 0     
          elif k == 3:
               l = 0
               for i in range(c):
                    for j in range(f-1):
                         sol += mat[i][j]*trunc(cf-2,x[j])
                    if trunc(cf-2,sol) == mat[i][f-1]:
                         l += 1
                    else:
                         l = 0
                    sol = 0    
          
          if l == d:
               break
          
          if error <= tol:
               s = 1
               break
          
          if it == 150:
               k = 1
               break
          
     if k == 0:
          print("{:^1}{:^11}{:^1}{:^72}{:^1}{:^15}{:^1}".format("╠","═══════════","╩","════════════════════════════════════════════════════════════════════════","╩","═══════════════","╣"))
          print("{:^1}{:^28}{:^72}{:^1}".format("║","Solucion aproximada ≈",f"{trunc(cf,x)}","║"))
          print("{:^102}".format("╚═══════════════════════════╦════════════════════════════════════════════════════════════════════════╣"))
          for i in range(d):
               print("{:^28}{:^1}{:^10}{:^62}{:^1}".format(" ","║",f"x{i} ≈",f"{trunc(cf,x[i])}","║"))
          print("{:^28}{:^74}".format(" ","╚════════════════════════════════════════════════════════════════════════╝"))
          if s == 1:
               print("{:^102}".format("╔════════════════════════════════════════════════════════════════════════════════════════════════════╗"))
               print("{:^1}{:^100}{:^1}".format("║","Paro por error","║"))
               print("{:^102}".format("╚════════════════════════════════════════════════════════════════════════════════════════════════════╝"))
     elif k == 1:
          print("{:^1}{:^11}{:^1}{:^72}{:^1}{:^15}{:^1}".format("╠","═══════════","╩","════════════════════════════════════════════════════════════════════════","╩","═══════════════","╣"))
          print("{:^1}{:^28}{:^72}{:^1}".format("║","Solucion aproximada ≈",f"{trunc(cf,x)}","║"))
          print("{:^102}".format("╚═══════════════════════════╦════════════════════════════════════════════════════════════════════════╣"))
          for i in range(d):
               print("{:^28}{:^1}{:^10}{:^62}{:^1}".format(" ","║",f"x{i} ≈",f"{trunc(cf,x[i])}","║"))
          print("{:^28}{:^74}".format(" ","╚════════════════════════════════════════════════════════════════════════╝"))
          print("{:^102}".format("╔════════════════════════════════════════════════════════════════════════════════════════════════════╗"))
          print("{:^1}{:^100}{:^1}".format("║","ADVERTENCIA PUEDE QUE ESTA NO SEA LA SOLUCION","║"))
          print("{:^1}{:^100}{:^1}".format("║","LA DIAGONAL DE LA MATRIZ NO ES DOMINANTE","║"))
          print("{:^102}".format("╚════════════════════════════════════════════════════════════════════════════════════════════════════╝"))
     elif k == 2:
          print("{:^102}".format("╔════════════════════════════════════════════════════════════════════════════════════════════════════╗"))
          print("{:^1}{:^100}{:^1}".format("║","ERROR HAY UN CERO EN LA DIAGONAL","║"))
          print("{:^102}".format("╚════════════════════════════════════════════════════════════════════════════════════════════════════╝"))
     elif k == 3:
          print("{:^1}{:^11}{:^1}{:^72}{:^1}{:^15}{:^1}".format("╠","═══════════","╩","════════════════════════════════════════════════════════════════════════","╩","═══════════════","╣"))
          print("{:^1}{:^28}{:^72}{:^1}".format("║","Solucion aproximada ≈",f"{trunc(cf,x)}","║"))
          print("{:^102}".format("╚═══════════════════════════╦════════════════════════════════════════════════════════════════════════╣"))
          for i in range(d):
               print("{:^28}{:^1}{:^10}{:^62}{:^1}".format(" ","║",f"x{i} ≈",f"{trunc(cf,x[i])}","║"))
          print("{:^28}{:^74}".format(" ","╚════════════════════════════════════════════════════════════════════════╝"))
          print("{:^102}".format("╔════════════════════════════════════════════════════════════════════════════════════════════════════╗"))
          print("{:^1}{:^100}{:^1}".format("║","ADVERTENCIA PUEDE QUE ESTA NO SEA LA SOLUCION","║"))
          print("{:^1}{:^100}{:^1}".format("║","LA DIAGONAL DE LA MATRIZ NO ES DOMINANTE","║"))
          print("{:^102}".format("╚════════════════════════════════════════════════════════════════════════════════════════════════════╝"))
     p = str(input("\n\t¿Deseas buscar la solucion a otro sistema de ecuaciones? [si/no] »» "))
     
