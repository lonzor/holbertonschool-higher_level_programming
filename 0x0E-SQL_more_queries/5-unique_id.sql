-- creates the table unique_id
-- id INT with the default value 1 and must be unique
-- If the table unique_id already exists, will not fail
CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1 UNIQUE, name VARCHAR(256));