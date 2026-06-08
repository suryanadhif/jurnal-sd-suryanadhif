import os
from dotenv import load_dotenv

load_dotenv()

db_password = os.getenv("DB_PASSWORD")

print("DB_PASSWORD :", db_password)