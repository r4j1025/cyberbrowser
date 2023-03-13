CREATE DATABASE url_database;

USE url_database;

CREATE TABLE urls (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(255) NOT NULL
);

INSERT INTO urls (url) VALUES
    ('http://faceb00k.com'),
    ('http://www.n3tflix.com'),
    ('http://twitter.0rg'),
    ('http://freemoney.com'),
    ('http://www.trustedbet.org'),
    ('http://amazom.in');
