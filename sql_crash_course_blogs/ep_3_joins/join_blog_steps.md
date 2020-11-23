### Create new database for this tutorial
```
sqlite3 join_tutorial
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
