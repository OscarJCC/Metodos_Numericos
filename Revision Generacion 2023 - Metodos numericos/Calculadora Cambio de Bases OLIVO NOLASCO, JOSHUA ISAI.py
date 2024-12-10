def decimal_binario(numero):
     #Definimos parte entera y fraccionaria para tomar en cuenta el caso fraccionario
     parte_entera = int(numero)
     parte_fraccionaria = numero - parte_entera
     #Creamos un str para la parte entera binaria
     parte_entera_binaria = ""
     #Ciclo while para obtener los binarios enteros
     while parte_entera > 0:
          residuo = parte_entera % 2
          parte_entera_binaria = str(residuo) + parte_entera_binaria
          parte_entera = parte_entera // 2
     #Definimos la parte fraccionaria de los binarios
     parte_fraccionaria_binaria = ""
     #Definimos el rango a decimales individuales
     rango = 100
     i = 0
     #Ciclo while para la parte fraccionaria
     while parte_fraccionaria > 0 and i < rango:
          parte_fraccionaria *= 2
          bit = int(parte_fraccionaria)
          parte_fraccionaria_binaria += str(bit)
          parte_fraccionaria -= bit
          i += 1
     #Se define binario como el str resultante
     binario = parte_entera_binaria
     #Condicional para definir si se agrega o no parte fraccionaria binaria
     if parte_fraccionaria_binaria:
          binario += "." + parte_fraccionaria_binaria
     
     return binario

def decimal_octal(numero):
     octal = ""
     #Ciclo while para calcular el valor octal
     while numero > 0:
          residuo = numero % 8
          octal = str(residuo) + octal
          numero = numero // 8
     return octal

def binario_decimal(binario):
     decimal = 0
     #Condicional para saber si existe un punto en el str ingresado y trabajar
     #con parte entera y fraccionaria
     if "." in binario:
          parte_entera, parte_fraccionaria = binario.split(".")
          longitud_entera = len(parte_entera)
          longitud_fraccionaria = len(parte_fraccionaria)
     #Ciclo for para obtener el valor decimal entero
          for i in range(longitud_entera):
               digito = int(parte_entera[longitud_entera - 1 - i])
               decimal += digito * (2 ** i)
     #Ciclo for para obtener el valor decimal fraccionario
          for i in range(longitud_fraccionaria):
               digito = int(parte_fraccionaria[i])
               decimal += digito * (2 ** -(i + 1))
     #Si no existe cierto punto, simplemente se realiza la operacion con enteros (int)
     else:
          longitud = len(binario)
          for i in range(longitud):
               digito = int(binario[longitud - 1 - i])
               decimal += digito * (2 ** i)
     
     return decimal

def binario_octal(binario):
     #Conversi ́on de valor binario a decimal llamando a la primera funci ́on
     decimal = binario_decimal(binario)
     octal = ""
     #Ciclo while para obtener el valor octal del decimal convertido
     while decimal > 0:
          residuo = decimal % 8
          octal = str(residuo) + octal
          decimal = decimal // 8
     return octal