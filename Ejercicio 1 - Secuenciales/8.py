# Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
# el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes 
# y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
sueldobase = int(input("Indique su sueldo base:"))
costeventa1 = int(input("Indique el coste de la venta:"))
costeventa2 = int(input("Indique el coste de la venta:"))
costeventa3 = int(input("Indique el coste de la venta:"))
totalcomisiones = (costeventa1*10/100) + (costeventa2*10/100) + (costeventa3*10/100)
total = (sueldobase+totalcomisiones)
print("El total de las comisiones es:",totalcomisiones)
print("El sueldo total es:",total)