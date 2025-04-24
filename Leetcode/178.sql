-- mysql window function
-- http://www.mysqltutorial.org/mysql-window-functions/

create table if not exists scores(id int, score float);
insert into scores value (1, 3.50);
insert into scores value (2, 3.65);
insert into scores value (3, 4.00);
insert into scores value (4, 3.85);
insert into scores value (5, 4.00);
insert into scores value (6, 3.65);

-- for version 8
-- select score, dense_rank() over (order by score desc) from scores;
-- rank() is similar will come with holes

select b.score as score, b.rank as rank from scores as a left join (
    -- increment by score and assign rank
    select c.score, @num:=@num+1 as rank from (select distinct score from scores order by score desc) as c, (select @num:=0) as d
) as b on a.score = b.score order by rank asc;