-- Database: public

-- DROP DATABASE IF EXISTS public;
/*

CREATE DATABASE public
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
*/
	

	CREATE TABLE items 
	(	id_items SERIAL PRIMARY KEY,
		libelle TEXT NOT NULL,
		price INTEGER NOT NULL
	);
 
	CREATE TABLE customers 
	(	id_customers SERIAL PRIMARY KEY,
		first_name VARCHAR(20) NOT NULL,
		last_name VARCHAR(20) NOT NULL
	);
	
	INSERT INTO items(libelle,price) VALUES('small desk',100),('large desk',300),('fan',80);
	INSERT INTO customers(first_name,last_name) VALUES('Greg', 'Jones'),('Sandra','Jones'),('Scott','Scott'),
	('Trevor','Green'),('Melanie','Jonhson');
	
	SELECT * FROM items;
	SELECT * FROM items WHERE price >80;
	SELECT * FROM items WHERE price <=300;
	SELECT * FROM customers WHERE last_name='Smith'; --no customers have smith as last name
	SELECT * FROM customers WHERE last_name='Jones'; 
	SELECT * FROM customers WHERE first_name !='Scott'; 
	
	