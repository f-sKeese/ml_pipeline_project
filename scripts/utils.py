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
