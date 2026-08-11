class Attendance:

    def __init__(self,EmployeeID,AttendanceDate,CheckIn,CheckOut,Status,WorkingHours,AttendanceID=None):
        self.AttendanceID = AttendanceID
        self.EmployeeID = EmployeeID
        self.AttendanceDate = AttendanceDate
        self.CheckIn = CheckIn
        self.CheckOut = CheckOut
        self.Status = Status
        self.WorkingHours = WorkingHours
        