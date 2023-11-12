# Write your MySQL query statement below
select S.student_id, S.student_name, S.subject_name, ifnull(cnt, 0) as attended_exams 
from (select *, count(*) as cnt
      from Examinations
      group by 1,2) E right join (select *
                                from Subjects S1 cross join Students S2) S 
                    on E.student_id=S.student_id  and E.subject_name =S.subject_name 
order by 1,3