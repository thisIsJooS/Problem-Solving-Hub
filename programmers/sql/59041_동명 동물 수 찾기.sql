-- 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회
-- 이름 순으로 조회

SELECT NAME, count(*) AS COUNT
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(*) >= 2 AND NAME IS NOT NULL
ORDER BY 1;

