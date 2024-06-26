# Write your MySQL query statement below
# select player_id, min(event_date) as first_login
# from Activity
# group by player_id

select distinct(player_id), min(event_date) over(partition by player_id) as first_login
from Activity