-- (PRODUCT_CODE 앞 2자리) 별 상품 개수를 출력
--  상품 카테고리 코드를 기준으로 오름차순 정렬

SELECT SUBSTRING(PRODUCT_CODE, 1, 2) AS CATEGORY, count(*) AS PRODUCTS
FROM PRODUCT
GROUP BY SUBSTRING(PRODUCT_CODE, 1, 2)
ORDER BY 1

-- SUBSTRING(string, start, length)
