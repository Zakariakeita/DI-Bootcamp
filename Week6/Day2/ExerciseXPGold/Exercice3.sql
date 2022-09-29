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
	
--Create a table named purchases. It should have 3 columns 
CREATE TABLE purchases (
 	purchases_id SERIAL PRIMARY KEY NOT NULL,
	customer_id INTEGER NOT NULL,
	items_id INTEGER NOT NULL,
	quantity_purchased INTEGER NOT NULL,
	FOREIGN KEY(customer_id) REFERENCES customers(id_customers),
	FOREIGN KEY(items_id) REFERENCES items(id_items)
);

--Insert purchases for the customers, use subqueries:
--Scott Scott bought one fan
INSERT INTO purchases(customer_id,items_id,quantity_purchased) VALUES((SELECT id_customers FROM customers WHERE last_name='Scott' AND first_name='Scott'),(SELECT id_items FROM items WHERE libelle='fan' ),1);
--Melanie Johnson bought ten large desks
INSERT INTO purchases(customer_id,items_id,quantity_purchased) VALUES((SELECT id_customers FROM customers WHERE last_name='Johnson' AND first_name='Melanie'),(SELECT id_items FROM items WHERE libelle='large desk' ),10);
--Greg Jones bougth two small desks
INSERT INTO purchases(customer_id,items_id,quantity_purchased) VALUES((SELECT id_customers FROM customers WHERE last_name='Jones' AND first_name='Greg'),(SELECT id_items FROM items WHERE libelle='small desk' ),2);

--Use SQL to get the following from the database:
--All purchases. Is this information useful to us?
SELECT * FROM purchases;
--All purchases, joining with the customers table.
SELECT * FROM purchases pu INNER JOIN customers cu ON pu.customer_id=cu.id_customers;
--Purchases of the customer with the ID equal to 5.
SELECT * FROM purchases WHERE customer_id=5;
--Purchases for a large desk AND a small desk
SELECT * FROM purchases pu INNER JOIN items i ON pu.items_id=i.id_items  WHERE i.libelle IN ('large desk','small desk');
--Use SQL to show all the customers who have made a purchase. Show the following fields/columns:
--Customer first name,Customer ,last name,Item name
SELECT cu.first_name,cu.last_name, i.libelle FROM customers cu INNER JOIN purchases pu ON cu.id_customers=pu.customer_id  INNER JOIN items i ON pu.items_id=i.id_items;

--Add a row which references a customer by ID, but does not reference an item by ID (leave it blank). Does this work? Why/why not?
INSERT INTO purchases(customer_id,quantity_purchased) VALUES((SELECT id_customers FROM customers WHERE last_name='Jones' AND first_name='Sandra'),2);
--  It doesn't work beacause item_id is define to not null

