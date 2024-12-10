from tkinter import *
from tkinter import messagebox

#-------------------------------Funciones--------------------------------------

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

#---------------------Creacion de ventana--------------------------
raiz = Tk()
raiz.iconbitmap("C:\\Users\\HP\\OneDrive\\Documentos\\Programacion\\Python\\Interfaces Grafica\\CodePython.ico")
raiz.resizable(False,False)
raiz.title("Calculadora_IntGrafic_Completa")

     #---------------------------------Menu---------------------------------------
     
     #----------------------------Funciones para menu-----------------------------

def InfoAcercaDe():
     messagebox.showinfo("Creador", "Oscar Joel Castro Contreras\n------ Ingeniero Fisico -------")
     
def AccionSalir():
     v = messagebox.askokcancel("Salir", "¿Deseas salir de la aplicacion?")
     if v == True:
          raiz.destroy()

def InfoProducto():
     messagebox.showinfo("Producto", "Convertidor de bases")
     

     #------------------------Variables Para Barra De Menu-----------------------------------

BarraMenu = Menu(raiz, bg = "blue", fg = "#03f943")
raiz.config(menu = BarraMenu)

     #----------------------Variables Dentro De La Barra de Menu----------------------
          
          #--- Opcion Informacion En El Menu ----------------------
InformacionMenu = Menu(BarraMenu, tearoff = 0, background = "black", fg = "#03f943")
BarraMenu.add_cascade(label = "INFORMACION", menu = InformacionMenu)

               #--- Subopciones De Informacion---------------------
InformacionMenu.add_command(label = "Acerca de...", command = InfoAcercaDe)
InformacionMenu.add_command(label = "Producto", command = InfoProducto)
InformacionMenu.add_command(label = "Salir", command = AccionSalir)

#---------------Creacion del cuadro de la ventana o widget------------------
frame = Frame(raiz)
frame.pack(fill = "none", expand = "True")
frame.config(bg = "black")

#-------------------------Variables Para Botones--------------------------------

NumP = StringVar()

NumBin = StringVar()

NumOct = StringVar()

NumDec = StringVar()

RBOpcion = IntVar()

#-------------------------Variables globales-------------------------------------

Op = ""

Resultado = 0

TOp = ""

P = 0

#------------------------Introduccion de texto---------------------------------

#-- Fila 1
OpElegida = Label(frame)
OpElegida.grid(row = 1, column = 1, padx =3, pady = 3, columnspan = 4)
OpElegida.config(text = "Convertidor De Bases:", bg = "black", fg = "#03f943")

OpEl = Label(frame)
OpEl.grid(row = 5, column = 1, padx = 3, pady = 3, columnspan = 4)
OpEl.config(text = "Deves Elige Una Base",bg = "black", fg = "#03f943")


#-------------------------Introduccion de una imagen-------------------

#----------------------Creacion de cuadro de texto-------------------------

#-- Fila 6
Pantalla = Entry(frame, textvariable = NumP)
Pantalla.grid(row = 6, column = 2, padx = 0, pady = 0, columnspan = 3)                                                         
Pantalla.config(background = "black", fg = "#03f943", justify = "center")

#-- Fila 2
PantallaBin = Entry(frame, textvariable = NumBin)
PantallaBin.grid(row = 2, column = 2, padx = 1, pady = 1, columnspan = 2)                                                         
PantallaBin.config(background = "black", fg = "#03f943", justify = "center")

#-- Fila 3
PantallaOct = Entry(frame, textvariable = NumOct)
PantallaOct.grid(row = 3, column = 2, padx = 1, pady = 1, columnspan = 2)                                                         
PantallaOct.config(background = "black", fg = "#03f943", justify = "center")

#-- Fila 4
PantallaDec = Entry(frame, textvariable = NumDec)
PantallaDec.grid(row = 4, column = 2, padx = 1, pady = 1, columnspan = 2)                                                         
PantallaDec.config(background = "black", fg = "#03f943", justify = "center")

#--------------------------Funciones Para Botones-----------------------------

def OpcionesRadBut():
     
     if RBOpcion.get() == 1:
          OpElegida.config(text = "Esta Seleccionada La Base (Bin)")
          OpEl.grid(row = 5, column = 1, padx = 3, pady = 3, columnspan = 4)
          OpEl.config(text = "Solo Puedes Colocar Numeros\nDe Base (Bin)")
          
          Boton7 = Button(frame, text = "", width = "7")
          Boton7.grid(row = 7, column = 1, padx = 1, pady = 1)
          Boton7.config(fg = "black", bg = "black")
          
          Boton8 = Button(frame, text = "", width = "7")
          Boton8.grid(row = 7, column = 2, padx = 1, pady = 1)
          Boton8.config(fg = "black", bg = "black")

          Boton9 = Button(frame, text = "", width = "7")
          Boton9.grid(row = 7, column = 3, padx = 1, pady = 1)
          Boton9.config(fg = "black", bg = "black")
          
          Boton4 = Button(frame, text = "4", width = "7")
          Boton4.grid(row = 8, column = 1, padx = 1, pady = 1)
          Boton4.config(fg = "black", bg = "black")

          Boton5 = Button(frame, text = "5", width = "7")
          Boton5.grid(row = 8, column = 2, padx = 1, pady = 1)
          Boton5.config(fg = "black", bg = "black")

          Boton6 = Button(frame, text = "6", width = "7")
          Boton6.grid(row = 8, column = 3, padx = 1, pady = 1)
          Boton6.config(fg = "black", bg = "black")
          
          Boton2 = Button(frame, text = "2", width = "7")
          Boton2.grid(row = 9, column = 2, padx = 1, pady = 1)
          Boton2.config(fg = "black", bg = "black")

          Boton3 = Button(frame, text = "3", width = "7")
          Boton3.grid(row = 9, column = 3, padx = 1, pady = 1)
          Boton3.config(fg = "black", bg = "black")
          
     elif RBOpcion.get() == 2:
          OpElegida.config(text = "Esta Seleccionada La Base (Oct)")
          OpEl.grid(row = 5, column = 1, padx = 3, pady = 3, columnspan = 4)
          OpEl.config(text = "Solo Puedes Colocar Numeros\nDe Base (Oct)")

          Boton7 = Button(frame, text = "7", width = "7", command = lambda:NumPantalla(7))
          Boton7.grid(row = 7, column = 1, padx = 1, pady = 1)
          Boton7.config(fg = "#03f943", bg = "black")
          
          Boton8 = Button(frame, text = "", width = "7")
          Boton8.grid(row = 7, column = 2, padx = 1, pady = 1)
          Boton8.config(fg = "black", bg = "black")

          Boton9 = Button(frame, text = "", width = "7")
          Boton9.grid(row = 7, column = 3, padx = 1, pady = 1)
          Boton9.config(fg = "black", bg = "black")
          
          Boton4 = Button(frame, text = "4", width = "7", command = lambda:NumPantalla(4))
          Boton4.grid(row = 8, column = 1, padx = 1, pady = 1)
          Boton4.config(fg = "#03f943", bg = "black")
          
          Boton5 = Button(frame, text = "5", width = "7", command = lambda:NumPantalla(5))
          Boton5.grid(row = 8, column = 2, padx = 1, pady = 1)
          Boton5.config(fg = "#03f943", bg = "black")
          
          Boton6 = Button(frame, text = "6", width = "7", command = lambda:NumPantalla(6))
          Boton6.grid(row = 8, column = 3, padx = 1, pady = 1)
          Boton6.config(fg = "#03f943", bg = "black")
          
          Boton2 = Button(frame, text = "2", width = "7", command = lambda:NumPantalla(2))
          Boton2.grid(row = 9, column = 2, padx = 1, pady = 1)
          Boton2.config(fg = "#03f943", bg = "black")

          Boton3 = Button(frame, text = "3", width = "7", command = lambda:NumPantalla(3))
          Boton3.grid(row = 9, column = 3, padx = 1, pady = 1)
          Boton3.config(fg = "#03f943", bg = "black")
          
     elif RBOpcion.get() == 3:
          OpElegida.config(text = "Esta Seleccionada La Base (Dec)")
          OpEl.grid(row = 5, column = 1, padx = 3, pady = 3, columnspan = 4)
          OpEl.config(text = "Solo Puedes Colocar Numeros\nDe Base (Dec)")
          
          Boton7 = Button(frame, text = "7", width = "7", command = lambda:NumPantalla(7))
          Boton7.grid(row = 7, column = 1, padx = 1, pady = 1)
          Boton7.config(fg = "#03f943", bg = "black")
          
          Boton8 = Button(frame, text = "8", width = "7", command = lambda:NumPantalla(8))
          Boton8.grid(row = 7, column = 2, padx = 1, pady = 1)
          Boton8.config(fg = "#03f943", bg = "black")
          
          Boton9 = Button(frame, text = "9", width = "7", command = lambda:NumPantalla(9))
          Boton9.grid(row = 7, column = 3, padx = 1, pady = 1)
          Boton9.config(fg = "#03f943", bg = "black")
          
          Boton4 = Button(frame, text = "4", width = "7", command = lambda:NumPantalla(4))
          Boton4.grid(row = 8, column = 1, padx = 1, pady = 1)
          Boton4.config(fg = "#03f943", bg = "black")
          
          Boton5 = Button(frame, text = "5", width = "7", command = lambda:NumPantalla(5))
          Boton5.grid(row = 8, column = 2, padx = 1, pady = 1)
          Boton5.config(fg = "#03f943", bg = "black")
          
          Boton6 = Button(frame, text = "6", width = "7", command = lambda:NumPantalla(6))
          Boton6.grid(row = 8, column = 3, padx = 1, pady = 1)
          Boton6.config(fg = "#03f943", bg = "black")
          
          Boton2 = Button(frame, text = "2", width = "7", command = lambda:NumPantalla(2))
          Boton2.grid(row = 9, column = 2, padx = 1, pady = 1)
          Boton2.config(fg = "#03f943", bg = "black")
          
          Boton3 = Button(frame, text = "3", width = "7", command = lambda:NumPantalla(3))
          Boton3.grid(row = 9, column = 3, padx = 1, pady = 1)
          Boton3.config(fg = "#03f943", bg = "black")

def NumPantalla(Num):
     
     global Op # --global-- perMIte utilizar un variable global dentro de la funcion
     global Resultado
     
     print("TnumE",Num,Op,Resultado)
     if Op != "":
          NumP.set(Num)
          Op = ""
     else:
          NumP.set(str(NumP.get()) + str(Num))
          
     print("Tnums",Num,Op,Resultado)

def AC():
     global Op,Resultado,P
     
     P = 0
     
     Resultado = 0
     Op = ""
     
     NumP.set(Op)
     NumBin.set(Op)
     NumOct.set(Op)
     NumDec.set(Op)
     
def Punto(Num):
     global Op, Resultado,P
     
     print("TnumE",Num,Op,Resultado,P)
     
     if P == 0:
          NumP.set(NumP.get() + Num)
          P = 1
     else:
          NumP.set(NumP.get())
     
     print("Tnums",Num,Op,Resultado,P)

def Igual(Num):
     global Op,Resultado
     
     print(RBOpcion.get(),float(Num))
     
     if RBOpcion.get() == 1:
          NumBin.set(Num)
          NumOct.set(str(Bin_Oct(float(Num)))+str(Binp_Octp(float(Num))))
          NumDec.set(str(Bin_Dec(float(Num)))+str(Binp_Decp(float(Num))))
     elif RBOpcion.get() == 2:
          NumBin.set(str(Oct_Bin(float(Num)))+str(Octp_Binp(float(Num))))
          NumOct.set(Num)
          NumDec.set(str(Oct_Dec(float(Num)))+str(Octp_Decp(float(Num))))
     elif RBOpcion.get() == 3:
          NumBin.set(str(Dec_Bin(float(Num)))+str(Decp_Binp(float(Num))))
          NumOct.set(str(Dec_Oct(float(Num)))+str(Decp_Octp(float(Num))))
          NumDec.set(Num)
     
     print(str(Decp_Binp(float(Num))))
     print("IgualS",Num,Op,Resultado,NumBin,NumOct,NumDec)
#-----------------------------------Botones------------------------------------

# -- fila 6
BotonAC = Button(frame, text = "AC", width = "7", command = lambda:AC())
BotonAC.grid(row = 6, column = 1, padx = 1, pady = 1)
BotonAC.config(fg = "#03f943", bg = "black")

#-- Fila 7
Boton7 = Button(frame, text = "7", width = "7", command = lambda:NumPantalla(7))
Boton7.grid(row = 7, column = 1, padx = 1, pady = 1)
Boton7.config(fg = "#03f943", bg = "black")

Boton8 = Button(frame, text = "8", width = "7", command = lambda:NumPantalla(8))
Boton8.grid(row = 7, column = 2, padx = 1, pady = 1)
Boton8.config(fg = "#03f943", bg = "black")

Boton9 = Button(frame, text = "9", width = "7", command = lambda:NumPantalla(9))
Boton9.grid(row = 7, column = 3, padx = 1, pady = 1)
Boton9.config(fg = "#03f943", bg = "black")

#-- Fila 8
Boton4 = Button(frame, text = "4", width = "7", command = lambda:NumPantalla(4))
Boton4.grid(row = 8, column = 1, padx = 1, pady = 1)
Boton4.config(fg = "#03f943", bg = "black")

Boton5 = Button(frame, text = "5", width = "7", command = lambda:NumPantalla(5))
Boton5.grid(row = 8, column = 2, padx = 1, pady = 1)
Boton5.config(fg = "#03f943", bg = "black")

Boton6 = Button(frame, text = "6", width = "7", command = lambda:NumPantalla(6))
Boton6.grid(row = 8, column = 3, padx = 1, pady = 1)
Boton6.config(fg = "#03f943", bg = "black")

#-- Fila 9
Boton1 = Button(frame, text = "1", width = "7", command = lambda:NumPantalla(1))
Boton1.grid(row = 9, column = 1, padx = 1, pady = 1)
Boton1.config(fg = "#03f943", bg = "black")

Boton2 = Button(frame, text = "2", width = "7", command = lambda:NumPantalla(2))
Boton2.grid(row = 9, column = 2, padx = 1, pady = 1)
Boton2.config(fg = "#03f943", bg = "black")

Boton3 = Button(frame, text = "3", width = "7", command = lambda:NumPantalla(3))
Boton3.grid(row = 9, column = 3, padx = 1, pady = 1)
Boton3.config(fg = "#03f943", bg = "black")

#-- Fila 10
BotonPunto = Button(frame, text = ".", width = "7", command = lambda:Punto("."))
BotonPunto.grid(row = 10, column = 1, padx = 1, pady = 1)
BotonPunto.config(fg = "#03f943", bg = "black")

Boton0 = Button(frame, text = "0", width = "7", command = lambda:NumPantalla(0))
Boton0.grid(row = 10, column = 2, padx = 1, pady = 1)
Boton0.config(fg = "#03f943", bg = "black")

BotonIgual = Button(frame, text = "=", width = "7", command = lambda:Igual(NumP.get()))
BotonIgual.grid(row = 10, column = 3, padx = 1, pady = 1)
BotonIgual.config(fg = "#03f943", bg = "black")

#------------------------------Botones Forma Radio-----------------------------

#-- Fila 2
BotonBin = Radiobutton(frame, text = "Bin =", variable = RBOpcion, value = 1, width = "5", command = OpcionesRadBut)
BotonBin.grid(row = 2, column = 1, padx = 1, pady = 1)
BotonBin.config(fg = "blue", bg = "black")

# -- Fila 3
BotonOct = Radiobutton(frame, text = "Oct =", variable = RBOpcion, value = 2, width = "5", command = OpcionesRadBut)
BotonOct.grid(row = 3, column = 1, padx = 1, pady = 1)
BotonOct.config(fg = "blue", bg = "black")

# -- Fila 4
BotonDec = Radiobutton(frame, text = "Dec =", variable = RBOpcion, value = 3, width = "5", command = OpcionesRadBut)
BotonDec.grid(row = 4, column = 1, padx = 1, pady = 1)
BotonDec.config(fg = "blue", bg = "black")

#-----------------------------Botones De Selecion----------------------------

raiz.mainloop()