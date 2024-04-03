from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Guru']
collection = db['Guru']

# Insert one document
data = {
    'id': 1,  # Example id
    'username': 'john_doe',
    'password': 'password123',
    'name': 'John',
    'age': 30,
    'email': 'john@example.com'
}
insert_result = collection.insert_one(data)
print("Inserted document ID:", insert_result.inserted_id)

# Insert multiple documents
data_list = [
    {'id': 2, 'username': 'alice_smith', 'password': 'pass456', 'name': 'Alice', 'age': 25, 'email': 'alice@example.com'},
    {'id': 3, 'username': 'bob_jones', 'password': 'bob_pass', 'name': 'Bob', 'age': 35, 'email': 'bob@example.com'},
    {'id': 4, 'username': 'charlie_brown', 'password': 'brown_pass', 'name': 'Charlie', 'age': 40, 'email': 'charlie@example.com'}
]
insert_result = collection.insert_many(data_list)
print("Inserted document IDs:", insert_result.inserted_ids)
