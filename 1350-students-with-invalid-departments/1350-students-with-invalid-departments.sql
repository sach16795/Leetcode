# Write your MySQL query statement below
 select id, name from (select Students.id as id, Students.name as name, Departments.id as did from Students left join Departments on Students.department_id = Departments.id) t1 where did is null