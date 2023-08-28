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
-- Dumping data for table `klient`
--

LOCK TABLES `klient` WRITE;
/*!40000 ALTER TABLE `klient` DISABLE KEYS */;
INSERT INTO `klient` VALUES (1,'Jmeno 1','Prijmeni 1'),(2,'Jmeno 2','Prijmeni 2'),(3,'Jmeno 3','Prijmeni 3'),(4,'Jmeno 4','Prijmeni 4'),(5,'Jmeno 5','Prijmeni 5');
/*!40000 ALTER TABLE `klient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `operace`
--

LOCK TABLES `operace` WRITE;
/*!40000 ALTER TABLE `operace` DISABLE KEYS */;
INSERT INTO `operace` VALUES (1,1,1,'Vklad','2023-08-10',123456789,NULL,100),(2,2,2,'Vyber','2023-08-11',987654321,NULL,50),(3,3,3,'Prevod','2023-08-12',111222333,987654321,300),(4,4,4,'Vklad','2023-08-13',444555666,NULL,150),(5,5,5,'Vyber','2023-08-14',777888999,NULL,200);
/*!40000 ALTER TABLE `operace` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `pobocky`
--

LOCK TABLES `pobocky` WRITE;
/*!40000 ALTER TABLE `pobocky` DISABLE KEYS */;
INSERT INTO `pobocky` VALUES (1,'Pobocka 1','Adresa 1'),(2,'Pobocka 2','Adresa 2'),(3,'Pobocka 3','Adresa 3'),(4,'Pobocka 4','Adresa 4'),(5,'Pobocka 5','Adresa 5');
/*!40000 ALTER TABLE `pobocky` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `ucty`
--

LOCK TABLES `ucty` WRITE;
/*!40000 ALTER TABLE `ucty` DISABLE KEYS */;
INSERT INTO `ucty` VALUES (1,1,123456789,1000,'2023-08-01'),(2,2,987654321,500,'2023-08-02'),(3,3,111222333,2000,'2023-08-03'),(4,4,444555666,300,'2023-08-04'),(5,5,777888999,1500,'2023-08-05');
/*!40000 ALTER TABLE `ucty` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `zamestnanci`
--

LOCK TABLES `zamestnanci` WRITE;
/*!40000 ALTER TABLE `zamestnanci` DISABLE KEYS */;
INSERT INTO `zamestnanci` VALUES (1,1,1,'Zamestnanec 1','Prijmeni 1'),(2,2,2,'Zamestnanec 2','Prijmeni 2'),(3,1,3,'Zamestnanec 3','Prijmeni 3'),(4,2,4,'Zamestnanec 4','Prijmeni 4'),(5,3,5,'Zamestnanec 5','Prijmeni 5');
/*!40000 ALTER TABLE `zamestnanci` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-28 21:36:19
