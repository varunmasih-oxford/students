create database franchise;
use franchise;
CREATE TABLE Franchise (
    franchise_name VARCHAR(100),
    inception_year INT,
    total_revenue_busd DECIMAL(10, 2),
    original_medium VARCHAR(50),
    owner VARCHAR(100),
    n_movies INT
);
select * from franchise_tbl;

-- alter table Franchise RENAME TO Franchise_tbl; 
INSERT INTO Franchise_tbl (franchise_name, inception_year, total_revenue_busd, original_medium, owner, n_movies)
VALUES 
    ('Star Wars', 1977, 46.7, 'movie', 'The Walt Disney Company', 12),
    ('Mickey Mouse and Friends', 1928, 52.2, 'cartoon', 'The Walt Disney Company', 33),
    ('Anpanman', 1973, 38.4, 'book', 'Froebel-kan', 33),
    ('Winnie the Pooh', 1924, 48.5, 'book', 'The Walt Disney Company', 6),
    ('Pokémon', 1996, 88, 'video game', 'The Pokémon Company', 24),
    ('Disney Princess', 2000, 45.4, 'movie', 'The Walt Disney', NULL);
