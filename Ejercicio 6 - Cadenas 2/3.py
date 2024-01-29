# 3. Dado un párrafo, buscar las comas comprobar que hay un blanco detrás, y ponerlo . 
# Comprobar que después de un punto, se escribe en mayúsculas  
cadena_1 = input("Introduce una cadena:")
nueva_cadena = ""

for i in range(len(cadena_1)):
    caracter = cadena_1[i] #POSICION DE LA CADENA

    if caracter == ',' and i + 1 < len(cadena_1) and cadena_1[i + 1] != ' ': # i + 1 < len(cadena_1) CARACTER MAS 1 TIENE QUE SER MENOR QUE LA CADENA
        nueva_cadena += caracter + ' '
    else:
        nueva_cadena += caracter

# Convertir la letra siguiente a mayúsculas después de un punto
resultado_final = ""
despues_de_punto = False #INCIALIZA EN FALSO
for char in nueva_cadena:
    if despues_de_punto and char.islower():
        resultado_final += ' ' + char.upper()
    else:
        resultado_final += char

    despues_de_punto = (char == '.') #SI ESTO SE CUMPLE despues_de_punto ES VERDADERO

print(resultado_final)