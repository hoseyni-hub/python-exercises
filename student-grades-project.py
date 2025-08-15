# Student grades management system

# Dictionary to store student names and their grades
students = {}

# Add new students and their grades
students["Alice"] = [18, 17, 19]
students["Bob"] = [14, 15, 13]
students["Charlie"] = [20, 19, 18]

# Function to calculate average grade
def calculate_average(grades):
    return sum(grades) / len(grades)

# Print each student's grades and average
for name, grades in students.items():
    avg = calculate_average(grades)
    print(f"Student: {name}")
    print(f"Grades: {grades}")
    print(f"Average: {avg:.2f}\n")