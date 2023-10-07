# Write your MySQL query statement below
select firstName, lastName, city, state from Person t1 left Join Address t2 on t1.personId=t2.personId;