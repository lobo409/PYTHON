# Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
# Por ejemplo: 1000 minutos son 16 horas y 40 minutos.
import math
minutos = int(input("Indique la cantidad de minutos:"))
horas = math.trunc(minutos/60) #math.trunc --> se queda con la parte entera de las horas sin tener en cuenta los decimales
minutos2 = minutos%60
print (minutos,"minutos son:", horas, "horas y",minutos2, "minutos")