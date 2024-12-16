
# app/app.py
from flask import Flask, render_template, request
import pg8000
import os

app = Flask(__name__, template_folder='../templates') #Corrected template folder path

#Database URL from environment variables
db_url = os.environ.get("DATABASE_URL")

# Home route to get user input for level
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        level = request.form["level"]
        return render_template("timetable.html", level=level)
    return render_template("index.html")

# Timetable route to fetch timetable data based on the level
@app.route("/timetable", methods=["GET"])
def timetable():
    level = request.args.get("level")
    
    try:
        # Connect to PostgreSQL using pg8000 (using DATABASE_URL)
        conn = pg8000.connect(dsn=db_url) # Use DSN for connection
        cur = conn.cursor()
    
        # Fetch timetable for the selected level
        query = f"SELECT * FROM Timetable WHERE level = {level};"
        cur.execute(query)
        rows = cur.fetchall()
        
        message = "No data found for this level." if not rows else None
        return render_template("timetable.html", data=rows, message=message)
    except Exception as e:
        return f"Database error: {str(e)}", 500 #Handle exceptions
    finally:
        if conn:
            conn.close()

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0') #Listen on all interfaces for docker