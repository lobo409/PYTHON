import random
import mysql.connector
import hashlib
import getpass

# Lista de palabras para el juego
palabras = ["python", "programacion", "ahorcado", "juego", "divertido", "codigo"]
palabra = random.choice(palabras)

# Número máximo de intentos permitidos
intentos_maximos = 10
intentos = 0
letras_usadas = []

# Pedir nombre de usuario
print("1. Crear cuenta")
print("2. Iniciar sesión")
print("3. Eliminar cuenta")
opcion = input("Indique una opcion: ")

# Conectar a la base de datos MySQL
connection = mysql.connector.connect(
    host='localhost',
    database='ahorcado',
    user='root',
    password='')

# Crear un cursor para interactuar con la base de datos
cursor = connection.cursor(prepared=True)

# Insertar nuevo usuario en la base de datos si no existe
if opcion == "1":
    nombre = input("Ingresa tu nickname del usuario: ")
    passwd = getpass.getpass("Ingresa una contraseña: ")
    hash_passwd = hashlib.sha256(passwd.encode()).hexdigest()
    insert_usuario = "INSERT INTO usuarios (Nombre, Contraseña) VALUES (%s, %s)"
    var_usuario = (nombre, hash_passwd)
    cursor.execute(insert_usuario, var_usuario)
    print("El usuario ha sido creado. Puedes comenzar el juego.")

    # Obtener el ID del usuario recién creado
    cursor.execute("SELECT ID FROM usuarios WHERE Nombre = %s", (nombre,))
    id_usuario = cursor.fetchone()[0] # Sacar el primer elemento de la siguientee fila

elif opcion == "2":
    intentos_login = 3
    while intentos_login > 0:
        usuario = input("Ingrese su nombre de usuario: ")
        contraseña = getpass.getpass("Contraseña: ")
        cursor.execute("SELECT ID, Contraseña FROM usuarios WHERE Nombre = %s", (usuario,))
        resultado = cursor.fetchone()
        resultado_id = resultado[0]
        resultado_passwd = hashlib.sha256(contraseña.encode()).hexdigest()
        if resultado_id and resultado_passwd == hashlib.sha256(contraseña.encode('utf-8')).hexdigest().lower():
            print("¡Inicio de sesión exitoso para el usuario con ID:", resultado[0], "!")
            # Obtener el ID del usuario que inició sesión
            id_usuario = resultado[0]
            break
        else:
            print("¡Nombre de usuario o contraseña incorrectos!")
            intentos_login -= 1
            print(f"Intentos restantes: {intentos_login}")
    else:
        print("Demasiados intentos fallidos. Saliendo del programa.")
        exit()
elif opcion == "3":
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = getpass.getpass("Contraseña: ")
    cursor.execute("SELECT ID, Contraseña FROM usuarios WHERE Nombre = %s", (usuario,))
    resultado = cursor.fetchone()
    resultado_id = resultado[0]
    resultado_passwd = hashlib.sha256(contraseña.encode()).hexdigest()
    if resultado_id and resultado_passwd == hashlib.sha256(contraseña.encode('utf-8')).hexdigest().lower():
        confirmacion = input("¿Estás seguro de que deseas eliminar tu cuenta? (Sí/No): ")
        if confirmacion.lower() == "si":
            cursor.execute("DELETE FROM usuarios WHERE Nombre = %s", (usuario,))
            connection.commit()
            print("¡Tu cuenta ha sido eliminada con éxito!")
            exit()
        else:
            print("Operación de eliminación cancelada.")
            exit()
else:
    print("Opción no válida.")
    exit()

# CREAR TABLERO
tablero = ["_"] * len(palabra)

# Bucle principal del juego
while True:
    # Mostrar el tablero actual
    print(" ".join(tablero))

    # Pedir al usuario que ingrese una letra
    letra = input("Ingrese una letra: ")

    # Verificar si la letra ya fue utilizada
    if letra in letras_usadas:
        print("Ya has utilizado esa letra. Por favor, usa otra letra.")
        continue

    # Verificar si la letra no está en la palabra
    if letra not in palabra:
        intentos += 1
        print(f"Incorrecto. Te quedan {intentos_maximos - intentos} intentos")
        letras_usadas.append(letra)
    else:
        letras_usadas.append(letra)

    # Actualizar el tablero con las letras adivinadas
    for i, letra_palabra in enumerate(palabra):
        if letra_palabra in letras_usadas:
            tablero[i] = letra_palabra

    # Verificar si se adivinó la palabra completa
    if "_" not in tablero:
        print("¡Felicidades! ¡Has adivinado la palabra!")
        insert_partida = "INSERT INTO partidas_jugadas (ID_Jugador, Partida_Ganada, intentos) VALUES (%s, 'Si', %s)"
        var_partida = (id_usuario, intentos)
        cursor.execute(insert_partida, var_partida)
        connection.commit()
        break

    # Verificar si se alcanzó el número máximo de intentos
    if intentos == intentos_maximos:
        print(f"¡Perdiste! La palabra era: {palabra}")
        insert_partida = "INSERT INTO partidas_jugadas (ID_Jugador, Partida_Perdida, intentos) VALUES (%s, 'Si', %s)"
        var_partida = (id_usuario, intentos)
        cursor.execute(insert_partida, var_partida)
        connection.commit()
        break

# Confirmar los cambios en la base de datos
connection.commit()

# Cerrar la conexión a la base de datos
connection.close()