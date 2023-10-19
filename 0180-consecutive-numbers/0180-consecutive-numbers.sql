# Write your MySQL query statement below
select distinct num as ConsecutiveNums 
from (select num,lead(num) over() num2, lead(num,2) over() num3
      from Logs) T
where num=num2 and num2=num3
