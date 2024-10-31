-- 2022년 1월의 도서 판매 데이터를 기준
-- 저자 ID를 오름차순으로, 저자 ID가 같다면 카테고리를 내림차순 정렬

WITH SALES AS (
    SELECT BOOK_ID, SUM(SALES) AS SALES
    FROM BOOK_SALES
    WHERE YEAR(SALES_DATE) = 2022 AND MONTH(SALES_DATE) = 1
    GROUP BY BOOK_ID
)

SELECT a.AUTHOR_ID, b.AUTHOR_NAME, a.CATEGORY, SUM(SALES*PRICE) AS TOTAL_SALES
FROM BOOK a
INNER JOIN AUTHOR b ON a.AUTHOR_ID = b.AUTHOR_ID
INNER JOIN SALES c ON a.BOOK_ID = c.BOOK_ID
GROUP BY b.AUTHOR_NAME, a.CATEGORY
ORDER BY 1, 3 DESC