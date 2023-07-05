const mysql = require('mysql');
const config = require('./config');

// Create a MySQL connection
const connection = mysql.createConnection({
  host: config.MYSQL.host,
  user: config.MYSQL.user,
  password: config.MYSQL.password,
});

// Connect to the MySQL server
connection.connect((error) => {
  if (error) {
    console.error('Error connecting to MySQL server:', error);
    return;
  }
  console.log('Connected to MySQL server');

  // Create the new database if it doesn't exist
  const newDatabase = 'nodeDB'; // Replace with your desired database name
  connection.query(`CREATE DATABASE IF NOT EXISTS ${newDatabase}`, (error) => {
    if (error) {
      console.error('Error creating database:', error);
      connection.end();
      return;
    }
    console.log('Database created:', newDatabase);

    // Switch to the newly created database
    connection.changeUser({ database: newDatabase }, (error) => {
      if (error) {
        console.error('Error switching to database:', error);
        connection.end();
        return;
      }

      // Create a table in the newly created database
      const createTableQuery = 'CREATE TABLE IF NOT EXISTS nodeTABLE (id INT PRIMARY KEY, name VARCHAR(50))';
      connection.query(createTableQuery, (error) => {
        if (error) {
          console.error('Error creating table:', error);
          connection.end();
          return;
        }
        console.log('Table created successfully.');

        // Close the MySQL connection
        connection.end((error) => {
          if (error) {
            console.error('Error disconnecting from MySQL server:', error);
            return;
          }
          console.log('Disconnected from MySQL server.');
        });
      });
    });
  });
});