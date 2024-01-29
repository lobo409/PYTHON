#Algoritmo solicita un usuario y contraseña y si es correcto HA ENTRADO EN EL SISTEMA
usuariosistema = "andres"
contyraseñasistema = "1234"
usuario = input("Indique el usuario:")
contraseña = input("Indique la contraseña:")
if usuario == usuariosistema and contraseña == contyraseñasistema:
    print("Acceso al sistema correcto. Bienvenido!")
else:
    print("Acceso al sistema incorrecto")