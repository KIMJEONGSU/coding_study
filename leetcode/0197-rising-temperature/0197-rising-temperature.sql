# 첫풀이(submit 실패)
# select id
# from (SELECT LEAD(id) over() as id ,LEAD(temperature) over() as temp , temperature
#     FROM Weather) T
# where temp > temperature

# 날짜를 기준으로 다시 작성
select A.id
from Weather A join Weather B on A.recordDate = DATE_ADD(B.recordDate,interval 1 day)
where A.temperature > B.temperature
