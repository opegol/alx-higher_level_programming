-- Script creates the table unique_id on MySQL server.

-- The database name will be passed as an argument of the mysql command
DROP TABLE IF EXISTS unique_id;
CREATE TABLE unique_id (
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256));
