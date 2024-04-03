create database patils;
use patils;

CREATE TABLE usera (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(100) NOT NULL
);

INSERT INTO usera (username, password) VALUES
('Guru', 'Guru'),
('user2', 'password2'),
('user3', 'password3');

select * from usera;
