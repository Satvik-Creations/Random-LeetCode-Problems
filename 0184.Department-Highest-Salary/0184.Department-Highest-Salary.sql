SELECT Department.name AS Department, Employee.name AS Employee, Employee.salary AS Salary FROM Employee
INNER JOIN Department ON Employee.departmentId = Department.id
WHERE Employee.salary IN (SELECT MAX(salary) FROM Employee E2 WHERE E2.departmentId = Employee.departmentId);

/*

Input:

Employee = 

| id | name  | salary | departmentId |
| -- | ----- | ------ | ------------ |
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |

Department =

| id | name  |
| -- | ----- |
| 1  | IT    |
| 2  | Sales |


Output:

| Department | Employee | Salary |
| ---------- | -------- | ------ |
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |


*/