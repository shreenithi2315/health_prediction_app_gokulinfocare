import sqlite3
db_file = "health_records.db"
def connect():
    conn = sqlite3.connect(db_file)
    return conn
def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            dob TEXT NOT NULL,
            email TEXT NOT NULL,
            glucose REAL,
                   haemoglobin REAL,
                   cholesterol REAL,
                  remarks TEXT ) """)
    conn.commit()
    conn.close() 


create_table()

def add_patient(full_name,dob, email, glucose, haemoglobin, cholesterol, remarks):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO patients (full_name, dob, email, glucose, haemoglobin, cholesterol, remarks)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (full_name, dob, email, glucose, haemoglobin, cholesterol, remarks))
    conn.commit()
    conn.close()

def get_all_patients():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_patient(patient_id, full_name, dob, email, glucose, haemoglobin, cholesterol, remarks):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE patients
        SET full_name=?, dob=?, email=?, glucose=?, haemoglobin=?, cholesterol=?, remarks=?
        WHERE id=?
    """, (full_name, dob, email, glucose, haemoglobin, cholesterol, remarks, patient_id))
    conn.commit()
    conn.close()

def delete_patient(patient_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM patients WHERE id=?", (patient_id,))
    conn.commit()
    conn.close()
