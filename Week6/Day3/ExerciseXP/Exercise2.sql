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
	

--Use UPDATE to change the language of some films. Make sure that you use valid languages.
UPDATE film SET language_id=(SELECT language_id FROM language WHERE name='French') WHERE film_id BETWEEN 1 AND 100;

--Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
-- the foreign keys are address_id refrereces ID for table adresss AND store_id references ID of Table Store
-- we must insert the valid value of this foreign keys

--We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
DROP TABLE customer_review; --It is an easy step
--Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
SELECT COUNT(r.rental_id) FROM rental r WHERE r.return_date IS NULL;

--Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
SELECT f.title ,f.rental_rate FROM rental r INNER JOIN inventory i ON i.inventory_id=r.inventory_id INNER JOIN film f ON f.film_id=i.film_id
WHERE r.return_date IS NULL AND f.rental_rate IN(SELECT MAX(rental_rate) FROM film)  LIMIT 30;

--Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
--The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
SELECT f.title FROM film f INNER JOIN film_actor fa ON f.film_id=fa.film_id  WHERE description ILIKE '%a sumo wrestler%' AND 
fa.actor_id=(SELECT actor_id FROM actor WHERE first_name='Penelope' AND last_name='Monroe');

--The 2nd film : A short documentary (less than 1 hour long), rated “R”.
SELECT f.title FROM film f INNER JOIN film_category fc ON f.film_id=fc.film_id  WHERE (f.length/60)<1 AND f.rating='R' 
AND fc.category_id=(SELECT category_id FROM category WHERE name ILIKE '%documentary%');

--The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
SELECT f.title FROM film f INNER JOIN inventory i ON f.film_id=i.film_id INNER JOIN rental r ON r.inventory_id=i.inventory_id WHERE f.rental_rate>4 AND r.return_date 
BETWEEN '2005-07-28' AND '2005-08-01' AND r.customer_id=(SELECT customer_id FROM customer WHERE first_name='Matthew' AND last_name='Mahan');

--The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.
SELECT f.title FROM film f INNER JOIN inventory i ON f.film_id=i.film_id INNER JOIN rental r ON r.inventory_id=i.inventory_id WHERE ((f.title ILIKE'%boat%') OR (f.description ILIKE'%boat%')) 
 AND r.return_date IS NOT NULL AND f.replacement_cost> (SELECT AVG(replacement_cost) FROM film) AND r.customer_id=(SELECT customer_id FROM customer WHERE first_name='Matthew' AND last_name='Mahan');