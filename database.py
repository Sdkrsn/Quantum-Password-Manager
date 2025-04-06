import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="quantum_pm",
        user="your_db_user",
        password="your_db_password",
        cursor_factory=RealDictCursor
    )
    return conn
