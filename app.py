from flask import Flask, request, jsonify
from auth import auth
from database import get_db_connection
from crypto import kyber_key_exchange, encrypt_password, decrypt_password

app = Flask(__name__)
app.register_blueprint(auth, url_prefix='/auth')

@app.route('/store', methods=['POST'])
def store_password():
    data = request.json
    username = data['username']
    user_password = data['password']

    key = kyber_key_exchange()
    encrypted = encrypt_password(user_password, key)

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO credentials (username, password_enc) VALUES (%s, %s)", (username, encrypted))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"msg": "Password stored securely"}), 201

@app.route('/retrieve', methods=['POST'])
def retrieve_password():
    data = request.json
    username = data['username']

    key = kyber_key_exchange()  # In real implementation, this must be persistent per session/user

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT password_enc FROM credentials WHERE username=%s", (username,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if not row:
        return jsonify({"msg": "No password stored"}), 404

    try:
        password = decrypt_password(row['password_enc'].tobytes(), key)
        return jsonify({"password": password}), 200
    except:
        return jsonify({"msg": "Decryption failed"}), 500
