-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versione server:              11.7.2-MariaDB - mariadb.org binary distribution
-- S.O. server:                  Win64
-- HeidiSQL Versione:            12.10.0.7000
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dump della struttura del database chess_ai
DROP DATABASE IF EXISTS `chess_ai`;
CREATE DATABASE IF NOT EXISTS `chess_ai` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
USE `chess_ai`;

-- Dump della struttura di tabella chess_ai.games
DROP TABLE IF EXISTS `games`;
CREATE TABLE IF NOT EXISTS `games` (
  `game_id` int(11) NOT NULL AUTO_INCREMENT,
  `start_datetime` datetime NOT NULL,
  `end_datetime` datetime DEFAULT NULL,
  `duration_seconds` int(11) DEFAULT NULL,
  `result` enum('1-0','0-1','1/2-1/2','*') DEFAULT NULL,
  `ai_metadata` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL COMMENT 'For future AI training data' CHECK (json_valid(`ai_metadata`)),
  PRIMARY KEY (`game_id`),
  KEY `start_datetime` (`start_datetime`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- L’esportazione dei dati non era selezionata.

-- Dump della struttura di tabella chess_ai.moves
DROP TABLE IF EXISTS `moves`;
CREATE TABLE IF NOT EXISTS `moves` (
  `move_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `game_id` int(11) NOT NULL,
  `ply_number` int(11) NOT NULL COMMENT 'Half-move counter',
  `move_notation` varchar(10) NOT NULL,
  `from_row` tinyint(4) NOT NULL COMMENT '0-7',
  `from_col` tinyint(4) NOT NULL COMMENT '0-7',
  `to_row` tinyint(4) NOT NULL COMMENT '0-7',
  `to_col` tinyint(4) NOT NULL COMMENT '0-7',
  `piece_type` char(1) NOT NULL COMMENT 'P,N,B,R,Q,K',
  `color` char(5) NOT NULL COMMENT 'white/black',
  `captured_piece` char(1) DEFAULT NULL,
  `is_castle` tinyint(1) DEFAULT 0,
  `is_promotion` tinyint(1) DEFAULT 0,
  `fen_before` varchar(90) NOT NULL,
  `fen_after` varchar(90) NOT NULL,
  `move_time` timestamp(3) NULL DEFAULT current_timestamp(3),
  PRIMARY KEY (`move_id`),
  KEY `game_id` (`game_id`,`ply_number`),
  KEY `fen_before` (`fen_before`(10)) COMMENT 'For position analysis',
  CONSTRAINT `moves_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `games` (`game_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- L’esportazione dei dati non era selezionata.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
