# 📚 Attendance Management System

A modern and responsive Attendance Management System built with Python Flask, SQLite, HTML, CSS, and JavaScript. This application helps manage students and track daily attendance efficiently through an intuitive dashboard interface.

## ✨ Features

- 👨‍🎓 Add Students with Unique Roll Numbers
- ✅ Mark Daily Attendance (Present/Absent)
- 📅 Store Attendance Date-wise
- 📋 View Complete Attendance Records
- 📊 Attendance Reports & Percentage Calculation
- 🎨 Modern Glassmorphism UI
- 🌙 Dark Theme Design
- ⚡ Smooth Animations
- 📱 Fully Responsive Layout
- 🔒 Duplicate Attendance Prevention
- 🗄️ SQLite Database Integration

---

## 🛠️ Technologies Used

- Python
- Flask
- SQLite
- HTML5
- CSS3
- JavaScript

---

## 📂 Project Structure

```text
attendance-management/
│
├── app.py
├── attendance.db
│
├── templates/
│   ├── dashboard.html
│   ├── students.html
│   ├── attendance.html
│   ├── records.html
│   └── reports.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
└── README.md
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/attendance-management.git
```

### Move to Project Folder

```bash
cd attendance-management
```

### Install Dependencies

```bash
pip install flask
```

### Run Application

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

---

## 📸 Modules

### 🏠 Dashboard
- Total Students
- Total Present
- Total Absent

### 👨‍🎓 Students
- Add New Student
- Unique Roll Number Validation
- Student List

### ✅ Attendance
- Select Student
- Select Date
- Mark Present / Absent
- Duplicate Entry Protection

### 📋 Records
- View Complete Attendance History
- Date-wise Attendance Records

### 📊 Reports
- Total Classes
- Present Count
- Attendance Percentage

---

## 🗄️ Database Schema

### Students Table

```sql
CREATE TABLE students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    roll_no INTEGER UNIQUE,
    name TEXT NOT NULL
);
```

### Attendance Table

```sql
CREATE TABLE attendance(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    attendance_date TEXT,
    status TEXT,
    FOREIGN KEY(student_id) REFERENCES students(id)
);
```

---

## 🎯 Future Enhancements

- Login System
- Admin Panel
- Search & Filter
- Edit Attendance
- Delete Attendance
- Export to Excel
- Export to PDF
- Attendance Charts
- QR Code Attendance
- Cloud Database Support

---

**screenshot**
<img width="1918" height="969" alt="image" src="https://github.com/user-attachments/assets/0f576532-1b55-4a53-8bd8-c58ca8d9230e" />


## 👨‍💻 Author

**Yash Gaidhane**

Python Developer | Flask Developer | Web Development Enthusiast

---

## ⭐ Support

If you like this project, please give it a star on GitHub.

Happy Coding! 🚀
