# Write your MySQL query statement below
select A1.machine_id, round(avg(A2.timestamp-A1.timestamp),3) as processing_time 
from Activity A1 inner join Activity A2
where A1.machine_id=A2.machine_id and A1.process_id=A2.process_id and a1.activity_type='start' and a2.activity_type='end'
group by A1.machine_id