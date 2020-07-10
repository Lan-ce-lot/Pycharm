-- 建库
create database robot;
-- 笑话
create table joke
(
	ID int NOT NULL AUTO_INCREMENT,
	txt varchar(200),
	PRIMARY KEY (ID)
)