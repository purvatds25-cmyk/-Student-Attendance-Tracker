students = []


def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    student = {
        "name": name,
        "roll_no": roll_no
    }

    students.append(student)

    print("Student added successfully!")


def view_students():
    if len(students) == 0:
        print("No students found.")
        return

    print("\n--- Student List ---")

    for student in students:
        print("Roll No:", student["roll_no"])
        print("Name:", student["name"])
        print("--------------------")


def mark_attendance():
    if len(students) == 0:
        print("No students found. Please add students first.")
        return

    roll_no = input("Enter student roll number: ")
    status = input("Enter attendance (P/A): ").upper()

    if status == "P":
        print("Attendance marked as Present.")
    elif status == "A":
        print("Attendance marked as Absent.")
    else:
        print("Invalid attendance. Enter P or A.")


while True:
    print("\n===== STUDENT ATTENDANCE TRACKER =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Mark Attendance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        mark_attendance()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")