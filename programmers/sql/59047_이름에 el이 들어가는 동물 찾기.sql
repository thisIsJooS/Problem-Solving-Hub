-- 이름에 "EL"이 들어가는 개의 아이디와 이름을 조회
-- 이름 순으로 조회

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE LOWER(NAME) LIKE '%el%' AND ANIMAL_TYPE = 'Dog'
ORDER BY 2;

