--  만원 단위의 가격대 별로 상품 개수를 출력
-- 가격대를 기준으로 오름차순 정렬

SELECT FLOOR(PRICE / 10000) * 10000 AS PRICE_GROUP, count(*) AS PRODUCTS
FROM PRODUCT
GROUP BY FLOOR(PRICE / 10000)
ORDER BY 1