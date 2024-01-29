#8.	Solicitar un número ejemplo 30 y pedir 30 números por teclado contando los positivos y los negativos;
numero=int(input('Introduce el numero de numeros que solicito:'))
positivos=0
negativos=0
for i in range(0,numero):
    numerointroducido=int(input('Introduce un numero:'))
    if numerointroducido > 0:
        positivos=positivos+1
    else:
        negativos=negativos+1
print('Positivos:',positivos)
print('Negativos:',negativos)