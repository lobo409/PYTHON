#!C:\Program Files\Python\python.exe

import cgi
import hashlib
import mysql.connector

print("Content-type: text/html\n")

form = cgi.FieldStorage()
usuario = form.getvalue('usuario', '')
contrasena = form.getvalue('contrasena', '')

if usuario and contrasena:
    hash_passwd = hashlib.sha256(contrasena.encode()).hexdigest()
    
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='empresa',
            user='root',
            password='')
        
        cursor = connection.cursor()
        
        query = "SELECT usuario, contrasena FROM usuarios WHERE usuario = %s"
        cursor.execute(query, (usuario,))
        result = cursor.fetchone()
        
        if result:
            _, hash_contrasena = result
            if hash_contrasena == hash_passwd:
                print('''<!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                <title>Pagina inicio</title>
                                <link rel="stylesheet" href="./../css/welcome.css">
                            </head>
                            <body>
                                <header>
                                    <nav>
                                        <ul>
                                            <li><a href="#">Inicio</a></li>
                                            <li><a href="#">Acerca De</a></li>
                                            <li><a href="#">Servicios</a></li>
                                            <li><a href="#">Contactos</a></li>
                                        </ul>
                                    </nav>
                                </header>

                                <div class="container">
                                    <h1>Bienvenido!</h1>
                                    <p>Ha iniciado sesion correctamente</p>
                                    <a href="./../index.html" class="logout-btn">Cerrar Sesion</a>
                                </div>

                                <footer>
                                    <p>&copy; 2024 Your Website. Todos los derechos reservados.</p>
                                </footer>
                            </body>
                        </html>''')
            else:
                print("<h2>ERROR!</h2>")
        else:
            print("<h2>Error de usuario!</h2>")
    except mysql.connector.Error as err:
        print("<h2>Error en la base de datos: {}</h2>".format(err))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
else:
    print("<h2>Por favor, ingrese usuario y contraseña.</h2>")

print("</body></html>")
