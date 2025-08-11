import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="user",
        password="password",
        database="my_guitar_shop"
    )

QUERIES = {
    "q1": "SELECT * FROM guitars LIMIT 5;",
    "q2": "SELECT brand, COUNT(*) FROM guitars GROUP BY brand;",
    "q3": "SELECT first_name, last_name FROM customers ORDER BY last_name LIMIT 10;",
    "q4": "SELECT order_id, SUM(item_price * quantity) AS total FROM order_items GROUP BY order_id;",
    "q5": "SELECT product_name, list_price FROM products WHERE list_price > 500;",
    "q6": "SELECT category_name, COUNT(*) FROM products GROUP BY category_name;",
    "q7": "SELECT brand, MAX(list_price) FROM products GROUP BY brand;",
    "q8": "SELECT product_name FROM products WHERE product_name LIKE '%Guitar%';",
    "q9": "SELECT c.first_name, c.last_name, COUNT(o.order_id) "
          "FROM customers c JOIN orders o ON c.customer_id = o.customer_id "
          "GROUP BY c.customer_id;",
    "q10": "SELECT o.order_id, o.order_date, c.first_name, c.last_name "
           "FROM orders o JOIN customers c ON o.customer_id = c.customer_id "
           "ORDER BY o.order_date DESC LIMIT 5;"
}

def run_query(query_key):
    if query_key not in QUERIES:
        raise KeyError(f"Invalid query key: {query_key}")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(QUERIES[query_key])
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows