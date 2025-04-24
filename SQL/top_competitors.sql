/*
this question is posted on hackerrank

related topic: 
join
multi table join
group by having

must review
*/
SELECT 
s.hacker_id,
h.name
from submissions as s
left join hackers as h on s.hacker_id = h.hacker_id
left join challenges as c on s.challenge_id = c.challenge_id
left join difficulty as d on c.difficulty_level = d.difficulty_level
where s.score = d.score
group by s.hacker_id, h.name
having count(s.hacker_id) > 1 
order by count(s.hacker_id) desc, s.hacker_id asc