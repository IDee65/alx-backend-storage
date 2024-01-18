-- Active: 1691578679906@@127.0.0.1@5432@plg

-- CREATE table users with id, name, email

CREATE TABLE
    IF NOT EXISTS users (
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        email VARCHAR(255) NOT NULL UNIQUE,
        name VARCHAR(255)
    );
