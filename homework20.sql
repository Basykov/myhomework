-- TASK1 закоментував, щоб він не змінював кожен раз базу данних.

--create table table_task1(my_value VARCHAR(15)); У мене воно вже створено тому закоментував

--insert into table_task1 (my_value)
--values ('Bb3')

--alter table table_task1 rename to _renamed_t_t1

--alter table _renamed_t_t1 add column my_sec_val INT 

--update  "_renamed_t_t1" set my_sec_val = 3 where my_value = 'Bb3';
--insert into "_renamed_t_t1" (my_value,my_sec_val) values ('Ff2',2);

--delete from "_renamed_t_t1" where my_sec_val = 3;

select my_value, my_sec_val
from _renamed_t_t1;


--TASK2

select first_name as  "First Name", last_name as "Last Name" from "_employees" e ;

select distinct department_id from "_employees" e ;

select * from "_employees" e order by first_name desc;

select first_name, last_name, salary, salary * 0.12 as PF from "_employees" e;

select  MAX(salary) as "Max", MIN(salary) as "Min" from "_employees" e;

select first_name, last_name, ROUND(salary/12, 2) as "Monthly Salary" from "_employees" e ;