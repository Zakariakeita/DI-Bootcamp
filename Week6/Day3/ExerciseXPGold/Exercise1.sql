-- Database: dvdrental

-- DROP DATABASE IF EXISTS dvdrental;

CREATE DATABASE dvdrental
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
	
--Get a list of all rentals which are out (have not been returned). How do we identify these films in the database?
SELECT * FROM rental WHERE return_date IS NULL;
--Get a list of all customers who have not returned their rentals. Make sure to group your results.
SELECT * FROM customer cu INNER JOIN rental r ON r.customer_id=cu.customer_id WHERE r.return_date IS NULL;
--Get a list of all the Action films with Joe Swank.
SELECT f.title FROM film f INNER JOIN film_category fc ON f.film_id=fc.film_id INNER JOIN film_actor fa ON fa.film_id=f.film_id 
WHERE fc.category_id=(SELECT category_id FROM category WHERE name='Action') 
AND fa.actor_id=(SELECT actor_id FROM actor WHERE last_name='Swank' AND first_name='Joe');

