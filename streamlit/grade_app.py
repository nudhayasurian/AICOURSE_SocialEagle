import streamlit as st

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(
    page_title="Grade Manager",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Grade Manager")
st.write("Add students and view class grade statistics.")


# -----------------------------
# Grade calculation
# -----------------------------
def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


# -----------------------------
# Session state
# -----------------------------
# This runs only when "students"
# does not already exist.
if "students" not in st.session_state:
    st.session_state.students = []


# -----------------------------
# Add student form
# -----------------------------
st.subheader("Add Student")

with st.form("student_form", clear_on_submit=True):

    name = st.text_input("Student Name")

    mark = st.number_input(
        "Mark",
        min_value=0,
        max_value=100,
        step=1
    )

    submitted = st.form_submit_button("Add Student")

    if submitted:

        if not name.strip():
            st.error("Please enter a student name.")

        else:
            student = {
                "Name": name.strip(),
                "Mark": mark,
                "Grade": calculate_grade(mark)
            }

            st.session_state.students.append(student)

            st.success(
                f"{name} added successfully with grade "
                f"{calculate_grade(mark)}."
            )


# -----------------------------
# Display students
# -----------------------------
st.subheader("Student Results")

if st.session_state.students:

    st.table(st.session_state.students)

    # Get all marks
    marks = [
        student["Mark"]
        for student in st.session_state.students
    ]

    # Calculate statistics
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    st.subheader("Class Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Class Average",
        f"{average:.2f}"
    )

    col2.metric(
        "Highest Mark",
        highest
    )

    col3.metric(
        "Lowest Mark",
        lowest
    )

else:
    st.info("No students have been added yet.")