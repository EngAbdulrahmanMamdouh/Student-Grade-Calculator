
import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Student Grade Calculator",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.stApp {
    background-color: #f4f7fb;
}
.main-title {
    font-size: 36px;
    font-weight: 800;
    color: #172554;
}
.subtitle {
    color: #64748b;
    font-size: 16px;
}
.result-card {
    background: white;
    padding: 22px;
    border-radius: 14px;
    border: 1px solid #e2e8f0;
    text-align: center;
}
.result-value {
    font-size: 30px;
    font-weight: 800;
    color: #1d4ed8;
}
.result-label {
    color: #64748b;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# Session state
if "students" not in st.session_state:
    st.session_state.students = []

if "latest_result" not in st.session_state:
    st.session_state.latest_result = None


# Grade calculation
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    return "F"


# Header
st.markdown(
    '<div class="main-title">Student Grade Calculator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Manage student grades and calculate academic performance.</div>',
    unsafe_allow_html=True
)

st.divider()

# Input form
st.subheader("Student Information")

with st.form("student_form"):
    student_name = st.text_input(
        "Student Name",
        placeholder="Enter student full name"
    )

    st.markdown("### Subject Scores")

    col1, col2 = st.columns(2)

    with col1:
        python_score = st.number_input(
            "Python",
            min_value=0.0,
            max_value=100.0,
            value=0.0
        )

        math_score = st.number_input(
            "Mathematics",
            min_value=0.0,
            max_value=100.0,
            value=0.0
        )

    with col2:
        english_score = st.number_input(
            "English",
            min_value=0.0,
            max_value=100.0,
            value=0.0
        )

        ai_score = st.number_input(
            "Artificial Intelligence",
            min_value=0.0,
            max_value=100.0,
            value=0.0
        )

    submitted = st.form_submit_button(
        "Calculate Results",
        use_container_width=True
    )

# Process results
if submitted:
    if not student_name.strip():
        st.error("Please enter the student name.")
    else:
        scores = {
            "Python": python_score,
            "Mathematics": math_score,
            "English": english_score,
            "Artificial Intelligence": ai_score
        }

        total = sum(scores.values())
        average = total / len(scores)
        grade = calculate_grade(average)
        result = "Pass" if average >= 50 else "Fail"

        student = {
            "Student Name": student_name.strip(),
            **scores,
            "Total": total,
            "Average": average,
            "Grade": grade,
            "Result": result
        }

        st.session_state.students.append(student)
        st.session_state.latest_result = student

# Latest result
if st.session_state.latest_result is not None:
    student = st.session_state.latest_result

    st.divider()
    st.subheader("Student Results")

    st.markdown(f"### {student['Student Name']}")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Total Score", f"{student['Total']:.2f}/400")

    with c2:
        st.metric("Average", f"{student['Average']:.2f}%")

    with c3:
        st.metric("Grade", student["Grade"])

    with c4:
        st.metric("Final Result", student["Result"])

    if student["Result"] == "Pass":
        st.success("Congratulations! The student has passed.")
    else:
        st.error("The student has failed.")

    st.subheader("Subject Breakdown")

    score_table = pd.DataFrame({
        "Subject": [
            "Python",
            "Mathematics",
            "English",
            "Artificial Intelligence"
        ],
        "Score": [
            student["Python"],
            student["Mathematics"],
            student["English"],
            student["Artificial Intelligence"]
        ]
    })

    st.dataframe(
        score_table,
        use_container_width=True,
        hide_index=True
    )

# All students
if st.session_state.students:
    st.divider()
    st.subheader("All Students Records")

    students_df = pd.DataFrame(st.session_state.students)

    st.dataframe(
        students_df,
        use_container_width=True,
        hide_index=True
    )

    csv_data = students_df.to_csv(index=False).encode("utf-8-sig")

    st.download_button(
        "Download Students Report (CSV)",
        data=csv_data,
        file_name="students_report.csv",
        mime="text/csv"
    )

    if st.button("Clear All Records"):
        st.session_state.students = []
        st.session_state.latest_result = None
        st.rerun()

# Footer
st.divider()
st.caption("Developed by Abdulrahman Mamdouh | AI & ML Virtual Internship 2026")
