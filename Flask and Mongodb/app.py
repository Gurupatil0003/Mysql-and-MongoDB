from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Configuration
client = MongoClient('mongodb://localhost:27017/')
db = client['Guru']
users_collection = db['Guru']

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = users_collection.find_one({'username': username, 'password': password})

        if user:
            # Login successful
            return redirect(url_for('success'))
        else:
            # Login failed
            return render_template('index.html', error='Invalid username or password')

    return render_template('index.html')

@app.route('/success')
def success():
    return 'Login Successful!'

if __name__ == '__main__':
    app.run(debug=True)
