-- 184. Department Highest Salary

create table if not exists Employee(Id int, Name varchar(10), Salary int, DepartmentId int);
insert into Employee values(1, "Joe", 70000, 1);
insert into Employee values(4, "Jim", 90000, 1);
insert into Employee values(2, "Henry", 80000, 2);
insert into Employee values(3, "Sam", 60000, 2);
insert into Employee values(4, "Max", 90000, 1);

create table if not exists Department(Id int, Name varchar(10));
insert into Department values(1, "IT");
insert into Department values(2, "Sales");


-- at the first glance, using one simple group by seems work. But turns out we might only get one entry for each group

select dep.Name as "Department", emp.Name as "Employee", emp.Salary as "Salary" from employee as emp join department as dep on emp.DepartmentId = dep.Id where (emp.DepartmentId, emp.Salary) in (select DepartmentId, max(Salary) from employee group by DepartmentId);