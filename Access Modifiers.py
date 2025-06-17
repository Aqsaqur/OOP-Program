class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

public_name = input("Enter your Name: ")
salary_priv = input("Enter Your Salary: ")
ssn_name = input("Enter Your SSN: ")

emp = Employee(public_name, salary_priv, ssn_name)

print("Public Name:", emp.name)
print("Protected Salary:", emp._salary)

try:
    print("Private SSN:", emp.__ssn)       #  Will raise AttributeError
except AttributeError:
    print(" Cannot access __ssn directly! It’s private.")

# Accessing private variable using name mangling
print("Accessing Private SSN (via name mangling):", emp._Employee__ssn)
