-- 분화된 연도별 대장균 크기의 편차: (분화된 연도별 가장 큰 대장균의 크기) - (각 대장균의 크기)
-- 연도에 대해 오름차순으로 정렬, 대장균 크기의 편차 오름차순

WITH MAX_SIZE AS (
    SELECT MAX(SIZE_OF_COLONY) AS SIZE, YEAR(DIFFERENTIATION_DATE) AS YEAR
    FROM ECOLI_DATA
    GROUP BY YEAR(DIFFERENTIATION_DATE)
)

SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR,
    (SELECT SIZE FROM MAX_SIZE WHERE YEAR=YEAR(DIFFERENTIATION_DATE)) - SIZE_OF_COLONY AS YEAR_DEV,
    ID
FROM ECOLI_DATA
ORDER BY 1, 2;