DROP TABLE IF EXISTS `daily`;
CREATE TABLE `daily`(
 `id` INT(5) NOT NULL AUTO_INCREMENT ,
  `title` VARCHAR(50) NOT NULL  COMMENT '标题' ,
  `body` VARCHAR(300) NOT NULL  COMMENT '内容',
  `create_time` DATETIME NOT NULL ,
  `modified_time` DATETIME  ,
  `category_id` INT(5) NOT NULL   COMMENT '分类',
  `user_id` VARCHAR(50) NOT NULL COMMENT '作者',
  `click` INT(10) not null DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;