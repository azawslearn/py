import mysql.connector
import configparser

# Read the MySQL configuration from the config file
config = configparser.ConfigParser()
config.read(r'C:\Users\Ivan\Desktop\Python_1\aws-db\config.cfg')

mysql_config = {
    'user': config.get('MYSQL', 'user'),
    'password': config.get('MYSQL', 'password'),
    'host': config.get('MYSQL', 'host'),
    'database': None,  # Set the database as None initially
}

try:
    # Connect to the MySQL server
    connection = mysql.connector.connect(**mysql_config)
    if connection.is_connected():
        print('Connected to MySQL server')

    # Create a cursor to execute SQL statements
    cursor = connection.cursor()

    # Create the new database if it doesn't exist
    new_database = 'words'  # Replace with your desired database name


    cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(new_database))
    print('Database created:', new_database)

    # Update the MySQL configuration with the new database
    mysql_config['database'] = new_database

    # Example: Create a table in the newly created database
    create_table_query = "CREATE TABLE IF NOT EXISTS my_table (id INT PRIMARY KEY, name VARCHAR(50))"
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully.")

    # Close the cursor and connection
    cursor.close()
    connection.close()
    print("Disconnected from MySQL server.")
except mysql.connector.Error as error:
    print('Error connecting to MySQL server:', error)
