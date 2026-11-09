import csv
import os
from datetime import datetime

'''
o        Mark attendance (class wise)
o        View student attendance
o        View class attendance by date
o        Attendance percentage
o        Update attendance
'''

Basic_Interface = """\n\n =====================================
    ATTENDANCE MANAGEMENT SYSTEM
=====================================
    1. Mark Attendance
    2. View Student Attendance
    3. View Class Attendance
    4. Attendance Percentage
    5. Update Attendance
    6. Exit
=====================================
"""

Mark_attendance = """\n=====================================
    MARK CLASS ATTENDANCE
    (P = Present, A = Absent, L = Leave)
====================================="""

View_student_attendance = """\n=====================================
    VIEW STUDENT ATTENDANCE BY ROLL NO
====================================="""

View_class_attendance = """\n=====================================
    VIEW CLASS ATTENDANCE BY DATE
====================================="""

Attendance_percentage = """\n=====================================
    CHECK ATTENDANCE PERCENTAGE
====================================="""

Update_attendance = """\n=====================================
    UPDATE ATTENDANCE
====================================="""

HEADER = ['Date', 'Roll No', 'Name', 'Class', 'Section', 'Status']
STATUS = {'P': 'Present', 'A': 'Absent', 'L': 'Leave'}
DATE_FORMAT = '%d-%m-%Y'
MIN_PERCENTAGE = 75


def create_file_if_missing(csv_path: str):
    # Pehli baar run hone par Attendance.csv header ke saath ban jayegi
    if not os.path.exists(csv_path) or os.path.getsize(csv_path) == 0:
        with open(csv_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(HEADER)


def read_rows(csv_path: str) -> list:
    # utf-8-sig: Excel wali CSV ke starting ke random characters hata deta hai
    with open(csv_path, 'r', newline='', encoding='utf-8-sig') as csv_file:
        return [row for row in csv.reader(csv_file) if row]


def get_date(prompt: str = "Enter Date (DD-MM-YYYY) or press Enter for today: ") -> str:
    while True:
        value = input(prompt).strip()
        if value == "":
            return datetime.today().strftime(DATE_FORMAT)
        try:
            return datetime.strptime(value, DATE_FORMAT).strftime(DATE_FORMAT)
        except ValueError:
            print("Invalid Date! Use DD-MM-YYYY format.")


def get_student(students_csv: str, roll_no: int):
    for row in read_rows(students_csv)[1:]:
        if row[0] == str(roll_no):
            return row
    return None


def get_class_students(students_csv: str, Class: int, section: str) -> list:
    students = []
    for row in read_rows(students_csv)[1:]:
        if row[2] == str(Class) and row[3] == section:
            students.append(row)
    return students


def mark_attendance(attendance_csv: str, students_csv: str, Class: int, section: str, date: str):
    students = get_class_students(students_csv, Class, section)

    if not students:
        print("No Students Found in this Class! (Check Class and Section)")
        return

    rows = read_rows(attendance_csv)
    already_marked = set()
    for row in rows[1:]:
        if row[0] == date and row[3] == str(Class) and row[4] == section:
            already_marked.add(row[1])

    new_records = []
    print(f"\nMarking Attendance for Class {Class} {section} on {date}\n")

    for student in students:
        roll_no, name = student[0], student[1]

        if roll_no in already_marked:
            print(f"{roll_no} - {name}: Already Marked, Skipping...")
            continue

        status = input(f"{roll_no} - {name} (P/A/L): ").strip().upper()
        while status not in STATUS:
            print("Invalid Input! Enter P, A or L.")
            status = input(f"{roll_no} - {name} (P/A/L): ").strip().upper()

        new_records.append([date, roll_no, name, Class, section, status])

    if not new_records:
        print("Attendance was already marked for the whole class on this date!")
        return

    with open(attendance_csv, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(new_records)

    present = sum(1 for r in new_records if r[5] == 'P')
    absent = sum(1 for r in new_records if r[5] == 'A')
    leave = sum(1 for r in new_records if r[5] == 'L')

    print("Successfully Marked Attendance!!")
    print(f"Present: {present}, Absent: {absent}, Leave: {leave}")


def view_student_attendance(attendance_csv: str, roll_no: int):
    rows = read_rows(attendance_csv)
    columns = rows[0]
    retrieved = [row for row in rows[1:] if row[1] == str(roll_no)]

    if not retrieved:
        print("No Records Found!")
        return

    print(f"Found Records({len(retrieved)}):\n\t", end='')
    for row in retrieved:
        dictionary = {}
        for i in range(len(columns)):
            dictionary[columns[i]] = row[i]
        dictionary['Status'] = STATUS.get(row[5], row[5])

        print(dictionary, end="\n\t")


def view_class_attendance(attendance_csv: str, Class: int, section: str, date: str):
    rows = read_rows(attendance_csv)
    columns = rows[0]
    retrieved = [row for row in rows[1:]
                 if row[0] == date and row[3] == str(Class) and row[4] == section]

    if not retrieved:
        print("No Records Found! (Check Class, Section and Date)")
        return

    print(f"Attendance of Class {Class} {section} on {date} ({len(retrieved)}):\n\t", end='')
    for row in retrieved:
        dictionary = {}
        for i in range(len(columns)):
            dictionary[columns[i]] = row[i]
        dictionary['Status'] = STATUS.get(row[5], row[5])

        print(dictionary, end="\n\t")


def attendance_percentage(attendance_csv: str, roll_no: int):
    rows = read_rows(attendance_csv)
    retrieved = [row for row in rows[1:] if row[1] == str(roll_no)]

    if not retrieved:
        print("No Records Found!")
        return

    total = len(retrieved)
    present = sum(1 for row in retrieved if row[5] == 'P')
    absent = sum(1 for row in retrieved if row[5] == 'A')
    leave = sum(1 for row in retrieved if row[5] == 'L')
    percentage = round(present / total * 100, 2)

    print(f"Student: {retrieved[0][2]} (Roll No {roll_no})")
    print(f"Total Days: {total}, Present: {present}, Absent: {absent}, Leave: {leave}")
    print(f"Attendance Percentage: {percentage}%")

    if percentage < MIN_PERCENTAGE:
        print(f"Warning: Attendance is below {MIN_PERCENTAGE}%!")


def update_attendance(attendance_csv: str, roll_no: int, date: str, status: str):
    rows = read_rows(attendance_csv)
    retrieved_row = None

    for i in range(1, len(rows)):
        if rows[i][0] == date and rows[i][1] == str(roll_no):
            retrieved_row = i

    if retrieved_row is None:
        print("No Record Found! (Check Roll Number and Date)")
        return

    print('\nUpdating:', rows[retrieved_row], 'To Status:', STATUS[status])
    rows[retrieved_row][5] = status

    with open(attendance_csv, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(rows)

    print("Successfully Updated Attendance!!")


def attendance_management(attendance_csv: str, students_csv: str):
    create_file_if_missing(attendance_csv)

    run = True

    while run:
        print(Basic_Interface)
        choice = input("Enter your choice: ")

        if choice == "1":
            print(Mark_attendance)
            Class = int(input("Enter Class: "))
            section = input("Enter Section: ")
            date = get_date()

            mark_attendance(attendance_csv, students_csv, Class, section, date)
            Continue = input("\nPress Enter key to continue...")

        elif choice == "2":
            print(View_student_attendance)
            roll_no = int(input("Enter Student Roll No: "))

            view_student_attendance(attendance_csv, roll_no)
            Continue = input("\nPress Enter key to continue...")

        elif choice == "3":
            print(View_class_attendance)
            Class = int(input("Enter Class: "))
            section = input("Enter Section: ")
            date = get_date()

            view_class_attendance(attendance_csv, Class, section, date)
            Continue = input("\nPress Enter key to continue...")

        elif choice == "4":
            print(Attendance_percentage)
            roll_no = int(input("Enter Student Roll No: "))

            attendance_percentage(attendance_csv, roll_no)
            Continue = input("\nPress Enter key to continue...")

        elif choice == "5":
            print(Update_attendance)
            roll_no = int(input("Enter Student Roll No: "))
            date = get_date("Enter Date to Update (DD-MM-YYYY): ")
            status = input("Enter New Status (P/A/L): ").strip().upper()

            if status not in STATUS:
                print("Invalid Status! Enter P, A or L.")
            else:
                update_attendance(attendance_csv, roll_no, date, status)
            Continue = input("\nPress Enter key to continue...")

        elif choice == "6":
            run = False
            print("Thank you for using this program!")
            Continue = input("Press Enter key to continue...")
            continue

        else:
            print("Invalid Choice!!")
            Continue = input("Press Enter key to continue...")


if __name__ == "__main__":
    attendance_management("..\\Spreadsheets\\Attendance.csv", "..\\Spreadsheets\\Students.csv")
