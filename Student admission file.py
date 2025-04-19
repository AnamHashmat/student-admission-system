class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Course: {self.course}")


class CollegeAdmissionSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, name, age, course):
        student = Student(student_id, name, age, course)
        self.students.append(student)
        print(f"Student {name} added successfully!")

    def view_students(self):
        if not self.students:
            print("No students have been admitted yet.")
        else:
            print("List of admitted students:")
            for student in self.students:
                student.display_info()

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print("Student found:")
                student.display_info()
                return
        print("Student not found.")

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"Student {student.name} removed successfully!")
                return
        print("Student not found.")


# Example usage
if __name__ == "__main__":
    system = CollegeAdmissionSystem()

    while True:
        print("\nCollege Admission System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Remove Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            course = input("Enter Course: ")
            system.add_student(student_id, name, age, course)
        elif choice == "2":
            system.view_students()
        elif choice == "3":
            student_id = input("Enter Student ID to search: ")
            system.search_student(student_id)
        elif choice == "4":
            student_id = input("Enter Student ID to remove: ")
            system.remove_student(student_id)
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")