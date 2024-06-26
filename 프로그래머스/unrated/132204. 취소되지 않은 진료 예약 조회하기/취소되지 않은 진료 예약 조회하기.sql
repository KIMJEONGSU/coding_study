-- 코드를 입력하세요
# SELECT A.APNT_NO , P.PT_NAME, A.PT_NO, A.MCDP_CD, D.DR_NAME, A.APNT_YMD 
# FROM (SELECT * 
#       FROM APPOINTMENT
#       WHERE MCDP_CD='CS' 
#       AND DATE_FORMAT(APNT_YMD,'%Y-%m-%d') = '2022-04-13' 
#       AND APNT_CNCL_YN='N' ) A 
      
#       JOIN DOCTOR D ON A.MDDR_ID=D.DR_ID
#       JOIN PATIENT P ON A.PT_NO=P.PT_NO
# ORDER BY A.APNT_NO ASC 
# 다른 컬럼을 사용해서 오답이었던것.



SELECT A.APNT_NO, P.PT_NAME, A.PT_NO, D.MCDP_CD, D.DR_NAME, A.APNT_YMD
FROM APPOINTMENT A
INNER JOIN PATIENT P ON A.PT_NO = P.PT_NO 
INNER JOIN DOCTOR  D ON A.MDDR_ID = D.DR_ID
WHERE DATE_FORMAT(A.APNT_YMD,'%Y-%m-%d') = '2022-04-13' 
AND A.APNT_CNCL_YN = 'N'
AND A.MCDP_CD = 'CS'
ORDER BY APNT_YMD ASC
