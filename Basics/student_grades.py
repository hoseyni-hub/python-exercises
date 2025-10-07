# Student Grades Management Program

students = {}  # dictionary to store names and grades

# get input from user
for i in range(5):
    name = input(f"Enter the name of student {i+1}: ")
    score = float(input(f"Enter the score of {name}: "))
    students[name] = score

# show all students
print("\n📋 List of students and scores:")
for name, score in students.items():
    print(f"{name}: {score}")

# find top student
top_student = max(students, key=students.get)
print(f"\n🏆 Top student: {top_student} with score {students[top_student]}")

# calculate average
average_score = sum(students.values()) / len(students)
print(f"\n📊 Class average: {average_score:.2f}")
