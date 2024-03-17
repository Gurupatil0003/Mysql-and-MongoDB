# Mysql Workbench-- Vscode Coonection

*MySQL is an open-source relational database management system (RDBMS) that is widely used for managing and manipulating structured data. It is one of the most popular databases in the world and is a key component of the LAMP (Linux, Apache, MySQL, PHP/Python/Perl) and MERN (MongoDB, Express.js, React, Node.js) stacks, which are commonly used for web development.*

## Here are some key characteristics and features of MySQL:

*-Relational Database Management System (RDBMS): MySQL is a relational database, which means it organizes data into tables with rows and columns. It follows the principles of relational database management and supports SQL (Structured Query Language) for interacting with the database.*

*-Open Source: MySQL is released under the GNU General Public License (GPL) and is freely available for use, modification, and distribution.*

*Cross-Platform Compatibility: MySQL is cross-platform, meaning it can run on various operating systems such as Linux, Windows, and macOS.*

*Scalability: MySQL is designed to be scalable, supporting the growth of databases as the amount of data and the number of users increase. It can handle both small and large-scale applications.*

*Performance: MySQL is known for its high performance and can efficiently handle complex queries and large datasets.*

*Community Support: Being open source, MySQL has a large and active community of developers and users. This community support is valuable for troubleshooting, sharing knowledge, and contributing to the improvement of the software.*

*Storage Engines: MySQL supports multiple storage engines, each with its own strengths and use cases. The most commonly used storage engine is InnoDB, which provides features like ACID compliance and transaction support.*

*Security: MySQL provides various security features, including user authentication, access control, and encryption. It allows database administrators to define user privileges and restrict unauthorized access.*

*Replication and Clustering: MySQL supports replication, allowing data to be copied to multiple servers for fault tolerance and performance. It also supports clustering for high availability and load balancing.*


# open your Mysql Workbench
-Below you will find 
-Username
-Server Address
-Port Number


<img width="100%" src="https://github.com/Gurupatil0003/Mysql_vs_Vscode_Connect/blob/main/Mysql%2C%20MangoDB%20vs%20Vscode/Screenshot%202023-12-22%20084930.png"/>

#Here In below Screenshot U can see My tables


# Here In below Screenshot U can see My databases and Tables

#Create your Own Database 
-you can create Database Using Below Code
```python

Create database patils;

```

- Successfully created your Datbase

# View Ur Database

-Using Below Code You can View Your Created Databases

```python

SHOW DATABASES;

```
```python

Create database patils;
```

#### Use ur Create Table
```python

USE patils;
```python

#### Create the "routess" table

CREATE TABLE routess (
    name VARCHAR(255),
    age INT
);


```
<img width="100%" src="https://github.com/Gurupatil0003/Mysql_vs_Vscode_Connect/blob/main/Screenshot%202024-03-17%20103108.png"/>


### Open Ur vscode .... Below u can see the code

```python
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mgpatils",
    database="patils"
)

if conn.is_connected():
    print("Connected to MySQL database")
    cursor = conn.cursor()

    # Insert data into table
    sql_insert = "INSERT INTO routess (name, age) VALUES (%s, %s)"
    values = [("John", 30), ("Alice", 25)]
    cursor.executemany(sql_insert, values)
    conn.commit()
    print(cursor.rowcount, "records inserted.")

    # Retrieve data from table
    cursor.execute("SELECT * FROM routess")

    rows = cursor.fetchall()
    print("Fetched data:")
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    conn.close()
    print("MySQL connection closed.")
else:
    print("Failed to connect to MySQL database")



```
<img width="100%" src="https://github.com/Gurupatil0003/Mysql_vs_Vscode_Connect/blob/main/Screenshot%202024-03-17%20103130.png"/>




# THE END and Thank You


# See You Again

<img width="100%" src="https://github.com/Gurupatil0003/Mysql_vs_Vscode_Connect/blob/main/Mysql%2C%20MangoDB%20vs%20Vscode/spy-x-family-anya-heh.gif"/>

