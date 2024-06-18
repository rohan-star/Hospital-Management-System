CREATE DATABASE  IF NOT EXISTS `hospital` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `hospital`;
-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: hospital
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Table structure for table `discardable_inventory`
--

DROP TABLE IF EXISTS `discardable_inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `discardable_inventory` (
  `iddiscardable_inventory` int NOT NULL AUTO_INCREMENT,
  `discardable_inventory_quantity` int DEFAULT NULL,
  PRIMARY KEY (`iddiscardable_inventory`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discardable_inventory`
--

LOCK TABLES `discardable_inventory` WRITE;
/*!40000 ALTER TABLE `discardable_inventory` DISABLE KEYS */;
INSERT INTO `discardable_inventory` VALUES (1,5),(2,11),(3,7),(4,7),(5,10),(6,1),(7,40);
/*!40000 ALTER TABLE `discardable_inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hospital`
--

DROP TABLE IF EXISTS `hospital`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hospital` (
  `idhospital` int NOT NULL AUTO_INCREMENT,
  `hospital_name` varchar(45) DEFAULT NULL,
  `hospital_email` varchar(45) DEFAULT NULL,
  `hospital_nationalid` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idhospital`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hospital`
--

LOCK TABLES `hospital` WRITE;
/*!40000 ALTER TABLE `hospital` DISABLE KEYS */;
INSERT INTO `hospital` VALUES (1,'Yashraj Hospital , Sawantwadi','yashrajhospital@gmail.com','34585');
/*!40000 ALTER TABLE `hospital` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory` (
  `idinventory` int NOT NULL AUTO_INCREMENT,
  `inventory_name` varchar(45) DEFAULT NULL,
  `inventory_description` varchar(150) DEFAULT NULL,
  `inventory_status` int DEFAULT NULL,
  `inventory_quantity` int DEFAULT NULL,
  `discardable_inventory_quantity` varchar(20) DEFAULT NULL,
  `replaceable_inventory_quantity` varchar(20) DEFAULT NULL,
  `purchasable_inventory_quantity` varchar(20) DEFAULT NULL,
  `required_currency` int DEFAULT NULL,
  PRIMARY KEY (`idinventory`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES (1,'Stethescope','Test Heartbeats',1,50,'0','2','3',10000),(4,'Ventilator','Use to help in respiration ',4,6,'1','2','3',50000),(5,'Operating Table','Bed where patients are operated',4,250,'5','1','1',30000),(6,'Syringe Pump','used to gradually administer specific amounts of fluids for use in chemical and biomedical research ',1,900,'40','5','300',45000);
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory_status`
--

DROP TABLE IF EXISTS `inventory_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory_status` (
  `idinventory_status` int NOT NULL AUTO_INCREMENT,
  `add_inventory_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`idinventory_status`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory_status`
--

LOCK TABLES `inventory_status` WRITE;
/*!40000 ALTER TABLE `inventory_status` DISABLE KEYS */;
INSERT INTO `inventory_status` VALUES (1,'Durable'),(2,'Expired'),(3,'Replace it'),(4,'replace it'),(5,'expired');
/*!40000 ALTER TABLE `inventory_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchasable_inventory`
--

DROP TABLE IF EXISTS `purchasable_inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchasable_inventory` (
  `idpurchasable_inventory` int NOT NULL AUTO_INCREMENT,
  `purchasable_inventory_quantity` int DEFAULT NULL,
  PRIMARY KEY (`idpurchasable_inventory`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchasable_inventory`
--

LOCK TABLES `purchasable_inventory` WRITE;
/*!40000 ALTER TABLE `purchasable_inventory` DISABLE KEYS */;
INSERT INTO `purchasable_inventory` VALUES (1,20),(2,30),(3,3),(4,300);
/*!40000 ALTER TABLE `purchasable_inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `records`
--

DROP TABLE IF EXISTS `records`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `records` (
  `idrecords` int NOT NULL AUTO_INCREMENT,
  `inventory_name` varchar(100) DEFAULT NULL,
  `inventory_quantity` int DEFAULT NULL,
  `current_status` varchar(100) DEFAULT NULL,
  `replacement_status` varchar(100) DEFAULT NULL,
  `inventory_status` varchar(100) DEFAULT NULL,
  `days` int DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `to_date` datetime DEFAULT NULL,
  PRIMARY KEY (`idrecords`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `records`
--

LOCK TABLES `records` WRITE;
/*!40000 ALTER TABLE `records` DISABLE KEYS */;
INSERT INTO `records` VALUES (1,'Stethescope',70,'In Use','-','Usable',9,'2020-09-21 00:00:00','2020-09-30 00:00:00'),(2,'Ventilator',10,'In Use','Not Done','Replace',11,'2020-09-21 00:00:00','2020-10-02 00:00:00');
/*!40000 ALTER TABLE `records` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `replaceable_inventory`
--

DROP TABLE IF EXISTS `replaceable_inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `replaceable_inventory` (
  `idreplaceable_inventory` int NOT NULL AUTO_INCREMENT,
  `replaceable_inventory_quantity` int DEFAULT NULL,
  PRIMARY KEY (`idreplaceable_inventory`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `replaceable_inventory`
--

LOCK TABLES `replaceable_inventory` WRITE;
/*!40000 ALTER TABLE `replaceable_inventory` DISABLE KEYS */;
INSERT INTO `replaceable_inventory` VALUES (1,15),(2,2),(3,5);
/*!40000 ALTER TABLE `replaceable_inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `idusers` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(45) DEFAULT NULL,
  `user_email` varchar(45) DEFAULT NULL,
  `user_password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idusers`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'RMA','arwari@gmail.com','1234');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-21  3:56:44
