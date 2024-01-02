ql syntax to create a database with one table and one row
-- in primary server to replicate from

CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 (
	id INTEGER,
	name VARCHAR(255)
);
INSERT INTO nexus6 (id, name) VALUES (1, "Joe Mama");
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
