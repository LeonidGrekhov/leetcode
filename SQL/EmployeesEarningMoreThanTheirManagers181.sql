/*
181. Employees Earning More Than Their Managers
Easy
2.2K
217
Companies
SQL Schema
Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+
id is the primary key column for this table.
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.
 

Write an SQL query to find the employees who earn more than their managers.

Return the result table in any order.

The query result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |
+----+-------+--------+-----------+
Output: 
+----------+
| Employee |
+----------+
| Joe      |
+----------+
Explanation: Joe is the only employee who earns more than his manager.
*/

create table employee (id INT NOT NULL auto_increment, name varchar(255) NOT NULL, salary INT, managerId INT, primary key (id) );
INSERT INTO `175_combine_two_tables`.`employee` (`id`, `name`,`salary`, `managerId`) VALUES ('1', 'Joe', '70000', '3');
INSERT INTO `175_combine_two_tables`.`employee` (`id`, `name`,`salary`, `managerId`) VALUES ('2', 'Henry', '80000', '4');
INSERT INTO `175_combine_two_tables`.`employee` (`id`, `name`,`salary`) VALUES ('3', 'Sam', '60000');
INSERT INTO `175_combine_two_tables`.`employee` (`id`, `name`,`salary`) VALUES ('4', 'Max', '90000');
select * from employee;

select e1.Name AS employee
from employee e1 JOIN employee e2
on e1.managerID = e2.id
where e1.salary > e2.salary;