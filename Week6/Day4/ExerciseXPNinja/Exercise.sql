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

--Write a query to find the first_name, last_name and salaries of the employees who have a higher salary than the employee whose last_name is Bull.
SELECT first_name, last_name,salary FROM employees WHERE salary >(SELECT salary FROM employees WHERE last_name='Bull');
select * from employees where country_id='US'
--Write a SQL subquery to find the first_name and last_name of the employees under a manager who works for a department based in the United States.
--Hint : Write single-row and multiple-row subqueries
SELECT e.first_name, e.last_name FROM employees e 
WHERE e.manager_id IN(SELECT DISTINCT em.employee_id FROM employees em
				  WHERE em.department_id IN (SELECT DISTINCT d.department_id FROM departments d
									   WHERE d.location_id IN(SELECT l.location_id FROM locations l
														  WHERE l.country_id =(SELECT co.country_id FROM countries co
																		WHERE co.country_name='United States of America'))));


--Write a SQL subquery to find the first_name and last_name of the employees who are working as managers.
SELECT first_name, last_name FROM employees WHERE (employee_id IN (SELECT manager_id FROM employees));

--Write a SQL subquery to find the employee(s) first_name and last_name, which salary is greater than the average salary of the employees.
SELECT first_name, last_name, salary FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);

--Write a SQL subquery to find the employee(s) first_name and last_name, which salary is equal to the minimum salary of their job position.
SELECT first_name, last_name, salary FROM employees  WHERE employees.salary = (SELECT min_salary FROM jobs WHERE employees.job_id = jobs.job_id);

--Write a query to find the names (first_name, last_name) of the employees who are not supervisors.
SELECT b.first_name,b.last_name FROM employees b WHERE NOT EXISTS (SELECT 'X' FROM employees a WHERE a.manager_id = b.employee_id);

--Write a SQL subquery to find the employee(s) ID, first name, last name and salary of all employees whose salary is above the average salary for their departments.
SELECT employee_id, first_name FROM employees AS A WHERE salary > (SELECT AVG(salary) FROM employees WHERE department_id = A.department_id);

--Write a subquery to find the 5th maximum salary of all salaries.
SELECT DISTINCT salary FROM employees e1 WHERE 5 = (SELECT COUNT(DISTINCT salary) FROM employees  e2 WHERE e1.salary <= e2.salary);
--Write a subquery to find the 4th minimum salary of all the salaries.
SELECT DISTINCT salary FROM employees e1 WHERE 4 = (SELECT COUNT(DISTINCT salary) FROM employees  e2 WHERE e2.salary <= e1.salary);
--Write a query to list the department name and number, of all the departments in which there are no employees.
SELECT * FROM departments WHERE department_id NOT IN (select department_id FROM employees);



--Write a query to find the addresses (location_id, street_address, city, state_province, country_name) of all the departments.
SELECT location_id, street_address, city, state_province, country_name FROM locations NATURAL JOIN countries;

--Write a query to make a join with the employees and departments table to find the name of the employee, including first_name and last name, department ID and name of departments.
SELECT first_name, last_name, department_id, department_name FROM employees JOIN departments USING (department_id);

--Write a SQL query to make a join with three tables: employees, departments and locations to find the name, including first_name and last_name, jobs, department name and ID, of the employees working in London.
SELECT e.first_name, e.last_name, e.job_id, e.department_id, d.department_name FROM employees e JOIN departments d ON (e.department_id = d.department_id) 
JOIN locations l ON (d.location_id = l.location_id) WHERE LOWER(l.city) = 'London';

--Write a query to make a join with two tables to find the employee id, last_name as Employee along with their manager_id and last name as Manager.
SELECT W1.employee_id as "Emp_id" , W1.last_name AS "Employee", W2.employee_id AS "Manager ID", W2.last_name AS "Manager" FROM employees W1 JOIN employees W2
ON W1.manager_id= W2.employee_id;

--Write a query to make a join with two tables employees and departments, to get the employees working in each department (retrieve the employees details, and the department name and number).
SELECT department_name AS 'Department Name', COUNT(*) AS 'No of Employees' FROM departments INNER JOIN employees ON employees.department_id = departments.department_id 
GROUP BY departments.department_id, department_name ORDER BY department_name;

--Write a query to make a join to find the employees who worked in a department which ID is 90 (retrieve the employee ID, job title and number of days the employee worked).
SELECT employee_id, job_title, end_date-start_date Days FROM job_history NATURAL JOIN jobs WHERE department_id=90;

--Write a query to make a join with three tables, departments, employees, and locations to display the department name, manager name, and city.
SELECT d.department_name, e.first_name, l.city FROM departments d JOIN employees e ON (d.manager_id = e.employee_id) JOIN locations l USING (location_id);

--Write a query to make a join with two tables, employees and jobs to display the job title and average salary of the employees.
SELECT job_title, AVG(salary) FROM employees NATURAL JOIN jobs GROUP BY job_title;

--Write a query to make a join with two tables, employees and departments to display department name, first_name and last_name, hire date and salary for all the managers who achieved a working experience of more than 15 years.
SELECT department_name, first_name, last_name,hire_date, salary,date_part('year',age(now(),hire_date)) Experience FROM departments w1 JOIN employees w2 
ON (w1.manager_id = w2.employee_id) WHERE date_part('year',age(now(),hire_date))>15;


--Write a query to update phone_number records. If the the substring ‘124’ was found in that column, update the phone_number to ‘999’.
UPDATE employees SET phone_number = REPLACE(phone_number, '124', '999') WHERE phone_number LIKE '%124%';

--Write a query to find the details of the employees who contain eight or more characters in their first name.
SELECT left(first_name, 8),REPEAT('$', FLOOR(salary/1000)) 'SALARY($)', salary FROM employees ORDER BY salary DESC;

--Write a query to join in uppercase, the first letter of the first_name, with the last_name, with '@example.com‘ in the email column.
SELECT UPPER(CONCAT(SUBSTRING(first_name,1,1),last_name,SUBSTRING(email,POSITION('@'IN email)))) FROM employees;

--Write a query to get the employee id, email but discard the last three characters of the email.
SELECT employee_id, REVERSE(SUBSTR(REVERSE(email), 4)) AS Email_ID FROM employees;

--Write a query to display the first word in the job title, if the job title contains more than one words.
SELECT job_title, SUBSTR(job_title,1, INSTR(job_title, ' ')-1) FROM jobs;

--Write a query that displays the first name and the length of the first name for all employees whose name starts with the letters ‘A’, ‘J’ or ‘M’. Give each column an appropriate label. Sort the results by the employees’ first names.
SELECT first_name "Name",LENGTH(first_name) "Length" FROM employees WHERE first_name LIKE 'J%' OR first_name LIKE 'M%' OR first_name LIKE 'A%'ORDER BY first_name ;

--Write a query to display the first name and salary for all employees. Display the salary with the $ symbol. Label the column as SALARY
SELECT first_name, LPAD(salary, 10, '$') SALARY FROM employees;
