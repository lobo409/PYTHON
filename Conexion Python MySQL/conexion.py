import mysql.connector

# Configuración de la conexión a la base de datos
config = {
    'user': 'nombre',
    'password': '1234',
    'host': 'localhost',
    'database': 'pacientes_alcorcon'
}

# Crear la conexión
conexion = mysql.connector.connect(**config) # **config se utiliza para desempaquetar el diccionario config que contiene la información de configuración necesaria para la conexión

# Crear un objeto cursor para ejecutar consultas
cursor = conexion.cursor()

try:
    # Consulta para seleccionar todos los datos de la tabla
    consulta = 'SELECT * FROM pacientes'

    # Ejecutar la consulta
    cursor.execute(consulta)

    # Obtener todos los resultados
    resultados = cursor.fetchall()

    # Mostrar los resultados
    for fila in resultados:
        print(fila)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()
