from services.department_service import DepartmentService
from models.department import Departments
import streamlit as st
import pandas as pd

deptservice = DepartmentService()

st.set_page_config(
    page_title="Department Management",
    page_icon="🏢",
    layout="wide"
)

st.title("🏢 Department Management")
st.caption("Manage your organization's departments")

delete = False
submit = False

if "show_form" not in st.session_state:
    st.session_state.show_form = False

if "edit_mode" not in st.session_state:
    st.session_state.edit_mode = False

if "delete_mode" not in st.session_state:
    st.session_state.delete_mode = False


search_key = st.text_input("🔍 Search Department")

if search_key:
    departments = deptservice.search_department(search_key)
else:
    departments = deptservice.get_all_departments()


columns = [
    "DepartmentID",
    "DepartmentName",
    "ManagerName",
    "Location",
    "Budget"
]

rows = [tuple(row) for row in departments]

df = pd.DataFrame(rows, columns=columns)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.divider()


col1, col2 = st.columns(2)

with col1:
    if st.button("➕ Add Department"):
        st.session_state.show_form = True
        st.session_state.edit_mode = False
        st.session_state.delete_mode = False
        st.session_state.department_id = None

with col2:
    if len(df) > 0:
        selected = st.selectbox(
            "Select Department",
            df["DepartmentID"]
        )
        col1,col2 = st.columns(2)
        with col1:
            if st.button("✏ Edit Department"):
                st.session_state.show_form = True
                st.session_state.edit_mode = True
                st.session_state.delete_mode = False
                st.session_state.department_id = selected
        with col2:
            if st.button("🗑 Delete Department"):
                st.session_state.show_form = True
                st.session_state.edit_mode = False
                st.session_state.delete_mode = True
                st.session_state.department_id = selected
            
    if st.session_state.edit_mode or st.session_state.delete_mode:

        dept = deptservice.get_department_by_id(
            st.session_state.department_id
        )

        DepartmentName = dept.DepartmentName
        ManagerName = dept.ManagerName
        Location = dept.Location
        Budget = float(dept.Budget)

    else:

        DepartmentName = ""
        ManagerName = ""
        Location = ""
        Budget = 0.0
if st.session_state.show_form:
    with st.sidebar:
        if st.session_state.edit_mode:
            title = "Update Department"
        elif st.session_state.delete_mode:
            title = "Delete Department"
        else:
            title = "Add Department"

        st.header(title)

        with st.form("department_form"):
            disabled = st.session_state.delete_mode

            department_name = st.text_input(
                "Department Name",
                value=DepartmentName,
                disabled=disabled
            )

            manager_name = st.text_input(
                "Manager Name",
                value=ManagerName,
                disabled=disabled
            )

            location = st.text_input(
                "Location",
                value=Location,
                disabled=disabled
            )

            budget = st.number_input(
                "Budget",
                min_value=0.0,
                value=Budget,
                step=10000.0,
                disabled=disabled
            )            
            col1, col2 = st.columns(2)

            with col1:
                if st.session_state.delete_mode:
                    delete = st.form_submit_button("🗑 Delete")
                elif st.session_state.edit_mode:
                    submit = st.form_submit_button("✏ Update")
                else:
                    submit = st.form_submit_button("💾 Save")

            with col2:
                cancel = st.form_submit_button("❌ Cancel")

            if cancel:
                st.session_state.show_form = False
                st.session_state.edit_mode = False
                st.session_state.delete_mode = False
                st.session_state.department_id = None
                st.rerun()

            if submit:

                if department_name.strip() == "":
                    st.error("Department Name is required.")

                else:

                    if st.session_state.edit_mode:

                        department = Departments(
                            department_name,
                            manager_name,
                            location,
                            budget,
                            st.session_state.department_id
                        )

                        existing = deptservice.get_department_by_name(
                            department.DepartmentName
                        )

                        if existing and existing.DepartmentID != st.session_state.department_id:
                            st.error(
                                f"Department '{department.DepartmentName}' already exists!"
                            )
                        else:
                            deptservice.update_department(department)

                            st.success("Department updated successfully!")

                            st.session_state.show_form = False
                            st.session_state.edit_mode = False
                            st.session_state.delete_mode = False
                            st.session_state.department_id = None
                            st.rerun()

                    else:

                        department = Departments(
                            department_name,
                            manager_name,
                            location,
                            budget
                        )

                        existing = deptservice.get_department_by_name(
                            department.DepartmentName
                        )

                        if existing:
                            st.error(
                                f"Department '{department.DepartmentName}' already exists!"
                            )
                        else:
                            deptservice.add_department(department)

                            st.success("Department added successfully!")

                            st.session_state.show_form = False
                            st.session_state.edit_mode = False
                            st.session_state.delete_mode = False
                            st.session_state.department_id = None
                            st.rerun()
            if delete:
                if deptservice.department_has_employee(st.session_state.department_id) > 0:
                    st.error("Cannot delete this department because employees are assigned to it.")
                else:
                    deptservice.delete_department(st.session_state.department_id)
                    st.success("Department deleted successfully!")
                    st.session_state.show_form = False
                    st.session_state.edit_mode = False
                    st.session_state.delete_mode = False
                    st.session_state.department_id = None
                    st.rerun()