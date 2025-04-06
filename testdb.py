from database import get_db_connection

try:
    conn = get_db_connection()
    print("✅ Connected to PostgreSQL!")
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)
