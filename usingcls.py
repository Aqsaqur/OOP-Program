# class Counter:
#     objects = 0

#     def __init__(self):
#         Counter.objects += 1

#     @classmethod
#     def display(cls):
#         print(f"The total objects: {cls.objects}")

# c1 = Counter()
# c2 = Counter()
# c3 = Counter()

# Counter.display()

# class Counter:
#     objects = 0

#     def __init__(self, name):
#         self.name = name
#         Counter.objects += 1

#     @classmethod 
#     def display(cls):
#         print(f"The Total objects: {cls.objects}")

# c1 = Counter(input("Enter Object: "))
# c2 = Counter(input("Enter Object: "))
# c3 = Counter(input("Enter Object: "))

# Counter.display()


# class Counter:
#     objects = 0

#     def __init__(self, name):
#         self.name = name
#         Counter.objects += 1

#     @classmethod
#     def display(cls):
#         print(f"the total object: {cls.objects}")

# c1 = Counter(input("Enter Object:"))
# c2 = Counter(input("Enter Object:"))
# c3 = Counter(input("Enter Object:"))

# Counter.display()



class Counter:
    object = 0

    def __init__(self, random):
        Counter.object += 1
        self.random = random
        self.totalobjects = Counter.object

    def __str__(self):
        return f"Counter Objects {self.totalobjects}: {self.random}"
    
    @classmethod
    def Display(cls):
        print(f"The total objects are {cls.object}")

c1 = Counter(input("Enter: "))
c2 = Counter(input("Enter:"))
c3 = Counter(input("Enter:"))


Counter.Display()
print(c1)
print(c2)
print(c3)
