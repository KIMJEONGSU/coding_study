# Write your MySQL query statement below
select P.product_id, round(sum(P.price*US.units)/sum(US.units),2) as average_price 
from Prices P cross join UnitsSold US on P.product_id=US.product_id and P.start_date <= US.purchase_date and US.purchase_date <= P.end_date
group by P.product_id