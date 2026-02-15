# ==============================
#   STUDENT MANAGEMENT SYSTEM
# ==============================

students = []

def add_student():
    print("\n--- Add New Student ---")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    grade = input("Enter Grade: ")

    student = {
        "Name": name,
        "Age": age,
        "Grade": grade
    }

    students.append(student)
    print("✅ Student added successfully!\n")


def view_students():
    print("\n--- Student List ---")
    if not students:
        print("No students found.\n")
        return

    for index, student in enumerate(students, start=1):
        print(f"\nStudent {index}")
        print("-" * 20)
        for key, value in student.items():
            print(f"{key}: {value}")
    print()


def delete_student():
    view_students()
    if not students:
        return

    try:
        num = int(input("Enter student number to delete: "))
        if 1 <= num <= len(students):
            removed = students.pop(num - 1)
            print(f"❌ Removed {removed['Name']} successfully!\n")
        else:
            print("Invalid number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def main():
    while True:
        print("=" * 35)
        print("   STUDENT MANAGEMENT SYSTEM")
        print("=" * 35)
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
