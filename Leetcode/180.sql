-- 180. Consecutive Numbers: Write a SQL query to find all numbers that appear at least three times consecutively.
-- TODO: important
create table if not exists Logs(
    id int,
    num int
);
insert into Logs values(1,1);
insert into Logs values(2,1);
insert into Logs values(3,1);
insert into Logs values(4,2);
insert into Logs values(5,1);
insert into Logs values(6,2);
insert into Logs values(7,2);

select distinct l1.num as ConsecutiveNums from Logs l1, Logs l2, Logs l3 where l1.id=l2.id-1 and l2.id=l3.id-1 and l1.num=l2.num and l2.num = l3.num;