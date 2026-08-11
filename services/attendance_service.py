from database import DBConnection

class AttendanceService:

    def __init__(self):
        db = DBConnection()
        self.conn = db.get_connection()
        self.cursor = self.conn.cursor()

    def add_attendance(self,attendance):
        self.cursor.execute("""
        insert into Attendances
        (EmployeeID, AttendanceDate, CheckIn, CheckOut, Status, WorkingHours)
        values(?,?,?,?,?,?)
        """,(attendance.EmployeeID,attendance.AttendanceDate,attendance.CheckIn,attendance.CheckOut,attendance.Status,attendance.WorkingHours))
        self.conn.commit()
        return True

    def get_all_attendance(self):
        self.cursor.execute("""
        select * from Attendances
        """)
        return self.cursor.fetchall()

    def get_attendance_by_id(self,attendance_id):
        self.cursor.execute("""
        select * from Attendances
        where AttendanceID = ?
        """,(attendance_id,))
        return self.cursor.fetchone()

    def update_attendance(self,attendance):
        self.cursor.execute("""
        update Attendances
        set EmployeeID=?,AttendanceDate=?,CheckIn=?,CheckOut=?,Status=?,WorkingHours=?
        where AttendanceID = ?
        """,(attendance.EmployeeID,attendance.AttendanceDate,attendance.CheckIn,attendance.CheckOut,attendance.Status,attendance.WorkingHours,attendance.AttendanceID))
        self.conn.commit()
        return True

    def delete_attendance(self,AttendanceID):
        self.cursor.execute("""
        delete from Attendances
        where AttendanceID = ?
        """,(AttendanceID,))
        self.conn.commit()
        return True

    def search_by_EmployeeName(self,EmployeeName):
        self.cursor.execute("""
        select a.*
        from Attendances a
        Join Employees e
        on a.EmployeeID = e.EmployeeID
        where e.FirstName Like ? or e.LastName Like ?
        """,(f"%{EmployeeName}%",f"%{EmployeeName}%"))
        return self.cursor.fetchall()

    def attendance_status(self):
        self.cursor.execute("""
        select Status, count(*) as Count
        from Attendances
        group by Status
        """)
        return self.cursor.fetchall()
