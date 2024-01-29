# Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.

num_base = 1

while num_base <= 5:
    print("Tabla del", num_base, ":")
    numero = 0
    
    while numero <=10:
        resultado = num_base * numero
        print(f"{num_base} x {numero} = {resultado}")
        numero = numero + 1
    
    print("--------------")
    num_base = num_base + 1