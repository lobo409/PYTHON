suma_pares = 0
suma_impares = 0

for numero in range(1, 101): #secuencia que comienza en 1 y va hasta 100 
    if numero % 2 == 0:
        suma_pares += numero #esto es una forma abreviada de escribir suma_pares = suma_pares + numero.
    else:
        suma_impares += numero #esto es una forma abreviada de escribir suma_impares = suma_impares + numero.

# Imprimir los resultados
print("Suma de los números pares del 1 al 100:", suma_pares)
print("Suma de los números impares del 1 al 100:", suma_impares)
