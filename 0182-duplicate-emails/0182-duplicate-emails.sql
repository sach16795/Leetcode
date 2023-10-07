# Write your MySQL query statement below
select email from (select email, count(email) as cnt from Person group by email having cnt >1 ) t1