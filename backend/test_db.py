import psycopg2

try:
    conn = psycopg2.connect(
        host='localhost',
        database='recipes_book_db',
        user='postgres',
        password='postgres1234',
        port=5432
    )
    print("✓ Connection successful!")
    conn.close()
except Exception as e:
    print(f"✗ Error: {e}")