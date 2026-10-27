SELECT * FROM Users
WHERE email REGEXP '^[A-Za-z0-9_]+@[A-Za-z]+[.]com$'
-- REGEXP (REGULAR EXPRESSION PICKED UP FROM GOOGLE SEARCH)
ORDER BY user_id;

/*

Input:

| user_id | email               |
| ------- | ------------------- |
| 1       | alice@example.com   |
| 2       | bob_at_example.com  |
| 3       | charlie@example.net |
| 4       | david@domain.com    |
| 5       | eve@invalid         |

Output:

| user_id | email             |
| ------- | ----------------- |
| 1       | alice@example.com |
| 4       | david@domain.com  |

*/