-- 총주문량이 3,000보다 높으면서 아이스크림의 주 성분이 과일인 아이스크림의 맛
-- 총주문량이 큰 순서대로 조회

SELECT a.FLAVOR
FROM FIRST_HALF AS a
INNER JOIN ICECREAM_INFO AS b
ON a.FLAVOR = b.FLAVOR
WHERE b.INGREDIENT_TYPE LIKE 'f%'
    AND a.TOTAL_ORDER > 3000
ORDER BY a.TOTAL_ORDER DESC;