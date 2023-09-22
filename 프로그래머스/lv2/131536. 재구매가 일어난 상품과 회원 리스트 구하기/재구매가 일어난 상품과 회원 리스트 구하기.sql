-- 코드를 입력하세요
select user_id, product_id from (
SELECT user_id, product_id, count(*) duplicate_purchase
from online_sale
group by user_id, product_id
) t
where duplicate_purchase > 1
order by user_id asc, product_id desc