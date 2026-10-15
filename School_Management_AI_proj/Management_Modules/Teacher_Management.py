import csv

'''
o	Add teacher
o	View teacher details
o	Search teacher
'''
Basic_Interface = """\n\n =====================================
    TEACHER MANAGEMENT SYSTEM
=====================================
    1. Add Teacher
    2. View Teacher
    3. Search Teacher
    4. Find Class Teacher
    5. Exit
=====================================
"""

Add_teacher = """\n=====================================
    ADD TEACHER TO DATABASE
====================================="""

View_teacher = """\n=====================================
    VIEW TEACHER BY ID NO
====================================="""

Search_teacher = """\n=====================================
    SEARCH TEACHER BY NAME
====================================="""

Find_Class_teacher = """\n=====================================
    SEARCH TEACHER BY NAME
====================================="""



def teacher_management(csv_path:str):
    def generate_id_no() -> int:
        with open(csv_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            last_id_no = int(list(reader)[-1][0])
            return last_id_no + 1

    def add_teacher(id_num:int, name:str, Class:int, section:str, number:int):
        with open(csv_path, 'a', newline='') as csv_file1:
            writer = csv.writer(csv_file1)

            writer.writerow([id_num, name, Class, section, number])
            print("Successfully Added Teacher to Database!!")

    def view_teacher(id_no:int):
        with open(csv_path, 'r') as csv_file2:
            reader2 = csv.reader(csv_file2)
            retrieved = None
            reader_list = list(reader2)
            columns = reader_list[0]
            columns[0] = 'Roll No'

            for row in reader_list:
                if row and row[0] == str(id_no):
                    retrieved = list(row)
                    break

            if retrieved:
                dictionary = {}

                for i in range(len(columns)):
                    dictionary[columns[i]] = retrieved[i]

                print("Found Record:", dictionary, end="\n\t")
            else:
                print("No Records Found!")

    def search_teacher(name:str):
        with open(csv_path, 'r') as csv_file2:
            reader2 = csv.reader(csv_file2)
            retrieved = []
            reader_list = list(reader2)
            columns = reader_list[0]
            columns[0] = 'Id Number' # Random Characters Error

            for row in reader_list:
                if row and row[1] == str(name):
                    retrieved.append(int(list(row)[0]))

            print(f"Found Records({len(retrieved)}):\n\t", end='')
            dictionary = {}
            for x in retrieved:
                for i in range(len(columns)):
                    dictionary[columns[i]] = reader_list[x][i]

                print(dictionary, end="\n\t")

    def view_class_teacher(Class:int, section:str):
        with open(csv_path, 'r') as csv_file3:
            reader3 = csv.reader(csv_file3)
            retrieved = []
            reader_list = list(reader3)
            columns = reader_list[0]
            columns[0] = 'Id Number'

            for row in reader_list:
                if row and row[2] == str(Class) and row[3] == section:
                    retrieved.append(int(list(row)[0]))

            print(f"Retrieved Teacher of {Class} {section}:\n\t", end='')
            dictionary = {}
            for x in retrieved:
                for i in range(len(columns)):
                    dictionary[columns[i]] = reader_list[x][i]

                print(dictionary, end="\n\t")

    run = True

    while run:
        print(Basic_Interface)
        choice = input("Enter your choice: ")

        if choice == "1":
            print(Add_teacher)
            name = input("Enter Teacher Name: ")
            Class = int(input("Enter Assigned Class: "))
            section = input("Enter Assigned Section: ")
            number = int(input("Enter Teacher's Number: "))
            id_no = generate_id_no()

            add_teacher(id_no, name, Class, section, number)
            view_teacher(id_no)
            Continue = input("Press Enter key to continue...")

        elif choice == "2":
            print(View_teacher)
            roll_no = int(input("Enter Teacher ID No: "))
            view_teacher(roll_no)
            Continue = input("Press Enter key to continue...")

        elif choice == "3":
            print(Search_teacher)
            name = input("Enter Teacher Name: ")
            search_teacher(name)
            Continue = input("Press Enter key to continue...")

        elif choice == "4":
            print(Find_Class_teacher)
            Class = int(input("Enter Class: "))
            section = input("Enter Section: ")

            view_class_teacher(Class, section)
            Continue = input("Press Enter key to continue...")
        
        elif choice == "5":
            run = False
            print("Thank you for using this program!")
            Continue = input("Press Enter key to continue...")
            continue
        else:
            print("Invalid Command!")
            Continue = input("Press Enter key to continue...")

teacher_management("..\\Spreadsheets\\Teachers.csv")
