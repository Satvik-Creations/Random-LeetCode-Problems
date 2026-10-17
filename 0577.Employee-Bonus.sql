-- # Write your MySQL query statement below

SELECT E.name, B.bonus FROM Employee E LEFT JOIN Bonus B
ON E.empID = B.empId
WHERE B.Bonus < 1000 OR B.Bonus IS NULL;

/*

Input:

Employee =

| empId | name   | supervisor | salary |
| ----- | ------ | ---------- | ------ |
| 3     | Brad   | null       | 4000   |
| 1     | John   | 3          | 1000   |
| 2     | Dan    | 3          | 2000   |
| 4     | Thomas | 3          | 4000   |

Bonus =

| empId | bonus |
| ----- | ----- |
| 2     | 500   |
| 4     | 2000  |

Output:

| name | bonus |
| ---- | ----- |
| Brad | null  |
| John | null  |
| Dan  | 500   |

*/

