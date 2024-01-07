select e.first_name, e.last_name, e.department_id, d.department_name
from employees e
join departments d on  e.department_id = d.department_id;

select e.first_name, e.last_name, d.department_name, l.city, l.state_province
from employees e
join departments d on e.department_id = d.department_id
join locations l on d.location_id = l.location_id;

select e.first_name, e.last_name, e.department_id, d.department_name
from employees e
join departments d on e.department_id = d.department_id
where e.department_id in (40, 80);

select d.department_name
from departments d
left join employees e on d.department_id = e.department_id
group by d.department_name;

select e.first_name as employee_name, m.first_name as manager_name
from employees e
left join employees m on e.manager_id = m.employee_id;

select j.job_title, CONCAT(e.first_name, ' ', e.last_name) as full_name, 
       (j.max_salary - e.salary) as salary_difference
from employees e
join jobs j on e.job_id = j.job_id;

select j.job_title, AVG(e.salary) as avg_salary
from employees e
join jobs j on e.job_id = j.job_id
group by j.job_title;

select CONCAT(e.first_name, ' ', e.last_name) as full_name, e.salary
from employees e
join departments d on e.department_id = d.department_id
join locations l on d.location_id = l.location_id
where l.city = 'London';

select d.department_name, COUNT(e.employee_id) as num_employees
from departments d
left join employees e on d.department_id = e.department_id
group by d.department_name;