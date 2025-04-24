"""
Write a SQL query to delete all duplicate email entries in a table named Person, keeping only unique emails based on its smallest Id.

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Id is the primary key column for this table.
For example, after running your query, the above Person table should have the following rows:

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
"""

create table if not exists person(Id int, email varchar(30));
insert into Person values(1, "john@example.com");
insert into Person values(2, "bob@example.com");
insert into Person values(3, "john@example.com");

-- locate the entries using self join
select p1.* from person p1, person p2 where p1.email=p2.email and p1.id > p2.id;

delete p1.* from person p1, person p2 where p1.email=p2.email and p1.id > p2.id;
