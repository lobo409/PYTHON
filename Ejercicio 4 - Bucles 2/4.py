# 5. Realizar un algoritmo del 1 al 200 y muestre la suma total de los pares 

contador = 1
suma = 0
while contador < 201:
    if contador % 2 == 0:
        suma = suma + contador
    contador +=1
print(f"la suma de los numeros pares es: {suma}")