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

CREATE TABLE students(
	id_students SERIAL PRIMARY KEY,
	first_name VARCHAR(20) NOT NULL,
	last_name VARCHAR(20) NOT NULL,
	birth_date DATE NOT NULL);
	
INSERT INTO students(first_name,last_name,birth_date) VALUES
	('Marc','Benichou',TO_DATE('02/11/1998','DD/MM/YYYY')),
	('Yoan','Cohen',TO_DATE('03/12/2010','DD/MM/YYYY')),
	('Lea','Benichou',TO_DATE('27/07/1986','DD/MM/YYYY')),
	('Amelia','Dux',TO_DATE('07/04/1996','DD/MM/YYYY')),
	('David','Grez',TO_DATE('14/06/2003','DD/MM/YYYY')),
	('Omer','Simpson',TO_DATE('03/10/1980','DD/MM/YYYY'));

INSERT INTO students(first_name,last_name,birth_date) VALUES
	('Cheick','Keita','02/11/1996');
	
SELECT students.id_students FROM students WHERE last_name='Cheick';
SELECT * FROM students;
SELECT first_name,last_name FROM students;
SELECT first_name,last_name FROM students WHERE id_students=2;
SELECT first_name,last_name FROM students WHERE last_name='Benichou' AND first_name='Marc';
SELECT first_name,last_name FROM students WHERE last_name='Benichou' OR first_name='Marc';
SELECT first_name,last_name FROM students WHERE  first_name ILIKE '%a%';
SELECT first_name,last_name FROM students WHERE  first_name ILIKE 'a%';
SELECT first_name,last_name FROM students WHERE  first_name ILIKE '%a';
SELECT first_name,last_name FROM students WHERE  first_name ILIKE '%a-';
SELECT first_name,last_name FROM students WHERE  id_students=1 AND id_students=3;
SELECT * FROM students WHERE  birth_date>= '1/01/2000';

