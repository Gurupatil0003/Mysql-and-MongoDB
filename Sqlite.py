from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Function to connect to SQLite database
def connect_db():
    conn = sqlite3.connect('sample.db')
    return conn

# Route to display data from the database
@app.route('/')
def display_data():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    conn.close()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
