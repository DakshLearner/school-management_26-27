import csv

Basic_Interface = """\n\n =====================================
    STUDENT MANAGEMENT SYSTEM
=====================================
    1. Add Student
    2. View Student
    3. Search Student
    4. Check Class List
    5. Update Student
    6. Delete Student
    7. Exit
=====================================
"""

Add_student = """\n=====================================
    ADD STUDENT TO DATABASE
====================================="""

View_student = """\n=====================================
    VIEW STUDENT BY ROLL NO
====================================="""

Search_student = """\n=====================================
    SEARCH STUDENT BY NAME
====================================="""

Class_List = """\n=====================================
    CHECK CLASS LIST
====================================="""

Update_student = """\n=====================================
    UPDATE STUDENT DETAILS
====================================="""

Delete_student = """\n=====================================
    DELETE STUDENT FROM DATABASE
====================================="""

def student_management(csv_path:str):
    def generate_roll_no() -> int:
        with open(csv_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            last_roll_no = int(list(reader)[-1][0])
            return last_roll_no + 1

    def add_student(roll_no: int, name:str, Class:int, section:str, number:int):
        with open(csv_path, 'a', newline='') as csv_file1:
            writer = csv.writer(csv_file1)
            writer.writerow([roll_no, name, Class, section, number])

            print("Successfully Added Student to Database!!")


    def view_student(roll_no:int):
        with open(csv_path, 'r') as csv_file2:
            reader2 = csv.reader(csv_file2)
            retrieved = None
            reader_list = list(reader2)
            columns = reader_list[0]
            columns[0] = 'Roll No'

            for row in reader_list:
                if row and row[0] == str(roll_no):
                    retrieved = list(row)
                    break

            if retrieved:
                dictionary = {}

                for i in range(len(columns)):
                    dictionary[columns[i]] = retrieved[i]

                print("Found Record:", dictionary, end="\n\t")
            else:
                print("No Records Found!")

    def class_list(Class:int, section:str):
        with open(csv_path, 'r') as csv_file2:
            reader2 = csv.reader(csv_file2)
            retrieved = []
            reader_list = list(reader2)
            columns = reader_list[0]
            columns[0] = 'Roll No'  # Random Characters Error

            for row in reader_list:
                if row and row[2] == str(Class) and row[3] == section:
                    retrieved.append(int(list(row)[0]))

            print(f"Found Records({len(retrieved)}):\n\t", end='')
            dictionary = {}
            for x in retrieved:
                for i in range(len(columns)):
                    dictionary[columns[i]] = reader_list[x][i]

                print(dictionary, end="\n\t")


    def search_student(name:str):
        with open(csv_path, 'r') as csv_file2:
            reader2 = csv.reader(csv_file2)
            retrieved = []
            reader_list = list(reader2)
            columns = reader_list[0]
            columns[0] = 'Roll No'  # Random Characters Error

            for row in reader_list:
                if row and row[1] == str(name):
                    retrieved.append(int(list(row)[0]))

            print(f"Found Records({len(retrieved)}):\n\t", end='')
            dictionary = {}
            for x in retrieved:
                for i in range(len(columns)):
                    dictionary[columns[i]] = reader_list[x][i]

                print(dictionary, end="\n\t")

    def update_student(roll_no:int, name:str, Class:int, section:str, number:int):
        with open(csv_path, 'r') as csv_file2:
            reader2 = csv.reader(csv_file2)
            reader_list = list(reader2)
            retrieved_row = None
            new_row = [str(roll_no), name, str(Class), section, str(number)]

            for i in range(len(reader_list)):
                if reader_list[i][0] == str(roll_no):
                    retrieved_row = i

            if retrieved_row:
                print('\nUpdating:', reader_list[retrieved_row], 'To:', new_row)
                for i in range(len(new_row)):
                    if new_row[i]: reader_list[retrieved_row][i] = new_row[i]

                print("Successfully Updated Student to Database!!")
            else:
                print("No Records Found! (Check Roll Number)")
                return

        with open(csv_path, 'w', newline='') as csv_file3:
            writer2 = csv.writer(csv_file3)
            writer2.writerows(reader_list)

    def delete_student(roll_no:int):
        with open(csv_path, 'r') as csv_file2:
            reader2 = csv.reader(csv_file2)
            reader_list = list(reader2)
            retrieved_row = None

            for i in range(len(reader_list)):
                if reader_list[i][0] == str(roll_no):
                    retrieved_row = i

            if retrieved_row:
                print(f"Deleting Record: {reader_list[retrieved_row]}...")
                del reader_list[retrieved_row]

                print("Successfully Deleted Student from Database!!")
            else:
                print("No Record Found! (Check Roll Number)")

        with open(csv_path, 'w', newline='') as csv_file3:
            writer2 = csv.writer(csv_file3)
            writer2.writerows(reader_list)

    run = True

    while run:
        print(Basic_Interface)
        choice = input("Enter your choice: ")

        if choice == "1":
            print(Add_student)
            name = input("Enter Student Name: ")
            Class = int(input("Enter Class: "))
            section = input("Enter Section: ")
            number = int(input("Enter Parent's Number: "))
            roll_no = generate_roll_no()

            add_student(roll_no, name, Class, section, number)
            view_student(roll_no)
            Continue = input("Press Enter key to continue...")

        elif choice == "2":
            print(View_student)
            roll_no = int(input("Enter Student Roll No: "))
            view_student(roll_no)
            Continue = input("Press Enter key to continue...")

        elif choice == "3":
            print(Search_student)
            name = input("Enter Student Name: ")
            search_student(name)
            Continue = input("Press Enter key to continue...")

        elif choice == "4":
            print(Class_List)
            Class = int(input("Enter Class: "))
            section = input("Enter Section: ")

            class_list(Class, section)
            Continue = input("Press Enter key to continue...")

        elif choice == "5":
            print(Update_student)

            roll_no = int(input("Enter Student Roll No: "))
            name = input("Enter Student Name: ")
            Class = int(input("Enter Class: "))
            section = input("Enter Section: ")
            number = int(input("Enter Parent's Number: "))

            update_student(roll_no, name, Class, section, number)
            Continue = input("\nPress Enter key to continue...")

        elif choice == "6":
            print(Delete_student)

            roll_no = int(input("Enter Student Roll No: "))

            delete_student(roll_no)
            Continue = input("\nPress Enter key to continue...")

        elif choice == "7":
            run = False
            print("Thank you for using this program!")
            Continue = input("Press Enter key to continue...")
            continue
        
        else:
            print("Invalid Choice!!")
            Continue = input("Press Enter key to continue...")

student_management("..\\Spreadsheets\\Students.csv")
