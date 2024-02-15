-- creates the database hbtn_0d_2 and the user user_0d_2

-- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
DROP DATABASE IF EXISTS hbtn_0d_2;
CREATE DATABASE hbtn_0d_2;
DROP USER IF EXISTS user_0d_2@localhost;
CREATE USER user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
