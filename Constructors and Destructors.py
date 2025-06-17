# class Logger:
#     def __init__(self, value):
#         self.value = value
#         print(f"Objects Created {self.value}")

#     def __del__(self):
#         print(f"Object destroyed {self.value}")

# val = input("Enter Object:")
# a = Logger(val)
# del val


class Logger:
    def __init__(self, value):
        self.value = value
        print(f"Object created successfully: {self.value}")

    def __del__(self):
        print(f"Object Destroyed: {self.value}")

val = input("Enter Object: ")
a = Logger(val)
del val

