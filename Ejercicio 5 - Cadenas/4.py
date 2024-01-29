# 4. Pide una cadena y un carácter por teclado y muestra cuantas veces aparece el carácter en la cadena.count
cadena = input("Escribe una cadena:")
caracter = input("Escribe un caracter:")

if caracter in cadena:
    contador = cadena.count(caracter)
    print (f"La cadena tiene {contador} caracteres")
else:
    print ("La cadena no tiene el caracter solicitado")