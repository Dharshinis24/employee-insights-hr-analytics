class Departments:

    def __init__(self,DepartmentName, ManagerName, Location, Budget,DepartmentID=None):
        self.DepartmentID = DepartmentID
        self.DepartmentName = DepartmentName
        self.ManagerName = ManagerName
        self.Location = Location
        self.Budget = Budget