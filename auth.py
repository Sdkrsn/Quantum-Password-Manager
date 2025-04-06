from database import get_db_connection
from crypto import hash_master_password, verify_master_password

def register_user(username, password):
    conn = get_db_connection()
    cur = conn.cursor()
    hashed_pw = hash_master_password(password)
    try:
        cur.execute("INSERT INTO users (username, master_password) VALUES (%s, %s)",
                    (username, hashed_pw))
        conn.commit()
        return True
    except:
        return False
    finally:
        cur.close()
        conn.close()

def authenticate_user(username, password):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT master_password FROM users WHERE username = %s", (username,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    if result:
        return verify_master_password(result['master_password'], password)
    return False
