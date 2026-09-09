# Write your MySQL query statement below

SELECT user_id, COUNT(follower_id) AS followers_count FROM Followers GROUP BY user_id ORDER BY user_id;

/*

Input 1:

| user_id | follower_id |
| ------- | ----------- |
| 0       | 1           |
| 1       | 0           |
| 2       | 0           |
| 2       | 1           |

Output 1:

| user_id | followers_count |
| ------- | --------------- |
| 0       | 1               |
| 1       | 1               |
| 2       | 2               |

Input 2:

| user_id | follower_id |
| ------- | ----------- |
| 39      | 13          |
| 20      | 76          |
| 54      | 86          |
| 17      | 41          |
| 78      | 27          |
| 56      | 76          |
| 98      | 27          |
| 77      | 53          |
| 78      | 44          |
| 82      | 27          |

Output 2:

| user_id | followers_count |
| ------- | --------------- |
| 17      | 1               |
| 20      | 1               |
| 39      | 1               |
| 54      | 1               |
| 56      | 1               |
| 77      | 1               |
| 78      | 2               |
| 82      | 1               |
| 98      | 1               |

*/