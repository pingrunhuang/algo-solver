-- 183. Customers Who Never Order

create table if not exists Customers(Id int, Name varchar(10));
insert into Customers values(1, "Joe");
insert into Customers values(2, "Henry");
insert into Customers values(3, "Sam");
insert into Customers values(4, "Max");

create table if not exists Orders(Id int, CustomerId int);
insert into Orders values(1, 3);
insert into Orders values(2, 1);

select Name as Customers from Customers left join Orders on Customers.id = Orders.customerId where Orders.id is null;