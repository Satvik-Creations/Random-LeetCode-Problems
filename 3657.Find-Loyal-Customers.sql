-- # Write your MySQL query statement below

SELECT customer_id FROM customer_transactions
GROUP BY customer_id
HAVING
SUM(transaction_type = "purchase") >= 3
AND 
DATEDIFF(MAX(transaction_date), MIN(transaction_date)) >= 30
AND
SUM(transaction_type = "refund")/COUNT(*) < 0.20
ORDER BY customer_id;


/*

Input:

| transaction_id | customer_id | transaction_date | amount | transaction_type |
| -------------- | ----------- | ---------------- | ------ | ---------------- |
| 1              | 101         | 2024-01-05       | 150    | purchase         |
| 2              | 101         | 2024-01-15       | 200    | purchase         |
| 3              | 101         | 2024-02-10       | 180    | purchase         |
| 4              | 101         | 2024-02-20       | 250    | purchase         |
| 5              | 102         | 2024-01-10       | 100    | purchase         |
| 6              | 102         | 2024-01-12       | 120    | purchase         |
| 7              | 102         | 2024-01-15       | 80     | refund           |
| 8              | 102         | 2024-01-18       | 90     | refund           |
| 9              | 102         | 2024-02-15       | 130    | purchase         |
| 10             | 103         | 2024-01-01       | 500    | purchase         |
| 11             | 103         | 2024-01-02       | 450    | purchase         |
| 12             | 103         | 2024-01-03       | 400    | purchase         |
| 13             | 104         | 2024-01-01       | 200    | purchase         |
| 14             | 104         | 2024-02-01       | 250    | purchase         |
| 15             | 104         | 2024-02-15       | 300    | purchase         |
| 16             | 104         | 2024-03-01       | 350    | purchase         |
| 17             | 104         | 2024-03-10       | 280    | purchase         |
| 18             | 104         | 2024-03-15       | 100    | refund           |

Output:

| customer_id |
| ----------- |
| 101         |
| 104         |

*/