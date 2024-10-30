-- 대여 시작일을 기준으로 2022년 8월부터 2022년 10월까지 총 대여 횟수가 5회 이상인 자동차들에 대해서
-- 해당 기간 동안의 월별 자동차 ID 별 총 대여 횟수
-- 월을 기준으로 오름차순 정렬
-- 자동차 ID를 기준으로 내림차순 정렬
-- 월의 총 대여 횟수가 0인 경우에는 결과에서 제외

WITH TMP AS (
    SELECT CAR_ID, MONTH(START_DATE) AS MONTH
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE YEAR(START_DATE) = 2022 AND MONTH(START_DATE) IN (8, 9, 10)
),
TMP2 AS (
    SELECT CAR_ID
    FROM TMP
    GROUP BY CAR_ID
    HAVING count(*) >= 5
)

SELECT MONTH, CAR_ID, count(*) AS RECORDS
FROM TMP
WHERE CAR_ID IN (SELECT * FROM TMP2)
GROUP BY MONTH, CAR_ID
ORDER BY 1, 2 DESC


