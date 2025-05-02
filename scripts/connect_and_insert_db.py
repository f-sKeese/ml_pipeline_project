import psycopg2

def connect_to_db():
    try:
        # Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname='my_database',
            user='my_user',  # Replace with your username if different
            password='my_password',  # Replace with your password
            host='localhost'
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def insert_data(conn):
    try:
        cursor = conn.cursor()
        # Insert data into the table
        cursor.execute("INSERT INTO my_table (name, value) VALUES ('Another Name', 456);")
        conn.commit()
        cursor.close()
    except Exception as e:
        print(f"Error inserting data: {e}")

def query_data(conn):
    try:
        cursor = conn.cursor()
        # Query data from the table
        cursor.execute("SELECT * FROM my_table;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
    except Exception as e:
        print(f"Error querying data: {e}")

def main():
    conn = connect_to_db()
    if conn:
        insert_data(conn)
        query_data(conn)
        conn.close()

if __name__ == "__main__":
    main()