# Student Grade Management System

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 20:
            self.grades.append(grade)
        else:
            print("Grade must be between 0 and 20.")

    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Student: {self.name}, Grades: {self.grades}, Average: {self.average():.2f}"


class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def class_average(self):
        if len(self.students) == 0:
            return 0
        total = sum(student.average() for student in self.students)
        return total / len(self.students)

    def display_students(self):
        for student in self.students:
            print(student)


# Example usage:
student1 = Student("Ali")
student2 = Student("Sara")

student1.add_grade(18)
student1.add_grade(15)
student2.add_grade(20)
student2.add_grade(10)

classroom = Classroom()
classroom.add_student(student1)
classroom.add_student(student2)

print("=== Students ===")
classroom.display_students()
print(f"Class average: {classroom.class_average():.2f}")
