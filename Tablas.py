"""
Nombre: Tablas
Fecha Inicio:
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

Tipos de tablas

T1 -- ═,║,╔,╗,╚,╝,╠,╣,╦,╩,╬
        
T2 -- ─,│,┌,┐,└,┘,├,┤,┬,┴,┼
           
"""

print("{:^89}".format("╔═══════════════════════════════════════════════════════════════════════════════════════╗"))
print("{:^1}{:^87}{:^1}".format("║","Ecuacion","║"))
print("{:^1}{:^13}{:^1}{:^25}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("╠","═════════════","╦","═════════════════════════","╦","═══════════════","╦","═══════════════","╦","═══════════════","╣"))
print("{:^1}{:^13}{:^1}{:^25}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("║","Interaccion","║","Raiz","║","F(x)","║","Error abs","║","Error rel","║"))
print("{:^1}{:^13}{:^1}{:^25}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("╠","═════════════","╬","═════════════════════════","╬","═══════════════","╬","═══════════════","╬","═══════════════","╣"))

i = 0
while i <= 19:
     print("{:^1}{:^13}{:^1}{:^25}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("║",i+1,"║",i**2,"║",i//5,"║",i/4,"║",i**1/2,"║"))
     i += 1
     
print("{:^1}{:^13}{:^1}{:^25}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}".format("╠","═════════════","╩","═════════════════════════","╩","═══════════════","╩","═══════════════","╩","═══════════════","╣"))
print("{:^1}{:^32}{:^32}{:^23}{:^1}".format("║","Raiz aproximada ~"," "," ","║"))
print("{:^88}".format("╚═══════════════════════════════════════════════════════════════════════════════════════╝"))