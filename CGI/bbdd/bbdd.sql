CREATE DATABASE empresa;

USE empresa;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(25) NOT NULL UNIQUE,
    contrasena VARCHAR(256) NOT NULL,
    email VARCHAR(25) NOT NULL
);