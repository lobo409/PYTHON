import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    database='pacientes_alcorcon',
    user='nombre',
    password='1234')

cursor = connection.cursor()
cursor.execute("select * from pacientes")
columnas = [columna[0] for columna in cursor.description]
print (columnas)
for fila in cursor:
    print (fila)