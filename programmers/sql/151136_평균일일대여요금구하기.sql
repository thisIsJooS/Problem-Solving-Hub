-- 자동차 종류가 'SUV'인 자동차들의 평균 일일 대여 요금을 출력
-- 평균 일일 대여 요금은 소수 첫 번째 자리에서 반올림

SELECT ROUND(AVG(DAILY_FEE)) AS AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV';
