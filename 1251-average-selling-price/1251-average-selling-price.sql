# Write your MySQL query statement below
select distinct(P.product_id), ifnull(round(sum(P.price*US.units)/sum(US.units),2),0) as average_price 
from Prices P left join UnitsSold US on P.product_id=US.product_id 
                                  AND US.purchase_date BETWEEN P.start_date AND P.end_date
group by P.product_id