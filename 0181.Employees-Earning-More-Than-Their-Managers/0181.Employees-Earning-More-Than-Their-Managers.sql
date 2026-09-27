-- # Write your MySQL query statement below 

SELECT E.name AS Employee FROM Employee E
JOIN Employee M ON E.managerId = M.id
WHERE E.salary > M.salary;


/*

Input:

| id | name  | salary | managerId |
| -- | ----- | ------ | --------- |
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | null      |
| 4  | Max   | 90000  | null      |

Output:

| Employee |
| -------- |
| Joe      |

*/