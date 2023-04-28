-- 코드를 입력하세요
SELECT 
    HISTORY_ID,
    CAR_ID,
    DATE_FORMAT(START_DATE, '%Y-%m-%d') as START_DATE,
    DATE_FORMAT(END_DATE, '%Y-%m-%d') as END_DATE,
    case when datediff(END_DATE, START_DATE) >= 29 then '장기 대여'
    else '단기 대여'
    end as rent_type
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where year(start_date) = 2022 and month(start_date) = 9
order by history_id desc;