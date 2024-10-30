-- 물고기 종류 별로 가장 큰 물고기의 ID, 물고기 이름, 길이를 출력
-- 물고기의 ID에 대해 오름차순
-- 물고기 종류별 가장 큰 물고기는 1마리만 있으며 10cm 이하의 물고기가 가장 큰 경우는 없습니다.

WITH MAX_VAL AS (
    SELECT FISH_TYPE, MAX(LENGTH) AS LENGTH
    FROM FISH_INFO
    GROUP BY FISH_TYPE
)

SELECT a.ID AS ID, c.FISH_NAME AS FISH_NAME, a.LENGTH AS LENGTH
FROM FISH_INFO a
INNER JOIN MAX_VAL b
ON a.FISH_TYPE = b.FISH_TYPE AND a.LENGTH = b.LENGTH
INNER JOIN FISH_NAME_INFO c
ON a.FISH_TYPE = c.FISH_TYPE
ORDER BY 1


--
SELECT ID AS ID, b.FISH_NAME AS FISH_NAME, LENGTH AS LENGTH
FROM FISH_INFO a
INNER JOIN FISH_NAME_INFO b
ON a.FISH_TYPE = b.FISH_TYPE
WHERE (a.FISH_TYPE, LENGTH) IN (
    SELECT FISH_TYPE, MAX(LENGTH)
    FROM FISH_INFO
    GROUP BY FISH_TYPE
)

