Navigate to a new empty directory in the terminal.

Type `sqlite3 test.db`, does two things:
- typing `sqlite3` will open the SQLite editor in your terminal
- typing `test.db` will create a new database called `test.db` that you can now add tables to
    - you can call `test.db` whatever you want
    - this command will also create a new file called `test.db` at your current location within your working diretory, this file is where SQLite will keep track of all of the data/tables belonging to the `test `database

Next, inside the SQLite editor, enter the following command to create a new table called `countries` within `test.db`(we are already connected to the `test` database since we specified `test.db` in our `sqlite3` command):
```
CREATE TABLE IF NOT EXISTS countries(
    generated_id INTEGER PRIMARY KEY,
    Country_ID INT(255) NOT NULL, 
    Country_Name VARCHAR(255) NOT NULL
    );
```
Now that we have a table, we need to add some rows to it:
```
INSERT INTO country(Country_ID, Country_Name)
VALUES 
    (8001, 'United States'),
    (8002, 'Canada');
```
Finally, let's check that our new entries have been added to our `country` table:
```
SELECT * FROM country;
```
Should see the following output:
```
1|8001|United States
2|8002|Canada
```
/*---------------*/

Now let's add a second table, we'll call it `clients`:

```
CREATE TABLE IF NOT EXISTS clients (
    generated_id INTEGER PRIMARY KEY,
    Client_Name VARCHAR(255) NOT NULL, 
    Country_ID INT(255) NOT NULL, 
    Date DATE NOT NULL
    );
```
`clients` need some entries as well, let's add those now:
```
INSERT INTO clients(Client_Name, Country_ID, Date)
VALUES 
    ('American Co.', 8001, CURRENT_DATE),
    ('Canadian Co.', 8002, CURRENT_DATE);
```
Now let's do a final check to make sure these values made it to the table:
```
SELECT * FROM clients;
```
Should see the following output:
```
1|American Co.|8001|2020-11-13
2|Canadian Co.|8002|2020-11-13
```

/*-----------------------*/


```
SELECT * FROM clients cl INNER JOIN country co
    ON cl.Country_ID=co.Country_ID;
```