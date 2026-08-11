from services.leave_service import LeaveService
from models.leave_request import LeaveRequest
from datetime import date


def test_get_all_leaves():

    service = LeaveService()
    leaves = service.get_all_leaves()

    assert leaves is not None


def test_get_leave_by_id():

    service = LeaveService()
    leaves = service.get_all_leaves()

    if len(leaves) > 0:

        leave_id = leaves[0].LeaveID
        leave = service.get_leave_by_id(leave_id)

        assert leave is not None
        assert leave.LeaveID == leave_id


def test_leave_status():

    service = LeaveService()
    leaves = service.Leave_Status()

    assert leaves is not None


def test_leave_crud():

    service = LeaveService()

    # ADD 

    leave = LeaveRequest(
        1002,
        "Casual Leave",
        date(2026, 8, 11),
        date(2026, 8, 12),
        "Personal work",
        "Pending"
    )

    result = service.add_leave(leave)

    assert result is True

    # Find inserted leave
    leaves = service.get_all_leaves()

    assert leaves is not None
    assert len(leaves) > 0

    leave_id = None

    for record in leaves:

        if (
            record.EmployeeID == 1002
            and record.StartDate == date(2026, 8, 11)
            and record.EndDate == date(2026, 8, 12)
        ):
            leave_id = record.LeaveID
            break

    assert leave_id is not None

    # GET 

    fetched = service.get_leave_by_id(
        leave_id
    )

    assert fetched is not None
    assert fetched.LeaveID == leave_id

    # UPDATE 

    updated_leave = LeaveRequest(
        1002,
        "Sick Leave",
        date(2026, 8, 11),
        date(2026, 8, 12),
        "Not feeling well",
        "Approved",
        leave_id
    )

    result = service.update_leave(
        updated_leave
    )

    assert result is True

    updated = service.get_leave_by_id(
        leave_id
    )

    assert updated is not None
    assert updated.EmployeeID == 1002
    assert updated.LeaveType == "Sick Leave"
    assert updated.Status == "Approved"

    # DELETE 

    result = service.delete_leave(
        leave_id
    )

    assert result is True

    # VERIFY DELETE 

    deleted = service.get_leave_by_id(
        leave_id
    )

    assert deleted is None

def test_get_leave_by_invalid_id():
    service = LeaveService()
    leave = service.get_leave_by_id(999999)

    assert leave is None

def test_leave_status_not_empty():
    service = LeaveService()
    result = service.Leave_Status()

    assert result is not None

    