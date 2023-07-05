
import pandas as pd
import mysql.connector
import configparser

# Read the MySQL configuration from the config file
config = configparser.ConfigParser()
config.read(r'C:\Users\Ivan\Desktop\Python_1\aws-db\config.cfg')

# Read the CSV file
csv_file = r"C:\Users\Ivan\Desktop\Python_1\aws-db\german_gender.csv"
df = pd.read_csv(csv_file, encoding="UTF-8", header=0)

# Extract the desired columns
column1 = df['index']
column2 = df['gender_singular']
column3 = df['remark']
column4 = df['plural_form']
column5 = df['translation']
column6 = df['number']
column7 = df['gender_short']

# Establish a connection to MySQL
mysql_config = {
    'user': config.get('MYSQL', 'user'),
    'password': config.get('MYSQL', 'password'),
    'host': config.get('MYSQL', 'host'),
    'database': "words",  # Set the database as None initially
}

# Connect to the MySQL server
connection = mysql.connector.connect(**mysql_config)

# Create a cursor to execute SQL statements
cursor = connection.cursor()

# Create the gender_table
table_name_1 = 'gender_table'
create_table_query_1 = f"CREATE TABLE IF NOT EXISTS {table_name_1} (gender_index INT, gender_gender VARCHAR(255), gender_translation VARCHAR(255), gender_number INT, gender_short VARCHAR(255))"
cursor.execute(create_table_query_1)

# Truncate the gender_table
truncate_query_1 = f"TRUNCATE TABLE {table_name_1}"
cursor.execute(truncate_query_1)

# Insert data into the gender_table
for i in range(len(column1)):
    insert_query = f"INSERT INTO {table_name_1} (gender_index, gender_gender, gender_translation, gender_number, gender_short) VALUES (%s, %s, %s, %s, %s)"
    values = (int(column1[i]), str(column2[i]), str(column5[i]), int(column6[i]), str(column7[i]))
    cursor.execute(insert_query, values)

# Commit the changes for gender_table
connection.commit()

print('gender table created and data inserted successfully.')


# Create the remarks_table
table_name_2 = 'remarks_table'
create_table_query_2 = f"CREATE TABLE IF NOT EXISTS {table_name_2} (remark_index INT, remark_remark VARCHAR(255), remark_number INT)"
cursor.execute(create_table_query_2)

# Truncate the remarks_table
truncate_query_2 = f"TRUNCATE TABLE {table_name_2}"
cursor.execute(truncate_query_2)

# Insert data into the remarks_table
for i in range(len(column1)):
    insert_query = f"INSERT INTO {table_name_2} (remark_index, remark_remark, remark_number) VALUES (%s, %s, %s)"
    values = (int(column1[i]), str(column3[i]), int(column6[i]))
    cursor.execute(insert_query, values)

# Commit the changes for remarks_table
connection.commit()

print('remarks table created and data inserted successfully.')

# Create the remarks_table
table_name_3 = 'plural_table'
create_table_query_3 = f"CREATE TABLE IF NOT EXISTS {table_name_3} (plural_index INT, plural_plural VARCHAR(255))"
cursor.execute(create_table_query_3)

# Truncate the remarks_table
truncate_query_2 = f"TRUNCATE TABLE {table_name_3}"
cursor.execute(truncate_query_2)

# Insert data into the remarks_table
for i in range(len(column1)):
    insert_query = f"INSERT INTO {table_name_3} (plural_index, plural_plural) VALUES (%s, %s)"
    values = (int(column1[i]), str(column4[i]))
    cursor.execute(insert_query, values)

# Commit the changes for remarks_table
connection.commit()

# Close the cursor and connection


print('plural table created and data inserted successfully.')


csv_file = r"C:\Users\Ivan\Desktop\Python_1\aws-db\examples.csv"
df1 = pd.read_csv(csv_file, encoding="UTF-8", header=0)

exaples_column1 = df1['index']
exaples_column2 = df1['example']
exaples_column3 = df1['translation']

table_name_4 = 'example_table'
create_table_query_4 = f"CREATE TABLE IF NOT EXISTS {table_name_4} (examples_index INT, examples_examples VARCHAR(255), examples_translation VARCHAR(255))"
cursor.execute(create_table_query_4)

# Truncate the gender_table
truncate_query_4 = f"TRUNCATE TABLE {table_name_4}"
cursor.execute(truncate_query_4)

# Insert data into the gender_table
for i in range(len(exaples_column1)):
    insert_query = f"INSERT INTO {table_name_4} (examples_index, examples_examples, examples_translation) VALUES (%s, %s, %s)"
    values = (int(exaples_column1[i]), str(exaples_column2[i]), str(exaples_column3[i]))
    cursor.execute(insert_query, values)

# Commit the changes for gender_table
connection.commit()

print('examples table created and data inserted successfully.')

cursor.close()
connection.close()