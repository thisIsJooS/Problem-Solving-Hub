-- 2022년도 한해 평가 점수가 가장 높은 사원 정보를 조회
-- 2022년도의 평가 점수는 상,하반기 점수의 합

WITH GRADE AS (
    SELECT EMP_NO, SUM(SCORE) AS SCORE
    FROM HR_GRADE
    GROUP BY EMP_NO
)

SELECT b.SCORE, a.EMP_NO, a.EMP_NAME, a.POSITION, a.EMAIL
FROM HR_EMPLOYEES a
INNER JOIN GRADE b
ON a.EMP_NO = b.EMP_NO
WHERE b.SCORE = (SELECT MAX(SCORE) FROM GRADE)


--

SELECT SUM(SCORE) AS SCORE, G.EMP_NO, E.EMP_NAME, E.POSITION, E.EMAIL
FROM HR_EMPLOYEES E
    INNER JOIN HR_GRADE G ON E.EMP_NO = G.EMP_NO
GROUP BY YEAR, EMP_NO
HAVING G.YEAR = '2022'
ORDER BY 1 DESC
LIMIT 1;