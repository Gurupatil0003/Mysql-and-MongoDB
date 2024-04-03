from flask import Flask, render_template, request, redirect, session
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mgpatils'
app.config['MYSQL_DB'] = 'patils'
mysql = MySQL(app)

# Secret key for session management
app.secret_key = 'your_secret_key'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        userDetails = request.form
        username = userDetails['username']
        password = userDetails['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO usera(username, password) VALUES(%s, %s)", (username, password))
        mysql.connection.commit()
        cur.close()
        return redirect('/login')
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userDetails = request.form
        username = userDetails['username']
        password = userDetails['password']
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM usera WHERE username = %s AND password = %s", (username, password))
        if result > 0:
            session['loggedin'] = True
            session['username'] = username
            return 'Logged in successfully!'
        else:
            return 'Incorrect username/password!'
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
