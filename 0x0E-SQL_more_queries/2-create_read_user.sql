-- creates database and user
-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

USE hbtn_0d_2;

-- create user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED WITH 'user_0d_2_pwd';

-- grant privileges
GRANT SELECT ON *.* TO 'user_0d_2'@'localhost';
