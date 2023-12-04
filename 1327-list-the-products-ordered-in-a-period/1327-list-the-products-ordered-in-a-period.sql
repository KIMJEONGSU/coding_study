# Write your MySQL query statement below
select product_name, sum(unit) as unit
from Products P right join Orders O on P.product_id=O.product_id
where order_date like '2020-02-%'
group by product_name
having sum(unit)>=100