create table if not exists Employee(id int, salary int);
insert into Employee values(1,100);
insert into Employee values(2,200);
insert into Employee values(3,300);


CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE OFFSET_VAL INT;
  SET OFFSET_VAL = N-1;
  RETURN (
      # Write your MySQL query statement below.
      select distinct salary from Employee order by salary desc limit 1 offset OFFSET_VAL
  );
END