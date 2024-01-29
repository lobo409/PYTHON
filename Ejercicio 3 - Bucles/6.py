# Mostrar la tabla de multiplicar del 1 al 10
for i in range(1, 11):
    print("Tabla del", i)
    
    for a in range(1, 11):
        total = i * a
        print(f"{i} x {a} = {total}")