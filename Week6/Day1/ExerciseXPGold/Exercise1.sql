-- Database: bootcamp

-- DROP DATABASE IF EXISTS bootcamp;

/*
CREATE DATABASE bootcamp
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	*/
	
---For the following questions, you have to fetch the first_names, last_names and birth_dates of the students.
--Fetch the first four students. You have to order the four students alphabetically by last_name.

SELECT * FROM students  ORDER BY last_name ASC LIMIT 4;
--Fetch the details of the youngest student.
SELECT * FROM students where birth_date = (SELECT MAX(birth_date) FROM students);
--Fetch three students skipping the first two students.
SELECT * FROM students  LIMIT 3 OFFSET 2;