def average_grade(students):
    """
    Calculate the average grade from a dictionary of students.
    :param students: dict with {student_name: grade}
    :return: average grade (float)
    """
    if not students:
        return None  # return None if dictionary is empty
    
    total = sum(students.values())
    count = len(students)
    return total / count


# Example usage:
grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90
}

print("Student Grades:", grades)
print("Average Grade:", average_grade(grades))