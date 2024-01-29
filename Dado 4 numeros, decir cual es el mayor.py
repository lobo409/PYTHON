#Dado 4 numeros, decir cual es el mayor
numero1 = int(input("Indicame el primer numero:"))
numero2 = int(input("Indicame el segundo numero:"))
numero3 = int(input("Indicame el tercer numero:"))
numero4 = int(input("Indicame el cuarto numero:"))

mayor = numero1

if numero2 > mayor:
    mayor = numero2
elif numero3 > mayor:
    mayor = numero3
elif numero4 > mayor:
    mayor = numero4

print(f"El número mayor es: {mayor}")