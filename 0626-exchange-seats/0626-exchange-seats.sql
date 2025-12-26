# Write your MySQL query statement below
select id, 
case 
    when id%2 = 1  and lead(student,1) over (order by id) is null  then student
    when id%2 = 0 then lag(student,1) over (order by id) 
    when id%2 = 1 then lead(student,1) over (order by id)
END as student
from Seat