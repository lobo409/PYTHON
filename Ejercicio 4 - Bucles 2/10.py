# Escribe un programa que, dados dos números, uno real (base) y un entero positivo (exponente), 
# saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.

base = int(input("Indique la base: "))
exponente = int(input("Indique el exponente: "))
inicio = 0
resultado = 1

while inicio < exponente:
    resultado = resultado * base
    inicio = inicio + 1

print("Resultado:", resultado)