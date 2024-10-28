-- 나이 정보가 없는 회원은 몇 명?

SELECT count(*) AS USERS
FROM USER_INFO
WHERE AGE IS NULL;