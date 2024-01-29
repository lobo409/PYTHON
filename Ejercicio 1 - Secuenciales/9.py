# Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.
preciototal = int(input("Indique el precio total del producto:"))
preciofinal = (preciototal-(preciototal*15/100))
print("El precio final es:", preciofinal)