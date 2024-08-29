from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL connection setup
db_config = {
    'user': 'root',
    'password': 'Haritha@03',
    'host': 'localhost',
    'database': 'expense_tracker'  # Update with your actual database name
}

def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s)', (username, email, password))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_user.html')

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        user_id = request.form['user_id']
        amount = request.form['amount']
        category = request.form['category']
        date = request.form['date']
        description = request.form['description']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO expenses (user_id, amount, category, date, description) VALUES (%s, %s, %s, %s, %s)',
            (user_id, amount, category, date, description)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_expense.html')


@app.route('/view_data')
def view_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM expenses')
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('view_data.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)







