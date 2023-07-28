'''
URL = https://school.programmers.co.kr/learn/courses/30/lessons/164673

사용언어 = MySQL

문제 설명
다음은 중고거래 게시판 정보를 담은 USED_GOODS_BOARD 테이블과 중고거래 게시판 첨부파일 정보를 담은 USED_GOODS_REPLY 테이블입니다. USED_GOODS_BOARD 테이블은 다음과 같으며 BOARD_ID, WRITER_ID, TITLE, CONTENTS, PRICE, CREATED_DATE, STATUS, VIEWS은 게시글 ID, 작성자 ID, 게시글 제목, 게시글 내용, 가격, 작성일, 거래상태, 조회수를 의미합니다.

문제 
USED_GOODS_BOARD와 USED_GOODS_REPLY 테이블에서 2022년 10월에 작성된 게시글 제목, 게시글 ID, 댓글 ID, 댓글 작성자 ID, 댓글 내용, 댓글 작성일을 조회하는 SQL문을 작성해주세요. 결과는 댓글 작성일을 기준으로 오름차순 정렬해주시고, 댓글 작성일이 같다면 게시글 제목을 기준으로 오름차순 정렬해주세요.
'''

SQL = '''
SELECT UGB.TITLE, 
       UGB.BOARD_ID, 
       UGR.REPLY_ID, 
       UGR.WRITER_ID, 
       UGR.CONTENTS, 
       DATE_FORMAT(UGR.CREATED_DATE,'%Y-%m-%d')
FROM USED_GOODS_BOARD AS UGB INNER JOIN USED_GOODS_REPLY AS UGR ON UGB.BOARD_ID=UGR.BOARD_ID
WHERE UGB.CREATED_DATE LIKE '2022-10%'
ORDER BY UGR.CREATED_DATE, UGB.TITLE
'''

# 조인할때 = 대신 AND를 쓰는 실수를 했음.
# DATE_FORMAT() 사용법에 대해 좀 더 알아보기 - https://www.tutorialspoint.com/mysql/mysql_date_time_functions_date_format.htm
