from database import DBConnection
class DepartmentService:

    def __init__(self):
        db = DBConnection()
        self.conn = db.get_connection()
        self.cursor = self.conn.cursor()
    def get_all_departments(self):
        self.cursor.execute("""
        select DepartmentID, DepartmentName, ManagerName, Location, Budget
        from Departments
        """)
        staffs = self.cursor.fetchall()
        return staffs

    def add_department(self,department):
        self.cursor.execute("""
        Insert into Departments(DepartmentName, ManagerName, Location, Budget)
        values(?,?,?,?)
        """,(department.DepartmentName,department.ManagerName,department.Location,department.Budget))
        self.conn.commit()
        return True
    
    def update_department(self,department):
        self.cursor.execute("""
        update Departments 
        set DepartmentName = ?, ManagerName = ?, Location = ?, Budget = ?
        where DepartmentID = ?
        """,(department.DepartmentName,department.ManagerName,department.Location,department.Budget,department.DepartmentID))
        self.conn.commit()
        return True

    def delete_department(self,DepartmentID):
        self.cursor.execute("""
        delete from Departments
        where DepartmentID = ?
        """,(DepartmentID,))
        self.conn.commit()
        return True

    def get_department_by_id(self,DepartmentID):
        self.cursor.execute("""
        select DepartmentID, DepartmentName, ManagerName, Location, Budget from Departments
        where DepartmentID = ?
        """,(DepartmentID,))
        dept = self.cursor.fetchone()
        return dept

    def search_department(self,keyword):
        self.cursor.execute("""
        select DepartmentID, DepartmentName, ManagerName, Location, Budget from Departments
        where DepartmentName Like ?
        """,(f"%{keyword}%",))
        dept = self.cursor.fetchall()
        return dept

    def department_has_employee(self,department_id):
        self.cursor.execute("""
        select count(*) from Employees
        where DepartmentID = ?
        """,(department_id,))
        return self.cursor.fetchone()[0]

    def get_department_count(self):
        self.cursor.execute("""
        select count(*) From Departments
        """)
        depts_count = self.cursor.fetchall()[0]
        return depts_count

    def department_wise_count(self):
        self.cursor.execute("""
        select DepartmentName, count(*) as count 
        from Departments
        group by DepartmentName
        """)
        return self.cursor.fetchall()

    def get_department_by_name(self, department_name):
        self.cursor.execute("""
            SELECT *
            FROM Departments
            WHERE DepartmentName = ?
        """, (department_name,))
        return self.cursor.fetchone()
            