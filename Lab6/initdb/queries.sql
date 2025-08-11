SELECT * FROM products p ;

SELECT * FROM customers c ;

SELECT city FROM addresses a ;

SELECT item_price, item_id FROM order_items oi ;

SELECT email_address, shipping_address_id FROM customers c ;

 -- inner joins

SELECT p.product_name, c.category_name
FROM products p
INNER JOIN categories c ON p.category_id = c.category_id;

SELECT o.order_id, o.order_date, c.email_address
FROM orders o  
INNER JOIN customers c ON o.customer_id = c.customer_id ;

SELECT c.customer_id, c.first_name, c.last_name, a.phone
FROM customers c 
INNER JOIN addresses a ON a.customer_id = c.customer_id;

SELECT p.product_name, p.list_price, p.discount_percent, c.category_name
FROM products p 
INNER JOIN categories c ON c.category_id = p.category_id;

SELECT p.product_name, p.list_price, oi.item_price, oi.quantity
FROM products p 
INNER JOIN order_items oi ON oi.product_id = p.product_id;

-- functions and group by

SELECT AVG(list_price) AS avererage_price FROM products p ;

SELECT a.state, COUNT(DISTINCT customer_id) AS customer_count
FROM addresses a 
GROUP BY a.state ;

SELECT order_id, SUM(item_price * quantity) AS sales
FROM order_items oi 
GROUP BY oi.order_id ;

SELECT SUM(discount_amount) AS total_discounts FROM order_items oi ;

SELECT c.category_name, COUNT(*) AS num_products
FROM products p
INNER JOIN categories c ON p.category_id = c.category_id
GROUP BY c.category_name;