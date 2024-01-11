-- 코드를 입력하세요
SET @MAXPRICE = (select max(price) from food_product);

SELECT *
from food_product
where price = @MAXPRICE