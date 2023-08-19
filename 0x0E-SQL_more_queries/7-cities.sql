-- create database and table
-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- switch to database
USE hbtn_0d_usa;

-- create table cities
CREATE TABLE IF NOT EXISTS cities (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(state_id),
	name VARCHAR NOT NULL
	);
