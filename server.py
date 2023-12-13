from flask import Flask, request, jsonify, make_response
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Initialize SQLite database
def init_sqlite_db():
    with sqlite3.connect('users.db') as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, email TEXT, password TEXT)')
    print("Database initialized!")

init_sqlite_db()

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='sha256')
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users(username, email, password) VALUES (?, ?, ?)", 
                       (data['username'], data['email'], hashed_password))
        conn.commit()

    return jsonify({"message": "User registered successfully!"})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (data['username'],))
        user = cursor.fetchone()

    if not user:
        return make_response('User not found!', 401)

    if check_password_hash(user[3], data['password']):
        return jsonify({"message": "Login successful!"})
    else:
        return make_response('Incorrect password!', 401)

if __name__ == '__main__':
    app.run(debug=True)