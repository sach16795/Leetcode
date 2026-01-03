# Write your MySQL query statement below
select round(count(distinct(player_id))/(select count(distinct(player_id)) from Activity ),2) as fraction from 
(select player_id, FIRST_VALUE(event_date) over (partition by player_id order by event_date) as login, event_date from Activity) t0 where DATEDIFF(event_date,login) =1