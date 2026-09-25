-- # Write your MySQL query statement below

SELECT MAX(num) AS num FROM MyNumbers WHERE num IN (SELECT num FROM MyNumbers GROUP BY num HAVING COUNT(num) = 1);

/*

Input:

| num |
| --- |
| 8   |
| 8   |
| 3   |
| 3   |
| 1   |
| 4   |
| 5   |
| 6   |

Output:

| num |
| --- |
| 6   |

*/