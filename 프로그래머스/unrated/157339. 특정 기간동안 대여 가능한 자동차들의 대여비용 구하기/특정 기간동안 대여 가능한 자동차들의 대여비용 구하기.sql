-- 코드를 입력하세요
SELECT CC.CAR_ID, 
       CC.CAR_TYPE,
       ROUND(CC.DAILY_FEE * 30 * (1 - CD.DISCOUNT_RATE / 100)) AS FEE
FROM CAR_RENTAL_COMPANY_CAR CC
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN CD ON CC.CAR_TYPE = CD.CAR_TYPE
WHERE CC.CAR_TYPE IN ('세단', 'SUV') 
  AND CC.CAR_ID NOT IN (
      SELECT CAR_ID
      FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
      WHERE END_DATE >= '2022-11-01'
  ) 
  AND CD.DURATION_TYPE = '30일 이상'
  AND CC.DAILY_FEE * 30 * (1 - CD.DISCOUNT_RATE / 100) >= 500000 
  AND CC.DAILY_FEE * 30 * (1 - CD.DISCOUNT_RATE / 100) < 2000000
ORDER BY FEE DESC, CAR_TYPE, CAR_ID DESC;
