-- Script creates the table id_not_null on MySQL server.

-- The database name will be passed as an argument of the mysql command
DROP TABLE IF EXISTS id_not_null;
CREATE TABLE id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256));
