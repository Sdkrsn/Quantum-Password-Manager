import os

DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_NAME = "password_manager"
DB_HOST = "localhost"

SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.urandom(32)
