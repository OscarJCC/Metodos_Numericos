"""
Nombre: Guass
Fecha Inicio: 17/10/2021
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

"""

def trunc(cf,num):
     #n = str(round(float(num)),cf)
     n = str(num)

     if type(num) == complex:
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

def PrintMat(matriz,c,f,cf):
     if cf > 14:
          print("\nMatriz:\n")
          for i in range(c):
               for j in range(f):
                    if j == f-1:
                         print("{:^3}{:^24}".format(" ¦ ",trunc(cf,matriz[i][j])),end=" ")
                    else:
                         print("{:^24}".format(trunc(cf,matriz[i][j])),end=" ")
               print("\n")
     else:
          print("\nMatriz:\n")
          for i in range(c):
               for j in range(f):
                    if j == f-1:
                         print("{:^3}{:^14}".format(" ¦ ",trunc(cf,matriz[i][j])),end=" ")
                    else:
                         print("{:^14}".format(trunc(cf,matriz[i][j])),end=" ")
               print("\n")

f = int(input("\n\tNumero de Variables  :"))+1
c = int(input("  \tNumero de Ecuaciones :"))

cf = int(input("\n\tCifras significativas:"))
tol = 10**(-1*(cf))

ecu= ""
for i in range(c):
     for j in range(f):
          if j >= f-1:
               ec = f"= (C{i}{j})"
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
          if i == 0 and j == 0:
               m = float(input(f"\nC{i}{j} = "))
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
               ec = f"{mat[i][j]} x{j+1} "
          else:
               ec = f"{mat[i][j]} x{j+1} + "
          ecu += ec
     if i == 0:
          print(f"\n{ecu}")
     else:
          print(ecu)
     ecu = ""

PrintMat(mat,c,f,cf)

v = 0
u = 0
while u < c and v < f-1:
     l = mat[v][u]
     if l == 0:
          break
     elif l != 0 and l != 1:
          for j in range(v,f):
               #print(f"{mat[v][j]} = {mat[v][j]}/{l}")
               mat[v][j] =  mat[v][j]/l
          
     PrintMat(mat,c,f,cf)

     u += 1
     while u < c:
          for i in range(u,c):
               l = mat[u][v]
               for j in range(v,f):
                    #print(f"{mat[i][j]} = {mat[i][j]} + (-1*{l})*{mat[v][j]}")
                    mat[i][j] = mat[i][j] + (-1*l)*mat[v][j]
               u += 1
          
     
     PrintMat(mat,c,f,cf)
          
     v += 1
     u = v
     

print("\n--- SCD ---")
print("SOLUCION:")
for i in range(f-1):
     print(f"x{i+1} = ", mat[i][f-1])