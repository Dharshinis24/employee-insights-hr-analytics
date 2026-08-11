from models.employee import Employee
from datetime import date

def test_employee_creation():
    employee = Employee(
        "Ananya",
        "Iyer",
        "Female",
        date(1999, 5, 20),
        "ananya.iyer@company.com",
        "9876500002",
        "Chennai",
        1,
        "Python Developer",
        70000.00,
        date(2021, 4, 10),
        4,
        "Active"
    )
    assert employee.EmployeeID is None
    assert employee.FirstName == "Ananya"
    assert employee.LastName == "Iyer"
    assert employee.Gender == "Female"
    assert employee.DateOfBirth == date(1999, 5, 20)
    assert employee.Email == "ananya.iyer@company.com"
    assert employee.Phone == "9876500002"
    assert employee.City ==  "Chennai"
    assert employee.DepartmentID == 1
    assert employee.JobTitle == "Python Developer"
    assert employee.Salary ==  70000.00
    assert employee.JoiningDate == date(2021, 4, 10)
    assert employee.ExperienceYears == 4
    assert employee.Status == "Active"
