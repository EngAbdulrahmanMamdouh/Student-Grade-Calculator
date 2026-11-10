
# Student Grade Calculator
# Codomax Internship 2026 - Module 02

def get_student_info():
    while True:
        name = input("Enter student name: ").strip()
        if name:
            return name
        print("Name cannot be empty!")


def get_valid_score(subject):
    while True:
        try:
            score = float(input(f"Enter {subject} score (0-100): "))

            if 0 <= score <= 100:
                return score

            print("Score must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


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


def calculate_results(scores):
    total = sum(scores.values())
    average = total / len(scores)
    grade = calculate_grade(average)
    result = "Pass" if average >= 50 else "Fail"

    return total, average, grade, result


def display_report(name, scores):
    total, average, grade, result = calculate_results(scores)

    print("\n" + "=" * 45)
    print("             STUDENT REPORT")
    print("=" * 45)

    print("Student Name:", name)

    for subject, score in scores.items():
        print(f"{subject:<25}: {score:.2f}")

    print("-" * 45)
    print(f"Total Score: {total:.2f}/400")
    print(f"Average: {average:.2f}%")
    print(f"Grade: {grade}")
    print(f"Result: {result}")
    print("=" * 45)


def main():
    subjects = [
        "Python",
        "Mathematics",
        "English",
        "Artificial Intelligence"
    ]

    while True:
        print("\nSTUDENT GRADE CALCULATOR")

        name = get_student_info()
        scores = {}

        for subject in subjects:
            scores[subject] = get_valid_score(subject)

        display_report(name, scores)

        choice = input("\nCalculate another student? (yes/no): ")
        if choice.strip().lower() not in ["yes", "y"]:
            print("\nThank you for using Student Grade Calculator!")
            break


if __name__ == "__main__":
    main()
