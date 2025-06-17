class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    def sub(a, b):
        return a - b
    
    def mul(a, b):
        return a * b
    
    def div(a, b):
        return a / b

print("Please select operation -\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")

sel = int(input("Select operation (1-4): "))

n1 = int(input("Enter sum 1:"))
n2 = int(input("Enter sum 2: "))
 

if sel == 1:
    print(n1, "+", n2, "=", MathUtils.add(n1, n2))
elif sel == 2:
    print(n1, "-", n2, "=", MathUtils.sub(n1, n2))
elif sel == 3:
    print(n1, "*", n2, "=", MathUtils.mul(n1, n2))
elif sel == 4:
    print(n1, "/", n2, "=", MathUtils.div(n1, n2))
else:
    print("Invalid input")
