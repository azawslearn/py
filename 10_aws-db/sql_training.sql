
#to query a table you need to first select the DB
USE words;

#select everything from a table and filter by id
SELECT *
FROM gender_table
WHERE gender_index = 1;

SELECT *
FROM gender_table
ORDER BY gender_gender;

#we can specify the name of the column we want

SELECT gender_gender 
FROM gender_table;

#we cann add numbers
#we can add aliases

SELECT 
	gender_gender, 
    gender_index, 
    gender_number, 
    gender_number + 10,
    gender_number + 10 AS alias_column
FROM gender_table;

#### WHERE CLAUES ###

SELECT *
FROM gender_table 
WHERE gender_index > 100;

SELECT *
FROM gender_table 
WHERE gender_short = 'F';

## Multiple conditions

SELECT *
FROM gender_table 
WHERE gender_index > 100 AND gender_short = 'N';

#WHERE NOT

SELECT *
FROM gender_table 
WHERE NOT gender_index > 100 AND gender_short = 'N';

#using IN

SELECT *
FROM gender_table 
WHERE gender_short IN ('N');


SELECT *
FROM gender_table 
WHERE gender_short NOT IN ('N');


#USING BETWEEN

SELECT *
FROM gender_table 
WHERE gender_index BETWEEN 40 AND 50;

#Rows that match specific word pattern LIKE
# we use % to indicate any number of characters
# we use _ for a single character

SELECT *
FROM gender_table 
WHERE gender_index LIKE '4%';

SELECT *
FROM gender_table 
WHERE gender_index LIKE '__4%';


#with the operator REGEXP we can use regular expresions
SELECT *
FROM gender_table 
WHERE gender_index REGEXP '44';

#looking for null values
SELECT *
FROM gender_table 
WHERE gender_index IS NULL;

#looking for null values
SELECT *
FROM gender_table 
WHERE gender_index IS NOT NULL;

#limit the results that we receive - LIMIT

SELECT *
FROM gender_table 
LIMIT 3;


#JOINS

SELECT *
FROM gender_table 
INNER JOIN plural_table ON gender_table.gender_index = plural_table.plural_index;

SELECT gender_index, plural_index, gender_gender, plural_plural
FROM gender_table 
INNER JOIN plural_table ON gender_table.gender_index = plural_table.plural_index;

#ADDING ALIASES

SELECT gender_index, plural_index, gender_gender, plural_plural
FROM gender_table g
INNER JOIN plural_table p
	ON g.gender_index = p.plural_index;

# JOINING Multiple tables

SELECT *
FROM gender_table g
INNER JOIN plural_table p
	ON g.gender_index = p.plural_index
JOIN remarks_table r
	ON g.gender_index = r.remark_index;
    


SELECT
	g.gender_index,
    g.gender_gender,
	p.plural_plural,
    r.remark_remark
FROM gender_table g
INNER JOIN plural_table p
	ON g.gender_index = p.plural_index
JOIN remarks_table r
	ON g.gender_index = r.remark_index;
    
#Joining on multiple tables 

SELECT *
FROM gender_table g
JOIN remarks_table r
	ON g.gender_index = r.remark_index
    AND g.gender_number = r.remark_number;
    
#LEFT / RGHT JOIN
# WE DO THE LEFT OR THE RIGHT join in order to see all the records for the table on the left or in the right

#INNER JOIN 

SELECT *
FROM gender_table g
JOIN example_table e
	ON g.gender_index = e.examples_index;

SELECT *
FROM gender_table g
LEFT JOIN example_table e
	ON g.gender_index = e.examples_index;
    
SELECT * 
FROM example_table e
RIGHT JOIN gender_table g
	on g.gender_index = e.examples_index;
    
#INSERTING DATA 

#in this way, we need to provide values for all the colums
INSERT INTO plural_table
VALUES (223, 'Plural Form');

#in this way we can specify only values for the columns we have already named
INSERT INTO plural_table (
#we specify the columns where we will insert data
plural_index,
plural_plural
)
VALUES (
223, 
'plural_form');

#insert multiple rows

INSERT INTO plural_table (
#we specify the columns where we will insert data
plural_index,
plural_plural
)
VALUES (223, 'plural_form'),
       (224, 'plural_form'),
       (225, 'plural_form');


    
    

