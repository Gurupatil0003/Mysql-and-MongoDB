# Data base Creation

```python
Create database Guru;
use Guru;
#### Create the "routess" table

CREATE TABLE Peoples(  
    name varchar(45) NOT NULL,  
    age int 
);  

INSERT INTO Peoples (name,age)   
VALUES ('Peter',32);  

SELECT * FROM Peoples;

```
## Using Python
```python
import pymysql

# Establish database connection
mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="mgpatils@",
    db="Guru"
)

# Create a cursor
mycursor = mydb.cursor()

# Define the SQL query
sql = "INSERT INTO peoples (name, age) VALUES (%s, %s)"
val = ("John", "34")

# Execute the query
mycursor.execute(sql, val)

# Commit the changes
mydb.commit()

print(f"{mycursor.rowcount} record inserted.")

```
