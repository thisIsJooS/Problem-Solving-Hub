-- 10cm 이하일 경우에는 LENGTH 가 NULL 이며, LENGTH 에 NULL 만 있는 경우는 없습니다.
-- 가장 큰 물고기 10마리의 ID와 길이를 출력하는 SQL 문을 작성해주세요
-- 길이 기준 내림차순, 길이가 같다면 ID 에 대해 오름차순
-- 가장 큰 물고기 10마리 중 NULL 인 경우는 없다.

SELECT ID, LENGTH
FROM FISH_INFO
WHERE LENGTH IS NOT NULL
ORDER BY LENGTH DESC, ID
LIMIT 10;