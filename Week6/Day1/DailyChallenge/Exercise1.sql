-- Database: Hollywood

-- DROP DATABASE IF EXISTS "Hollywood";

/*CREATE DATABASE "Hollywood"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
*/
-- CREATE TABLE actors
	/*CREATE TABLE actors
	(
		 actor_id SERIAL PRIMARY KEY,
		 first_name VARCHAR (50) NOT NULL,
		 last_name VARCHAR (100) NOT NULL,
		 age DATE NOT NULL,
		 number_oscars SMALLINT NOT NULL
	);*/

	
INSERT INTO actors (first_name, last_name, age, number_oscars) VALUES('Matt','Damon','08/10/1970', 5);
INSERT INTO actors (first_name, last_name, age, number_oscars) VALUES('George','Clooney','06/05/1961', 2);

--In this exercise we will be using the actors table from todays lesson.
--Count how many actors are in the table.
SELECT COUNT(*) FROM actors;
--Try to add a new actor with some blank fields. What do you think the outcome will be ?
INSERT INTO actors (first_name, last_name, age, number_oscars) VALUES('','','', NULL);
--It imposible beacause the attributes is define to not null

