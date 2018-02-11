/*
SQLyog Ultimate v11.24 (32 bit)
MySQL - 10.1.19-MariaDB : Database - blog
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`blog` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `blog`;

/*Table structure for table `mysql_province` */

DROP TABLE IF EXISTS `mysql_province`;

CREATE TABLE `mysql_province` (
  `code` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `mysql_province` */

insert  into `mysql_province`(`code`,`name`) values (11,'北京市'),(12,'天津市'),(13,'河北省'),(14,'山西省'),(15,'内蒙古自治区'),(21,'辽宁省'),(22,'吉林省'),(23,'黑龙江省'),(31,'上海市'),(32,'江苏省'),(33,'浙江省'),(34,'安徽省'),(35,'福建省'),(36,'江西省'),(37,'山东省'),(41,'河南省'),(42,'湖北省'),(43,'湖南省'),(44,'广东省'),(45,'广西壮族自治区'),(46,'海南省'),(50,'重庆市'),(51,'四川省'),(52,'贵州省'),(53,'云南省'),(54,'西藏自治区'),(61,'陕西省'),(62,'甘肃省'),(63,'青海省'),(64,'宁夏回族自治区'),(65,'新疆维吾尔自治区');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
