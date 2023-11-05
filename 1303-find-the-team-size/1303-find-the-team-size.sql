# Write your MySQL query statement below
select employee_id, team_size from ((select employee_id, team_id from Employee) t1 left join (select team_id, count(team_id) as team_size from Employee group by team_id) t2 on t1.team_id = t2.team_id)
