import mysql.connector as mysql

def create_db():
    conn = mysql.connect(
        host = "localhost",
        user = 'root',
        password = "Shruti1818"
    )

    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS PROJECT")
    cursor.close()
    conn.close()

def create_table():
    conn = mysql.connect(
        host = "localhost",
        user = "root",
        password = "Shruti1818",
        database = "PROJECT"
    )

    cursor = conn.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS admin (registration_no int primary key, name varchar(20), dob varchar(20), gender varchar(20), class varchar(20), religion varchar(20), skill varchar(20), father_name varchar(20), mother_name varchar(20), father_occupation varchar(20), mother_occupation varchar(20))
"""

    cursor.execute(query)
    conn.close()
    cursor.close()
    print("done")    
create_db()
create_table()
