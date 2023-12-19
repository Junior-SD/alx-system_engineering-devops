ql syntax to create the user and grant permission
-- to use "cat create_user.sql | mysql -uroot -p"
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY '';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
