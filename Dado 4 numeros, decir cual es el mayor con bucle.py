#Dado 4 numeros, decir cual es el mayor
# Lista de números
lista = [23, 56, 12, 45, 78, 34, 90, 800, 17, 42, 65, 31, 50, 73, 19, 88, 5, 27, 60, 95, 14, 68, 37, 81, 3, 69, 22, 47, 74, 10]

# Inicializar la variable en 0
mayor = 0

# Iterar sobre la lista para encontrar el número mayor
for numero in lista: #para numero dentro de la longitud de lista haz 
    if numero > mayor:
        mayor = numero

# Imprimir el resultado
print(f"El número mayor es: {mayor}")