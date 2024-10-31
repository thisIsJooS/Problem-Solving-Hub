-- # A : Front End 스킬과 Python 스킬을 함께 가지고 있는 개발자
-- # B : C# 스킬을 가진 개발자
-- # C : 그 외의 Front End 개발자
--
-- # GRADE가 존재하는 개발자의 GRADE, ID, EMAIL을 조회
-- # GRADE와 ID를 기준으로 오름차순 정렬


WITH TMP AS (
    SELECT
        CASE
            WHEN SKILL_CODE & (SELECT SUM(CODE) FROM SKILLCODES WHERE CATEGORY='Front End')
                AND SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME='Python') THEN 'A'
            WHEN SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME='C#') THEN 'B'
            WHEN SKILL_CODE & (SELECT SUM(CODE) FROM SKILLCODES WHERE CATEGORY='Front End') THEN 'C'
            ELSE NULL
        END AS GRADE,
        ID,
        EMAIL
    FROM DEVELOPERS
)

SELECT *
FROM TMP
WHERE GRADE IS NOT NULL
ORDER BY 1, 2;