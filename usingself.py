# # class Student:
# #     def __init__(self, name, marks):
# #         self.name = name
# #         self.marks = marks

# #     def Display(self):
# #         print(f"The name of the student is {self.name}, the marks are {self.marks}")


# # St = input("Enter the name: ")
# # mk = input("Enter the marks: ")

# # student = Student(St, mk)
# # student.Display()

# class Student:
#     def __init__(self, name, mark, rollnumber):
#         self.name = name
#         self.mark = float(mark)
#         self.rollnumber = int(rollnumber)

#     def display(self):
#         print(f"The Name of the Student {self.name}, The Total Marks of the Student {self.mark}, and The Roll. no is {self.rollnumber}")

# student_lists = []

# for i in range(2):
#     print(f"\n Enter details for student {i + 1}:")
#     s_n = input("Enter the Name: ")
#     m_k = float(input("Enter The Marks: "))
#     roll = int(input("Enter the Roll Number: "))
#     student = Student(s_n, m_k, roll)
#     student_lists.append(student)


# print("\n --- Students Information ---")
# for student in student_lists:
#     student.display()

# class Student: 
#     def __init__(self, marks, name, rollnum):
#         self.name = name
#         self.marks = float(marks)
#         self.rollnum = int(rollnum)

#     def Display(self):
#         print(f"The name of the student {self.name}, The total marks {self.marks}, and the roll num {self.rollnumi}")

# student_list = []

# for i in range(2):
#     print(f"/n Enter details for student {i + 1}")
#     s_n = input("Enter The Name: ")
#     m_k = float(input("Enter Marks: "))
#     roll = int(input("Enter Roll no. :"))
#     student = Student(s_n, m_k, roll)
#     student_list.append(student)

# print("\n --- Students Information ---")
# for student in student_list:
#     student.display()



class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"The Name of The Student Is: {self.name}, And the Total marks {self.marks}")

std_name = input("Enter student Name: ")
mk = input("Enter the Marks of student: ")

info = Student(std_name, mk)
info.display()

