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
        if not data or not data.get('title') or not data.get('description'):
            return jsonify({"error": "Missing required fields"}), 400
            
        conn = get_db_connection()
        cursor = conn.cursor()
        
        sql = """INSERT INTO opportunities 
                 (title, description, research_area, faculty_name, department, required_skills, available_positions, application_deadline) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (data.get('title'), data.get('description'), data.get('research_area'), 
                  data.get('faculty_name'), data.get('department'), data.get('required_skills'), 
                  data.get('available_positions'), data.get('application_deadline'))
        
        cursor.execute(sql, values)
        conn.commit()
        new_id = cursor.lastrowid 
        
        cursor.close()
        conn.close()
        return jsonify({"message": "Opportunity created successfully", "id": new_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 2. Retrieve All Research Opportunities[cite: 2]
@app.route('/api/opportunities', methods=['GET'])
def get_all_opportunities():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True) # dictionary=True makes it output JSON formatting easily
        cursor.execute("SELECT * FROM opportunities")
        opportunities = cursor.fetchall()
        
        cursor.close()
        conn.close()
        return jsonify(opportunities), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 3. Retrieve One Research Opportunity[cite: 2]
@app.route('/api/opportunities/<int:id>', methods=['GET'])
def get_opportunity(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM opportunities WHERE id = %s", (id,))
        opportunity = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        if opportunity:
            return jsonify(opportunity), 200
        return jsonify({"error": "Opportunity not found"}), 404 # 404 error required by assignment[cite: 3]
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 4. Update a Research Opportunity[cite: 2]
@app.route('/api/opportunities/<int:id>', methods=['PUT'])
def update_opportunity(id):
    try:
        data = request.get_json()
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # We only update the status for simplicity in this example, but you can expand it
        sql = "UPDATE opportunities SET status = %s WHERE id = %s"
        cursor.execute(sql, (data.get('status', 'Open'), id))
        conn.commit()
        
        cursor.close()
        conn.close()
        return jsonify({"message": "Opportunity updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 5. Delete a Research Opportunity[cite: 2]
@app.route('/api/opportunities/<int:id>', methods=['DELETE'])
def delete_opportunity(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM opportunities WHERE id = %s", (id,))
        conn.commit()
        
        cursor.close()
        conn.close()
        return jsonify({"message": "Opportunity deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
