# Write your MySQL query statement below
select user_id, concat(upper(left(name,1)),substring(lower(name),2,length(name))) as name
from Users
order by user_id