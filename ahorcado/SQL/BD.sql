CREATE DATABASE ahorcado;

USE ahorcado;

CREATE TABLE IF NOT EXISTS `usuarios` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Contraseña` varchar(256) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Nombre` (`Nombre`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `partidas_jugadas` (
  `ID_Partida` int NOT NULL AUTO_INCREMENT,
  `ID_Jugador` int DEFAULT NULL,
  `Fecha_Partida` datetime DEFAULT CURRENT_TIMESTAMP,
  `Intentos` int NOT NULL,
  `Partida_Ganada` varchar(2) DEFAULT NULL,
  `Partida_Perdida` varchar(2) DEFAULT NULL,
  PRIMARY KEY (`ID_Partida`),
  KEY `ID_Jugador` (`ID_Jugador`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

