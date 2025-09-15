# Student Grades Analyzer

students = {
    "Alice": [85, 90, 78],
    "Bob": [70, 88, 92],
    "Charlie": [95, 85, 87]
}

for name, grades in students.items():
    avg = sum(grades) / len(grades)
    print(f"{name}'s average grade: {avg:.2f}")

overall_avg = sum(sum(g) for g in students.values()) / sum(len(g) for g in students.values())
print(f"\nClass average: {overall_avg:.2f}")