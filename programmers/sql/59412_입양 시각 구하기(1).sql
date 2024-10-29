-- 몇 시에 입양이 가장 활발하게 일어나는지
-- 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회
-- 시간대 순으로 정렬

SELECT HOUR(DATETIME) AS HOUR, count(*) AS COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR(DATETIME)
HAVING HOUR BETWEEN 9 AND 19
ORDER BY 1;


