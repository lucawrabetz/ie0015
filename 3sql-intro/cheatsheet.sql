/* SQLite CHEAT SHEET */

/* luca@lucambp ~ sqlite3    --- Start sqlite prompt */

/* sqlite3 (SQLite command line client) dot commands */

/* sqlite> .open file.db    --- Opens or creates a database file */
/* sqlite> .close    --- Closes the current database connection */
/* sqlite> .quit / .exit    --- Exits the sqlite3 shell */
/* sqlite> .databases    --- Lists open database connections */
/* sqlite> .tables    --- Lists tables in the current database */
/* sqlite> .schema [table]    --- Shows the CREATE statement for a table */
/* sqlite> .headers on | off    --- Toggles display of column headers */
/* sqlite> .mode column | list    --- Sets output mode (column or list) */
/* sqlite> .separator [char]    --- Sets the field separator for .import */
/* sqlite> .import file table    --- Imports data from a CSV file into a table */
/* sqlite> .dump    --- Exports the database schema and data */


/* Remember - you can run SQL code in the sqlite3 prompt! */

/* sqlite> SELECT * FROM table    --- Retrieves all rows from a table */
/* sqlite> SELECT col1, col2 FROM table    --- Retrieves specific columns */
/* sqlite> SELECT * FROM table WHERE condition    --- Filters rows based on a condition */
/* sqlite> INSERT INTO table (cols) VALUES (vals)    --- Inserts a new row */
/* sqlite> CREATE TABLE table (cols)    --- Creates a new table */
/* sqlite> UPDATE table SET col=val WHERE condition    --- Updates existing rows */
/* sqlite> DELETE FROM table WHERE condition    --- Deletes rows based on a condition */
/* sqlite> CREATE TABLE table (cols)    --- Creates a new table */
/* sqlite> DROP TABLE table    --- Deletes a table */
/* sqlite> SELECT * FROM listings WHERE DATE(host_since) > '2022-01-01' */
/* sqlite> SELECT * FROM listings ORDER BY DATE(host_since) */
/* sqlite> SELECT strftime('%Y-%m-%d', host_since) AS formatted_date FROM listings */
/* sqlite> SELECT strftime('%Y-%m-%d %H:%M:%S', host_since) AS formatted_date_time FROM listings */
/* sqlite> SELECT strftime('%d %b %Y', host_since) AS formatted_date_month_name FROM listings */

/* TABLES TO BE CREATED FOR AIRBNB DATASET */
CREATE TABLE listings (
  id INTEGER PRIMARY KEY,
  host_since TEXT,
  host_response_rate REAL,
  host_acceptance_rate REAL,
  price REAL,
  minimum_nights INTEGER,
  review_scores_rating REAL
);

CREATE TABLE reviews (
  id INTEGER PRIMARY KEY,
  listing_id INTEGER,
  reviewer_name TEXT,
  comments TEXT,
  FOREIGN KEY (listing_id) REFERENCES listings(id)
);
