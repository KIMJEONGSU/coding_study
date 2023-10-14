# Write your MySQL query statement below
select round(count(if(scheduled_or_immediate='scheduled',null,scheduled_or_immediate))/count(customer_id)*100,2) as immediate_percentage 
from (select customer_id, scheduled_or_immediate, ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS row_num
from (select *,
             case when order_date = customer_pref_delivery_date then 'immediate'
             else 'scheduled'
             end scheduled_or_immediate
      from Delivery
      order by customer_id, order_date) A) B
where row_num=1