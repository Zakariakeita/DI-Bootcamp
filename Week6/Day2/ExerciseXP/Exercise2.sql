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

--In the dvdrental database write a query to select all the columns from the “customer” table.	
SELECT * FROM customer;
--Write a query to display the names (first_name, last_name) using an alias named “full_name”.
SELECT (first_name, last_name) as full_name FROM customer;
--Lets get all the dates that accounts were created. Write a query to select all the create_date from the “customer” table (there should be no duplicates).
SELECT DISTINCT create_date FROM customer;
--Write a query to get all the customer details from the customer table, it should be displayed in descending order by their first name.
SELECT * FROM customer ORDER BY first_name DESC;
--Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.
SELECT film_id,title,description,release_year,rental_rate FROM film ORDER BY rental_rate ASC;
--Write a query to get the address, and the phone number of all customers living in the Texas district, these details can be found in the “address” table.
SELECT address,phone FROM address WHERE district='Texas';
--Write a query to retrieve all movie details where the movie id is either 15 or 150.
SELECT * FROM film WHERE film_id IN (15,150) ;
--Write a query which should check if your favorite movie exists in the database. Have your query get the film ID, title, description, length and the rental rate, these details can be found in the “film” table.
SELECT film_id,title,description,film.length,rental_rate FROM film WHERE title='African Egg';
--No luck finding your movie? Maybe you made a mistake spelling the name. Write a query to get the film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie.
SELECT film_id,title,description,film.length,rental_rate FROM film WHERE title ILIKE 'Af%';
--Write a query which will find the 10 cheapest movies.
SELECT  film_id,title,description,film.length,rental_rate FROM film ORDER BY rental_rate ASC LIMIT 10;
--Not satisfied with the results. Write a query which will find the next 10 cheapest movies.
SELECT  film_id,title,description,film.length,rental_rate FROM film  ORDER BY rental_rate ASC  OFFSET 10 FETCH FIRST 10 ROWS ONLY;
--Write a query which will join the data in the customer table and the payment table. You want to get the amount and the date of every payment made by a customer, ordered by their id (from 1 to…).
SELECT pa.amount, pa.payment_date FROM payment pa INNER JOIN customer cu ON pa.customer_id=cu.customer_id ORDER BY cu.customer_id ASC;
--You need to check your inventory. Write a query to get all the movies which are not in inventory.
SELECT f.film_id,f.title,f.description,f.length,f.rental_rate FROM film f WHERE f.film_id NOT IN (SELECT film_id FROM inventory);
--Write a query to find which city is in which country.
SELECT co.country, ci.city FROM country co INNER JOIN city ci ON ci.country_id=co.country_id;
--Bonus You want to be able to see how your sellers have been doing? Write a query to get the customer’s id, names (first and last), the amount and the date of payment ordered by the id of the staff member who sold them the dvd.
SELECT cu.customer_id,cu.first_name,cu.last_name, pa.amount,pa.payment_date FROM customer cu JOIN payment pa ON pa.customer_id=cu.customer_id JOIN staff s ON s.staff_id=pa.staff_id ORDER BY pa.staff_id ;










