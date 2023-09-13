# Write your MySQL query statement below
select user_id, case when sum(num)=0 then 0.00
                     when sum(num)!=0 then round(sum(num)/count(num),2)
                     when num is null then 0.00
                     end as confirmation_rate 
from (select S.user_id , case when C.action='timeout' then 0
                        when C.action='confirmed' then 1
                        end as num
    from Signups S left join Confirmations C on S.user_id=C.user_id) T
group by user_id