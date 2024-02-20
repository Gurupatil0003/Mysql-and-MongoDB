import sqlite3

# Connect to SQLite database (if it doesn't exist, it will be created)
conn = sqlite3.connect('sample.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Drop the existing users table if it exists
cursor.execute("DROP TABLE IF EXISTS users")

# Create a new table with the desired schema, including the 'age' column
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL,
                    age INTEGER)''')

# Insert sample values into the table with the 'age' column
cursor.execute("INSERT INTO users (id, username, email, age) VALUES (?, ?, ?, ?)", (3, 'Guru', 'guru@example.com', 22))
cursor.execute("INSERT INTO users (id, username, email, age) VALUES (?, ?, ?, ?)", (4, 'Mounesh', 'mounesh@example.com', 22))

# Commit the changes
conn.commit()

# Close the connection
conn.close()
