# Write your MySQL query statement below
select query_name, 
        round(sum(rating/position)/count(query_name),2) as quality, 
        round(sum(if(rating<3,'Yes','No')='Yes') /count(rating) * 100,2) as poor_query_percentage 
from Queries
group by query_name 