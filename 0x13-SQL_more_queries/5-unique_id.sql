-- Insure that the field is never empty and the ID is unique
CREATE TABLE IF NOT EXISTS unique_id ( id INT UNIQUE DEFAULT 1, name VARCHAR(256) NOT NULL);
