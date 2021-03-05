-- creates the database hbtn_0d_usa and the table cities
CREATE DATABASE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  state_id INT NOT NULL FOREIGN KEY REFERENCES table(id)
  name VARCHAR(256) NOT NULL);
  
