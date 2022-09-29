-- Database: dvdrental

-- DROP DATABASE IF EXISTS dvdrental;

/*
CREATE DATABASE dvdrental
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	*/
--Find out how many films there are for each rating.
SELECT rating ,count(film_id) FROM film GROUP BY rating;
--Get a list of all the movies that have a rating of G or PG-13.
SELECT  film_id,title,description,rating FROM film WHERE rating IN ('G','PG-13') AND (film.length/60)<2 AND rental_rate<3 ORDER BY title ASC;
--Find a customer in the customer table, and change his/her details to your details, using SQL UPDATE.
UPDATE customer SET first_name='CHEICK',last_name='KEITA',email='keita@gmail.com',last_update=CURRENT_DATE WHERE customer_id=1;
--Now find the customer’s address, and use UPDATE to change the address to your address (or make one up).
UPDATE address SET address='16 NELSON MANDELA' WHERE  address_id=(SELECT address_id FROM customer WHERE customer_id=1);
