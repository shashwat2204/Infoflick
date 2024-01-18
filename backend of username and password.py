from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

app = Flask(__name__)

# A JSON file to store user data
USERS_FILE = 'users.json'

# Helper functions to load and save user data to the JSON file
def load_users():
    try:
        with open(USERS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file, indent=2)

# Route for the login form
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = load_users()
        if username in users and users[username]['password'] == password:
            return 'Login successful'
        else:
            return 'Invalid username or password'

    return render_template('login.html')

# Route for the sign-up form
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = load_users()
        if username in users:
            return 'Username already exists. Please choose a different one.'

        users[username] = {'password': password}
        save_users(users)
        return 'Sign up successful'

    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
