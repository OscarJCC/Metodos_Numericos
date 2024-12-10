"""
Nombre: Convertido de sistema Decimal a Binorio
Fecha Inicio: 17/08/2021
Fecha Final: 29/08/2021
Autor: Oscar Joel Castro Contreras
Descripcion:

"""
# FUNCIONES

# Funcion Dec_Bin:
def Dec_Bin(num):
     # Obtien la parte entera
     ent = int(num)
     
     if ent != 0:
          # Define si es negativo o positivo
          a = 0
          if ent < 0:
               ent = -1*ent
               a = 1
     
          # Obtiene los 1 y 0 y los guarda en una lista
          ndec = []
          while ent != 0:
               ndec.append(ent % 2)
               ent = ent // 2
     
          # Invierte el orden de los lista ndec
          nb = []
          for i in range(1,len(ndec)+1):
               nb.append(str(ndec[len(ndec)-i]))
     
          # Guarda la lista ndec en un str
          nbin = ""
          for i in range(len(nb)):
               nbin += (nb[i])
     
          #Retorna el resultado segun su signo
          if a == 1:
               return -1*int(nbin)
          else:
               return int(nbin)
     else:
          return 0
     
#FUBCIOB Decp_Binp
def Decp_Binp(num):
     # Define si es positivo o negativo y saca la parte decimal
     if num >= 0:
          decp = round(num - int(num),len(str(num)))
     else:
          num = -1*num
          decp = round(num - int(num),len(str(num)))
     
     if decp == 0.0:
          return ""
     else:
          # Obtiene los 1 y 0 y trunca el numero a 16 interaciones
          b = 1
          de = 0
          bind = []
          while b <= 16:
               de = decp*2
               if de == 0:
                    break
               else:
                    b += 1
               decp = round(de - int(de), len(str(decp)))
               bind.append(str(int(de)))
     
          # Guarda los 1 y 0 en str
          nbind = "."
          for i in range(len(bind)):
               nbind += (bind[i])
     
     #Retorna el resultado
     if b == 17:
          return nbind + "  >> Infinito"
     else:
          return nbind

#Funcion Dec_Oct:
def Dec_Oct(num):
     # Obtiene la parte entera
     ent = int(num)
     
     #define si el numero es mayor a 8
     if ent <=-8 or ent >= 8:
          
          #Define si es negativo
          a = 0
          if ent < 0:
               ent = -1*ent
               a = 1
          
          #Obtiene los numeros que represetan al numero octal
          i = 0
          no =[]
          while i == 0:
               d = ent // 8
               de = d * 8
               o =  ent - de
               ent = d
               no.append(o)
               if de == 0:
                    break
          
          # Acomda los numero representantes
          noc = []
          for i in range(1,len(no)+1):
               noc.append(str(no[len(no)-i]))
          
          # Guarda los numeros representantes en un str
          noct = ""
          for i in range(len(noc)):
               noct += (noc[i])
          
          # Retorna el resultado
          if a == 1:
               return -1*int(noct)
          else:
               return int(noct)
     else:
          return ent

#Funcion Decp_Octp:
def Decp_Octp(num):
     # Define si es positivo o negativo y saca la parte decimal
     if num > 0:
          de = round(num - int(num),len(str(num)))
     else:
          num = -1*num
          de = round(num - int(num),len(str(num)))

     #Covierte parte decimal a octal decimal
     i = 0
     oc = []
     while i <= 15:
          o = de*8
          oc.append(int(o))
          if round(o - int(o),len(str(o))) == 0:
               break
          else:
               de = round(o - int(o),len(str(o)))
               i += 1

     # Guarda los str
     octp = "."
     for i in range(len(oc)):
          octp += (str(oc[i]))
     
     #Retorna el resultado
     if i == 15:
          return octp + "  >> Infinito"
     else:
          return octp

# Funcion Bin_Dec:
def Bin_Dec(num):
     # Obtiene la parte entera
     ent = int(num)
     ent = str(ent)
     
     # Define si es positivo o negativo y conviete los 1 y 0 en int
     a = 0
     nb = []
     if int(ent) < 0:
          nbi = str(-1*int(ent))
          for i in range(len(nbi)):
               nb.append(int(nbi[i]))
          a = 1
     else:
          for i in range(len(ent)):
               nb.append(int(ent[i]))
     
     # Convierte el a numero decimal
     ndec = 0
     for i in range(0,len(nb)):
          ndec += nb[i] * (2)**((len(nb)-1)-i)
     
     # Retorna el resultado
     if a == 1:
          return -1*ndec
     else:
          return ndec

#FUNCION Binp_Decp:
def Binp_Decp(num):
     #Define si es negativo o positivo y saca parte decimal
     if num > 0:
          num = round(num - int(num),len(str(num)))
     else:
          num = -1*num
          num = round(num - int(num),len(str(num)))
          
     num = str(num)

     # Define si es positivo o negativo y convierte los 1 y 0 en float
     nb = []
     for i in range(2, len(num)):
          nb.append(float(num[i]))
     
     # Convierte el numero a decimal
     ndec = 0.0
     for i in range(len(nb)):
          ndec += (nb[i] * ((2)**(-(i+1))))

     # Guarda los 1 y 0 despues del punto en un str
     ndec = str(ndec)
     nbind = "."
     for i in range(2, len(ndec)):
          nbind += (ndec[i])
     
     # Retorna el resultado
     return nbind

#Funcion Bin_Oct:
def Bin_Oct(num):
     # Obtiene la parte entera
     ent = int(num)

     #Define si es negativo o positivo
     a = 0
     if ent < 0:
          ent = -1*ent
          a = 1

     # Define loq ue vale cada numero binario y octal
     dic = {
          0:0,1:1,10:2,11:3,100:4,101:5,110:6,111:7
          }

     # Convierte en lista el binario
     ent = list(str(ent))

     #Define cuantos dijitos tiene el binario
     if len(ent) > 3:
          e = len(ent)-3
     else:
          e = 0

     # Hace la convercion de binario a octal
     j = 0
     no = ""
     d = []
     while j == 0:
          # Divide y Extrae de 3 dijito en numero binario
          for i in range(e,len(ent)):
               d.append(int(ent[i]))

          # Convierte los 3 dijitos binarion en str
          nb = ""
          for i in range(len(d)):
               nb += str(d[i])
     
          # Conviete los 3 dijitos en un octal
          n = ""
          n = dic[int(nb)]
          no += str(n)
     
          # Ayuda a obtener los 3 digitos siguientes del numero binario
          del ent[e:len(ent)]
          del d[0:3]
          if len(ent) > 3:
               e -= 3
          else:
               e = 0
     
          # Termina el cuando ya se recorio todo en numero binario
          if ent == []:
               j = 1

     #Invierte los la lista noc
     noc = []
     for i in range(1,len(no)+1):
          noc.append(str(no[len(no)-i]))

     # Guarda en un str el otal
     noct = ""
     for i in range(len(noc)):
          noct+= (noc[i])

     # Retorna el resultado
     if a == 1:
          return -1*int(noct)
     else:
          return noct

#Funcion Binp_Octp:
def Binp_Octp(num):
     #Define si es negativo o positivo y saca parte decimal
     if num > 0:
          binp = round(num - int(num),len(str(num)))
     else:
          num = -1*num
          binp = round(num - int(num),len(str(num)))

     # Define lo ue vale cada numero binario y octal
     dic = {
          "0":0,"000":0,"00":0,"001":1,"01":2,"010":2,"011":3,
          "1":4,"100":4,"10":4,"101":5,"11":6,"110":6,"111":7
          }

     # Convierte en lista el binario
     binp = list(str(binp))
     bi = []
     for i in range(2,len(binp)):
          bi.append(int(binp[i]))

     #Define cuantos dijitos tiene el binario
     if len(bi) > 3:
          e = 3
     else:
          e = len(bi)
     
     # Hace la convercion de binario a octal
     j = 0
     no = ""
     d = []
     while j == 0:
          # Divide y Extrae de 3 dijito en numero binario
          for i in range(e):
               d.append(int(bi[i]))

          # Convierte los 3 dijitos binarion en str
          nb = ""
          for i in range(len(d)):
               nb += str(d[i])

          # Conviete los 3 dijitos en un octal
          n = ""
          n = dic[nb]
          no += str(n)
     
          # Ayuda a obtener los 3 digitos siguientes del numero binario
          del bi[0:e]
          del d[0:e]
          if len(bi) > 3:
               e = 3
          else:
               e = len(bi)
     
          # Termina el cuando ya se recorio todo en numero binario
          if bi == []:
               j = 1

     # Guarda en un str el otal
     noct = "."
     for i in range(len(no)):
          noct+= (no[i])

     # Retorna el resultado
     return noct

#Funcion Oct_Dec:
def Oct_Dec(num):
     # Obtie parte entera
     ent = int(num)
     
          #Define si es negativo o positivo
     a = 0
     if ent < 0:
          ent = -1*ent
          a = 1
          
     ent = list(str(ent))
     
     #Convierte elementos de lista en int
     noc = []
     for i in range(len(ent)):
          noc.append(int(ent[i]))

     #Convierte a decimal
     dec = 0
     for i in range(1,len(noc)+1):
          dec += noc[i-1] * ((8)**(len(noc)-i))

     #Retorna el resultado
     if a == 1:
          return -1*dec
     else:
          return dec

#Funcion Octp_Decp
def Octp_Decp(num):
     #Define si es negativo o positivo y saca parte decimal
     if num > 0:
          octp = round(num - int(num),len(str(num)))
     else:
          num = -1*num
          octp = round(num - int(num),len(str(num)))

     #Convierte los digitos en lista 
     oc = list(str(octp))
     de = []
     for i in range(2,len(str(octp))):
          de.append(int(oc[i]))

     #Transforma en octal
     decp = 0
     for i in range(1,len(de)+1):
          decp += (de[i-1]*((8)**(-i)))
     
     return decp

#Funcion Oct_Bin:
def Oct_Bin(num):
     # Obtiene la parte entera
     ent = int(num)
     
     #Define si es negativo
     a = 0
     if ent < 0:
          ent = -1*ent
          a = 1
          
     # Define lo que vale cada numero en binario
     dic = {
     "0":[0,0,0],"1":[0,0,1],"2":[0,1,0],"3":[0,1,1],
     "4":[1,0,0],"5":[1,0,1],"6":[1,1,0],"7":[1,1,1],
     }

     # Convierte el Octal en Binario
     bi = []
     for i in str(ent):
          bi += dic[i]

     # Guarada en str
     nbin = ""
     for i in range(len(bi)):
          nbin += (str(bi[i]))
     nbin = int(nbin)
     
     # Retorna el resultado
     if a == 1:
          return -1*nbin
     else:
          return nbin

#Funcion Octp_Binp:
def Octp_Binp(num):
     #Define si es negativo o positivo y saca parte decimal
     if num > 0:
          dec = round(num - int(num),len(str(num)))
     else:
          num = -1*num
          dec = round(num - int(num),len(str(num)))
          
     # Define lo que vale cada numero en binario
     dic = {
     "0":[0,0,0],"1":[0,0,1],"2":[0,1,0],"3":[0,1,1],
     "4":[1,0,0],"5":[1,0,1],"6":[1,1,0],"7":[1,1,1],
     }

     # COnvierte en lista
     dec = list(str(dec))
     
     #Extrae los numeros despues del punto
     decp = ""
     for i in range(2,len(dec)):
          decp += dec[i]
     
     # Convierte el Octal en Binario
     bi = []
     for i in str(decp):
          bi += dic[i]

     # Guarada en str
     nbin = "."
     for i in range(len(bi)):
          nbin += (str(bi[i]))
     nbin = float(nbin)
     
     # Retorna el resultado
     return nbin

print("""
      INSTRUCCIONES:
      Selecciona una de las opciones del menu segun lo que deseas realizar, coloca 
      el numero que le corresponde.
      El programa solo puede convertir entre Decimal, Binario y Octal, dependiendo 
      de la accion que elijas el programa convertira a las otras 2 bases restantes.""")

i = "si"
 
while i == "s" or i == "S" or i == "si" or i == "SI" or i == "Si" or i == "sI":
     
     print("""
           ╔═════════════════════════════════════╗
           ╠═════════════___MENU___══════════════╣
           ╠══ ► Convertir un Decimal_10 » 1 « ══╣
           ╠══ ► Convertir un Binario_2  » 2 « ══╣
           ╠══ ► Convertir un Octal_8    » 3 « ══╣
           ╚═════════════════════════════════════╝
          """)
     
     
     p = str(input("¿Que accion deseas realizar? »» "))
     
     if p != "1" and p != "2" and p != "3" and p != "N" and p != "n" and p != "NO" and p != "no" and p != "No" and p != "nO":
          print("\n\t┌────────────────────────────────────────────────────────────────────────────────────┐")
          print("  \t│  Error:  Desves colocar el numero que corresponde a la accion que deseas realizar  │")
          print("  \t└────────────────────────────────────────────────────────────────────────────────────┘")
          
     elif p == "1":
          try:
               num = float(input("\nEscribe el numero Decimal:\n\t"))
               print("\n\tForma Binaria: ",Dec_Bin(num),Decp_Binp(num),sep = "")
               print("\n\tForma Octal: ",Dec_Oct(num),Decp_Octp(num),sep = "")

          except ValueError:
               print("\n\t┌──────────────────────────────────┐")
               print("  \t│  Error:  Desves colocar numeros  │")
               print("  \t└──────────────────────────────────┘")
          except KeyError:
               print("\n\t┌───────────────────────┐")
               print("  \t│  Error:  De redondeo  │")
               print("  \t└───────────────────────┘")
               
     elif p == "2":
          try:
               num = float(input("\nEscribe el numero Binario:\n\t"))
               for i in str(num):
                    if i == "0" or i == "1" or i == "-" or i == '.' or i == "e":
                         v = True
                    elif i != "0" or i != "1":
                         v = False
                         break
               
               if v == True:
                    print("\n\tForma Decimal: ", Bin_Dec(num),Binp_Decp(num),sep = "")
                    print("\n\tForma Octal: ",Bin_Oct(num),Binp_Octp(num),sep = "")
               else:
                    print("\n\t┌───────────────────────────────────────────┐")
                    print("  \t│  Error:  Deves colocar un numero Binario  │")
                    print("  \t└───────────────────────────────────────────┘")
                    
          except ValueError:
               print("\n\t┌──────────────────────────────────┐")
               print("  \t│  Error:  Desves colocar numeros  │")
               print("  \t└──────────────────────────────────┘")
          except KeyError:
               print("\n\t┌───────────────────────┐")
               print("  \t│  Error:  De redondeo  │")
               print("  \t└───────────────────────┘")
               
     elif p == "3":
          try:
               num = float(input("\nEscribe el numero Octal:\n\t"))
               n = []    
               for i in str(num):
                    if i == '.' or i == "-" or i == "e":
                         n.append(i)
                    else:
                         n.append(int(i))

               for i in n:
                    if i == "-" or i == '.' or i == "e":
                         v = True
                    elif i >= 0 and i <= 7:
                         v = True
                    else:
                         v = False
                         break 
               
               if v == True:
                    print("\n\tForma Decimal: ",Oct_Dec(num)+Octp_Decp(num))
                    print("\n\tForma Binaria: ",Oct_Bin(num)+Octp_Binp(num))
               else:
                    print("\n\t┌─────────────────────────────────────────┐")
                    print("  \t│  Error:  Deves colocar un numero Octal  │")
                    print("  \t└─────────────────────────────────────────┘")
               
          except ValueError:
               print("\n\t┌──────────────────────────────────┐")
               print("  \t│  Error:  Desves colocar numeros  │")
               print("  \t└──────────────────────────────────┘")
          except KeyError:
               print("\n\t┌───────────────────────┐")
               print("  \t│  Error:  De redondeo  │")
               print("  \t└───────────────────────┘")
     
     elif p == "N" or p == "n" or p == "NO" or p == "no" or p == "No" or p == "nO":
          break
     
     i = str(input("\n¿Deseas convertir otro numero? [si/no] »» "))