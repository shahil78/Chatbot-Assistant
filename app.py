from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('company_db_sql')
    conn.row_factory = sqlite3.Row
    return conn

# Parse user query and generate SQL
def parse_query(query):
    query = query.lower()
    if "show me all employees in the" in query:
        department = query.split("department")[0].split("the ")[-1].strip()
        return f"SELECT * FROM Employees WHERE Department = '{department.capitalize()}'"
    elif "who is the manager of the" in query:
        department = query.split("department")[0].split("the ")[-1].strip()
        return f"SELECT Manager FROM Departments WHERE Name = '{department.capitalize()}'"
    elif "list all employees hired after" in query:
        date = query.split("after")[-1].strip()
        return f"SELECT * FROM Employees WHERE Hire_date > '{date}'"
    elif "what is the total salary expense for the" in query:
        department = query.split("department")[0].split("the ")[-1].strip()
        return f"SELECT SUM(Salary) AS Total_Salary FROM Employees WHERE Department = '{department.capitalize()}'"
    else:
        return None

# Handle user queries
@app.route('/query', methods=['POST'])
def handle_query():
    user_query = request.json.get('query')
    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    sql_query = parse_query(user_query)
    if not sql_query:
        return jsonify({"error": "Unsupported query"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(sql_query)
        result = cursor.fetchall()
        if not result:
            return jsonify({"response": "No results found"}), 200
        return jsonify({"response": [dict(row) for row in result]}), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# Home route
@app.route('/')
def home():
    return "Welcome to the Company Chat Assistant!"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)