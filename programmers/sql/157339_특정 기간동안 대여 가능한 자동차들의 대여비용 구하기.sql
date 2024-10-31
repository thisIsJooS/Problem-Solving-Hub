-- # 자동차 종류가 '세단' 또는 'SUV' 인 자동차
-- # 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능
-- # 30일간의 대여 금액이 50만원 이상 200만원 미만
--
-- # 대여 금액을 기준으로 내림차순 정렬
-- # 자동차 종류를 기준으로 오름차순 정렬,
-- # 자동차 ID를 기준으로 내림차순 정렬

WITH DISCOUNT AS (
    SELECT CAR_TYPE, (1-DISCOUNT_RATE*0.01) AS RATE -- 10% 이면 0.9 로 저장됨
    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    WHERE CAR_TYPE IN ('SUV', '세단')
        AND DURATION_TYPE = '30일 이상'
)

SELECT
    CAR_ID,
    CAR_TYPE,
    ROUND(DAILY_FEE * 30 * RATE) AS FEE
FROM CAR_RENTAL_COMPANY_CAR
JOIN DISCOUNT USING (CAR_TYPE)
WHERE CAR_ID NOT IN (SELECT DISTINCT CAR_ID
                     FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                     WHERE END_DATE > '2022-11-01')
    AND CAR_TYPE IN ('SUV', '세단')
    AND DAILY_FEE * 30 * RATE >= 500000
    AND DAILY_FEE * 30 * RATE < 2000000
ORDER BY 3 DESC, 2, 1 DESC