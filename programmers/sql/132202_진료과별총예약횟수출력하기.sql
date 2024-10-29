-- 2022년 5월에 예약한 환자 수를 진료과코드 별로 조회
-- 진료과별 예약한 환자 수를 기준으로 오름차순 정렬
-- 예약한 환자 수가 같다면 진료과 코드를 기준으로 오름차순 정렬

SELECT MCDP_CD AS 진료과코드, count(*) AS '5월예약건수'
FROM APPOINTMENT
WHERE YEAR(APNT_YMD) = 2022 AND MONTH(APNT_YMD) = 5
GROUP BY MCDP_CD
ORDER BY 2, 1

--
WITH NEW_TABLE AS (
    SELECT * FROM APPOINTMENT WHERE YEAR(APNT_YMD) = 2022 AND MONTH(APNT_YMD) = 5
)

SELECT MCDP_CD AS 진료과코드, count(*) AS '5월예약건수'
FROM NEW_TABLE
GROUP BY MCDP_CD
ORDER BY 2, 1

