#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa
import math
cateto = int(input('Indica la medida de los catetos:'))
hipotenusa = math.sqrt((cateto**2) + (cateto**2))
print('La hipotenusa es', hipotenusa)