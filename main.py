import csv
from datetime import date

students = []


# ---------------- ADD STUDENT ----------------
def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("Student with this roll number already exists!")
            return

    student = {
        "name": name,
        "roll_no": roll_no
    }

    students.append(student)
    print("Student added successfully!")


# ---------------- VIEW STUDENTS ----------------
def view_students():
    if len(students) == 0:
        print("No students found.")
        return

    print("\n--- Student List ---")

    for student in students:
        print("Roll No:", student["roll_no"])
        print("Name:", student["name"])
        print("--------------------")


# ---------------- MARK ATTENDANCE ----------------
def mark_attendance():
    if len(students) == 0:
        print("No students found. Please add students first.")
        return

    roll_no = input("Enter student roll number: ")

    student_found = False

    for student in students:
        if student["roll_no"] == roll_no:
            student_found = True
            break

    if not student_found:
        print("Student not found.")
        return

    status = input("Enter attendance (P/A): ").upper()

    if status != "P" and status != "A":
        print("Invalid attendance. Enter P or A.")
        return

    today = date.today()

    with open("attendance.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([today, roll_no, status])

    if status == "P":
        print("Attendance marked as Present.")
    else:
        print("Attendance marked as Absent.")


# ---------------- ATTENDANCE PERCENTAGE ----------------
def attendance_percentage():
    if len(students) == 0:
        print("No students found.")
        return

    roll_no = input("Enter student roll number: ")

    present = 0
    total = 0

    try:
        with open("attendance.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) >= 3 and row[1] == roll_no:
                    total += 1

                    if row[2] == "P":
                        present += 1

    except FileNotFoundError:
        print("No attendance record found.")
        return

    if total == 0:
        print("No attendance record found for this student.")
        return

    percentage = (present / total) * 100

    print("\n--- Attendance Details ---")
    print("Roll No:", roll_no)
    print("Present Days:", present)
    print("Total Days:", total)
    print("Attendance Percentage:", round(percentage, 2), "%")

    if percentage < 75:
        print("Status: Defaulter")
    else:
        print("Status: Not a Defaulter")


# ---------------- ATTENDANCE REPORT ----------------
def attendance_report():
    if len(students) == 0:
        print("No students found.")
        return

    print("\n========== ATTENDANCE REPORT ==========")

    try:
        with open("attendance.csv", "r") as file:
            reader = csv.reader(file)
            records = list(reader)

    except FileNotFoundError:
        print("No attendance records found.")
        return

    for student in students:
        roll_no = student["roll_no"]
        name = student["name"]

        present = 0
        total = 0

        for row in records:
            if len(row) >= 3 and row[1] == roll_no:
                total += 1

                if row[2] == "P":
                    present += 1

        if total > 0:
            percentage = (present / total) * 100
        else:
            percentage = 0

        print("\nRoll No:", roll_no)
        print("Name:", name)
        print("Present:", present)
        print("Total Days:", total)
        print("Percentage:", round(percentage, 2), "%")

        if percentage < 75:
            print("Status: Defaulter")
        else:
            print("Status: Not a Defaulter")

        print("----------------------------")


# ---------------- MAIN MENU ----------------
while True:
    print("\n====================================")
    print("     STUDENT ATTENDANCE TRACKER")
    print("====================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Mark Attendance")
    print("4. Attendance Percentage")
    print("5. Attendance Report")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        mark_attendance()

    elif choice == "4":
        attendance_percentage()

    elif choice == "5":
        attendance_report()

    elif choice == "6":
        print("Thank you for using Student Attendance Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")