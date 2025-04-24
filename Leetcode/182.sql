-- 182. Duplicate Emails
create table if not exists Person(Id int, email varchar(10));
insert into Person values(1, "a@b.com");
insert into Person values(2, "c@d.com");
insert into Person values(3, "a@b.com");

select email from (select email, count(*) as count from person group by email) as t where count>1;

-- having is the alternative way of specifying condition
select Email from Person group by Email having count(Email) > 1;