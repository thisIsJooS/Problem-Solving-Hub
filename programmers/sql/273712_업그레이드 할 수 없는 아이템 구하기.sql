-- 더 이상 업그레이드할 수 없는 아이템의 아이템
-- 아이템 ID를 기준으로 내림차순 정렬


SELECT a.ITEM_ID, ITEM_NAME, RARITY
FROM ITEM_INFO a
INNER JOIN ITEM_TREE b
ON a.ITEM_ID = b.ITEM_ID
WHERE a.ITEM_ID NOT IN (SELECT PARENT_ITEM_ID FROM ITEM_TREE WHERE PARENT_ITEM_ID IS NOT NULL)
ORDER BY 1 DESC;

-- ITEM_TREE 테이블의 PARENT_ITEM_ID에는 NULL값이 있기 때문에 IN 연산자 사용시 NULL이 안들어 올 수 있도록 조치를 취해야 한다.
-- IN 연산자는 = 과 같은 역할이기 때문에 비교하려는 대상에 입력값이 없다면 False로 처리함.