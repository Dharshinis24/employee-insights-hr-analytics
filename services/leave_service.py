from database import DBConnection


class LeaveService:

    def __init__(self):
        db = DBConnection()
        self.conn = db.get_connection()
        self.cursor = self.conn.cursor()

    def add_leave(self, leave):
        self.cursor.execute("""
            INSERT INTO Leaves
            (
                EmployeeID,
                LeaveType,
                StartDate,
                EndDate,
                Reason,
                Status
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            leave.EmployeeID,
            leave.LeaveType,
            leave.StartDate,
            leave.EndDate,
            leave.Reason,
            leave.Status
        ))

        self.conn.commit()
        return True

    def get_all_leaves(self):
        self.cursor.execute("""
            SELECT
                LeaveID,
                EmployeeID,
                LeaveType,
                StartDate,
                EndDate,
                Reason,
                Status
            FROM Leaves
        """)

        return self.cursor.fetchall()

    def get_leave_by_id(self, leave_id):
        self.cursor.execute("""
            SELECT
                LeaveID,
                EmployeeID,
                LeaveType,
                StartDate,
                EndDate,
                Reason,
                Status
            FROM Leaves
            WHERE LeaveID = ?
        """, (leave_id,))

        return self.cursor.fetchone()

    def update_leave(self, leave):
        self.cursor.execute("""
            UPDATE Leaves
            SET
                EmployeeID = ?,
                LeaveType = ?,
                StartDate = ?,
                EndDate = ?,
                Reason = ?,
                Status = ?
            WHERE LeaveID = ?
        """, (
            leave.EmployeeID,
            leave.LeaveType,
            leave.StartDate,
            leave.EndDate,
            leave.Reason,
            leave.Status,
            leave.LeaveID
        ))

        self.conn.commit()
        return True

    def delete_leave(self, leave_id):
        self.cursor.execute("""
            DELETE FROM Leaves
            WHERE LeaveID = ?
        """, (leave_id,))

        self.conn.commit()
        return True

    def search_by_EmployeeName(self, search_key):
        self.cursor.execute("""
            SELECT
                l.LeaveID,
                l.EmployeeID,
                l.LeaveType,
                l.StartDate,
                l.EndDate,
                l.Reason,
                l.Status
            FROM Leaves l
            INNER JOIN Employees e
                ON l.EmployeeID = e.EmployeeID
            WHERE e.FirstName LIKE ?
               OR e.LastName LIKE ?
        """, (
            "%" + search_key + "%",
            "%" + search_key + "%"
        ))

        return self.cursor.fetchall()

    def Leave_Status(self):
        self.cursor.execute("""
        select Status, count(*) as Count
        from Leaves
        group by Status
        """)
        return self.cursor.fetchall()

    