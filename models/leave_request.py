class LeaveRequest:

    def __init__(self,EmployeeID,LeaveType,StartDate,EndDate,Reason,Status,LeaveID=None):
        self.LeaveID = LeaveID
        self.EmployeeID = EmployeeID
        self.LeaveType = LeaveType
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.Reason = Reason
        self.Status = Status