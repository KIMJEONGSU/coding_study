# Write your MySQL query statement below
select E.employee_id, E.name, T.reports_count, T.average_age
from (select count(reports_to) as reports_count, reports_to, round(avg(age)) as average_age
        from Employees
        group by reports_to) T join Employees E
        on T.reports_to=E.employee_id
order by employee_id
        