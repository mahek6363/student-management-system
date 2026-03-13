students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    students[roll] = {
        "name": name,
        "age": age,
        "course": course
    }

    print("✅ Student added successfully\n")


def view_students():
    if not students:
        print("No students found\n")
        return

    print("\n📋 Student List")
    for roll, info in students.items():
        print(f"Roll: {roll} | Name: {info['name']} | Age: {info['age']} | Course: {info['course']}")
    print()


def search_student():
    roll = input("Enter Roll Number to search: ")

    if roll in students:
        info = students[roll]
        print(f"Name: {info['name']}")
        print(f"Age: {info['age']}")
        print(f"Course: {info['course']}\n")
    else:
        print("❌ Student not found\n")


def update_student():
    roll = input("Enter Roll Number to update: ")

    if roll in students:
        name = input("Enter new name: ")
        age = input("Enter new age: ")
        course = input("Enter new course: ")

        students[roll] = {
            "name": name,
            "age": age,
            "course": course
        }

        print("✅ Student updated\n")
    else:
        print("❌ Student not found\n")


def delete_student():
    roll = input("Enter Roll Number to delete: ")

    if roll in students:
        del students[roll]
        print("✅ Student deleted\n")
    else:
        print("❌ Student not found\n")


def menu():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice\n")


menu()