## Creating a Database
- To create a database in MongoDB, start by creating a MongoClient object, then specify a connection URL with the correct ip address and the name of the database 
 you want to create.

- MongoDB will create the database if it does not exist, and make a connection to it
```python 
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
```
## Creating a Collection
- To create a collection in MongoDB, use database object and specify the name of the collection you want to create.

MongoDB will create the collection if it does not exist.
```python
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

mycol = mydb["customers"]
```
## Insert Into Collection

- insert a record, or document as it is called in MongoDB, into a collection, we use the insert_one() method.

- The first parameter of the insert_one() method is a dictionary containing the name(s) and value(s) of each field in the document you want to insert.

- Insert a record in the "customers" collection:
```python
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

```
## find()
- To select data from a table in MongoDB, we can also use the find() method.

- The find() method returns all occurrences in the selection.

- The first parameter of the find() method is a query object. In this example we use an empty query object, which selects all documents in the collection.

- No parameters in the find() method gives you the same result as SELECT * in MySQL.

```python
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Guru"]
mycol = mydb["Guru"]

x = mycol.find_one()

print(x)
```
## Sort () method
```python
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydoc = mycol.find().sort("name")

for x in mydoc:

```

## Sort Descending
Use the value -1 as the second parameter to sort descending.
```python
sort("name", 1) #ascending
sort("name", -1) #descending
```
- Sort the result reverse alphabetically by name:
```python
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydoc = mycol.find().sort("name", -1)

for x in mydoc:
  print(x)
  print(x)
```
## Delete method

```python
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Mountain 21" }

mycol.delete_one(myquery)
```


## Upadate method
```python
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)

```
## limit Method
```python

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myresult = mycol.find().limit(5)

#print the result:
for x in myresult:
  print(x)
```
## Drop Collection
```

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myresult = mycol.find().limit(5)

#print the result:
for x in myresult:
  print(x)

```

## Mangodb Crud Operation
```python
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
mycollection = db["mycollection"]

# Create (Insert) Data
data = {"name": "John", "age": 30}
result = mycollection.insert_one(data)

data_list = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35}
]
result = mycollection.insert_many(data_list)

# Read (Retrieve) Data
result = mycollection.find_one({"name": "John"})
results = mycollection.find()

for doc in results:
    print(doc)

# Update Data
mycollection.update_one({"name": "John"}, {"$set": {"age": 40}})
mycollection.update_many({"age": {"$lt": 30}}, {"$set": {"status": "young"}})

# Delete Data
mycollection.delete_one({"name": "John"})
mycollection.delete_many({"age": {"$gte": 30}})
mycollection.delete_many({})


```
