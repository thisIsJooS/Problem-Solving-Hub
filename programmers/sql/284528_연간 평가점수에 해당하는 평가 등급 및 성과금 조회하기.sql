-- 평가 점수별 등급과 등급에 따른 성과금 정보가 아래와 같을 때, 사번, 성명, 평가 등급, 성과금을 조회
-- 결과는 사번 기준으로 오름차순 정렬


WITH

FINAL_SCORE AS (
    SELECT EMP_NO, AVG(SCORE) AS SCORE
    FROM HR_GRADE
    GROUP BY EMP_NO
),

TMP AS (
    SELECT a.EMP_NO AS EMP_NO, a.EMP_NAME AS EMP_NAME, a.SAL AS SAL,
        CASE
            WHEN b.SCORE >= 96 THEN 'S'
            WHEN b.SCORE >= 90 THEN 'A'
            WHEN b.SCORE >= 80 THEN 'B'
            ELSE 'C'
        END AS GRADE
    FROM HR_EMPLOYEES a
    INNER JOIN FINAL_SCORE b
    ON a.EMP_NO = b.EMP_NO
)

SELECT EMP_NO, EMP_NAME, GRADE,
    CASE
        WHEN GRADE = 'S' THEN ROUND(SAL * 0.2)
        WHEN GRADE = 'A' THEN ROUND(SAL * 0.15)
        WHEN GRADE = 'B' THEN ROUND(SAL * 0.1)
        ELSE 0
    END AS BONUS
FROM TMP