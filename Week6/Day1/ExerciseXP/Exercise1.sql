-- Database: public

-- DROP DATABASE IF EXISTS public;

--Create a database called public.
CREATE DATABASE public
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

	
--Add two tables
--items

	CREATE TABLE items 
	(	id_items SERIAL PRIMARY KEY,
		libelle TEXT NOT NULL,
		price INTEGER NOT NULL
	);
 
 --customers.
	CREATE TABLE customers 
	(	id_customers SERIAL PRIMARY KEY,
		first_name VARCHAR(20) NOT NULL,
		last_name VARCHAR(20) NOT NULL
	);

--Add the following items to the items table:
-- Small Desk – 100 (ie. price)
--Large desk – 300
-- Fan – 80
	INSERT INTO items(libelle,price) VALUES('small desk',100),('large desk',300),('fan',80);
	INSERT INTO customers(first_name,last_name) VALUES('Greg', 'Jones'),('Sandra','Jones'),('Scott','Scott'),
	('Trevor','Green'),('Melanie','Jonhson');

--All the items.
	SELECT * FROM items;
--All the items with a price above 80 (80 not included).
	SELECT * FROM items WHERE price >80;
--All the items with a price below 300. (300 included)
	SELECT * FROM items WHERE price <=300;
--All customers whose last name is ‘Smith’ (What will be your outcome?).
	SELECT * FROM customers WHERE last_name='Smith'; --no customers have smith as last name
--All customers whose last name is ‘Jones’.
	SELECT * FROM customers WHERE last_name='Jones'; 
--All customers whose firstname is not ‘Scott’.
	SELECT * FROM customers WHERE first_name !='Scott'; 
	
	
	