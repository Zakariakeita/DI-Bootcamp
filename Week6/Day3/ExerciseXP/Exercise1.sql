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
	
--Get a list of all film languages.
SELECT l.name FROM language l;

--Get a list of all films joined with their languages – select the following details : film title, description, and language name. Try your query with different joins:
--Get all films, even if they don’t have languages.
SELECT f.title,f.description,l.name FROM language l RIGHT OUTER JOIN film f ON l.language_id=f.language_id;
--Get all languages, even if there are no films in those languages.
SELECT f.title,f.description,l.name FROM language l LEFT OUTER JOIN film f ON l.language_id=f.language_id;
--Create a new table called new_film with the following columns : id, name. Add some new films to the table.
CREATE TABLE  new_film 
(
	id SERIAL PRIMARY KEY NOT NULL,
	name VARCHAR(50) NOT NULL
);

INSERT INTO new_film(name) VALUES('Game of Throne'),('Scorpion'),('Spartacus');

--Create a new table called customer_review, which will contain film reviews that customers will make.
--Think about the DELETE constraint: if a film is deleted, it’s review should be automatically deleted.
--It should have the following columns:
--review_id – a primary key, non null, auto-increment.
--film_id – references the new_film table. The film that is being reviewed.
--language_id – references the language table. What language the review is in.
--title – the title of the review.
--score – the rating of the review (1-10).
--review_text – the text of the review. No limit on the length.
--last_update – when the review was last updated.
CREATE TABLE  customer_review
(
	review_id SERIAL PRIMARY KEY NOT NULL,
	film_id INTEGER NOT NULL,
	language_id INTEGER NOT NULL,
	title VARCHAR(50) NOT NULL,
	score INTEGER NOT NULL CHECK(score>=1 AND score<=10),
	review_text TEXT NOT NULL, 
	last_update DATE NOT NULL,
	FOREIGN KEY(film_id) REFERENCES new_film(id ) ON DELETE CASCADE,
	FOREIGN KEY(language_id) REFERENCES language(language_id)
);
--Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
INSERT INTO customer_review(film_id,language_id,title,score,review_text,last_update) 
VALUES((SELECT id FROM new_film WHERE name='Spartacus'),(SELECT language_id FROM language WHERE name='English'),
		'Duration',5,'The duration of movies is too long ',CURRENT_DATE),
		((SELECT id FROM new_film WHERE name='Scorpion'),(SELECT language_id FROM language WHERE name='French'),
		'Fiction',3,'The movies contains too much fiction',CURRENT_DATE);

--Delete a film that has a review from the new_film table, what happens to the customer_review table?
DELETE FROM new_film WHERE name='Spartacus';
-- THe movies is deleted on customer_review table


