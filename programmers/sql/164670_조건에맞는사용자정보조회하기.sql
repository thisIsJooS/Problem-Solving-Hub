--  중고 거래 게시물을 3건 이상 등록한 사용자
-- 전체 주소는 시, 도로명 주소, 상세 주소가 함께 출력되도록 해주시고
-- 전화번호의 경우 xxx-xxxx-xxxx 같은 형태로 하이픈 문자열(-)을 삽입
-- 회원 ID를 기준으로 내림차순 정렬

WITH USERS AS (
    SELECT WRITER_ID
    FROM USED_GOODS_BOARD
    GROUP BY WRITER_ID
    HAVING count(*) >= 3
)

SELECT USER_ID, NICKNAME,
    CONCAT(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) AS 전체주소,
    CONCAT(SUBSTRING(TLNO, 1, 3), '-', SUBSTRING(TLNO, 4, 4), '-', SUBSTRING(TLNO, 8, 4)) AS 전화번호
FROM USED_GOODS_USER
WHERE USER_ID IN (SELECT * FROM USERS)
ORDER BY 1 DESC;