# Write your MySQL query statement below
SELECT DISTINCT email FROM Person GROUP BY email HAVING COUNT(email) > 1;

/*
Input:

| id | email   |
| -- | ------- |
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |

*/