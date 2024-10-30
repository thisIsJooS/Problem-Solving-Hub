-- 자동차 종류가 '세단'인 자동차들 중
--  10월에 대여를 시작한 기록이 있는 자동차 ID 리스트를 출력
-- 리스트는 중복이 없어야 하며,
-- 자동차 ID 기준 내림차순 정렬

WITH TMP AS (
    SELECT DISTINCT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE MONTH(START_DATE) = 10
)

SELECT CAR_ID
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_ID IN (SELECT * FROM TMP) AND CAR_TYPE = '세단'
ORDER BY 1 DESC;