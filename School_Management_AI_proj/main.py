# ==========================================================
# SCHOOL MANAGEMENT SYSTEM (Class 11 Project Level)
# ==========================================================

# Importing the module files from the Management_Modules folder
from Management_Modules import Student_Management
from Management_Modules import Teacher_Management
from Management_Modules import Attendance_Management

def main():
    while True:
        # Displaying the main menu
        print("\n" + "=" * 40)
        print("     SCHOOL MANAGEMENT SYSTEM")
        print("=" * 40)
        print("1. Student Management")
        print("2. Teacher Management")
        print("3. Attendance Management")
        print("4. Exit")
        print("=" * 40)
        
        # Taking user choice
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            print("\n--- Opening Student Management ---")
            # Assuming your student module has a function named 'menu' or 'main'
            Student_Management.main()
            
        elif choice == '2':
            print("\n--- Opening Teacher Management ---")
            # Assuming your teacher module has a function named 'main'
            Teacher_Management.main()
            
        elif choice == '3':
            print("\n--- Opening Attendance Management ---")
            # Assuming your attendance module has a function named 'main'
            Attendance_Management.main()
            
        elif choice == '4':
            print("\nThank you for using the system. Exiting...")
            break  # Exits the while loop and ends the program
            
        else:
            print("\nInvalid Choice! Please enter a number between 1 and 4.")

# Program execution starts here
if __name__ == "__main__":
    main()
