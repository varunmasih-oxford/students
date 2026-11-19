create database C415;
use c415;

create table franchises(
franchise_name varchar(100),
inception_year INT,
total_revenue_busd decimal(10,2),
original_medium varchar (50),
owner varchar(100),
n_movies INT);	



INSERT INTO franchises(franchise_name, inception_year, total_revenue_busd, original_medium, owner, n_movies)
VALUES 
    ('Star Wars', 1977, 46.7, 'movie', 'The Walt Disney Company', 12),
    ('Mickey Mouse and Friends', 1928, 52.2, 'cartoon', 'The Walt Disney Company', 33),
    ('Anpanman', 1973, 38.4, 'book', 'Froebel-kan', 33),
    ('Winnie the Pooh', 1924, 48.5, 'book', 'The Walt Disney Company', 6),
    ('Pokémon', 1996, 88, 'video game', 'The Pokémon Company', 24),
    ('Disney Princess', 2000, 45.4, 'movie', 'The Walt Disney', NULL);




select * from franchises; -- all rows all column
select franchise_name from franchises; 
select franchise_name,total_revenue_busd from franchises; 

select franchise_name as Name ,total_revenue_busd as Revenue from franchises; 
select 
franchise_name as Name,
total_revenue_busd as Revenue 
from franchises ORDER BY Revenue; 

select 
franchise_name as Name,
total_revenue_busd as Revenue 
from franchises ORDER BY Revenue DESC; 

select 
franchise_name as Name,
total_revenue_busd as Revenue 
from franchises ORDER BY Revenue DESC LIMIT 2; 

select 
distinct owner
from franchises;

select 
franchise_name as Name,
total_revenue_busd as Revenue 
from franchises
WHERE total_revenue_busd <> 52.20; 




