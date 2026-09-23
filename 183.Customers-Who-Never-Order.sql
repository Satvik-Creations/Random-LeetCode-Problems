-- # Write your MySQL query statement below

SELECT name AS Customers FROM Customers
WHERE Customers.id NOT IN (SELECT customerID AS id FROM Orders);


/*

Input:

Customers = 

| id | name  |
| -- | ----- |
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |

Orders =

| id | customerId |
| -- | ---------- |
| 1  | 3          |
| 2  | 1          |

Output:

| Customers |
| --------- |
| Henry     |
| Max       |

*/