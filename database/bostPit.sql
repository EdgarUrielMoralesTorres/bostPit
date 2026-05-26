-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.28-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.8.0.6908
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para bostpit
CREATE DATABASE IF NOT EXISTS `bostpit` /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci */;
USE `bostpit`;

-- Volcando estructura para tabla bostpit.club
CREATE TABLE IF NOT EXISTS `club` (
  `id_club` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_club` varchar(100) DEFAULT NULL,
  `descripcion` varchar(100) DEFAULT NULL,
  `telefono` int(11) DEFAULT NULL,
  `correo` varchar(100) DEFAULT NULL,
  `encargado ` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_club`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- La exportación de datos fue deseleccionada.s

-- Volcando estructura para tabla bostpit.objetos
CREATE TABLE IF NOT EXISTS `objetos` (
  `id_objetos` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_objeto` varchar(100) NOT NULL,
  `categoria` int(11) NOT NULL,
  `lugar` varchar(100) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  PRIMARY KEY (`id_objetos`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla bostpit.reportes
CREATE TABLE IF NOT EXISTS `reportes` (
  `id_reporte` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_incidente` int(11) DEFAULT NULL,
  `lugar` varchar(100) DEFAULT NULL,
  `prioridad` int(11) DEFAULT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  `estado`  VARCHAR(50) DEFAULT 'Pendiente',

  PRIMARY KEY (`id_reporte`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla bostpit.tienda
CREATE TABLE IF NOT EXISTS `tienda` (
  `id_tienda` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_comida` varchar(100) DEFAULT NULL,
  `descripcion` varchar(100) DEFAULT NULL,
  `foto_comida` varchar(100) DEFAULT NULL,
  `precio` int(11) DEFAULT NULL,
  `stock` INT DEFAULT 0,
  PRIMARY KEY (`id_tienda`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla bostpit.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id_Usuario` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `contraseña` varchar(200) DEFAULT NULL,
  `telefono` int(50) DEFAULT 0,
  `foto_perfil` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_Usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- La exportación de datos fue deseleccionada.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
