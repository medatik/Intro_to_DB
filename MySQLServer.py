import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (adjust user & password as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='admin',
            password='1234'  # Change this to your actual password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        # Ensure connection is closed
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            # Optional: print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()
