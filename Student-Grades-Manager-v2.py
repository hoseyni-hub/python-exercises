students = {}

while True:
    print("\n--- Student Grades Manager ---")
    print("1. Add student")
    print("2. Show all students")
    print("3. Calculate average grade")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = float(input("Enter student grade: "))
        students[name] = grade
        print(f"{name} added with grade {grade}")
    
    elif choice == "2":
        if not students:
            print("No students yet.")
        else:
            for name, grade in students.items():
                print(f"{name}: {grade}")
    
    elif choice == "3":
        if not students:
            print("No grades available.")
        else:
            avg = sum(students.values()) / len(students)
            print(f"Average grade: {avg:.2f}")
    
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")