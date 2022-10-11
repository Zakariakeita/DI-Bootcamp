-- Database: hr. backup

-- DROP DATABASE IF EXISTS "hr. backup";

CREATE DATABASE "hr. backup"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
	
	
--Write a query to display the names (first_name, last_name) using an alias name “First Name”, “Last Name” from employee table.
   SELECT first_name AS "First Name", last_name AS "Last Name" FROM employees
--Write a query to get a unique department ID from employee table.
   SELECT DISTINCT department_id FROM employees;
--Write a query to get the details of all employees from the employee table in descending order by their first name.
   SELECT * FROM employees ORDER BY first_name DESC;
--Write a query to get the names (first_name, last_name), salary and 15% of salary as PF (ie. alias) for all the employees.
   SELECT first_name, last_name, salary, ROUND(salary*0.15, 2) AS PF FROM employees;
--Write a query to get the employee ID, names (first_name, last_name) and salary in ascending order according to their salary.
   SELECT employee_id, first_name, last_name, salary FROM employees ORDER BY salary;
--Write a query to get the total sum of all salaries paid to the employees.
   SELECT SUM(salary) FROM employees;
--Write a query to get the maximum and minimum salary paid to the employees.
   SELECT max(salary), min(salary) FROM employees
--Write a query to get the average salary paid to the employees.
    SELECT ROUND(AVG(salary),2) FROM employees;
--Write a query to get the number of employees working with the company.
    select count(employee_id) from employees;
--Write a query to get all the first name from the employees table in upper case.
    SELECT UPPER(first_name) FROM employees;
--Write a query to get the first three characters of the first name for all the employees in the employees table.
    SELECT SUBSTRING(first_name FOR 3) FROM employees;
--Write a query to get the full name of all the employees from employees table. You have to include the first name and last name
    SELECT CONCAT(first_name, ' ', last_name) FROM employees;
--Write a query to get the first name, last name and the length of the full name of all the employees from employees table.
    SELECT first_name, last_name, LENGTH(CONCAT(first_name, ' ', last_name)) FROM employees;
--Write a query to check whether the first_name column of the employees table containing any number.
    SELECT * FROM employees WHERE first_name ~ '\d';
--Write a query to select first ten records from a table.
    SELECT * FROM employees LIMIT 10;
--Restricting And Sorting
--Write a query to display the name, including first_name and last_name and salary for all employees whose salary is out of the range between $10,000 and $15,000.
    SELECT first_name, last_name, salary FROM employees WHERE salary BETWEEN 10000 AND 15000
--Write a query to display the name, including first_name and last_name and hire date for all employees who were hired in 1987.
    SELECT CONCAT(first_name, ' ', last_name) "Full name", hire_date FROM employees WHERE DATE_PART('year', hire_date) = 1987;
--Write a query to get the first name of the employee who holds the letter ‘c’ and ‘e’ in the first name.
    SELECT first_name FROM employees WHERE first_name ILIKE '%c%e%'
--Write a query to display the last name, job, and salary for all those employees who hasn’t worked as a Programmer or a Shipping Clerk, and not drawing the salary $4,500, $10,000, or $15,000.
    SELECT first_name, last_name, job_title, salary FROM employees join jobs ON employees.job_id = jobs.job_id WHERE job_title NOT IN ('Programmer', 'Shipping Clerk') AND salary NOT IN ('4500', '10000', '15000')
--Write a query to display the last names of employees whose last name contain exactly six characters.
    SELECT last_name FROM employees WHERE LENGTH(last_name) = 6
--Write a query to display the last name of employees having ‘e’ as the third character.
    SELECT last_name FROM employees WHERE last_name LIKE '__e%'
--Write a query to display the jobs/designations available in the employees table.
    SELECT DISTINCT job_title FROM employees INNER JOIN jobs ON employees.job_id = jobs.job_id;
--Write a query to select all information of employees whose last name is either ‘JONES’ or ‘BLAKE’ or ‘SCOTT’ or ‘KING’ or ‘FORD’.
    SELECT * FROM employees WHERE last_name IN ('JONES', 'BLAKE', 'SCOTT', 'KING', 'FORD')