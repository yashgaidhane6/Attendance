from flask import Flask, render_template, request, redirect, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "attendance_secret"


# ================= DATABASE =================

def init_db():
    conn = sqlite3.connect("attendance.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        roll_no INTEGER UNIQUE,
        name TEXT NOT NULL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS attendance(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        attendance_date TEXT,
        status TEXT,
        FOREIGN KEY(student_id) REFERENCES students(id)
    )
    """)

    conn.commit()
    conn.close()

init_db()


# ================= DASHBOARD =================

@app.route("/")
def dashboard():

    conn = sqlite3.connect("attendance.db")
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM students")
    total_students = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM attendance WHERE status='Present'")
    total_present = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM attendance WHERE status='Absent'")
    total_absent = cur.fetchone()[0]

    conn.close()

    return render_template(
        "dashboard.html",
        total_students=total_students,
        total_present=total_present,
        total_absent=total_absent
    )


# ================= STUDENTS =================

@app.route("/students")
def students():

    conn = sqlite3.connect("attendance.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM students ORDER BY roll_no")
    students = cur.fetchall()

    conn.close()

    return render_template(
        "students.html",
        students=students
    )


@app.route("/add_student", methods=["POST"])
def add_student():

    roll_no = request.form["roll_no"]
    name = request.form["name"]

    conn = sqlite3.connect("attendance.db")
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO students (roll_no,name) VALUES (?,?)",
            (roll_no,name)
        )

        conn.commit()
        flash("Student Added Successfully")

    except:
        flash("Roll Number Already Exists")

    conn.close()

    return redirect("/students")


# ================= ATTENDANCE =================

@app.route("/attendance")
def attendance():

    conn = sqlite3.connect("attendance.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT id,roll_no,name FROM students ORDER BY roll_no"
    )

    students = cur.fetchall()

    conn.close()

    return render_template(
        "attendance.html",
        students=students
    )


@app.route("/mark_attendance", methods=["POST"])
def mark_attendance():

    student_id = request.form["student_id"]
    date = request.form["date"]
    status = request.form["status"]

    conn = sqlite3.connect("attendance.db")
    cur = conn.cursor()

    cur.execute("""
    SELECT *
    FROM attendance
    WHERE student_id=?
    AND attendance_date=?
    """,(student_id,date))

    exists = cur.fetchone()

    if exists:

        flash("Attendance already marked.")

    else:

        cur.execute("""
        INSERT INTO attendance
        (student_id,attendance_date,status)
        VALUES (?,?,?)
        """,(student_id,date,status))

        conn.commit()

        flash("Attendance Saved")

    conn.close()

    return redirect("/attendance")


# ================= RECORDS =================

@app.route("/records")
def records():

    conn = sqlite3.connect("attendance.db")
    cur = conn.cursor()

    cur.execute("""
    SELECT
    students.roll_no,
    students.name,
    attendance.attendance_date,
    attendance.status
    FROM attendance
    JOIN students
    ON attendance.student_id = students.id
    ORDER BY attendance.attendance_date DESC
    """)

    records = cur.fetchall()

    conn.close()

    return render_template(
        "records.html",
        records=records
    )


# ================= REPORTS =================

@app.route("/reports")
def reports():

    conn = sqlite3.connect("attendance.db")
    cur = conn.cursor()

    cur.execute("""
    SELECT
    students.roll_no,
    students.name,
    COUNT(attendance.id),
    SUM(
        CASE
        WHEN attendance.status='Present'
        THEN 1
        ELSE 0
        END
    )
    FROM students
    LEFT JOIN attendance
    ON students.id = attendance.student_id
    GROUP BY students.id
    """)

    reports = cur.fetchall()

    conn.close()

    return render_template(
        "reports.html",
        reports=reports
    )


if __name__ == "__main__":
    app.run(debug=True)