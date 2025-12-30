# Write your MySQL query statement below
select round(count(distinct(player_id))/(select count(distinct(player_id)) from Activity),2) as fraction from 
(select player_id, MIN(event_date) OVER (PARTITION BY player_id) as first_login, event_date from Activity)t0 where DATEDIFF(event_date, first_login) = 1;