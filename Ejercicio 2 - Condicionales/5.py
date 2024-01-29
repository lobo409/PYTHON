#Crea un programa que pida al usuario dos números y muestre su división
numero1 = int(input("Indique el primer numero:"))
numero2 = int(input("Indique el segundo numero:"))
if numero2 != 0: # Verifica si el segundo número es diferente de cero (para evitar división por cero)
    division = numero1 / numero2
    print("El resultado de la división es:", division)
else:
    print("No se puede dividir por cero")