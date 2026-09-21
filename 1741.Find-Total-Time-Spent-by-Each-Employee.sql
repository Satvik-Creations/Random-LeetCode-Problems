-- # Write your MySQL query statement below

SELECT event_day AS day, emp_id, SUM(out_time - in_time) AS total_time FROM Employees GROUP BY day, emp_id ORDER BY total_time;


/*

Input:

| emp_id | event_day  | in_time | out_time |
| ------ | ---------- | ------- | -------- |
| 1      | 2020-11-28 | 4       | 32       |
| 1      | 2020-11-28 | 55      | 200      |
| 1      | 2020-12-3  | 1       | 42       |
| 2      | 2020-11-28 | 3       | 33       |
| 2      | 2020-12-9  | 47      | 74       |


Output:

| day        | emp_id | total_time |
| ---------- | ------ | ---------- |
| 2020-11-28 | 1      | 173        |
| 2020-12-03 | 1      | 41         |
| 2020-11-28 | 2      | 30         |
| 2020-12-09 | 2      | 27         |

*/