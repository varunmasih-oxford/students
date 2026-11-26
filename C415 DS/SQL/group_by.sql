use c415;

SELECT * from franchises;



SELECT COUNT(*) from franchises;

-- group && aggr
SELECT original_medium, COUNT(*) as "total count" from franchises GROUP BY original_medium;
SELECT 
owner, SUM(n_movies) as "total movies"
from franchises
GROUP by owner;
SELECT 
owner, AVG(total_revenue_busd) as avg_sales
from franchises
GROUP by owner
HAVING avg_sales > 50
ORDER BY AVG(total_revenue_busd) desc;



SELECT 
original_medium, SUM(total_revenue_busd) as tota_rev 
from franchises 
WHERE owner = 'The Walt Disney Company'
GROUP BY original_medium
HAVING tota_rev > 50
ORDER BY original_medium;

SELECT * from franchises
ORDER BY total_revenue_busd DESC
LIMIT 3,2;

show TABLES;

select CURDATE();
select CURTIME();
select NOW();



