![JOIN Venn Diagram](imgs/join_venn_diagram)
### INNER JOIN
- will only return connected rows if there is a matching value in both tables

t1.name    |t1.ID     |t2.country   |t2.ID
...         1           ...          1
...         2           ...          2
...         3           ...          3

### LEFT JOIN 
- will return every row from the left table (even if there is no matching row in the right table), but only rows from the right table if they have a corresponding values in the left table (will return NULLs in place)

t1.name    |t1.ID     |t2.country   |t2.ID
...         4           ...          4
...         5           NULL         NULL
...         6           ...          6

### RIGHT JOIN
- will return every row from the right table (even if there is no matching row in the left table), and will only return rows from the left table that have corresponding values in the left right (will return NULLs in place)

t1.name    |t1.ID     |t2.country   |t2.ID
...         7           ...          7
NULL        NULL        ...          8
...         9           ...          9

### FULL JOIN (FULL OUTER JOIN)
_MySQL and SQLite do not support FULL JOINs_
- combination of the LEFT and RIGHT JOIN
- ill return every row from left and right tables. When corresponding columns have matching values, rows are connected.  When corresponding rows don't have a match in the other table, NULLs are used in their place

t1.name    |t1.ID     |t2.country   |t2.ID
...         10          ...          10
NULL        NULL        ...          11
...         12          NULL         NULL


- we need to join tables when there is useful information about an item in one table located in another
- we join tables on common columns
- NULLs are treated differently depending on the type of join

### process
- start with a SELECT statement for all the columns (from both tables) you wish to access, initially we only select FROM the first table
```
SELECT *
    FROM clients            "Left table"
```
- then add our JOIN statement followed by the second table we wish to access
```
    INNER JOIN countries    "Right table"
```
- we call the first table (in the FROM clause) the "left table" and the second table (indicated in our INNER JOIN clause) ur "right table"
- the join keyword indicates we'll be joining these two tables
- we then have to specify "how" to connect rows from these two tables by using an ON clause
```
ON clients.Country_ID = countries.Country_ID;
```
- we use the syntax `first_table.common_column = second_table.common_column` to tell SQL that `common_column` holds the same data in each table, and that we watnt to use this column to link information between tables

- the return will be all rows and columns in both tables
- if entries in one table don't have a corresponding value in `common_column` in the other table, those entries are not returned in the JOIN statement