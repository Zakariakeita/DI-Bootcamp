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
	
--How many stores there are, and in which city and country they are located.
SELECT COUNT(s.store_id) as Nombre, ci.city,co.country FROM store s INNER JOIN address ad ON s.address_id=ad.address_id INNER JOIN city ci ON
ci.city_id=ad.city_id INNER JOIN country co ON co.country_id=ci.country_id GROUP BY ci.city,co.country ;

--How many hours of viewing time there are in total in each store – in other words, the sum of the length of every inventory item in each store.
SELECT SUM(f.length), i.store_id FROM film f INNER JOIN inventory i ON f.film_id=i.film_id GROUP BY i.store_id;

--A list of all customers in the cities where the stores are located.
SELECT cu.first_name,cu.last_name ,ci.city FROM customer cu INNER JOIN address ad ON cu.address_id=ad.address_id INNER JOIN city ci ON ci.city_id=ad.city_id
INNER JOIN store s ON cu.store_id=s.store_id WHERE cu.address_id=s.address_id;
--A list of all customers in the countries where the stores are located.

--Some people will be frightened by watching scary movies while zombies walk the streets. Create a ‘safe list’ of all movies which do not include the ‘Horror’ category, or contain the words ‘beast’, ‘monster’, ‘ghost’, ‘dead’, ‘zombie’, or ‘undead’ in their titles or descriptions… Get the sum of their viewing time (length).
--Hint : use the CHECK contraint

--For both the ‘general’ and the ‘safe’ lists above, also calculate the time in hours and days (not just minutes).