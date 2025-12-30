# Write your MySQL query statement below
select id, visit_date, people from 
(select id, visit_date, people,
lag(people,1) over (order by id) as negone, 
lag(people,2) over (order by id) as negtwo, 
lead(people,1) over (order by id) as posone, 
lead(people,2) over (order by id) as postwo from Stadium)t0 
where people >=100 and ((negone >=100 and negtwo  >=100)  or (negone  >=100 and posone >=100) or (posone >=100 and postwo >=100))order by id 