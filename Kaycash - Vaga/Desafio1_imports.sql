CREATE DATABASE  IF NOT EXISTS `desafio` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `desafio`;
-- MySQL dump 10.13  Distrib 8.0.12, for Win64 (x86_64)
--
-- Host: localhost    Database: desafio
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `desafio1_imoveis`
--

DROP TABLE IF EXISTS `desafio1_imoveis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `desafio1_imoveis` (
  `ID_IMOVEL` int(11) DEFAULT NULL,
  `ID_BAIRRO` int(11) DEFAULT NULL,
  `AREA_m2` int(11) DEFAULT NULL,
  `PRECO` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `desafio1_imoveis`
--

LOCK TABLES `desafio1_imoveis` WRITE;
/*!40000 ALTER TABLE `desafio1_imoveis` DISABLE KEYS */;
INSERT INTO `desafio1_imoveis` VALUES (1,1,126,827600),(2,2,129,1111246),(3,3,92,762763),(4,1,96,748262),(5,2,116,841057),(6,3,99,658592),(7,3,104,1022486),(8,3,141,950101),(9,2,101,1159807),(10,1,140,1176378),(11,1,121,861442),(12,1,142,1134910),(13,3,61,1000850),(14,1,66,762721),(15,1,90,1187119),(16,2,119,1062869),(17,2,100,902953),(18,2,101,971834),(19,3,110,875982),(20,2,143,718857);
/*!40000 ALTER TABLE `desafio1_imoveis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `desafio1_nome_bairros`
--

DROP TABLE IF EXISTS `desafio1_nome_bairros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `desafio1_nome_bairros` (
  `ID_BAIRRO` int(11) DEFAULT NULL,
  `NOME_BAIRRO` text,
  `ATUACAO` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `desafio1_nome_bairros`
--

LOCK TABLES `desafio1_nome_bairros` WRITE;
/*!40000 ALTER TABLE `desafio1_nome_bairros` DISABLE KEYS */;
INSERT INTO `desafio1_nome_bairros` VALUES (1,'Itaim Bibi','S'),(2,'Vila Olimpia','N'),(3,'Pinheiros','S'),(4,'Vila Madalena','N'),(5,'Vila Mariana','N');
/*!40000 ALTER TABLE `desafio1_nome_bairros` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-17 12:52:37
