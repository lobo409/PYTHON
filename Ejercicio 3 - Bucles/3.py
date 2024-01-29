# 3.Mostrar la tabla de multiplicar de un número que se introduce por teclado
numero = int(input("Introduce un numero:"))
for tabla in range(0, 11):
    resultado = numero * tabla
    print(f"{numero} x {tabla} = {resultado}")
