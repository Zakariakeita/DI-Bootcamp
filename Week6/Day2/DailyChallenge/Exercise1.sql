CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
)
--PROVIDE : to create a table FirstTab
--OUTPUT : CREATE TABLE

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar')
--PROVIDE : to insert this four element in FirstTab
--OUTPUT : INSERT 0 4

SELECT * FROM FirstTab
--PROVIDE : to display all element of FirstTab
--OUTPUT : Display the contents of TABLE FirsTab

CREATE TABLE SecondTab (
    id integer 
)
--PROVIDE : to create a table SecondTab
--OUTPUT : CREATE TABLE

INSERT INTO SecondTab VALUES
(5),
(NULL)
--PROVIDE : to insert this four element in FirstTab
--OUTPUT : INSERT 0 2

SELECT * FROM SecondTab
--PROVIDE : to display all element of SecondTab
--OUTPUT : Display the contents of TABLE SecondTab


--Q1. What will be the OUTPUT of the following statement?
SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )
--OUTPUT : 0
--Q2. What will be the OUTPUT of the following statement?
SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
--OUTPUT : 2
--Q3. What will be the OUTPUT of the following statement?
SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
--OUTPUT : 0
--Q4. What will be the OUTPUT of the following statement?
SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )
--OUTPUT : 2
