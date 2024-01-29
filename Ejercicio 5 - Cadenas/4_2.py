# 4. Pide una cadena y un carácter por teclado y muestra cuantas veces aparece el carácter en la cadena y en que posicion esta.count
# Solicitar una cadena y un carácter al usuario
cadena = input("Ingresa una cadena: ")
caracter = input("Ingresa un carácter: ")

# Inicializar el contador de ocurrencias
contador = 0

# Imprimir las posiciones donde aparece el carácter y contar las ocurrencias
print("Posiciones en las que aparece el carácter:")
for i in range(len(cadena)):
    if cadena[i] == caracter:
        print(f"Posición {i}")
        contador += 1

print(f"El carácter '{caracter}' aparece {contador} veces en la cadena.")
