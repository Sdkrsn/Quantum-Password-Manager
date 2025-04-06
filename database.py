import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="quantum_pm",
        user="postgres",  # or your custom username
        password="Sdkrsn@1234",  # replace with the password you set
        cursor_factory=RealDictCursor
    )
    return conn
