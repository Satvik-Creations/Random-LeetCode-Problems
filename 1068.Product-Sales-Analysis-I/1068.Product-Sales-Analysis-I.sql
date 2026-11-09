-- # Write your MySQL query statement below

SELECT P.product_name, S.year, S.price FROM Sales S
LEFT JOIN Product P ON S.product_id = P.product_id

/*

Input:

Sales=

| sale_id | product_id | year | quantity | price |
| ------- | ---------- | ---- | -------- | ----- |
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |

Product=

| product_id | product_name |
| ---------- | ------------ |
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |

Output:

| product_name | year | price |
| ------------ | ---- | ----- |
| Nokia        | 2009 | 5000  |
| Nokia        | 2008 | 5000  |
| Apple        | 2011 | 9000  |

*/