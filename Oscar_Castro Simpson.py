
"""
Nombre: Simpson 1/3 y 3/8
Fecha Inicio:
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

"""

def F(ecuacion,x):
     pi = 3.141592653589793238  
     exp = 2.71828182845904523
     return eval(str(ecuacion))

print("""
                                        Simpson 1/3 y 3/8
      INSTRUCCIONES:
      
      Este programa usa el método de Simpson 1/3 y 3/8 para encontrar la solución a una integral 
      definida.
      
      El programa te pedirá colocar la función que dependa de (x), los limites inferior y superior 
      de la integral y un numero de intervalos en lo que quieres que se parta el área bajo la curva 
      de la función.""")

# ((exp**(x**(1/2)))*(((exp**(x**(1/2)))-1)**(1/2)))/(x**(1/2))

p = "si"
while p == "s" or p == "S" or p == "si" or p == "SI" or p == "Si" or p == "sI":
     
     ecu = str(input("\n\tColoca f(x) = "))
     
     a = float(input("\n\tLimite inferior (a): "))
     
     b = float(input("  \tLimite superior (b): "))
     
     i = 1
     while i == 1: 
          i = 0
          try:
               n = int(input("\n\tNumero de intervalos (n):"))
          except:
               print("\n\t┌─────────────────────────────────────────┐")
               print("  \t│  Error: (n) deve ser un numero entero.  │")
               print("  \t└─────────────────────────────────────────┘")
               i = 1
          
     if n % 2 == 0:
          h = (b-a)/n

          x = []
          for i in range(n+1):
               if i == 0:
                    x.append(a)
               else:
                    x.append(x[i-1] + h)

          s = 0
          for i in range(n+1):
               if i == 0:
                    s += F(ecu,x[i])
               elif i == n:
                    s += F(ecu,x[i])
               elif i % 2 == 0:
                    s += 2*F(ecu,x[i])
               elif i % 2 != 0:
                    s += 4*F(ecu,x[i])

          sol = (h/3)*s

          print("{:^49}".format("\n╔═══════════════════════════════════════════════╗"))
          print("{:^1}{:19}{:^25}{:^1}".format("║"," Solución aproximada ≈",sol,"║"))
          print("{:^49}".format("╚═══════════════════════════════════════════════╝"))
     
     elif n % 2 != 0:
          h = (b-a)/n

          x = []
          for i in range(n+1):
               if i == 0:
                    x.append(a)
               else:
                    x.append(x[i-1]+h)
          
          s1 = 0
          for i in range(n-2):
               if i == 0 or i == n-3:
                    s1 += F(ecu,x[i])
               elif i % 2 == 0:
                    s1 += 2*F(ecu,x[i])
               elif i % 2 != 0:
                    s1 += 4*F(ecu,x[i])

          sol1 = ((x[n-3]-a)/(3*(n-3)))*s1
          
          s2 = 0
          for i in range(n-3,n+1):
               if i == n-3 or i == n:
                    s2 += F(ecu,x[i])
               else:
                    s2 += 3*F(ecu,x[i])

          sol2 = ((b-x[n-3])/8)*s2
          
          sol = sol1 + sol2
          
          print("{:^49}".format("\n╔═══════════════════════════════════════════════╗"))
          print("{:^1}{:19}{:^25}{:^1}".format("║"," Solución aproximada ≈",sol,"║"))
          print("{:^49}".format("╚═══════════════════════════════════════════════╝"))
          
     p = str(input("\n\t¿Deseas buscar la integral definida de otra función? [si/no] »» "))