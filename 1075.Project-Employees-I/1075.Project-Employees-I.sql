# Write your MySQL query statement below

SELECT P.project_id, ROUND(AVG(E.experience_years),2) AS average_years FROM Project P
INNER JOIN Employee E
ON P.employee_id = E.employee_id
GROUP BY P.project_id;


/*

Input:

Project=

| project_id | employee_id |
| ---------- | ----------- |
| 1          | 1           |
| 1          | 2           |
| 1          | 3           |
| 2          | 1           |
| 2          | 4           |

Employee=

| employee_id | name   | experience_years |
| ----------- | ------ | ---------------- |
| 1           | Khaled | 3                |
| 2           | Ali    | 2                |
| 3           | John   | 1                |
| 4           | Doe    | 2                |

Output:

| project_id | average_years |
| ---------- | ------------- |
| 1          | 2             |
| 2          | 2.5           |

*/