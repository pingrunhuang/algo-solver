-- 181. Employees Earning More Than Their Managers
create table if not exists Employee(Id int, Name varchar(10), Salary int, ManagerId int);
insert into Employee values(1, "Joe", 70000, 3);
insert into Employee values(2, "Henry", 80000, 4);
insert into Employee values(3, "Sam", 60000, NULL);
insert into Employee values(4, "Max", 90000, NULL);

-- my solution 
 select x.Name as Employee from employee as x where x.Salary > (select y.Salary from employee y where y.Id = x.ManagerId);


-- join solution
SELECT a.NAME AS Employee FROM Employee AS a JOIN Employee AS b ON a.ManagerId = b.Id AND a.Salary > b.Salary;

-- 2 tables
select a.Name as "Employee" from Employee as a, Employee as b where a.ManagerId=b.Id and a.Salary > b.Salary;