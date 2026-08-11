create database EmployeeAnalyticsDB
use EmployeeAnalyticsDB
go
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY IDENTITY(1,1),
    DepartmentName VARCHAR(100) NOT NULL UNIQUE,
    ManagerName VARCHAR(100),
    Location VARCHAR(100),
    Budget DECIMAL(15,2),
    CreatedDate DATETIME DEFAULT GETDATE()
);

CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY IDENTITY(1001,1),

    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50),

    Gender VARCHAR(10)
        CHECK(Gender IN ('Male','Female','Other')),

    DateOfBirth DATE NOT NULL,

    Email VARCHAR(100) UNIQUE,

    Phone VARCHAR(15),

    City VARCHAR(50),

    DepartmentID INT NOT NULL,

    JobTitle VARCHAR(100),

    Salary DECIMAL(10,2)
        CHECK(Salary>=0),

    JoiningDate DATE,

    ExperienceYears INT
        CHECK(ExperienceYears>=0),

    Status VARCHAR(20)
        DEFAULT 'Active'
        CHECK(Status IN ('Active','Inactive')),

    FOREIGN KEY (DepartmentID)
        REFERENCES Departments(DepartmentID)
);

create table Attendances(
    AttendanceID int identity(1,1) primary key,
    EmployeeID int,
    AttendanceDate Date,
    CheckIn Datetime,
    CheckOut Datetime,
    Status varchar(20),
    WorkingHours decimal(5,2),
    foreign key(EmployeeID) references Employees(EmployeeID))

CREATE TABLE Leaves (
    LeaveID INT IDENTITY(1,1) PRIMARY KEY,
    EmployeeID INT NOT NULL,
    LeaveType VARCHAR(30) NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    Reason VARCHAR(255),
    Status VARCHAR(20) NOT NULL DEFAULT 'Pending',
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);
