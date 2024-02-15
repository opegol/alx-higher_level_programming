-- script that creates the MySQL server user user_0d_1

-- The user_0d_1 password should be set to user_0d_1_pwd
DROP USER IF EXISTS 'user_0d_1'@'localhost';
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
