-- # Write your MySQL query statement below

SELECT x, y, z, 
CASE
    WHEN (x + y > z) AND (x + z > y) AND (y + z > x) THEN "Yes"
    ELSE "No"
END AS triangle
FROM Triangle;

/*

Input:

| x  | y  | z  |
| -- | -- | -- |
| 13 | 15 | 30 |
| 10 | 20 | 15 |

Output:

| x  | y  | z  | triangle |
| -- | -- | -- | -------- |
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |


*/