-- Script creates the table first_table on MySQL server.

-- The database name will be passed as an argument of the mysql command
DROP TABLE IF EXISTS first_table;
CREATE TABLE first_table (
	id INT,
	name VARCHAR(256));
