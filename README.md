# 📊 Employee Insights – HR Analytics

Employee Insights is an HR Management and Analytics application built using Python, Streamlit, and Microsoft SQL Server.

The application allows organizations to manage employee information, departments, attendance, and leave requests through an interactive web interface. It also provides an HR analytics dashboard with useful employee and organizational insights.

---

## 🚀 Features

### 👨‍💼 Employee Management
- Add new employees
- View employee details
- Edit employee information
- Delete employees
- Search employees by first name or last name
- View employee statistics

### 🏢 Department Management
- Add departments
- View department details
- Edit departments
- Delete departments
- Search departments
- Prevent duplicate department names
- Prevent deletion of departments that have assigned employees

### 📅 Attendance Management
- Add attendance records
- View attendance records
- Edit attendance records
- Delete attendance records
- Search attendance by employee name
- Track check-in and check-out times
- Calculate working hours
- Track attendance status

### 📝 Leave Management
- Add leave requests
- View leave requests
- Edit leave requests
- Delete leave requests
- Track leave type
- Track leave start and end dates
- Manage leave status
- Search leave records

### 📊 HR Analytics Dashboard
- Total employee count
- Total department count
- Average salary
- Highest salary
- Department-wise employee count
- Average salary by department
- Employees by city
- Employee status distribution
- Gender distribution
- Leave status summary
- Attendance status summary

### 🧪 Testing
The project includes automated tests using `pytest`.

Current test result:

**34 tests passed successfully.**

---

## 🛠️ Technologies Used

### Frontend
- Streamlit
- HTML
- CSS

### Backend
- Python
- Object-Oriented Programming
- Service-based architecture

### Database
- Microsoft SQL Server
- SQL
- pyodbc

### Data & Visualization
- Pandas
- Plotly

### Testing
- Pytest

### Development Tools
- Visual Studio Code
- Git
- GitHub

---

## 📁 Project Structure

```text
Employee-Insights-HR-Analytics/
│
├── database/
│   ├── procedures.sql
│   ├── sample_data.sql
│   ├── schema.sql
│   └── views.sql
│
├── models/
│   ├── attendance.py
│   ├── department.py
│   ├── employee.py
│   └── leave_request.py
│
├── pages/
│   ├── 1_Employee_Management.py
│   ├── 2_Department_Management.py
│   ├── 3_Attendance.py
│   └── 4_Leave_Management.py
│
├── screenshots/
│   ├── dashboard.png
│   └── employees.png
│
├── services/
│   ├── analytics_service.py
│   ├── attendance_service.py
│   ├── department_service.py
│   ├── employee_service.py
│   └── leave_service.py
│
├── tests/
│   ├── test_attendance.py
│   ├── test_database.py
│   ├── test_department.py
│   ├── test_department_services.py
│   ├── test_employee.py
│   ├── test_employee_services.py
│   └── test_leave.py
│
├── app.py
├── config.py
├── database.py
├── requirements.txt
├── .gitignore
└── README.md