# Write your MySQL query statement below

SELECT class from Courses GROUP BY class HAVING COUNT(class) >= 5;

/*
Input:

| student | class    |
| ------- | -------- |
| A       | Math     |
| B       | English  |
| C       | Math     |
| D       | Biology  |
| E       | Math     |
| F       | Computer |
| G       | Math     |
| H       | Math     |
| I       | Math     |


Output:

| class |
| ----- |
| Math  |

*/