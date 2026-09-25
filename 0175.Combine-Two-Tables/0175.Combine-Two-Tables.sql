-- # Write your MySQL query statement below

SELECT Person.firstName, Person.lastName, Address.city, Address.state FROM Person
LEFT JOIN Address ON Person.personID = Address.personID;


/*

Input:

Person = 

| personId | lastName | firstName |
| -------- | -------- | --------- |
| 1        | Wang     | Allen     |
| 2        | Alice    | Bob       |

Address =

| addressId | personId | city          | state      |
| --------- | -------- | ------------- | ---------- |
| 1         | 2        | New York City | New York   |
| 2         | 3        | Leetcode      | California |

Output:

| firstName | lastName | city          | state    |
| --------- | -------- | ------------- | -------- |
| Allen     | Wang     | null          | null     |
| Bob       | Alice    | New York City | New York |


*/
