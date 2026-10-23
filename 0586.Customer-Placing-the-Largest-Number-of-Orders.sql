-- # Write your MySQL query statement below

SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(customer_number) DESC
LIMIT 1;

/*

Input:

| order_number | customer_number |
| ------------ | --------------- |
| 1            | 1               |
| 2            | 2               |
| 3            | 3               |
| 4            | 3               |

Output:

| customer_number |
| --------------- |
| 3               |

*/