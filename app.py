from services.employee_service import EmployeeService
from services.department_service import DepartmentService
from services.leave_service import LeaveService
from services.attendance_service import AttendanceService
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Employee Insights",
    page_icon="👨‍💼",
    layout="wide"
)
st.title("🏠 Employee Insights")

empservice = EmployeeService()
deptservice = DepartmentService()
col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("👨 Employee", empservice.get_employee_count())
with col2:
    data = deptservice.get_department_count()
    count = data[0]
    st.metric("🏢 Departments", count)
with col3:
    avg_salary = empservice.get_average_salary()
    st.metric("💰 Avg Salary", f"₹{avg_salary:,.0f}")
with col4:
    highest = empservice.get_highest_salary()
    st.metric("🏆 Highest Salary", f"₹{highest.Salary:,.0f}")


data = deptservice.department_wise_count()
dept_df = [tuple(row) for row in data]
columns = ["DepartmentName","Total count"]
df = pd.DataFrame(dept_df,columns=columns)
st.subheader("Department-wise Employee Count")
st.bar_chart(data=df,x="DepartmentName",y="Total count",use_container_width=True)
st.subheader("Average Salary by Department")
dept_wise_salary_data = empservice.dept_wise_avg_salary()
dept_wise_salary_data = [tuple(row) for row in dept_wise_salary_data]
dept_wise_salary_df = pd.DataFrame(dept_wise_salary_data,columns=["DepartmentName","Avg Salary"])
st.bar_chart(data=dept_wise_salary_df,x="DepartmentName",y="Avg Salary",use_container_width=True)
city_data = empservice.employee_by_city()
city_data = [tuple(row) for row in city_data]
city_df = pd.DataFrame(city_data,columns=["City","Employees_Count"])
st.subheader("Employees by City")
st.bar_chart(city_df,x="City",y="Employees_Count",use_container_width=True)
col1,col2 = st.columns(2)
with col1:
    empstatus = empservice.status_count()
    data = [tuple(row) for row in empstatus]
    status_df = pd.DataFrame(data,columns=["Status","Count"])
    employee_status = px.pie(status_df,names="Status",values="Count",title="Employee Status")
    st.plotly_chart(employee_status,use_container_width=True)
with col2:
    gender_data = empservice.gender_distribution()
    gender_data = [tuple(row) for row in gender_data]
    gender_df = pd.DataFrame(gender_data,columns=["Gender","count"])
    gender_pie = px.pie(gender_df,names="Gender",values="count",title="Gender Distribution")
    st.plotly_chart(gender_pie,use_container_width=True)
leave_service = LeaveService()
st.subheader("Leave Status")
leave_status = leave_service.Leave_Status()
leave_status = [tuple(row) for row in leave_status]
leave_status_df = pd.DataFrame(leave_status,columns=["Status","Count"])
st.dataframe(leave_status_df,use_container_width=True,hide_index=True)
st.bar_chart(leave_status_df,x="Status",y="Count")
attend_service = AttendanceService()
st.subheader("Attendance Status")
attendance_status_data = attend_service.attendance_status()
attendance_status_data = [tuple(row) for row in attendance_status_data]
attendance_status_df = pd.DataFrame(attendance_status_data,columns=["Status","Count"])
st.dataframe(attendance_status_df,use_container_width=True,hide_index=True)
fix = px.pie(attendance_status_df,names="Status",values="Count")
st.plotly_chart(fix,use_container_width=True)
