-- Database: bootcamp

-- DROP DATABASE IF EXISTS bootcamp;

--Create a database called bootcamp.


CREATE DATABASE bootcamp
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

--Create a table called students.
--Add the following columns:
--id
--last_name
--first_name
--birth_date
--The id must be auto_incremented.
--Make sure to choose the correct data type for each column.
--To help, here is the data that you will have to insert. (How do we insert a date to a table?)
CREATE TABLE students(
	id_students SERIAL PRIMARY KEY,
	first_name VARCHAR(20) NOT NULL,
	last_name VARCHAR(20) NOT NULL,
	birth_date DATE NOT NULL);
	
--Insert the data seen above to the students table. Find the most efficient way to insert the data.
INSERT INTO students(first_name,last_name,birth_date) VALUES
	('Marc','Benichou',TO_DATE('02/11/1998','DD/MM/YYYY')),
	('Yoan','Cohen',TO_DATE('03/12/2010','DD/MM/YYYY')),
	('Lea','Benichou',TO_DATE('27/07/1986','DD/MM/YYYY')),
	('Amelia','Dux',TO_DATE('07/04/1996','DD/MM/YYYY')),
	('David','Grez',TO_DATE('14/06/2003','DD/MM/YYYY')),
	('Omer','Simpson',TO_DATE('03/10/1980','DD/MM/YYYY'));

--Insert your last_name, first_name and birth_date to the students table (Take a look at the id given).
INSERT INTO students(first_name,last_name,birth_date) VALUES
	('Cheick','Keita','02/11/1996');
SELECT students.id_students FROM students WHERE last_name='Cheick';
--Fetch all of the data from the table.
SELECT * FROM students;
--Fetch all of the students first_names and last_names.
SELECT first_name,last_name FROM students;
--For the following questions, only fetch the first_names and last_names of the students.
--Fetch the student which id is equal to 2.
SELECT first_name,last_name FROM students WHERE id_students=2;
--Fetch the student whose last_name is Benichou AND first_name is Marc.
SELECT first_name,last_name FROM students WHERE last_name='Benichou' AND first_name='Marc';
--Fetch the students whose last_names are Benichou OR first_names are Marc.
SELECT first_name,last_name FROM students WHERE last_name='Benichou' OR first_name='Marc';
--Fetch the students whose first_names contain the letter a.
SELECT first_name,last_name FROM students WHERE  first_name ILIKE '%a%';
--Fetch the students whose first_names start with the letter a.
SELECT first_name,last_name FROM students WHERE  first_name ILIKE 'a%';
--Fetch the students whose first_names end with the letter a.
SELECT first_name,last_name FROM students WHERE  first_name ILIKE '%a';
--Fetch the students whose second to last letter of their first_names are a (Example: Leah).
SELECT first_name,last_name FROM students WHERE  first_name ILIKE '%a-';
--Fetch the students whose id’s are equal to 1 AND 3 .
SELECT first_name,last_name FROM students WHERE  id_students=1 AND id_students=3;
--Fetch the students whose birth_dates are equal to or come after 1/01/2000. (show all their info).
SELECT * FROM students WHERE  birth_date>= '1/01/2000';







