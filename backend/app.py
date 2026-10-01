from flask import Flask, jsonify
import mysql.connector
import os
from dotenv import load_dotenv

# Load the secret variables from the .env file
load_dotenv()

app = Flask(__name__)

# Create a function to connect to the database
def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return connection

# A simple test route to verify everything works
@app.route('/', methods=['GET'])
def test_connection():
    try:
        conn = get_db_connection()
        conn.close()
        return jsonify({"message": "Database connection successful!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
