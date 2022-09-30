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
	
	
--Write a SQL statement to change the following details belonging all employes who’s department_id is 110:
--email column should be: ‘not available’
--commission_pct column should be: 0.10
UPDATE employees SET email='not available',commission_pct=0.10 WHERE department_id=110;
--Write a SQL statement which will change the email column of all employees to ‘available’ whom work in the ‘Accounting’ department.
UPDATE employees SET email='available' WHERE department_id=(SELECT department_id FROM departments WHERE department_name='Accounting');
--Write a SQL statement to change the salary of the employee whose ID is 105. If the existing salary is less than 5000, change it to 8000.
UPDATE employees SET salary=8000 WHERE employee_id=105 AND salary< 5000;


--Write a query to find the number of jobs available in the employees table.
SELECT COUNT(DISTINCT job_id) FROM employees;
--Write a query to get the number of employees working in each post.
SELECT COUNT(employee_id), job_id FROM employees GROUP BY job_id;
--Write a query to get the difference between the highest and lowest salaries.
SELECT (MAX(salary)- MIN(salary)) AS difference FROM employees;
--Write a query to find a manager ID and the salary of the lowest-paid employee under that manager.
SELECT e.manager_id, e.salary FROM employees e WHERE e.salary=(SELECT MIN(salary) FROM employees WHERE manager_id=e.manager_id);
--Write a query to get the average salary for each post excluding Programmer.
SELECT AVG(e.salary) AS Average, j.job_title FROM employees e,jobs j WHERE e.job_id=j.job_id AND j.job_title !='Programmer' GROUP BY j.job_title ;
--Write a query to get the average salary for all departments that employ more than 10 employees.
SELECT AVG(e.salary) AS Average, d.department_name FROM employees e,departments d  WHERE e.department_id=d.department_id 
GROUP BY d.department_name HAVING COUNT(employee_id)>10;


--Write a SQL statement to change the name of the column “state_province” to “state” in the locations table, keeping the same data type and size.
ALTER TABLE locations RENAME COLUMN state_province TO state;
--Write a SQL statement to add a primary key to the “location_id” column in the locations table.
ALTER TABLE locations ADD PRIMARY KEY(location_id);


--Write a SQL statement to create a simple table “new_countries” including columns country_id and country_name.
--make sure that no duplicate data is added to the country_id column (which data type should you use for the column country_id ?)
--make sure that no countries except Italy, India and China will be entered in the table.
CREATE TABLE new_countries(
	country_id SERIAL PRIMARY KEY,
	country_name VARCHAR(20) CHECK(country_name IN ('India','Italy','China'))
);

--Write a SQL statement to create a duplicate copy of the “new_countries” table including the structure and the data of the “new_countries” table.
CREATE TABLE copy_new_countries AS SELECT * FROM new_countries;

--Write a SQL statement to create a table named “new_jobs” including columns job_id, job_title, min_salary, max_salary
--make sure that the max_salary column won’t exceed 25000.
--make sure that job_title, min_salary and max_salary have the following default values:
--job_title is blank
--min_salary is 8000
--max_salary is NULL.
CREATE TABLE new_jobs (
	job_id SERIAL PRIMARY KEY,
	job_title VARCHAR(50) DEFAULT '', 
	min_salary INTEGER DEFAULT 8000, 
	max_salary INTEGER CHECK(max_salary<25000) DEFAULT NULL 
);

--Write an SQL statement to create a table called “new_employees” the table should include the following columns: employee_id, first_name, last_name, email, phone_number hire_date, job_id and salary.
--make sure that, the employee_id column does not contain any duplicate value at the time of insertion,
--make sure that the foreign key column job_id, references the column job_id in the “new_jobs” table.
CREATE TABLE new_employees (
	employee_id INTEGER PRIMARY KEY,
	first_name VARCHAR(50) , 
	last_name VARCHAR(50) , 
	email  VARCHAR(50) , 
	phone_number  VARCHAR(50) ,
	hire_date DATE, 
	job_id INTEGER NOT NULL,
	salary INTEGER NOT NULL,
	FOREIGN KEY(job_id) REFERENCES new_jobs(job_id)
);

--Write a SQL statement to create a table called “new_job_history” the table should include the following columns: employee_id, start_date, end_date, job_id
--make sure that the foreign key employee_id references the column employee_id in the “new_employees” table.
--make sure that the foreign key job_id is equal to an id that exists in the “new_jobs” table.
CREATE TABLE new_job_history (
	employee_id INTEGER ,
	start_date DATE , 
	end_date DATE, 
	job_id INTEGER NOT NULL,
	FOREIGN KEY(job_id) REFERENCES new_jobs(job_id) ON DELETE SET NULL ON UPDATE SET NULL,
	FOREIGN KEY(employee_id) REFERENCES new_employees(employee_id)
);

--Write a SQL statement to insert a record with your own value into the “new_countries” table.
INSERT INTO new_countries (country_name) VALUES ('India');

--Using only one insert statement insert 3 row of data to the “new_countries” table
INSERT INTO new_countries (country_name) VALUES ('India'),('Italy'),('China');

--Write a SQL statement to insert the rows whithin the “new_countries” table to a duplicate table.
INSERT INTO copy_new_countries (country_name) VALUES ('India'),('Italy'),('China');

--Write a SQL statement to insert data into the “new_employees” table, the job_id column must contain values which exist in the “new_jobs” table.
INSERT INTO new_jobs (job_title, min_salary, max_salary) VALUES ('Programmer',20000,22000);

INSERT INTO new_employees (employee_id, first_name, last_name, email, phone_number ,hire_date, job_id,salary) 
VALUES (1,'Cheick','KEITA','cheick@gmail.com','2345676509','2022-10-12',(SELECT job_id FROM new_jobs WHERE job_title='Programmer'),50000);