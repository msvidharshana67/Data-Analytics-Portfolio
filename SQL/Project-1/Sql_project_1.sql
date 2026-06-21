create schema project;
use project;

create table departments
(
id int primary key,
dept_name varchar(50),
location varchar(50)
);

insert into departments values 
(1,"IT","Delhi"),
(2,"Sales","Mumbai"),
(3,"HR","Chennai"),
(4,"Marketing","Bangalore"),
(5,"Finance","Delhi");

create table products
(
id int primary key,
product_name varchar(50),
category varchar(50),
price int
);

insert into products values 
(1,"Laptop","Electronics",50000),
(2,"Mobile","Electronics",20000),
(3,"iPhone","Electronics",80000),
(4,"Chair","Furniture",5000),
(5,"Table","Furniture",12000),
(6,"Book","Books",500);

create table accounts
(
id int primary key,
account_holder varchar(100),
balance int
);

insert into accounts values 
(1,"Ram",50000),
(2,"Sita",40000),
(3,"John",30000);

-- 1.	Display all students older than 20, sorted by age descending.
 
select * from students where age > 20
order by age desc; 

-- 2.	Fetch distinct cities where students are enrolled.

select distinct(city) from students;

-- 3.	List top 3 highest-paid employees.

select name,salary from employees order by salary desc
limit 3;

-- 4.	Show employees whose salary is between 40,000 and 90,000.

select name,salary from employees where salary between 40000 and 90000; 

-- 5.	Find employees from Sales or Marketing earning more than 50,000.

select e.name,e.salary,d.dept_name from employees as e
inner join departments as d
on e.dept_id = d.id
where dept_name in ("Sales","Marketing") and salary > 50000;

-- 6.	Retrieve customers whose names start with ‘A’ and end with ‘a’.

select * from customers where customer_name like "A%a";

-- 7.	Find products not belonging to Electronics category.

select product_name from products where not category = "Electronics";

-- 8.	Display employees who do not have a bonus.

update employees set bonus = null where bonus = "";
select name from employees where bonus is null;

-- 9.	Fetch orders placed in the last 30 days.

SELECT * FROM orders
WHERE order_date BETWEEN CURDATE() - INTERVAL 30 DAY AND CURDATE();

-- 10.	Show students whose age is NOT between 18 and 22.

select name,age from students where not age between 18 and 22;

-- 11.	Use CASE to label employees as Junior, Mid, Senior based on salary.

select name,salary,
case
when salary >= 80000 then "Senior"
when salary >= 45000 then "Mid"
else "Junior"
end as e_position
from employees;

-- 12.	Count how many students belong to each city.

select city,count(*) as student_count from students group by city;

-- 13.	List employees sorted by department then salary descending.

select e.name,e.salary,d.dept_name from employees as e
left join departments as d
on e.dept_id = d.id 
order by dept_name,salary desc;

-- 14.	Display first 5 records skipping the first 3.

select * from employees limit 3,5;

-- 15.	Find customers whose email is NULL.

update customers set email = null where email = "";
select * from customers where email is null;

---------------------------------------------------------------------

-- 16.	Display full name of employees using CONCAT. (concating name and dept_id)

select concat(name," ",dept_id) as emp_name_dept_id from employees;

-- 17.	Convert all product names to uppercase.

select upper(product_name) as Product_Name from products;

-- 18.	Find length of each customer name.

select customer_name,length(customer_name) as cust_name_len from customers;

-- 19.	Extract first 4 letters of product name.

select left(product_name,4) as product_name from products;

-- 20.	Replace word “Phone” with “Mobile” in product names.

select replace(product_name,"Phone","Mobile") as replace_pro from products;

-- 21.	Trim spaces from customer names.

select trim(customer_name) as cust_trim from customers;

-- 22.	Display employee name as emp_name and salary as income.

select name as emp_name, salary as income from employees;

-- 23.	Show product name and category combined as one column.

select concat(product_name," ",category) as product from products;

-- 24.	Convert city names to lowercase.

select lower(city) as cities from customers;

-- 25.	Display first name and last name separately from full name.

select substring_index(customer_name, ' ', 1) as first_name,
substring_index(customer_name, ' ', -1) as last_name
from customers;

---------------------------------------------------------------------------------------------------------------

-- 26.	Display employee name with department name.

select e.name,d.dept_name from employees as e
left join departments as d on e.dept_id = d.id;

-- 27.	Show all employees even if they don’t belong to any department.

select e.name,d.dept_name from employees as e
left join departments as d on e.dept_id = d.id ;

-- select * from employees where dept_id is null;  there is no null 

-- 28.	Find departments with no employees.

select d.dept_name from departments as d
left join employees as e on d.id = e.dept_id 
where e.emp_id is null;

-- 29.	Display employee and their manager name (SELF JOIN).

select e.name as emp_name,m.name as man_name from employees as e 
left join employees as m on e.manager_id = m.emp_id ;  

-- 30.	List all customers with their order amounts.

select c.customer_name,o.order_amount from customers as c 
left join orders as o on c.cust_id = o.customer_id;

-- 31.	Show customers who never placed an order.

select c.customer_name from customers as c 
left join orders as o on c.cust_id = o.customer_id 
where o.ord_id is null;

-- 32.	Find products that were never sold.

select p.product_name from products as p 
left join order_items as o on p.id = o.product_id
where o.product_id is null; 

-- 33.	Display total sales per product with product category.

select p.product_name,p.category,sum(s.sales_amount) as total_sales from products as p 
left join sales as s on p.id = s.product_id 
group by p.product_name,p.category;

-- 34.	Show employees working in departments located in ‘Delhi’.

select e.name,d.dept_name from employees as e 
left join departments as d on e.dept_id = d.id
where d.location = "Delhi";

-- 35.	Find orders along with customer name and city.

select o.ord_id,c.customer_name,c.city from orders as o
left join customers as c on o.customer_id = c.cust_id ;

-- 36.	Display employees earning more than their manager.

select e.name,e.salary from employees as e inner join employees as m on e.manager_id = m.emp_id 
where e.salary > m.salary;

-- 37.	Show each department’s total salary expense.

select d.dept_name,sum(e.salary) as total_salary_exp from departments as d
left join employees as e on d.id = e.dept_id 
group by d.dept_name;

-- 38.	List orders with product and customer details.

select o.ord_id,c.customer_name,c.city,p.product_name,oi.quantity from orders as o 
inner join customers as c on o.customer_id = c.cust_id
inner join order_items as oi on o.ord_id = oi.order_id
inner join products as p on oi.product_id = p.id ;

-- 39. Find employees who do NOT have a manager.

select * from employees where manager_id is null;

-- 40.	Find departments having more than 3 employees.

select d.dept_name,count(e.emp_id) as emp_count from departments as d
left join employees as e on d.id = e.dept_id
group by d.dept_name 
having emp_count > 3;

---------------------------------------------------------------------------------------------------------------------

-- 41.	Find total number of employees.

select count(emp_id) as total_employees from employees;

-- 42.	Calculate average salary per department.

select d.dept_name,avg(e.salary) as average_salary from departments as d
left join employees as e on d.id = e.dept_id 
group by d.id,d.dept_name;

-- 43.	Find max and min salary in each department.

select d.dept_name,min(e.salary) as min_salary,max(e.salary) as max_salary from departments as d
left join employees as e on d.id = e.dept_id 
group by d.id,d.dept_name;

-- 44.	Count number of orders per customer.

select c.customer_name, count(o.ord_id) as no_of_orders from customers as c
left join orders as o on c.cust_id = o.customer_id
group by c.cust_id,c.customer_name;

-- 45.	Find total sales amount per day.

select sale_date , sum(sales_amount) as sales_amount from sales group by sale_date;

-- 46.	Display products with total quantity sold > 10.

select p.product_name, sum(oi.quantity) as quantity_sold from products as p
left join order_items as oi on p.id = oi.product_id 
group by p.product_name 
having quantity_sold > 10;

-- 47.	Find departments with average salary above 60,000.

select d.dept_name,avg(e.salary) as average_salary from departments as d
left join employees as e on d.id = e.dept_id 
group by d.dept_name
having average_salary > 60000;

-- 48.	Show cities having more than 2 students.

select city,count(std_id) as stud_count from students
group by city having stud_count > 2;

-- 49.	Find customers who placed more than 2 orders.

select c.customer_name, count(o.ord_id) as no_of_orders from customers as c
left join orders as o on c.cust_id = o.customer_id
group by c.cust_id,c.customer_name
having no_of_orders > 2;

-- 50.	Display product category wise revenue.

select p.category,sum(s.sales_amount) as revenue from products as p
left join sales as s on p.id = s.product_id 
group by p.category;

-- 51.	Find employees whose salary is above department average. 

select e.name, e.salary, e.dept_id from employees e
where e.salary > (select avg(salary) from employees where dept_id = e.dept_id);

-- 52.	Count how many employees earn bonus.

select count(emp_id) as bonus_earn_emp from employees where bonus is not null;

-- 53.	Show highest paid employee per department.

select e.name,e.dept_id,e.salary from employees as e
where e.salary = 
(select max(salary) from employees where dept_id = e.dept_id)
order by e.dept_id asc;

-- 54.	Find days with sales more than daily average.

select order_date, sum(order_amount) as total_sales from orders
group by order_date
having sum(order_amount) > (select avg(daily_total) from 
(select sum(order_amount) as daily_total from orders group by order_date) as tab2 );

-- 55.	Calculate total inventory value per category.

select p.category, sum(oi.quantity * p.price) as total_invetory from products as p
left join order_items as oi on p.id = oi.product_id
group by p.category;

---------------------------------------------------------------------------------------------------------------

-- 56.	Find employees earning more than company average salary.

select name,salary from employees where salary >
(select avg(salary) from employees);

-- 57.	List students scoring above class average.

select name,mark from students where mark >
(select avg(mark) from students);

-- 58.	Find customers who placed at least one order.

select distinct c.customer_name from customers as c 
inner join orders as o on c.cust_id = o.customer_id;

-- 59.	Find customers who placed no orders.

select customer_name from customers where cust_id not in 
(select customer_id from orders);

-- 60.	Display products priced higher than average price.

select product_name,price from products where price > 
(select avg(price) from products);

-- 61.	Find employee with second highest salary.

select name,salary from employees order by salary desc limit 1 offset 1;

-- 62.	Display departments with salary expense above average.

select d.dept_name,sum(e.salary) as total_salary from employees as e left join departments as d on e.dept_id = d.id
group by d.dept_name 
having sum(e.salary) > 
(select avg(dept_total) from
(select sum(salary) as dept_total from employees group by dept_id)
as t1);

-- 63.	Find customers who ordered both Laptop and Mobile.

select c.customer_name from customers as c 
join orders as o on c.cust_id = o.customer_id 
join order_items as oi on o.ord_id = oi.order_id 
join products as p on p.id = oi.product_id
where p.product_name in ("Laptop","Mobile")
group by c.customer_name
having count(distinct p.product_name)=2;

-- 64.	Show employees whose salary equals department max salary.

select * from employees as e where salary = (select max(salary) from employees where dept_id=e.dept_id);

-- 65.	Find products sold more than average quantity.
 
 select product_id, sum(quantity) as total_qty from order_items 
 group by product_id 
 having sum(quantity) > (select avg(total_qty) from 
 (select sum(quantity) as total_qty from order_items group by product_id) as t2); 
 
-- 66.	Find latest order per customer.

select c.customer_name,c.cust_id, max(o.order_date) as latest_order from customers as c
join orders as o on c.cust_id = o.customer_id 
group by c.cust_id,c.customer_name;

-- 67.	Display employees working in departments with no bonus employees.

select d.dept_name from departments d where d.id not in (
select distinct dept_id from employees where bonus is not null);

-- 68.	Find customers who placed orders worth more than 10,000.

select c.customer_name,o.order_amount from customers as c 
left join orders as o on c.cust_id = o.customer_id 
where o.order_amount > 7000;

-- 69.	Show employees whose manager earns less than them.

select e.name,e.salary from employees as e left join
employees as m on e.manager_id = m.emp_id
where e.salary > m.salary;

-- 70.	Find top 3 selling products using subquery.

select product_id,total_qty from (
select product_id,sum(quantity) as total_qty from order_items group by product_id ) as tab3
order by total_qty desc limit 3;
	
-------------------------------------------------------------------------------------------------------

-- 71.	Dense rank employees within each department.

select name,dept_id,salary,
dense_rank() over (partition by dept_id order by salary desc) as d_rank
from employees;

-- 72.	Show running total of sales by date.

select product_id,sale_date,sales_amount, 
sum(sales_amount) over (order by sale_date) as running_total
from sales;

-- 73.	Find top 2 earners per department.

select name,dept_name,salary,top_earn from (
select e.name,d.dept_name,e.salary,
dense_rank() over (partition by e.dept_id order by e.salary desc ) as top_earn
from employees as e left join departments as d on e.dept_id = d.id ) as ranked_data
where top_earn <=2 ;

-- 74.	Calculate moving average of sales (last 3 days).

select product_id,sale_date,sales_amount, 
avg(sales_amount) over (order by sale_date 
rows between 2 preceding and current row ) as moving_avg
from sales;

-- 75.	Assign row numbers to orders by date.

select o.*,
row_number () over(order by order_date ) as row_num
from orders as o;

-- 76.	Find highest sale per day using window function.

select * from (select s.*, rank() over(partition by sale_date order by sales_amount desc) as high_sale
from sales as s) as tab1 where high_sale = 1;

-- 77.	Compare each employee salary with department average.

select name,salary,
avg(salary) over (partition by dept_id ) as dept_avg ,
case 
    when salary > avg(salary) over (partition by dept_id) then 'Above Avg'
    when salary < avg(salary) over (partition by dept_id) then 'Below Avg'
    else 'Equal'
end as comparison
from employees;

-- 78.	Show cumulative quantity sold per product.

select product_id,
sum(quantity) over (partition by product_id order by order_id) as cum_qty
from order_items;

-- 79.	Rank customers based on total purchase amount.
 
select customer_id,sum(order_amount) as total_purchase,
dense_rank() over(order by sum(order_amount) desc) as rank_cust
from orders group by customer_id;

----------------------------------------------------------------------------------------------------------
-- 81.	Insert 3 new students in a single query.

insert into students values 
(109,"Avni",21,"Bangalore",94),
(110,"Ananya",23,"chennai",85),
(111,"Shree",19,"Delhi",76);

-- 82.	Update salary by 10% for Sales employees.

update employees as e left join departments as d on e.dept_id = d.id
set e.salary = e.salary * (10/100) where d.dept_name = "Sales";

-- 83.	Delete customers with no orders.

delete from customers where cust_id not in (select customer_id from orders);

-- 84.	Demonstrate COMMIT and ROLLBACK using account transfer.

start transaction;
update accounts set balance = balance - 1000 where id = 2;
update accounts set balance = balance + 1000 where id = 1;

rollback; -- if updated data is wrong can rollback;
commit;  -- if data is correct then commit;

-- 85.	Truncate temporary table.

create table std1
(student_id int ,
student_name varchar(50),
department_id int
);

insert into std1 values
(1,"aira",101),
(2,"dhivya",102),
(3,"nandhu",103),
(4,"sarika",104);

truncate table std1;

-- 86.	Create a view for high salary employees.

create or replace view high_salary as
select * from employees order by salary desc limit 10;         

create or replace view high_salary_2 as
select * from employees where salary > 65000;

-- 87.	Update data using view.

update high_salary_2 set bonus = bonus + 200 where emp_id = 68;

-- 88.	Drop an existing view.

drop view high_salary;

-- 89.	Create index on customer email.

alter table customers modify email varchar(100) unique;
create index cust_mail on customers(email);

-- 90.	Show indexes on orders table.

show index from orders;

-- 91.	Create procedure to fetch employee by id.

delimiter //
create procedure emp_details (in id int)
begin
select * from employees where emp_id = id;
end //

call emp_details(75);

-- 92.	Create procedure to count total orders.

delimiter //
create procedure total_orders ()
begin
select count(*) as total_orders from orders;
end //

call total_orders();

-- 93.	Create function to calculate tax (10%).

delimiter //
create function tax (p_id int)
returns decimal(10,2)
deterministic
begin
declare tx decimal(10,2);
select price into tx from products where id = p_id;
set tx = tx * (10/100);
return tx;
end //

select tax(4);

-- 94.	Create trigger to log inserts on orders.

create table log_data (
log_id int auto_increment primary key,
order_id int,
log_data_type varchar(20),
log_time datetime
);

delimiter // 
create trigger log_insert
after insert on orders
for each row
begin
insert into log_data values (new.ord_id,"INSERT",now());   
end //

-- 95.	Create trigger to log deletes on customers.

create table log_data_cust (
log_id int auto_increment primary key,
customer_id int,
log_data_type varchar(20),
log_time datetime
);

delimiter // 
create trigger log_delete
after delete on customers
for each row
begin
insert into log_data_cust values (old.cust_id,"DELETE",now());   
end //

-- 96.	Create event to delete old logs monthly.

create event old_logs_delete
on schedule every 1 month
starts '2026-03-31 11:59:00'
do
delete from log_data where log_time < now() - interval 1 month;

-- 97.	Identify which constraints create indexes automatically.

-- Primary key, unique

-- 98.	Difference scenario using DELETE vs TRUNCATE.

delete from std1 where std_id = 1; -- delete row by row,can rollback  
truncate table std1;  -- deletes whole datas fastly, can't rollback.

-- 99.	Restore database from backup.

-- 100.	Export sales report to CSV.


