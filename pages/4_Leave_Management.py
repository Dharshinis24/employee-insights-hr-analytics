from services.leave_service import LeaveService
from models.leave_request import LeaveRequest
from datetime import date

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Leave Management",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Leave Management")
leave_service = LeaveService()

if "show_form" not in st.session_state:
    st.session_state.show_form = False

if "edit_mode" not in st.session_state:
    st.session_state.edit_mode = False

if "delete_mode" not in st.session_state:
    st.session_state.delete_mode = False

if "leave_id" not in st.session_state:
    st.session_state.leave_id = None

update = False
submit = False
delete = False

st.caption("Manage employee leave requests")


search_key = st.text_input(
    "Search by First Name or Last Name"
)

if search_key:
    data = leave_service.search_by_EmployeeName(search_key)
else:
    data = leave_service.get_all_leaves()

data = [tuple(row) for row in data]

df = pd.DataFrame(
    data,
    columns=[
        "LeaveID",
        "EmployeeID",
        "LeaveType",
        "startDate",
        "EndDate",
        "Reason",
        "Status"
    ]
)
st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.divider()
col1, col2 = st.columns(2)

with col1:

    if st.button("➕ Add Leave"):

        st.session_state.show_form = True
        st.session_state.edit_mode = False
        st.session_state.delete_mode = False
        st.session_state.leave_id = None


with col2:

    if len(df) > 0:

        selected = st.selectbox(
            "Select Leave",
            df["LeaveID"]
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button("✏ Edit Leave"):

                st.session_state.show_form = True
                st.session_state.edit_mode = True
                st.session_state.delete_mode = False
                st.session_state.leave_id = selected

        with col2:

            if st.button("🗑 Delete Leave"):

                st.session_state.show_form = True
                st.session_state.edit_mode = False
                st.session_state.delete_mode = True
                st.session_state.leave_id = selected


if st.session_state.edit_mode or st.session_state.delete_mode:

    selected_leave = leave_service.get_leave_by_id(
        st.session_state.leave_id
    )

    LeaveID = st.session_state.leave_id
    EmployeeID = selected_leave.EmployeeID
    LeaveType = selected_leave.LeaveType
    StartDate = selected_leave.StartDate
    EndDate = selected_leave.EndDate
    Reason = selected_leave.Reason
    Status = selected_leave.Status

else:

    LeaveID = None
    EmployeeID = 0
    LeaveType = "Casual Leave"
    StartDate = date.today()
    EndDate = date.today()
    Reason = ""
    Status = "Pending"


if st.session_state.show_form:

    disabled = st.session_state.delete_mode

    with st.sidebar:

        if st.session_state.delete_mode:
            st.header("Delete Leave")

        elif st.session_state.edit_mode:
            st.header("Update Leave")

        else:
            st.header("Add Leave")


        with st.form("leave_form"):

            # Employee ID
            empid = st.number_input(
                "Employee ID",
                min_value=1001,
                value=int(EmployeeID) if EmployeeID else 1001,
                disabled=disabled
            )
            leave_types = [
                "Casual Leave",
                "Sick Leave",
                "Earned Leave",
                "Maternity Leave",
                "Other"
            ]

            leave_type = st.selectbox(
                "Leave Type",
                leave_types,
                index=(
                    leave_types.index(LeaveType)
                    if LeaveType in leave_types
                    else 0
                ),
                disabled=disabled
            )
            start_date = st.date_input(
                "From Date",
                value=StartDate,
                disabled=disabled
            )

            end_date = st.date_input(
                "To Date",
                value=EndDate,
                disabled=disabled
            )
            reason = st.text_area(
                "Reason",
                value=Reason if Reason else "",
                disabled=disabled
            )
            status_list = [
                "Pending",
                "Approved",
                "Rejected"
            ]

            status = st.selectbox(
                "Status",
                status_list,
                index=(
                    status_list.index(Status)
                    if Status in status_list
                    else 0
                ),
                disabled=disabled
            )

            col1, col2 = st.columns(2)

            with col1:

                if st.session_state.edit_mode:

                    update = st.form_submit_button(
                        "✏ Update"
                    )

                elif st.session_state.delete_mode:

                    delete = st.form_submit_button(
                        "🗑 Delete"
                    )

                else:

                    submit = st.form_submit_button(
                        "💾 Save"
                    )


            with col2:

                cancel = st.form_submit_button(
                    "❌ Cancel"
                )
            if cancel:

                st.session_state.show_form = False
                st.session_state.edit_mode = False
                st.session_state.delete_mode = False
                st.session_state.leave_id = None

                st.rerun()

            if update:

                if end_date < start_date:

                    st.error(
                        "To Date cannot be before From Date."
                    )

                else:

                    leave = LeaveRequest(
                        empid,
                        leave_type,
                        start_date,
                        end_date,
                        reason,
                        status,
                        st.session_state.leave_id
                    )

                    leave_service.update_leave(leave)

                    st.success(
                        "Leave updated successfully!"
                    )

                    st.session_state.show_form = False
                    st.session_state.edit_mode = False
                    st.session_state.delete_mode = False
                    st.session_state.leave_id = None

                    st.rerun()

            if delete:

                leave_service.delete_leave(
                    st.session_state.leave_id
                )

                st.success(
                    "Leave deleted successfully!"
                )

                st.session_state.show_form = False
                st.session_state.edit_mode = False
                st.session_state.delete_mode = False
                st.session_state.leave_id = None

                st.rerun()
            if submit:

                if end_date < start_date:

                    st.error(
                        "To Date cannot be before From Date."
                    )

                else:

                    leave = LeaveRequest(
                        empid,
                        leave_type,
                        start_date,
                        end_date,
                        reason,
                        "Pending"
                    )

                    leave_service.add_leave(leave)

                    st.success(
                        "Leave request added successfully!"
                    )

                    st.session_state.show_form = False
                    st.session_state.edit_mode = False
                    st.session_state.delete_mode = False
                    st.session_state.leave_id = None

                    st.rerun()