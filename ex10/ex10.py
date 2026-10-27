
import json
import os
from datetime import datetime

FILE_NAME = "attendance.json"


class AttendanceManagement:

    def __init__(self):
        self.students = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(FILE_NAME):
            try:
                with open(FILE_NAME, "r") as file:
                    self.students = json.load(file)
            except (json.JSONDecodeError, OSError):
                self.students = {}

    def save_data(self):
        with open(FILE_NAME, "w") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self):
        roll = input("Enter Roll Number: ").strip()

        if roll in self.students:
            print("Student already exists!")
            return

        name = input("Enter Student Name: ").strip()

        if not roll or not name:
            print("Invalid student details!")
            return

        self.students[roll] = {
            "name": name,
            "attendance": {}
        }

        self.save_data()
        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No students available!")
            return

        print("\n----- Student List -----")
        print("Roll No\tStudent Name")

        for roll, details in self.students.items():
            print(f"{roll}\t{details['name']}")

    def mark_attendance(self):
        if not self.students:
            print("No students available!")
            return

        date = input(
            "Enter Date (YYYY-MM-DD) or press Enter for today: "
        ).strip()

        if not date:
            date = datetime.now().strftime("%Y-%m-%d")

        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format!")
            return

        print("\n----- Mark Attendance -----")

        for roll, details in self.students.items():
            while True:
                print(f"{roll} - {details['name']}")
                status = input("Present/Absent (P/A): ").upper()

                if status in ["P", "A"]:
                    details["attendance"][date] = status
                    break
                else:
                    print("Enter only P or A!")

        self.save_data()
        print("Attendance marked successfully!")

    def view_attendance(self):
        roll = input("Enter Roll Number: ").strip()

        if roll not in self.students:
            print("Student not found!")
            return

        student = self.students[roll]
        records = student["attendance"]

        print("\n----- Attendance Details -----")
        print("Name:", student["name"])
        print("Roll Number:", roll)

        if not records:
            print("No attendance records found!")
            return

        print("Date\t\tStatus")

        for date, status in sorted(records.items()):
            result = "Present" if status == "P" else "Absent"
            print(f"{date}\t{result}")

    def attendance_report(self):
        if not self.students:
            print("No students available!")
            return

        print("\n----- Attendance Report -----")
        print("Roll\tName\tPresent\tTotal\tPercentage")

        for roll, student in self.students.items():
            records = student["attendance"]
            total = len(records)

            present = sum(
                1 for status in records.values()
                if status == "P"
            )

            if total > 0:
                percentage = (present / total) * 100
            else:
                percentage = 0

            print(
                f"{roll}\t{student['name']}\t"
                f"{present}\t{total}\t{percentage:.2f}%"
            )

            if total > 0 and percentage < 75:
                print("   Warning: Attendance below 75%")

    def search_student(self):
        roll = input("Enter Roll Number to Search: ").strip()

        if roll in self.students:
            student = self.students[roll]
            print("\nStudent Found!")
            print("Roll Number:", roll)
            print("Name:", student["name"])
        else:
            print("Student not found!")

    def delete_student(self):
        roll = input("Enter Roll Number to Delete: ").strip()

        if roll in self.students:
            del self.students[roll]
            self.save_data()
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    def menu(self):
        while True:
            print("\n================================")
            print("    ATTENDANCE MANAGEMENT SYSTEM")
            print("================================")
            print("1. Add Student")
            print("2. View Students")
            print("3. Mark Attendance")
            print("4. View Attendance")
            print("5. Attendance Report")
            print("6. Search Student")
            print("7. Delete Student")
            print("8. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.mark_attendance()
            elif choice == "4":
                self.view_attendance()
            elif choice == "5":
                self.attendance_report()
            elif choice == "6":
                self.search_student()
            elif choice == "7":
                self.delete_student()
            elif choice == "8":
                print("Thank you for using the system!")
                break
            else:
                print("Invalid choice! Try again.")


if __name__ == "__main__":
    system = AttendanceManagement()
    system.menu()