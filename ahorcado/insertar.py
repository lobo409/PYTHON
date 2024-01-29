import mysql.connector
connection = mysql.connector.connect(
    host='localhost',
    database='ahorcado',
    user='root',
    password='')

from ahorcado import nombre, intentos

cursor = connection.cursor()
insert = "INSERT INTO ahorcado () VALUES(%s, %s)"
var = (nombre, intentos)
cursor.execute(insert,var)

cursor.commit()
connection.close()