import argparse
import mysql.connector

QUERIES = {
    "q1": "SELECT * FROM products p;",
    "q2": "SELECT * FROM customers c;",
    "q3": "SELECT city FROM addresses a;",
    "q4": "SELECT item_price, item_id FROM order_items oi;",
    "q5": "SELECT email_address, shipping_address_id FROM customers c;",

    "q6": """
        SELECT p.product_name, c.category_name
        FROM products p
        INNER JOIN categories c ON p.category_id = c.category_id;
    """,
    "q7": """
        SELECT o.order_id, o.order_date, c.email_address
        FROM orders o  
        INNER JOIN customers c ON o.customer_id = c.customer_id;
    """,
    "q8": """
        SELECT c.customer_id, c.first_name, c.last_name, a.phone
        FROM customers c 
        INNER JOIN addresses a ON a.customer_id = c.customer_id;
    """,
    "q9": """
        SELECT p.product_name, p.list_price, p.discount_percent, c.category_name
        FROM products p 
        INNER JOIN categories c ON c.category_id = p.category_id;
    """,
    "q10": """
        SELECT p.product_name, p.list_price, oi.item_price, oi.quantity
        FROM products p 
        INNER JOIN order_items oi ON oi.product_id = p.product_id;
    """,

    "q11": "SELECT AVG(list_price) AS average_price FROM products p;",
    "q12": """
        SELECT a.state, COUNT(DISTINCT customer_id) AS customer_count
        FROM addresses a 
        GROUP BY a.state;
    """,
    "q13": """
        SELECT order_id, SUM(item_price * quantity) AS sales
        FROM order_items oi 
        GROUP BY oi.order_id;
    """,
    "q14": "SELECT SUM(discount_amount) AS total_discounts FROM order_items oi;",
    "q15": """
        SELECT c.category_name, COUNT(*) AS num_products
        FROM products p
        INNER JOIN categories c ON p.category_id = c.category_id
        GROUP BY c.category_name;
    """
}

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="user",
        password="password",
        database="my_guitar_shop"
    )

def run_query(query_key):
    if query_key not in QUERIES:
        raise KeyError(f"Invalid query key: {query_key}")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(QUERIES[query_key])
    columns = cursor.column_names
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return columns, rows

def main():
    parser = argparse.ArgumentParser(description="Lab 6 Query Runner")
    parser.add_argument("--query", help="Query key to run (q1, q2, ... q15)")
    parser.add_argument("--list", action="store_true", help="List available queries")
    args = parser.parse_args()

    while True:
        print("\nAvailable queries:")
        for key in sorted(QUERIES.keys(), key=lambda k: int(k[1:])):
            print(f"  {key}")
        query_key = input("Enter query key to run (or type 'exit' to quit): ").strip()
        if query_key.lower() in ('exit', 'quit', 'q'):
            print("Exiting.")
            break
        if query_key not in QUERIES:
            print(f"Invalid query key: {query_key}")
            continue

        try:
            columns, results = run_query(query_key)
            if not results:
                print("No results found.")
                continue
            print("\t".join(columns))
            for row in results:
                print("\t".join(str(item) for item in row))
        except Exception as e:
            print(f"Error running query: {e}")

if __name__ == "__main__":
    main()