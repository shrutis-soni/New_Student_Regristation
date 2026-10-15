import os
from dotenv import load_dotenv
import google.generativeai as genai
import mysql.connector as mysql

load_dotenv()  # Load environment variables from .env


#==================== Connect to MySQL ====================#
def connect_db():
    return mysql.connect(
        host="localhost",
        user="root",
        password="Shruti1818",
        database="PROJECT"
    )


#==================== Format Query Output (if rows returned) ====================#
def format_dynamic_rows(rows, column_names):
    result = ""
    for row in rows:
        result += "\n".join([f"{col}: {val}" for col, val in zip(column_names, row)]) + "\n\n"
    return result.strip()


#==================== Main AI Query Handler (Full SQL Access) ====================#
def GenerativeAI(query):
    apikey = os.getenv("AIzaSyA6gyolFDgLD2RYUzW9KxutrUMz5P5BIA8")
    system_prompt = """
You are a database assistant with full SQL access to a MySQL database named 'PROJECT' with a table 'admin'.
The 'admin' table has these columns: registration_no, name, dob, gender, class, religion, skill, father, mother, father_job, mother_job.
Generate an appropriate SQL command (SELECT, INSERT, UPDATE, DELETE, CREATE, etc.) based on the user's natural language.
Return ONLY the raw SQL statement without code fences or explanation.
"""

    # Configure Gemini
    genai.configure(api_key="AIzaSyA6gyolFDgLD2RYUzW9KxutrUMz5P5BIA8")
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        system_instruction=system_prompt
    )

    # Ask Gemini to generate the SQL query
    result = model.generate_content(f"Convert this to a SQL query: {query}")
    sql = result.text.strip().strip("sql").strip("")

    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(sql)

        # If it's a SELECT query, fetch and return results
        if sql.strip().lower().startswith("select"):
            rows = cursor.fetchall()
            if not rows:
                return "No matching records found."
            column_names = [desc[0] for desc in cursor.description]
            return format_dynamic_rows(rows, column_names)

        # If it's not SELECT, commit changes
        conn.commit()
        return f"SQL command executed successfully:\n{sql}"

    except Exception as e:
        return f"SQL execution error: {str(e)}"

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass