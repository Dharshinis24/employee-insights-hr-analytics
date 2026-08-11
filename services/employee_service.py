from database import DBConnection

class EmployeeService:

    def __init__(self):
        db = DBConnection()
        self.conn = db.get_connection()
        self.cursor = self.conn.cursor()

    def get_all_employees(self):
        self.cursor.execute(""" 
        select * from Employees
        """)
        rows = self.cursor.fetchall()
        return rows

    def get_employee_by_id(self,employee_id):
        self.cursor.execute(""" 
        select * from Employees
        where EmployeeID = ?
        """,(employee_id,))
        employee = self.cursor.fetchone()
        return employee

    def add_employee(self,employee):
        self.cursor.execute("""
        Insert into Employees (FirstName,LastName,Gender,DateOfBirth,Email,Phone,City,DepartmentID,JobTitle,Salary,JoiningDate,ExperienceYears,Status)
        values(?,?,?,?,?,?,?,?,?,?,?,?,?)
        """,(employee.FirstName,employee.LastName,employee.Gender,employee.DateOfBirth,employee.Email,employee.Phone,employee.City,employee.DepartmentID,employee.JobTitle,employee.Salary,employee.JoiningDate,employee.ExperienceYears,employee.Status))
        self.conn.commit()
        return True
    
    def update_employee(self,employee):
        self.cursor.execute("""
        update Employees
        set FirstName = ?, LastName = ?, Gender = ?, DateOfBirth = ?, Email = ?, Phone = ?, City = ?, DepartmentID = ?, JobTitle = ?, Salary = ?, JoiningDate = ?, ExperienceYears = ?, Status = ?
        where EmployeeID = ?
        """,(employee.FirstName,employee.LastName,employee.Gender,employee.DateOfBirth,employee.Email,employee.Phone,employee.City,employee.DepartmentID,employee.JobTitle,employee.Salary,employee.JoiningDate,employee.ExperienceYears,employee.Status,employee.EmployeeID))
        self.conn.commit()

    def delete_employee(self,employee_id):
        self.cursor.execute("""
        delete from Employees
        where EmployeeID = ?
        """,(employee_id,))
        self.conn.commit()

    def search_employees(self,keyword):
        self.cursor.execute("""
        select * from Employees
        where FirstName Like ? or LastName Like ?
        """,(f"%{keyword}%", f"%{keyword}%"))
        employees = self.cursor.fetchall()
        return employees

    def get_employee_count(self):
        self.cursor.execute("""
        select count(*)
        from Employees
        """)
        count = self.cursor.fetchone()[0]
        return count
    
    def get_average_salary(self):
        self.cursor.execute("""
        select Avg(Salary) as Average_Salary
        from Employees
        """)
        avg_salary = self.cursor.fetchone()[0]
        return avg_salary
    
    def get_highest_salary(self):
        self.cursor.execute("""
        select top 1 EmployeeID,FirstName,LastName,Salary 
        from Employees
        order by Salary desc
        """)
        highest_salary = self.cursor.fetchone()
        return highest_salary

    def get_department_employee_count(self):
        self.cursor.execute("""
        select d.DepartmentName, count(*) as Department_wise_employee_count
        from Employees e
        join Departments d
        on e.DepartmentID = d.DepartmentID
        group by d.DepartmentName
        """)
        dept_employee_count = self.cursor.fetchall()
        return dept_employee_count

    def status_count(self):
        self.cursor.execute("""
        select Status, count(*)
        from Employees
        group by Status
        """)
        return self.cursor.fetchall()

    def gender_distribution(self):
        self.cursor.execute("""
        select Gender, count(*)
        from Employees
        group by Gender
        """)
        return self.cursor.fetchall()

    def dept_wise_avg_salary(self):
        self.cursor.execute("""
        select d.DepartmentName,avg(e.Salary)
        from Employees e
        Join Departments d
        on d.DepartmentID = e.DepartmentID
        group by d.DepartmentName
        """)
        return self.cursor.fetchall()

    def employee_by_city(self):
        self.cursor.execute("""
        select City, count(*) as Employees_Count
        from Employees
        group by City
        """)
        return self.cursor.fetchall()







