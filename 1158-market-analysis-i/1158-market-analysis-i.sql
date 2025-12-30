# Write your MySQL query statement below
select t1.buyer_id, join_date,coalesce(orders_in_2019,0) as orders_in_2019  from (select user_id as buyer_id, join_date from Users) t1 left join 
(select buyer_id, count(item_id) as orders_in_2019  from Orders where extract(year from order_date)='2019' group by buyer_id)t2 on t1.buyer_id = t2.buyer_id 