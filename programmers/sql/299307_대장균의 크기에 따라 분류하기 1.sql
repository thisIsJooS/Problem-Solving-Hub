-- 대장균 개체의 크기가 100 이하라면 'LOW', 100 초과 1000 이하라면 'MEDIUM', 1000 초과라면 'HIGH' 라고 분류
-- 개체의 ID 에 대해 오름차순 정렬

SELECT ID,
    CASE
        WHEN SIZE_OF_COLONY <= 100 THEN 'LOW'
        WHEN SIZE_OF_COLONY <= 1000 THEN 'MEDIUM'
        ELSE 'HIGH'
    END AS SIZE
FROM ECOLI_DATA
ORDER BY 1;