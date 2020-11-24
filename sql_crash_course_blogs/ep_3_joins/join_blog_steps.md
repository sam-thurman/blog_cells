### Create new database for this tutorial
```
sqlite3 JOIN_tutorial
```
### Create `clients`, `countries`, `orders` and `products` tables
```
CREATE TABLE IF NOT EXISTS clients(
    generated_id INT PRIMARY KEY,
    Client_Name TEXT NOT NULL, 
    Country_ID INT NOT NULL
    );
```
```
CREATE TABLE IF NOT EXISTS countries(
    generated_ID INT PRIMARY KEY,
    Country_Name TEXT NOT NULL,
    Country_ID INT NOT NULL
    );
```
```
CREATE TABLE IF NOT EXISTS orders(
    generated_ID INT PRIMARY KEY,
    Client_Name TEXT NOT NULL,
    Product_Code INT NOT NULL,
    Quantity INT NOT NULL,
    Order_Date TEXT NOT NULL
    );
```
```
CREATE TABLE IF NOT EXISTS products(
    generated_ID INT PRIMARY KEY,
    Product_Name TEXT NOT NULL,
    Product_Code INT NOT NULL
    );
```
### Insert values into all the tables so they make sense for our exercise
```
INSERT INTO clients (Client_Name, Country_ID)
    VALUES
    ("Paddy's Pub", 8001),
    ("Universal Exports", 8003),
    ("Bubbles' Shed n' Breakfast", 8002),
    ("Stay Puft", 8001),
    ("Han's Garage", 8004);
    
```
```
INSERT INTO countries(Country_Name, Country_ID)
    VALUES
    ("United States", 8001),
    ("Canada", 8002),
    ("United Kingdom", 8003),
    ("Japan", 8004);
```
```
INSERT INTO products(Product_Name, Product_Code)
    VALUES
    ("N65 Mask (20ct)", 176123),
    ("Powder Free Latex Gloves (200ct)", 143185),
    ("Hand Sanitizer 8oz.", 735162),
    ("Facial Tissue (120ct per box)", 196109),
    ("Small Plastic Drum (5 gal)", 935671),
    ("Medium Plastic Drum (10 gal)", 935682),
    ("Large Plastic Drum (20 gal)", 935693);
```
```
INSERT INTO orders(Client_Name, Product_Code, Quantity, Order_Date)
        VALUES
        ("Paddy's Pub", 735162, 20, DATE()),
        ("Stay Puft", 176123, 5, DATE()),
        ("Bubbles' Shed n' Breakfast", 935671, 5, DATE()),
        ("Bubbles' Shed n' Breakfast", 935693, 2, DATE()),
        ("Universal Exports", 143185, 100, DATE()),
        ("Han's Garage", 176123, 20, DATE()),
        ("Paddy's Pub", 176123, 1, DATE());
```

### INNER JOINing our tables
If we wanted to get a list of our current outstanding orders, and easily be able to tell what each item is, we could select all the data from both `orders` and `products` tables
```
SELECT * 
    FROM orders
    INNER JOIN products
    ON orders.Product_Code = products.Product_Code;
```
You'll notice that we actually have two `Product_Code` columns in our return.  This is default behavior when using `SELECT *` and a `JOIN` statement, we can escape this behavior by explicilty asking for our columns as opposed to using `*`. Doing this, we are also able to organize our returned columns in whatever order we'd like.

When we explicitly ask for a shared column (called an ambiguous column), we always have to specify which table we want the information from. In the case of a `JOIN`, it really doesn't matter which table we choose to pull from since both tables contain the same information in that column. If we were to be pulling from a column with a shared name but containing different information (`generated_ID` column), then we would have to be a little more careful about which column we speficy in our `SELECT` statement.
```
SELECT Client_Name, Order_Date, Product_Name, Quantity, orders.Product_Code
    FROM orders
    INNER JOIN products
    ON orders.Product_Code = products.Product_Code;
```

We don't always necessarily need to grab all the columns, though.  And sometimes, we don't even need data from our ON column, we simply need to use it to link tables.  Here's an example where we JOIN our tables on `Country_ID` but only ask for data from `Client_Name` and `Country_Name`
```
SELECT Client_Name, Country_Name
    FROM clients
    INNER JOIN countries
    ON clients.Country_ID = countries.Country_ID;
```