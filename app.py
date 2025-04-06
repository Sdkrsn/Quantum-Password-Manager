from flask import Flask, request, render_template
from database import PasswordDB
from auth import AuthManager

app = Flask(__name__)
db = PasswordDB()
auth = AuthManager(db)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db.register_user(username, password)
        return "User registered!"
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)