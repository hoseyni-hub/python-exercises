# Task: Calculate the average grade of a student from a dictionary of courses.

def calculate_average(grades):
    total = sum(grades.values())
    return total / len(grades)

if __name__ == "__main__":
    student_grades = {
        "Math": 18,
        "English": 15,
        "History": 14,
        "Physics": 19
    }

    avg = calculate_average(student_grades)
    print("Student grades:", student_grades)
    print("Average grade:", round(avg, 2))
