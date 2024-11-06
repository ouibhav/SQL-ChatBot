import sqlite3

## connect to sqllite
connection=sqlite3.connect("sample2.db")

##create a cursor object to insert record,create table
cursor=connection.cursor()

## create the table
table_info="""
CREATE TABLE Products(product_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL)
"""

cursor.execute(table_info)

table_info="""
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL
)
"""

cursor.execute(table_info)

table_info="""
CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY,
    order_id INT,
    amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
)
"""

cursor.execute(table_info)

## Insert some more records

cursor.execute('''INSERT INTO Products VALUES(1, 'Laptop', 1200.00)''')
cursor.execute('''INSERT INTO Products VALUES(2, 'Smartphone', 800.00)''')
cursor.execute('''INSERT INTO Products VALUES(3, 'Tablet', 400.00)''')
cursor.execute('''INSERT INTO Orders VALUES(1, 101, '2024-10-15')''')
cursor.execute('''INSERT INTO Orders VALUES(2, 102, '2024-10-22')''')
cursor.execute('''INSERT INTO Orders VALUES(3, 103, '2024-09-01')''')
cursor.execute('''INSERT INTO Transactions VALUES(1, 1, 1200.00)''')
cursor.execute('''INSERT INTO Transactions VALUES(2, 2, 800.00)''')
cursor.execute('''INSERT INTO Transactions VALUES(3, 3, 400.00)''')

## Display all the records
print("The inserted records are")
data=cursor.execute('''Select * from Products''')
for row in data:
    print(row)
data=cursor.execute('''Select * from Orders''')
for row in data:
    print(row)
data=cursor.execute('''Select * from Transactions''')
for row in data:
    print(row)

## Commit your changes in the database
connection.commit()
connection.close()
