"""
Given a Weather table, write a SQL query to find all dates' Ids with higher temperature compared to its previous (yesterday's) dates.

+---------+------------------+------------------+
| Id(INT) | RecordDate(DATE) | Temperature(INT) |
+---------+------------------+------------------+
|       1 |       2015-01-01 |               10 |
|       2 |       2015-01-02 |               25 |
|       3 |       2015-01-03 |               20 |
|       4 |       2015-01-04 |               30 |
+---------+------------------+------------------+
For example, return the following Ids for the above Weather table:

+----+
| Id |
+----+
|  2 |
|  4 |
+----+
"""


create table if not exists Weather(Id int, RecordDate DATE, Temperature int);
insert into Weather values(1, "2015-01-01", 10);
insert into Weather values(2, "2015-01-02", 25);
insert into Weather values(3, "2015-01-03", 20);
insert into Weather values(4, "2015-01-04", 30);


select w2.id as Id from weather w1, weather w2 where DATEDIFF(w2.recorddate, w1.recorddate) = 1 and w1.temperature<w2.temperature;