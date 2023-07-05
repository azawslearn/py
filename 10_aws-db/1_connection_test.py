
import mysql.connector
import configparser

# Read the MySQL configuration from the config file
config = configparser.ConfigParser()
config.read(r'C:\Users\Ivan\Desktop\Python_1\aws-db\config.cfg')

mysql_config = {
    'user': config.get('MYSQL', 'user'),
    'password': config.get('MYSQL', 'password'),
    'host': config.get('MYSQL', 'host'),
}

try:
    # Connect to the MySQL server
    connection = mysql.connector.connect(**mysql_config)
    if connection.is_connected():
        print('Connected to MySQL server')

    # Test the connection
    cursor = connection.cursor()
    cursor.execute('SELECT 1')
    result = cursor.fetchone()
    print('MySQL server version:', result[0])

    # Close the cursor and connection
    cursor.close()
    connection.close()
    print('Disconnected from MySQL server')
except mysql.connector.Error as error:
    print('Error connecting to MySQL server:', error)