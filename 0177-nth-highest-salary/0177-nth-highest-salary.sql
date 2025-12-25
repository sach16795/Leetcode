CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select distinct(salary) from (select id,salary, dense_rank() over (ORDER BY salary DESC) as x from Employee )t0 where x = N 

  );
END