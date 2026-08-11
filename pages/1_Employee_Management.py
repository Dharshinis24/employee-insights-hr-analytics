from services.employee_service import EmployeeService
from models.employee import Employee
import streamlit as st
import pandas as pd


empservice = EmployeeService()

st.set_page_config(
    page_title="Employee Management",
    page_icon="👨‍💼",
    layout="wide"
)

st.title("👨‍💼 Employee Management")
st.caption("Manage your organization's employees")

delete = False
submit = False

if "show_form" not in st.session_state:
    st.session_state.show_form = False

if "edit_mode" not in st.session_state:
    st.session_state.edit_mode = False

if "delete_mode" not in st.session_state:
    st.session_state.delete_mode = False

search = st.text_input("Search by First Name or Last Name")
if search:
    employee = empservice.search_employees(search)

else:
    employee = empservice.get_all_employees()

columns = [
    "EmployeeID",
    "FirstName",
    "LastName",
    "Gender",
    "DateOfBirth",
    "Email",
    "Phone",
    "City",
    "DepartmentID",
    "JobTitle",
    "Salary",
    "JoiningDate",
    "ExperienceYears",
    "Status"
]


rows = [tuple(row) for row in employee]

df = pd.DataFrame(rows, columns=columns)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    height=500
)

st.divider()

col1,col2 = st.columns(2)

with col1:
    if st.button("➕ Add New Employee"):
        st.session_state.show_form = True
        st.session_state.edit_mode = False
        st.session_state.delete_mode = False
        st.session_state.employeeid = None

with col2:
    if len(df) > 0:
        select_emp = st.selectbox("Select Employee",df["EmployeeID"])
        col1,col2 = st.columns(2)
        with col1:
            if st.button("✏ Edit Employee"):
                st.session_state.show_form = True
                st.session_state.edit_mode = True 
                st.session_state.employeeid = select_emp
        with col2:
            if st.button("🗑 Delete Employee"):
                st.session_state.show_form = True
                st.session_state.delete_mode = True 
                st.session_state.employeeid = select_emp

    if st.session_state.edit_mode or st.session_state.delete_mode:

        emp = empservice.get_employee_by_id(st.session_state.employeeid)
        EmployeeID = st.session_state.employeeid
        FirstName = emp.FirstName
        LastName = emp.LastName
        Gender = emp.Gender
        DateOfBirth = emp.DateOfBirth
        Email = emp.Email
        Phone = emp.Phone
        City = emp.City
        DepartmentID = emp.DepartmentID
        JobTitle = emp.JobTitle
        Salary = float(emp.Salary)
        JoiningDate = emp.JoiningDate
        ExperienceYears = emp.ExperienceYears
        Status = emp.Status

    else:
        FirstName = ""
        LastName = ""
        Gender = "Male"
        DateOfBirth = None
        Email = ""
        Phone = ""
        City = ""
        DepartmentID = 1
        JobTitle = ""
        Salary = 0.0
        JoiningDate = None
        ExperienceYears = 0
        Status = "Active"
if st.session_state.show_form:
    with st.sidebar:
        if st.session_state.edit_mode:
            title = "Update Employee"
        elif st.session_state.delete_mode:
            title = "Delete Employee"
        else:
            title = "Add Employee"
        st.title(title)
        with st.form("employee_form"):
            disabled = st.session_state.delete_mode
            first_name = st.text_input("First Name",value=FirstName,disabled=disabled)
            last_name = st.text_input("Last Name",value=LastName,disabled=disabled)
            gender = ["Male", "Female"]
            gender = st.selectbox("Gender",gender,index=gender.index(Gender) if Gender in gender else 0,disabled=disabled)
            dob = st.date_input("Date of Birth",value=DateOfBirth,disabled=disabled)
            email = st.text_input("Email",value=Email,disabled=disabled)
            phone = st.text_input("Phone",value=Phone,disabled=disabled)
            city = st.text_input("City",value=City,disabled=disabled)
            departments = {
                    "Finance": 1,
                    "IT": 2,
                    "HR": 3,
                    "Sales": 4,
                    "Marketing": 5
                }
            department_names = list(departments.keys())

            if DepartmentID in departments.values():
                selected_department = next(key for key,value in departments.items() if value==DepartmentID)
            else:
                selected_department = department_names[0]

            department_name = st.selectbox("Department",department_names,index=department_names.index(selected_department),disabled=disabled)

            DepartmentID = departments[department_name]
            
            job_title = st.text_input("Job Title",value=JobTitle,disabled=disabled)
            salary = st.number_input("Salary",min_value=0.0,step=1000.0,value=Salary,disabled=disabled)
        
            joining_date = st.date_input("Joining Date",value=JoiningDate,disabled=disabled)
            experience = st.number_input("Experience (Years)",min_value=0,value=ExperienceYears,disabled=disabled)
            status_list = ["Active", "Inactive"]
            status = st.selectbox("Status",status_list,index = status_list.index(Status) if Status in status_list else 0, disabled=disabled
                    )
            col1, col2 = st.columns(2)
        
            with col1:
                if st.session_state.delete_mode:
                    delete = st.form_submit_button("🗑 Delete")
                if st.session_state.edit_mode:
                    submit = st.form_submit_button("✏ Update")
                else:
                    submit = st.form_submit_button("💾 Save")
        
            with col2:
                cancel = st.form_submit_button("❌ Cancel")
        
                if cancel:
                    st.session_state.show_form = False
                    st.session_state.edit_mode = False
                    st.rerun()
            if submit:
                if first_name.strip() == "" or email.strip() == "":
                    st.error("First Name and Email are required.")
                else:
                    if st.session_state.edit_mode:
                        employee = Employee(
                        first_name,
                        last_name,
                        gender,
                        dob,
                        email,
                        phone,
                        city,
                        DepartmentID,
                        job_title,
                        salary,
                        joining_date,
                        experience,
                        status,
                        EmployeeID)
                        empservice.update_employee(employee)
                        st.success("Employee updated successfully!")

                    else:
                        employee = Employee(
                        first_name,
                        last_name,
                        gender,
                        dob,
                        email,
                        phone,
                        city,
                        DepartmentID,
                        job_title,
                        salary,
                        joining_date,
                        experience,
                        status)
                        empservice.add_employee(employee)
                        st.success("Employee added successfully!")
                    st.session_state.show_form = False
                    st.session_state.edit_mode = False
                    st.session_state.delete_mode = False
                    st.rerun()
            if delete:
                empservice.delete_employee(EmployeeID)
                st.success("Employee deleted successfully!")
                st.session_state.show_form = False
                st.session_state.edit_mode = False
                st.session_state.delete_mode = False
                st.rerun()

        





