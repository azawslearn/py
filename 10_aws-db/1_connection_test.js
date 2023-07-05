const mysql = require('mysql');
const config = require('./config');

// Read the MySQL configuration from the config file
const mysqlConfig = config.MYSQL;

// Create a MySQL connection pool
const pool = mysql.createPool(mysqlConfig);

// Use the connection pool to query the database
pool.query('SELECT 1', (error, results) => {
  if (error) {
    console.error('Error connecting to MySQL server:', error);
  } else {
    console.log('Connected to MySQL server');
    console.log('MySQL server version:', results[0][0]);
  }
  
  // Close the connection pool
  pool.end();
});