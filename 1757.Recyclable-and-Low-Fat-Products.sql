-- # Write your MySQL query statement below

SELECT product_id FROM Products WHERE low_fats = "Y" AND recyclable = "Y";


/*

Input:

Products=

| product_id | low_fats | recyclable |
| ---------- | -------- | ---------- |
| 0          | Y        | N          |
| 1          | Y        | Y          |
| 2          | N        | Y          |
| 3          | Y        | Y          |
| 4          | N        | N          |

Output:

| product_id |
| ---------- |
| 1          |
| 3          |


*/