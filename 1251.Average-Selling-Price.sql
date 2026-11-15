-- # Write your MySQL query statement below

SELECT P.product_id,
CASE
    WHEN SUM(US.units) IS NULL OR (US.units) = 0 THEN 0
    ELSE ROUND(SUM(P.price * US.units)/SUM(units),2)
END AS average_price
FROM Prices P
LEFT JOIN UnitsSold US
ON P.product_id = US.product_id
AND US.purchase_date BETWEEN P.start_date AND P.end_date
GROUP BY product_id;


/*

Input1:

Prices=

| product_id | start_date | end_date   | price |
| ---------- | ---------- | ---------- | ----- |
| 1          | 2019-02-17 | 2019-02-28 | 5     |
| 1          | 2019-03-01 | 2019-03-22 | 20    |
| 2          | 2019-02-01 | 2019-02-20 | 15    |
| 2          | 2019-02-21 | 2019-03-31 | 30    |

UnitsSold=

| product_id | purchase_date | units |
| ---------- | ------------- | ----- |
| 1          | 2019-02-25    | 100   |
| 1          | 2019-03-01    | 15    |
| 2          | 2019-02-10    | 200   |
| 2          | 2019-03-22    | 30    |

Output1:

| product_id | average_price |
| ---------- | ------------- |
| 1          | 6.96          |
| 2          | 16.96         |

Input2:

Prices=

| product_id | start_date | end_date   | price |
| ---------- | ---------- | ---------- | ----- |
| 1          | 2023-01-01 | 2023-01-31 | 10    |
| 2          | 2023-01-01 | 2023-01-31 | 20    |

UnitsSold=

| product_id | purchase_date | units |
| ---------- | ------------- | ----- |

Output2:

| product_id | average_price |
| ---------- | ------------- |
| 1          | 0             |
| 2          | 0             |

Input3:

Prices=

| product_id | start_date | end_date   | price |
| ---------- | ---------- | ---------- | ----- |
| 1          | 2024-01-01 | 2024-12-31 | 20    |

UnitsSold=

| product_id | purchase_date | units |
| ---------- | ------------- | ----- |
| 1          | 2024-02-01    | 0     |

Output3:

| product_id | average_price |
| ---------- | ------------- |
| 1          | 0             |

*/