from services.employee_service import EmployeeService
from models.employee import Employee
from datetime import date


def test_get_all_employees():

    service = EmployeeService()
    employees = service.get_all_employees()

    assert employees is not None
    assert isinstance(employees, list)


def test_get_employee_by_id():

    service = EmployeeService()
    employee = service.get_employee_by_id(1002)

    assert employee is not None
    assert employee.EmployeeID == 1002


def test_get_employee_count():

    service = EmployeeService()
    count = service.get_employee_count()

    assert count >= 0


def test_get_average_salary():

    service = EmployeeService()
    average_salary = service.get_average_salary()

    assert average_salary is not None
    assert average_salary > 0


def test_get_highest_salary():

    service = EmployeeService()
    employee = service.get_highest_salary()

    assert employee is not None
    assert employee.Salary > 0


def test_search_employees():

    service = EmployeeService()
    employees = service.search_employees("Ananya")

    assert employees is not None


def test_employee_crud():

    service = EmployeeService()
    test_employee = Employee(
        "Test",
        "Employee",
        "Male",
        date(1998, 1, 1),
        "test.employee@company.com",
        "9999999999",
        "Chennai",
        1,
        "Test Developer",
        40000,
        date(2025, 1, 1),
        1,
        "Active"
    )

    # ADD
    result = service.add_employee(test_employee)
    assert result is True

    # Find the newly added employee
    employees = service.search_employees("Test")
    assert len(employees) > 0

    employee_id = employees[0].EmployeeID

    # GET
    employee = service.get_employee_by_id(employee_id)

    assert employee is not None
    assert employee.FirstName == "Test"
    assert employee.LastName == "Employee"

    # UPDATE
    updated_employee = Employee(
        "Updated",
        "Employee",
        "Male",
        date(1998, 1, 1),
        "test.employee@company.com",
        "9999999999",
        "Chennai",
        1,
        "Senior Test Developer",
        50000,
        date(2025, 1, 1),
        2,
        "Active",
        employee_id
    )

    service.update_employee(updated_employee)

    employee = service.get_employee_by_id(employee_id)

    assert employee.FirstName == "Updated"
    assert employee.JobTitle == "Senior Test Developer"
    assert employee.Salary == 50000

    # SEARCH
    search_result = service.search_employees("Updated")

    assert len(search_result) > 0

    # DELETE
    service.delete_employee(employee_id)

    # VERIFY DELETE
    deleted_employee = service.get_employee_by_id(employee_id)

    assert deleted_employee is None

def test_get_employee_by_invalid_id():
    service = EmployeeService()
    employee = service.get_employee_by_id(999999)

    assert employee is None

def test_search_employee_no_result():
    service = EmployeeService()
    employees = service.search_employees("XYZNOTFOUND")

    assert len(employees) == 0