from services.attendance_service import AttendanceService
from models.attendance import Attendance
from datetime import date, datetime


def test_get_all_attendance():

    service = AttendanceService()
    attendance = service.get_all_attendance()

    assert attendance is not None


def test_get_attendance_by_id():

    service = AttendanceService()
    attendance = service.get_attendance_by_id(2)

    assert attendance is not None
    assert attendance.AttendanceID == 2


def test_search_by_employee_name():

    service = AttendanceService()
    attendance = service.search_by_EmployeeName("Rohan")

    assert attendance is not None


def test_attendance_status():

    service = AttendanceService()
    attendance = service.attendance_status()

    assert attendance is not None


def test_attendance_crud():

    service = AttendanceService()

    #ADD

    attendance = Attendance(
        1002,
        date(2026, 8, 10),
        datetime(2026, 8, 10, 9, 0),
        datetime(2026, 8, 10, 17, 0),
        "Present",
        8.0
    )

    result = service.add_attendance(attendance)

    assert result is True

    # Find inserted attendance
    records = service.search_by_EmployeeName("Ananya")

    assert records is not None
    assert len(records) > 0

    # Find the record with our date
    attendance_id = None

    for record in records:
        if record.AttendanceDate == date(2026, 8, 10):
            attendance_id = record.AttendanceID
            break

    assert attendance_id is not None

    #GET 

    fetched = service.get_attendance_by_id(attendance_id)

    assert fetched is not None
    assert fetched.AttendanceID == attendance_id

    #UPDATE 

    updated_attendance = Attendance(
        1002,
        date(2026, 8, 10),
        datetime(2026, 8, 10, 10, 0),
        datetime(2026, 8, 10, 18, 0),
        "Present",
        8.0,
        attendance_id
    )

    result = service.update_attendance(
        updated_attendance
    )

    assert result is True

    updated = service.get_attendance_by_id(
        attendance_id
    )

    assert updated is not None
    assert updated.EmployeeID == 1002
    assert updated.Status == "Present"

    #DELETE 
    result = service.delete_attendance(
        attendance_id
    )

    assert result is True

    #VERIFY DELETE 

    deleted = service.get_attendance_by_id(
        attendance_id
    )

    assert deleted is None

def test_get_attendance_by_invalid_id():
    service = AttendanceService()
    attendance = service.get_attendance_by_id(999999)

    assert attendance is None

def test_search_attendance_no_result():
    service = AttendanceService()
    attendance = service.search_by_EmployeeName("XYZNOTFOUND")

    assert len(attendance) == 0