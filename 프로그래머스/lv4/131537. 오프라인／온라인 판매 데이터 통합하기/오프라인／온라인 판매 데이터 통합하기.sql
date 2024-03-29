-- 코드를 입력하세요
SELECT date_format(sales_date, '%Y-%m-%d') as sales_date, PRODUCT_ID, USER_ID, SALES_AMOUNT FROM ONLINE_SALE 
WHERE MONTH(SALES_DATE) = 3
AND YEAR(SALES_DATE) = 2022
UNION
SELECT date_format(sales_date, '%Y-%m-%d') as sales_date, PRODUCT_ID, NULL as USER_ID, SALES_AMOUNT FROM OFFLINE_SALE
WHERE MONTH(SALES_DATE) = 3
AND YEAR(SALES_DATE) = 2022
ORDER BY SALES_DATE, PRODUCT_ID, USER_ID ASC;