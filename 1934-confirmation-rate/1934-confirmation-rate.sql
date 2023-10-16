# Write your MySQL query statement below
select B.user_id, ifnull(round(min(A.confirmation_rate)/count(A.confirmation_rate),2),0) as confirmation_rate 
from (select user_id,
       sum(if(action='confirmed',1,0)) over (partition by user_id) as confirmation_rate 
      from Confirmations) A right join Signups B on A.user_id=B.user_id
group by B.user_id