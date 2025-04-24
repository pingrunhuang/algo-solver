-- This question is posted by hackerrank in advanced select the pads
/*
related topic:
case when
group by
alias table
string concatenation
*/
select concat(name,"(",substring(occupation,1,1),")") from occupations order by name asc;

select
case 
    when num>1 then concat("There are a total of ", num, " ", lower(occupation), "s.")
    else concat("There are a total of ", num, " ", lower(occupation), ".")
end as result from (
select count(occupation) as num, occupation from occupations group by occupation
order by occupation asc) as newtable order by num asc;


