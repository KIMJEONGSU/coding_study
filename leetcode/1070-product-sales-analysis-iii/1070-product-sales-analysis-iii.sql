# Write your MySQL query statement below
with t as
(select *,RANK() over(partition by product_id order by year) as num
from Sales)

select product_id, year as first_year, quantity,price 
from t
where num=1

#처음에는 row_number을 사용했는데 rank를 사용해야함.
#ROW_NUMBER는 중복을 허용하지 않고, DENSE_RANK/RANK 는 중복을 허용한다는 것