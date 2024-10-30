-- 일부 동물의 입양일이 잘못 입력
-- 보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름을 조회
-- 보호 시작일이 빠른 순으로 조회

WITH TMP AS (
    SELECT a.ANIMAL_ID, a.NAME, a.DATETIME AS START, b.DATETIME AS END
    FROM ANIMAL_INS a
    INNER JOIN ANIMAL_OUTS b
    ON a.ANIMAL_ID = b.ANIMAL_ID
)

SELECT ANIMAL_ID, NAME
FROM TMP
WHERE END-START < 0
ORDER BY START


