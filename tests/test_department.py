from services.department_service import DepartmentService
from models.department import Departments


def test_get_all_departments():

    service = DepartmentService()
    departments = service.get_all_departments()

    assert departments is not None
    assert len(departments) > 0


def test_get_department_by_id():

    service = DepartmentService()
    department = service.get_department_by_id(1)

    assert department is not None
    assert department.DepartmentID == 1


def test_search_department():

    service = DepartmentService()
    departments = service.search_department("HR")

    assert departments is not None


def test_get_department_by_name():

    service = DepartmentService()
    department = service.get_department_by_name("HR")

    if department is not None:
        assert department.DepartmentName == "HR"


def test_department_has_employee():

    service = DepartmentService()
    count = service.department_has_employee(1)

    assert count >= 0


def test_get_department_count():

    service = DepartmentService()
    count = service.get_department_count()

    assert count[0] >= 0


def test_department_wise_count():

    service = DepartmentService()
    departments = service.department_wise_count()

    assert departments is not None


def test_department_crud():

    service = DepartmentService()

    #ADD 

    department = Departments(
        "Test Department",
        "Test Manager",
        "Chennai",
        100000
    )

    result = service.add_department(department)

    assert result is True

    # Find the inserted department
    inserted = service.get_department_by_name(
        "Test Department"
    )

    assert inserted is not None

    department_id = inserted.DepartmentID

    assert inserted.DepartmentName == "Test Department"

    #GET 

    fetched = service.get_department_by_id(
        department_id
    )

    assert fetched is not None
    assert fetched.DepartmentID == department_id

    #UPDATE 
    updated_department = Departments(
        "Updated Test Department",
        "Updated Manager",
        "Bangalore",
        200000,
        department_id
    )

    result = service.update_department(
        updated_department
    )

    assert result is True

    updated = service.get_department_by_id(
        department_id
    )

    assert updated is not None
    assert updated.DepartmentName == "Updated Test Department"
    assert updated.ManagerName == "Updated Manager"
    assert updated.Location == "Bangalore"
    assert float(updated.Budget) == 200000

    #DELETE 

    result = service.delete_department(
        department_id
    )

    assert result is True

    # VERIFY DELETE 

    deleted = service.get_department_by_id(
        department_id
    )

    assert deleted is None

def test_get_department_by_invalid_id():
    service = DepartmentService()

    department = service.get_department_by_id(999999)

    assert department is None

def test_duplicate_department():
    service = DepartmentService()

    department = Departments(
        "HR",
        "Test Manager",
        "Chennai",
        500000
    )

    existing = service.get_department_by_name("HR")

    assert existing is not None