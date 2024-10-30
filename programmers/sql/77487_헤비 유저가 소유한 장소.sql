-- 공간을 둘 이상 등록한 사람을 "헤비 유저"
-- 헤비 유저가 등록한 공간의 정보를 아이디 순으로 조회


WITH TMP AS (
    SELECT HOST_ID
    FROM PLACES
    GROUP BY HOST_ID
    HAVING count(*) >= 2
)

SELECT *
FROM PLACES
WHERE HOST_ID IN (SELECT * FROM TMP)


