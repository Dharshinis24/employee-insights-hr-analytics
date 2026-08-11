import pyodbc

class DBConnection:

    def __init__(self):
        try:
            self.conn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};'
                'SERVER=localhost\\SQLEXPRESS;'
                'DATABASE=EmployeeAnalyticsDB;'
                'Trusted_Connection=Yes'
            )
           
        except pyodbc.Error as e:
            print("Error: ",e)
        else:
            print("Database connected")

    def get_connection(self):
        return self.conn

    