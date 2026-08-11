from services.attendance_service import AttendanceService
from models.attendance import Attendance
from datetime import datetime,date,time
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Attendance Management",
    page_icon="📅",
    layout="wide"
)

st.title("📅 Attendance Management")
AttendService = AttendanceService()

if "show_form" not in st.session_state:
    st.session_state.show_form = False
if "edit_mode" not in st.session_state:
    st.session_state.edit_mode = False
if "delete_mode" not in st.session_state:
    st.session_state.delete_mode = False
if "attendance_id" not in st.session_state:
    st.session_state.attendance_id = None
update = False
submit = False
delete = False

st.caption("To track the attendance of Employee")

search_key = st.text_input("Search by First Name or Last Name")
if search_key:
    data = AttendService.search_by_EmployeeName(search_key)
else:
    data = AttendService.get_all_attendance()

data = [tuple(row) for row in data]
df = pd.DataFrame(data,columns=["AttendanceID","EmployeeID","AttendanceDate","CheckIn","CheckOut","Status","WorkingHours"])
st.dataframe(df,use_container_width=True,hide_index=True)
st.divider()
col1,col2 = st.columns(2)
with col1:
    if st.button("➕ Add Attendance"):
        st.session_state.show_form = True
        st.session_state.edit_mode = False
        st.session_state.delete_mode = False
with col2:
    if len(df) > 0:
        selected = st.selectbox("Select Attendance",df["AttendanceID"])
        col1,col2 = st.columns(2)
        with col1:
            if st.button("✏ Edit Attendance"):
                st.session_state.show_form = True
                st.session_state.edit_mode = True
                st.session_state.delete_mode = False
                st.session_state.attendance_id = selected
        with col2:
            if st.button("🗑 Delete Attendane"):
                st.session_state.show_form = True
                st.session_state.edit_mode = False
                st.session_state.delete_mode = True
                st.session_state.attendance_id = selected
if st.session_state.edit_mode or st.session_state.delete_mode:
    selected_attendance = AttendService.get_attendance_by_id(st.session_state.attendance_id)
    AttendanceID = st.session_state.attendance_id
    EmployeeID = selected_attendance.EmployeeID
    AttendanceDate = selected_attendance.AttendanceDate
    CheckIn = selected_attendance.CheckIn
    CheckOut = selected_attendance.CheckOut
    Status = selected_attendance.Status
    WorkingHours = float(selected_attendance.WorkingHours)

else:
    AttendanceID = None
    EmployeeID = 0
    AttendanceDate = date.today()
    CheckIn = None
    CheckOut = None
    Status = "Present"
    WorkingHours = 0.0

if st.session_state.show_form:
    disabled = st.session_state.delete_mode
    with st.sidebar:
        if st.session_state.delete_mode:
            title = "Delete Attendance"
        elif st.session_state.edit_mode:
            title = "Update Attendance"
        else:
            title = "Add Attendance"
        st.title(title)
        with st.form("Attendance form"):
            empid = st.number_input("Employee ID",min_value=1001,value=int(EmployeeID) if EmployeeID else 1001,disabled=disabled)
            attendancedate = st.date_input("Attendance Date",value=AttendanceDate,disabled=disabled)
            checkin_time = CheckIn.time() if CheckIn is not None else time(9, 0)
            checkout_time = CheckOut.time() if CheckOut is not None else time(17, 0)
            checkin = st.time_input("Check IN",value=checkin_time,step=60,disabled=disabled)
            checkout = st.time_input("Check Out",value=checkout_time,step=60,disabled=disabled)
            status_list = ["Present","Absent","Half Day","Leave"]
            status = st.selectbox("Status",status_list,index=status_list.index(Status) if Status in status_list else 0,disabled=disabled)
            if status in ["Absent", "Leave"]:
                checkin_datetime = None
                checkout_datetime = None
                working_hours = 0.0
            else:
                checkin_datetime = datetime.combine(
                    attendancedate,
                    checkin
                )
                checkout_datetime = datetime.combine(
                    attendancedate,
                    checkout
                )
                if checkout_datetime > checkin_datetime:
                    working_hours = round(
                        (checkout_datetime - checkin_datetime).total_seconds() / 3600,
                        2
                    )
                else:
                    working_hours = 0.0
            st.number_input(
                "Working Hours",
                min_value=0.0,
                value=float(working_hours),
                disabled=True
            )
            col1,col2 = st.columns(2)
            with col1:
                if st.session_state.edit_mode:
                    update = st.form_submit_button("✏ Update")
                elif st.session_state.delete_mode:
                    delete = st.form_submit_button("🗑 Delete")
                else:
                    submit = st.form_submit_button("💾 Save")
                
            with col2:
                cancel = st.form_submit_button("Cancel")
            
            if cancel:
                st.session_state.show_form = False
                st.session_state.edit_mode = False
                st.session_state.delete_mode = False
                st.session_state.attendance_id = None
                st.rerun()
            if update:
                attendance = Attendance(
                    empid,attendancedate,checkin_datetime,checkout_datetime,status,working_hours,st.session_state.attendance_id
                )
                AttendService.update_attendance(attendance)
                st.success("Updated Successfully!")
                st.session_state.show_form = False
                st.session_state.edit_mode = False
                st.session_state.delete_mode = False
                st.rerun()
            if delete:
                AttendService.delete_attendance(st.session_state.attendance_id)
                st.success("Deleted Successfully!")
                st.session_state.show_form = False
                st.session_state.edit_mode = False
                st.session_state.delete_mode = False
                st.rerun()
            if submit:
                attendance = Attendance(
                    empid,attendancedate,checkin_datetime,checkout_datetime,status,working_hours,st.session_state.attendance_id
                )
                AttendService.add_attendance(attendance)
                st.success("Added Successfully!")
                st.session_state.show_form = False
                st.session_state.edit_mode = False
                st.session_state.delete_mode = False
                st.rerun()


                
  

