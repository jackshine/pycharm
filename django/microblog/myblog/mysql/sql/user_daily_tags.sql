#文章自定义标签
DROP TABLE IF EXISTS `user_daily_tags`;
CREATE TABLE `user_daily_tags`(
  `id` INT(5) NOT NULL AUTO_INCREMENT ,
   `NAME` VARCHAR(50) NOT NULL,
  `user_login_id` int(5) not null,
  `daily_id` INT(5) NOT NULL  ,
  PRIMARY KEY (`id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;