import psycopg2
import pandas as pd

def connect_to_db(dbname='postgres'):
    try:
        # Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname=dbname,
            user='gomte',
            password='password',
            host='localhost',
            port='5432'
        )
        conn.autocommit = True
        return conn

    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def create_db(conn, db_name):
    try:
        conn = conn
        cursor = conn.cursor()
        # Check if table exists
        cursor.execute(f"SELECT datname FROM pg_database WHERE datname = %s;", (db_name,))
        if cursor.fetchone() is not None:
            print(f"Database {db_name} already exists.")
            return
        else:
            # Create database
            cursor.execute(f"CREATE DATABASE {db_name};")
            print(f"Database {db_name} created successfully.")
            return
    except Exception as e:
        print(f"Error creating database: {e}")

def create_table(conn, table_name):
    try:
        conn = conn
        cursor = conn.cursor()
        # Check if table exists
        cursor.execute("SELECT * from information_schema.tables WHERE table_name = %s;", (table_name,))
        if cursor.fetchone() is not None:
            print(f"Table {table_name} already exists.")
            cursor.close()
            return
        else:
            # Create table if it doesn't exist
            cursor.execute(f"CREATE TABLE {table_name} (id SERIAL PRIMARY KEY, smiles TEXT);")
            print(f"Table {table_name} created successfully.")
            cursor.close()
            return
    except Exception as e:
        print(f"Error creating table: {e}")

def insert_data(conn, table_name, csv_path):
    # Load csv with pandas
    df = pd.read_csv(csv_path)
    try:
        cursor = conn.cursor()
        # Insert data into the table
        for row in df.itertuples():
            id = row.id
            smiles = row.smiles
            cursor.execute(f"INSERT INTO {table_name} (id, smiles) VALUES (%s, %s);", (id, smiles))
            conn.commit()
        cursor.execute(f"SELECT * FROM {table_name};")
        print("Inserted data:")
        print(cursor.fetchall())
        cursor.close()
    except Exception as e:
        print(f"Error inserting data: {e}")

if __name__ == "__main__":
    conn = connect_to_db()
    if conn:
        db_name = "smiles_db"
        table_name = "smiles_table"
        conn = connect_to_db()
        create_db(conn, db_name)
        conn.close()
        ## Reconnecting to the new database
        conn = connect_to_db(db_name)
        create_table(conn, table_name)
        conn.close()
        ## Insert data in new table
        conn = connect_to_db(db_name)
        csv_path = "../data/sample_smiles.csv"
        insert_data(conn, table_name, csv_path)
        conn.close()


