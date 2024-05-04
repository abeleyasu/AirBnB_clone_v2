-- Task:
-- Script to setup MySQL for hbnb_dev database

-- Create hbnb_dev_db if not exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create user hbnb_dev if not exists
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant privileges to hbnb_dev user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
