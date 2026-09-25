-- # Write your MySQL query statement below

SELECT tweet_id FROM Tweets WHERE LENGTH(content) > 15;

/*

Input:

| tweet_id | content                           |
| -------- | --------------------------------- |
| 1        | Let us Code                       |
| 2        | More than fifteen chars are here! |


Output:

| tweet_id |
| -------- |
| 2        |

*/