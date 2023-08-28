CREATE DATABASE  IF NOT EXISTS `bank` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bank`;
-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: bank
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `klient`
--

DROP TABLE IF EXISTS `klient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `klient` (
  `Klient_id` int NOT NULL AUTO_INCREMENT,
  `jmeno` varchar(50) DEFAULT NULL,
  `prijmeni` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Klient_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `operace`
--

DROP TABLE IF EXISTS `operace`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `operace` (
  `Operace_id` int NOT NULL AUTO_INCREMENT,
  `Zamestnanec_id` int DEFAULT NULL,
  `Ucet_id` int DEFAULT NULL,
  `typ_operace` enum('Vklad','Vyber','Prevod') DEFAULT NULL,
  `datum_operace` date DEFAULT NULL,
  `cislo_zdroj_uctu` int DEFAULT NULL,
  `cislo_cil_uctu` int DEFAULT NULL,
  `castka` int DEFAULT NULL,
  PRIMARY KEY (`Operace_id`),
  KEY `Zamestnanec_id` (`Zamestnanec_id`),
  KEY `Ucet_id` (`Ucet_id`),
  CONSTRAINT `operace_ibfk_1` FOREIGN KEY (`Zamestnanec_id`) REFERENCES `zamestnanci` (`Zamestnanec_id`),
  CONSTRAINT `operace_ibfk_2` FOREIGN KEY (`Ucet_id`) REFERENCES `ucty` (`Ucet_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pobocky`
--

DROP TABLE IF EXISTS `pobocky`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pobocky` (
  `Pobocka_id` int NOT NULL AUTO_INCREMENT,
  `nazev` varchar(50) DEFAULT NULL,
  `adresa` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Pobocka_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `soucet_transakci`
--

DROP TABLE IF EXISTS `soucet_transakci`;
/*!50001 DROP VIEW IF EXISTS `soucet_transakci`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `soucet_transakci` AS SELECT 
 1 AS `SUM(castka)`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `soucet_zustatku`
--

DROP TABLE IF EXISTS `soucet_zustatku`;
/*!50001 DROP VIEW IF EXISTS `soucet_zustatku`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `soucet_zustatku` AS SELECT 
 1 AS `SUM(pocatecni_zustatek)`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `ucty`
--

DROP TABLE IF EXISTS `ucty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ucty` (
  `Ucet_id` int NOT NULL AUTO_INCREMENT,
  `Klient_id` int DEFAULT NULL,
  `cislo_uctu` int DEFAULT NULL,
  `pocatecni_zustatek` int DEFAULT NULL,
  `datum_vytvoreni` date DEFAULT NULL,
  PRIMARY KEY (`Ucet_id`),
  KEY `Klient_id` (`Klient_id`),
  CONSTRAINT `ucty_ibfk_1` FOREIGN KEY (`Klient_id`) REFERENCES `klient` (`Klient_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `zamestnanci`
--

DROP TABLE IF EXISTS `zamestnanci`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `zamestnanci` (
  `Zamestnanec_id` int NOT NULL AUTO_INCREMENT,
  `Pobocka_id` int DEFAULT NULL,
  `Ucet_id` int DEFAULT NULL,
  `jmeno` varchar(50) DEFAULT NULL,
  `prijmeni` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Zamestnanec_id`),
  KEY `Pobocka_id` (`Pobocka_id`),
  KEY `Ucet_id` (`Ucet_id`),
  CONSTRAINT `zamestnanci_ibfk_1` FOREIGN KEY (`Pobocka_id`) REFERENCES `pobocky` (`Pobocka_id`),
  CONSTRAINT `zamestnanci_ibfk_2` FOREIGN KEY (`Ucet_id`) REFERENCES `ucty` (`Ucet_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Final view structure for view `soucet_transakci`
--

/*!50001 DROP VIEW IF EXISTS `soucet_transakci`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `soucet_transakci` AS select sum(`operace`.`castka`) AS `SUM(castka)` from `operace` where (`operace`.`Zamestnanec_id` = 1) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `soucet_zustatku`
--

/*!50001 DROP VIEW IF EXISTS `soucet_zustatku`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `soucet_zustatku` AS select sum(`ucty`.`pocatecni_zustatek`) AS `SUM(pocatecni_zustatek)` from `ucty` where (`ucty`.`Klient_id` = 1) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-28 21:37:26
