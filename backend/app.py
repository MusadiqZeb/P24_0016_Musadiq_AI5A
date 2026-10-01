from flask import Flask, jsonify, request
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return connection

# 1. Create a Research Opportunity[cite: 2]
@app.route('/api/opportunities', methods=['POST'])
def create_opportunity():
    try:
        data = request.get_json()
        
        # Basic validation to trigger a 400 Bad Request if data is missing[cite: 3]
        if not data or not data.get('title') or not data.get('description'):
            return jsonify({"error": "Missing required fields"}), 400
            
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # The SQL command to insert data[cite: 2]
        sql = """INSERT INTO opportunities 
                 (title, description, research_area, faculty_name, department, required_skills, available_positions, application_deadline) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        
        values = (
            data.get('title'), data.get('description'), data.get('research_area'), 
            data.get('faculty_name'), data.get('department'), data.get('required_skills'), 
            data.get('available_positions'), data.get('application_deadline')
        )
        
        cursor.execute(sql, values)
        conn.commit() # Permanently saves to the database
        new_id = cursor.lastrowid 
        
        cursor.close()
        conn.close()
        
        # Returns a 201 Created status code upon success[cite: 3]
        return jsonify({"message": "Opportunity created successfully", "id": new_id}), 201
        
    except Exception as e:
        # Returns a 500 Internal Server Error if something breaks[cite: 3]
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)