from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# MySQL Configuration
db = pymysql.connect(
    host='localhost',
    user='root',
    password='mgpatils',
    database='patils'
)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor = db.cursor()
        cursor.execute('SELECT * FROM usera WHERE username = %s AND password = %s', (username, password))
        user = cursor.fetchone()

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
