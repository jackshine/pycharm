DROP TABLE IF EXISTS `daily`;
CREATE TABLE `daily`(
 `ID` INT(5) NOT NULL AUTO_INCREMENT ,
  `title` INT(5) NOT NULL AUTO_INCREMENT comment '标题' ,
  `body` VARCHAR(300) NOT NULL  comment '内容',
  `created_time` VARCHAR(50) NOT NULL ,
  `modified_time` VARCHAR(50) NOT NULL  ,
  `category_id` VARCHAR(50) NOT NULL  comment '分类',
  `user_id` VARCHAR(50) NOT NULL comment '作者',
  PRIMARY KEY (`ID`)
) ENGINE=INNODB DEFAULT CHARSET=UTF8;