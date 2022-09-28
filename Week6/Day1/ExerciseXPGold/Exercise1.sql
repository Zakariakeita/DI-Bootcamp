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
	
SELECT * FROM students  ORDER BY last_name ASC LIMIT 4;
SELECT * FROM students where birth_date = (SELECT MAX(birth_date) FROM students);
SELECT * FROM students  LIMIT 3 OFFSET 2;