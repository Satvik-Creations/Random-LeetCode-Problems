-- # Write your MySQL query statement below

SELECT user_id, COUNT(user_id) AS prompt_count, ROUND(AVG(tokens),2) AS avg_tokens FROM prompts
GROUP BY user_id
HAVING prompt_count >= 3 AND MAX(tokens) > ROUND(AVG(tokens),2)
ORDER BY avg_tokens DESC, user_id ASC;

/*

Input:

| user_id | prompt                  | tokens |
| ------- | ----------------------- | ------ |
| 1       | Write a blog outline    | 120    |
| 1       | Generate SQL query      | 80     |
| 1       | Summarize an article    | 200    |
| 2       | Create resume bullet    | 60     |
| 2       | Improve LinkedIn bio    | 70     |
| 3       | Explain neural networks | 300    |
| 3       | Generate interview Q&A  | 250    |
| 3       | Write cover letter      | 180    |
| 3       | Optimize Python code    | 220    |

Output:

| user_id | prompt_count | avg_tokens |
| ------- | ------------ | ---------- |
| 3       | 4            | 237.5      |
| 1       | 3            | 133.33     |


*/