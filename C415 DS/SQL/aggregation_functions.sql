use c415;

SELECT * from franchises;

SELECT count(*)
from franchises; 

SELECT count(n_movies)
from franchises; 

SELECT sum(total_revenue_busd)
from franchises; 

SELECT avg(total_revenue_busd)
from franchises; 

SELECT max(total_revenue_busd)
from franchises; 

SELECT min(total_revenue_busd)
from franchises; 

SELECT 
original_medium,
avg(total_revenue_busd)
from franchises
group by original_medium; 