-- Database: public

-- DROP DATABASE IF EXISTS public;

CREATE DATABASE public
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
--Fetch the last 2 customers in alphabetical order (A-Z) – exclude ‘id’ from the results.
SELECT first_name,last_name,id_customers FROM (SELECT first_name,last_name,id_customers FROM customers ORDER BY id_customers DESC LIMIT 2 ) tmp ORDER BY id_customers ASC  ;
--Use SQL to delete all purchases made by Scott.
DELETE FROM purchases pu WHERE pu.customer_id= (SELECT id_customers FROM customers WHERE last_name='Scott');
--Does Scott still exist in the customers table, even though he has been deleted? Try and find him.
SELECT * FROM customers WHERE last_name='Scott';
--Use SQL to find all purchases. Join purchases with the customers table, so that Scott’s order will appear, although instead of the customer’s first and last name, you should only see empty/blank. (Which kind of join should you use?).
SELECT * FROM customers cu LEFT OUTER JOIN purchases pu ON pu.customer_id=cu.id_customers; 
--Use SQL to find all purchases. Join purchases with the customers table, so that Scott’s order will NOT appear. (Which kind of join should you use?)
SELECT * FROM customers cu RIGHT OUTER JOIN purchases pu ON pu.customer_id=cu.id_customers; 