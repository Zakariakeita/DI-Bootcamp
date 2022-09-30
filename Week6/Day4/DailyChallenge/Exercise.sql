--Create a table called product_orders and a table called items. You decide which fields should be in each table, although make sure the items table has a column called price.
CREATE TABLE product_orders(
	id SERIAL PRIMARY KEY,
	name VARCHAR(20)
	user_id INTEGER,
	FOREIGN KEY (user_id) REFERENCES users(user_id)
);

--There should be a one to many relationship between the product_orders table and the items table. An order can have many items, but an item can belong to only one order.
CREATE TABLE items(
	items_id SERIAL PRIMARY KEY,
	price INTEGER,
	product_orders_id INTEGER,
	FOREIGN KEY (product_orders_id) REFERENCES product_orders(id)
);

--Create a function that returns the total price for a given order.
CREATE FUNCTION price(my_id INTEGER)
RETURNS INTEGER AS $price$
BEGIN
	RETURN (SELECT price FROM items i INNER JOIN product_orders po ON i.items_id=po.id WHERE po.id=my_id);
END;
$price$ LANGUAGE plpgsql;


--Bonus :
--Create a table called users.
--There should be a one to many relationship between the users table and the product_orders table.
CREATE TABLE users(
	user_id SERIAL PRIMARY KEY,
	name VARCHAR(20)
);

--Create a function that returns the total price for a given order of a given user.
CREATE FUNCTION total_price(order_id INTEGER,user_id INTEGER)
RETURNS INTEGER AS $total_price$
BEGIN
	RETURN (SELECT price FROM items i INNER JOIN product_orders po ON i.items_id=po.id INNER JOIN users u ON u.user_id=po.user_id WHERE u.user_id=user_id AND po.id=order_id);
END;
$total_price$ LANGUAGE plpgsql;
