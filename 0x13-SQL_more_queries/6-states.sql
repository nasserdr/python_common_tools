-- creates the database hbtn_0d_usa and the table states
CREATE DATABASE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states ( id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL);