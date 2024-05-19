-- Task: 
-- Script to setup MySQL for hbnb_test database

-- Create hbnb_test_db if not exists
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create user hbnb_test if not exists
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges to hbnb_test user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
