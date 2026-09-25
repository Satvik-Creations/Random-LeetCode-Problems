-- # Write your MySQL query statement below

SELECT user_id, max(time_stamp) as last_stamp FROM Logins WHERE time_stamp >= "2020-01-01 00:00:00" AND time_stamp <= "2020-12-31 23:59:59" GROUP BY user_id ORDER BY user_id DESC;

/*
Input:

| user_id | time_stamp          |
| ------- | ------------------- |
| 6       | 2020-06-30 15:06:07 |
| 6       | 2021-04-21 14:06:06 |
| 6       | 2019-03-07 00:18:15 |
| 8       | 2020-02-01 05:10:53 |
| 8       | 2020-12-30 00:46:50 |
| 2       | 2020-01-16 02:49:50 |
| 2       | 2019-08-25 07:59:08 |
| 14      | 2019-07-14 09:00:00 |
| 14      | 2021-01-06 11:59:59 |

Output:

| user_id | last_stamp          |
| ------- | ------------------- |
| 6       | 2020-06-30 15:06:07 |
| 8       | 2020-12-30 00:46:50 |
| 2       | 2020-01-16 02:49:50 |

*/