import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Define the SQL CREATE TABLE statement as a string
    create_table_sql = '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    '''
    # Execute the SQL statement using cursor.execute()
    cursor.execute(create_table_sql)

    # Commit the changes to the database
    conn.commit()

    # Close the database connection
    conn.close()

# Call the function to create the table when the application starts
create_table()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['txt']
        email = request.form['email']
        password = request.form['pswd']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
        conn.commit()
        conn.close()

        return 'User registered successfully!'  # You can render a template or redirect to another page here

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)


