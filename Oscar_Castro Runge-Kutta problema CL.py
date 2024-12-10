"""
Nombre: Runge-Kutta
Fecha Inicio:
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

"""

import numpy as np
import matplotlib.pyplot as plt

def F(ecuacion,y):
     g = 9.81
     pi = 3.141592653589793238  
     exp = 2.71828182845904523
     return eval(str(ecuacion))

def F3(ecuacion,v,y,t):
     g = 9.81
     pi = 3.141592653589793238  
     exp = 2.71828182845904523
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
                                   Runge-Kutta problema de ejemplo:
      INSTRUCCIONES:
      Haz un programa que calcule la posición y de un objeto en caída libre:
      
                                        dy^2
                                        ──── = -g
                                         dt
                                         
      Tomando la ecuación diferencial y definiendo vy = dy/dt, la convertimos en el siguiente sistema 
      de ecuaciones diferenciales
      
                                    dy                  dv_y
                                    ── = vy ,           ──── = -g
                                    dt                   dt
                                    
      En los problemas anteriores únicamente se considera una ecuación diferencial, en esta tenemos dos,
      dado que la ecuación diferencial es de segundo orden. Para resolver de manera númerica lo único 
      que se debe hacer es resolver las ecuaciones al mismo tiempo y encontrar vy y y. camion
      y0 = 100
      v0 = 0
      t0 = 0
      tf = 10
      h = Tamaño de paso
      """)

p = "si"
while p == "s" or p == "S" or p == "si" or p == "SI" or p == "Si" or p == "sI":
          
     y0 = float(input("\n\t y(0) = "))
     
     v0 = float(input("\n\t v(0) = "))
     
     t0 = float(input("\n\t t_0 = "))
     
     tf = float(input("\n\t t_f = "))
     
     h = float(input("\n\t h = "))
     
     fv = -9.81
     fy = "v"
     t = t0
     v = v0
     y = y0
     vl = []
     yl = []
     tl = []
     hv = []
     hy = [] 
     while t < tf:
          
          if t == t0:
               print("{:^63}".format("╔═════════════════════════════════════════════════════════════╗"))
               print("{:^1}{:^61}{:^1}".format("║","RK4","║"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^24}{:^1}".format("╠","═══════════","╦","════════════════════════","╦","════════════════════════","╣"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^24}{:^1}".format("║","t -> (s)","║","v -> (m/s)","║","y -> (m)","║"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^24}{:^1}".format("╠","═══════════","╬","════════════════════════","╬","════════════════════════","╣"))
               print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^24}{:^1}".format("║",round(float(t),4),"║",v,"║",y,"║"))
               vl.append(v)
               yl.append(y)
               tl.append(t)
               hv.append(-9.81*t)
               hy.append((-4.905*(t**2)) + 100)

          k1 = h*F3(fv,v,y,t)
          l1 = h*F3(fy,v,y,t)
          
          k2 = h*F3(fv,v+(k1/2),y+(l1/2),t+(h/2))
          l2 = h*F3(fy,v+(k1/2),y+(l1/2),t+(h/2))
          
          k3 = h*F3(fv,v+(k2/2),y+(l2/2),t+(h/2))
          l3 = h*F3(fy,v+(k2/2),y+(l2/2),t+(h/2))
          
          k4 = h*F3(fv,v+k3,y+l3,t+h)
          l4 = h*F3(fy,v+k3,y+l3,t+h)
          
          v = v + ((k1+(2*k2)+(2*k3)+k4)/6)
          y = y + ((l1+(2*l2)+(2*l3)+l4)/6)
          
          vl.append(v)
          yl.append(y)
          tl.append(t)
          hv.append(-9.81*t)
          hy.append((-4.905*(t**2)) + 100)
          
          t += h
          
          print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^24}{:^1}".format("║",round(float(t),4),"║",v,"║",y,"║"))
     
     print("{:^1}{:^11}{:^1}{:^24}{:^1}{:^24}{:^1}".format("╚","═══════════","╩","════════════════════════","╩","════════════════════════","╝"))
     
     archivo = open("RungeKutta.txt","w")
     archivo.write("vl   ,  yl\n")
     A = len(vl)
     for i in range(A):
          archivo.write(f"{vl[i]}  ,    ")
          archivo.write(f"{yl[i]}\n")
     archivo.close()
     
     #Grafica
     G = str(input("\n\t¿Deseas que se graficar? [si/no] »» "))
     if G == "s" or G == "S" or G == "si" or G == "SI" or G == "Si" or G == "sI":
          k = np.linspace(-1000,1000,100001)
          g = [0]*100001
               
          h = []
          for i in k:
               u = F(fy,i)
               h.append(u)
          
          plt.style.use("dark_background") 
          fig, ax = plt.subplots()
          ax.set_title("Runge-Kutta")
          ax.plot(k,g,color="red")
          ax.plot(g,k,color="red")
          ax.plot(tl,vl,color="blue",label=f"$f(x) = dvy/dt = -g$")
          ax.plot(tl,yl,color="Turquoise",label=f"$f(x) = dy/dt = vy$")
          ax.plot(tl,hv,color="green",label=f"$vy = -9.81*t$")
          ax.plot(tl,hy,color="purple",label=f"$y = -4.905*t^2 + 100$")
          limx = OrCre(tl)
          limy = OrCre(yl)
          d = len(vl)
     
          if limx[0] > 100 or limx[d-1] > 100 or limx[0] < -100 or limx[d-1] < -100:
               ax.set_xlim(limx[0]-10,limx[d-1]+10)
          else:
               ax.set_xlim(limx[0]-1,limx[d-1]+1)
               
          if limy[0] > 100 or limy[d-1] > 100 or limy[0] < -100 or limy[d-1] < -100:
               ax.set_ylim(limy[0]-10,limy[d-1]+10)
          else:
               ax.set_ylim(limy[0]-1,limy[d-1]+1)
          ax.legend()
          plt.show()
     
     p = str(input("\n\t¿Deseas evaluar con otras condiciones iniciales? [si/no] »» "))