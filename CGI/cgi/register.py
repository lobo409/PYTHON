#!C:\Program Files\Python\python.exe

import cgi
import hashlib
import mysql.connector

print("Content-type: text/html\n")
print("<html><head><title>Formulario Procesado</title></head><body>")
form = cgi.FieldStorage()

usuario = form.getvalue('usuario', '')
contrasena = form.getvalue('contrasena', '')
email = form.getvalue('email', '')

if usuario and contrasena and email:
    # Database connection
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='empresa',
            user='root',
            password='')
        
        cursor = connection.cursor()

        # Convert the password to bytes
        passwd_bytes = contrasena.encode('utf-8')

        # Create an SHA-256 hash object
        passwd_hash = hashlib.sha256()

        # Update the hash with the password bytes
        passwd_hash.update(passwd_bytes)

        # Get the hexadecimal representation of the hash
        passwd_hash_hex = passwd_hash.hexdigest()

        # Insert data into the database using a parameterized query
        query = "INSERT INTO usuarios (usuario, contrasena, email) VALUES (%s, %s, %s)"
        data = (usuario, passwd_hash_hex ,email)
        cursor.execute(query, data)

        # Commit the changes to the database
        connection.commit()
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
                                    <p>Se ha registrado correctamente</p>
                                    <a href="./../index.html" class="logout-btn">Cerrar Sesion</a>
                                </div>

                                <footer>
                                    <p>&copy; 2024 Your Website. Todos los derechos reservados.</p>
                                </footer>
                            </body>
                        </html>''')
    except mysql.connector.Error as err:
        print("<h2>Error en la base de datos: {}</h2>".format(err))
    finally:
        # Close the database connection
        if connection.is_connected():
            cursor.close()
            connection.close()
else:
    print("<h2>Faltan datos en el formulario.</h2>")

print("</body></html>")
