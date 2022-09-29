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

--UPDATE
--‘Lea Benichou’ and ‘Marc Benichou’ are twins, they should have the same birth_dates. Update both their birth_dates to 02/11/1998.
UPDATE students SET birth_date='02/11/1998' WHERE last_name='Benichou';
--Change the last_name of David from ‘Grez’ to ‘Guez’.
UPDATE students SET last_name='Guez' WHERE first_name='David';

--DELETE
--Delete the student named ‘Lea Benichou’ from the table.
DELETE FROM students WHERE last_name='Benichou' AND first_name='Lea';

--COUNT
--Count how many students are in the table.
SELECT COUNT(*) FROM students;
--Count how many students were born after 1/01/2000.
SELECT COUNT(*) FROM students WHERE birth_date > '1/01/2000';
--Add a column to the student table called math_grade.
ALTER TABLE students ADD COLUMN math_grade INTEGER ;
--Add 80 to the student which id is 1.
UPDATE students SET math_grade=80 WHERE id_students=1;
--Add 90 to the students which have ids of 2 or 4.
UPDATE students SET math_grade=90 WHERE id_students IN (1,4);
--Add 40 to the student which id is 6.
UPDATE students SET math_grade=40 WHERE id_students=6;
--Count how many students have a grade bigger than 83
SELECT COUNT(*) FROM students WHERE math_grade>83;
--Add another student named ‘Omer Simpson’ with the same birth_date as the one already in the table. Give him a grade of 70.
INSERT INTO students VALUES(6,'Omer', 'Simpson', (SELECT birth_date FROM students WHERE last_name='Simpson' AND first_name='Omer'),70);
/*Bonus: Count how many grades each student has.
Tip: You should display the first_name, last_name and the number of grades of each student. If you followed the instructions above correctly, all the students should have 1 math grade, except Omer Simpson which has 2.
Tip : Use an alias called total_grade to fetch the grades.
Hint : Use GROUP BY. */
SELECT first_name,last_name ,COUNT(math_grade) as total_grade FROM students GROUP BY first_name,last_name ;


