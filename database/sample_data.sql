INSERT INTO Departments (DepartmentName, ManagerName, Location, Budget)
VALUES
('IT', 'Arun Kumar', 'Chennai', 5000000),
('HR', 'Priya Sharma', 'Chennai', 1500000),
('Finance', 'Rahul Gupta', 'Bangalore', 3000000),
('Sales', 'Kavitha Nair', 'Coimbatore', 4000000),
('Marketing', 'Deepak Verma', 'Hyderabad', 2500000);

INSERT INTO Employees
(FirstName, LastName, Gender, DateOfBirth, Email, Phone, City, DepartmentID, JobTitle, Salary, JoiningDate, ExperienceYears, Status)
VALUES
('Aarav','Sharma','Male','1998-02-15','aarav.sharma@company.com','9876500001','Chennai',1,'Software Engineer',65000,'2022-06-15',3,'Active'),
('Ananya','Iyer','Female','1999-05-20','ananya.iyer@company.com','9876500002','Chennai',1,'Python Developer',70000,'2021-04-10',4,'Active'),
('Rohan','Patel','Male','1996-09-12','rohan.patel@company.com','9876500003','Bangalore',2,'HR Executive',45000,'2023-01-20',2,'Active'),
('Priya','Menon','Female','1997-01-18','priya.menon@company.com','9876500004','Coimbatore',2,'HR Manager',80000,'2019-07-11',6,'Active'),
('Vikram','Singh','Male','1995-08-09','vikram.singh@company.com','9876500005','Hyderabad',3,'Accountant',60000,'2020-11-01',5,'Active'),
('Sneha','Rao','Female','1998-11-23','sneha.rao@company.com','9876500006','Bangalore',3,'Financial Analyst',72000,'2021-03-15',4,'Active'),
('Karthik','Raj','Male','1997-04-14','karthik.raj@company.com','9876500007','Erode',1,'Backend Developer',68000,'2022-01-10',3,'Active'),
('Meera','Nair','Female','1999-07-30','meera.nair@company.com','9876500008','Salem',4,'Sales Executive',50000,'2023-02-14',2,'Active'),
('Arjun','Kumar','Male','1996-10-10','arjun.kumar@company.com','9876500009','Madurai',4,'Sales Manager',85000,'2018-12-18',7,'Active'),
('Divya','S','Female','2000-02-28','divya.s@company.com','9876500010','Erode',5,'Marketing Executive',48000,'2024-01-08',1,'Active'),

('Hari','Prasad','Male','1997-12-19','hari.prasad@company.com','9876500011','Trichy',1,'Full Stack Developer',75000,'2020-09-05',5,'Active'),
('Nisha','K','Female','1998-06-15','nisha.k@company.com','9876500012','Chennai',5,'SEO Analyst',52000,'2023-05-12',2,'Active'),
('Rahul','Verma','Male','1994-03-08','rahul.verma@company.com','9876500013','Bangalore',3,'Finance Manager',95000,'2017-06-18',8,'Active'),
('Lakshmi','R','Female','1999-09-25','lakshmi.r@company.com','9876500014','Coimbatore',2,'Recruiter',47000,'2022-08-01',3,'Active'),
('Sanjay','Das','Male','1996-07-17','sanjay.das@company.com','9876500015','Hyderabad',4,'Business Development Executive',62000,'2021-02-15',4,'Active'),
('Pooja','M','Female','1997-11-29','pooja.m@company.com','9876500016','Chennai',1,'Data Analyst',73000,'2020-10-12',5,'Active'),
('Ashwin','R','Male','1995-05-03','ashwin.r@company.com','9876500017','Salem',1,'DevOps Engineer',81000,'2019-09-09',6,'Active'),
('Keerthana','P','Female','1998-08-14','keerthana.p@company.com','9876500018','Madurai',5,'Content Strategist',56000,'2022-04-25',3,'Active'),
('Ganesh','M','Male','1999-12-01','ganesh.m@company.com','9876500019','Erode',3,'Accounts Executive',51000,'2023-09-01',2,'Active'),
('Monika','J','Female','1996-01-11','monika.j@company.com','9876500020','Trichy',4,'Sales Coordinator',54000,'2021-06-20',4,'Active'),

('Suresh','B','Male','1993-04-21','suresh.b@company.com','9876500021','Chennai',1,'Technical Lead',120000,'2016-02-10',9,'Active'),
('Anitha','R','Female','1997-03-16','anitha.r@company.com','9876500022','Bangalore',2,'HR Executive',46000,'2024-02-01',1,'Active'),
('Vignesh','S','Male','1998-09-28','vignesh.s@company.com','9876500023','Coimbatore',5,'Digital Marketing Executive',50000,'2023-10-10',2,'Active'),
('Bhavya','L','Female','1999-10-30','bhavya.l@company.com','9876500024','Hyderabad',3,'Junior Accountant',43000,'2024-03-15',1,'Active'),
('Kiran','P','Male','1995-06-13','kiran.p@company.com','9876500025','Chennai',4,'Regional Sales Manager',98000,'2018-05-25',7,'Active'),
('Deepa','S','Female','1998-12-04','deepa.s@company.com','9876500026','Erode',1,'QA Engineer',64000,'2022-07-18',3,'Active'),
('Naveen','K','Male','1997-08-18','naveen.k@company.com','9876500027','Salem',3,'Financial Analyst',71000,'2021-01-11',4,'Active'),
('Harini','V','Female','1999-02-06','harini.v@company.com','9876500028','Madurai',5,'Brand Executive',58000,'2022-11-01',3,'Active'),
('Prakash','T','Male','1996-11-15','prakash.t@company.com','9876500029','Trichy',2,'HR Manager',90000,'2019-04-18',6,'Active'),
('Swathi','N','Female','2000-05-12','swathi.n@company.com','9876500030','Coimbatore',1,'Software Engineer',62000,'2024-01-15',1,'Active');


INSERT INTO Attendances
(EmployeeID, AttendanceDate, CheckIn, CheckOut, Status, WorkingHours)
VALUES
(1002, '2026-08-04', '2026-08-04 09:05:00', '2026-08-04 17:20:00', 'Present', 8.25),
(1003, '2026-08-04', '2026-08-04 09:15:00', '2026-08-04 17:10:00', 'Present', 7.92),
(1004, '2026-08-04', '2026-08-04 09:00:00', '2026-08-04 13:00:00', 'Half Day', 4.00),
(1005, '2026-08-04', NULL, NULL, 'Leave', 0.00),
(1006, '2026-08-04', '2026-08-04 09:10:00', '2026-08-04 18:00:00', 'Present', 8.83),
(1007, '2026-08-05', '2026-08-05 09:00:00', '2026-08-05 17:00:00', 'Present', 8.00),
(1008, '2026-08-05', '2026-08-05 09:20:00', '2026-08-05 17:15:00', 'Present', 7.92),
(1009, '2026-08-05', NULL, NULL, 'Absent', 0.00),
(1010, '2026-08-05', '2026-08-05 09:05:00', '2026-08-05 17:00:00', 'Present', 7.92),
(1011, '2026-08-05', '2026-08-05 09:00:00', '2026-08-05 17:30:00', 'Present', 8.50),
(1012, '2026-08-06', '2026-08-06 09:10:00', '2026-08-06 17:10:00', 'Present', 8.00),
(1013, '2026-08-06', '2026-08-06 09:00:00', '2026-08-06 13:00:00', 'Half Day', 4.00),
(1014, '2026-08-06', NULL, NULL, 'Leave', 0.00),
(1015, '2026-08-06', '2026-08-06 09:15:00', '2026-08-06 17:15:00', 'Present', 8.00),
(1016, '2026-08-07', '2026-08-07 09:00:00', '2026-08-07 17:00:00', 'Present', 8.00),
(1017, '2026-08-07', '2026-08-07 09:10:00', '2026-08-07 17:20:00', 'Present', 8.17),
(1018, '2026-08-07', NULL, NULL, 'Absent', 0.00),
(1019, '2026-08-07', '2026-08-07 09:05:00', '2026-08-07 17:05:00', 'Present', 8.00),
(1020, '2026-08-08', '2026-08-08 09:00:00', '2026-08-08 17:00:00', 'Present', 8.00),
(1021, '2026-08-08', '2026-08-08 08:45:00', '2026-08-08 17:30:00', 'Present', 8.75),
(1022, '2026-08-08', '2026-08-08 09:20:00', '2026-08-08 13:20:00', 'Half Day', 4.00),
(1023, '2026-08-08', NULL, NULL, 'Leave', 0.00),
(1024, '2026-08-08', '2026-08-08 09:10:00', '2026-08-08 17:10:00', 'Present', 8.00),
(1025, '2026-08-09', '2026-08-09 09:00:00', '2026-08-09 17:30:00', 'Present', 8.50),
(1026, '2026-08-09', '2026-08-09 09:15:00', '2026-08-09 17:00:00', 'Present', 7.75),
(1027, '2026-08-09', NULL, NULL, 'Absent', 0.00),
(1028, '2026-08-09', '2026-08-09 09:05:00', '2026-08-09 17:05:00', 'Present', 8.00),
(1029, '2026-08-09', '2026-08-09 09:00:00', '2026-08-09 13:00:00', 'Half Day', 4.00),
(1030, '2026-08-09', '2026-08-09 09:10:00', '2026-08-09 17:10:00', 'Present', 8.00);

INSERT INTO Leaves
(EmployeeID, LeaveType, StartDate, EndDate, Reason, Status)
VALUES
(1005, 'Sick Leave', '2026-08-04', '2026-08-05', 'Fever and rest', 'Approved'),
(1014, 'Casual Leave', '2026-08-06', '2026-08-06', 'Personal work', 'Pending'),
(1018, 'Annual Leave', '2026-08-07', '2026-08-08', 'Family function', 'Approved'),
(1023, 'Sick Leave', '2026-08-08', '2026-08-08', 'Medical appointment', 'Rejected'),
(1009, 'Casual Leave', '2026-08-10', '2026-08-11', 'Personal reasons', 'Pending'),
(1027, 'Annual Leave', '2026-08-11', '2026-08-12', 'Vacation', 'Approved'),
(1004, 'Maternity Leave', '2026-08-13', '2026-08-15', 'Personal leave', 'Pending'),
(1012, 'Casual Leave', '2026-08-14', '2026-08-14', 'Family function', 'Approved'),
(1022, 'Sick Leave', '2026-08-15', '2026-08-16', 'Health reasons', 'Pending'),
(1028, 'Annual Leave', '2026-08-17', '2026-08-19', 'Vacation', 'Approved'),
(1003, 'Casual Leave', '2026-08-20', '2026-08-20', 'Personal work', 'Rejected'),
(1016, 'Sick Leave', '2026-08-21', '2026-08-22', 'Fever', 'Pending');

