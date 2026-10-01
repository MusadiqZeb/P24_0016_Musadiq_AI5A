# Research Opportunity Portal (Full-Stack API)

**Student Name:** Musadiq Zeb  
**Student ID:** P24-0016  
**Class:** AI5A  
**GitHub Repository:**  https://github.com/MusadiqZeb/P24_0016_Musadiq_AI5A  
**Demo Video:** Included in the `zip` file.  

## Project Overview
This project is a full-stack web application for managing university research opportunities. It features a Python/Flask REST API backend, a MySQL database, and an HTML/Bootstrap frontend.

## Project Structure
* `/backend` - Contains the Flask API (`app.py`), virtual environment, and `requirements.txt`.
* `/frontend` - Contains the visual web interface (`index.html`).
* `setup.sql` - Database schema and table creation script.
* `.env` - (Not included for security) Contains database credentials.
* `Research_Portal_API.postman_collection.json` - Exported API tests.

## 1. Database Setup
1. Ensure MySQL is installed and running.
2. Log into MySQL and run the provided SQL script to build the schema:
   `source /path/to/setup.sql;`
3. Create a `.env` file in the `backend` directory with the following credentials:
   ```
   DB_HOST=localhost
   DB_USER=your_mysql_username
   DB_PASSWORD=your_mysql_password
   DB_NAME=research_portal
   ```

## 2. Backend Setup & Execution
1. Open a terminal and navigate to the `backend` folder.
2. Create and activate a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the Flask server:
   ```bash
   python3 app.py
   ```
   The backend will run at `http://127.0.0.1:5000`.

## 3. Frontend Execution
1. Ensure the Flask backend is currently running.
2. Open a standard file manager and navigate to the `frontend` folder.
3. Double-click `index.html` to open it in any modern web browser (Chrome, Firefox, etc.).
4. Use the interface to create and view research opportunities.

## 4. API Testing (Postman)
To verify the endpoints independently:
1. Open Postman or Bruno.
2. Import the `Research_Portal_API.postman_collection.json` file.
3. Run the collection against `http://127.0.0.1:5000`.
