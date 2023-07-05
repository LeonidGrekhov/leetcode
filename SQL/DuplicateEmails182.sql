/*
182. Duplicate Emails
Easy
1.8K
62
Companies
SQL Schema
Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key column for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
 

Write an SQL query to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.

Return the result table in any order.

The query result format is in the following example.

 

Example 1:

Input: 
Person table:
+----+---------+
| id | email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
Output: 
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Explanation: a@b.com is repeated two times.
*/
CREATE TABLE IF NOT EXISTS Person (id INT, email VARCHAR(255));
TRUNCATE TABLE Person;
INSERT INTO Person (id, email) VALUES ('1', 'a@b.com');
INSERT INTO Person (id, email) VALUES ('2', 'c@d.com');
INSERT INTO Person (id, email) VALUES ('3', 'a@b.com');
SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(*) > 1;