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

    # Create function to insert data
    def insert_data(name, age):
        sql_insert = "INSERT INTO routess (name, age) VALUES (%s, %s)"
        values = (name, age)
        cursor.execute(sql_insert, values)
        conn.commit()
        print(cursor.rowcount, "record inserted.")

    # Read function to retrieve data
    def fetch_data():
        cursor.execute("SELECT * FROM routess")
        rows = cursor.fetchall()
        print("Fetched data:")
        for row in rows:
            print(row)

    # Update function to modify existing data
    def update_data(name, new_age):
        sql_update = "UPDATE routess SET age = %s WHERE name = %s"
        values = (new_age, name)
        cursor.execute(sql_update, values)
        conn.commit()
        print(cursor.rowcount, "record(s) updated.")

    # Delete function to remove data
    def delete_data(name):
        sql_delete = "DELETE FROM routess WHERE name = %s"
        values = (name,)
        cursor.execute(sql_delete, values)
        conn.commit()
        print(cursor.rowcount, "record(s) deleted.")

    # Testing CRUD operations
    insert_data("Bob", 35)  # Create
    fetch_data()            # Read
    update_data("John", 40) # Update
    fetch_data()            # Read
    delete_data("Alice")    # Delete
    fetch_data()            # Read

    # Close cursor and connection
    cursor.close()
    conn.close()
    print("MySQL connection closed.")
else:
    print("Failed to connect to MySQL database")




```

### Output in VScode terminal
<img width="100%" src="https://github.com/Gurupatil0003/Mysql-and-MongoDB/blob/main/Screenshot%202024-03-18%20233925.png"/>

### Mysql Workbench output
<img width="100%" src="https://github.com/Gurupatil0003/Mysql-and-MongoDB/blob/main/Screenshot%202024-03-18%20234211.png"/>



# MongoDB 
MongoDB is a popular open-source, NoSQL database management system that stores data in flexible, JSON-like documents. It is designed for scalability, performance, and high availability. MongoDB uses a document-oriented data model, which means data is stored in JSON-like documents instead of rows and columns like traditional relational databases.

#### Lets Start with installation
[Download MongoDB Compass](https://www.mongodb.com/try/download/compass)

<img width="100%" src="https://github.com/Gurupatil0003/Mysql_vs_Vscode_Connect/blob/main/Screenshot%202024-03-18%20232009.png"/>

### Click on Create Database 

<img width="100%" src="https://github.com/Gurupatil0003/Mysql_vs_Vscode_Connect/blob/main/Screenshot%202024-03-18%20232052.png"/>


### Manogodb -- CRUD operation
```python
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Guru"]
collection = db["Guru"]

# Create (Insert) Operation
def create_document(data):
    result = collection.insert_one(data)
    print("Inserted document id:", result.inserted_id)

# Read (Retrieve) Operation
def read_documents():
    cursor = collection.find()
    print("Fetched data:")
    for document in cursor:
        print(document)

# Update Operation
def update_document(filter, update):
    result = db.command("update", "mycollection", updates=[{"q": filter, "u": update}])
    print(result)

# Delete Operation
def delete_document(filter):
    result = db.command("delete", "mycollection", deletes=[{"q": filter, "limit": 1}])
    print(result)

# Example usage
if __name__ == "__main__":
    # Create document
    create_document({"name": "John", "age": 30})

    # Read documents
    read_documents()

    # Update document
    update_document({"name": "John"}, {"$set": {"age": 35}})

    # Read documents after update
    read_documents()

    # Delete document
    delete_document({"name": "John"})

    # Read documents after deletion
    read_documents()

# Close MongoDB connection
client.close()
```

<img width="100%" src="https://github.com/Gurupatil0003/Mysql-and-MongoDB/blob/main/Screenshot%202024-03-19%20000152.png"/>

### Here same code with Image Data

```python
import pymongo
import base64

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Guru"]
collection = db["Guru"]

# Create (Insert) Operation
def create_document(data):
    result = collection.insert_one(data)
    print("Inserted document id:", result.inserted_id)

# Read (Retrieve) Operation
def read_documents():
    cursor = collection.find()
    print("Fetched data:")
    for document in cursor:
        print(document)

# Update Operation
def update_document(filter, update):
    result = collection.update_one(filter, update)
    print(result.modified_count, "document(s) updated.")

# Delete Operation
def delete_document(filter):
    result = collection.delete_one(filter)
    print(result.deleted_count, "document(s) deleted.")

# Function to insert image data
def insert_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_image

# Example usage
if __name__ == "__main__":
    # Create documents
    image_path = "C:\\Users\\LENOVO\\hh\\immg.jpeg"  # Path to your image file
    image_data = insert_image(image_path)
    
    create_document({
        "name": "John",
        "rollnumber": 12345,
        "div": "A",
        "semester": 1,
        "image": image_data
    })

    # Read documents
    read_documents()

    # Update document
    update_document({"name": "John"}, {"$set": {"semester": 2}})

    # Read documents after update
    read_documents()

    # Delete document
    delete_document({"name": "John"})

    # Read documents after deletion
    read_documents()

# Close MongoDB connection
client.close()

```

### Finall out Come

<img width="100%" src="https://github.com/Gurupatil0003/Mysql_vs_Vscode_Connect/blob/main/Screenshot%202024-03-18%20232542.png"/>

# THE END and Thank You


# See You Again

<img width="100%" src="https://github.com/Gurupatil0003/Mysql_vs_Vscode_Connect/blob/main/Mysql%2C%20MangoDB%20vs%20Vscode/spy-x-family-anya-heh.gif"/>

