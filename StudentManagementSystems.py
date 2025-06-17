class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name 
        self.age = age 
        self.grade = grade

    def update_info(self, name=None, age=None, grade=None):
        if name:
            self.name= name 
        if age:
            self.age = age
        if grade:
            self.grade = grade
    
    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return True
        return False
    
    def get_all_students(self):
        return self.students
    
    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def find_student_by_name(self, name):
        return [s for s in self.students if s.name.lower() == name.lower()]


def main():
    manage = StudentManager()

    while True:
        print("\n --------- Student Managent System --------")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. View All Students")
        print("4. Search by ID")
        print("5. Search by Name")
        print("6. Update Student Info")
        print("7. Exit") 

        choice = input("Enter your Choice (1-7): ")

        if choice == '1':
            sid = input("Enter Student ID: ")
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            grade = input("Enter grade: ")
            student = Student(sid, name, age, grade)
            manage.add_student(student)
            print("Student added successfully!")

        elif choice == '2':
            sid = input("Enter student ID to remove: ")
            if manage.remove_student(sid):
                print("Student removed. ")

        elif choice == '3':
            students = manage.get_all_students()
            if students:
                for s in students:
                    print(s)

            else:
                print("No Students in the system.")

        elif choice == '4':
            sid = input("Enter student ID to search: ")
            student = manage.find_student_by_id(sid)
            print(student if student else "Student not found. ")

        elif choice == '5':
            name = input("Enter Name to search:")
            students = manage.find_student_by_id(name)
            if students:
                for s in students:
                    print(s)

            else:
                print("No matching students found. ")

        elif choice == '6':
            sid = input(("ENter Student ID to upadate: "))
            student = manage.find_student_by_id(sid)
            if student:
                name = input("New name (leave blank to kepp same): ")
                age = input("New age (leave blank to keep same): ")
                grade = input("New grade (leave blank to keep same): ")

                student.update_info(
                    nama=name if name else None,
                    age=int(age) if age else None,
                    grade=grade if grade else None
                )
                print("Student info updated.")

            else:
                print("Student not found. ")

        elif choice == '7':
            print("Exiting... Goodbye!")
            break 

        else: 
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

