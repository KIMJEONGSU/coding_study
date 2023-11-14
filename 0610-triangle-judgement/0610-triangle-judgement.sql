# Write your MySQL query statement below
select *, case when abs(x+y) > abs(z) and abs(x+z) > abs(y) and abs(z+y) > abs(x) then 'Yes'
            else 'No'
            end as triangle
from Triangle