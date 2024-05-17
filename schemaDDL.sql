-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: search
-- ------------------------------------------------------
-- Server version	8.0.31

 SET NAMES utf8 ;

--
-- Table structure for table `content`
--

DROP TABLE IF EXISTS `content`;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `content` (
  `id` int NOT NULL,
  `text` longtext,
  PRIMARY KEY (`id`),
  KEY `idx_text` (`text`(10))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Table structure for table `objects`
--

DROP TABLE IF EXISTS `objects`;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `objects` (
  `id` int NOT NULL,
  `full_path` varchar(1000) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `type` int DEFAULT NULL,
  `size` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dump completed on 2024-05-17 22:15:11
