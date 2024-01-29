-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 29-01-2024 a las 11:47:01
-- Versión del servidor: 8.0.31
-- Versión de PHP: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ahorcado`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `partidas_jugadas`
--

DROP TABLE IF EXISTS `partidas_jugadas`;
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

--
-- Volcado de datos para la tabla `partidas_jugadas`
--

INSERT INTO `partidas_jugadas` (`ID_Partida`, `ID_Jugador`, `Fecha_Partida`, `Intentos`, `Partida_Ganada`, `Partida_Perdida`) VALUES
(1, 1, '2024-01-25 23:43:13', 2, 'Si', NULL),
(2, 1, '2024-01-25 23:43:42', 3, 'Si', NULL),
(3, 1, '2024-01-25 23:45:34', 5, 'Si', NULL),
(4, 1, '2024-01-29 09:34:29', 0, 'Si', NULL),
(5, 2, '2024-01-29 09:35:05', 4, 'Si', NULL),
(6, 2, '2024-01-29 09:35:31', 1, 'Si', NULL),
(7, 1, '2024-01-29 12:33:28', 10, NULL, 'Si');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `Contraseña` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Nombre` (`Nombre`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`ID`, `Nombre`, `Contraseña`) VALUES
(1, 'andres', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
