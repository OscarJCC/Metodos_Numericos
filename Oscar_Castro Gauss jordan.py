"""
Nombre: Gauss Jordan
Fecha Inicio: 18/10/2021
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

"""       
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
     if cf > 5:
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

print("""
                                        Gauss Jordan
      INSTRUCCIONES:
      Este programa usa el método de Gauss Jordán para encontrar la solución a cualquier 
      sistema de ecuaciones. Al llenar la matriz debes tomar en cuenta que no puede a ver 
      ceros en la diagonal.""")

p = "si"
while p == "s" or p == "S" or p == "si" or p == "SI" or p == "Si" or p == "sI":
     i = 0
     Z = "n"
     while i == 0:
          f = int(input("\n\tNumero de Variables  :"))+1
          c = int(input("  \tNumero de Ecuaciones :"))
               
          cf = int(input("\n\tCifras significativas:"))
          tol = 10**(-1*(cf))
          """
          except:
               print("\n\t┌───────────────────────────┐")
               print("  \t│  Error:  Coloca numeros.  │")
               print("  \t└───────────────────────────┘")
               z = str(input("\n\t¿Deseas intentar de nuevo?[si/no] »» "))
               if z == "s" or z == "S" or z == "si" or z == "SI" or z == "Si" or z == "sI":
                    i = 0
               else:
                    FIN
          """          
          if f-1 == 0 or f-1 == 1:
               print("\n\t┌─────────────────────────────────────────────────┐")
               print("  \t│  Error:  Colocaste muy pocas variables [ +1 ].  │")
               print("  \t└─────────────────────────────────────────────────┘")
               z = str(input("\n\t¿Deseas intentar de nuevo?[si/no] »» "))
               if z == "s" or z == "S" or z == "si" or z == "SI" or z == "Si" or z == "sI":
                    i = 0
               else:
                    FIN
                    
          elif c == 0 or c == 1:
               print("\n\t┌──────────────────────────────────────────────────┐")
               print("  \t│  Error:  Colocaste muy pocas ecuaciones [ +1 ].  │")
               print("  \t└──────────────────────────────────────────────────┘")
               z = str(input("\n\t¿Deseas intentar de nuevo?[si/no] »» "))
               if z == "s" or z == "S" or z == "si" or z == "SI" or z == "Si" or z == "sI":
                    i = 0
               else:
                    FIN
          elif c < 0  or f < 0 or cf < 0:
               print("\n\t┌────────────────────────────────────────────────────────────────┐")
               print("  \t│  Error:  Colocaste un numero negativo, coloca solo positivos.  │")
               print("  \t└────────────────────────────────────────────────────────────────┘")
               z = str(input("\n\t¿Deseas intentar de nuevo?[si/no] »» "))
               if z == "s" or z == "S" or z == "si" or z == "SI" or z == "Si" or z == "sI":
                    i = 0
               else:
                    FIN
          else:
               i = 1
     
     i = 0
     while i == 0:
          N = ""
          print("""
            ╔════════════════════╗   ╔═══════════════════════╗
           ═╣ R = Numeros Reales ╠═══╣ C = Numeros complejos ╠═
            ╚════════════════════╝   ╚═══════════════════════╝""")
     
          N = str(input("\n\t¿Que tipo de numeros usaras?[R/C] »» "))
          """
          except:
               print("\n\t┌─────────────────────────────────┐")
               print("  \t│  Error:  Coloca una [R/r/C/c].  │")
               print("  \t└─────────────────────────────────┘")
               z = str(input("\n\t¿Deseas intentar de nuevo?[si/no] »» "))
               if z == "s" or z == "S" or z == "si" or z == "SI" or z == "Si" or z == "sI":
                    i = 0
               else:
                    FIN
          """          
          if N == "R" or N == "r":
               i = 1
               C = 0
          elif N == "C" or N == "c":
               C = 1
               i = 1
          else:
               print("\n\t┌─────────────────────────────────┐")
               print("  \t│  Error:  Coloca una [R/r/C/c].  │")
               print("  \t└─────────────────────────────────┘")
               z = str(input("\n\t¿Deseas intentar de nuevo?[si/no] »» "))
               if z == "s" or z == "S" or z == "si" or z == "SI" or z == "Si" or z == "sI":
                    i = 0
               else:
                    FIN
     
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

          if N == "R" or N == "r":
               ma = []
               mat = []
               for i in range(c):
                    for j in range(f):
                         if j == 0:
                              m = float(input(f"\nC{i}{j} = "))
                         elif j >= f-1:
                              m = float(input(f"S{i+1} = "))
                         else:
                              m = float(input(f"C{i}{j} = "))
                         ma.append(m)
                    mat.append(ma)
                    ma = []
                    print(mat)
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
               
          elif N == "C" or N == "c":
               ma = []
               mat = []
               for i in range(c):
                    for j in range(f):
                         if j == 0:
                              m = complex(input(f"\nC{i}{j} = "))
                         elif j >= f-1:
                              m = complex(input(f"S{i+1} = "))
                         else:
                              m = complex(input(f"C{i}{j} = "))
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
          
          name = "Matriz"
          PrintMat(name,mat,c,f,cf)
          
          for i in range(c-1):
               b = mat[i][i]
               if b == 0:
                    break
          
          if b == 0:
               print("\n\t┌──────────────────────────────────────────────────────────────────────────────┐")
               print("  \t│  Error:  Hay un cero en la diagonal coloca las ecuaciones en otra posición.  │")
               print("  \t└──────────────────────────────────────────────────────────────────────────────┘")
               m = str(input("\t\n¿Deseas cambiar de posicion las ecuaciones? [si/no] »»"))
          else:
               m = str(input("- Observa la matriz - ¿Deseas cambiar los coeficientes? [si/no] »» "))
          
     v = 0
     u = 0
     s = 0
     while u < c and v < f-1:
          
          l = mat[v][u]
          #print(f"---  {l}  ---")
          if l == 0 and mat[v][u+1] != 0 and u != f-1 and u != f-2:
               u += 1
               l = mat[v][u]
               s = 1
               for j in range(v,f):
                    #print(f"{mat[v][j]} = {mat[v][j]}/{l}")
                    mat[v][j] =  mat[v][j]/l
          elif l == 0:
               break
          elif l != 0 and l != 1:
               for j in range(v,f):
                    #print(f"{mat[v][j]} = {mat[v][j]}/{l}")
                    mat[v][j] =  mat[v][j]/l
          
          PrintMat(name,mat,c,f,cf)
     
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
                         #print(f"---  {l}  ---")
                         for j in range(v,f):
                              #print(f"{mat[i][j]} = {mat[i][j]} + (-1*{l})*{mat[v][j]}")
                              mat[i][j] = mat[i][j] + (-1*l)*mat[v][j]
                         u += 1
                         #print(f"-- {u} -- {v} --")
          
               elif u != 1 and s != 1:
                    u = 0
                    for i in range(u,c):
                         if u != v:
                              l = mat[u][v]
                              #print(f"---  {l}  ---")
                              for j in range(v,f):
                                   #print(f"{mat[i][j]} = {mat[i][j]} + (-1*{l})*{mat[v][j]}")
                                   mat[i][j] = mat[i][j] + (-1*l)*mat[v][j]
                         u += 1
                         #print(f"-- {u} -- {v} --")
               
               elif s == 1 and u != 1:
                    u = 0
                    v += 1
                    for i in range(u,c):
                         if u != v-1:
                              l = mat[u][v]
                              #print(f"---  {l}  ---")
                              for j in range(v,f):
                                   #print(f"{mat[i][j]} = {mat[i][j]} + (-1*{l})*{mat[v][j]}")
                                   mat[i][j] = mat[i][j] + (-1*l)*mat[v-1][j]
                         u += 1
                         #print(f"-- {u} -- {v} --")
          
          PrintMat(name,mat,c,f,cf)
     
          v += 1
          u = v
          #print(f"\n\n-- {u} -- {v} --\n\n")
     name = "Matriz Reducida"
     PrintMat(name,mat,c,f,cf)
     
     a = 0
     if c == f-1 or c > f-1:
          for i in range(c-1):
               for j in range(f-2):
                    a += mat[i][j]
               if a == 0 and mat[i][f-1] != 0:
                    a = mat[c-1][f-1]
                    break
               #elif mat[i][j]
               a = 0
     
     l = 0
     if a != 0:
          print("╔═══════════════════════╗")
          print("║ SISTEMA INDETERMINADO ║")
          print("╚═══════════════════════╝")
          print(f"{0.0} != {a}")
     elif s == 1:
          print("╔═══════════════════════════════════╗")
          print("║ SISTEMA CONSISTENTE INDETERMINADO ║")
          print("╚═══════════════════════════════════╝")
     elif c < f-1:
          print("╔═══════════════════════════════════╗")
          print("║ SISTEMA CONSISTENTE INDETERMINADO ║")
          print("╚═══════════════════════════════════╝")
          if C == 0:
               ecu= ""
               for i in range(c):
                    for j in range(f):
                         if j == f-1:
                              if mat[i][j] == 0:
                                   ec = f"{mat[i][j]}"
                              elif l == 1:
                                   ec = f"{trunc(cf,mat[i][j])}"
                                   l = 0
                              elif mat[i][j] > 0:
                                   ec = f"+ {trunc(cf,mat[i][j])}"
                              else:
                                   ec = f"- {abs(trunc(cf,mat[i][j]))}"
                         elif j == f-2:
                              if mat[i][j] == 0:
                                   ec = ""
                              elif l == 1:
                                   ec = f"{trunc(cf,-1*mat[i][j])} x{j+1} "
                                   l = 0
                              elif -1*mat[i][j] > 0:
                                   ec = f"+ {trunc(cf,-1*mat[i][j])} x{j+1} "
                              else:
                                   ec = f"- {abs(trunc(cf,mat[i][j]))} x{j+1} "
                         elif i == j and mat[i][j] == 1:
                              ec = f"x{j+1} = "
                         elif mat[i][j] == 0:
                                   ec = ""
                         elif -1*mat[i][j] == 1:
                              if j == f-2:
                                   ec = f"x{j+1} "
                              elif l != 0:
                                   ec = f"x{j+1} + "
                         elif -1*mat[i][j] == -1:
                              if j == f-2:
                                   ec = f"- x{j+1} "
                              else:
                                   ec = f"- x{j+1} + "
                         else:
                              if mat[i][j] == 0:
                                   ec = ""
                              elif j == f-3:
                                   if -1*mat[i][f-2] > 0: 
                                        ec = f"{trunc(cf,-1*mat[i][j])} x{j+1} + "
                                        l = 1
                                   else:
                                        ec = f"{trunc(cf,-1*mat[i][j])} x{j+1} "
                                        l = 0
                              else:
                                   ec = f"{trunc(cf,-1*mat[i][j])} x{j+1} "
                                   l = 0
                         ecu += ec
                    if i == 0:
                         print(f"\n{ecu}")
                    else:
                         print(ecu)
                    ecu = ""
                    
          for i in range(c,f-1):
               ec = f"x{i+1} = x{i+1}"
               print(ec)
          
     elif c > f-1:
          print("╔═════════════════════════════════╗")
          print("║ SISTEMA CONSISTENTE DETERMINADO ║")
          print("╚═════════════════════════════════╝")
          print("SOLUCION:")
          for i in range(f-1):
               print(f"x{i+1} = ",trunc(cf,mat[i][f-1]))
               
     elif c == f-1:
          for i in range(c):
               if mat[i][i] == 1:
                    l = 0
               elif mat[i][i] == 0 and mat[i][i+1] != 0:
                    l = 1
               else:
                    l = 2
          if l == 0:
               print("╔═════════════════════════════════╗")
               print("║ SISTEMA CONSISTENTE DETERMINADO ║")
               print("╚═════════════════════════════════╝")
               print("SOLUCION:")
               for i in range(f-1):
                    print(f"x{i+1} = ",trunc(cf,mat[i][f-1]))
          elif l == 1:
               print("╔═══════════════════════╗")
               print("║ SISTEMA INDETERMINADO ║")
               print("╚═══════════════════════╝")
               print(f"{mat[c-1][f-2]} != {mat[c-1][f-1]}")
          elif l == 2:
               print("╔═══════════════════════════════════╗")
               print("║ SISTEMA CONSISTENTE INDETERMINADO ║")
               print("╚═══════════════════════════════════╝")
               if C == 0:
                    ecu= ""
                    for i in range(c):
                         for j in range(f):
                              if i == j and mat[i][j] == 0 and mat[i][j+1] == 0:
                                   ec = f"x{j+1} = x{j+1}"
                              elif i == j and mat[i][j] != 1:
                                   if mat[i][j] >= 0:
                                        ec = f"+ {mat[i][j]} x{j+1} = "
                                   elif mat[i][j] < 0:
                                        ec = f"- {abs(mat[i][j])} x{j+1} = "
                              elif j == f-1:
                                   if mat[i][j] == 0:
                                        ec = ""
                                   elif l == 1:
                                        ec = f"{trunc(cf,mat[i][j])}"
                                        l = 0
                                   elif mat[i][j] > 0:
                                        ec = f"+ {trunc(cf,mat[i][j])}"
                                   else:
                                        ec = f"- {abs(trunc(cf,mat[i][j]))}"
                              elif j == f-2:
                                   if mat[i][j] == 0:
                                        ec = ""
                                   elif l == 1:
                                        ec = f"{trunc(cf,-1*mat[i][j])} x{j+1} "
                                        l = 0
                                   elif -1*mat[i][j] > 0:
                                        ec = f"+ {trunc(cf,-1*mat[i][j])} x{j+1} "
                                   else:
                                        ec = f"- {abs(trunc(cf,mat[i][j]))} x{j+1} "
                              elif i == j and mat[i][j] == 1:
                                   ec = f"x{j+1} = "
                              elif mat[i][j] == 0:
                                   ec = ""
                              elif -1*mat[i][j] == 1:
                                   if j == f-2:
                                        ec = f"x{j+1} "
                                   elif l != 0:
                                        ec = f"x{j+1} + "
                              elif -1*mat[i][j] == -1:
                                   if j == f-2:
                                        ec = f"- x{j+1} "
                                   else:
                                        ec = f"- x{j+1} + "
                              else:
                                   if mat[i][j] == 0:
                                        ec = ""
                                   elif j == f-3:
                                        if mat[i][f-3] > 0: 
                                             ec = f"{trunc(cf,-1*mat[i][j])} x{j+1} "
                                             l = 1
                                        else:
                                             ec = f"- {abs(trunc(cf,-1*mat[i][j]))} x{j+1} "
                                             l = 0
                                   else:
                                        if mat[i][j] < 0:
                                             ec = f"- {abs(trunc(cf,-1*mat[i][j]))} x{j+1} "
                                             l = 0
                                        else:
                                             ec = f"+ {trunc(cf,-1*mat[i][j])} x{j+1} "
                                             l = 0
                              ecu += ec
                         if i == 0:
                              print(f"\n{ecu}")
                         else:
                              print(ecu)
                         ecu = ""

     p = str(input("\n\t¿Deseas buscar la solucion a otro sistema de ecuaciones? [si/no] »» "))