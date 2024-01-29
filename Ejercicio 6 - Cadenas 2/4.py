mensaje_original = input('Introduce una cadena: ')
mensaje_filtrado = mensaje_original

 # Lista de palabras malsonantes o patrones a buscar
malsonantes = ['palabra1', 'palabra2', 'palabra3']

# Reemplazar las palabras malsonantes con una carita feliz cada palabra malsonante que encuentre la reemplaza
for palabra in malsonantes:
    mensaje_filtrado = mensaje_filtrado.replace(palabra, ':)')


print("Mensaje original:", mensaje_original)
print("Mensaje filtrado:", mensaje_filtrado)