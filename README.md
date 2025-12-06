# UniTrack - University Attendance Management System

## 📋 Project Overview

**UniTrack** is a comprehensive web-based attendance management system designed for educational institutions. It streamlines the process of tracking student attendance, managing medical absences, and generating attendance reports. The system is built with Flask and SQLAlchemy, providing a secure, scalable solution for universities and colleges.

## 🎯 Purpose

The primary purpose of UniTrack is to:
- **Automate attendance tracking** - Replace manual attendance sheets with a digital system
- **Simplify absence management** - Allow students to submit medical reports for absences
- **Generate insights** - Provide administrators with attendance statistics and reports
- **Ensure accountability** - Track attendance patterns and maintain comprehensive records
- **Improve efficiency** - Reduce administrative workload through automated processes

## ✨ Key Features

### 🔐 User Roles & Authentication
- **Administrator** - Full system control (manage users, approve medical reports, export data)
- **Admin/Lecturer** - Mark attendance, view records, manage students in their courses
- **Student** - View personal attendance, upload medical reports, track attendance percentage

### 📊 Attendance Management
- **Individual Attendance Marking** - Mark students present/absent one by one
- **Bulk Attendance Marking by Subject** - Select a course and date, then mark all enrolled students at once
- **CSV File Upload** - Import attendance records in bulk using CSV files
- **Attendance History** - View complete attendance records with filters
- **Monthly Attendance Statistics** - Visual progress bars showing monthly attendance percentage

### 🏥 Medical Report System
- **Student Report Submission** - Upload medical documents (PDF, JPG, PNG, DOC, DOCX) for absences
- **Admin Approval/Rejection** - Review submitted medical reports and approve/reject them
- **Status Tracking** - Track pending and approved medical reports
- **Medical Status** - Approved medical absences are displayed as "Medical" instead of "Absent"

### 📈 Reporting & Analytics
- **Attendance Export** - Export attendance records as CSV files
- **Monthly Statistics** - Calculate and display monthly attendance percentages
- **Color-Coded Indicators** - Visual feedback on attendance levels (green ≥75%, yellow ≥50%, red <50%)
- **Student Enrollment Management** - Track which students are enrolled in which courses

### 👥 User Management
- **Administrator Only** - Add and remove users from the system
- **Role-Based Access Control** - Different permissions for different user roles
- **Password Management** - Secure password hashing with werkzeug
- **Forgot Password Feature** - Self-service password reset for users
- **Profile Editing** - Users can update their name and password

## 🛠️ Technology Stack

- **Backend Framework**: Flask 3.0.0
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: Bootstrap 5, HTML5, Jinja2 Templates
- **Authentication**: Werkzeug (Password Hashing & Security)
- **File Handling**: Secure file uploads with size limits
- **Python Version**: 3.x

## 📦 Project Structure

```
unitrack/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── instance/
│   └── database.db                 # SQLite database
├── static/                         # Static files (CSS, JS, images)
├── templates/                      # HTML templates
│   ├── base.html                   # Base template with navbar
│   ├── login.html                  # Login page
│   ├── student_dash.html           # Student dashboard with attendance stats
│   ├── admin_dash.html             # Admin dashboard
│   ├── mark_attendance_bulk.html   # Bulk attendance marking
│   ├── bulk_upload.html            # CSV upload page
│   ├── upload_medical.html         # Medical report upload
│   ├── profile.html                # User profile editing
│   ├── forgot_password.html        # Password reset
│   └── ...
└── uploads/
    └── medical_reports/            # Uploaded medical documents
```

## 📡 GitHub Pages Deployment

- **Note:** GitHub Pages only serves static sites. This repository contains a Flask app (server-side logic, database, sessions, and file uploads) which cannot run on GitHub Pages. The provided workflow will export a small set of public pages (login, forgot password, and the root) to static HTML and deploy them to GitHub Pages.
- **Limitations:** Dynamic features (authentication, database reads/writes, file uploads, admin actions) will NOT work on GitHub Pages because they require a running Flask server.

### How it works
- A script `generate_static.py` uses Flask's test client to fetch a few public routes and write them to `build/` as static HTML.
- A GitHub Actions workflow (`.github/workflows/deploy.yml`) runs on each push to `main`, generates the static files and deploys them to GitHub Pages.

### How to enable
1. Push this repository to GitHub (if not already pushed).
2. On GitHub, go to the repository Settings → Pages (or the Pages sidebar) and ensure the site is set to use GitHub Pages from the GitHub Actions deployment (this is automatic once the workflow runs successfully).
3. Push to `main` to trigger the workflow. After the workflow succeeds, your static site will be published by GitHub Pages.

### To host the full dynamic app instead
- Deploy the Flask app to a service that supports Python apps (e.g., Render.com, Railway, Fly, or a VPS). Then either:
   - Use your service URL directly, or
   - Host only static frontend on GitHub Pages and point client requests to your deployed backend.

If you'd like, I can:
- Configure a more complete static export (freeze more routes and add URL generators), or
- Add a deployment config to host the full Flask app on a platform like Render or Railway.

## 🖥️ Desktop App (Local wrapper)

You can run UniTrack as a simple desktop application. The approach provided here runs the Flask app locally and opens it inside a native window using `pywebview`. This gives a desktop-like experience while the Flask server runs in the background on the local machine.

### How to run locally as a desktop app
1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Run the desktop launcher:
```bash
python desktop.py
```
This will:
- Initialize the local SQLite DB (if empty)
- Start the Flask server on `http://127.0.0.1:5000`
- Open a native window (if `pywebview` is available and a display is present) or your default browser.

### Packaging as a single executable
You can bundle the app into a single executable using `PyInstaller`.

1. Install `pyinstaller`:
```bash
pip install pyinstaller
```
2. Build the executable (example for Linux/macOS/Windows):
```bash
pyinstaller --onefile --add-data "templates:templates" --add-data "static:static" --add-data "instance:instance" desktop.py
```
- On Windows, replace colons in `--add-data` with semicolons: `templates;templates`.
- The produced executable will be in `dist/desktop`.

Notes:
- The packaged app will still run a local Flask server and open a window. The database remains local (SQLite in `instance/database.db`).
- `pywebview` requires additional system libraries for GUI backends on some platforms (GTK/Qt on Linux). If those aren't available, the launcher falls back to opening the default browser.

If you want, I can:
- Add a `pyinstaller` spec file and a GitHub Action to produce releases, or
- Switch the launcher to use `waitress` as the WSGI server for better production behaviour inside the bundle.

## 🗄️ Database Models

### User
- Stores user information (index_number, password, role, name)
- Roles: `administrator`, `admin`, `student`

### Attendance
- Records attendance entries (student_index, course_code, date, status)
- Status: `Present`, `Absent`, `Medical`

### StudentCourse
- Tracks student enrollment in courses

### MedicalReport
- Stores medical report submissions (student_index, document_path, approval_status)

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/DulsaraPrasad/unitrack.git
   cd unitrack
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Open your browser and navigate to `http://localhost:5000`

## 👤 Test Accounts

### Administrator (Full Access)
- **Username**: `Dulsara`
- **Password**: `Dulsara`
- **Permissions**: Manage users, approve medical reports, export data

### Admins/Lecturers (Attendance Marking)
- **Username**: `dulsara` | **Password**: `4321`
- **Username**: `dilki` | **Password**: `4321`
- **Username**: `hashan` | **Password**: `4321`
- **Permissions**: Mark attendance, view records

### Sample Students
- **Username**: `S1001` - `S1005`
- **Password**: `1234`
- **Permissions**: View attendance, upload medical reports

## 📝 Usage Guide

### For Students
1. **Login** with your student index and password
2. **View Attendance** - Check your attendance records on the dashboard
3. **Check Monthly Stats** - Monitor your monthly attendance percentage
4. **Upload Medical Report** - Submit medical documents for absences
5. **Edit Profile** - Update your name and password from the Profile page

### For Admins/Lecturers
1. **Login** with your admin credentials
2. **Mark Attendance** - Use individual form or bulk marking by subject
3. **Bulk Upload** - Import attendance from CSV files
4. **View Records** - See all attendance records with filters
5. **Manage Medical Reports** - Review and approve student submissions

### For Administrators
1. **Login** with administrator credentials
2. **All Admin Features** - Plus additional capabilities:
3. **User Management** - Add/remove users from the system
4. **Export Data** - Download attendance records as CSV
5. **Approve Medical Reports** - Review and approve medical submissions

## 📊 Features in Detail

### Bulk Attendance Marking
1. Navigate to "Mark by Subject" on the admin dashboard
2. Select a course from the dropdown
3. Select the date
4. All students enrolled in that course will appear
5. Mark each student as Present or Absent
6. Click "Mark Attendance for All" to save

### CSV Bulk Upload
**Required CSV Format:**
```
student_index,date,status
S1001,2024-12-04,Present
S1002,2024-12-04,Absent
S1003,2024-12-05,Present
```

### Monthly Attendance Calculation
- System automatically calculates attendance percentage per month
- Includes Present, Absent, and Medical statuses
- Visual progress bar with color indicators

### Medical Report Workflow
1. **Student** submits medical report for an absence
2. **Admin** reviews the uploaded document
3. **Admin** approves or rejects the submission
4. **System** updates attendance status to "Medical" if approved
5. **Student** sees updated status in their dashboard

## 🔒 Security Features

- **Password Hashing** - Werkzeug secure hashing for all passwords
- **Session Management** - Flask session-based authentication
- **File Validation** - Only allowed file types (PDF, JPG, PNG, DOC, DOCX)
- **File Size Limit** - 16MB maximum file size
- **SQL Injection Protection** - SQLAlchemy ORM prevents SQL injection
- **Role-Based Access Control** - Routes check user roles before granting access

## 🎓 Courses Supported

The system comes pre-configured with the following courses:
- NANO2112 - Mathematics for Nano Science Technology I
- NANO2122 - Fundamentals of Nano-Electronics
- NANO2132 - Digital Electronics
- NANO2142 - Introduction to Software Development
- NANO2151 - Principles of Material Science Engineering
- NANO2162 - Engineering Design & Drawings
- NANO2172 - Physical Chemistry for Nanotechnology
- NANO2182 - Management for Technology
- ETCH2111 - English Language & Communication Skills II
- PDEV2110 - Career Development II

## 📱 Responsive Design

UniTrack is built with Bootstrap 5, ensuring:
- **Mobile-friendly** interface
- **Responsive layouts** that work on all devices
- **Touch-friendly** buttons and controls
- **Fast loading times** with optimized assets

## 🐛 Error Handling

The application includes comprehensive error handling:
- Form validation
- Database constraint checking
- File upload validation
- User-friendly error messages
- Session management
- Exception logging

## 🔄 Data Flow

```
Login → Authentication → Role Check → Dashboard
         ↓
    Student → View Attendance → Upload Medical Report
    Admin → Mark Attendance → Export Data → Approve Medical Reports
    Administrator → Manage Users → Full System Control
```

## 📞 Support & Maintenance

For issues or feature requests:
1. Check the error messages displayed in the application
2. Review the debug information in browser console
3. Check database integrity
4. Verify user roles and permissions

## 📄 License

This project is developed for university attendance management.

## 👨‍💻 Developer

**Project Owner**: DulsaraPrasad

---

## 🎯 Future Enhancements

Potential features for future versions:
- Email notifications for attendance alerts
- SMS reminders for low attendance
- Biometric attendance integration
- Mobile app for attendance tracking
- Advanced analytics and reporting
- API endpoints for third-party integration
- Student performance correlation with attendance
- QR code-based attendance marking
- Automated alerts for attendance thresholds

---

**Last Updated**: December 5, 2025
**Version**: 1.0.0