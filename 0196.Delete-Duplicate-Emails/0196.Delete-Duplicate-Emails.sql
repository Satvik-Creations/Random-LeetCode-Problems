DELETE P2 FROM Person P1 JOIN Person P2 ON P1.email = P2.email AND P1.id < P2.id;

/*

Input: 

| id | email            |
| -- | ---------------- |
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |

Output:

| id | email            |
| -- | ---------------- |
| 1  | john@example.com |
| 2  | bob@example.com  |

*/