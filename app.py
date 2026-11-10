
import streamlit as st
import pandas as pd

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="GradeFlow | Student Analytics",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# SESSION STATE
# ==========================================

if "students" not in st.session_state:
    st.session_state.students = []

# ==========================================
# DESIGN SYSTEM
# ==========================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #0b1120;
    color: #f1f5f9;
}

[data-testid="stSidebar"] {
    background: #111a2e;
    border-right: 1px solid #26334c;
}

[data-testid="stSidebar"] * {
    color: #e2e8f0;
}

.main-title {
    font-size: 36px;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -1.2px;
}

.subtitle {
    color: #94a3b8;
    font-size: 14px;
    margin-top: 5px;
}

.section-title {
    color: #f8fafc;
    font-size: 21px;
    font-weight: 700;
    margin-top: 15px;
}

.metric-card {
    background: linear-gradient(145deg, #17243b, #111b30);
    border: 1px solid #293a58;
    border-radius: 16px;
    padding: 20px;
    min-height: 125px;
}

.metric-label {
    color: #94a3b8;
    font-size: 13px;
    font-weight: 500;
}

.metric-value {
    color: #ffffff;
    font-size: 29px;
    font-weight: 800;
    margin-top: 12px;
}

.metric-note {
    color: #38bdf8;
    font-size: 12px;
    margin-top: 5px;
}

.panel {
    background: #111c31;
    border: 1px solid #293a58;
    border-radius: 16px;
    padding: 20px;
}

div[data-testid="stForm"] {
    background: #111c31;
    border: 1px solid #293a58;
    border-radius: 16px;
    padding: 22px;
}

.stButton > button,
.stDownloadButton > button {
    border-radius: 10px;
    font-weight: 600;
    min-height: 42px;
}

.stButton > button[kind="primary"],
.stFormSubmitButton > button {
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    border: none;
    color: white;
}

div[data-testid="stDataFrame"] {
    border: 1px solid #293a58;
    border-radius: 12px;
    overflow: hidden;
}

hr {
    border-color: #293a58;
}

[data-testid="stMetric"] {
    background: #111c31;
    border: 1px solid #293a58;
    padding: 15px;
    border-radius: 13px;
}

.stCaption {
    color: #94a3b8;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# CALCULATIONS
# ==========================================

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


def get_student_data():
    return pd.DataFrame(st.session_state.students)


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:
    st.markdown("# 🎓 GradeFlow")
    st.caption("STUDENT PERFORMANCE SYSTEM")
    st.divider()

    page = st.radio(
        "NAVIGATION",
        ["Dashboard", "Add Student", "Students Records"],
        label_visibility="visible"
    )

    st.divider()

    st.markdown("### About")
    st.caption(
        "A student performance management system "
        "built with Python and Streamlit."
    )

    st.markdown("---")
    st.caption("Developed by Abdulrahman Mamdouh")
    st.caption("AI & ML Virtual Internship 2026")

# ==========================================
# HEADER
# ==========================================

st.markdown(
    '<div class="main-title">Student Performance</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Monitor academic results, manage students, '
    'and analyze performance.</div>',
    unsafe_allow_html=True
)

st.divider()

# ==========================================
# DASHBOARD
# ==========================================

if page == "Dashboard":

    st.markdown(
        '<div class="section-title">Overview Dashboard</div>',
        unsafe_allow_html=True
    )

    if not st.session_state.students:
        st.info(
            "No student records yet. Go to Add Student to create your first record."
        )
        if st.button("Go to Add Student", type="primary"):
            st.session_state["navigation_page"] = "Add Student"
            st.rerun()

    else:
        df = get_student_data()

        total_students = len(df)
        class_average = df["Average"].mean()
        highest_student = df.loc[df["Average"].idxmax()]
        lowest_student = df.loc[df["Average"].idxmin()]
        pass_count = int((df["Result"] == "Pass").sum())
        fail_count = int((df["Result"] == "Fail").sum())
        pass_rate = (pass_count / total_students) * 100

        # Metric cards
        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.markdown(
                f'<div class="metric-card">'
                f'<div class="metric-label">TOTAL STUDENTS</div>'
                f'<div class="metric-value">{total_students}</div>'
                f'<div class="metric-note">Registered students</div>'
                f'</div>',
                unsafe_allow_html=True
            )

        with c2:
            st.markdown(
                f'<div class="metric-card">'
                f'<div class="metric-label">CLASS AVERAGE</div>'
                f'<div class="metric-value">{class_average:.1f}%</div>'
                f'<div class="metric-note">Overall performance</div>'
                f'</div>',
                unsafe_allow_html=True
            )

        with c3:
            st.markdown(
                f'<div class="metric-card">'
                f'<div class="metric-label">PASS RATE</div>'
                f'<div class="metric-value">{pass_rate:.1f}%</div>'
                f'<div class="metric-note">{pass_count} students passed</div>'
                f'</div>',
                unsafe_allow_html=True
            )

        with c4:
            st.markdown(
                f'<div class="metric-card">'
                f'<div class="metric-label">FAILED STUDENTS</div>'
                f'<div class="metric-value">{fail_count}</div>'
                f'<div class="metric-note">Need improvement</div>'
                f'</div>',
                unsafe_allow_html=True
            )

        st.markdown("")

        # Top and lowest performers
        left, right = st.columns(2)

        with left:
            st.markdown("### 🏆 Top Performer")
            st.markdown(
                f'<div class="panel">'
                f'<h2 style="color:#a5b4fc;">{highest_student["Student Name"]}</h2>'
                f'<h1 style="color:white;">{highest_student["Average"]:.2f}%</h1>'
                f'<p style="color:#94a3b8;">Grade {highest_student["Grade"]}</p>'
                f'</div>',
                unsafe_allow_html=True
            )

        with right:
            st.markdown("### 📊 Lowest Performer")
            st.markdown(
                f'<div class="panel">'
                f'<h2 style="color:#fbbf24;">{lowest_student["Student Name"]}</h2>'
                f'<h1 style="color:white;">{lowest_student["Average"]:.2f}%</h1>'
                f'<p style="color:#94a3b8;">Grade {lowest_student["Grade"]}</p>'
                f'</div>',
                unsafe_allow_html=True
            )

        st.markdown("### Grade Distribution")

        grade_order = ["A", "B", "C", "D", "F"]
        grade_counts = (
            df["Grade"]
            .value_counts()
            .reindex(grade_order, fill_value=0)
        )

        chart_df = pd.DataFrame({
            "Grade": grade_counts.index,
            "Students": grade_counts.values
        }).set_index("Grade")

        st.bar_chart(chart_df, use_container_width=True)

        st.markdown("### Recent Student Records")
        st.dataframe(
            df[["Student Name", "Average", "Grade", "Result"]].tail(5),
            use_container_width=True,
            hide_index=True
        )

# ==========================================
# ADD STUDENT
# ==========================================

elif page == "Add Student":

    st.markdown("### ➕ Add New Student")
    st.caption("Enter student information and subject scores.")

    with st.form("student_form", clear_on_submit=True):

        name = st.text_input(
            "Student Full Name",
            placeholder="e.g. Abdulrahman Mamdouh"
        )

        st.markdown("#### Subject Scores")

        col1, col2 = st.columns(2)

        with col1:
            python_score = st.number_input(
                "Python",
                min_value=0.0,
                max_value=100.0,
                value=0.0,
                step=1.0
            )

            math_score = st.number_input(
                "Mathematics",
                min_value=0.0,
                max_value=100.0,
                value=0.0,
                step=1.0
            )

        with col2:
            english_score = st.number_input(
                "English",
                min_value=0.0,
                max_value=100.0,
                value=0.0,
                step=1.0
            )

            ai_score = st.number_input(
                "Artificial Intelligence",
                min_value=0.0,
                max_value=100.0,
                value=0.0,
                step=1.0
            )

        submitted = st.form_submit_button(
            "Calculate & Save Student",
            type="primary",
            use_container_width=True
        )

    if submitted:
        if not name.strip():
            st.error("Please enter the student's name.")

        else:
            scores = [
                python_score,
                math_score,
                english_score,
                ai_score
            ]

            total = sum(scores)
            average = total / 4
            grade = calculate_grade(average)
            result = "Pass" if average >= 50 else "Fail"

            student = {
                "Student Name": name.strip(),
                "Python": python_score,
                "Mathematics": math_score,
                "English": english_score,
                "Artificial Intelligence": ai_score,
                "Total": total,
                "Average": average,
                "Grade": grade,
                "Result": result
            }

            st.session_state.students.append(student)

            st.success("Student added successfully!")

            st.metric("Total Score", f"{total:.2f}/400")
            st.metric("Average", f"{average:.2f}%")
            st.metric("Grade", grade)
            st.metric("Result", result)

# ==========================================
# STUDENTS RECORDS
# ==========================================

elif page == "Students Records":

    st.markdown("### 👥 Students Records")
    st.caption("Search, review, and export student information.")

    if not st.session_state.students:
        st.info("No student records available yet.")

    else:
        df = get_student_data()

        search = st.text_input(
            "Search Student",
            placeholder="Type a student name..."
        )

        filtered_df = df[
            df["Student Name"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

        st.dataframe(
            filtered_df,
            use_container_width=True,
            hide_index=True
        )

        st.caption(f"Showing {len(filtered_df)} of {len(df)} students")

        csv_data = filtered_df.to_csv(
            index=False
        ).encode("utf-8-sig")

        st.download_button(
            "⬇ Download CSV Report",
            data=csv_data,
            file_name="student_grades_report.csv",
            mime="text/csv",
            use_container_width=True
        )

        st.divider()

        if st.button("Clear All Student Records"):
            st.session_state.students = []
            st.rerun()

# ==========================================
# FOOTER
# ==========================================

st.divider()

st.markdown(
    '<div style="text-align:center;color:#64748b;'
    'font-size:12px;padding:10px;">'
    'GRADE FLOW · Built with Python & Streamlit · '
    'Abdulrahman Mamdouh · 2026'
    '</div>',
    unsafe_allow_html=True
)
