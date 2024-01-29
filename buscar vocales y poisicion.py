#Busca las vocales de un texto e indica la posicion

# vocales = ['a', 'e', 'i', 'o', 'u']

# texto = input("Facilite un texto:")
# posicion = 0

# for letra in texto:
#     if letra.lower() in vocales:
        # print(f"La vocal '{letra}' esta en la posición {posicion}")
    # posicion += 1
    
    
vocales = ['a', 'e', 'i', 'o', 'u']

texto = input("Facilite un texto:")

for posicion in range(len(texto)):
    letra = texto[posicion]
    if letra.lower() in vocales:
        print(f"La vocal '{letra}' está en la posición {posicion}")