-- 코드를 입력하세요
SELECT date_format(sales_date, '%Y-%m-%d') as sales_date, product_id, user_id, sales_amount
from online_sale
where month(sales_date) = 3
union all
SELECT date_format(sales_date, '%Y-%m-%d') as sales_date, product_id, NULL, sales_amount
from offline_sale
where month(sales_date) = 3
order by 1,2,3

