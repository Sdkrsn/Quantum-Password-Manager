from flask import Flask, request, render_template, redirect, url_for
from auth import register_user, authenticate_user

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Register page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        success = register_user(request.form['username'], request.form['password'])
        if success:
            return redirect(url_for('login'))
        else:
            return "Registration failed. Try a different username."
    return render_template('register.html')

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        success = authenticate_user(request.form['username'], request.form['password'])
        if success:
            return redirect(url_for('dashboard'))
        else:
            return "Login failed. Please check your credentials."
    return render_template('login.html')

# Dashboard (after login)
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
