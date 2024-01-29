# Realizar un algoritmo que pida  10 números  
# El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

mayorcero = 0
menorcero = 0
igualcero = 0
contador = 0

while contador < 10:
    numero = int(input("Ingrese un numero:"))

    if numero > 0:
        mayorcero += 1
    elif numero < 0:
        menorcero += 1
    else:
        igualcero += 1

    contador += 1
    
print("Cantidad de números mayores que 0:", mayorcero)
print("Cantidad de números menores que 0:", menorcero)
print("Cantidad de números iguales a 0:", igualcero)