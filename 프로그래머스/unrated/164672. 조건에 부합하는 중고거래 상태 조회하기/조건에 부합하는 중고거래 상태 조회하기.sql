-- 코드를 입력하세요
SELECT
    board_id,
    writer_id,
    title,
    price,
    case when status = 'sale' then '판매중'
    when status = 'reserved' then '예약중'
    when status = 'done' then '거래완료' end as status
    from USED_GOODS_BOARD
    where year(created_Date) = 2022 and month(created_Date) = 10 and day(created_Date) = 5
    order by board_id desc;