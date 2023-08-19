-- create database and  table
-- create Database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
-- create table "states"
CREATE TABLE IF NOT EXISTS states (
	id INT NOT NULL  AUTO_INCREMENT PRIMARY KEY,
	VARCHAR(256) NOR NULL,
);
