from flask import Blueprint, request, jsonify
from database import get_db_connection
from crypto import hash_master_password, verify_master_password

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    password = data['password']

    hashed_pw = hash_master_password(password)

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, master_password) VALUES (%s, %s)", (username, hashed_pw))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"msg": "User registered"}), 201

@auth.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT master_password FROM users WHERE username=%s", (username,))
    user = cur.fetchone()
    cur.close()
    conn.close()

    if not user:
        return jsonify({"msg": "User not found"}), 404

    if verify_master_password(user['master_password'], password):
        return jsonify({"msg": "Login successful"}), 200
    else:
        return jsonify({"msg": "Wrong password"}), 401
