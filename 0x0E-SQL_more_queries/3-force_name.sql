-- Script creates the table force_name on MySQL server.

-- The database name will be passed as an argument of the mysql command
DROP TABLE IF EXISTS force_name;
CREATE TABLE force_name (
	id INT, 
	name VARCHAR(256) NOT NULL);
